#!/usr/bin/env python3
"""
analyse_runs.py — Multi-run stability analyser for scan_file.py output.

Reads multiple scan result directories (one per run) and produces:
  - Per-finding detection rate across runs
  - Confidence score distribution (mean, std dev, min, max)
  - Gate verdict distribution per file
  - Temperature-sensitive findings (detection rate < threshold)
  - Agent timing statistics
  - Agent failure/truncation counts
  - Cross-run diff: findings that appear in some runs but not others
  - Summary CSV and Markdown report

Usage:
    python analyse_runs.py run1/ run2/ run3/ ...
    python analyse_runs.py --runs-dir all_runs/ --pattern "run_*"
    python analyse_runs.py run1/ run2/ --out analysis/ --threshold 0.8
    python analyse_runs.py run1/ run2/ --label "temp=0.7" --out analysis/

Directory structure expected (scan_file.py default output):
    <run_dir>/
        <file_safe_name>/
            evidence.json
            gate.json
            fixes.json
            scope.json
            threat_model.json
            hypotheses.json
            pre_scan.json          (optional)
            _evidence_raw.txt
            _gate_raw.txt
            _scope_raw.txt
            _threat_raw.txt
            _hypotheses_raw.txt
            _fix_raw.txt
            _<agent>_FAILED.txt   (on failure)
            report.md
        _merged/
            summary.json
            report.md
"""

import argparse
import csv
import json
import math
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    HAS_RICH = True
except ImportError:
    HAS_RICH = False

console = Console() if HAS_RICH else None

AGENTS = ["scope", "threat", "hypotheses", "evidence", "fix", "gate", "pre_scan"]
SEVERITIES = ["Critical", "High", "Medium", "Low"]

# ─────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────

def cprint(msg: str, style: str = "") -> None:
    if HAS_RICH:
        console.print(msg, style=style)
    else:
        # Strip rich markup for plain output
        clean = re.sub(r"\[.*?\]", "", msg)
        print(clean)


def load_json(path: Path) -> dict | list | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def parse_raw_elapsed(raw_path: Path) -> float | None:
    """Extract elapsed seconds from _<agent>_raw.txt header line."""
    if not raw_path.exists():
        return None
    try:
        first_line = raw_path.read_text(encoding="utf-8").split("\n", 1)[0]
        m = re.search(r"elapsed:\s*([\d.]+)s", first_line)
        return float(m.group(1)) if m else None
    except Exception:
        return None


def parse_raw_finish_reason(raw_path: Path) -> str:
    """Extract finish_reason from _<agent>_raw.txt header line."""
    if not raw_path.exists():
        return "missing"
    try:
        first_line = raw_path.read_text(encoding="utf-8").split("\n", 1)[0]
        m = re.search(r"finish_reason:\s*(\S+)", first_line)
        return m.group(1) if m else "unknown"
    except Exception:
        return "error"


def finding_key(finding: dict) -> str:
    """
    Stable identity key for a finding across runs.
    Prefer id field; fall back to title+severity normalised.
    """
    fid = finding.get("id", "")
    title = re.sub(r"\s+", " ", finding.get("title", "")).strip().lower()
    sev = finding.get("severity", "")
    if fid:
        # Strip run-specific numeric suffix variations e.g. FND-001 vs FND-002
        # but keep the semantic content — use title+severity as canonical key
        return f"{title}|{sev}"
    return f"{title}|{sev}"


def wilson_ci(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    """Wilson score confidence interval for a proportion."""
    if n == 0:
        return 0.0, 0.0
    p = k / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    spread = (z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))) / denom
    return max(0.0, centre - spread), min(1.0, centre + spread)


def std_dev(values: list[float]) -> float:
    if len(values) < 2:
        return 0.0
    mean = sum(values) / len(values)
    return math.sqrt(sum((v - mean) ** 2 for v in values) / (len(values) - 1))


# ─────────────────────────────────────────────
# Data loading
# ─────────────────────────────────────────────

