# precommit-scan — Local developer pre-commit hook

`precommit_scan.py` is a single-agent scanner that runs on staged files at commit time. **Always exits 0 — warn-only.** The commit proceeds regardless of findings.

## Files

| File | Description |
|---|---|
| `precommit_scan.py` | Warn-only pre-commit hook scanner |
| `agents_precommit.yaml` | Configuration for the pre-commit hook scanner |
| `pre-commit-config.yaml` | pre-commit framework hook definition |

---

## Setup

**Option A: pre-commit framework (recommended)**

```bash
pip install pre-commit openai pyyaml rich
# Place precommit_scan.py, agents_precommit.yaml, and pre-commit-config.yaml in repo root
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

---

## CLI options

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

---

## Usage examples

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

---

## Environment variable overrides

| Variable | Description |
|---|---|
| `PRECOMMIT_LLM_BASE_URL` | Override `base_url` in config (default: `http://localhost:1234/v1`) |
| `PRECOMMIT_LLM_API_KEY` | Override `api_key` in config |
| `PRECOMMIT_LLM_MODEL` | Model name override |

---

## Config search order

The hook looks for `agents_precommit.yaml` in the following locations (first match wins):

1. Path passed via `--config`
2. `agents_precommit.yaml` (repo root)
3. `security/agents_precommit.yaml`
4. `.security/agents_precommit.yaml`
5. Same directory as `precommit_scan.py`

---

## Troubleshooting

**Pre-commit hook is too slow**
- Switch to `Qwen2.5-Coder-7B` if running a larger model — ~10–20s per file vs 40s+.
- Reduce `max_chars_per_file` in `agents_precommit.yaml` (default: 8000).
- Add `--skip-if-offline` so the hook is silent when LMStudio isn't loaded.

**Reasoning model producing only `<think>` blocks with no JSON**
- Set `presence_penalty: 1.5` in `agents_precommit.yaml`.
- This applies to Qwen3.5, QwQ, and DeepSeek-R1. Leave at `0.0` for Qwen2.5-Coder and other non-reasoning models.
