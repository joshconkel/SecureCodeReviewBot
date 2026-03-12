# Local Agentic Code Security Scanner
Use an Agentic AI approach with JSON artifact pipelines to perform an initial secure code review. Build your gating criteria, start up a LM Studio instance with Qwen, and start doing first pass reviews!

The pipeline scans a directory of source files, runs each file through a chain of specialized security agents (scope → threat model → hypotheses → evidence → fix → gate), and produces structured JSON artifacts and a Markdown report per file plus a merged summary across all files.

---

## How it works

```
[LMStudio Pre-scan]   →  pre_scan_json  (PRE-### findings, optional)
        ↓
[Scope Agent]         →  entry points, auth boundaries, removed controls
        ↓
[Context Fetcher]     →  prioritized fetch plan for gap resolution
        ↓
[Threat Model]        →  STRIDE threats, abuse cases, chained attacks
        ↓
[Vuln Hypotheses]     →  HYP-### candidates seeded from threat + pre-scan
        ↓
[Evidence Builder]    →  Confirmed / Refuted / Inconclusive + FND-### keys
        ↓
[Fix & Hardening]     →  minimal + better fix proposals per confirmed finding
        ↓
[Policy Gate]         →  PASS / NEEDS_HUMAN / FAIL decision
```

Each agent receives only the data it needs — the pipeline deliberately slims payloads between stages to stay within local model context windows. All inter-agent data is written to disk as JSON so you can inspect, replay, or extend any stage independently.

---

## Requirements

**Python**
```bash
pip install openai pyyaml rich
```