class RunData:
    """All findings/timing/verdicts from a single scan run directory."""

    def __init__(self, run_dir: Path):
        self.run_dir = run_dir
        self.run_label = run_dir.name
        self.file_results: dict[str, dict] = {}   # file_key → parsed data
        self._load()

    def _load(self) -> None:
        for child in sorted(self.run_dir.iterdir()):
            if not child.is_dir() or child.name.startswith("_"):
                continue
            self.file_results[child.name] = self._load_file_dir(child)

    def _load_file_dir(self, d: Path) -> dict:
        result: dict[str, Any] = {
            "path": d,
            "agents": {},
        }

        for agent in AGENTS:
            json_path  = d / f"{agent}.json" if agent != "threat" else d / "threat_model.json"
            # scan_file.py writes threat as threat_model.json
            if agent == "threat":
                json_path = d / "threat_model.json"
            else:
                json_path = d / f"{agent}.json"
            raw_path   = d / f"_{agent}_raw.txt"
            fail_path  = d / f"_{agent}_FAILED.txt"

            result["agents"][agent] = {
                "data":          load_json(json_path),
                "elapsed":       parse_raw_elapsed(raw_path),
                "finish_reason": parse_raw_finish_reason(raw_path),
                "failed":        fail_path.exists(),
                "missing":       not json_path.exists() and not fail_path.exists(),
            }

        # Convenience shortcuts
        ev   = result["agents"]["evidence"]["data"] or {}
        gate = result["agents"]["gate"]["data"]     or {}
        pre  = result["agents"]["pre_scan"]["data"] or {}

        result["confirmed_findings"]   = ev.get("confirmed_findings_minimal", [])
        result["inconclusive"]         = ev.get("inconclusive_high_severity", [])
        result["gate_decision"]        = gate.get("decision", "UNKNOWN")
        result["gate_enumeration"]     = gate.get("finding_enumeration", [])
        result["gate_rationale"]       = gate.get("rationale", [])
        result["pre_scan_findings"]    = pre.get("confirmed_findings", [])
        result["uncovered_pre_scan"]   = ev.get("uncovered_pre_scan_findings", [])

        return result


# ─────────────────────────────────────────────
# Analysis engine
# ─────────────────────────────────────────────

