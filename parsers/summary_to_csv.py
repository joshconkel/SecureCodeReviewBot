#!/usr/bin/env python3
"""
Summary Report → Detailed CSV Exporter
=======================================
Reads a findings_summary.txt produced by parse_findings.py and extracts
every finding into a flat CSV with the following columns:

  Finding ID      — globally unique: [scan_id]-[finding_key]  e.g. scan_001-FND-001
  Title           — full finding title
  Severity        — CRITICAL / HIGH / MEDIUM / LOW / INFO / UNKNOWN
  Category        — e.g. AuthN, DataLeak, BusinessLogic
  File            — affected file path(s)
  Line(s)         — affected line numbers
  Description     — cleaned description (Notes content only, no duplicate trace/excerpt)
  Trace           — execution / call trace
  Code Excerpt    — verbatim code block from the finding
  Fix (minimal)   — minimal remediation guidance
  Fix (better)    — enhanced remediation guidance
  Tests Needed    — bullet list of required tests (joined with " | ")

Usage
-----
  python summary_to_csv.py <findings_summary.txt>
  python summary_to_csv.py <findings_summary.txt> --output detailed_findings.csv
  python summary_to_csv.py reports/findings_summary.txt --output reports/detailed.csv
"""

import re
import csv
import sys
import argparse
import textwrap
from pathlib import Path


# ---------------------------------------------------------------------------
# Field label patterns
# All labels are left-padded with two spaces and right-padded with spaces
# before the colon, e.g.:  "  Title        : "
# We capture everything after the colon (stripping leading space).
# ---------------------------------------------------------------------------

# Matches the opening line of a finding block:
#   "Finding #   1  [scan_001] FND-001  *** BLOCKER ***"
#   "Finding #  10  [scan_002] PRE-001"
RE_FINDING_HEADER = re.compile(
    r"^Finding\s+#\s*(\d+)\s+\[([^\]]+)\]\s+(\S+)(?:\s+\*+.*)?$"
)

# Matches a scan-set section header:
#   "Scan: scan_001"
RE_SCAN_HEADER = re.compile(r"^Scan:\s+(.+)$")

# Matches a labelled single-line field (label may have trailing spaces for alignment):
#   "  Title        : Some text"
#   "  Severity     : HIGH  (confidence 95%)"
RE_FIELD = re.compile(
    r"^  (Title|Severity|Category|File\(s\)|Line\(s\)|Trace)\s*:\s(.*)$"
)

# Multi-line block field openers — value starts on next line(s)
RE_CODE_EXCERPT = re.compile(r"^  Code excerpt\s*:\s*$")
RE_DESCRIPTION  = re.compile(r"^  Description\s*:\s*$")
RE_FIX_MINIMAL  = re.compile(r"^  Fix \(minimal\)\s*:\s*$")
RE_FIX_BETTER   = re.compile(r"^  Fix \(better\)\s*:\s*$")
RE_TESTS_NEEDED = re.compile(r"^  Tests needed\s*:\s*$")

# Bullet item inside Tests needed block
RE_BULLET = re.compile(r"^\s+[•\-\*]\s+(.+)$")

# Indented continuation line (4 spaces = content line inside a block)
RE_INDENTED = re.compile(r"^    (.*)$")

# Section separators / scan headers that signal end-of-findings-detail
RE_SECTION_SEP  = re.compile(r"^={10,}$")
RE_DASH_SEP     = re.compile(r"^[─\-]{10,}$")

# Severity cleanup — strip confidence annotation
RE_SEVERITY_CLEAN = re.compile(r"^(\w+)\s*(?:\(.*\))?$")

# Notes extractor from description block
RE_NOTES_LINE = re.compile(r"^Notes:\s+(.+)$", re.DOTALL)


# ---------------------------------------------------------------------------
# State machine parser
# ---------------------------------------------------------------------------

