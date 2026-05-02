"""
quick_scan.py  –  Fast single-agent security scanner for CI/CD pipelines
=========================================================================
Makes a single LLM call per file.  Designed to run as a PR gate in Azure
DevOps or GitHub Actions.  All six LLM backends from scan.py are supported.

Exit codes
----------
  0  PASS    — no significant findings
  1  WARN    — findings present but below the fail threshold
  2  FAIL    — Critical/High findings above the confidence threshold
  3  ERROR   — scanner error (treat as WARN during rollout)

Provider flags (mutually exclusive; default: --lmstudio)
---------------------------------------------------------
  --lmstudio      LM Studio local server (OpenAI-compatible)
  --openai        OpenAI API
  --anthropic     Anthropic API (native SDK)
  --bedrock       AWS Bedrock (boto3 converse)
  --azure         Azure AI Foundry (OpenAI-compatible)
  --gemini        Google Gemini (native SDK)

Requirements
------------
  pip install openai pyyaml rich          # always required
  pip install anthropic                   # --anthropic
  pip install boto3                       # --bedrock
  pip install google-generativeai         # --gemini

Usage
-----
  # LM Studio (default)
  python quick_scan.py src/

  # Scan only files changed in the current PR (Azure DevOps)
  python quick_scan.py $(Build.SourcesDirectory) \\
      --files $(git diff --name-only origin/$(System.PullRequest.TargetBranch)) \\
      --out $(Build.ArtifactStagingDirectory)/security-scan

  # OpenAI, single file
  python quick_scan.py src/ --openai --api-key sk-... --files src/auth.py

  # Anthropic, warn-only rollout mode
  python quick_scan.py src/ --anthropic --api-key sk-ant-... --warn-only

  # AWS Bedrock with named profile
  python quick_scan.py src/ --bedrock --aws-region eu-west-1 --aws-profile prod

  # Azure AI Foundry
  python quick_scan.py src/ --azure \\
      --endpoint https://my-resource.openai.azure.com \\
      --api-key <key> --azure-deployment gpt-4o

  # Gemini
  python quick_scan.py src/ --gemini --api-key AIza...

  # GitHub Actions annotations
  python quick_scan.py src/ --openai --api-key sk-... --gha

  # Suppress Azure DevOps log commands
  python quick_scan.py src/ --no-ado
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any, Protocol
from urllib.parse import urlparse

import yaml
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console(stderr=True)   # Rich output to stderr; stdout is reserved for ADO/GHA commands

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

VERSION = "1.0.0"

DEFAULT_EXTENSIONS = {
    ".cs", ".py", ".rb", ".js", ".ts", ".java", ".go", ".php",
    ".json", ".yml", ".yaml", ".config", ".xml", ".env",
    ".csproj", ".toml",
}

SKIP_DIRS = {
    ".git", ".svn", ".hg", "node_modules", "vendor", "bower_components",
    "bin", "obj", "dist", "build", "out", "target", ".venv", "venv",
    "__pycache__", ".pytest_cache", ".mypy_cache", ".tox", "coverage",
    ".next", ".nuxt", "Migrations", "migrations",
}

# Confidence thresholds for gate decisions
FAIL_CONFIDENCE_THRESHOLD = 0.70   # Critical/High above this → FAIL
WARN_CONFIDENCE_THRESHOLD = 0.40   # Critical/High above this → WARN

# Max tokens for the single quick-scan agent call
QUICK_SCAN_MIN_TOKENS  = 8000
QUICK_SCAN_MAX_CHARS   = 12000    # file content chars sent to model
MAX_FILE_READ_BYTES    = 16 * 1024 * 1024

# Default endpoints per provider (mirrors scan.py)
PROVIDER_DEFAULTS = {
    "lmstudio":  "http://localhost:1234/v1",
    "openai":    "https://api.openai.com/v1",
    "anthropic": "https://api.anthropic.com",
    "bedrock":   None,
    "azure":     None,
    "gemini":    "https://generativelanguage.googleapis.com",
}

PROVIDER_DEFAULT_MODELS = {
    "lmstudio":  None,
    "openai":    "gpt-4o",
    "anthropic": "claude-sonnet-4-5",
    "bedrock":   "anthropic.claude-3-5-sonnet-20241022-v2:0",
    "azure":     "gpt-4o",
    "gemini":    "gemini-2.0-flash",
}

# Exit codes
EXIT_PASS  = 0
EXIT_WARN  = 1
EXIT_FAIL  = 2
EXIT_ERROR = 3

# Severity weights for rollup decision
SEVERITY_RANK = {"CRITICAL": 4, "HIGH": 3, "MEDIUM": 2, "LOW": 1, "INFO": 0}


# ---------------------------------------------------------------------------
# Security utilities  (identical to scan.py)
# ---------------------------------------------------------------------------

def atomic_write_text(path: Path, content: str, encoding: str = "utf-8") -> None:
    """Write content atomically via a sibling temp file + os.replace()."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding=encoding) as fh:
            fh.write(content)
        os.replace(tmp, path)
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def redact_url_credentials(url: str) -> str:
    """Strip embedded credentials from a URL before logging."""
    try:
        parsed = urlparse(url)
        if parsed.username or parsed.password:
            safe = parsed._replace(
                netloc=f"***@{parsed.hostname}"
                + (f":{parsed.port}" if parsed.port else "")
            )
            return safe.geturl()
    except Exception:
        pass
    return url


def validate_endpoint_url(url: str, provider: str) -> str:
    """Reject non-HTTP(S) schemes to prevent file:// / ftp:// SSRF probes."""
    if not url:
        return url
    try:
        parsed = urlparse(url)
    except Exception as exc:
        raise ValueError(f"[{provider}] Invalid endpoint URL {url!r}: {exc}") from exc
    if parsed.scheme.lower() not in {"http", "https"}:
        raise ValueError(
            f"[{provider}] Endpoint must use http:// or https://. "
            f"Got {parsed.scheme!r} in {url!r}."
        )
    if not parsed.netloc:
        raise ValueError(
            f"[{provider}] Endpoint {url!r} has no host. "
            "Provide a full URL such as https://api.example.com/v1"
        )
    return url


