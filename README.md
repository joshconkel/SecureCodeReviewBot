# Local Agentic Code Security Scanner

Use an agentic AI approach with JSON artifact pipelines to perform an initial secure code review. Build your gating criteria, start up an LM Studio instance with Qwen, and start doing first-pass reviews.

The pipeline scans a directory of source files, runs each file through a chain of specialized security agents (scope → threat model → hypotheses → evidence → fix → gate), and produces structured JSON artifacts and a Markdown report per file, plus a merged summary across all files.

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

## Project files

```
agents.yaml                  Full pipeline configuration — agent prompts, schemas, gate policy
agents_quick.yaml            Configuration for the fast single-stage CI/CD scanner
agents_precommit.yaml        Configuration for the local pre-commit hook scanner
scan_file.py                 Main orchestrator — runs the full 7-stage pipeline over a directory
quick_scan.py                Fast single-agent scanner designed for CI/CD pipeline gates
precommit_scan.py            Warn-only pre-commit hook for local developer use
parse_findings.py            Post-scan parser — consolidates results and exports reports
lmstudio_system_prompt.txt   System prompt for the optional LMStudio pre-scan stage (Stage 0)
```

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

## scan_file.py — Full pipeline orchestrator

Runs each file through all seven pipeline stages and writes a full artifact set per file.

### CLI options

| Flag | Default | Description |
|---|---|---|
| `directory` | *(required)* | Root directory to scan |
| `--file` | | Scan a single file instead of the whole directory |
| `--config` | `agents.yaml` | Path to pipeline config |
| `--out` | `scan_results` | Output directory for all artifacts |
| `--model` | *(auto-detect)* | LMStudio model name |
| `--max-files` | `50` | Max files to scan (0 = unlimited) |
| `--max-chars` | `16000` | Max characters of file content sent per agent call |
| `--max-tokens` | `3000` | Base generation budget (per-agent floors apply — see below) |
| `--retries` | `2` | Retry attempts per agent on JSON parse failure |
| `--policy` | | Path to a custom gate policy text file |
| `--patterns` | | Path to org coding standards / patterns text file |
| `--arch` | | Path to architecture constraints text file |
| `--extensions` | | Extra file extensions to include, comma-separated (e.g. `.jsx,.tsx`) |
| `--pre-scan` | | Run the automated OWASP pre-scan (Stage 0) on every file |
| `--prescan-file` | | Load a manually-produced pre-scan JSON for single-file mode |

### Per-agent token floors

Even if `--max-tokens` is lower, each agent enforces a minimum generation budget so its JSON schema fits:

| Agent | Floor |
|---|---|
| pre_scan | 10,000 |
| scope | 25,000 |
| threat | 25,000 |
| hypotheses | 30,000 |
| evidence | 55,000 |
| fix | 55,000 |
| gate | 60,000 |

If you see `Response truncated` errors on a specific agent, increase its floor in `scan_file.py` under `AGENT_MIN_TOKENS`.

### Output structure

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

### Gate decisions

| Decision | Meaning |
|---|---|
| `PASS` | No confirmed Critical/High findings, no uncovered pre-scan findings, no inconclusive high-severity items |
| `NEEDS_HUMAN` | Inconclusive high-severity finding, or confirmed High finding with borderline confidence |
| `FAIL` | Confirmed Critical finding (conf ≥ 0.7), confirmed AuthN/AuthZ High (conf ≥ 0.8), or any confirmed Critical/High finding with no proposed fix |

> **Important:** `PASS` means no blocking findings were detected in the code provided. It does **not** mean the code is secure. The pipeline only sees what it is given — missing context, non-diff files, runtime configuration, and infrastructure are outside its view.

> **Fixes are proposals, not patches.** `fixes.json` contains recommended changes. Findings remain open until the code is actually changed and re-scanned.

---

## quick_scan.py — Fast CI/CD pipeline scanner

Single-agent, single LLM call per file. Designed to run in CI pipelines (Azure DevOps, GitHub Actions) as a PR gate. Scans only changed files from a git diff.

**Exit codes**

| Code | Meaning |
|---|---|
| `0` | PASS — no significant findings |
| `1` | WARN — findings present but below fail threshold |
| `2` | FAIL — Critical/High findings above confidence threshold |
| `3` | ERROR — scanner error (treat as WARN to avoid false blocks) |

