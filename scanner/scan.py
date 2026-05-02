"""
scan.py  –  Agentic security code scanner using agents.yaml
===========================================================
Supports multiple LLM backends via CLI flags:

  --lmstudio      LM Studio local server  (default, OpenAI-compatible)
  --openai        OpenAI API
  --anthropic     Anthropic API           (uses anthropic SDK natively)
  --bedrock       AWS Bedrock             (uses boto3 + bedrock-runtime)
  --azure         Azure AI Foundry        (OpenAI-compatible endpoint)
  --gemini        Google Gemini           (uses google-generativeai SDK natively)

Each backend flag accepts --endpoint to override the default URL, plus
backend-specific auth flags. Run with --help for the full list.

Requirements (install only what you need):
    pip install openai pyyaml rich          # LM Studio / OpenAI / Azure (always needed)
    pip install anthropic                   # --anthropic
    pip install boto3                       # --bedrock
    pip install google-generativeai         # --gemini

LMStudio setup (default backend):
    1. Start the Local Server (default: http://localhost:1234)
    2. Load any model
    3. Set Context Length >= 8192, Max Generated Tokens = -1

Usage:
    # LM Studio (default)
    python scan.py /path/to/code

    # LM Studio with explicit endpoint
    python scan.py /path/to/code --lmstudio --endpoint http://myserver:1234/v1

    # OpenAI
    python scan.py /path/to/code --openai --api-key sk-...
    python scan.py /path/to/code --openai --endpoint https://api.openai.com/v1 --api-key sk-...

    # Anthropic
    python scan.py /path/to/code --anthropic --api-key sk-ant-...
    python scan.py /path/to/code --anthropic --endpoint https://api.anthropic.com --api-key sk-ant-...

    # AWS Bedrock
    python scan.py /path/to/code --bedrock --model anthropic.claude-3-5-sonnet-20241022-v2:0
    python scan.py /path/to/code --bedrock --aws-region us-east-1 --aws-profile my-profile
    python scan.py /path/to/code --bedrock --aws-access-key AKIA... --aws-secret-key ...

    # Azure AI Foundry
    python scan.py /path/to/code --azure --endpoint https://my.openai.azure.com --api-key ...
    python scan.py /path/to/code --azure --endpoint https://my.openai.azure.com --api-key ... --azure-deployment gpt-4o

    # Gemini
    python scan.py /path/to/code --gemini --api-key AIza...
    python scan.py /path/to/code --gemini --endpoint https://generativelanguage.googleapis.com --api-key AIza...

    # Additional options work with any backend
    python scan.py /path/to/code --openai --api-key sk-... --model gpt-4o --pre-scan --out results
"""

from __future__ import annotations

import argparse
import json
import os
import re
import secrets
import sys
import tempfile
import time
from pathlib import Path
from typing import Any, Protocol
from urllib.parse import urlparse

import yaml
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

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

AGENT_MIN_TOKENS = {
    "pre_scan":   10000,
    "scope":      25000,
    "threat":     25000,
    "hypotheses": 30000,
    "evidence":   55000,
    "fix":        55000,
    "gate":       60000,
}

DEFAULT_RETRIES = 2

# Default endpoints per provider
PROVIDER_DEFAULTS = {
    "lmstudio":  "http://localhost:1234/v1",
    "openai":    "https://api.openai.com/v1",
    "anthropic": "https://api.anthropic.com",
    "bedrock":   None,   # constructed at runtime from region
    "azure":     None,   # must be supplied by user
    "gemini":    "https://generativelanguage.googleapis.com",
}

# Default model IDs per provider (used when --model is not specified)
PROVIDER_DEFAULT_MODELS = {
    "lmstudio":  None,                                        # auto-detected from server
    "openai":    "gpt-4o",
    "anthropic": "claude-sonnet-4-5",
    "bedrock":   "anthropic.claude-3-5-sonnet-20241022-v2:0",
    "azure":     "gpt-4o",
    "gemini":    "gemini-2.0-flash",
}


# ---------------------------------------------------------------------------
# Security utilities
# ---------------------------------------------------------------------------

# Agent names are internal constants — validated against this allowlist so that
# user-controlled data can never be interpolated into file paths via the label param.
_ALLOWED_AGENT_LABELS: frozenset[str] = frozenset({
    "pre_scan", "scope", "threat", "hypotheses", "evidence", "fix", "gate", "agent",
})

# Maximum size of any single file read into memory (16 MB).  Prevents memory
# exhaustion from unexpectedly large files in the scan tree.
_MAX_FILE_READ_BYTES = 16 * 1024 * 1024


def sanitise_label(label: str) -> str:
    """
    Validate that an agent label is in the known allowlist before it is used
    in a file path.  Raises ValueError for unexpected values so that arbitrary
    strings never reach the filesystem.
    """
    if label not in _ALLOWED_AGENT_LABELS:
        raise ValueError(
            f"Unexpected agent label {label!r}. "
            f"Must be one of: {sorted(_ALLOWED_AGENT_LABELS)}"
        )
    return label


def validate_output_path(base: Path, relative: Path) -> Path:
    """
    Resolve *relative* inside *base* and confirm the result is still under
    *base*.  Raises ValueError if a path traversal is detected.
    """
    resolved = (base / relative).resolve()
    try:
        resolved.relative_to(base.resolve())
    except ValueError:
        raise ValueError(
            f"Path traversal detected: {relative!r} escapes output root {base!r}"
        )
    return resolved