def validate_output_path(base: Path, relative: Path) -> Path:
    """Confirm resolved path stays inside base; raise ValueError on traversal."""
    resolved = (base / relative).resolve()
    try:
        resolved.relative_to(base.resolve())
    except ValueError:
        raise ValueError(
            f"Path traversal detected: {relative!r} escapes output root {base!r}"
        )
    return resolved


# ---------------------------------------------------------------------------
# JSON extraction helpers  (identical to scan.py)
# ---------------------------------------------------------------------------

def strip_fences(text: str) -> str:
    text = (text or "").strip()
    text = re.sub(r"^```[a-zA-Z]*\s*", "", text)
    text = re.sub(r"\s*```\s*$", "", text)
    return text.strip()


def fix_control_chars(text: str) -> str:
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
    text = text.replace("\u201c", '"').replace("\u201d", '"')
    text = text.replace("\u2018", "'").replace("\u2019", "'")
    text = text.replace("\x00", "")
    text = re.sub(r"//[^\n]*", "", text)
    text = re.sub(r'([{\[,]\s*)([A-Za-z_][A-Za-z0-9_]*)\s*:', r'\1"\2":', text)
    text = re.sub(r",\s*([}\]])", r"\1", text)
    return text.strip()


def strip_think_blocks(text: str) -> str:
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<think>.*$",         "", text, flags=re.DOTALL | re.IGNORECASE)
    return text.strip()


def extract_json(raw: str) -> dict:
    if not raw or not raw.strip():
        raise ValueError("Empty response from model")

    raw = strip_think_blocks(raw)
    if not raw.strip():
        raise ValueError(
            "Response contained only a think block — no JSON produced. "
            "Try setting presence_penalty: 1.5 in agents_quick.yaml."
        )

    candidates: list[str] = [strip_fences(raw)]

    start = raw.find("{")
    if start != -1:
        depth = 0
        for i in range(start, len(raw)):
            if raw[i] == "{":
                depth += 1
            elif raw[i] == "}":
                depth -= 1
                if depth == 0:
                    candidates.append(raw[start : i + 1])
                    break

    all_blocks: list[str] = []
    for m in re.finditer(r"\{", raw):
        s = m.start()
        depth = 0
        for i in range(s, len(raw)):
            if raw[i] == "{":
                depth += 1
            elif raw[i] == "}":
                depth -= 1
                if depth == 0:
                    all_blocks.append(raw[s : i + 1])
                    break
    if all_blocks:
        candidates.append(max(all_blocks, key=len))

    def _identity(x: str) -> str:
        return x

    def _fix_ctrl(x: str) -> str:
        return fix_control_chars(x)

    def _repair(x: str) -> str:
        return repair_json(x)

    def _fix_ctrl_repair(x: str) -> str:
        return fix_control_chars(repair_json(x))

    for cand in candidates:
        for transform in [_identity, _fix_ctrl, _repair, _fix_ctrl_repair]:
            try:
                result = json.loads(transform(cand))
                if isinstance(result, dict):
                    return result
            except Exception:
                continue

    try:
        return json.loads(fix_control_chars(repair_json(raw)))
    except Exception:
        pass

    raise ValueError(
        f"Could not extract valid JSON from model output. "
        f"First 300 chars: {raw[:300]!r}"
    )


# ---------------------------------------------------------------------------
# LLM backend abstraction  (identical protocol to scan.py)
# ---------------------------------------------------------------------------

class LLMBackend(Protocol):
    def call(
        self,
        system: str,
        user: str,
        max_tokens: int,
        temperature: float = 0.0,
        presence_penalty: float = 0.0,
    ) -> tuple[str, str]: ...

    def get_model(self) -> str: ...


