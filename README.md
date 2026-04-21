# Local Agentic Code Security Scanner

Use an agentic AI approach with JSON artifact pipelines to perform an initial secure code review. Connect to a local LM Studio instance, a cloud provider, or any OpenAI-compatible endpoint, and start doing first-pass reviews.

The pipeline scans a directory of source files, runs each file through a chain of specialized security agents (scope → threat model → hypotheses → evidence → fix → gate), and produces structured JSON artifacts and a Markdown report per file, plus a merged summary across all files.

---

## What's new

### Multi-provider LLM backend support (`scan.py`)

`scan.py` (previously `scan_file.py`) now supports six LLM backends selectable at runtime via a single CLI flag. LM Studio remains the default — no flags required for existing workflows.

| Provider | Flag | Auth |
|---|---|---|
| LM Studio (default) | `--lmstudio` | None (local) |
| OpenAI | `--openai` | `--api-key` or `OPENAI_API_KEY` |
| Anthropic | `--anthropic` | `--api-key` or `ANTHROPIC_API_KEY` |
| AWS Bedrock | `--bedrock` | Key flags, profile, or ambient credential chain |
| Azure AI Foundry | `--azure` | `--api-key` or `AZURE_OPENAI_API_KEY` |
| Google Gemini | `--gemini` | `--api-key` or `GEMINI_API_KEY` |

