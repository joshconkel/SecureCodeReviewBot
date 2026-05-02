# Local Agentic Code Security Scanner

Use an agentic AI approach with JSON artifact pipelines to perform an initial secure code review. Connect to a local LM Studio instance, a cloud provider, or any OpenAI-compatible endpoint, and start doing first-pass reviews.

The pipeline scans a directory of source files, runs each file through a chain of specialized security agents (scope → threat model → hypotheses → evidence → fix → gate), and produces structured JSON artifacts and a Markdown report per file, plus a merged summary across all files.

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

Each agent receives only the data it needs - the pipeline deliberately slims payloads between stages to stay within model context windows. All inter-agent data is written to disk as JSON so you can inspect, replay, or extend any stage independently.

![Agent Pipeline](Agent_Pipeline.png)

---

## Project structure

| Path | Description |
|---|---|
| [`scanner/`](scanner/README.md) | Full 7-stage pipeline orchestrator (`scan.py`). Supports LM Studio, OpenAI, Anthropic, Bedrock, Azure, Gemini. |
| [`quick-scan/`](quick-scan/README.md) | Fast single-agent CI/CD scanner (`quick_scan.py`). Designed as a PR gate for Azure DevOps and GitHub Actions. |
| [`precommit-scan/`](precommit-scan/README.md) | Warn-only local pre-commit hook (`precommit_scan.py`). Runs on staged files at commit time. |
| [`parsers/`](parsers/README.md) | Post-scan utilities. `parse_findings.py` consolidates scan output; `summary_to_csv.py` exports a detailed per-finding CSV. |
| [`policies/`](policies/README.md) | Gate policy format reference and example policy. (`gate_policy.txt`)|

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

> **GPU note:** On an 8 GB VRAM card (RTX 3070 Ti / 4060 Ti), Qwen2.5-Coder-7B Q4_K_M uses ~4.1 GB for weights + ~0.8 GB KV cache at 8192 context ≈ ~5 GB total, leaving comfortable headroom. Do not run a 14B model on 8 GB - it will split layers to CPU and become unusably slow.

---

## Quick start

```bash
# LM Studio (default - no extra flags needed)
python scanner/scan.py /path/to/code

# OpenAI
python scanner/scan.py /path/to/code --openai --api-key sk-...

# Anthropic
python scanner/scan.py /path/to/code --anthropic --api-key sk-ant-...

# AWS Bedrock (ambient credentials)
python scanner/scan.py /path/to/code --bedrock --aws-region us-east-1

# Azure AI Foundry
python scanner/scan.py /path/to/code --azure \
    --endpoint https://my-resource.openai.azure.com \
    --api-key <your-key> \
    --azure-deployment gpt-4o

# Google Gemini
python scanner/scan.py /path/to/code --gemini --api-key AIza...
```

See [`scanner/README.md`](scanner/README.md) for the full flag reference and usage examples.

---

## Supported languages and file types

### Source code
`.cs` `.py` `.rb` `.js` `.ts` `.java` `.go` `.php`

### Infrastructure as Code
`.tf` `.tfvars` `.bicep`

### Config and manifests
`.json` `.yml` `.yaml` `.config` `.xml` `.env` `.csproj` `.toml`
`requirements.txt` `package.json` `Gemfile` `Gemfile.lock` `package-lock.json` `poetry.lock`

Additional extensions from `scanner/agents.yaml → review.include_extensions` are merged in automatically. Use `--extensions` to add more at runtime without editing config.

---

## What's new

### Multi-provider LLM backend support (`scan.py`)

`scan.py` now supports six LLM backends selectable at runtime via a single CLI flag. LM Studio remains the default - no flags required for existing workflows.

| Provider | Flag | Auth |
|---|---|---|
| LM Studio (default) | `--lmstudio` | None (local) |
| OpenAI | `--openai` | `--api-key` or `OPENAI_API_KEY` |
| Anthropic | `--anthropic` | `--api-key` or `ANTHROPIC_API_KEY` |
| AWS Bedrock | `--bedrock` | Key flags, profile, or ambient credential chain |
| Azure AI Foundry | `--azure` | `--api-key` or `AZURE_OPENAI_API_KEY` |
| Google Gemini | `--gemini` | `--api-key` or `GEMINI_API_KEY` |

### New companion scripts

| Script | Purpose |
|---|---|
| `parsers/parse_findings.py` | Walks a directory of scan output folders, consolidates findings across all scan sets, produces `findings_summary.txt` and `findings_jira.csv` |
| `parsers/summary_to_csv.py` | Reads a `findings_summary.txt` file and exports a flat detailed CSV with one row per finding, including code excerpts, fix guidance, and test requirements |

---

## License

MIT
