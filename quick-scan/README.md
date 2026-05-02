# quick-scan — Fast CI/CD pipeline scanner

`quick_scan.py` is a single-agent, single LLM call per file scanner designed to run in CI pipelines (Azure DevOps, GitHub Actions) as a PR gate. It scans only changed files from a git diff.

## Files

| File | Description |
|---|---|
| `quick_scan.py` | Fast single-agent scanner |
| `agents_quick.yaml` | Configuration for the fast single-stage scanner |

---

## Exit codes

| Code | Meaning |
|---|---|
| `0` | PASS — no significant findings |
| `1` | WARN — findings present but below fail threshold |
| `2` | FAIL — Critical/High findings above confidence threshold |
| `3` | ERROR — scanner error (treat as WARN to avoid false blocks) |

---

## CLI options

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

---

## Usage examples

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

---

## Output files

```
quick_scan_results/
  <safe_filename>/
    result.json             Per-file findings and gate decision
    raw_response.txt        Raw model output + finish_reason + elapsed time
  quick_scan_rollup.json    Consolidated results across all files
  quick_scan_summary.md     Markdown summary suitable for PR comments
```

---

## Azure DevOps integration

Add a step to your pipeline YAML that runs `quick_scan.py` and publishes the output as a build artifact. Required pipeline variables:

| Variable | Description |
|---|---|
| `LLM_BASE_URL` | LMStudio server URL or cloud API base URL |
| `LLM_API_KEY` | API key (`lm-studio` for local LMStudio) |
| `LLM_MODEL` | Model name |
| `QUICK_SCAN_WARN_ONLY` | Set to `true` to disable hard PR blocks during rollout |

### GitHub Actions

Use `--gha` to emit workflow annotations instead of ADO log commands:

```bash
python quick_scan.py src/ --gha
```

Findings appear as inline annotations on the PR diff.

---

## Troubleshooting

**Reasoning model producing only `<think>` blocks with no JSON**
- Set `presence_penalty: 1.5` in `agents_quick.yaml`.
- This applies to Qwen3.5, QwQ, and DeepSeek-R1. Leave at `0.0` for Qwen2.5-Coder and other non-reasoning models.