class StabilityAnalyser:

    def __init__(self, runs: list[RunData], threshold: float = 0.8):
        self.runs      = runs
        self.n_runs    = len(runs)
        self.threshold = threshold   # below this detection rate → temperature-sensitive
        self._analyse()

    def _analyse(self) -> None:
        # Collect all file keys across all runs
        all_file_keys: set[str] = set()
        for run in self.runs:
            all_file_keys.update(run.file_results.keys())
        self.file_keys = sorted(all_file_keys)

        # Per-file, per-finding stability
        # finding_stats[file_key][finding_key] = {detections, confidences, severities}
        self.finding_stats: dict[str, dict[str, dict]] = defaultdict(lambda: defaultdict(
            lambda: {"detections": 0, "confidences": [], "severities": [], "run_ids": []}
        ))

        # Gate verdict distribution per file
        self.gate_verdicts: dict[str, list[str]] = defaultdict(list)

        # Agent timing per agent per file
        self.agent_timing: dict[str, dict[str, list[float]]] = defaultdict(
            lambda: defaultdict(list)
        )

        # Agent failures / truncations
        self.agent_failures:    dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
        self.agent_truncations: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))

        # Per-run total elapsed (sum of all agent times for a file)
        self.file_total_elapsed: dict[str, list[float]] = defaultdict(list)

        for run_idx, run in enumerate(self.runs):
            for fkey, fdata in run.file_results.items():

                # Gate verdict
                self.gate_verdicts[fkey].append(fdata["gate_decision"])

                # Findings
                for finding in fdata["confirmed_findings"]:
                    fk = finding_key(finding)
                    fs = self.finding_stats[fkey][fk]
                    fs["detections"] += 1
                    fs["run_ids"].append(run_idx)
                    conf = finding.get("confidence")
                    if conf is not None:
                        try:
                            fs["confidences"].append(float(conf))
                        except (ValueError, TypeError):
                            pass
                    sev = finding.get("severity", "")
                    if sev:
                        fs["severities"].append(sev)
                    # Keep a sample finding object for display
                    if "sample" not in fs:
                        fs["sample"] = finding

                # Agent timing + failures
                run_total = 0.0
                for agent, adata in fdata["agents"].items():
                    if adata["elapsed"] is not None:
                        self.agent_timing[fkey][agent].append(adata["elapsed"])
                        run_total += adata["elapsed"]
                    if adata["failed"]:
                        self.agent_failures[fkey][agent] += 1
                    if adata["finish_reason"] in ("length", "max_tokens", "MAX_TOKENS"):
                        self.agent_truncations[fkey][agent] += 1

                if run_total > 0:
                    self.file_total_elapsed[fkey].append(run_total)

    # ── Computed properties ──

    def detection_rate(self, fkey: str, finding_k: str) -> float:
        runs_with_file = sum(1 for r in self.runs if fkey in r.file_results)
        if runs_with_file == 0:
            return 0.0
        return self.finding_stats[fkey][finding_k]["detections"] / runs_with_file

    def runs_with_file(self, fkey: str) -> int:
        return sum(1 for r in self.runs if fkey in r.file_results)

    def gate_verdict_counts(self, fkey: str) -> dict[str, int]:
        counts: dict[str, int] = defaultdict(int)
        for v in self.gate_verdicts[fkey]:
            counts[v] += 1
        return dict(counts)

    def gate_consistency(self, fkey: str) -> float:
        """Fraction of runs that agree on the majority verdict."""
        verdicts = self.gate_verdicts[fkey]
        if not verdicts:
            return 0.0
        counts = self.gate_verdict_counts(fkey)
        majority = max(counts.values())
        return majority / len(verdicts)

    def sensitive_findings(self, fkey: str) -> list[dict]:
        """Findings with detection rate below threshold."""
        result = []
        n = self.runs_with_file(fkey)
        for fk, stats in self.finding_stats[fkey].items():
            rate = stats["detections"] / n if n else 0
            if rate < self.threshold:
                result.append({
                    "key":        fk,
                    "rate":       rate,
                    "detections": stats["detections"],
                    "n_runs":     n,
                    "sample":     stats.get("sample", {}),
                    "conf_mean":  sum(stats["confidences"]) / len(stats["confidences"]) if stats["confidences"] else None,
                    "conf_std":   std_dev(stats["confidences"]),
                })
        return sorted(result, key=lambda x: x["rate"])

    def stable_findings(self, fkey: str) -> list[dict]:
        """Findings with detection rate >= threshold."""
        result = []
        n = self.runs_with_file(fkey)
        for fk, stats in self.finding_stats[fkey].items():
            rate = stats["detections"] / n if n else 0
            if rate >= self.threshold:
                confs = stats["confidences"]
                result.append({
                    "key":        fk,
                    "rate":       rate,
                    "detections": stats["detections"],
                    "n_runs":     n,
                    "sample":     stats.get("sample", {}),
                    "conf_mean":  sum(confs) / len(confs) if confs else None,
                    "conf_std":   std_dev(confs),
                    "conf_min":   min(confs) if confs else None,
                    "conf_max":   max(confs) if confs else None,
                    "severity":   max(set(stats["severities"]), key=stats["severities"].count) if stats["severities"] else "?",
                    "ci_lo":      wilson_ci(stats["detections"], n)[0],
                    "ci_hi":      wilson_ci(stats["detections"], n)[1],
                })
        return sorted(result, key=lambda x: -x["rate"])


# ─────────────────────────────────────────────
# Report generation
# ─────────────────────────────────────────────