### CLI options

| Flag | Default | Description |
|---|---|---|
| `directory` | *(required)* | Root directory to scan |
| `--config` | `agents_quick.yaml` | Path to quick scan config |
| `--files` | | Explicit list of files to scan (overrides directory walk, e.g. from `git diff`) |
| `--model` | *(auto-detect)* | Model name override (e.g. `gpt-4o-mini`, `claude-haiku-4-5`) |
| `--out` | `quick_scan_results` | Output directory for JSON/Markdown reports |
| `--max-files` | `50` | Max files in directory mode |
| `--no-ado` | | Suppress Azure DevOps `##vso` log commands |
| `--gha` | | Emit GitHub Actions annotations instead of ADO commands |
| `--warn-only` | | Never exit with code 2 — useful for initial rollout |

### Usage examples

```bash
# Scan a directory
python quick_scan.py src/

# Scan only files changed in the current PR (Azure DevOps)
python quick_scan.py $(Build.SourcesDirectory) \
    --files $(git diff --name-only origin/$(System.PullRequest.TargetBranch)) \
    --out $(Build.ArtifactStagingDirectory)/security-scan

# Override model
python quick_scan.py src/ --model gpt-4o-mini

# Rollout mode — warn but never block PRs
python quick_scan.py src/ --warn-only
```

### Output files

```
quick_scan_results/
  <safe_filename>/
    result.json             Per-file findings and gate decision
    raw_response.txt        Raw model output + finish_reason + elapsed time
  quick_scan_rollup.json    Consolidated results across all files
  quick_scan_summary.md     Markdown summary suitable for PR comments
```

### Azure DevOps integration

See `azure-pipelines-quick-scan.yml` for a ready-to-use pipeline definition. Required pipeline variables:

| Variable | Description |
|---|---|
| `LLM_BASE_URL` | LMStudio server URL or cloud API base URL |
| `LLM_API_KEY` | API key (`lm-studio` for local LMStudio) |
| `LLM_MODEL` | Model name |
| `QUICK_SCAN_WARN_ONLY` | Set to `true` to disable hard PR blocks during rollout |

---

## precommit_scan.py — Local developer pre-commit hook

Single-agent scanner that runs on staged files at commit time. **Always exits 0 — warn-only.** The commit proceeds regardless of findings.

### Setup

**Option A: pre-commit framework (recommended)**
```bash
pip install pre-commit openai pyyaml rich
# Place precommit_scan.py, agents_precommit.yaml, and .pre-commit-config.yaml in repo root
pre-commit install
```

**Option B: Git hook directly**
```bash
# Create .git/hooks/pre-commit:
#!/bin/sh
python precommit_scan.py --staged --skip-if-offline
exit 0
chmod +x .git/hooks/pre-commit
```

### CLI options

| Flag | Default | Description |
|---|---|---|
| `--staged` | *(default)* | Scan files staged for the current commit |
| `--files FILE [FILE ...]` | | Scan specific files instead of staged files |
| `--dir DIR` | | Scan all supported files under a directory |
| `--config` | *(auto-search)* | Path to `agents_precommit.yaml` |
| `--model` | *(auto-detect)* | Model name override |
| `--skip-if-offline` | | Exit 0 silently if LMStudio is not running |
| `--verbose` | | Show full finding details instead of compact one-line output |
| `--json-out FILE` | | Write full JSON results to a file |

> `--staged`, `--files`, and `--dir` are mutually exclusive.

### Usage examples

```bash
# Scan staged files (default — what runs automatically on git commit)
python precommit_scan.py

# Scan specific files manually
python precommit_scan.py --files src/auth.py infra/main.tf

# First-run audit of an entire directory
python precommit_scan.py --dir src/

# Skip silently if LMStudio isn't running
python precommit_scan.py --skip-if-offline

# Full finding details in terminal
python precommit_scan.py --verbose

# Save results to JSON
python precommit_scan.py --json-out scan_output.json
```

### Environment variable overrides

| Variable | Description |
|---|---|
| `PRECOMMIT_LLM_BASE_URL` | Override `base_url` in config (default: `http://localhost:1234/v1`) |
| `PRECOMMIT_LLM_API_KEY` | Override `api_key` in config |
| `PRECOMMIT_LLM_MODEL` | Model name override |

