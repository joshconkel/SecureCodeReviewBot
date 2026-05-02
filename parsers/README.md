# parsers — Post-scan results utilities

Two scripts for consolidating and exporting scan output produced by `scanner/scan.py`.

## Files

| File | Description |
|---|---|
| `parse_findings.py` | Walks a directory of scan output folders, consolidates findings across all scan sets, produces `findings_summary.txt` and `findings_jira.csv` |
| `summary_to_csv.py` | Reads a `findings_summary.txt` and exports a flat detailed CSV with one row per finding |

---

## parse_findings.py — Results consolidator

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

### Troubleshooting

**`parse_findings.py` reports no scan sets found**
- Ensure the directory contains subdirectories with at least one recognised file (`evidence.json`, `fix.json`, `gate.json`, `pre_scan.json`, or `scope.json`).
- Timestamp-prefixed filenames (e.g. `1234_evidence.json`) are handled automatically.

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