def build_markdown(analyser: StabilityAnalyser, label: str) -> str:
    md = []
    n  = analyser.n_runs

    md.append(f"# Scan stability analysis — {label}")
    md.append(f"\n**Runs analysed:** {n}  |  "
              f"**Files:** {len(analyser.file_keys)}  |  "
              f"**Stability threshold:** {analyser.threshold:.0%}\n")

    md.append("## Summary")
    md.append("| File | Runs | Gate: PASS | FAIL | NEEDS_HUMAN | Gate consistency | "
              "Stable findings | Sensitive findings |")
    md.append("|---|---|---|---|---|---|---|---|")

    for fkey in analyser.file_keys:
        n_f    = analyser.runs_with_file(fkey)
        vc     = analyser.gate_verdict_counts(fkey)
        gc     = analyser.gate_consistency(fkey)
        stable = len(analyser.stable_findings(fkey))
        sens   = len(analyser.sensitive_findings(fkey))
        md.append(
            f"| `{fkey}` | {n_f} | {vc.get('PASS',0)} | {vc.get('FAIL',0)} | "
            f"{vc.get('NEEDS_HUMAN',0)} | {gc:.0%} | {stable} | {sens} |"
        )

    for fkey in analyser.file_keys:
        md.append(f"\n---\n\n## File: `{fkey}`")
        n_f = analyser.runs_with_file(fkey)
        vc  = analyser.gate_verdict_counts(fkey)
        gc  = analyser.gate_consistency(fkey)

        md.append(f"\n**Runs with this file:** {n_f}  |  "
                  f"**Gate consistency:** {gc:.0%}  |  "
                  f"**Verdict distribution:** " +
                  "  ".join(f"{k}: {v}" for k, v in sorted(vc.items())))

        # Stable findings
        stable = analyser.stable_findings(fkey)
        if stable:
            md.append(f"\n### Stable findings  (detection rate ≥ {analyser.threshold:.0%})\n")
            md.append("| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |")
            md.append("|---|---|---|---|---|---|")
            for f in stable:
                s      = f["sample"]
                title  = s.get("title", f["key"])
                sev    = f.get("severity", "?")
                rate   = f["rate"]
                ci_lo  = f["ci_lo"]
                ci_hi  = f["ci_hi"]
                cm     = f"{f['conf_mean']:.2f}" if f["conf_mean"] is not None else "—"
                cs     = f"{f['conf_std']:.3f}" if f["conf_std"] else "—"
                md.append(f"| {title} | {sev} | {rate:.0%} ({f['detections']}/{n_f}) | "
                           f"[{ci_lo:.2f}, {ci_hi:.2f}] | {cm} | {cs} |")

        # Sensitive findings
        sensitive = analyser.sensitive_findings(fkey)
        if sensitive:
            md.append(f"\n### ⚠ Temperature-sensitive findings  (detection rate < {analyser.threshold:.0%})\n")
            md.append("| Finding | Severity | Detection rate | Conf mean | Notes |")
            md.append("|---|---|---|---|---|")
            for f in sensitive:
                s     = f["sample"]
                title = s.get("title", f["key"])
                sev   = s.get("severity", "?")
                rate  = f["rate"]
                cm    = f"{f['conf_mean']:.2f}" if f["conf_mean"] is not None else "—"
                note  = "borderline confidence" if (f["conf_mean"] or 0) < 0.7 else "model inconsistency"
                md.append(f"| {title} | {sev} | {rate:.0%} ({f['detections']}/{n_f}) | {cm} | {note} |")

        # Agent timing
        md.append("\n### Agent timing\n")
        md.append("| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |")
        md.append("|---|---|---|---|---|---|---|")
        for agent in AGENTS:
            times = analyser.agent_timing[fkey].get(agent, [])
            fails = analyser.agent_failures[fkey].get(agent, 0)
            trunc = analyser.agent_truncations[fkey].get(agent, 0)
            if not times and fails == 0 and trunc == 0:
                continue
            mean = sum(times) / len(times) if times else 0
            sd   = std_dev(times)
            mn   = min(times) if times else 0
            mx   = max(times) if times else 0
            md.append(f"| {agent} | {mean:.1f} | {sd:.1f} | {mn:.1f} | {mx:.1f} | {fails} | {trunc} |")

        # Total run time
        totals = analyser.file_total_elapsed.get(fkey, [])
        if totals:
            mean_t = sum(totals) / len(totals)
            md.append(f"\n**Mean total elapsed per run:** {mean_t:.0f}s  |  "
                      f"Min: {min(totals):.0f}s  |  Max: {max(totals):.0f}s\n")

    # Appendix: gate verdict detail
    md.append("\n---\n\n## Gate verdict detail per run\n")
    for fkey in analyser.file_keys:
        md.append(f"\n### `{fkey}`\n")
        md.append("| Run | Verdict |")
        md.append("|---|---|")
        for run in analyser.runs:
            if fkey in run.file_results:
                verdict = run.file_results[fkey]["gate_decision"]
                md.append(f"| {run.run_label} | {verdict} |")

    return "\n".join(md)