### Config search order

The hook looks for `agents_precommit.yaml` in the following locations (first match wins):

1. Path passed via `--config`
2. `agents_precommit.yaml` (repo root)
3. `security/agents_precommit.yaml`
4. `.security/agents_precommit.yaml`
5. Same directory as `precommit_scan.py`

---

## parse_findings.py — Results parser and report exporter

Walks a directory of pipeline scan output folders, consolidates findings across all scan sets, and produces structured report files. Designed to run after `scan_file.py` has produced its output.

### Expected input layout

```
scan_results/
  AddNewUser_scan/
    evidence.json       → confirmed findings (primary source)
    fix.json            → remediation details per finding
    gate.json           → gate decision, blockers, required human review
    pre_scan.json       → pre-scan findings (optional)
    scope.json          → scope metadata and risk signal
  Login_scan/
    1234_evidence.json  → timestamp-prefixed filenames are handled automatically
    1234_fix.json
    ...
```

All five file types are matched by suffix — leading numeric timestamp prefixes (e.g. `1775963083761_evidence.json`) are stripped automatically.

### CLI options

| Flag | Default | Description |
|---|---|---|
| `root_dir` | *(required)* | Root directory containing scan subdirectories |
| `--output-dir` | *(root_dir)* | Directory for output files |
| `--summary-file` | `findings_summary.txt` | Human-readable consolidated report filename |
| `--structured-csv-file` | `findings_structured.csv` | Structured findings CSV filename |
| `--json` | | Also export findings as a JSON file |
| `--json-file` | `findings_structured.json` | JSON output filename (only used with `--json`) |

### Usage examples

```bash
# Basic — outputs to scan_results/
python parse_findings.py ./scan_results

# Write reports to a separate directory
python parse_findings.py ./scan_results --output-dir ./reports

# Export CSV + JSON
python parse_findings.py ./scan_results --output-dir ./reports --json

# Custom filenames
python parse_findings.py ./scan_results \
    --summary-file security_report.txt \
    --structured-csv-file findings.csv \
    --json --json-file findings.json
```

### Output files

| File | Description |
|---|---|
| `findings_summary.txt` | Full human-readable report — gate decisions, severity breakdown, per-finding detail, required human review, follow-up actions |
| `findings_structured.csv` | Structured CSV with one row per finding (expanded for multiple Notes values) |
| `findings_structured.json` | Same data as CSV in JSON array format (opt-in via `--json`) |

### Structured CSV / JSON columns

| Column | Description |
|---|---|
| Scan ID | Name of the scan folder (e.g. `AddNewUser_scan`) |
| Finding Key | Globally unique `CODESCAN-001`, `CODESCAN-002`, … assigned in order across all scan sets |
| Is Blocker | `YES` or `NO` — whether the finding triggered a gate blocker |
| Title | Short description of the finding |
| Severity | `CRITICAL`, `HIGH`, `MEDIUM`, `LOW` |
| Confidence | Model confidence as a percentage (e.g. `87%`) |
| Category | Vulnerability category (e.g. `DataLeak`, `Injection`, `AuthN`) |
| File(s) | Affected file path(s) with line ranges |
| Line(s) | Line range(s) within the file |
| Trace | Evidence trace — source to sink or auth flow |
| Code Excerpt | Relevant code snippet (first excerpt, max 500 chars) |
| Notes | Individual note from the fix recommendation (one row per note) |
| Fix (minimal) | One-sentence summary of the minimal safe fix |
| Fix (better) | One-sentence summary of the preferred fix |
| Tests Needed | Required regression tests — test name and proof on separate lines |

> **Row expansion:** When a finding has multiple Notes values, it produces one row per note with all other columns repeated. The `Finding Key` (e.g. `CODESCAN-001`) is the same across all expanded rows for the same finding.

> **JSON format difference:** `Tests Needed` is a JSON array of strings in the JSON export rather than a line-separated string, making it easier to iterate in downstream tooling.

---

## Supported languages and file types

### Source code
`.cs` `.py` `.rb` `.js` `.ts` `.java` `.go` `.php`

### Infrastructure as Code
`.tf` `.tfvars` `.bicep`