**LMStudio**
- Download from [lmstudio.ai](https://lmstudio.ai/)
- Start the Local Server (default: `http://localhost:1234`)
- Recommended model: **Qwen2.5-Coder-7B-Instruct Q4_K_M** (~4.7 GB download)

**LMStudio server settings (critical)**

| Setting | Value | Why |
|---|---|---|
| Context Length | `8192` | Pipeline needs up to ~6,000 tokens per call |
| GPU Offload | `99` | Forces all layers to VRAM; LMStudio clamps to actual layer count |
| Max Generated Tokens | `-1` | Let per-request `max_tokens` control output length |
| Flash Attention | On | Reduces KV cache memory ~30% |

> **GPU note:** On an 8 GB VRAM card (RTX 3070 Ti / 4060 Ti), Qwen2.5-Coder-7B Q4_K_M uses ~4.1 GB for weights + ~0.8 GB KV cache at 8192 context ≈ ~5 GB total, leaving comfortable headroom. Do not run a 14B model on 8 GB — it will split layers to CPU and become unusably slow.

---

## Project files

```
agents.yaml                 Pipeline configuration — agent prompts, schemas, gate policy
scan_file.py                Orchestrator — runs the pipeline over a directory
lmstudio_system_prompt.txt  System prompt for the optional LMStudio pre-scan stage (Stage 0)
```

---

## Quick start

```bash
# Scan an entire directory
python scan_file.py "C:\path\to\your\code"

# Scan a single file
python scan_file.py "C:\path\to\your\code" --file src/Auth.cs

# Limit to first 10 files (good for testing)
python scan_file.py "C:\path\to\your\code" --max-files 10

# Specify a different model (auto-detected from LMStudio if omitted)
python scan_file.py "C:\path\to\your\code" --model qwen2.5-coder-7b-instruct
```

---

## All CLI options

| Flag | Default | Description |
|---|---|---|
| `directory` | *(required)* | Root directory to scan |
| `--file` | | Scan a single file instead of the whole directory |
| `--config` | `agents.yaml` | Path to pipeline config |
| `--out` | `scan_results` | Output directory for all artifacts |
| `--model` | *(auto-detect)* | LMStudio model name |
| `--max-files` | `50` | Max files to scan (0 = unlimited) |
| `--max-chars` | `16000` | Max characters of file content sent per agent call |
| `--max-tokens` | `3000` | Base generation budget (per-agent floors apply, see below) |
| `--retries` | `2` | Retry attempts per agent on JSON parse failure |
| `--policy` | | Path to a custom gate policy text file |
| `--patterns` | | Path to org coding standards / patterns text file |
| `--arch` | | Path to architecture constraints text file |
| `--extensions` | | Extra file extensions to include, comma-separated (e.g. `.jsx,.tsx`) |

---

## Per-agent token floors

Even if `--max-tokens` is lower, each agent enforces a minimum generation budget so its JSON schema fits:

| Agent | Floor |
|---|---|
| scope | 2,500 |
| threat | 2,500 |
| hypotheses | 3,000 |
| evidence | 3,500 |
| fix | 3,000 |
| gate | 2,000 |

If you see `Response truncated` errors on a specific agent, increase its floor in `scan_file.py` under `AGENT_MIN_TOKENS`.

---

## Output structure

```
scan_results/
  Auth.cs/
    scope.json              Scope agent output
    threat_model.json       Threat model
    hypotheses.json         Vulnerability hypotheses
    evidence.json           Confirmed / Refuted / Inconclusive findings
    fixes.json              Proposed fixes (NOT applied to codebase)
    gate.json               Gate decision + blockers + audit trail
    report.md               Human-readable summary
    _scope_raw.txt          Raw model output + finish_reason + elapsed time
    _threat_raw.txt
    _hypotheses_raw.txt
    _evidence_raw.txt
    _fix_raw.txt
    _gate_raw.txt
    _<agent>_FAILED.txt     Written only on failure — contains error + last raw output
  _merged/
    summary.json            Rollup of all file decisions
    report.md               Combined report across all scanned files
```

---

## Gate decisions

| Decision | Meaning |
|---|---|
| `PASS` | No confirmed Critical/High findings, no uncovered pre-scan findings, no inconclusive high-severity items |
| `NEEDS_HUMAN` | Inconclusive high-severity finding, or confirmed High finding with borderline confidence |
| `FAIL` | Confirmed Critical finding (conf ≥ 0.7), confirmed AuthN/AuthZ High (conf ≥ 0.8), or any confirmed Critical/High finding with no proposed fix |

> **Important:** `PASS` means no blocking findings were detected in the code provided. It does **not** mean the code is secure. The pipeline only sees what it is given — missing context, non-diff files, runtime configuration, and infrastructure are outside its view.

> **Fixes are proposals, not patches.** `fixes.json` contains recommended changes. Findings remain open until the code is actually changed and re-scanned.

---

## Supported languages (default)

`.cs` `.py` `.rb` `.js` `.ts` `.java` `.go` `.php` `.json` `.yml` `.yaml` `.config` `.xml` `.env` `.csproj` `.toml`

Additional extensions from `agents.yaml → review.include_extensions` are merged in automatically. Use `--extensions` to add more at runtime without editing config.

---

## agents.yaml structure

```yaml
llm:
  base_url: "http://localhost:1234/v1"
  api_key: "local-lm-studio"          # value doesn't matter for LMStudio
  temperature: 0
  max_tokens: 16000                    # upper ceiling; per-agent floors override upward
  per_request_timeout: 600            # seconds before a single agent call times out

shared_definitions:                   # severity levels, confidence rubric, OWASP crosswalk
  ...

review:
  max_context_chars: 20000            # max file content chars sent to each agent
  include_extensions: [...]

agents:
  scope:     { system: ..., user_template: ... }
  context_fetcher: { ... }
  threat:    { ... }
  hypotheses: { ... }
  evidence:  { ... }
  fix:       { ... }
  gate:      { ... }
```

The gate policy lives inside `agents.gate.user_template` and can be overridden at runtime with `--policy path/to/policy.txt`.

---

## Optional: LMStudio pre-scan (Stage 0)

`lmstudio_system_prompt.txt` contains a system prompt for an initial OWASP sweep you can run directly in the LMStudio chat UI before invoking the pipeline. It produces a `pre_scan_json` blob (PRE-### findings) that feeds into the threat, hypotheses, evidence, and gate agents for deeper reconciliation.

To use it, paste the contents into LMStudio's System Prompt field, send your code file as the user message, and save the JSON response. Future versions of the pipeline will automate this stage.

---

## Troubleshooting

**`TIMEOUT after Ns` on an agent**
- LMStudio GPU Offload is 0 — all inference is on CPU. Set GPU Offload to 99.
- Context Length is too high (e.g. 32768) — KV cache pre-allocation is slow even on GPU. Set to 8192.
- The agent's token floor is too high for your hardware. Reduce `AGENT_MIN_TOKENS` for that agent in `scan_file.py`.

**`Response truncated (finish_reason='length')`**
- The model hit its generation limit mid-JSON. Increase the agent's floor in `AGENT_MIN_TOKENS`.
- Confirm LMStudio Server → Max Generated Tokens is set to `-1`.

**`scope failed: ValueError … Tail: …}\n}\n` ` ``` ` `'`**
- The model wrapped its JSON in markdown fences. This is handled automatically — if you see this error you are running an older version of `scan_file.py`. Replace with the latest version.

**Agent produces `{}` / `_FAILED.txt` written**
- Check `_<agent>_FAILED.txt` for the exact error and last raw output.
- JSON parse failures retry automatically with a correction nudge. Timeouts and connection errors do not retry.

**Everything is slow (200+ seconds per agent)**
- GPU Offload is 0 — see above.
- You may be running a model larger than your VRAM can fit. Check LMStudio's model info for parameter count and quantization. Qwen2.5-Coder-7B Q4_K_M is the recommended starting point for 8 GB VRAM.

---

## License

MIT