def build_csv(analyser: StabilityAnalyser) -> list[dict]:
    """Flat CSV rows — one row per file × finding."""
    rows = []
    for fkey in analyser.file_keys:
        n_f = analyser.runs_with_file(fkey)
        vc  = analyser.gate_verdict_counts(fkey)
        gc  = analyser.gate_consistency(fkey)

        all_findings = {
            **{k: v for k, v in analyser.finding_stats[fkey].items()}
        }
        for fk, stats in all_findings.items():
            confs = stats["confidences"]
            rate  = stats["detections"] / n_f if n_f else 0
            ci_lo, ci_hi = wilson_ci(stats["detections"], n_f)
            sample = stats.get("sample", {})
            rows.append({
                "file":             fkey,
                "finding_key":      fk,
                "finding_title":    sample.get("title", fk),
                "finding_id":       sample.get("id", ""),
                "severity":         sample.get("severity", ""),
                "detection_rate":   f"{rate:.4f}",
                "detections":       stats["detections"],
                "n_runs":           n_f,
                "ci_lo_95":         f"{ci_lo:.4f}",
                "ci_hi_95":         f"{ci_hi:.4f}",
                "conf_mean":        f"{sum(confs)/len(confs):.4f}" if confs else "",
                "conf_std":         f"{std_dev(confs):.4f}" if confs else "",
                "conf_min":         f"{min(confs):.4f}" if confs else "",
                "conf_max":         f"{max(confs):.4f}" if confs else "",
                "stable":           "yes" if rate >= analyser.threshold else "no",
                "gate_pass":        vc.get("PASS", 0),
                "gate_fail":        vc.get("FAIL", 0),
                "gate_needs_human": vc.get("NEEDS_HUMAN", 0),
                "gate_consistency": f"{gc:.4f}",
            })

    return rows


def build_summary_json(analyser: StabilityAnalyser, label: str) -> dict:
    summary: dict[str, Any] = {
        "label":       label,
        "n_runs":      analyser.n_runs,
        "threshold":   analyser.threshold,
        "files":       {},
    }
    for fkey in analyser.file_keys:
        n_f   = analyser.runs_with_file(fkey)
        vc    = analyser.gate_verdict_counts(fkey)
        gc    = analyser.gate_consistency(fkey)
        stab  = analyser.stable_findings(fkey)
        sens  = analyser.sensitive_findings(fkey)

        totals = analyser.file_total_elapsed.get(fkey, [])
        timing_summary = {}
        for agent in AGENTS:
            times = analyser.agent_timing[fkey].get(agent, [])
            if times:
                timing_summary[agent] = {
                    "mean_s": round(sum(times) / len(times), 2),
                    "std_s":  round(std_dev(times), 2),
                    "min_s":  round(min(times), 2),
                    "max_s":  round(max(times), 2),
                    "failures":    analyser.agent_failures[fkey].get(agent, 0),
                    "truncations": analyser.agent_truncations[fkey].get(agent, 0),
                }

        summary["files"][fkey] = {
            "runs_with_file":    n_f,
            "gate_verdicts":     vc,
            "gate_consistency":  round(gc, 4),
            "stable_findings":   stab,
            "sensitive_findings": sens,
            "agent_timing":      timing_summary,
            "total_elapsed_mean_s": round(sum(totals) / len(totals), 1) if totals else None,
        }
    return summary