### Config and manifests
`.json` `.yml` `.yaml` `.config` `.xml` `.env` `.csproj` `.toml`
`requirements.txt` `package.json` `Gemfile` `Gemfile.lock` `package-lock.json` `poetry.lock`

Additional extensions from `agents.yaml → review.include_extensions` are merged in automatically. Use `--extensions` to add more at runtime without editing config.

---

## agents.yaml structure

```yaml
llm:
  base_url: "http://localhost:1234/v1"
  api_key: "local-lm-studio"          # value doesn't matter for LMStudio
  temperature: 0                       # always 0 — reproducible output
  max_tokens: 16000                    # upper ceiling; per-agent floors override upward
  per_request_timeout: 600            # seconds before a single agent call times out
  presence_penalty: 0.0               # set to 1.5 for Qwen3.5 / reasoning models

shared_definitions:                   # severity levels, confidence rubric, OWASP crosswalk
  ...

review:
  max_context_chars: 20000            # max file content chars sent to each agent
  include_extensions: [...]

agents:
  scope:           { system: ..., user_template: ... }
  context_fetcher: { ... }
  threat:          { ... }
  hypotheses:      { ... }
  evidence:        { ... }
  fix:             { ... }
  gate:            { ... }
```

The gate policy lives inside `agents.gate.user_template` and can be overridden at runtime with `--policy path/to/policy.txt`. For more information on policy file format, see `gate_policy.md`.

---

## Optional: LMStudio pre-scan (Stage 0)

`lmstudio_system_prompt.txt` contains a system prompt for an initial OWASP sweep you can run directly in the LMStudio chat UI before invoking the pipeline. It produces a `pre_scan_json` blob (PRE-### findings) that feeds into the threat, hypotheses, evidence, and gate agents for deeper reconciliation.

To use it manually: paste the contents into LMStudio's System Prompt field, send your code file as the user message, and save the JSON response. To automate it, pass `--pre-scan` to `scan_file.py` or provide a saved response with `--prescan-file`.

---

## Troubleshooting

**`TIMEOUT after Ns` on an agent**
- LMStudio GPU Offload is 0 — all inference is on CPU. Set GPU Offload to 99.
- Context Length is too high (e.g. 32768) — KV cache pre-allocation is slow even on GPU. Set to 8192.
- The agent's token floor is too high for your hardware. Reduce `AGENT_MIN_TOKENS` for that agent in `scan_file.py`.

**`Response truncated (finish_reason='length')`**
- The model hit its generation limit mid-JSON. Increase the agent's floor in `AGENT_MIN_TOKENS`.
- Confirm LMStudio Server → Max Generated Tokens is set to `-1`.

**`scope failed: ValueError` with trailing `}` or fences**
- The model wrapped its JSON in markdown fences. This is handled automatically. If you still see this, you may be running an older version of `scan_file.py`.

**Agent produces `{}` / `_FAILED.txt` written**
- Check `_<agent>_FAILED.txt` for the exact error and last raw output.
- JSON parse failures retry automatically with a correction nudge. Timeouts and connection errors do not retry.

**Everything is slow (200+ seconds per agent)**
- GPU Offload is 0 — see above.
- You may be running a model larger than your VRAM can fit. Qwen2.5-Coder-7B Q4_K_M is the recommended starting point for 8 GB VRAM.

**Reasoning model producing only `<think>` blocks with no JSON**
- Set `presence_penalty: 1.5` in `agents.yaml` (or `agents_quick.yaml` / `agents_precommit.yaml`).
- This applies to Qwen3.5, QwQ, and DeepSeek-R1. Leave at `0.0` for Qwen2.5-Coder and other non-reasoning models.

**Pre-commit hook is too slow**
- Switch to `Qwen2.5-Coder-7B` if running a larger model — ~10–20s per file vs 40s+.
- Reduce `max_chars_per_file` in `agents_precommit.yaml` (default: 8000).
- Add `--skip-if-offline` so the hook is silent when LMStudio isn't loaded.

**`parse_findings.py` reports no scan sets found**
- Ensure the directory contains subdirectories with at least one recognised file (`evidence.json`, `fix.json`, `gate.json`, `pre_scan.json`, or `scope.json`).
- Timestamp-prefixed filenames (e.g. `1234_evidence.json`) are handled automatically.

---

## License

MIT