class FindingParser:
    """
    Line-by-line state machine that extracts finding records from the
    FINDINGS DETAIL section of findings_summary.txt.
    """

    def __init__(self):
        self.findings: list[dict] = []
        self._current: dict | None = None
        self._current_scan: str = ""

        # Current active multi-line block being accumulated
        self._block: str | None = None   # "code_excerpt" | "description" |
                                         # "fix_minimal" | "fix_better" | "tests"
        self._block_lines: list[str] = []

    # ── Public entry point ──────────────────────────────────────────────────

    def parse(self, text: str) -> list[dict]:
        """Parse the full report text and return a list of finding dicts."""
        in_detail = False

        for raw_line in text.splitlines():
            line = raw_line.rstrip()

            # Locate the FINDINGS DETAIL section
            if not in_detail:
                if "FINDINGS DETAIL" in line:
                    in_detail = True
                continue

            # Stop at REQUIRED HUMAN REVIEW or trailing separator after detail
            if "REQUIRED HUMAN REVIEW" in line or "RECOMMENDED FOLLOW-UPS" in line:
                self._flush_block()
                self._save_current()
                break

            self._process_line(line)

        # Save the last finding if we fell off the end of the file
        self._flush_block()
        self._save_current()

        return self.findings

    # ── Internal helpers ────────────────────────────────────────────────────

    def _process_line(self, line: str) -> None:
        # Scan-set section header
        m = RE_SCAN_HEADER.match(line)
        if m:
            self._flush_block()
            self._current_scan = m.group(1).strip()
            return

        # New finding header — save previous finding and start fresh
        m = RE_FINDING_HEADER.match(line)
        if m:
            self._flush_block()
            self._save_current()
            global_num  = m.group(1)
            scan_id     = m.group(2)
            finding_key = m.group(3)
            self._current_scan = scan_id   # keep in sync
            self._current = self._empty_finding(global_num, scan_id, finding_key)
            self._block = None
            return

        if self._current is None:
            return

        # ── Single-line labelled fields ──────────────────────────────────────
        m = RE_FIELD.match(line)
        if m:
            self._flush_block()
            label = m.group(1)
            value = m.group(2).strip()

            if label == "Title":
                self._current["Title"] = value
            elif label == "Severity":
                sm = RE_SEVERITY_CLEAN.match(value)
                self._current["Severity"] = sm.group(1) if sm else value
            elif label == "Category":
                self._current["Category"] = value
            elif label == "File(s)":
                self._current["File"] = value
            elif label == "Line(s)":
                self._current["Line(s)"] = value
            elif label == "Trace":
                self._current["Trace"] = value
            return

        # ── Multi-line block openers ─────────────────────────────────────────
        if RE_CODE_EXCERPT.match(line):
            self._flush_block()
            self._block = "code_excerpt"
            self._block_lines = []
            return
        if RE_DESCRIPTION.match(line):
            self._flush_block()
            self._block = "description"
            self._block_lines = []
            return
        if RE_FIX_MINIMAL.match(line):
            self._flush_block()
            self._block = "fix_minimal"
            self._block_lines = []
            return
        if RE_FIX_BETTER.match(line):
            self._flush_block()
            self._block = "fix_better"
            self._block_lines = []
            return
        if RE_TESTS_NEEDED.match(line):
            self._flush_block()
            self._block = "tests"
            self._block_lines = []
            return

        # ── Content lines inside an active block ─────────────────────────────
        if self._block:
            if self._block == "tests":
                # Tests are bullet lines
                bm = RE_BULLET.match(line)
                if bm:
                    self._block_lines.append(bm.group(1).strip())
                elif line.strip() == "":
                    pass  # blank lines inside test block are ok
                else:
                    # Non-bullet, non-blank = end of tests block
                    self._flush_block()
            else:
                # Indented continuation or blank
                im = RE_INDENTED.match(line)
                if im or line.strip() == "":
                    self._block_lines.append(im.group(1) if im else "")
                else:
                    # Anything non-indented ends the block
                    self._flush_block()
                    # Re-process this line in case it opens a new block
                    self._process_line(line)

    def _flush_block(self) -> None:
        """Commit the accumulated block lines into the current finding."""
        if self._current is None or self._block is None:
            self._block = None
            self._block_lines = []
            return

        # Strip trailing blank lines
        lines = self._block_lines
        while lines and lines[-1].strip() == "":
            lines.pop()

        text = "\n".join(lines).strip()

        if self._block == "code_excerpt":
            # Only store the first code excerpt; ignore duplicate
            if not self._current["Code Excerpt"]:
                self._current["Code Excerpt"] = text

        elif self._block == "description":
            # The description block re-embeds trace and code excerpt.
            # We only want the Notes line(s).
            notes = self._extract_notes(text)
            self._current["Description"] = notes

        elif self._block == "fix_minimal":
            self._current["Fix (minimal)"] = text

        elif self._block == "fix_better":
            self._current["Fix (better)"] = text

        elif self._block == "tests":
            self._current["Tests Needed"] = " | ".join(self._block_lines)

        self._block = None
        self._block_lines = []

    def _extract_notes(self, description_text: str) -> str:
        """
        Pull only the 'Notes: ...' portion out of the description block,
        which otherwise duplicates Trace and Code Excerpt content.
        Returns the raw notes string, or the full description if no Notes line.
        """
        for line in description_text.splitlines():
            m = RE_NOTES_LINE.match(line.strip())
            if m:
                return m.group(1).strip()
        # Fallback: return whatever isn't a trace/code-excerpt re-echo
        # by keeping only lines that don't start with "Trace:" or "Code excerpt:"
        kept = []
        skip_next_block = False
        for line in description_text.splitlines():
            ls = line.strip()
            if ls.startswith("Trace:") or ls.startswith("Code excerpt:"):
                skip_next_block = True
                continue
            if skip_next_block:
                if ls == "" or ls.startswith("/*") or re.match(r"^[a-zA-Z]", ls):
                    if ls == "":
                        skip_next_block = False
                    continue
            kept.append(line)
        return "\n".join(kept).strip()

    def _save_current(self) -> None:
        if self._current:
            self.findings.append(self._current)
        self._current = None

    @staticmethod
    def _empty_finding(global_num: str, scan_id: str, finding_key: str) -> dict:
        return {
            "Finding ID":   f"{scan_id}-{finding_key}",
            "Global #":     int(global_num),
            "Title":        "",
            "Severity":     "",
            "Category":     "",
            "File":         "",
            "Line(s)":      "",
            "Description":  "",
            "Trace":        "",
            "Code Excerpt": "",
            "Fix (minimal)":"",
            "Fix (better)": "",
            "Tests Needed": "",
        }