# ─────────────────────────────────────────────
# Terminal display (rich)
# ─────────────────────────────────────────────

def display_terminal(analyser: StabilityAnalyser, label: str) -> None:
    if not HAS_RICH:
        print(f"\n=== Stability analysis: {label} ===")
        print(f"Runs: {analyser.n_runs}  Files: {len(analyser.file_keys)}")

    cprint(f"\n[bold]Stability analysis[/bold] — {label}")
    cprint(f"Runs: [cyan]{analyser.n_runs}[/cyan]  "
           f"Files: [cyan]{len(analyser.file_keys)}[/cyan]  "
           f"Threshold: [cyan]{analyser.threshold:.0%}[/cyan]\n")

    for fkey in analyser.file_keys:
        cprint(f"\n[bold underline]{fkey}[/bold underline]")

        n_f   = analyser.runs_with_file(fkey)
        vc    = analyser.gate_verdict_counts(fkey)
        gc    = analyser.gate_consistency(fkey)
        stab  = analyser.stable_findings(fkey)
        sens  = analyser.sensitive_findings(fkey)

        gc_colour = "green" if gc >= 0.9 else ("yellow" if gc >= 0.7 else "red")
        cprint(f"  Runs: {n_f}  |  Gate consistency: [{gc_colour}]{gc:.0%}[/{gc_colour}]  |  "
               f"PASS:{vc.get('PASS',0)}  FAIL:{vc.get('FAIL',0)}  "
               f"NEEDS_HUMAN:{vc.get('NEEDS_HUMAN',0)}")

        if HAS_RICH:
            if stab:
                t = Table(title="Stable findings", header_style="bold green",
                          show_edge=False, padding=(0, 1))
                t.add_column("Finding",       max_width=40)
                t.add_column("Sev",           width=9)
                t.add_column("Rate",          width=8)
                t.add_column("95% CI",        width=14)
                t.add_column("Conf μ",        width=7)
                t.add_column("Conf σ",        width=7)
                for f in stab:
                    s     = f["sample"]
                    title = (s.get("title") or f["key"])[:40]
                    sev   = s.get("severity", "?")
                    sev_c = {"Critical":"red","High":"yellow","Medium":"cyan","Low":"dim"}.get(sev, "")
                    t.add_row(
                        title,
                        f"[{sev_c}]{sev}[/{sev_c}]" if sev_c else sev,
                        f"{f['rate']:.0%} ({f['detections']}/{n_f})",
                        f"[{f['ci_lo']:.2f}, {f['ci_hi']:.2f}]",
                        f"{f['conf_mean']:.2f}" if f["conf_mean"] is not None else "—",
                        f"{f['conf_std']:.3f}" if f["conf_std"] else "—",
                    )
                console.print(t)

            if sens:
                t2 = Table(title=f"⚠ Sensitive findings (rate < {analyser.threshold:.0%})",
                           header_style="bold yellow", show_edge=False, padding=(0, 1))
                t2.add_column("Finding",   max_width=40)
                t2.add_column("Sev",       width=9)
                t2.add_column("Rate",      width=12)
                t2.add_column("Conf μ",    width=7)
                for f in sens:
                    s     = f["sample"]
                    title = (s.get("title") or f["key"])[:40]
                    sev   = s.get("severity", "?")
                    t2.add_row(
                        title,
                        sev,
                        f"[yellow]{f['rate']:.0%}[/yellow] ({f['detections']}/{n_f})",
                        f"{f['conf_mean']:.2f}" if f["conf_mean"] is not None else "—",
                    )
                console.print(t2)

        else:
            for f in stab:
                s = f["sample"]
                print(f"  STABLE  {s.get('title','?')[:50]}  "
                      f"{s.get('severity','?')}  {f['rate']:.0%}")
            for f in sens:
                s = f["sample"]
                print(f"  SENSITIVE  {s.get('title','?')[:50]}  "
                      f"{s.get('severity','?')}  {f['rate']:.0%}")

        # Timing summary
        totals = analyser.file_total_elapsed.get(fkey, [])
        if totals:
            cprint(f"  [dim]Mean total elapsed: {sum(totals)/len(totals):.0f}s  "
                   f"(min {min(totals):.0f}s  max {max(totals):.0f}s)[/dim]")