Every provider also accepts `--endpoint` to override the default API URL, and `--model` to select a specific model. See [scan.py — full pipeline orchestrator](#scanpy--full-pipeline-orchestrator) for the complete flag reference.

If you run into token limit issues in different APIs, modify the default AGENT_MIN_TOKENS values in the scan.py file to work within those limits. Sizes are appropriate for local models out of the box.

### New companion scripts

| Script | Purpose |
|---|---|
| `parse_findings.py` | Walks a directory of scan output folders, consolidates findings across all scan sets, produces `findings_summary.txt` and `findings_jira.csv` |
| `summary_to_csv.py` | Reads a `findings_summary.txt` file and exports a flat detailed CSV with one row per finding, including code excerpts, fix guidance, and test requirements |

### Security hardening (`scan.py`)

Eight vulnerability classes were identified via static analysis (Cortex / Qwen Coder review) and remediated. See [Security fixes](#security-fixes) for the full list.

---

## How it works

```
[Pre-scan Agent]      →  pre_scan_json  (PRE-### findings, optional)
        ↓
[Scope Agent]         →  entry points, auth boundaries, removed controls
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

Each agent receives only the data it needs — the pipeline deliberately slims payloads between stages to stay within model context windows. All inter-agent data is written to disk as JSON so you can inspect, replay, or extend any stage independently.

---

## Project files

```
agents.yaml                  Full pipeline configuration — agent prompts, schemas, gate policy
agents_quick.yaml            Configuration for the fast single-stage CI/CD scanner
agents_precommit.yaml        Configuration for the local pre-commit hook scanner
scan.py                      Main orchestrator — runs the full 7-stage pipeline over a directory
                             Supports LM Studio, OpenAI, Anthropic, Bedrock, Azure, Gemini
quick_scan.py                Fast single-agent scanner designed for CI/CD pipeline gates
precommit_scan.py            Warn-only pre-commit hook for local developer use
parse_findings.py            Post-scan consolidator — walks scan output folders, produces
                             findings_summary.txt and findings_jira.csv
summary_to_csv.py            Reads findings_summary.txt and exports a detailed per-finding CSV
lmstudio_system_prompt.txt   System prompt for the optional LMStudio pre-scan stage (Stage 0)
```

---

## Requirements

### Core (always required)

```bash
pip install openai pyyaml rich
```

### Per-provider (install only the ones you use)

```bash
pip install anthropic           # --anthropic
pip install boto3               # --bedrock
pip install google-generativeai # --gemini
# Azure and OpenAI use the openai package already installed above
```

### LM Studio (default backend)

- Download from [lmstudio.ai](https://lmstudio.ai/)
- Start the Local Server (default: `http://localhost:1234`)
- Recommended model: **Qwen2.5-Coder-7B-Instruct Q4_K_M** (~4.7 GB download)

**LM Studio server settings (critical)**

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
# LM Studio (default — no extra flags needed)
python scan.py /path/to/code

# OpenAI
python scan.py /path/to/code --openai --api-key sk-...

# Anthropic
python scan.py /path/to/code --anthropic --api-key sk-ant-...

# AWS Bedrock (ambient credentials)
python scan.py /path/to/code --bedrock --aws-region us-east-1

# Azure AI Foundry
python scan.py /path/to/code --azure \
    --endpoint https://my-resource.openai.azure.com \
    --api-key <your-key> \
    --azure-deployment gpt-4o

# Google Gemini
python scan.py /path/to/code --gemini --api-key AIza...

# Scan a single file with any backend
python scan.py /path/to/code --openai --api-key sk-... --file src/Auth.cs

# Limit to first 10 files (useful for testing)
python scan.py /path/to/code --max-files 10

# Run OWASP pre-scan on every file, then full pipeline
python scan.py /path/to/code --pre-scan
```

---

## scan.py — Full pipeline orchestrator

Runs each file through all seven pipeline stages and writes a full artifact set per file.

### Provider selection flags

Exactly one provider flag may be used per invocation. If none is given, `--lmstudio` is the default.

| Flag | Provider | Default endpoint |
|---|---|---|
| `--lmstudio` | LM Studio local server | `http://localhost:1234/v1` |
| `--openai` | OpenAI API | `https://api.openai.com/v1` |
| `--anthropic` | Anthropic API (native SDK) | `https://api.anthropic.com` |
| `--bedrock` | AWS Bedrock (boto3 converse) | Regional (e.g. `bedrock-runtime.us-east-1.amazonaws.com`) |
| `--azure` | Azure AI Foundry | **Required via `--endpoint`** |
| `--gemini` | Google Gemini (native SDK) | `https://generativelanguage.googleapis.com` |

### Common endpoint and auth flags

| Flag | Description |
|---|---|
| `--endpoint URL` | Override the provider's default API endpoint. Required for `--azure`. Credentials embedded in URLs (e.g. `user:secret@host`) are automatically redacted from log output. Only `http://` and `https://` schemes are accepted. |
| `--api-key KEY` | API key for the selected provider. Falls back to the environment variable for that provider if omitted. |
| `--model ID` | Model to use. If omitted, provider defaults apply (LM Studio auto-detects from server; others use a sensible default). |

### AWS Bedrock flags

| Flag | Default | Description |
|---|---|---|
| `--aws-region` | `us-east-1` | AWS region for the Bedrock runtime endpoint |
| `--aws-profile` | | Named profile from `~/.aws/credentials` |
| `--aws-access-key` | | Explicit AWS access key ID |
| `--aws-secret-key` | | Explicit AWS secret access key |
| `--aws-session-token` | | Session token for temporary credentials / assume-role |

**Bedrock credential priority:** explicit key flags → `--aws-profile` → ambient chain (env vars, instance role, SSO).

### Azure AI Foundry flags

| Flag | Default | Description |
|---|---|---|
| `--azure-deployment` | *(same as `--model`)* | Azure deployment name when different from the model ID |
| `--azure-api-version` | `2024-02-01` | Azure OpenAI API version string |

### Environment variable fallbacks

| Variable | Provider |
|---|---|
| `OPENAI_API_KEY` | `--openai` |
| `ANTHROPIC_API_KEY` | `--anthropic` |
| `AZURE_OPENAI_API_KEY` | `--azure` |
| `GEMINI_API_KEY` or `GOOGLE_API_KEY` | `--gemini` |
| `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_DEFAULT_REGION` | `--bedrock` (standard boto3 env vars) |

### Provider default models

| Provider | Default model |
|---|---|
| LM Studio | Auto-detected from server |
| OpenAI | `gpt-4o` |
| Anthropic | `claude-sonnet-4-5` |
| Bedrock | `anthropic.claude-3-5-sonnet-20241022-v2:0` |
| Azure | `gpt-4o` |
| Gemini | `gemini-2.0-flash` |

### Scanner options

| Flag | Default | Description |
|---|---|---|
| `directory` | *(required)* | Root directory to scan |
| `--file` | | Scan a single file instead of the whole directory |
| `--config` | `agents.yaml` | Path to pipeline config |
| `--out` | `scan_results` | Output directory for all artifacts |
| `--max-files` | `50` | Max files to scan (0 = unlimited) |
| `--max-chars` | `16000` | Max characters of file content sent per agent call |
| `--max-tokens` | `3000` | Base generation budget (per-agent floors apply — see below) |
| `--retries` | `2` | Retry attempts per agent on JSON parse failure |
| `--policy` | | Path to a custom gate policy text file |
| `--patterns` | | Path to org coding standards / patterns text file |
| `--arch` | | Path to architecture constraints text file |
| `--extensions` | | Extra file extensions to include, comma-separated (e.g. `.jsx,.tsx`) |
| `--pre-scan` | | Run the automated OWASP pre-scan (Stage 0) on every file |
| `--prescan-file` | | Load a manually-produced pre-scan JSON (single-file mode only) |

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

If you see `Response truncated` errors on a specific agent, increase its floor in `scan.py` under `AGENT_MIN_TOKENS`.

e.g. for Open AI GPT 4o:

AGENT_MIN_TOKENS = {
    "pre_scan":   4000,
    "scope":      6000,
    "threat":     6000,
    "hypotheses": 8000,
    "evidence":   12000,
    "fix":        12000,
    "gate":       12000,
}

### Usage examples

```bash
# ===========================================================================
# LM Studio (default — no provider flag needed)
# ===========================================================================

# Scan an entire directory
python scan.py /path/to/code

# Scan a single file
python scan.py /path/to/code --file src/Auth.cs

# Remote LM Studio server, specific model, limit to 20 files
python scan.py /path/to/code \
    --lmstudio \
    --endpoint http://192.168.1.50:1234/v1 \
    --model qwen2.5-coder-7b-instruct \
    --max-files 20

# Full pipeline with OWASP pre-scan, custom output directory
python scan.py /path/to/code \
    --pre-scan \
    --out ./results/sprint-42 \
    --max-chars 12000 \
    --max-tokens 4000

# Single file with a manually-produced pre-scan JSON
python scan.py /path/to/code \
    --file src/AddNewUser.cs \
    --prescan-file ./prescan/AddNewUser_prescan.json

# ===========================================================================
# OpenAI
# ===========================================================================

# Basic — API key via flag
python scan.py /path/to/code \
    --openai \
    --api-key sk-...

# Specific model, custom output, with pre-scan
python scan.py /path/to/code \
    --openai \
    --api-key sk-... \
    --model gpt-4o-mini \
    --out ./results \
    --pre-scan

# API key from environment variable (no --api-key needed)
export OPENAI_API_KEY=sk-...
python scan.py /path/to/code --openai

# OpenAI-compatible third-party endpoint
python scan.py /path/to/code \
    --openai \
    --endpoint https://api.groq.com/openai/v1 \
    --api-key gsk_... \
    --model llama-3.3-70b-versatile

# ===========================================================================
# Anthropic
# ===========================================================================

# Basic
python scan.py /path/to/code \
    --anthropic \
    --api-key sk-ant-...

# Specific model, gate policy file, architecture constraints
python scan.py /path/to/code \
    --anthropic \
    --api-key sk-ant-... \
    --model claude-opus-4-5 \
    --policy ./policies/gate_policy.txt \
    --arch ./docs/architecture.txt

# API key from environment variable
export ANTHROPIC_API_KEY=sk-ant-...
python scan.py /path/to/code --anthropic

# ===========================================================================
# AWS Bedrock
# ===========================================================================

# Ambient credentials (instance role, SSO, env vars)
python scan.py /path/to/code \
    --bedrock \
    --model anthropic.claude-3-5-sonnet-20241022-v2:0

# Named profile, non-default region
python scan.py /path/to/code \
    --bedrock \
    --aws-region eu-west-1 \
    --aws-profile prod-security

# Explicit access key (e.g. in a CI environment without instance roles)
python scan.py /path/to/code \
    --bedrock \
    --aws-region us-east-1 \
    --aws-access-key AKIAIOSFODNN7EXAMPLE \
    --aws-secret-key wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

# Temporary credentials with session token (assume-role)
python scan.py /path/to/code \
    --bedrock \
    --aws-region us-east-1 \
    --aws-access-key ASIA... \
    --aws-secret-key ... \
    --aws-session-token AQoXnyc4lcK...

# ===========================================================================
# Azure AI Foundry
# ===========================================================================

# Basic — endpoint is required
python scan.py /path/to/code \
    --azure \
    --endpoint https://my-resource.openai.azure.com \
    --api-key <your-azure-key>

# Custom deployment name and API version
python scan.py /path/to/code \
    --azure \
    --endpoint https://my-resource.openai.azure.com \
    --api-key <your-azure-key> \
    --azure-deployment gpt-4o-prod \
    --azure-api-version 2024-08-01-preview

# API key from environment variable
export AZURE_OPENAI_API_KEY=<your-azure-key>
python scan.py /path/to/code \
    --azure \
    --endpoint https://my-resource.openai.azure.com \
    --azure-deployment gpt-4o-prod

# ===========================================================================
# Google Gemini
# ===========================================================================

# Basic
python scan.py /path/to/code \
    --gemini \
    --api-key AIza...

# Specific model
python scan.py /path/to/code \
    --gemini \
    --api-key AIza... \
    --model gemini-2.0-flash

# API key from environment variable
export GEMINI_API_KEY=AIza...
python scan.py /path/to/code --gemini

# ===========================================================================
# Common options — work with any provider
# ===========================================================================

# Scan only the first 10 files (useful for testing a new provider config)
python scan.py /path/to/code --openai --api-key sk-... \
    --max-files 10

# Add extra file extensions to the scan
python scan.py /path/to/code --openai --api-key sk-... \
    --extensions .jsx,.tsx,.vue

# Provide org coding patterns and architecture constraints
python scan.py /path/to/code --anthropic --api-key sk-ant-... \
    --patterns ./standards/secure_coding.txt \
    --arch ./docs/system_architecture.txt \
    --policy ./policies/gate_policy.txt

# Raise token budget for large files or reasoning models
python scan.py /path/to/code --openai --api-key sk-... \
    --max-tokens 8000 \
    --max-chars 20000

# Reduce context sent per call for faster/cheaper runs
python scan.py /path/to/code --openai --api-key sk-... \
    --max-chars 8000 \
    --max-tokens 3000

# Increase retries for flaky or slow endpoints
python scan.py /path/to/code --lmstudio \
    --retries 3
```

> **`--endpoint` note:** Only `http://` and `https://` schemes are accepted. Credentials embedded in the URL (e.g. `user:secret@host`) are automatically redacted from log output and never written to disk.

> **Auth precedence:** `--api-key` always takes precedence over the environment variable. For Bedrock, explicit key flags take precedence over `--aws-profile`, which takes precedence over the ambient boto3 credential chain.

> **Azure deployment:** `--azure-deployment` only needs to be set when the deployment name in your Azure resource differs from the model ID you would normally pass to `--model`.

### Output structure

```
scan_results/
  Auth.cs/
    scope.json              Scope agent output
    threat.json             Threat model
    hypotheses.json         Vulnerability hypotheses
    evidence.json           Confirmed / Refuted / Inconclusive findings
    fix.json                Proposed fixes (NOT applied to codebase)
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

> **Fixes are proposals, not patches.** `fix.json` contains recommended changes. Findings remain open until the code is actually changed and re-scanned.

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

## parse_findings.py — Results consolidator and report exporter

Walks a directory of scan output folders (one subdirectory per scan set), consolidates findings from all five pipeline JSON files, and produces a single summary report and a Jira-importable CSV. Designed to run after `scan.py` has produced its output.

### How scan sets are discovered

Each subdirectory that contains at least one recognised pipeline file is treated as a scan set. Files are matched by suffix — leading numeric timestamp prefixes (e.g. `1775963083761_evidence.json`) are stripped automatically.

```
scan_results/
  AddNewUser_scan/
    evidence.json       → confirmed findings (primary source)
    fix.json            → remediation details per finding
    gate.json           → gate decision, blockers, required human review
    pre_scan.json       → pre-scan findings (optional)
    scope.json          → scope metadata and risk signal
  Login_scan/
    1234_evidence.json  → timestamp-prefixed filenames handled automatically
    1234_fix.json
    ...
```

### Data sources per finding

| File | What is extracted |
|---|---|
| `evidence.json` | Finding key, title, severity, category, confidence, locations, code excerpts, trace |
| `fix.json` | Minimal fix, better fix, required tests, logging guidance (joined by `finding_key`) |
| `gate.json` | Blocker status, gate decision, required human review items |
| `pre_scan.json` | Any pre-scan findings not already covered by evidence findings |
| `scope.json` | Repo name, PR label, risk signal |

### CLI options

| Flag | Default | Description |
|---|---|---|
| `root_dir` | *(required)* | Root directory containing scan subdirectories |
| `--output-dir` | *(root_dir)* | Directory for output files |
| `--summary-file` | `findings_summary.txt` | Human-readable consolidated report filename |
| `--csv-file` | `findings_jira.csv` | Jira-importable CSV filename |

### Usage examples

```bash
# Basic — outputs to scan_results/
python parse_findings.py ./scan_results

# Write reports to a separate directory
python parse_findings.py ./scan_results --output-dir ./reports

# Custom filenames
python parse_findings.py ./scan_results \
    --output-dir ./reports \
    --summary-file security_report.txt \
    --csv-file jira_tickets.csv
```

### Output files

| File | Description |
|---|---|
| `findings_summary.txt` | Full human-readable report — gate decisions per scan set, severity and category breakdowns, per-scan finding counts table, per-finding detail with code excerpts and fix proposals, required human review, and follow-up actions |
| `findings_jira.csv` | Two-column CSV (`Summary`, `Description`) for Jira bulk import. Each row is globally unique — `Summary` is prefixed with `[scan_id][BLOCKER?][SEVERITY][CATEGORY]` so identical finding keys from different scan sets are distinguishable |

### findings_jira.csv Summary format

```
[scan_id][BLOCKER][HIGH][AuthN] FND-001 — Commented-out username/password validation logic
[scan_id][MEDIUM][DataLeak] FND-002 — Unconditional Console.WriteLine leaks internal state
```

The `Description` field uses Jira wiki markup and includes: severity, category, rule ID, affected files and lines, description, remediation (minimal and better), required tests, logging guidance, required human review items, and follow-up actions.

---

## summary_to_csv.py — Detailed findings CSV exporter

Reads a `findings_summary.txt` file produced by `parse_findings.py` and exports a flat CSV with one row per finding, expanding all fields individually. Useful for tracking in spreadsheets, importing into ticketing systems beyond Jira, or feeding into downstream tooling.

### CLI options

| Flag | Default | Description |
|---|---|---|
| `summary_file` | *(required)* | Path to `findings_summary.txt` |
| `--output` / `-o` | `detailed_findings.csv` (next to input) | Output CSV path |

### Usage examples

```bash
python summary_to_csv.py findings_summary.txt
python summary_to_csv.py findings_summary.txt --output reports/detailed.csv
python summary_to_csv.py reports/findings_summary.txt -o reports/detailed_findings.csv
```

### CSV columns

| Column | Description |
|---|---|
| `Finding ID` | Globally unique: `[scan_id]-[finding_key]` (e.g. `AddNewUser_scan-FND-001`) |
| `Title` | Short description of the finding |
| `Severity` | `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, `INFO`, or `UNKNOWN` |
| `Category` | Vulnerability category (e.g. `AuthN`, `DataLeak`, `BusinessLogic`) |
| `File` | Affected file path(s) |
| `Line(s)` | Affected line number(s) or range |
| `Description` | Notes content from the fix recommendation (duplicate trace/excerpt content stripped) |
| `Trace` | Execution / call trace from source to sink |
| `Code Excerpt` | Verbatim code block from the finding (first excerpt only) |
| `Fix (minimal)` | One-sentence summary of the minimal safe fix |
| `Fix (better)` | One-sentence summary of the preferred enhanced fix |
| `Tests Needed` | Required regression tests, pipe-separated (`test_name — proof \| test_name — proof`) |

A terminal preview is printed showing all findings in a compact table before the file is written.

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
  base_url: "http://localhost:1234/v1"   # overridden by --endpoint at runtime
  api_key: "local-lm-studio"             # value doesn't matter for LMStudio
  temperature: 0                         # always 0 — reproducible output
  max_tokens: 16000                      # upper ceiling; per-agent floors override upward
  per_request_timeout: 600              # seconds before a single agent call times out
  presence_penalty: 0.0                 # set to 1.5 for Qwen3.5 / reasoning models

shared_definitions:                     # severity levels, confidence rubric, OWASP crosswalk
  ...

review:
  max_context_chars: 20000             # max file content chars sent to each agent
  include_extensions: [...]

agents:
  scope:      { system: ..., user_template: ... }
  threat:     { ... }
  hypotheses: { ... }
  evidence:   { ... }
  fix:        { ... }
  gate:       { ... }
```

The gate policy lives inside `agents.gate.user_template` and can be overridden at runtime with `--policy path/to/policy.txt`. For more information on policy file format, see `gate_policy.md`.

---

## Optional: LMStudio pre-scan (Stage 0)

`lmstudio_system_prompt.txt` contains a system prompt for an initial OWASP sweep you can run directly in the LMStudio chat UI before invoking the pipeline. It produces a `pre_scan_json` blob (PRE-### findings) that feeds into the threat, hypotheses, evidence, and gate agents for deeper reconciliation.

To use it manually: paste the contents into LMStudio's System Prompt field, send your code file as the user message, and save the JSON response. To automate it, pass `--pre-scan` to `scan.py` or provide a saved response with `--prescan-file`.

---

## Security fixes

The following vulnerabilities were identified by static analysis (Cortex / Qwen Coder Next review) and remediated in `scan.py`. All fixes are present in the current version.

### CWE-573 — Lambda closure capture (`extract_json`)
**Was:** Four `lambda` expressions in a list literal used as a transform pipeline, including a no-op `lambda x: x` that static analysers flag as a potential closure capture bug.  
**Fixed:** Replaced with four named private functions (`_identity`, `_fix_ctrl`, `_repair`, `_fix_ctrl_repair`). Named functions are independently testable and unambiguous to analysis tools.

### CWE-61 — Symlink traversal (`collect_files`)
**Was:** `os.walk()` called without `followlinks=False`, allowing a symlink inside the scan tree to silently redirect traversal outside the intended root.  
**Fixed:** `os.walk(root, followlinks=False)` is now used at all call sites.

### CWE-22 — Path traversal (`safe_name` construction)
**Was:** Output directory names were derived from relative file paths using only a `re.sub` that stripped some special characters but left `..` sequences intact. A file path like `../../etc/cron.d/file` would have written output outside `scan_results/`.  
**Fixed:** Added explicit `..` collapse, null byte (`\x00`) stripping, leading dot/space trimming, a non-empty fallback, and a `validate_output_path()` function that resolves the full path and asserts it remains inside the output root via `Path.relative_to()`.

### CWE-73 — External control of file path via agent label (`call_agent`, `scan_file`)
**Was:** The `label` parameter was used directly in `f"_{label}_FAILED.txt"` and `f"_{name}.json"` path constructions with no validation.  
**Fixed:** `sanitise_label()` enforces an explicit allowlist (`_ALLOWED_AGENT_LABELS`) at the entry point of `call_agent` and inside `scan_file`'s inner `agent()` helper. Any value outside the allowlist raises `ValueError` before reaching the filesystem.

### CWE-532 — Credential exposure in logs (endpoint display)
**Was:** `args.endpoint` was printed verbatim in the startup banner and backend selection log line. A URL containing embedded credentials (e.g. `https://key:secret@api.host/v1`) would expose them to the terminal and any log aggregator.  
**Fixed:** `redact_url_credentials()` strips the userinfo component from any URL before display, replacing it with `***`.

### CWE-918 — SSRF via non-HTTP endpoint scheme (`build_backend`)
**Was:** No validation prevented `file://`, `ftp://`, or custom URI schemes from being passed as `--endpoint`, which could probe local filesystem paths or internal services through the HTTP client.  
**Fixed:** `validate_endpoint_url()` rejects any scheme outside `{http, https}` and verifies a hostname is present before the value reaches any backend constructor.

### CWE-400 — Resource exhaustion via oversized scan targets (`collect_files`)
**Was:** Files were read with `read_text()` regardless of size. An unexpectedly large file (e.g. a binary mistakenly matched by extension) could exhaust available memory.  
**Fixed:** `collect_files()` now calls `stat()` during collection and skips any file exceeding `_MAX_FILE_READ_BYTES` (16 MB) with a warning. The same limit is applied to all auxiliary input files (policy, patterns, arch, prescan, config).

### CWE-377 / TOCTOU race — Non-atomic file writes (all output paths)
**Was:** All output files were written with `Path.write_text()`. A process crash mid-write left a truncated or empty JSON file that subsequent runs could silently read as valid data. In concurrent use, a window existed between `mkdir()` and `write_text()` where another process could replace the directory with a symlink.  
**Fixed:** All seven output write sites now use `atomic_write_text()`, which writes to a sibling `.tmp` file via `tempfile.mkstemp()` (mode 0600, unpredictable name) then calls `os.replace()` — a POSIX atomic rename — to move it into place. The temp file is cleaned up on any write error.

### CWE-20 — Missing input validation on config and auxiliary files (`main`)
**Was:** `agents.yaml` and auxiliary text files (policy, patterns, arch, prescan) were read with bare `Path.read_text()` or broad `except Exception` catches, with no size limit and no validation that the YAML parsed as a mapping.  
**Fixed:** All file reads go through size-checked helpers. `yaml.YAMLError` and `json.JSONDecodeError` are caught specifically. The YAML config is validated as a `dict` after parsing. The prescan file is validated as a `dict` before use.

---

## Troubleshooting

**`TIMEOUT after Ns` on an agent**
- LMStudio GPU Offload is 0 — all inference is on CPU. Set GPU Offload to 99.
- Context Length is too high (e.g. 32768) — KV cache pre-allocation is slow even on GPU. Set to 8192.
- The agent's token floor is too high for your hardware. Reduce `AGENT_MIN_TOKENS` for that agent in `scan.py`.

**`Response truncated (finish_reason='length')`**
- The model hit its generation limit mid-JSON. Increase the agent's floor in `AGENT_MIN_TOKENS`.
- Confirm LMStudio Server → Max Generated Tokens is set to `-1`.

**`scope failed: ValueError` with trailing `}` or fences**
- The model wrapped its JSON in markdown fences. This is handled automatically. If you still see this, you may be running an older version of `scan.py`.

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

**Cloud provider authentication errors**
- OpenAI / Anthropic / Gemini: confirm the API key is correct and exported in the environment variable, or passed explicitly with `--api-key`.
- Azure: `--endpoint` is required and must be the full resource endpoint (e.g. `https://my-resource.openai.azure.com`).
- Bedrock: run `aws sts get-caller-identity` to confirm credentials are valid in the target region. If using a named profile, pass `--aws-profile`.
- All providers: endpoints must use `http://` or `https://` — other schemes are rejected for security reasons.

**`validate_output_path: path traversal detected`**
- A filename in the scan tree contains `..` sequences that would escape the output directory. The file is skipped automatically with an error entry in the results. Check the file path for unexpected characters.

---

## License

MIT        ↓
[Policy Gate]         →  PASS / NEEDS_HUMAN / FAIL decision
```

Each agent receives only the data it needs — the pipeline deliberately slims payloads between stages to stay within model context windows. All inter-agent data is written to disk as JSON so you can inspect, replay, or extend any stage independently.

---

## Project files

```
agents.yaml                  Full pipeline configuration — agent prompts, schemas, gate policy
agents_quick.yaml            Configuration for the fast single-stage CI/CD scanner
agents_precommit.yaml        Configuration for the local pre-commit hook scanner
scan.py                      Main orchestrator — runs the full 7-stage pipeline over a directory
                             Supports LM Studio, OpenAI, Anthropic, Bedrock, Azure, Gemini
quick_scan.py                Fast single-agent scanner designed for CI/CD pipeline gates
precommit_scan.py            Warn-only pre-commit hook for local developer use
parse_findings.py            Post-scan consolidator — walks scan output folders, produces
                             findings_summary.txt and findings_jira.csv
summary_to_csv.py            Reads findings_summary.txt and exports a detailed per-finding CSV
lmstudio_system_prompt.txt   System prompt for the optional LMStudio pre-scan stage (Stage 0)
```

---

## Requirements

### Core (always required)

```bash
pip install openai pyyaml rich
```

### Per-provider (install only the ones you use)

```bash
pip install anthropic           # --anthropic
pip install boto3               # --bedrock
pip install google-generativeai # --gemini
# Azure and OpenAI use the openai package already installed above
```

### LM Studio (default backend)

- Download from [lmstudio.ai](https://lmstudio.ai/)
- Start the Local Server (default: `http://localhost:1234`)
- Recommended model: **Qwen2.5-Coder-7B-Instruct Q4_K_M** (~4.7 GB download)

**LM Studio server settings (critical)**

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
# LM Studio (default — no extra flags needed)
python scan.py /path/to/code

# OpenAI
python scan.py /path/to/code --openai --api-key sk-...

# Anthropic
python scan.py /path/to/code --anthropic --api-key sk-ant-...

# AWS Bedrock (ambient credentials)
python scan.py /path/to/code --bedrock --aws-region us-east-1

# Azure AI Foundry
python scan.py /path/to/code --azure \
    --endpoint https://my-resource.openai.azure.com \
    --api-key <your-key> \
    --azure-deployment gpt-4o

# Google Gemini
python scan.py /path/to/code --gemini --api-key AIza...

# Scan a single file with any backend
python scan.py /path/to/code --openai --api-key sk-... --file src/Auth.cs

# Limit to first 10 files (useful for testing)
python scan.py /path/to/code --max-files 10

# Run OWASP pre-scan on every file, then full pipeline
python scan.py /path/to/code --pre-scan
```

---

## scan.py — Full pipeline orchestrator

Runs each file through all seven pipeline stages and writes a full artifact set per file.

### Provider selection flags

Exactly one provider flag may be used per invocation. If none is given, `--lmstudio` is the default.

| Flag | Provider | Default endpoint |
|---|---|---|
| `--lmstudio` | LM Studio local server | `http://localhost:1234/v1` |
| `--openai` | OpenAI API | `https://api.openai.com/v1` |
| `--anthropic` | Anthropic API (native SDK) | `https://api.anthropic.com` |
| `--bedrock` | AWS Bedrock (boto3 converse) | Regional (e.g. `bedrock-runtime.us-east-1.amazonaws.com`) |
| `--azure` | Azure AI Foundry | **Required via `--endpoint`** |
| `--gemini` | Google Gemini (native SDK) | `https://generativelanguage.googleapis.com` |

### Common endpoint and auth flags

| Flag | Description |
|---|---|
| `--endpoint URL` | Override the provider's default API endpoint. Required for `--azure`. Credentials embedded in URLs (e.g. `user:secret@host`) are automatically redacted from log output. Only `http://` and `https://` schemes are accepted. |
| `--api-key KEY` | API key for the selected provider. Falls back to the environment variable for that provider if omitted. |
| `--model ID` | Model to use. If omitted, provider defaults apply (LM Studio auto-detects from server; others use a sensible default). |

### AWS Bedrock flags

| Flag | Default | Description |
|---|---|---|
| `--aws-region` | `us-east-1` | AWS region for the Bedrock runtime endpoint |
| `--aws-profile` | | Named profile from `~/.aws/credentials` |
| `--aws-access-key` | | Explicit AWS access key ID |
| `--aws-secret-key` | | Explicit AWS secret access key |
| `--aws-session-token` | | Session token for temporary credentials / assume-role |

**Bedrock credential priority:** explicit key flags → `--aws-profile` → ambient chain (env vars, instance role, SSO).

### Azure AI Foundry flags

| Flag | Default | Description |
|---|---|---|
| `--azure-deployment` | *(same as `--model`)* | Azure deployment name when different from the model ID |
| `--azure-api-version` | `2024-02-01` | Azure OpenAI API version string |

### Environment variable fallbacks

| Variable | Provider |
|---|---|
| `OPENAI_API_KEY` | `--openai` |
| `ANTHROPIC_API_KEY` | `--anthropic` |
| `AZURE_OPENAI_API_KEY` | `--azure` |
| `GEMINI_API_KEY` or `GOOGLE_API_KEY` | `--gemini` |
| `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_DEFAULT_REGION` | `--bedrock` (standard boto3 env vars) |

### Provider default models

| Provider | Default model |
|---|---|
| LM Studio | Auto-detected from server |
| OpenAI | `gpt-4o` |
| Anthropic | `claude-sonnet-4-5` |
| Bedrock | `anthropic.claude-3-5-sonnet-20241022-v2:0` |
| Azure | `gpt-4o` |
| Gemini | `gemini-2.0-flash` |

### Scanner options

| Flag | Default | Description |
|---|---|---|
| `directory` | *(required)* | Root directory to scan |
| `--file` | | Scan a single file instead of the whole directory |
| `--config` | `agents.yaml` | Path to pipeline config |
| `--out` | `scan_results` | Output directory for all artifacts |
| `--max-files` | `50` | Max files to scan (0 = unlimited) |
| `--max-chars` | `16000` | Max characters of file content sent per agent call |
| `--max-tokens` | `3000` | Base generation budget (per-agent floors apply — see below) |
| `--retries` | `2` | Retry attempts per agent on JSON parse failure |
| `--policy` | | Path to a custom gate policy text file |
| `--patterns` | | Path to org coding standards / patterns text file |
| `--arch` | | Path to architecture constraints text file |
| `--extensions` | | Extra file extensions to include, comma-separated (e.g. `.jsx,.tsx`) |
| `--pre-scan` | | Run the automated OWASP pre-scan (Stage 0) on every file |
| `--prescan-file` | | Load a manually-produced pre-scan JSON (single-file mode only) |

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

If you see `Response truncated` errors on a specific agent, increase its floor in `scan.py` under `AGENT_MIN_TOKENS`.

### Output structure

```
scan_results/
  Auth.cs/
    scope.json              Scope agent output
    threat.json             Threat model
    hypotheses.json         Vulnerability hypotheses
    evidence.json           Confirmed / Refuted / Inconclusive findings
    fix.json                Proposed fixes (NOT applied to codebase)
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

> **Fixes are proposals, not patches.** `fix.json` contains recommended changes. Findings remain open until the code is actually changed and re-scanned.

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

## parse_findings.py — Results consolidator and report exporter

Walks a directory of scan output folders (one subdirectory per scan set), consolidates findings from all five pipeline JSON files, and produces a single summary report and a Jira-importable CSV. Designed to run after `scan.py` has produced its output.

### How scan sets are discovered

Each subdirectory that contains at least one recognised pipeline file is treated as a scan set. Files are matched by suffix — leading numeric timestamp prefixes (e.g. `1775963083761_evidence.json`) are stripped automatically.

```
scan_results/
  AddNewUser_scan/
    evidence.json       → confirmed findings (primary source)
    fix.json            → remediation details per finding
    gate.json           → gate decision, blockers, required human review
    pre_scan.json       → pre-scan findings (optional)
    scope.json          → scope metadata and risk signal
  Login_scan/
    1234_evidence.json  → timestamp-prefixed filenames handled automatically
    1234_fix.json
    ...
```

### Data sources per finding

| File | What is extracted |
|---|---|
| `evidence.json` | Finding key, title, severity, category, confidence, locations, code excerpts, trace |
| `fix.json` | Minimal fix, better fix, required tests, logging guidance (joined by `finding_key`) |
| `gate.json` | Blocker status, gate decision, required human review items |
| `pre_scan.json` | Any pre-scan findings not already covered by evidence findings |
| `scope.json` | Repo name, PR label, risk signal |

### CLI options

| Flag | Default | Description |
|---|---|---|
| `root_dir` | *(required)* | Root directory containing scan subdirectories |
| `--output-dir` | *(root_dir)* | Directory for output files |
| `--summary-file` | `findings_summary.txt` | Human-readable consolidated report filename |
| `--csv-file` | `findings_jira.csv` | Jira-importable CSV filename |

### Usage examples

```bash
# Basic — outputs to scan_results/
python parse_findings.py ./scan_results

# Write reports to a separate directory
python parse_findings.py ./scan_results --output-dir ./reports

# Custom filenames
python parse_findings.py ./scan_results \
    --output-dir ./reports \
    --summary-file security_report.txt \
    --csv-file jira_tickets.csv
```

### Output files

| File | Description |
|---|---|
| `findings_summary.txt` | Full human-readable report — gate decisions per scan set, severity and category breakdowns, per-scan finding counts table, per-finding detail with code excerpts and fix proposals, required human review, and follow-up actions |
| `findings_jira.csv` | Two-column CSV (`Summary`, `Description`) for Jira bulk import. Each row is globally unique — `Summary` is prefixed with `[scan_id][BLOCKER?][SEVERITY][CATEGORY]` so identical finding keys from different scan sets are distinguishable |

### findings_jira.csv Summary format

```
[scan_id][BLOCKER][HIGH][AuthN] FND-001 — Commented-out username/password validation logic
[scan_id][MEDIUM][DataLeak] FND-002 — Unconditional Console.WriteLine leaks internal state
```

The `Description` field uses Jira wiki markup and includes: severity, category, rule ID, affected files and lines, description, remediation (minimal and better), required tests, logging guidance, required human review items, and follow-up actions.

---

## summary_to_csv.py — Detailed findings CSV exporter

Reads a `findings_summary.txt` file produced by `parse_findings.py` and exports a flat CSV with one row per finding, expanding all fields individually. Useful for tracking in spreadsheets, importing into ticketing systems beyond Jira, or feeding into downstream tooling.

### CLI options

| Flag | Default | Description |
|---|---|---|
| `summary_file` | *(required)* | Path to `findings_summary.txt` |
| `--output` / `-o` | `detailed_findings.csv` (next to input) | Output CSV path |

### Usage examples

```bash
python summary_to_csv.py findings_summary.txt
python summary_to_csv.py findings_summary.txt --output reports/detailed.csv
python summary_to_csv.py reports/findings_summary.txt -o reports/detailed_findings.csv
```

### CSV columns

| Column | Description |
|---|---|
| `Finding ID` | Globally unique: `[scan_id]-[finding_key]` (e.g. `AddNewUser_scan-FND-001`) |
| `Title` | Short description of the finding |
| `Severity` | `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, `INFO`, or `UNKNOWN` |
| `Category` | Vulnerability category (e.g. `AuthN`, `DataLeak`, `BusinessLogic`) |
| `File` | Affected file path(s) |
| `Line(s)` | Affected line number(s) or range |
| `Description` | Notes content from the fix recommendation (duplicate trace/excerpt content stripped) |
| `Trace` | Execution / call trace from source to sink |
| `Code Excerpt` | Verbatim code block from the finding (first excerpt only) |
| `Fix (minimal)` | One-sentence summary of the minimal safe fix |
| `Fix (better)` | One-sentence summary of the preferred enhanced fix |
| `Tests Needed` | Required regression tests, pipe-separated (`test_name — proof \| test_name — proof`) |

A terminal preview is printed showing all findings in a compact table before the file is written.

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
  base_url: "http://localhost:1234/v1"   # overridden by --endpoint at runtime
  api_key: "local-lm-studio"             # value doesn't matter for LMStudio
  temperature: 0                         # always 0 — reproducible output
  max_tokens: 16000                      # upper ceiling; per-agent floors override upward
  per_request_timeout: 600              # seconds before a single agent call times out
  presence_penalty: 0.0                 # set to 1.5 for Qwen3.5 / reasoning models

shared_definitions:                     # severity levels, confidence rubric, OWASP crosswalk
  ...

review:
  max_context_chars: 20000             # max file content chars sent to each agent
  include_extensions: [...]

agents:
  scope:      { system: ..., user_template: ... }
  threat:     { ... }
  hypotheses: { ... }
  evidence:   { ... }
  fix:        { ... }
  gate:       { ... }
```

The gate policy lives inside `agents.gate.user_template` and can be overridden at runtime with `--policy path/to/policy.txt`. For more information on policy file format, see `gate_policy.md`.

---

## Optional: LMStudio pre-scan (Stage 0)

`lmstudio_system_prompt.txt` contains a system prompt for an initial OWASP sweep you can run directly in the LMStudio chat UI before invoking the pipeline. It produces a `pre_scan_json` blob (PRE-### findings) that feeds into the threat, hypotheses, evidence, and gate agents for deeper reconciliation.

To use it manually: paste the contents into LMStudio's System Prompt field, send your code file as the user message, and save the JSON response. To automate it, pass `--pre-scan` to `scan.py` or provide a saved response with `--prescan-file`.

---

## Security fixes

The following vulnerabilities were identified by static analysis (Cortex / Qwen Coder Next review) and remediated in `scan.py`. All fixes are present in the current version.

### CWE-573 — Lambda closure capture (`extract_json`)
**Was:** Four `lambda` expressions in a list literal used as a transform pipeline, including a no-op `lambda x: x` that static analysers flag as a potential closure capture bug.  
**Fixed:** Replaced with four named private functions (`_identity`, `_fix_ctrl`, `_repair`, `_fix_ctrl_repair`). Named functions are independently testable and unambiguous to analysis tools.

### CWE-61 — Symlink traversal (`collect_files`)
**Was:** `os.walk()` called without `followlinks=False`, allowing a symlink inside the scan tree to silently redirect traversal outside the intended root.  
**Fixed:** `os.walk(root, followlinks=False)` is now used at all call sites.

### CWE-22 — Path traversal (`safe_name` construction)
**Was:** Output directory names were derived from relative file paths using only a `re.sub` that stripped some special characters but left `..` sequences intact. A file path like `../../etc/cron.d/file` would have written output outside `scan_results/`.  
**Fixed:** Added explicit `..` collapse, null byte (`\x00`) stripping, leading dot/space trimming, a non-empty fallback, and a `validate_output_path()` function that resolves the full path and asserts it remains inside the output root via `Path.relative_to()`.

### CWE-73 — External control of file path via agent label (`call_agent`, `scan_file`)
**Was:** The `label` parameter was used directly in `f"_{label}_FAILED.txt"` and `f"_{name}.json"` path constructions with no validation.  
**Fixed:** `sanitise_label()` enforces an explicit allowlist (`_ALLOWED_AGENT_LABELS`) at the entry point of `call_agent` and inside `scan_file`'s inner `agent()` helper. Any value outside the allowlist raises `ValueError` before reaching the filesystem.

### CWE-532 — Credential exposure in logs (endpoint display)
**Was:** `args.endpoint` was printed verbatim in the startup banner and backend selection log line. A URL containing embedded credentials (e.g. `https://key:secret@api.host/v1`) would expose them to the terminal and any log aggregator.  
**Fixed:** `redact_url_credentials()` strips the userinfo component from any URL before display, replacing it with `***`.

### CWE-918 — SSRF via non-HTTP endpoint scheme (`build_backend`)
**Was:** No validation prevented `file://`, `ftp://`, or custom URI schemes from being passed as `--endpoint`, which could probe local filesystem paths or internal services through the HTTP client.  
**Fixed:** `validate_endpoint_url()` rejects any scheme outside `{http, https}` and verifies a hostname is present before the value reaches any backend constructor.

### CWE-400 — Resource exhaustion via oversized scan targets (`collect_files`)
**Was:** Files were read with `read_text()` regardless of size. An unexpectedly large file (e.g. a binary mistakenly matched by extension) could exhaust available memory.  
**Fixed:** `collect_files()` now calls `stat()` during collection and skips any file exceeding `_MAX_FILE_READ_BYTES` (16 MB) with a warning. The same limit is applied to all auxiliary input files (policy, patterns, arch, prescan, config).

### CWE-377 / TOCTOU race — Non-atomic file writes (all output paths)
**Was:** All output files were written with `Path.write_text()`. A process crash mid-write left a truncated or empty JSON file that subsequent runs could silently read as valid data. In concurrent use, a window existed between `mkdir()` and `write_text()` where another process could replace the directory with a symlink.  
**Fixed:** All seven output write sites now use `atomic_write_text()`, which writes to a sibling `.tmp` file via `tempfile.mkstemp()` (mode 0600, unpredictable name) then calls `os.replace()` — a POSIX atomic rename — to move it into place. The temp file is cleaned up on any write error.

### CWE-20 — Missing input validation on config and auxiliary files (`main`)
**Was:** `agents.yaml` and auxiliary text files (policy, patterns, arch, prescan) were read with bare `Path.read_text()` or broad `except Exception` catches, with no size limit and no validation that the YAML parsed as a mapping.  
**Fixed:** All file reads go through size-checked helpers. `yaml.YAMLError` and `json.JSONDecodeError` are caught specifically. The YAML config is validated as a `dict` after parsing. The prescan file is validated as a `dict` before use.

---

## Troubleshooting

**`TIMEOUT after Ns` on an agent**
- LMStudio GPU Offload is 0 — all inference is on CPU. Set GPU Offload to 99.
- Context Length is too high (e.g. 32768) — KV cache pre-allocation is slow even on GPU. Set to 8192.
- The agent's token floor is too high for your hardware. Reduce `AGENT_MIN_TOKENS` for that agent in `scan.py`.

**`Response truncated (finish_reason='length')`**
- The model hit its generation limit mid-JSON. Increase the agent's floor in `AGENT_MIN_TOKENS`.
- Confirm LMStudio Server → Max Generated Tokens is set to `-1`.

**`scope failed: ValueError` with trailing `}` or fences**
- The model wrapped its JSON in markdown fences. This is handled automatically. If you still see this, you may be running an older version of `scan.py`.

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

**Cloud provider authentication errors**
- OpenAI / Anthropic / Gemini: confirm the API key is correct and exported in the environment variable, or passed explicitly with `--api-key`.
- Azure: `--endpoint` is required and must be the full resource endpoint (e.g. `https://my-resource.openai.azure.com`).
- Bedrock: run `aws sts get-caller-identity` to confirm credentials are valid in the target region. If using a named profile, pass `--aws-profile`.
- All providers: endpoints must use `http://` or `https://` — other schemes are rejected for security reasons.

**`validate_output_path: path traversal detected`**
- A filename in the scan tree contains `..` sequences that would escape the output directory. The file is skipped automatically with an error entry in the results. Check the file path for unexpected characters.

---

## License

MIT
