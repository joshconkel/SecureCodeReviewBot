"""
scan.py  –  Agentic security code scanner using LMStudio + agents.yaml
===========================================================================
Rewrites the previous run_scan_file.py from scratch.

Key differences from the previous version:
  - Uses plain chat completions (NO response_format / json_schema mode).
    Local models on LMStudio do not reliably honour json_schema structured
    output. Plain completions with explicit JSON instructions are more stable.
  - JSON extraction is aggressive: strips fences, finds the largest {...} block,
    repairs common issues, and falls back gracefully without crashing.
  - Token budgets are generous and never capped below safe minimums.
  - Each agent stage writes its raw output and parsed result to disk so you
    can inspect exactly what the model produced at every step.
  - Schemas are used for DISPLAY / logging only — not for validation that
    crashes the pipeline. A partial result is better than no result.

Requirements:
    pip install openai pyyaml rich

LMStudio setup:
    1. Start the Local Server (default: http://localhost:1234)
    2. Load any model (tested with Qwen3-Coder-30B, DeepSeek-Coder)
    3. In Server Settings set:
         Context Length        >= 8192
         Max Generated Tokens  = -1  (unlimited)  or >= 4096

Usage:
    python scan.py "C:\\AI\\WebGoat.NET\\WebGoat\\App_Code"
    python scan.py /path/to/code --config agents.yaml --out results --max-files 10
    python scan.py /path/to/code --file src/auth.py
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Any

import yaml
from openai import OpenAI
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Extensions to scan (supplemented by agents.yaml include_extensions)
DEFAULT_EXTENSIONS = {
    ".cs", ".py", ".rb", ".js", ".ts", ".java", ".go", ".php",
    ".json", ".yml", ".yaml", ".config", ".xml", ".env",
    ".csproj", ".toml",
}

# Directories to always skip
SKIP_DIRS = {
    ".git", ".svn", ".hg", "node_modules", "vendor", "bower_components",
    "bin", "obj", "dist", "build", "out", "target", ".venv", "venv",
    "__pycache__", ".pytest_cache", ".mypy_cache", ".tox", "coverage",
    ".next", ".nuxt", "Migrations", "migrations",
}

# Per-agent token minimums. The model will never be called with less than this.
AGENT_MIN_TOKENS = {
    "scope":       2500,
    "threat":      2500,
    "hypotheses":  3000,
    "evidence":    3500,
    "fix":         3000,
    "gate":        2000,
}

# How many times to retry a single agent call on failure
DEFAULT_RETRIES = 2

# ---------------------------------------------------------------------------
# JSON extraction helpers
# ---------------------------------------------------------------------------

def strip_fences(text: str) -> str:
    """Remove markdown code fences."""
    text = (text or "").strip()
    text = re.sub(r"^```[a-zA-Z]*\s*", "", text)
    text = re.sub(r"\s*```\s*$", "", text)
    return text.strip()


def fix_control_chars(text: str) -> str:
    """Escape raw control characters that break json.loads."""
    out = []
    for ch in text:
        o = ord(ch)
        if o < 0x20:
            if   ch == "\n": out.append("\\n")
            elif ch == "\t": out.append("\\t")
            elif ch == "\r": out.append("\\r")
            elif ch == "\b": out.append("\\b")
            elif ch == "\f": out.append("\\f")
            else:            out.append(f"\\u{o:04x}")
        else:
            out.append(ch)
    return "".join(out)


def repair_json(text: str) -> str:
    """Conservative JSON repairs: smart quotes, unquoted keys, trailing commas."""
    # Smart quotes
    text = text.replace("\u201c", '"').replace("\u201d", '"')
    text = text.replace("\u2018", "'").replace("\u2019", "'")
    # Null bytes
    text = text.replace("\x00", "")
    # Strip // comments
    text = re.sub(r"//[^\n]*", "", text)
    # Quote unquoted object keys:  { key: → { "key":
    text = re.sub(r'([{\[,]\s*)([A-Za-z_][A-Za-z0-9_]*)\s*:', r'\1"\2":', text)
    # Trailing commas before } or ]
    text = re.sub(r",\s*([}\]])", r"\1", text)
    return text.strip()


def extract_json(raw: str) -> dict:
    """
    Try every strategy to extract a JSON object from model output.
    Returns the parsed dict, or raises ValueError with a clear message.
    """
    if not raw or not raw.strip():
        raise ValueError("Empty response from model")

    candidates = []

    # Strategy 1: strip fences, try direct parse
    cleaned = strip_fences(raw)
    candidates.append(cleaned)

    # Strategy 2: find the outermost { ... } block
    start = raw.find("{")
    if start != -1:
        depth = 0
        for i in range(start, len(raw)):
            if raw[i] == "{":
                depth += 1
            elif raw[i] == "}":
                depth -= 1
                if depth == 0:
                    candidates.append(raw[start:i+1])
                    break

    # Strategy 3: find ALL {...} blocks, take the largest
    all_blocks = []
    for m in re.finditer(r"\{", raw):
        s = m.start()
        depth = 0
        for i in range(s, len(raw)):
            if raw[i] == "{": depth += 1
            elif raw[i] == "}":
                depth -= 1
                if depth == 0:
                    all_blocks.append(raw[s:i+1])
                    break
    if all_blocks:
        candidates.append(max(all_blocks, key=len))

    # Try each candidate with and without repairs
    for cand in candidates:
        for transform in [lambda x: x, fix_control_chars, repair_json,
                          lambda x: fix_control_chars(repair_json(x))]:
            try:
                result = json.loads(transform(cand))
                if isinstance(result, dict):
                    return result
            except Exception:
                continue

    # Last resort: try to parse the whole raw output
    try:
        return json.loads(fix_control_chars(repair_json(raw)))
    except Exception:
        pass

    raise ValueError(
        f"Could not extract valid JSON from model output. "
        f"First 300 chars: {raw[:300]!r}"
    )


# ---------------------------------------------------------------------------
# LMStudio client
# ---------------------------------------------------------------------------

def make_client(cfg: dict) -> OpenAI:
    # Default timeout is generous — local models can be slow on large files.
    # Set per_request_timeout in agents.yaml llm section to override.
    # Use httpx.Timeout for granular control: connect fast, read slow.
    import httpx
    req_timeout = float(cfg["llm"].get("per_request_timeout", 300))  # 5 min default
    timeout = httpx.Timeout(
        connect=10.0,       # fail fast if LMStudio isn't running
        read=req_timeout,   # generation can be slow on large files
        write=30.0,
        pool=10.0,
    )
    return OpenAI(
        base_url=cfg["llm"]["base_url"],
        api_key=cfg["llm"].get("api_key", "lm-studio"),
        timeout=timeout,
    )


def get_model(client: OpenAI, preferred: str | None) -> str:
    if preferred:
        return preferred
    models = client.models.list()
    if models.data:
        return models.data[0].id
    raise RuntimeError("No models available. Is LMStudio server running?")


def call_llm(
    client: OpenAI,
    model: str,
    system: str,
    user: str,
    max_tokens: int,
    temperature: float = 0.0,
) -> tuple[str, str]:
    """
    Call the model. Returns (content, finish_reason).
    Uses plain chat completions — no json_schema mode.
    """
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user",   "content": user},
        ],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    choice = resp.choices[0]
    content = choice.message.content or ""
    finish_reason = getattr(choice, "finish_reason", "") or ""
    return content, finish_reason


def call_agent(
    client: OpenAI,
    model: str,
    agent_cfg: dict,
    user_prompt: str,
    max_tokens: int,
    retries: int = DEFAULT_RETRIES,
    label: str = "agent",
    raw_out_path: Path | None = None,
) -> dict:
    """
    Call one agent. Returns parsed JSON dict.
    On failure after retries, returns {} so the pipeline continues.
    """
    system = (
        agent_cfg.get("system", "").strip()
        + "\n\nIMPORTANT: Output ONLY a single valid JSON object. "
        "No explanation, no markdown fences, no text before or after the JSON. "
        "Start your response with { and end with }."
    )

    messages = [
        {"role": "system", "content": system},
        {"role": "user",   "content": user_prompt},
    ]

    last_raw = ""
    last_err = ""
    effective_max_tokens = max(max_tokens, AGENT_MIN_TOKENS.get(label, 2000))

    for attempt in range(retries + 1):
        t_start = time.monotonic()
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.0,
                max_tokens=effective_max_tokens,
            )
            elapsed = time.monotonic() - t_start
            choice = resp.choices[0]
            last_raw = choice.message.content or ""
            finish_reason = getattr(choice, "finish_reason", "") or ""

            if raw_out_path:
                raw_out_path.parent.mkdir(parents=True, exist_ok=True)
                raw_out_path.write_text(
                    f"finish_reason: {finish_reason}  elapsed: {elapsed:.1f}s\n---\n{last_raw}",
                    encoding="utf-8", errors="replace"
                )

            stripped = last_raw.strip()

            # Detect genuine truncation vs model wrapping output in markdown fences.
            # finish_reason="stop" + trailing ``` is a complete response, not truncated.
            # Only treat as truncated if the server hard-cut the output (finish_reason="length")
            # or if after stripping fences the content doesn't end with }.
            fence_stripped = re.sub(r"```[a-z]*\s*$", "", stripped).rstrip()
            actually_truncated = (
                finish_reason == "length"
                or (fence_stripped and not fence_stripped.endswith("}"))
            )

            if actually_truncated:
                current_floor = AGENT_MIN_TOKENS.get(label, 2000)
                raise ValueError(
                    f"Response truncated (finish_reason={finish_reason!r}, agent={label}, "
                    f"max_tokens={effective_max_tokens}). "
                    f"Increase AGENT_MIN_TOKENS['{label}'] in scan_file.py "
                    f"(currently {current_floor}) or pass a higher --max-tokens value. "
                    f"Also confirm LMStudio Server → 'Max Generated Tokens' is set to -1. "
                    f"Tail: ...{stripped[-60:]!r}"
                )

            result = extract_json(last_raw)
            return result

        except Exception as e:
            elapsed = time.monotonic() - t_start
            err_str = str(e)
            err_type = type(e).__name__

            # Classify the error so we can give a useful message and decide
            # whether retrying makes sense.
            is_timeout    = (
                "timed out" in err_str.lower()
                or "timeout"  in err_str.lower()
                or "ReadTimeout" in err_type
                or "ConnectTimeout" in err_type
            )
            is_truncation = "truncated" in err_str.lower() or "finish_reason='length'" in err_str
            is_conn_err   = (
                "connection" in err_str.lower()
                or "refused"  in err_str.lower()
                or "ConnectError" in err_type
            )

            if is_timeout:
                last_err = (
                    f"TIMEOUT after {elapsed:.0f}s on attempt {attempt+1}/{retries+1} "
                    f"(agent={label}, max_tokens={effective_max_tokens}). "
                    f"FIX: increase per_request_timeout in agents.yaml llm section "
                    f"(current default 300s). For large files try --max-chars to reduce "
                    f"context sent per call."
                )
            elif is_conn_err:
                last_err = (
                    f"CONNECTION ERROR on attempt {attempt+1}/{retries+1}: {err_str[:200]}. "
                    f"Is LMStudio server still running at the configured base_url?"
                )
            else:
                last_err = f"{err_type} on attempt {attempt+1}/{retries+1} ({elapsed:.1f}s): {err_str[:300]}"

            # Don't retry timeouts or connection errors — they will just hang again.
            # Only retry parse/JSON errors where a nudge might help.
            should_retry = attempt < retries and not is_timeout and not is_conn_err

            if should_retry:
                if is_truncation:
                    nudge = (
                        "Your response was truncated. "
                        "Produce a MUCH shorter JSON response. "
                        "Maximum 2 items per array. "
                        "Strings must be under 80 characters. "
                        "Response MUST start with { and end with }."
                    )
                else:
                    nudge = (
                        f"Your previous response could not be parsed as JSON. Error: {err_str[:200]}. "
                        "Output ONLY a valid JSON object. "
                        "Start with { and end with }. "
                        "No markdown, no explanation, no text outside the JSON."
                    )
                messages.append({"role": "assistant", "content": last_raw})
                messages.append({"role": "user",      "content": nudge})
            else:
                # No point continuing — break out of retry loop immediately
                break

    # All retries exhausted (or broken early) — log clearly and return {} so pipeline continues
    console.print(f"[red]  ✗ {label} failed: {last_err}[/red]")
    if raw_out_path:
        err_path = raw_out_path.parent / f"_{label}_FAILED.txt"
        err_path.write_text(
            f"FAILED\nError: {last_err}\nLast raw output:\n{last_raw}",
            encoding="utf-8", errors="replace"
        )
    return {}


# ---------------------------------------------------------------------------
# Template rendering
# ---------------------------------------------------------------------------

def render(template: str, **kwargs) -> str:
    """Fill {{variable}} placeholders. Warns on unresolved ones."""
    out = template
    for k, v in kwargs.items():
        placeholder = "{{" + k + "}}"
        value = v if isinstance(v, str) else json.dumps(v, indent=2)
        out = out.replace(placeholder, value)

    unresolved = re.findall(r"\{\{(\w+)\}\}", out)
    if unresolved:
        console.print(f"[yellow]  ⚠ Unresolved template variables: {unresolved}[/yellow]")
    return out


# ---------------------------------------------------------------------------
# File collection
# ---------------------------------------------------------------------------

def collect_files(
    root: Path,
    extensions: set[str],
    max_files: int,
    single_file: Path | None = None,
) -> list[Path]:
    if single_file:
        if not single_file.is_file():
            raise SystemExit(f"File not found: {single_file}")
        return [single_file]

    found = []
    for dirpath, dirnames, filenames in os.walk(root):
        # Prune excluded directories in-place
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            p = Path(dirpath) / fn
            if p.suffix.lower() in extensions or p.name in extensions:
                found.append(p)
                if max_files > 0 and len(found) >= max_files:
                    return found
    return found


# ---------------------------------------------------------------------------
# File → diff / excerpt
# ---------------------------------------------------------------------------

def file_to_diff(rel_path: str, content: str) -> str:
    """Wrap file content as a synthetic git diff."""
    lines = content.splitlines()
    body = "\n".join("+" + ln for ln in lines) if lines else "+(empty)"
    return (
        f"diff --git a/{rel_path} b/{rel_path}\n"
        f"new file mode 100644\n"
        f"--- /dev/null\n"
        f"+++ b/{rel_path}\n"
        f"@@ -0,0 +1,{max(len(lines), 1)} @@\n"
        f"{body}\n"
    )


def file_to_numbered(rel_path: str, content: str) -> str:
    """Numbered line listing for evidence agent."""
    lines = content.splitlines()
    numbered = "\n".join(f"{i+1:>4}: {ln}" for i, ln in enumerate(lines))
    return f"FILE: {rel_path}\n{numbered}"


def clamp(text: str, max_chars: int) -> str:
    if len(text) <= max_chars:
        return text
    half = max_chars // 2
    return text[:half] + f"\n... [truncated {len(text)-max_chars} chars] ...\n" + text[-half:]


# ---------------------------------------------------------------------------
# Report builder
# ---------------------------------------------------------------------------

def build_report(
    rel_path: str,
    scope: dict,
    threat: dict,
    hypotheses: dict,
    evidence: dict,
    fixes: dict,
    gate: dict,
) -> str:
    lines = [
        f"# Security Review: {rel_path}",
        "",
        f"## Gate Decision: {gate.get('decision', 'UNKNOWN')}",
        "",
    ]

    # Rationale
    rationale = gate.get("rationale", [])
    if rationale:
        lines.append("## Rationale")
        for r in rationale:
            lines.append(f"- {r}")
        lines.append("")

    # Blockers
    blockers = gate.get("blockers", [])
    lines.append("## Blockers")
    if blockers:
        for b in blockers:
            fk  = b.get("finding_key", "?")
            sev = b.get("severity", "?")
            con = b.get("confidence", "?")
            act = b.get("required_action", "")
            lines.append(f"- **{fk}** [{sev}, conf={con}]: {act}")
    else:
        lines.append("- None")
    lines.append("")

    # Confirmed findings
    findings = evidence.get("confirmed_findings_minimal", [])
    lines.append("## Confirmed Findings")
    if findings:
        for f in findings:
            fk  = f.get("finding_key", "?")
            sev = f.get("severity", "?")
            ttl = f.get("title", "")
            cat = f.get("category", "")
            con = f.get("confidence", "?")
            lines.append(f"- **{fk}** [{sev}] {ttl} ({cat}, conf={con})")
            evid = f.get("evidence", {})
            trace = evid.get("trace", "")
            if trace:
                lines.append(f"  - Trace: {trace}")
    else:
        lines.append("- None")
    lines.append("")

    # Fixes — clearly labelled as PROPOSED, not applied
    # Build a lookup so we can cross-reference findings with fix coverage
    fix_list    = fixes.get("fixes", [])
    fixed_keys  = {fx.get("finding_key") for fx in fix_list}
    findings_needing_fix = [
        f for f in evidence.get("confirmed_findings_minimal", [])
        if f.get("severity") in ("Critical", "High")
    ]
    unaddressed = [f for f in findings_needing_fix if f.get("finding_key") not in fixed_keys]

    lines.append("## Proposed Fixes (NOT yet applied to codebase)")
    lines.append("> ⚠ These fixes are recommendations only. The findings remain open until")
    lines.append("> the code changes are implemented, reviewed, and re-scanned.")
    lines.append("")
    if fix_list:
        for fx in fix_list:
            fk  = fx.get("finding_key", "?")
            sev = fx.get("severity", "?")
            ttl = fx.get("title", "")
            mf  = fx.get("recommended_change", {}).get("minimal_fix", {}).get("summary", "")
            bf  = fx.get("recommended_change", {}).get("better_fix", {}).get("summary", "")
            lines.append(f"- **{fk}** [{sev}] {ttl}")
            if mf:
                lines.append(f"  - Minimal fix: {mf}")
            if bf and bf != mf:
                lines.append(f"  - Better fix:  {bf}")
    else:
        lines.append("- None (fix agent produced no output)")
    lines.append("")

    # Unaddressed findings — Critical/High with no proposed fix at all
    if unaddressed:
        lines.append("## ⛔ Unaddressed Findings (no fix proposed)")
        lines.append("> These Critical/High findings have no proposed fix. Manual review required.")
        lines.append("")
        for f in unaddressed:
            fk  = f.get("finding_key", "?")
            sev = f.get("severity", "?")
            ttl = f.get("title", "")
            lines.append(f"- **{fk}** [{sev}] {ttl}")
        lines.append("")

    # Questions for humans
    questions = evidence.get("questions_for_humans", [])
    if questions:
        lines.append("## Questions for Humans")
        for q in questions:
            lines.append(f"- {q}")
        lines.append("")

    # Risk signal
    risk = scope.get("review_risk_signal", {})
    if risk:
        lines.append(f"## Scope Risk Signal: {risk.get('risk', '?')}")
        for w in risk.get("why", []):
            lines.append(f"- {w}")
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Per-file pipeline
# ---------------------------------------------------------------------------

def scan_file(
    client: OpenAI,
    model: str,
    agents: dict,
    rel_path: str,
    content: str,
    repo_root: str,
    pr_label: str,
    out_dir: Path,
    max_chars: int,
    max_tokens: int,
    policy_text: str,
    patterns_text: str,
    arch_text: str,
) -> dict:
    """Run the full agent chain for one file. Returns summary dict."""

    diff    = clamp(file_to_diff(rel_path, content), max_chars)
    excerpt = clamp(file_to_numbered(rel_path, content), max_chars)
    out_dir.mkdir(parents=True, exist_ok=True)

    def agent(name: str, prompt: str) -> dict:
        tok = max(max_tokens, AGENT_MIN_TOKENS.get(name, 2000))
        result = call_agent(
            client, model, agents[name], prompt,
            max_tokens=tok,
            label=name,
            raw_out_path=out_dir / f"_{name}_raw.txt",
        )
        (out_dir / f"{name}.json").write_text(
            json.dumps(result, indent=2), encoding="utf-8"
        )
        return result

    # ------------------------------------------------------------------
    # 1. SCOPE
    # ------------------------------------------------------------------
    console.print(f"    [dim]→ scope[/dim]")
    scope_prompt = render(
        agents["scope"]["user_template"],
        repo=repo_root,
        pr=pr_label,
        diff=diff,
    )
    scope = agent("scope", scope_prompt)

    # ------------------------------------------------------------------
    # 2. THREAT
    # ------------------------------------------------------------------
    console.print(f"    [dim]→ threat[/dim]")
    threat_prompt = render(
        agents["threat"]["user_template"],
        scope_json=json.dumps(scope, indent=2),
        pre_scan_json="{}",
        arch_constraints=arch_text or "(none)",
    )
    threat = agent("threat", threat_prompt)

    # ------------------------------------------------------------------
    # 3. HYPOTHESES
    # ------------------------------------------------------------------
    console.print(f"    [dim]→ hypotheses[/dim]")
    hyp_prompt = render(
        agents["hypotheses"]["user_template"],
        scope_json=json.dumps(scope, indent=2),
        threat_json=json.dumps(threat, indent=2),
        pre_scan_json="{}",
        csharp_notes="(use defaults from system prompt)",
        python_notes="(use defaults from system prompt)",
        ruby_notes="(use defaults from system prompt)",
        node_notes="(use defaults from system prompt)",
    )
    hypotheses = agent("hypotheses", hyp_prompt)

    # ------------------------------------------------------------------
    # 4. EVIDENCE
    # ------------------------------------------------------------------
    console.print(f"    [dim]→ evidence[/dim]")
    ev_prompt = render(
        agents["evidence"]["user_template"],
        hypotheses_json=json.dumps(hypotheses, indent=2),
        fetched_context=excerpt,
        pre_scan_json="{}",
    )
    evidence = agent("evidence", ev_prompt)

    # ------------------------------------------------------------------
    # 5. FIX
    # ------------------------------------------------------------------
    console.print(f"    [dim]→ fix[/dim]")
    fix_prompt = render(
        agents["fix"]["user_template"],
        evidence_json=json.dumps(evidence, indent=2),
        patterns=patterns_text or "(none)",
    )
    fixes = agent("fix", fix_prompt)

    # ------------------------------------------------------------------
    # 6. GATE
    # ------------------------------------------------------------------
    console.print(f"    [dim]→ gate[/dim]")
    gate_prompt = render(
        agents["gate"]["user_template"],
        evidence_json=json.dumps(evidence, indent=2),
        fixes_json=json.dumps(fixes, indent=2),
        pre_scan_json="{}",
        policy=policy_text or "(use default policy)",
    )
    gate = agent("gate", gate_prompt)

    # ------------------------------------------------------------------
    # Report
    # ------------------------------------------------------------------
    report = build_report(rel_path, scope, threat, hypotheses, evidence, fixes, gate)
    (out_dir / "report.md").write_text(report, encoding="utf-8")

    decision = gate.get("decision", "UNKNOWN")
    n_findings = len(evidence.get("confirmed_findings_minimal", []))
    n_blockers  = len(gate.get("blockers", []))
    return {
        "file":      rel_path,
        "decision":  decision,
        "findings":  n_findings,
        "blockers":  n_blockers,
        "out_dir":   str(out_dir),
    }


# ---------------------------------------------------------------------------
# Merged rollup
# ---------------------------------------------------------------------------

def write_rollup(results: list[dict], out_root: Path) -> None:
    merged_dir = out_root / "_merged"
    merged_dir.mkdir(parents=True, exist_ok=True)

    overall = "PASS"
    fail_files, needs_files, pass_files = [], [], []

    for r in results:
        d = r.get("decision", "UNKNOWN")
        if d == "FAIL":
            overall = "FAIL"
            fail_files.append(r["file"])
        elif d == "NEEDS_HUMAN":
            if overall != "FAIL":
                overall = "NEEDS_HUMAN"
            needs_files.append(r["file"])
        else:
            pass_files.append(r["file"])

    summary = {
        "overall_decision": overall,
        "total_files": len(results),
        "fail": fail_files,
        "needs_human": needs_files,
        "pass": pass_files,
        "per_file": results,
    }
    (merged_dir / "summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )

    md = [
        "# Merged Security Review Summary",
        "",
        f"**Overall Decision: {overall}**  |  "
        f"Files scanned: {len(results)}  |  "
        f"FAIL: {len(fail_files)}  |  "
        f"NEEDS_HUMAN: {len(needs_files)}  |  "
        f"PASS: {len(pass_files)}",
        "",
    ]

    if fail_files:
        md.append("## FAIL Files")
        md.extend(f"- {f}" for f in fail_files)
        md.append("")

    if needs_files:
        md.append("## NEEDS_HUMAN Files")
        md.extend(f"- {f}" for f in needs_files)
        md.append("")

    md.append("## All Results")
    md.append("| File | Decision | Findings | Blockers |")
    md.append("|------|----------|----------|----------|")
    for r in results:
        md.append(
            f"| {r['file']} | {r.get('decision','?')} | "
            f"{r.get('findings',0)} | {r.get('blockers',0)} |"
        )
    md.append("")

    (merged_dir / "report.md").write_text("\n".join(md), encoding="utf-8")
    console.print(f"\n[green]Rollup written to {merged_dir}[/green]")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(
        description="Agentic security scanner — scans a directory using LMStudio + agents.yaml"
    )
    ap.add_argument(
        "directory",
        help="Directory to scan (required positional argument)",
    )
    ap.add_argument(
        "--file", default="",
        help="Scan a single file instead of a whole directory (path relative to directory or absolute)",
    )
    ap.add_argument("--config",    default="agents.yaml",  help="Path to agents.yaml")
    ap.add_argument("--out",       default="scan_results",  help="Output directory for artifacts")
    ap.add_argument("--model",     default=None,            help="LMStudio model name (auto-detect if omitted)")
    ap.add_argument("--max-files", type=int, default=50,   help="Max files to scan (0 = unlimited)")
    ap.add_argument("--max-chars", type=int, default=16000, help="Max chars of file content sent per agent call")
    ap.add_argument("--max-tokens",type=int, default=3000,  help="Base max_tokens for LLM calls (per-agent floors apply)")
    ap.add_argument("--retries",   type=int, default=2,    help="Retries per agent call on failure")
    ap.add_argument("--policy",    default="",             help="Path to gate policy text file")
    ap.add_argument("--patterns",  default="",             help="Path to org patterns/standards text file")
    ap.add_argument("--arch",      default="",             help="Path to architecture constraints text file")
    ap.add_argument("--extensions",default="",             help="Comma-separated extra extensions to include (e.g. .jsx,.tsx)")
    args = ap.parse_args()

    # ------------------------------------------------------------------
    # Load config
    # ------------------------------------------------------------------
    config_path = Path(args.config)
    if not config_path.exists():
        raise SystemExit(f"agents.yaml not found at: {config_path.resolve()}")

    cfg = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    agents_cfg = cfg.get("agents", {})

    # Apply defaults for llm config keys that may be missing from agents.yaml
    cfg.setdefault("llm", {})
    cfg["llm"].setdefault("base_url", "http://localhost:1234/v1")
    cfg["llm"].setdefault("api_key", "lm-studio")
    cfg["llm"].setdefault("per_request_timeout", 300)  # seconds per LLM call; raise for slow HW or large files

    required_agents = {"scope", "threat", "hypotheses", "evidence", "fix", "gate"}
    missing = required_agents - set(agents_cfg.keys())
    if missing:
        raise SystemExit(f"agents.yaml is missing agent definitions: {missing}")

    # ------------------------------------------------------------------
    # Extensions
    # ------------------------------------------------------------------
    yaml_exts = set(cfg.get("review", {}).get("include_extensions", []))
    extra_exts = {e.strip() for e in args.extensions.split(",") if e.strip()}
    extensions = DEFAULT_EXTENSIONS | yaml_exts | extra_exts

    # ------------------------------------------------------------------
    # Resolve paths
    # ------------------------------------------------------------------
    scan_root = Path(args.directory).resolve()
    if not scan_root.exists():
        raise SystemExit(f"Directory not found: {scan_root}")

    single_file: Path | None = None
    if args.file:
        p = Path(args.file)
        single_file = p if p.is_absolute() else (scan_root / p).resolve()

    out_root = Path(args.out)
    out_root.mkdir(parents=True, exist_ok=True)

    policy_text   = Path(args.policy).read_text(encoding="utf-8")   if args.policy   and Path(args.policy).exists()   else ""
    patterns_text = Path(args.patterns).read_text(encoding="utf-8") if args.patterns and Path(args.patterns).exists() else ""
    arch_text     = Path(args.arch).read_text(encoding="utf-8")     if args.arch     and Path(args.arch).exists()     else ""

    # ------------------------------------------------------------------
    # LMStudio client
    # ------------------------------------------------------------------
    client = make_client(cfg)
    model  = get_model(client, args.model)

    # ------------------------------------------------------------------
    # Collect files
    # ------------------------------------------------------------------
    targets = collect_files(scan_root, extensions, args.max_files, single_file)
    if not targets:
        raise SystemExit(
            f"No files found matching extensions {sorted(extensions)} under {scan_root}.\n"
            f"Use --extensions to add more, or --file to target a specific file."
        )

    # ------------------------------------------------------------------
    # Startup banner
    # ------------------------------------------------------------------
    console.print(Panel(
        f"[bold cyan]Security Scanner[/bold cyan]\n"
        f"Model:      {model}\n"
        f"Root:       {scan_root}\n"
        f"Files:      {len(targets)}\n"
        f"Output:     {out_root.resolve()}\n"
        f"Max tokens: {args.max_tokens} (per-agent floors: {AGENT_MIN_TOKENS})\n"
        f"Max chars:  {args.max_chars}",
        title="scan.py",
    ))

    # ------------------------------------------------------------------
    # Scan each file
    # ------------------------------------------------------------------
    results = []
    for i, file_path in enumerate(targets, 1):
        try:
            rel = str(file_path.relative_to(scan_root)).replace("\\", "/")
        except ValueError:
            rel = file_path.name

        console.print(f"\n[bold]({i}/{len(targets)}) {rel}[/bold]")

        try:
            content = file_path.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            console.print(f"  [red]Could not read file: {e}[/red]")
            results.append({"file": rel, "decision": "ERROR", "findings": 0, "blockers": 0})
            continue

        # Sanitize rel path for use as directory name
        safe_name = re.sub(r'[\\/:*?"<>|]+', "_", rel)
        out_dir = out_root / safe_name

        t_file_start = time.monotonic()
        try:
            result = scan_file(
                client=client,
                model=model,
                agents=agents_cfg,
                rel_path=rel,
                content=content,
                repo_root=str(scan_root),
                pr_label=f"scan:{rel}",
                out_dir=out_dir,
                max_chars=args.max_chars,
                max_tokens=args.max_tokens,
                policy_text=policy_text,
                patterns_text=patterns_text,
                arch_text=arch_text,
            )
            elapsed_file = time.monotonic() - t_file_start
            results.append(result)

            decision = result.get("decision", "?")
            colour = {"PASS": "green", "FAIL": "red", "NEEDS_HUMAN": "yellow"}.get(decision, "white")
            console.print(
                f"  [{colour}]{decision}[/{colour}]  "
                f"{result.get('findings', 0)} finding(s), "
                f"{result.get('blockers', 0)} blocker(s)  "
                f"[dim]({elapsed_file:.0f}s)[/dim]  → {out_dir}"
            )

        except KeyboardInterrupt:
            console.print("\n[yellow]Interrupted by user.[/yellow]")
            break
        except Exception as e:
            console.print(f"  [red]Pipeline error: {e}[/red]")
            results.append({"file": rel, "decision": "ERROR", "findings": 0, "blockers": 0})

    # ------------------------------------------------------------------
    # Rollup
    # ------------------------------------------------------------------
    if results:
        write_rollup(results, out_root)

    # Final summary
    decisions = [r.get("decision") for r in results]
    console.print(
        f"\n[bold]Done.[/bold]  "
        f"FAIL={decisions.count('FAIL')}  "
        f"NEEDS_HUMAN={decisions.count('NEEDS_HUMAN')}  "
        f"PASS={decisions.count('PASS')}  "
        f"ERROR={decisions.count('ERROR')}"
    )


if __name__ == "__main__":
    main()