# ─────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────

def collect_run_dirs(args) -> list[Path]:
    dirs: list[Path] = []

    if args.runs_dir:
        base = Path(args.runs_dir)
        if not base.is_dir():
            sys.exit(f"ERROR: --runs-dir not found: {base}")
        pattern = args.pattern or "*"
        candidates = sorted(base.glob(pattern))
        dirs = [c for c in candidates if c.is_dir() and not c.name.startswith("_")]

    if args.run_dirs:
        for d in args.run_dirs:
            p = Path(d)
            if not p.is_dir():
                sys.exit(f"ERROR: run directory not found: {p}")
            dirs.append(p)

    if not dirs:
        sys.exit("ERROR: no run directories found. Pass them as positional args or use --runs-dir.")

    return dirs


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Analyse multiple scan_file.py output directories for finding stability.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    ap.add_argument(
        "run_dirs", nargs="*",
        help="One or more scan output directories (one per run).",
    )
    ap.add_argument(
        "--runs-dir", default="",
        help="Parent directory containing all run subdirectories.",
    )
    ap.add_argument(
        "--pattern", default="*",
        help="Glob pattern for run subdirectory names under --runs-dir (default: *).",
    )
    ap.add_argument(
        "--out", default="stability_analysis",
        help="Output directory for report files (default: stability_analysis/).",
    )
    ap.add_argument(
        "--label", default="",
        help="Label for this analysis run (e.g. 'temp=0.7  model=Qwen30B').",
    )
    ap.add_argument(
        "--threshold", type=float, default=0.8,
        help="Detection rate below which a finding is flagged as temperature-sensitive (default: 0.8).",
    )
    ap.add_argument(
        "--no-csv", action="store_true",
        help="Skip CSV output.",
    )
    ap.add_argument(
        "--no-json", action="store_true",
        help="Skip JSON summary output.",
    )
    args = ap.parse_args()

    run_dirs = collect_run_dirs(args)
    label    = args.label or f"{len(run_dirs)} runs"

    cprint(f"\n[bold]Loading {len(run_dirs)} run(s)...[/bold]")
    runs: list[RunData] = []
    for d in run_dirs:
        cprint(f"  [dim]→ {d.name}[/dim]")
        runs.append(RunData(d))

    if not runs:
        sys.exit("ERROR: no runs loaded.")

    analyser = StabilityAnalyser(runs, threshold=args.threshold)

    # Terminal display
    display_terminal(analyser, label)

    # Write outputs
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Markdown report
    md_path = out_dir / "stability_report.md"
    md_path.write_text(build_markdown(analyser, label), encoding="utf-8")
    cprint(f"\n[green]✓[/green] Report written → {md_path}")

    # CSV
    if not args.no_csv:
        csv_path = out_dir / "findings.csv"
        rows = build_csv(analyser)
        if rows:
            with csv_path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
                writer.writeheader()
                writer.writerows(rows)
            cprint(f"[green]✓[/green] CSV written → {csv_path}")

    # JSON summary
    if not args.no_json:
        json_path = out_dir / "stability_summary.json"
        json_path.write_text(
            json.dumps(build_summary_json(analyser, label), indent=2),
            encoding="utf-8",
        )
        cprint(f"[green]✓[/green] JSON written → {json_path}")

    cprint("\n[bold]Done.[/bold]\n")


if __name__ == "__main__":
    main()