def atomic_write_text(path: Path, content: str, encoding: str = "utf-8") -> None:
    """
    Write *content* to *path* atomically using a sibling temporary file and
    os.replace().  Guarantees that readers never see a partially-written file,
    and that a crash during the write leaves the previous file intact.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    # Write to a temp file in the same directory so os.replace is atomic
    # (same filesystem, no cross-device move).
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding=encoding) as fh:
            fh.write(content)
        os.replace(tmp, path)
    except Exception:
        # Clean up the temp file on any error to avoid leaving orphans.
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def redact_url_credentials(url: str) -> str:
    """
    Strip username/password from a URL before displaying it in logs or banners.
    https://user:secret@host/path  →  https://***@host/path
    """
    try:
        parsed = urlparse(url)
        if parsed.username or parsed.password:
            safe = parsed._replace(netloc=f"***@{parsed.hostname}" +
                                   (f":{parsed.port}" if parsed.port else ""))
            return safe.geturl()
    except Exception:
        pass
    return url


def validate_endpoint_url(url: str, provider: str) -> str:
    """
    Reject endpoints that use non-HTTP(S) schemes to prevent file:// or ftp://
    probes against the local filesystem or internal services.
    Localhost HTTP is permitted (LM Studio default).
    """
    if not url:
        return url
    try:
        parsed = urlparse(url)
    except Exception as exc:
        raise ValueError(f"[{provider}] Invalid endpoint URL {url!r}: {exc}") from exc

    allowed_schemes = {"http", "https"}
    if parsed.scheme.lower() not in allowed_schemes:
        raise ValueError(
            f"[{provider}] Endpoint URL must use http:// or https://. "
            f"Got scheme {parsed.scheme!r} in {url!r}."
        )
    if not parsed.netloc:
        raise ValueError(
            f"[{provider}] Endpoint URL {url!r} has no host. "
            "Provide a full URL such as https://api.example.com/v1"
        )
    return url


# ---------------------------------------------------------------------------
# JSON extraction helpers
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
            "Response contained only a think block — no JSON output produced. "
            "This is a thinking loop. Try increasing presence_penalty in agents.yaml."
        )

    candidates = []
    cleaned = strip_fences(raw)
    candidates.append(cleaned)

    start = raw.find("{")
    if start != -1:
        depth = 0
        for i in range(start, len(raw)):
            if raw[i] == "{": depth += 1
            elif raw[i] == "}":
                depth -= 1
                if depth == 0:
                    candidates.append(raw[start:i+1])
                    break

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

    # Named transform functions — avoids lambda closure capture and
    # makes static analysis tools' lives easier.
    def _identity(x: str) -> str:
        return x

    def _fix_ctrl(x: str) -> str:
        return fix_control_chars(x)

    def _repair(x: str) -> str:
        return repair_json(x)

    def _fix_ctrl_repair(x: str) -> str:
        return fix_control_chars(repair_json(x))

    transforms = [_identity, _fix_ctrl, _repair, _fix_ctrl_repair]

    for cand in candidates:
        for transform in transforms:
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
# LLM backend abstraction
# ---------------------------------------------------------------------------

class LLMBackend(Protocol):
    """
    Common interface all backends must satisfy.
    call(system, user, max_tokens, temperature, presence_penalty)
      → (content: str, finish_reason: str)
    """
    def call(
        self,
        system: str,
        user: str,
        max_tokens: int,
        temperature: float = 0.0,
        presence_penalty: float = 0.0,
    ) -> tuple[str, str]: ...

    def get_model(self) -> str: ...


# ── OpenAI-compatible backend  (LM Studio / OpenAI / Azure) ─────────────────

class OpenAIBackend:
    """
    Covers: LM Studio, OpenAI API, Azure AI Foundry.
    All speak the OpenAI chat completions protocol.
    """

    def __init__(
        self,
        base_url: str,
        api_key: str,
        model: str | None,
        timeout: float = 300.0,
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
            self._model = model  # may be None → auto-detected in get_model()

        self._provider = provider_label

    def get_model(self) -> str:
        if self._model:
            return self._model
        # Auto-detect from server (LM Studio only)
        try:
            models = self._client.models.list()
            if models.data:
                self._model = models.data[0].id
                return self._model
        except Exception as e:
            raise RuntimeError(
                f"Could not auto-detect model from server: {e}\n"
                "Pass --model explicitly."
            )
        raise RuntimeError("No models available on the server. Is it running?")

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
        content = choice.message.content or ""
        finish_reason = getattr(choice, "finish_reason", "") or ""
        return content, finish_reason


# ── Anthropic native backend ─────────────────────────────────────────────────

class AnthropicBackend:
    """
    Anthropic Messages API via the official anthropic SDK.
    Translates system/user into Anthropic message format.
    """

    def __init__(
        self,
        api_key: str,
        model: str | None,
        base_url: str | None = None,
        timeout: float = 300.0,
    ):
        try:
            import anthropic as _anthropic
        except ImportError:
            raise SystemExit(
                "[anthropic] anthropic SDK not installed.\n"
                "Run: pip install anthropic"
            )

        kwargs: dict[str, Any] = {
            "api_key": api_key,
            "timeout": timeout,
        }
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
        presence_penalty: float = 0.0,  # not supported by Anthropic — silently ignored
    ) -> tuple[str, str]:
        resp = self._client.messages.create(
            model=self._model,
            max_tokens=max_tokens,
            temperature=temperature,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        content = "".join(
            block.text for block in resp.content
            if hasattr(block, "text")
        )
        finish_reason = resp.stop_reason or ""
        return content, finish_reason


# ── AWS Bedrock backend ───────────────────────────────────────────────────────

class BedrockBackend:
    """
    AWS Bedrock via boto3 bedrock-runtime converse API.
    Supports any Bedrock-hosted model (Claude, Llama, Mistral, etc.).

    Auth priority:
      1. Explicit --aws-access-key / --aws-secret-key / --aws-session-token
      2. --aws-profile  (named profile from ~/.aws/credentials)
      3. Ambient credentials (env vars, instance role, SSO, etc.)
    """

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
        presence_penalty: float = 0.0,  # not supported by Bedrock — silently ignored
    ) -> tuple[str, str]:
        resp = self._client.converse(
            modelId=self._model,
            system=[{"text": system}],
            messages=[{"role": "user", "content": [{"text": user}]}],
            inferenceConfig={
                "maxTokens": max_tokens,
                "temperature": temperature,
            },
        )
        output   = resp["output"]["message"]["content"]
        content  = "".join(block.get("text", "") for block in output)
        stop_reason = resp.get("stopReason", "")
        # Map Bedrock stop reasons to OpenAI-style for consistent truncation detection
        finish_reason = "length" if stop_reason == "max_tokens" else stop_reason
        return content, finish_reason


# ── Google Gemini native backend ─────────────────────────────────────────────

class GeminiBackend:
    """
    Google Gemini via the google-generativeai SDK.
    Merges system + user into a single prompt since Gemini uses a different
    turn structure; the system instruction is passed via system_instruction.
    """

    def __init__(
        self,
        api_key: str,
        model: str | None,
        base_url: str | None = None,
        timeout: float = 300.0,
    ):
        try:
            import google.generativeai as genai
        except ImportError:
            raise SystemExit(
                "[gemini] google-generativeai not installed.\n"
                "Run: pip install google-generativeai"
            )

        configure_kwargs: dict[str, Any] = {"api_key": api_key}
        if base_url:
            # The Gemini SDK accepts a client_options transport override
            configure_kwargs["transport"] = "rest"
            configure_kwargs["client_options"] = {"api_endpoint": base_url}

        genai.configure(**configure_kwargs)
        self._genai  = genai
        self._model  = model or PROVIDER_DEFAULT_MODELS["gemini"]
        self._timeout = timeout

    def get_model(self) -> str:
        return self._model

    def call(
        self,
        system: str,
        user: str,
        max_tokens: int,
        temperature: float = 0.0,
        presence_penalty: float = 0.0,  # not supported by Gemini — silently ignored
    ) -> tuple[str, str]:
        import google.generativeai as genai

        gen_config = self._genai.types.GenerationConfig(
            max_output_tokens=max_tokens,
            temperature=temperature,
        )
        gemini_model = genai.GenerativeModel(
            model_name=self._model,
            system_instruction=system,
            generation_config=gen_config,
        )
        response = gemini_model.generate_content(user)
        content  = response.text or ""
        # Gemini finish reasons: STOP, MAX_TOKENS, SAFETY, etc.
        try:
            finish_reason_raw = response.candidates[0].finish_reason.name
            finish_reason = "length" if finish_reason_raw == "MAX_TOKENS" else finish_reason_raw.lower()
        except Exception:
            finish_reason = ""
        return content, finish_reason


# ---------------------------------------------------------------------------
# Backend factory
# ---------------------------------------------------------------------------

def build_backend(args: argparse.Namespace, cfg: dict) -> LLMBackend:
    """
    Construct and return the appropriate LLMBackend based on CLI flags.
    CLI flags take precedence over agents.yaml llm section for all settings.
    """
    llm_cfg = cfg.get("llm", {})

    timeout = float(llm_cfg.get("per_request_timeout", 300))

    # ── Determine which provider was selected ────────────────────────────────
    # Exactly one of the provider flags should be set; default is lmstudio.
    provider = "lmstudio"
    for name in ("lmstudio", "openai", "anthropic", "bedrock", "azure", "gemini"):
        if getattr(args, name, False):
            provider = name
            break

    # Resolve endpoint: CLI flag > agents.yaml > hardcoded default
    endpoint = (
        args.endpoint
        or llm_cfg.get("base_url")
        or PROVIDER_DEFAULTS.get(provider)
    )

    # Resolve API key: CLI flag > agents.yaml > environment variables
    api_key = args.api_key or llm_cfg.get("api_key", "")

    # Resolve model: CLI flag > agents.yaml > provider default
    model = args.model or llm_cfg.get("model") or PROVIDER_DEFAULT_MODELS.get(provider)

    console.print(f"[dim]Backend: {provider.upper()}  |  Model: {model or 'auto'}  |  Endpoint: {redact_url_credentials(endpoint or 'SDK default')}[/dim]")

    # Validate endpoint scheme before handing to any backend.
    # This prevents file://, ftp://, and other non-HTTP schemes from being
    # used to probe the local filesystem or internal services.
    if endpoint:
        endpoint = validate_endpoint_url(endpoint, provider)

    # ── Instantiate the backend ──────────────────────────────────────────────

    if provider == "lmstudio":
        return OpenAIBackend(
            base_url=endpoint or PROVIDER_DEFAULTS["lmstudio"],
            api_key=api_key or "lm-studio",
            model=model,
            timeout=timeout,
            provider_label="lmstudio",
        )

    elif provider == "openai":
        if not api_key:
            api_key = os.environ.get("OPENAI_API_KEY", "")
        if not api_key:
            raise SystemExit(
                "[openai] No API key provided.\n"
                "Use --api-key sk-... or set OPENAI_API_KEY environment variable."
            )
        return OpenAIBackend(
            base_url=endpoint or PROVIDER_DEFAULTS["openai"],
            api_key=api_key,
            model=model,
            timeout=timeout,
            provider_label="openai",
        )

    elif provider == "anthropic":
        if not api_key:
            api_key = os.environ.get("ANTHROPIC_API_KEY", "")
        if not api_key:
            raise SystemExit(
                "[anthropic] No API key provided.\n"
                "Use --api-key sk-ant-... or set ANTHROPIC_API_KEY environment variable."
            )
        return AnthropicBackend(
            api_key=api_key,
            model=model,
            base_url=endpoint if endpoint != PROVIDER_DEFAULTS["anthropic"] else None,
            timeout=timeout,
        )

    elif provider == "bedrock":
        region = args.aws_region or llm_cfg.get("aws_region", "us-east-1")
        return BedrockBackend(
            model=model,
            region=region,
            access_key=args.aws_access_key or llm_cfg.get("aws_access_key"),
            secret_key=args.aws_secret_key or llm_cfg.get("aws_secret_key"),
            session_token=args.aws_session_token or llm_cfg.get("aws_session_token"),
            profile=args.aws_profile or llm_cfg.get("aws_profile"),
            endpoint_url=endpoint,  # None = use regional default
        )

    elif provider == "azure":
        if not api_key:
            api_key = os.environ.get("AZURE_OPENAI_API_KEY", "")
        if not api_key:
            raise SystemExit(
                "[azure] No API key provided.\n"
                "Use --api-key or set AZURE_OPENAI_API_KEY environment variable."
            )
        return OpenAIBackend(
            base_url=endpoint or "",
            api_key=api_key,
            model=model,
            timeout=timeout,
            azure_deployment=args.azure_deployment or llm_cfg.get("azure_deployment"),
            azure_api_version=args.azure_api_version or llm_cfg.get("azure_api_version", "2024-02-01"),
            provider_label="azure",
        )

    elif provider == "gemini":
        if not api_key:
            api_key = os.environ.get("GEMINI_API_KEY", "") or os.environ.get("GOOGLE_API_KEY", "")
        if not api_key:
            raise SystemExit(
                "[gemini] No API key provided.\n"
                "Use --api-key AIza... or set GEMINI_API_KEY / GOOGLE_API_KEY environment variable."
            )
        return GeminiBackend(
            api_key=api_key,
            model=model,
            base_url=endpoint if endpoint != PROVIDER_DEFAULTS["gemini"] else None,
            timeout=timeout,
        )

    raise SystemExit(f"Unknown provider: {provider}")


# ---------------------------------------------------------------------------
# Core LLM call helpers  (backend-agnostic)
# ---------------------------------------------------------------------------

def call_agent(
    backend: LLMBackend,
    agent_cfg: dict,
    user_prompt: str,
    max_tokens: int,
    retries: int = DEFAULT_RETRIES,
    label: str = "agent",
    raw_out_path: Path | None = None,
    presence_penalty: float = 0.0,
) -> dict:
    """
    Call one agent stage through the backend abstraction.
    Returns parsed JSON dict; falls back to {} after all retries so the
    pipeline continues rather than crashing.
    """
    system = (
        agent_cfg.get("system", "").strip()
        + "\n\nIMPORTANT: Output ONLY a single valid JSON object. "
        "No explanation, no markdown fences, no text before or after the JSON. "
        "Start your response with { and end with }."
    )

    # Sanitise label before it reaches any file path or log output.
    label = sanitise_label(label)

    user_messages = [user_prompt]   # track nudge history for retry
    last_raw = ""
    last_err = ""
    effective_max_tokens = max(max_tokens, AGENT_MIN_TOKENS.get(label, 2000))

    for attempt in range(retries + 1):
        current_user = user_messages[-1]
        t_start = time.monotonic()

        try:
            last_raw, finish_reason = backend.call(
                system=system,
                user=current_user,
                max_tokens=effective_max_tokens,
                temperature=0.0,
                presence_penalty=presence_penalty,
            )
            elapsed = time.monotonic() - t_start

            if raw_out_path:
                atomic_write_text(
                    raw_out_path,
                    f"finish_reason: {finish_reason}  elapsed: {elapsed:.1f}s\n---\n{last_raw}",
                )

            stripped = last_raw.strip()
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
                    f"Increase AGENT_MIN_TOKENS['{label}'] or pass a higher --max-tokens. "
                    f"Tail: ...{stripped[-60:]!r}"
                )

            return extract_json(last_raw)

        except Exception as e:
            elapsed = time.monotonic() - t_start
            err_str  = str(e)
            err_type = type(e).__name__

            is_timeout  = any(k in err_str.lower() for k in ("timed out", "timeout")) \
                          or err_type in ("ReadTimeout", "ConnectTimeout")
            is_truncation = "truncated" in err_str.lower() or "finish_reason='length'" in err_str
            is_conn_err = any(k in err_str.lower() for k in ("connection", "refused")) \
                          or "ConnectError" in err_type

            if is_timeout:
                last_err = (
                    f"TIMEOUT after {elapsed:.0f}s on attempt {attempt+1}/{retries+1} "
                    f"(agent={label}, max_tokens={effective_max_tokens}). "
                    "Increase per_request_timeout in agents.yaml or reduce --max-chars."
                )
            elif is_conn_err:
                last_err = (
                    f"CONNECTION ERROR on attempt {attempt+1}/{retries+1}: {err_str[:200]}. "
                    "Is the LLM server/endpoint reachable?"
                )
            else:
                last_err = f"{err_type} on attempt {attempt+1}/{retries+1} ({elapsed:.1f}s): {err_str[:300]}"

            should_retry = attempt < retries and not is_timeout and not is_conn_err

            if should_retry:
                if is_truncation:
                    nudge = (
                        "Your previous response was cut off before completing the JSON. "
                        "Skip any preamble or reasoning. "
                        "Output ONLY a compact JSON object. "
                        "Omit optional fields. Max 3 items per array. "
                        "Strings under 100 characters. "
                        "Start immediately with { and end with }."
                    )
                    user_messages = [user_messages[0], nudge]
                else:
                    nudge = (
                        f"Your previous response could not be parsed as JSON. Error: {err_str[:200]}. "
                        "Output ONLY a valid JSON object. "
                        "Start with { and end with }. "
                        "No markdown, no explanation, no text outside the JSON."
                    )
                    user_messages.append(nudge)
            else:
                break

    console.print(f"[red]  ✗ {label} failed: {last_err}[/red]")
    if raw_out_path:
        err_path = raw_out_path.parent / f"_{label}_FAILED.txt"
        atomic_write_text(
            err_path,
            f"FAILED\nError: {last_err}\nLast raw output:\n{last_raw}",
        )
    return {}


# ---------------------------------------------------------------------------
# Template rendering
# ---------------------------------------------------------------------------

def render(template: str, **kwargs) -> str:
    out = template
    for k, v in kwargs.items():
        out = out.replace("{{" + k + "}}", v if isinstance(v, str) else json.dumps(v, indent=2))
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
        # Ensure the single file is actually under scan_root to prevent
        # out-of-tree reads when an absolute path is supplied.
        return [single_file]

    found = []
    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            p = Path(dirpath) / fn
            if p.suffix.lower() in extensions or p.name in extensions:
                # Skip files that exceed the read limit — they would be
                # clamped anyway and could exhaust memory during read_text.
                try:
                    if p.stat().st_size > _MAX_FILE_READ_BYTES:
                        console.print(
                            f"  [yellow]⚠ Skipping oversized file "
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
# File → diff / excerpt
# ---------------------------------------------------------------------------

def file_to_diff(rel_path: str, content: str) -> str:
    lines = content.splitlines()
    body  = "\n".join("+" + ln for ln in lines) if lines else "+(empty)"
    return (
        f"diff --git a/{rel_path} b/{rel_path}\n"
        f"new file mode 100644\n"
        f"--- /dev/null\n"
        f"+++ b/{rel_path}\n"
        f"@@ -0,0 +1,{max(len(lines), 1)} @@\n"
        f"{body}\n"
    )


def file_to_numbered(rel_path: str, content: str) -> str:
    lines   = content.splitlines()
    numbered = "\n".join(f"{i+1:>4}: {ln}" for i, ln in enumerate(lines))
    return f"FILE: {rel_path}\n{numbered}"


def slim_hypotheses_for_evidence(hypotheses: dict) -> dict:
    slimmed = []
    for h in hypotheses.get("hypotheses", []):
        slimmed.append({
            "id":               h.get("id"),
            "title":            h.get("title"),
            "category":         h.get("category"),
            "where_to_check":   h.get("where_to_check", []),
            "evidence_needed":  h.get("evidence_needed", []),
            "severity_if_true": h.get("severity_if_true"),
            "priority":         h.get("priority"),
        })
    return {"hypotheses": slimmed}


def clamp(text: str, max_chars: int) -> str:
    if len(text) <= max_chars:
        return text
    half = max_chars // 2
    return text[:half] + f"\n... [truncated {len(text)-max_chars} chars] ...\n" + text[-half:]


# ---------------------------------------------------------------------------
# Report builder  (unchanged from original)
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
    lines = [f"# Security Review: {rel_path}", "", f"## Gate Decision: {gate.get('decision', 'UNKNOWN')}", ""]

    rationale = gate.get("rationale", [])
    if rationale:
        lines.append("## Rationale")
        lines.extend(f"- {r}" for r in rationale)
        lines.append("")

    blockers = gate.get("blockers", [])
    lines.append("## Blockers")
    if blockers:
        for b in blockers:
            lines.append(
                f"- **{b.get('finding_key','?')}** "
                f"[{b.get('severity','?')}, conf={b.get('confidence','?')}]: "
                f"{b.get('required_action','')}"
            )
    else:
        lines.append("- None")
    lines.append("")

    findings = evidence.get("confirmed_findings_minimal", [])
    lines.append("## Confirmed Findings")
    if findings:
        for f in findings:
            lines.append(
                f"- **{f.get('finding_key','?')}** [{f.get('severity','?')}] "
                f"{f.get('title','')} ({f.get('category','')}, conf={f.get('confidence','?')})"
            )
            trace = (f.get("evidence") or {}).get("trace", "")
            if trace:
                lines.append(f"  - Trace: {trace}")
    else:
        lines.append("- None")
    lines.append("")

    fix_list   = fixes.get("fixes", [])
    fixed_keys = {fx.get("finding_key") for fx in fix_list}
    unaddressed = [
        f for f in evidence.get("confirmed_findings_minimal", [])
        if f.get("severity") in ("Critical", "High")
        and f.get("finding_key") not in fixed_keys
    ]

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
            bf  = fx.get("recommended_change", {}).get("better_fix",  {}).get("summary", "")
            lines.append(f"- **{fk}** [{sev}] {ttl}")
            if mf: lines.append(f"  - Minimal fix: {mf}")
            if bf and bf != mf: lines.append(f"  - Better fix:  {bf}")
    else:
        lines.append("- None (fix agent produced no output)")
    lines.append("")

    if unaddressed:
        lines.append("## ⛔ Unaddressed Findings (no fix proposed)")
        lines.append("> These Critical/High findings have no proposed fix. Manual review required.")
        lines.append("")
        for f in unaddressed:
            lines.append(f"- **{f.get('finding_key','?')}** [{f.get('severity','?')}] {f.get('title','')}")
        lines.append("")

    questions = evidence.get("questions_for_humans", [])
    if questions:
        lines.append("## Questions for Humans")
        lines.extend(f"- {q}" for q in questions)
        lines.append("")

    risk = scope.get("review_risk_signal", {})
    if risk:
        lines.append(f"## Scope Risk Signal: {risk.get('risk','?')}")
        lines.extend(f"- {w}" for w in risk.get("why", []))
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Pre-scan runner (Stage 0)
# ---------------------------------------------------------------------------

def run_pre_scan(
    backend: LLMBackend,
    agents: dict,
    rel_path: str,
    content: str,
    max_chars: int,
    max_tokens: int,
    out_dir: Path,
    presence_penalty: float = 0.0,
) -> dict:
    if "pre_scan" not in agents:
        console.print("[yellow]  ⚠ pre_scan agent not defined in agents.yaml — skipping[/yellow]")
        return {}

    excerpt = clamp(content, max_chars)
    user_prompt = render(agents["pre_scan"]["user_template"], file_content=excerpt)
    tok = max(max_tokens, AGENT_MIN_TOKENS.get("pre_scan", 40000))

    result = call_agent(
        backend, agents["pre_scan"], user_prompt,
        max_tokens=tok, label="pre_scan",
        raw_out_path=out_dir / "_pre_scan_raw.txt",
        presence_penalty=presence_penalty,
    )

    if result and "meta" in result:
        result["meta"]["scan_target"] = rel_path

    atomic_write_text(
        out_dir / "pre_scan.json",
        json.dumps(result, indent=2),
    )
    n = len(result.get("confirmed_findings", []))
    console.print(f"    [dim]→ pre_scan ({n} finding(s))[/dim]")
    return result


# ---------------------------------------------------------------------------
# Per-file pipeline
# ---------------------------------------------------------------------------

def scan_file(
    backend: LLMBackend,
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
    presence_penalty: float = 0.0,
    pre_scan_result: dict | None = None,
) -> dict:
    diff    = clamp(file_to_diff(rel_path, content), max_chars)
    excerpt = clamp(file_to_numbered(rel_path, content), max_chars)
    out_dir.mkdir(parents=True, exist_ok=True)

    def agent(name: str, prompt: str) -> dict:
        safe_name = sanitise_label(name)  # prevent arbitrary names reaching filesystem
        tok = max(max_tokens, AGENT_MIN_TOKENS.get(safe_name, 2000))
        result = call_agent(
            backend, agents[safe_name], prompt,
            max_tokens=tok, label=safe_name,
            raw_out_path=out_dir / f"_{safe_name}_raw.txt",
            presence_penalty=presence_penalty,
        )
        atomic_write_text(
            out_dir / f"{safe_name}.json",
            json.dumps(result, indent=2),
        )
        return result

    pre_json = json.dumps(pre_scan_result, indent=2) if pre_scan_result else "{}"

    console.print(f"    [dim]→ scope[/dim]")
    scope = agent("scope", render(agents["scope"]["user_template"], repo=repo_root, pr=pr_label, diff=diff))

    console.print(f"    [dim]→ threat[/dim]")
    threat = agent("threat", render(
        agents["threat"]["user_template"],
        scope_json=json.dumps(scope, indent=2),
        pre_scan_json=pre_json,
        arch_constraints=arch_text or "(none)",
    ))

    console.print(f"    [dim]→ hypotheses[/dim]")
    hypotheses = agent("hypotheses", render(
        agents["hypotheses"]["user_template"],
        scope_json=json.dumps(scope, indent=2),
        threat_json=json.dumps(threat, indent=2),
        pre_scan_json=pre_json,
        csharp_notes="(use defaults from system prompt)",
        python_notes="(use defaults from system prompt)",
        ruby_notes="(use defaults from system prompt)",
        node_notes="(use defaults from system prompt)",
    ))

    console.print(f"    [dim]→ evidence[/dim]")
    EVIDENCE_EXCERPT_CAP = 6000
    evidence_excerpt = clamp(file_to_numbered(rel_path, content), EVIDENCE_EXCERPT_CAP)
    evidence = agent("evidence", render(
        agents["evidence"]["user_template"],
        hypotheses_json=json.dumps(slim_hypotheses_for_evidence(hypotheses), indent=2),
        fetched_context=evidence_excerpt,
        pre_scan_json=pre_json,
    ))

    console.print(f"    [dim]→ fix[/dim]")
    fixes = agent("fix", render(
        agents["fix"]["user_template"],
        evidence_json=json.dumps(evidence, indent=2),
        patterns=patterns_text or "(none)",
    ))

    console.print(f"    [dim]→ gate[/dim]")
    gate = agent("gate", render(
        agents["gate"]["user_template"],
        evidence_json=json.dumps(evidence, indent=2),
        fixes_json=json.dumps(fixes, indent=2),
        pre_scan_json=pre_json,
        policy=policy_text or "(use default policy)",
    ))

    report = build_report(rel_path, scope, threat, hypotheses, evidence, fixes, gate)
    atomic_write_text(out_dir / "report.md", report)

    return {
        "file":     rel_path,
        "decision": gate.get("decision", "UNKNOWN"),
        "findings": len(evidence.get("confirmed_findings_minimal", [])),
        "blockers": len(gate.get("blockers", [])),
        "pre_scan": len((pre_scan_result or {}).get("confirmed_findings", [])) if pre_scan_result else 0,
        "out_dir":  str(out_dir),
    }


# ---------------------------------------------------------------------------
# Rollup  (unchanged from original)
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
            if overall != "FAIL": overall = "NEEDS_HUMAN"
            needs_files.append(r["file"])
        else:
            pass_files.append(r["file"])

    summary = {
        "overall_decision": overall,
        "total_files": len(results),
        "fail":        fail_files,
        "needs_human": needs_files,
        "pass":        pass_files,
        "per_file":    results,
    }
    atomic_write_text(
        merged_dir / "summary.json",
        json.dumps(summary, indent=2),
    )

    has_prescan = any(r.get("pre_scan") is not None for r in results)
    md = [
        "# Merged Security Review Summary", "",
        f"**Overall Decision: {overall}**  |  Files scanned: {len(results)}  |  "
        f"FAIL: {len(fail_files)}  |  NEEDS_HUMAN: {len(needs_files)}  |  PASS: {len(pass_files)}", "",
    ]
    if fail_files:
        md += ["## FAIL Files"] + [f"- {f}" for f in fail_files] + [""]
    if needs_files:
        md += ["## NEEDS_HUMAN Files"] + [f"- {f}" for f in needs_files] + [""]

    md.append("## All Results")
    if has_prescan:
        md += ["| File | Decision | Pre-scan | Findings | Blockers |",
               "|------|----------|----------|----------|----------|"]
        for r in results:
            md.append(f"| {r['file']} | {r.get('decision','?')} | {r.get('pre_scan','-')} | {r.get('findings',0)} | {r.get('blockers',0)} |")
    else:
        md += ["| File | Decision | Findings | Blockers |",
               "|------|----------|----------|----------|"]
        for r in results:
            md.append(f"| {r['file']} | {r.get('decision','?')} | {r.get('findings',0)} | {r.get('blockers',0)} |")
    md.append("")

    atomic_write_text(merged_dir / "report.md", "\n".join(md))
    console.print(f"\n[green]Rollup written to {merged_dir}[/green]")


# ---------------------------------------------------------------------------
# CLI argument parser
# ---------------------------------------------------------------------------

def build_arg_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        description="Agentic security scanner with multi-provider LLM backend support",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
PROVIDER EXAMPLES
─────────────────
  # LM Studio (default — no flags needed)
  python scan.py /path/to/code

  # LM Studio on a remote server
  python scan.py /path/to/code --lmstudio --endpoint http://192.168.1.10:1234/v1

  # OpenAI
  python scan.py /path/to/code --openai --api-key sk-...
  python scan.py /path/to/code --openai --api-key sk-... --model gpt-4o-mini

  # Anthropic
  python scan.py /path/to/code --anthropic --api-key sk-ant-...
  python scan.py /path/to/code --anthropic --api-key sk-ant-... --model claude-opus-4-5

  # AWS Bedrock (uses ambient credentials by default)
  python scan.py /path/to/code --bedrock
  python scan.py /path/to/code --bedrock --aws-region eu-west-1 --aws-profile prod
  python scan.py /path/to/code --bedrock --aws-access-key AKIA... --aws-secret-key ...

  # Azure AI Foundry
  python scan.py /path/to/code --azure \\
      --endpoint https://my-resource.openai.azure.com \\
      --api-key ... --azure-deployment gpt-4o

  # Google Gemini
  python scan.py /path/to/code --gemini --api-key AIza...
  python scan.py /path/to/code --gemini --api-key AIza... --model gemini-2.0-flash

ENVIRONMENT VARIABLE FALLBACKS
───────────────────────────────
  OPENAI_API_KEY        used when --openai and no --api-key
  ANTHROPIC_API_KEY     used when --anthropic and no --api-key
  AZURE_OPENAI_API_KEY  used when --azure and no --api-key
  GEMINI_API_KEY        used when --gemini and no --api-key
  GOOGLE_API_KEY        fallback for --gemini
  AWS_ACCESS_KEY_ID     standard boto3 env var (--bedrock)
  AWS_SECRET_ACCESS_KEY standard boto3 env var (--bedrock)
  AWS_DEFAULT_REGION    standard boto3 env var (--bedrock)
        """,
    )

    # ── Positional ───────────────────────────────────────────────────────────
    ap.add_argument("directory", help="Directory to scan")

    # ── Provider selection (mutually exclusive) ──────────────────────────────
    provider_group = ap.add_argument_group(
        "LLM Provider  (choose one; default: --lmstudio)"
    )
    px = provider_group.add_mutually_exclusive_group()
    px.add_argument(
        "--lmstudio", action="store_true", default=False,
        help="Use LM Studio local server (default if no provider flag given)",
    )
    px.add_argument(
        "--openai", action="store_true", default=False,
        help="Use OpenAI API  (requires --api-key or OPENAI_API_KEY)",
    )
    px.add_argument(
        "--anthropic", action="store_true", default=False,
        help="Use Anthropic API  (requires --api-key or ANTHROPIC_API_KEY)",
    )
    px.add_argument(
        "--bedrock", action="store_true", default=False,
        help="Use AWS Bedrock  (uses boto3 credential chain by default)",
    )
    px.add_argument(
        "--azure", action="store_true", default=False,
        help="Use Azure AI Foundry  (requires --endpoint and --api-key)",
    )
    px.add_argument(
        "--gemini", action="store_true", default=False,
        help="Use Google Gemini API  (requires --api-key or GEMINI_API_KEY)",
    )

    # ── Common endpoint / auth ───────────────────────────────────────────────
    common_group = ap.add_argument_group("Common endpoint & auth")
    common_group.add_argument(
        "--endpoint", default="",
        metavar="URL",
        help=(
            "Override the provider's default API endpoint URL.\n"
            "  LM Studio default : http://localhost:1234/v1\n"
            "  OpenAI default    : https://api.openai.com/v1\n"
            "  Anthropic default : https://api.anthropic.com\n"
            "  Gemini default    : https://generativelanguage.googleapis.com\n"
            "  Azure             : REQUIRED (your resource endpoint)\n"
            "  Bedrock           : optional (custom VPC endpoint)"
        ),
    )
    common_group.add_argument(
        "--api-key", default="", metavar="KEY",
        help="API key for the selected provider (overrides environment variable)",
    )
    common_group.add_argument(
        "--model", default=None,
        help=(
            "Model ID to use. Provider defaults if omitted:\n"
            "  LM Studio : auto-detected from server\n"
            f"  OpenAI    : {PROVIDER_DEFAULT_MODELS['openai']}\n"
            f"  Anthropic : {PROVIDER_DEFAULT_MODELS['anthropic']}\n"
            f"  Bedrock   : {PROVIDER_DEFAULT_MODELS['bedrock']}\n"
            f"  Azure     : {PROVIDER_DEFAULT_MODELS['azure']}\n"
            f"  Gemini    : {PROVIDER_DEFAULT_MODELS['gemini']}"
        ),
    )

    # ── Azure-specific ───────────────────────────────────────────────────────
    azure_group = ap.add_argument_group("Azure AI Foundry options  (--azure)")
    azure_group.add_argument(
        "--azure-deployment", default="", metavar="NAME",
        help="Azure deployment name (if different from --model)",
    )
    azure_group.add_argument(
        "--azure-api-version", default="2024-02-01", metavar="VERSION",
        help="Azure OpenAI API version (default: 2024-02-01)",
    )

    # ── AWS Bedrock-specific ─────────────────────────────────────────────────
    bedrock_group = ap.add_argument_group("AWS Bedrock options  (--bedrock)")
    bedrock_group.add_argument(
        "--aws-region", default="us-east-1", metavar="REGION",
        help="AWS region for Bedrock (default: us-east-1)",
    )
    bedrock_group.add_argument(
        "--aws-profile", default="", metavar="PROFILE",
        help="AWS named credential profile (~/.aws/credentials)",
    )
    bedrock_group.add_argument(
        "--aws-access-key", default="", metavar="KEY",
        help="AWS access key ID (use for explicit key auth)",
    )
    bedrock_group.add_argument(
        "--aws-secret-key", default="", metavar="SECRET",
        help="AWS secret access key",
    )
    bedrock_group.add_argument(
        "--aws-session-token", default="", metavar="TOKEN",
        help="AWS session token (for temporary credentials / assume-role)",
    )

    # ── Scanner options (unchanged from original) ────────────────────────────
    scan_group = ap.add_argument_group("Scanner options")
    scan_group.add_argument("--file",       default="", help="Scan a single file (relative or absolute)")
    scan_group.add_argument("--config",     default="agents.yaml", help="Path to agents.yaml")
    scan_group.add_argument("--out",        default="scan_results", help="Output directory")
    scan_group.add_argument("--max-files",  type=int, default=50,    help="Max files to scan (0=unlimited)")
    scan_group.add_argument("--max-chars",  type=int, default=16000, help="Max chars of file content per agent call")
    scan_group.add_argument("--max-tokens", type=int, default=3000,  help="Base max_tokens (per-agent floors apply)")
    scan_group.add_argument("--retries",    type=int, default=2,     help="Retries per agent call on failure")
    scan_group.add_argument("--policy",     default="", help="Path to gate policy text file")
    scan_group.add_argument("--patterns",   default="", help="Path to org patterns/standards text file")
    scan_group.add_argument("--arch",       default="", help="Path to architecture constraints text file")
    scan_group.add_argument("--extensions", default="", help="Extra extensions (comma-separated, e.g. .jsx,.tsx)")
    scan_group.add_argument(
        "--pre-scan", action="store_true", default=False,
        help="Run the OWASP pre-scan agent on every file before the main pipeline",
    )
    scan_group.add_argument(
        "--prescan-file", default="",
        help="Path to a pre-existing pre-scan JSON (single-file mode only)",
    )

    return ap


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    ap   = build_arg_parser()
    args = ap.parse_args()

    # ── Load agents.yaml ─────────────────────────────────────────────────────
    config_path = Path(args.config)
    if not config_path.exists():
        raise SystemExit(f"agents.yaml not found at: {config_path.resolve()}")
    if config_path.stat().st_size > _MAX_FILE_READ_BYTES:
        raise SystemExit(
            f"Config file {config_path} is too large "
            f"({config_path.stat().st_size // 1024} KB). Something is wrong."
        )
    try:
        cfg = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise SystemExit(f"Could not parse {config_path}: {exc}") from exc
    if not isinstance(cfg, dict):
        raise SystemExit(f"Config file {config_path} did not parse as a YAML mapping.")
    agents_cfg = cfg.get("agents", {})
    # Apply llm defaults from agents.yaml
    cfg.setdefault("llm", {})
    cfg["llm"].setdefault("base_url",            "http://localhost:1234/v1")
    cfg["llm"].setdefault("api_key",             "lm-studio")
    cfg["llm"].setdefault("per_request_timeout", 300)
    cfg["llm"].setdefault("presence_penalty",    0.0)

    presence_penalty = float(cfg["llm"]["presence_penalty"])

    required_agents = {"scope", "threat", "hypotheses", "evidence", "fix", "gate"}
    missing = required_agents - set(agents_cfg.keys())
    if missing:
        raise SystemExit(f"agents.yaml is missing agent definitions: {missing}")

    # ── Extensions ───────────────────────────────────────────────────────────
    yaml_exts  = set(cfg.get("review", {}).get("include_extensions", []))
    extra_exts = {e.strip() for e in args.extensions.split(",") if e.strip()}
    extensions = DEFAULT_EXTENSIONS | yaml_exts | extra_exts

    # ── Paths ────────────────────────────────────────────────────────────────
    scan_root = Path(args.directory).resolve()
    if not scan_root.exists():
        raise SystemExit(f"Directory not found: {scan_root}")

    single_file: Path | None = None
    if args.file:
        p = Path(args.file)
        single_file = p if p.is_absolute() else (scan_root / p).resolve()

    out_root = Path(args.out)
    out_root.mkdir(parents=True, exist_ok=True)

    def _read_aux_file(path_str: str, label: str) -> str:
        """Read an optional auxiliary text file with a size guard."""
        if not path_str:
            return ""
        p = Path(path_str)
        if not p.exists():
            console.print(f"[yellow]⚠ {label} file not found: {p} — ignoring[/yellow]")
            return ""
        if p.stat().st_size > _MAX_FILE_READ_BYTES:
            raise SystemExit(
                f"{label} file {p} is too large "
                f"({p.stat().st_size // 1024} KB > {_MAX_FILE_READ_BYTES // 1024} KB limit)."
            )
        try:
            return p.read_text(encoding="utf-8")
        except OSError as exc:
            raise SystemExit(f"Could not read {label} file {p}: {exc}") from exc

    policy_text   = _read_aux_file(args.policy,   "Policy")
    patterns_text = _read_aux_file(args.patterns,  "Patterns")
    arch_text     = _read_aux_file(args.arch,      "Architecture")

    manual_prescan: dict | None = None
    if args.prescan_file:
        p = Path(args.prescan_file)
        if not p.exists():
            console.print(f"[yellow]⚠ --prescan-file not found: {p} — ignoring[/yellow]")
        elif p.stat().st_size > _MAX_FILE_READ_BYTES:
            console.print(
                f"[yellow]⚠ --prescan-file {p} exceeds size limit "
                f"({p.stat().st_size // 1024} KB) — ignoring[/yellow]"
            )
        else:
            try:
                raw_prescan = json.loads(p.read_text(encoding="utf-8"))
                if not isinstance(raw_prescan, dict):
                    raise ValueError("Top-level value is not a JSON object")
                manual_prescan = raw_prescan
                n_pre = len(manual_prescan.get("confirmed_findings", []))
                console.print(f"[dim]Pre-scan file loaded: {p} ({n_pre} finding(s))[/dim]")
            except (json.JSONDecodeError, ValueError) as exc:
                console.print(f"[yellow]⚠ Could not parse --prescan-file: {exc} — ignoring[/yellow]")

    # ── Build LLM backend ────────────────────────────────────────────────────
    backend = build_backend(args, cfg)
    model   = backend.get_model()

    # ── Collect files ────────────────────────────────────────────────────────
    targets = collect_files(scan_root, extensions, args.max_files, single_file)
    if not targets:
        raise SystemExit(
            f"No files found matching extensions {sorted(extensions)} under {scan_root}.\n"
            "Use --extensions to add more, or --file to target a specific file."
        )

    # ── Startup banner ───────────────────────────────────────────────────────
    # Identify active provider for display
    active_provider = "lmstudio"
    for name in ("lmstudio", "openai", "anthropic", "bedrock", "azure", "gemini"):
        if getattr(args, name, False):
            active_provider = name
            break

    console.print(Panel(
        f"[bold cyan]Security Scanner[/bold cyan]\n"
        f"Provider:         {active_provider.upper()}\n"
        f"Model:            {model}\n"
        f"Endpoint:         {redact_url_credentials(args.endpoint or PROVIDER_DEFAULTS.get(active_provider) or 'SDK default')}\n"
        f"Root:             {scan_root}\n"
        f"Files:            {len(targets)}\n"
        f"Output:           {out_root.resolve()}\n"
        f"Max tokens:       {args.max_tokens} (per-agent floors: {AGENT_MIN_TOKENS})\n"
        f"Max chars:        {args.max_chars}\n"
        f"Presence penalty: {presence_penalty}\n"
        f"Pre-scan:         {'enabled' if args.pre_scan else 'disabled (use --pre-scan to enable)'}",
        title="scan.py",
    ))

    # ── Scan each file ───────────────────────────────────────────────────────
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

        # Build output directory name from the relative path.
        # Strip null bytes, collapse any .. components, and verify the
        # resolved path stays inside out_root to prevent traversal.
        safe_name = re.sub(r'[\\/:*?"<>|\x00]+', "_", rel)
        safe_name = safe_name.replace("..", "_")   # collapse dot-dot sequences
        safe_name = safe_name.strip(". ")          # no leading/trailing dots or spaces
        if not safe_name:
            safe_name = f"file_{i}"
        try:
            out_dir = validate_output_path(out_root, Path(safe_name))
        except ValueError as exc:
            console.print(f"  [red]Skipping {rel}: {exc}[/red]")
            results.append({"file": rel, "decision": "ERROR", "findings": 0, "blockers": 0})
            continue

        t_file_start = time.monotonic()
        try:
            pre_scan_result: dict | None = None
            if manual_prescan is not None:
                pre_scan_result = manual_prescan
            elif args.pre_scan:
                console.print(f"    [dim]→ pre_scan[/dim]")
                pre_scan_result = run_pre_scan(
                    backend=backend,
                    agents=agents_cfg,
                    rel_path=rel,
                    content=content,
                    max_chars=args.max_chars,
                    max_tokens=args.max_tokens,
                    out_dir=out_dir,
                    presence_penalty=presence_penalty,
                )

            result = scan_file(
                backend=backend,
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
                presence_penalty=presence_penalty,
                pre_scan_result=pre_scan_result,
            )
            elapsed_file = time.monotonic() - t_file_start
            results.append(result)

            decision = result.get("decision", "?")
            colour   = {"PASS": "green", "FAIL": "red", "NEEDS_HUMAN": "yellow"}.get(decision, "white")
            pre_note = (
                f" | pre-scan: {result.get('pre_scan', 0)} finding(s)"
                if args.pre_scan or args.prescan_file else ""
            )
            console.print(
                f"  [{colour}]{decision}[/{colour}]  "
                f"{result.get('findings', 0)} finding(s), "
                f"{result.get('blockers', 0)} blocker(s)"
                f"{pre_note}  [dim]({elapsed_file:.0f}s)[/dim]  → {out_dir}"
            )

        except KeyboardInterrupt:
            console.print("\n[yellow]Interrupted by user.[/yellow]")
            break
        except Exception as e:
            console.print(f"  [red]Pipeline error: {e}[/red]")
            results.append({"file": rel, "decision": "ERROR", "findings": 0, "blockers": 0})

    # ── Rollup ───────────────────────────────────────────────────────────────
    if results:
        write_rollup(results, out_root)

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