class OpenAIBackend:
    def __init__(
        self,
        base_url: str,
        api_key: str,
        model: str | None,
        timeout: float = 120.0,
        azure_deployment: str | None = None,
        azure_api_version: str = "2024-02-01",
        provider_label: str = "openai",
    ):
        import httpx
        from openai import OpenAI, AzureOpenAI

        http_timeout = httpx.Timeout(connect=10.0, read=timeout, write=30.0, pool=10.0)

        if provider_label == "azure":
            if not base_url:
                raise SystemExit(
                    "[azure] --endpoint is required for Azure AI Foundry.\n"
                    "Example: https://my-resource.openai.azure.com"
                )
            self._client = AzureOpenAI(
                azure_endpoint=base_url,
                api_key=api_key,
                api_version=azure_api_version,
                timeout=http_timeout,
            )
            self._model = azure_deployment or model or PROVIDER_DEFAULT_MODELS["azure"]
        else:
            self._client = OpenAI(
                base_url=base_url,
                api_key=api_key or "lm-studio",
                timeout=http_timeout,
            )
            self._model = model

        self._provider = provider_label

    def get_model(self) -> str:
        if self._model:
            return self._model
        try:
            models = self._client.models.list()
            if models.data:
                self._model = models.data[0].id
                return self._model
        except Exception as exc:
            raise RuntimeError(
                f"Could not auto-detect model from server: {exc}\n"
                "Pass --model explicitly."
            )
        raise RuntimeError("No models available. Is the server running?")

    def call(
        self,
        system: str,
        user: str,
        max_tokens: int,
        temperature: float = 0.0,
        presence_penalty: float = 0.0,
    ) -> tuple[str, str]:
        extra: dict[str, Any] = {}
        if presence_penalty != 0.0:
            extra["presence_penalty"] = presence_penalty
        resp = self._client.chat.completions.create(
            model=self.get_model(),
            messages=[
                {"role": "system", "content": system},
                {"role": "user",   "content": user},
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            **extra,
        )
        choice = resp.choices[0]
        return choice.message.content or "", getattr(choice, "finish_reason", "") or ""


class AnthropicBackend:
    def __init__(
        self,
        api_key: str,
        model: str | None,
        base_url: str | None = None,
        timeout: float = 120.0,
    ):
        try:
            import anthropic as _anthropic
        except ImportError:
            raise SystemExit(
                "[anthropic] anthropic SDK not installed.\n"
                "Run: pip install anthropic"
            )
        kwargs: dict[str, Any] = {"api_key": api_key, "timeout": timeout}
        if base_url:
            kwargs["base_url"] = base_url
        self._client = _anthropic.Anthropic(**kwargs)
        self._model  = model or PROVIDER_DEFAULT_MODELS["anthropic"]

    def get_model(self) -> str:
        return self._model

    def call(
        self,
        system: str,
        user: str,
        max_tokens: int,
        temperature: float = 0.0,
        presence_penalty: float = 0.0,
    ) -> tuple[str, str]:
        resp = self._client.messages.create(
            model=self._model,
            max_tokens=max_tokens,
            temperature=temperature,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        content = "".join(
            block.text for block in resp.content if hasattr(block, "text")
        )
        return content, resp.stop_reason or ""


class BedrockBackend:
    def __init__(
        self,
        model: str | None,
        region: str = "us-east-1",
        access_key: str | None = None,
        secret_key: str | None = None,
        session_token: str | None = None,
        profile: str | None = None,
        endpoint_url: str | None = None,
    ):
        try:
            import boto3
        except ImportError:
            raise SystemExit(
                "[bedrock] boto3 not installed.\n"
                "Run: pip install boto3"
            )
        session_kwargs: dict[str, Any] = {}
        if profile:
            session_kwargs["profile_name"] = profile
        session = boto3.Session(**session_kwargs)
        client_kwargs: dict[str, Any] = {"region_name": region}
        if access_key and secret_key:
            client_kwargs["aws_access_key_id"]     = access_key
            client_kwargs["aws_secret_access_key"] = secret_key
            if session_token:
                client_kwargs["aws_session_token"] = session_token
        if endpoint_url:
            client_kwargs["endpoint_url"] = endpoint_url
        self._client = session.client("bedrock-runtime", **client_kwargs)
        self._model  = model or PROVIDER_DEFAULT_MODELS["bedrock"]

    def get_model(self) -> str:
        return self._model

    def call(
        self,
        system: str,
        user: str,
        max_tokens: int,
        temperature: float = 0.0,
        presence_penalty: float = 0.0,
    ) -> tuple[str, str]:
        resp = self._client.converse(
            modelId=self._model,
            system=[{"text": system}],
            messages=[{"role": "user", "content": [{"text": user}]}],
            inferenceConfig={"maxTokens": max_tokens, "temperature": temperature},
        )
        output  = resp["output"]["message"]["content"]
        content = "".join(block.get("text", "") for block in output)
        stop    = resp.get("stopReason", "")
        return content, "length" if stop == "max_tokens" else stop


class GeminiBackend:
    def __init__(
        self,
        api_key: str,
        model: str | None,
        base_url: str | None = None,
        timeout: float = 120.0,
    ):
        try:
            import google.generativeai as genai
        except ImportError:
            raise SystemExit(
                "[gemini] google-generativeai not installed.\n"
                "Run: pip install google-generativeai"
            )
        kwargs: dict[str, Any] = {"api_key": api_key}
        if base_url:
            kwargs["transport"]      = "rest"
            kwargs["client_options"] = {"api_endpoint": base_url}
        genai.configure(**kwargs)
        self._genai   = genai
        self._model   = model or PROVIDER_DEFAULT_MODELS["gemini"]
        self._timeout = timeout

    def get_model(self) -> str:
        return self._model

    def call(
        self,
        system: str,
        user: str,
        max_tokens: int,
        temperature: float = 0.0,
        presence_penalty: float = 0.0,
    ) -> tuple[str, str]:
        import google.generativeai as genai

        gen_cfg = self._genai.types.GenerationConfig(
            max_output_tokens=max_tokens,
            temperature=temperature,
        )
        m = genai.GenerativeModel(
            model_name=self._model,
            system_instruction=system,
            generation_config=gen_cfg,
        )
        response = m.generate_content(user)
        content  = response.text or ""
        try:
            raw_reason    = response.candidates[0].finish_reason.name
            finish_reason = "length" if raw_reason == "MAX_TOKENS" else raw_reason.lower()
        except Exception:
            finish_reason = ""
        return content, finish_reason


# ---------------------------------------------------------------------------
# Backend factory
# ---------------------------------------------------------------------------

def build_backend(args: argparse.Namespace, cfg: dict) -> LLMBackend:
    llm_cfg = cfg.get("llm", {})
    timeout = float(llm_cfg.get("per_request_timeout", 120))

    provider = "lmstudio"
    for name in ("lmstudio", "openai", "anthropic", "bedrock", "azure", "gemini"):
        if getattr(args, name, False):
            provider = name
            break

    endpoint = (
        args.endpoint
        or llm_cfg.get("base_url")
        or PROVIDER_DEFAULTS.get(provider)
    )
    api_key  = args.api_key or llm_cfg.get("api_key", "")
    model    = args.model or llm_cfg.get("model") or PROVIDER_DEFAULT_MODELS.get(provider)

    console.print(
        f"[dim]Backend: {provider.upper()}  |  "
        f"Model: {model or 'auto'}  |  "
        f"Endpoint: {redact_url_credentials(endpoint or 'SDK default')}[/dim]"
    )

    if endpoint:
        endpoint = validate_endpoint_url(endpoint, provider)

    if provider == "lmstudio":
        return OpenAIBackend(
            base_url=endpoint or PROVIDER_DEFAULTS["lmstudio"],
            api_key=api_key or "lm-studio",
            model=model,
            timeout=timeout,
            provider_label="lmstudio",
        )

    if provider == "openai":
        api_key = api_key or os.environ.get("OPENAI_API_KEY", "")
        if not api_key:
            raise SystemExit(
                "[openai] No API key. Use --api-key or set OPENAI_API_KEY."
            )
        return OpenAIBackend(
            base_url=endpoint or PROVIDER_DEFAULTS["openai"],
            api_key=api_key,
            model=model,
            timeout=timeout,
            provider_label="openai",
        )

    if provider == "anthropic":
        api_key = api_key or os.environ.get("ANTHROPIC_API_KEY", "")
        if not api_key:
            raise SystemExit(
                "[anthropic] No API key. Use --api-key or set ANTHROPIC_API_KEY."
            )
        return AnthropicBackend(
            api_key=api_key,
            model=model,
            base_url=endpoint if endpoint != PROVIDER_DEFAULTS["anthropic"] else None,
            timeout=timeout,
        )

    if provider == "bedrock":
        return BedrockBackend(
            model=model,
            region=args.aws_region or llm_cfg.get("aws_region", "us-east-1"),
            access_key=args.aws_access_key or llm_cfg.get("aws_access_key"),
            secret_key=args.aws_secret_key or llm_cfg.get("aws_secret_key"),
            session_token=args.aws_session_token or llm_cfg.get("aws_session_token"),
            profile=args.aws_profile or llm_cfg.get("aws_profile"),
            endpoint_url=endpoint,
        )

    if provider == "azure":
        api_key = api_key or os.environ.get("AZURE_OPENAI_API_KEY", "")
        if not api_key:
            raise SystemExit(
                "[azure] No API key. Use --api-key or set AZURE_OPENAI_API_KEY."
            )
        return OpenAIBackend(
            base_url=endpoint or "",
            api_key=api_key,
            model=model,
            timeout=timeout,
            azure_deployment=args.azure_deployment or llm_cfg.get("azure_deployment"),
            azure_api_version=args.azure_api_version
                              or llm_cfg.get("azure_api_version", "2024-02-01"),
            provider_label="azure",
        )

    if provider == "gemini":
        api_key = (
            api_key
            or os.environ.get("GEMINI_API_KEY", "")
            or os.environ.get("GOOGLE_API_KEY", "")
        )
        if not api_key:
            raise SystemExit(
                "[gemini] No API key. Use --api-key or set GEMINI_API_KEY / GOOGLE_API_KEY."
            )
        return GeminiBackend(
            api_key=api_key,
            model=model,
            base_url=endpoint if endpoint != PROVIDER_DEFAULTS["gemini"] else None,
            timeout=timeout,
        )

    raise SystemExit(f"Unknown provider: {provider}")


# ---------------------------------------------------------------------------
# File collection
# ---------------------------------------------------------------------------

def collect_files(
    root: Path,
    extensions: set[str],
    max_files: int,
    explicit_files: list[str],
) -> list[Path]:
    """
    Return the list of files to scan.

    If explicit_files is provided (e.g. from --files or git diff output) those
    paths are resolved relative to root and validated.  Otherwise the tree
    under root is walked.
    """
    if explicit_files:
        targets: list[Path] = []
        for f in explicit_files:
            p = Path(f)
            if not p.is_absolute():
                p = (root / p).resolve()
            if not p.is_file():
                console.print(f"[yellow]⚠ Skipping (not found): {f}[/yellow]")
                continue
            if p.stat().st_size > MAX_FILE_READ_BYTES:
                console.print(f"[yellow]⚠ Skipping oversized file: {f}[/yellow]")
                continue
            if p.suffix.lower() not in extensions and p.name not in extensions:
                console.print(f"[dim]Skipping unsupported extension: {f}[/dim]")
                continue
            targets.append(p)
        return targets

    found: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            p = Path(dirpath) / fn
            if p.suffix.lower() in extensions or p.name in extensions:
                try:
                    if p.stat().st_size > MAX_FILE_READ_BYTES:
                        console.print(
                            f"[yellow]⚠ Skipping oversized file "
                            f"({p.stat().st_size // 1024} KB): {p}[/yellow]"
                        )
                        continue
                except OSError:
                    continue
                found.append(p)
                if max_files > 0 and len(found) >= max_files:
                    return found
    return found


# ---------------------------------------------------------------------------
# Single-agent LLM call
# ---------------------------------------------------------------------------

def quick_scan_file(
    backend: LLMBackend,
    system_prompt: str,
    rel_path: str,
    content: str,
    max_chars: int,
    max_tokens: int,
    presence_penalty: float,
    retries: int,
) -> dict:
    """
    Run one LLM call for a single file.  Returns a parsed dict with at least:
      decision      — "PASS" | "WARN" | "FAIL" | "ERROR"
      findings      — list of finding dicts
      summary       — one-line human-readable summary string
    Returns {"decision": "ERROR", "findings": [], "summary": "..."} on failure.
    """
    # Clamp file content to stay within context limits
    if len(content) > max_chars:
        half = max_chars // 2
        content = (
            content[:half]
            + f"\n... [truncated {len(content) - max_chars} chars] ...\n"
            + content[-half:]
        )

    # Number lines so finding line references are meaningful
    numbered = "\n".join(
        f"{i+1:>4}: {ln}" for i, ln in enumerate(content.splitlines())
    )
    user_prompt = (
        f"FILE: {rel_path}\n\n"
        f"{numbered}\n\n"
        "Analyse the file above for security vulnerabilities.\n"
        "Respond ONLY with a single valid JSON object matching the schema in your system prompt."
    )

    effective_tokens = max(max_tokens, QUICK_SCAN_MIN_TOKENS)
    last_raw = ""
    last_err = ""

    for attempt in range(retries + 1):
        t0 = time.monotonic()
        try:
            last_raw, finish_reason = backend.call(
                system=system_prompt,
                user=user_prompt,
                max_tokens=effective_tokens,
                temperature=0.0,
                presence_penalty=presence_penalty,
            )
            elapsed = time.monotonic() - t0

            # Detect truncation
            stripped      = last_raw.strip()
            fence_stripped = re.sub(r"```[a-z]*\s*$", "", stripped).rstrip()
            if finish_reason == "length" or (
                fence_stripped and not fence_stripped.endswith("}")
            ):
                raise ValueError(
                    f"Response truncated (finish_reason={finish_reason!r}). "
                    f"Increase --max-tokens (currently {effective_tokens})."
                )

            result = extract_json(last_raw)
            # Normalise to expected schema
            result.setdefault("decision", "PASS")
            result.setdefault("findings", [])
            result.setdefault("summary",  f"Scan complete ({elapsed:.0f}s)")
            return result

        except Exception as exc:
            elapsed  = time.monotonic() - t0
            last_err = str(exc)
            err_type = type(exc).__name__

            is_timeout = (
                any(k in last_err.lower() for k in ("timed out", "timeout"))
                or err_type in ("ReadTimeout", "ConnectTimeout")
            )
            is_conn = (
                any(k in last_err.lower() for k in ("connection", "refused"))
                or "ConnectError" in err_type
            )

            should_retry = attempt < retries and not is_timeout and not is_conn
            if not should_retry:
                break

            nudge = (
                f"Your previous response could not be parsed as JSON. "
                f"Error: {last_err[:150]}. "
                "Output ONLY a valid JSON object. Start with { and end with }."
            )
            user_prompt = nudge   # replace user prompt with correction nudge

    console.print(f"[red]  ✗ quick_scan failed for {rel_path}: {last_err[:200]}[/red]")
    return {
        "decision": "ERROR",
        "findings": [],
        "summary":  f"Scanner error: {last_err[:120]}",
        "_raw":     last_raw,
        "_error":   last_err,
    }


# ---------------------------------------------------------------------------
# Gate decision logic
# ---------------------------------------------------------------------------

def compute_gate_decision(result: dict, warn_only: bool) -> int:
    """
    Derive an exit code from the parsed agent result.

    The model is asked to set result["decision"] directly, but we also
    independently verify by inspecting the findings list so CI pipelines
    cannot be trivially bypassed by a misbehaving model.
    """
    if result.get("decision") == "ERROR":
        return EXIT_ERROR

    findings = result.get("findings", [])

    has_critical_or_high = any(
        f.get("severity", "").upper() in ("CRITICAL", "HIGH")
        and float(f.get("confidence", 0)) >= FAIL_CONFIDENCE_THRESHOLD
        for f in findings
        if isinstance(f, dict)
    )
    has_medium_or_above = any(
        SEVERITY_RANK.get(f.get("severity", "").upper(), 0) >= SEVERITY_RANK["MEDIUM"]
        and float(f.get("confidence", 0)) >= WARN_CONFIDENCE_THRESHOLD
        for f in findings
        if isinstance(f, dict)
    )

    model_decision = str(result.get("decision", "PASS")).upper()

    if has_critical_or_high or model_decision == "FAIL":
        return EXIT_WARN if warn_only else EXIT_FAIL
    if has_medium_or_above or model_decision in ("WARN", "NEEDS_HUMAN"):
        return EXIT_WARN
    return EXIT_PASS


# ---------------------------------------------------------------------------
# CI/CD annotation helpers
# ---------------------------------------------------------------------------

def _ado_severity(severity: str) -> str:
    """Map finding severity to ADO task.logissue type."""
    return "error" if severity.upper() in ("CRITICAL", "HIGH") else "warning"


def emit_ado_annotations(rel_path: str, findings: list[dict]) -> None:
    """Print Azure DevOps ##vso[task.logissue] commands to stdout."""
    for f in findings:
        if not isinstance(f, dict):
            continue
        sev   = f.get("severity", "LOW")
        title = f.get("title", f.get("description", "Security finding"))
        line  = str(f.get("line", f.get("line_number", "")))
        ado_type = _ado_severity(sev)
        line_part = f";linenumber={line}" if line else ""
        # ADO log issue command — deliberately written to stdout
        print(
            f"##vso[task.logissue type={ado_type}"
            f";sourcepath={rel_path}"
            f"{line_part}"
            f";code=SECURITY-{sev.upper()}]"
            f"[{sev}] {title}"
        )


def emit_gha_annotations(rel_path: str, findings: list[dict]) -> None:
    """Print GitHub Actions workflow commands to stdout."""
    for f in findings:
        if not isinstance(f, dict):
            continue
        sev   = f.get("severity", "LOW")
        title = f.get("title", f.get("description", "Security finding"))
        line  = str(f.get("line", f.get("line_number", "")))
        gha_level = "error" if sev.upper() in ("CRITICAL", "HIGH") else "warning"
        line_part = f",line={line}" if line else ""
        # GHA annotation command — deliberately written to stdout
        print(f"::{gha_level} file={rel_path}{line_part}::[{sev}] {title}")


# ---------------------------------------------------------------------------
# Output writers
# ---------------------------------------------------------------------------

def write_per_file_artifacts(
    out_dir: Path,
    rel_path: str,
    result: dict,
    raw_response: str,
    elapsed: float,
    exit_code: int,
) -> None:
    """Write result.json and raw_response.txt for one scanned file."""
    out_dir.mkdir(parents=True, exist_ok=True)

    result_payload = {
        "file":      rel_path,
        "decision":  result.get("decision", "ERROR"),
        "exit_code": exit_code,
        "findings":  result.get("findings", []),
        "summary":   result.get("summary", ""),
        "elapsed_s": round(elapsed, 1),
    }
    atomic_write_text(out_dir / "result.json", json.dumps(result_payload, indent=2))
    atomic_write_text(
        out_dir / "raw_response.txt",
        f"elapsed: {elapsed:.1f}s\n---\n{raw_response}",
    )


def write_rollup(
    results: list[dict],
    out_root: Path,
    overall_exit: int,
) -> None:
    """Write quick_scan_rollup.json and quick_scan_summary.md."""
    rollup = {
        "overall_exit_code": overall_exit,
        "overall_decision":  {
            EXIT_PASS:  "PASS",
            EXIT_WARN:  "WARN",
            EXIT_FAIL:  "FAIL",
            EXIT_ERROR: "ERROR",
        }.get(overall_exit, "UNKNOWN"),
        "total_files": len(results),
        "per_file":    results,
    }
    atomic_write_text(
        out_root / "quick_scan_rollup.json",
        json.dumps(rollup, indent=2),
    )

    # Markdown summary for PR comments
    decision_str = rollup["overall_decision"]
    emoji = {"PASS": "✅", "WARN": "⚠️", "FAIL": "❌", "ERROR": "⚠️"}.get(decision_str, "")
    md: list[str] = [
        f"# {emoji} Quick Security Scan — {decision_str}",
        "",
        f"**Files scanned:** {len(results)}  |  "
        f"FAIL: {sum(1 for r in results if r['exit_code'] == EXIT_FAIL)}  |  "
        f"WARN: {sum(1 for r in results if r['exit_code'] == EXIT_WARN)}  |  "
        f"PASS: {sum(1 for r in results if r['exit_code'] == EXIT_PASS)}  |  "
        f"ERROR: {sum(1 for r in results if r['exit_code'] == EXIT_ERROR)}",
        "",
        "| File | Decision | Findings |",
        "|------|----------|----------|",
    ]
    for r in results:
        decision = r.get("decision", "?")
        n        = len(r.get("findings", []))
        md.append(f"| `{r['file']}` | {decision} | {n} |")

    # Finding detail for non-passing files
    failing = [r for r in results if r.get("exit_code", EXIT_PASS) != EXIT_PASS]
    if failing:
        md += ["", "## Findings requiring attention", ""]
        for r in failing:
            for f in r.get("findings", []):
                if not isinstance(f, dict):
                    continue
                sev   = f.get("severity", "?")
                title = f.get("title", f.get("description", "Finding"))
                line  = f.get("line", f.get("line_number", ""))
                loc   = f"`{r['file']}`" + (f" line {line}" if line else "")
                md.append(f"- **[{sev}]** {title} — {loc}")

    md.append("")
    atomic_write_text(out_root / "quick_scan_summary.md", "\n".join(md))


# ---------------------------------------------------------------------------
# Default agent config (used when no agents_quick.yaml is found)
# ---------------------------------------------------------------------------

DEFAULT_QUICK_SCAN_SYSTEM = """\
You are a senior application security engineer performing a fast triage scan.
Analyse the supplied source file for OWASP Top 10 vulnerabilities, hardcoded
secrets, insecure dependencies, and obvious logic flaws.

Respond ONLY with a single valid JSON object in exactly this schema:

{
  "decision": "PASS" | "WARN" | "FAIL",
  "summary": "<one sentence overall assessment>",
  "findings": [
    {
      "title": "<short finding title>",
      "severity": "CRITICAL" | "HIGH" | "MEDIUM" | "LOW" | "INFO",
      "confidence": 0.0-1.0,
      "line": <integer or null>,
      "description": "<concise explanation of the vulnerability>",
      "remediation": "<concise fix recommendation>"
    }
  ]
}

Rules:
- decision = FAIL if any CRITICAL or HIGH finding has confidence >= 0.7
- decision = WARN if any MEDIUM finding is present or HIGH < 0.7 confidence
- decision = PASS if no significant findings
- findings may be an empty array
- Output ONLY the JSON object — no markdown fences, no explanation, no text outside the braces.
"""


def load_config(config_path_str: str) -> tuple[dict, str]:
    """
    Load agents_quick.yaml if it exists.
    Returns (cfg dict, system_prompt string).
    Falls back to DEFAULT_QUICK_SCAN_SYSTEM if no config is found.
    """
    search_paths = [
        Path(config_path_str),
        Path("agents_quick.yaml"),
        Path("security/agents_quick.yaml"),
        Path(".security/agents_quick.yaml"),
        Path(__file__).parent / "agents_quick.yaml",
    ]

    for candidate in search_paths:
        if candidate.is_file():
            if candidate.stat().st_size > MAX_FILE_READ_BYTES:
                raise SystemExit(f"Config file {candidate} is too large.")
            try:
                raw_cfg = yaml.safe_load(candidate.read_text(encoding="utf-8"))
            except yaml.YAMLError as exc:
                raise SystemExit(f"Could not parse {candidate}: {exc}") from exc
            if not isinstance(raw_cfg, dict):
                raise SystemExit(f"Config {candidate} did not parse as a YAML mapping.")

            # Extract system prompt from agents.quick_scan.system or agents.scan.system
            agents = raw_cfg.get("agents", {})
            system = (
                (agents.get("quick_scan") or {}).get("system")
                or (agents.get("scan") or {}).get("system")
                or DEFAULT_QUICK_SCAN_SYSTEM
            )
            console.print(f"[dim]Config: {candidate}[/dim]")
            return raw_cfg, system

    console.print("[dim]No agents_quick.yaml found — using built-in system prompt[/dim]")
    return {}, DEFAULT_QUICK_SCAN_SYSTEM


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_arg_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        description="Fast single-agent security scanner for CI/CD pipelines",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
EXIT CODES
  0  PASS    No significant findings
  1  WARN    Findings present but below fail threshold
  2  FAIL    Critical/High findings above confidence threshold
  3  ERROR   Scanner error (treat as WARN during rollout)

PROVIDER EXAMPLES
  # LM Studio (default)
  python quick_scan.py src/

  # Scan PR-changed files (Azure DevOps)
  python quick_scan.py $(Build.SourcesDirectory) \\
      --files $(git diff --name-only origin/$(System.PullRequest.TargetBranch))

  # OpenAI
  python quick_scan.py src/ --openai --api-key sk-...

  # Anthropic, warn-only
  python quick_scan.py src/ --anthropic --api-key sk-ant-... --warn-only

  # AWS Bedrock
  python quick_scan.py src/ --bedrock --aws-region us-east-1 --aws-profile prod

  # Azure AI Foundry
  python quick_scan.py src/ --azure \\
      --endpoint https://my-resource.openai.azure.com \\
      --api-key <key> --azure-deployment gpt-4o

  # Gemini + GitHub Actions annotations
  python quick_scan.py src/ --gemini --api-key AIza... --gha
        """,
    )

    # ── Positional ────────────────────────────────────────────────────────────
    ap.add_argument("directory", help="Root directory to scan")

    # ── Provider selection (mutually exclusive) ───────────────────────────────
    pgroup = ap.add_argument_group("LLM Provider  (choose one; default: --lmstudio)")
    px = pgroup.add_mutually_exclusive_group()
    px.add_argument("--lmstudio",  action="store_true", default=False,
                    help="LM Studio local server (default)")
    px.add_argument("--openai",    action="store_true", default=False,
                    help="OpenAI API  (needs --api-key or OPENAI_API_KEY)")
    px.add_argument("--anthropic", action="store_true", default=False,
                    help="Anthropic API  (needs --api-key or ANTHROPIC_API_KEY)")
    px.add_argument("--bedrock",   action="store_true", default=False,
                    help="AWS Bedrock  (uses boto3 credential chain)")
    px.add_argument("--azure",     action="store_true", default=False,
                    help="Azure AI Foundry  (needs --endpoint and --api-key)")
    px.add_argument("--gemini",    action="store_true", default=False,
                    help="Google Gemini  (needs --api-key or GEMINI_API_KEY)")

    # ── Common auth ───────────────────────────────────────────────────────────
    auth = ap.add_argument_group("Common endpoint & auth")
    auth.add_argument("--endpoint",  default="", metavar="URL",
                      help="Override the provider's default API endpoint URL")
    auth.add_argument("--api-key",   default="", metavar="KEY",
                      help="API key (overrides environment variable)")
    auth.add_argument("--model",     default=None,
                      help="Model ID (provider default if omitted)")

    # ── Azure ─────────────────────────────────────────────────────────────────
    az = ap.add_argument_group("Azure AI Foundry  (--azure)")
    az.add_argument("--azure-deployment",  default="", metavar="NAME",
                    help="Azure deployment name")
    az.add_argument("--azure-api-version", default="2024-02-01", metavar="VER",
                    help="Azure OpenAI API version (default: 2024-02-01)")

    # ── Bedrock ───────────────────────────────────────────────────────────────
    bk = ap.add_argument_group("AWS Bedrock  (--bedrock)")
    bk.add_argument("--aws-region",        default="us-east-1", metavar="REGION")
    bk.add_argument("--aws-profile",       default="", metavar="PROFILE")
    bk.add_argument("--aws-access-key",    default="", metavar="KEY")
    bk.add_argument("--aws-secret-key",    default="", metavar="SECRET")
    bk.add_argument("--aws-session-token", default="", metavar="TOKEN")

    # ── Scanner options ───────────────────────────────────────────────────────
    sc = ap.add_argument_group("Scanner options")
    sc.add_argument("--files",      nargs="+", default=[], metavar="FILE",
                    help="Explicit list of files to scan (e.g. from git diff --name-only)")
    sc.add_argument("--config",     default="agents_quick.yaml",
                    help="Path to agents_quick.yaml (auto-searched if not found)")
    sc.add_argument("--out",        default="quick_scan_results",
                    help="Output directory for per-file JSON and rollup (default: quick_scan_results)")
    sc.add_argument("--max-files",  type=int, default=50,
                    help="Max files to scan in directory mode (0 = unlimited, default: 50)")
    sc.add_argument("--max-chars",  type=int, default=QUICK_SCAN_MAX_CHARS,
                    help=f"Max file content chars sent to the model (default: {QUICK_SCAN_MAX_CHARS})")
    sc.add_argument("--max-tokens", type=int, default=QUICK_SCAN_MIN_TOKENS,
                    help=f"Max tokens for the LLM response (default: {QUICK_SCAN_MIN_TOKENS})")
    sc.add_argument("--retries",    type=int, default=1,
                    help="Retry attempts on JSON parse failure (default: 1)")
    sc.add_argument("--extensions", default="",
                    help="Extra extensions comma-separated (e.g. .jsx,.tsx)")

    # ── CI/CD output options ──────────────────────────────────────────────────
    ci = ap.add_argument_group("CI/CD output options")
    ci.add_argument("--warn-only", action="store_true", default=False,
                    help="Never exit 2 — emit WARN instead of FAIL (safe rollout mode)")
    ci.add_argument("--no-ado",    action="store_true", default=False,
                    help="Suppress Azure DevOps ##vso[task.logissue] commands")
    ci.add_argument("--gha",       action="store_true", default=False,
                    help="Emit GitHub Actions ::error / ::warning annotations instead of ADO commands")

    return ap


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    ap   = build_arg_parser()
    args = ap.parse_args()

    # ── Load config ───────────────────────────────────────────────────────────
    cfg, system_prompt = load_config(args.config)
    llm_cfg = cfg.get("llm", {})

    presence_penalty = float(llm_cfg.get("presence_penalty", 0.0))
    max_chars        = args.max_chars
    max_tokens       = args.max_tokens

    # ── Paths ─────────────────────────────────────────────────────────────────
    scan_root = Path(args.directory).resolve()
    if not scan_root.exists():
        raise SystemExit(f"Directory not found: {scan_root}")

    out_root = Path(args.out)
    out_root.mkdir(parents=True, exist_ok=True)

    extra_exts = {e.strip() for e in args.extensions.split(",") if e.strip()}
    extensions = DEFAULT_EXTENSIONS | extra_exts

    # ── Build backend ─────────────────────────────────────────────────────────
    backend = build_backend(args, cfg)
    model   = backend.get_model()

    # ── Collect files ─────────────────────────────────────────────────────────
    targets = collect_files(scan_root, extensions, args.max_files, args.files)
    if not targets:
        console.print("[yellow]No files found to scan.[/yellow]")
        sys.exit(EXIT_PASS)

    # ── Identify active provider ───────────────────────────────────────────────
    active_provider = "lmstudio"
    for name in ("lmstudio", "openai", "anthropic", "bedrock", "azure", "gemini"):
        if getattr(args, name, False):
            active_provider = name
            break

    console.print(Panel(
        f"[bold cyan]Quick Security Scanner[/bold cyan]\n"
        f"Provider:    {active_provider.upper()}\n"
        f"Model:       {model}\n"
        f"Endpoint:    {redact_url_credentials(args.endpoint or PROVIDER_DEFAULTS.get(active_provider) or 'SDK default')}\n"
        f"Files:       {len(targets)}\n"
        f"Output:      {out_root.resolve()}\n"
        f"Max chars:   {max_chars}\n"
        f"Max tokens:  {max_tokens}\n"
        f"Warn-only:   {args.warn_only}\n"
        f"ADO:         {'disabled' if args.no_ado else 'enabled'}\n"
        f"GHA:         {'enabled' if args.gha else 'disabled'}",
        title="quick_scan.py",
    ))

    # ── Scan files ────────────────────────────────────────────────────────────
    all_results: list[dict] = []
    overall_exit = EXIT_PASS

    for i, file_path in enumerate(targets, 1):
        try:
            rel = str(file_path.relative_to(scan_root)).replace("\\", "/")
        except ValueError:
            rel = file_path.name

        console.print(f"\n[bold]({i}/{len(targets)}) {rel}[/bold]")

        # Read file
        try:
            content = file_path.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            console.print(f"  [red]Could not read: {exc}[/red]")
            all_results.append({
                "file": rel, "decision": "ERROR", "exit_code": EXIT_ERROR,
                "findings": [], "summary": str(exc),
            })
            overall_exit = max(overall_exit, EXIT_ERROR)
            continue

        # Build safe output directory name
        safe_name = re.sub(r'[\\/:*?"<>|\x00]+', "_", rel)
        safe_name = safe_name.replace("..", "_").strip(". ")
        if not safe_name:
            safe_name = f"file_{i}"
        try:
            out_dir = validate_output_path(out_root, Path(safe_name))
        except ValueError as exc:
            console.print(f"  [red]Path error: {exc}[/red]")
            all_results.append({
                "file": rel, "decision": "ERROR", "exit_code": EXIT_ERROR,
                "findings": [], "summary": str(exc),
            })
            overall_exit = max(overall_exit, EXIT_ERROR)
            continue

        # Run the scan
        t0 = time.monotonic()
        result   = quick_scan_file(
            backend=backend,
            system_prompt=system_prompt,
            rel_path=rel,
            content=content,
            max_chars=max_chars,
            max_tokens=max_tokens,
            presence_penalty=presence_penalty,
            retries=args.retries,
        )
        elapsed  = time.monotonic() - t0
        exit_code = compute_gate_decision(result, args.warn_only)
        overall_exit = max(overall_exit, exit_code)

        # Write per-file artifacts
        raw = result.pop("_raw", "")
        result.pop("_error", None)
        write_per_file_artifacts(out_dir, rel, result, raw, elapsed, exit_code)

        # Emit CI/CD annotations
        findings = result.get("findings", [])
        if not args.no_ado and not args.gha and findings:
            emit_ado_annotations(rel, findings)
        elif args.gha and findings:
            emit_gha_annotations(rel, findings)

        # Terminal output
        decision = result.get("decision", "ERROR")
        colour   = {"PASS": "green", "WARN": "yellow", "FAIL": "red", "ERROR": "red"}.get(
            decision, "white"
        )
        n = len(findings)
        console.print(
            f"  [{colour}]{decision}[/{colour}]  "
            f"{n} finding(s)  [dim]({elapsed:.0f}s)[/dim]  → {out_dir}"
        )
        if findings:
            for f in findings:
                if not isinstance(f, dict):
                    continue
                sev   = f.get("severity", "?")
                title = f.get("title", f.get("description", "Finding"))
                line  = f.get("line", "")
                loc   = f" (line {line})" if line else ""
                sev_colour = {"CRITICAL": "red", "HIGH": "red", "MEDIUM": "yellow"}.get(
                    sev.upper(), "white"
                )
                console.print(
                    f"    [{sev_colour}][{sev}][/{sev_colour}] {title}{loc}"
                )

        row = {
            "file":      rel,
            "decision":  decision,
            "exit_code": exit_code,
            "findings":  findings,
            "summary":   result.get("summary", ""),
            "elapsed_s": round(elapsed, 1),
        }
        all_results.append(row)

    # ── Rollup ────────────────────────────────────────────────────────────────
    write_rollup(all_results, out_root, overall_exit)

    # ── Final summary ──────────────────────────────────────────────────────────
    decision_label = {
        EXIT_PASS: "PASS", EXIT_WARN: "WARN",
        EXIT_FAIL: "FAIL", EXIT_ERROR: "ERROR",
    }.get(overall_exit, "UNKNOWN")
    colour = {"PASS": "green", "WARN": "yellow", "FAIL": "red", "ERROR": "red"}.get(
        decision_label, "white"
    )
    console.print(
        f"\n[bold]Done.[/bold]  "
        f"[{colour}]{decision_label}[/{colour}]  "
        f"FAIL={sum(1 for r in all_results if r['exit_code'] == EXIT_FAIL)}  "
        f"WARN={sum(1 for r in all_results if r['exit_code'] == EXIT_WARN)}  "
        f"PASS={sum(1 for r in all_results if r['exit_code'] == EXIT_PASS)}  "
        f"ERROR={sum(1 for r in all_results if r['exit_code'] == EXIT_ERROR)}"
    )
    console.print(f"Rollup: {out_root / 'quick_scan_rollup.json'}")
    console.print(f"Summary: {out_root / 'quick_scan_summary.md'}")

    sys.exit(overall_exit)


if __name__ == "__main__":
    main()