# ---------------------------------------------------------------------------
# CSV writer
# ---------------------------------------------------------------------------

CSV_FIELDS = [
    "Finding ID",
    "Title",
    "Severity",
    "Category",
    "File",
    "Line(s)",
    "Description",
    "Trace",
    "Code Excerpt",
    "Fix (minimal)",
    "Fix (better)",
    "Tests Needed",
]


def write_csv(findings: list[dict], output_path: Path) -> None:
    with open(output_path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for f in findings:
            writer.writerow({k: f.get(k, "") for k in CSV_FIELDS})
    print(f"Detailed CSV → {output_path}  ({len(findings)} row(s))")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Parse findings_summary.txt and export a detailed findings CSV.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            Examples:
              python summary_to_csv.py findings_summary.txt
              python summary_to_csv.py findings_summary.txt --output detailed.csv
              python summary_to_csv.py reports/findings_summary.txt \\
                  --output reports/detailed_findings.csv
        """),
    )
    p.add_argument("summary_file",
                   help="Path to the findings_summary.txt file to parse.")
    p.add_argument("--output", "-o", default=None,
                   help="Output CSV path (default: detailed_findings.csv next to input).")
    return p


def main() -> None:
    args    = build_parser().parse_args()
    src     = Path(args.summary_file).resolve()

    if not src.is_file():
        print(f"[ERROR] File not found: {src}", file=sys.stderr)
        sys.exit(1)

    out = Path(args.output).resolve() if args.output \
          else src.parent / "detailed_findings.csv"

    print(f"Reading : {src}")
    text = src.read_text(encoding="utf-8", errors="replace")

    parser   = FindingParser()
    findings = parser.parse(text)

    if not findings:
        print("[WARN] No findings extracted — check that the file contains "
              "a FINDINGS DETAIL section.", file=sys.stderr)
        sys.exit(1)

    print(f"Parsed  : {len(findings)} finding(s)")

    # Quick field preview in terminal
    print()
    print(f"{'#':<5} {'Finding ID':<25} {'Sev':<8} {'Title'}")
    print(f"{'-'*4}  {'-'*23}  {'-'*6}  {'-'*45}")
    for f in findings:
        title_preview = f["Title"][:48] + ("…" if len(f["Title"]) > 48 else "")
        print(f"{f['Global #']:<5} {f['Finding ID']:<25} {f['Severity']:<8} {title_preview}")

    print()
    write_csv(findings, out)


if __name__ == "__main__":
    main()
