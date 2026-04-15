#!/usr/bin/env python3
"""
Security Findings Parser & Jira CSV Report Generator
=====================================================
Designed for the llmster security-scan pipeline output format.

Walks a root directory recursively, groups JSON files into scan sets
(one per subdirectory), and produces a consolidated report across all sets.

Expected files per scan folder (matched by suffix, prefix timestamps ok):
  evidence.json   → confirmed findings  (primary source)
  fix.json        → remediation details per finding
  gate.json       → gate decision, blockers, required human review
  pre_scan.json   → pre-scan confirmed findings
  scope.json      → scope metadata and risk signal

Example layout
--------------
  scan_results/
    AddNewUser_scan/
      evidence.json
      fix.json
      gate.json
      pre_scan.json
      scope.json
    Login_scan/
      1234_evidence.json
      1234_fix.json
      ...

Outputs
-------
  findings_summary.txt   — consolidated human-readable report
  findings_jira.csv      — Jira-importable CSV (Summary + Description)
                           Each row is globally unique: [SCAN-ID][FND-KEY]

Usage
-----
  python parse_findings.py <root_directory>
  python parse_findings.py <root_directory> --output-dir ./reports
  python parse_findings.py <root_directory> --csv-file tickets.csv
"""

import os
import re
import sys
import json
import csv
import argparse
import textwrap
from datetime import datetime
from pathlib import Path
from collections import defaultdict


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

SEVERITY_RANK = {
    "CRITICAL": 5,
    "HIGH":     4,
    "MEDIUM":   3,
    "LOW":      2,
    "INFO":     1,
    "UNKNOWN":  0,
}

SEVERITY_TO_JIRA_PRIORITY = {
    "CRITICAL": "Highest",
    "HIGH":     "High",
    "MEDIUM":   "Medium",
    "LOW":      "Low",
    "INFO":     "Lowest",
    "UNKNOWN":  "Low",
}

# Recognised pipeline filenames — matched by suffix after stripping any
# leading timestamp prefix (e.g. "1775963083761_evidence.json" → "evidence")
PIPELINE_SUFFIXES = {
    "evidence",
    "fix",
    "gate",
    "pre_scan",
    "scope",
}

SKIP_DIRS = {".git", "node_modules", "__pycache__", "vendor", ".venv", "dist"}

SEP  = "=" * 80
SEP2 = "-" * 60


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_json(path: Path) -> dict | list | None:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        return json.loads(text) if text.strip() else None
    except (OSError, json.JSONDecodeError) as e:
        print(f"  [WARN] Could not load {path}: {e}", file=sys.stderr)
        return None


def normalise_severity(raw: str) -> str:
    aliases = {
        "CRIT":          "CRITICAL",
        "ERROR":         "HIGH",
        "WARN":          "MEDIUM",
        "WARNING":       "MEDIUM",
        "INFORMATIONAL": "INFO",
        "NOTE":          "INFO",
    }
    upper = (raw or "UNKNOWN").strip().upper()
    return aliases.get(upper, upper if upper in SEVERITY_RANK else "UNKNOWN")


def match_pipeline_key(filename: str) -> str | None:
    """
    Return the pipeline key for a filename, or None if unrecognised.

    Handles:
      evidence.json              → "evidence"
      1775963083761_evidence.json → "evidence"
      pre_scan.json              → "pre_scan"
      1234_pre_scan.json         → "pre_scan"
    """
    stem = Path(filename).stem.lower()          # strip .json
    # Strip leading numeric prefix if present (e.g. "1775963083761_evidence")
    if "_" in stem:
        stem = stem.split("_", 1)[1]            # "evidence"
        # Handle double-prefixed names just in case
        while "_" in stem and not any(stem == k for k in PIPELINE_SUFFIXES):
            candidate = stem.split("_", 1)[1]
            if any(candidate == k or candidate.startswith(k) for k in PIPELINE_SUFFIXES):
                stem = candidate
            else:
                break
    return stem if stem in PIPELINE_SUFFIXES else None


def fmt_locations(locations: list[dict]) -> str:
    parts = []
    for loc in locations or []:
        f = loc.get("file", "")
        l = loc.get("lines", "")
        parts.append(f"{f}:{l}" if l else f)
    return "; ".join(parts)


def wrap_block(text: str, width: int = 74, indent: str = "    ") -> str:
    if not text:
        return f"{indent}N/A"
    lines = []
    for para in str(text).splitlines():
        wrapped = textwrap.wrap(para, width) or [""]
        lines.extend(f"{indent}{line}" for line in wrapped)
    return "\n".join(lines)


def make_scan_id(folder: Path, index: int) -> str:
    """
    Human-readable scan identifier.  Uses the folder name; falls back to
    a zero-padded index so IDs are always unique.
    """
    name = folder.name.strip()
    return name if name else f"SCAN-{index:03d}"


# ---------------------------------------------------------------------------
# ScanSet — one directory of pipeline files
# ---------------------------------------------------------------------------

class ScanSet:
    def __init__(self, scan_id: str, folder: Path, file_map: dict[str, Path]):
        self.scan_id  = scan_id
        self.folder   = folder
        self.file_map = file_map
        self._cache: dict[str, object] = {}

    def _get(self, key: str) -> dict | list | None:
        if key not in self._cache:
            path = self.file_map.get(key)
            self._cache[key] = load_json(path) if path else None
        return self._cache[key]

    @property
    def evidence(self)  -> dict: return self._get("evidence")  or {}
    @property
    def fix(self)       -> dict: return self._get("fix")       or {}
    @property
    def gate(self)      -> dict: return self._get("gate")      or {}
    @property
    def pre_scan(self)  -> dict: return self._get("pre_scan")  or {}
    @property
    def scope(self)     -> dict: return self._get("scope")     or {}

    @property
    def repo(self) -> str:
        for src in (self.evidence, self.gate, self.scope):
            repo = (src.get("meta") or {}).get("repo") or \
                   (src.get("meta") or {}).get("repository")
            if repo:
                return repo
        return str(self.folder)

    @property
    def pr(self) -> str:
        for src in (self.evidence, self.scope):
            pr = (src.get("meta") or {}).get("pr")
            if pr:
                return pr
        return "unknown"

    @property
    def gate_decision(self) -> str:
        return self.gate.get("decision", "N/A")

    @property
    def files_present(self) -> list[str]:
        return sorted(self.file_map.keys())


# ---------------------------------------------------------------------------
# Directory walker
# ---------------------------------------------------------------------------

def find_scan_sets(root: Path) -> list[ScanSet]:
    """
    Walk root recursively.  Each directory that contains at least one
    recognised pipeline file becomes a ScanSet.
    """
    folder_files: dict[Path, dict[str, Path]] = defaultdict(dict)

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [
            d for d in sorted(dirnames)
            if not d.startswith(".") and d not in SKIP_DIRS
        ]
        folder = Path(dirpath)
        for fname in filenames:
            key = match_pipeline_key(fname)
            if key and key not in folder_files[folder]:   # first match wins
                folder_files[folder][key] = folder / fname

    # Build ScanSets sorted by folder path for stable ordering
    scan_sets = []
    for idx, folder in enumerate(sorted(folder_files.keys()), start=1):
        fmap = folder_files[folder]
        if not fmap:
            continue
        scan_id = make_scan_id(folder, idx)
        scan_sets.append(ScanSet(scan_id, folder, fmap))

    if not scan_sets:
        print("[WARN] No pipeline JSON files found under the root directory.",
              file=sys.stderr)
    return scan_sets


# ---------------------------------------------------------------------------
# Finding extraction
# ---------------------------------------------------------------------------

def _get_fix_summary(fix_data: dict, fix_key: str) -> str:
    return ((fix_data.get("recommended_change") or {})
            .get(fix_key) or {}).get("summary", "")


def _get_required_tests(fix_data: dict) -> list[str]:
    tests = (fix_data.get("tests") or {}).get("must_add") or []
    return [
        f"{t.get('name', '')} — {t.get('what_it_proves', '')}"
        for t in tests if isinstance(t, dict)
    ]


def _get_logging_avoid(fix_data: dict) -> list[str]:
    return (fix_data.get("logging_and_telemetry") or {}).get("avoid") or []


def _description_body(fnd: dict, fix_data: dict) -> str:
    parts = []
    trace = (fnd.get("evidence") or {}).get("trace")
    if trace:
        parts.append(f"Trace: {trace}")
    excerpts = (fnd.get("evidence") or {}).get("excerpts") or []
    if excerpts:
        parts.append(f"Code excerpt:\n{excerpts[0][:500]}")
    notes = fix_data.get("notes") or []
    if notes:
        parts.append("Notes: " + " | ".join(notes))
    return "\n\n".join(parts)


def extract_findings(ss: ScanSet) -> list[dict]:
    """
    Extract all confirmed findings from a ScanSet and enrich each with
    data from fix, gate, and scope files.

    Every finding dict carries 'scan_id' so it can be globally identified
    in reports spanning multiple scan sets.
    """
    seen_keys: set[str] = set()
    findings:  list[dict] = []

    # Build lookups from supporting files
    fix_lookup: dict[str, dict] = {
        fix.get("finding_key", ""): fix
        for fix in ss.fix.get("fixes") or []
        if fix.get("finding_key")
    }
    blocker_keys: set[str] = {
        b.get("finding_key", "")
        for b in ss.gate.get("blockers") or []
    }
    required_human_review = ss.gate.get("required_human_review") or []
    followups             = ss.fix.get("followups") or []

    # ── Primary source: evidence.json → confirmed_findings_minimal ──────────
    for fnd in ss.evidence.get("confirmed_findings_minimal") or []:
        key = fnd.get("finding_key") or fnd.get("id") or ""
        if key in seen_keys:
            continue
        seen_keys.add(key)

        fix_data  = fix_lookup.get(key, {})
        locations = (fnd.get("evidence") or {}).get("locations") or []

        findings.append({
            # Identification
            "scan_id":       ss.scan_id,
            "repo":          ss.repo,
            "pr":            ss.pr,
            "gate_decision": ss.gate_decision,
            "source":        "evidence",
            "finding_key":   key,
            "hypothesis_id": fnd.get("hypothesis_id", ""),
            # Core fields
            "title":       fnd.get("title", "Untitled Finding"),
            "severity":    normalise_severity(fnd.get("severity", "UNKNOWN")),
            "category":    fnd.get("category", "Unknown"),
            "confidence":  fnd.get("confidence", 0.0),
            "is_blocker":  key in blocker_keys,
            # Location
            "locations":   locations,
            "file_path":   fmt_locations(locations),
            "line_nums":   "; ".join(
                str(loc.get("lines", ""))
                for loc in locations if loc.get("lines")
            ),
            # Evidence
            "excerpts":    (fnd.get("evidence") or {}).get("excerpts") or [],
            "trace":       (fnd.get("evidence") or {}).get("trace", ""),
            "description": _description_body(fnd, fix_data),
            # Remediation
            "remediation_minimal": _get_fix_summary(fix_data, "minimal_fix"),
            "remediation_better":  _get_fix_summary(fix_data, "better_fix"),
            "tests_required":      _get_required_tests(fix_data),
            "logging_avoid":       _get_logging_avoid(fix_data),
            # Contextual
            "required_human_review": required_human_review,
            "followups":             followups,
        })

    # ── Supplementary: pre_scan.json → confirmed_findings ───────────────────
    for fnd in ss.pre_scan.get("confirmed_findings") or []:
        key = fnd.get("id", "")
        if key in seen_keys:
            continue
        seen_keys.add(key)

        location  = fnd.get("location") or {}
        locations = [location] if location else []

        findings.append({
            "scan_id":       ss.scan_id,
            "repo":          ss.repo,
            "pr":            ss.pr,
            "gate_decision": ss.gate_decision,
            "source":        "pre_scan",
            "finding_key":   key,
            "hypothesis_id": "",
            "title":         fnd.get("title", "Untitled Finding"),
            "severity":      normalise_severity(fnd.get("severity", "UNKNOWN")),
            "category":      fnd.get("owasp_category", "Unknown"),
            "confidence":    fnd.get("confidence", 0.0),
            "is_blocker":    False,
            "locations":     locations,
            "file_path":     fmt_locations(locations),
            "line_nums":     str(location.get("lines", "")),
            "excerpts":      [],
            "trace":         fnd.get("evidence", ""),
            "description":   fnd.get("impact", fnd.get("notes", "")),
            "remediation_minimal": "",
            "remediation_better":  "",
            "tests_required":      [],
            "logging_avoid":       [],
            "required_human_review": required_human_review,
            "followups":             followups,
        })

    # Sort within scan set: blockers first, then severity desc, then title
    findings.sort(key=lambda f: (
        not f["is_blocker"],
        -SEVERITY_RANK.get(f["severity"], 0),
        f["title"],
    ))
    return findings


# ---------------------------------------------------------------------------
# Jira field builders
# ---------------------------------------------------------------------------

def build_jira_summary(f: dict) -> str:
    """
    Globally unique one-line summary.

    Format: [scan_id][BLOCKER?][SEVERITY][CATEGORY] KEY — Title
    Example: [AddNewUser_scan][BLOCKER][HIGH][AuthN] FND-001 — Commented-out…
    """
    blocker  = "[BLOCKER]" if f["is_blocker"] else ""
    scan_tag = f"[{f['scan_id']}]"
    sev_tag  = f"[{f['severity']}]"
    cat_tag  = f"[{f['category']}]"
    key      = f["finding_key"]
    title    = f["title"][:90]
    return f"{scan_tag}{blocker}{sev_tag}{cat_tag} {key} — {title}"


def build_jira_description(f: dict) -> str:
    """Full Jira Description using wiki markup (*bold*)."""
    parts = []

    def h(text):
        parts.append(f"\n*{text}*")

    def add(label, value):
        if value:
            parts.append(f"*{label}:* {value}")

    h("Finding Metadata")
    add("Scan",          f["scan_id"])
    add("Repository",    f["repo"])
    add("PR / Scan",     f["pr"])
    add("Finding Key",   f["finding_key"])
    add("Hypothesis",    f["hypothesis_id"])
    add("Severity",      f["severity"])
    add("Priority",      SEVERITY_TO_JIRA_PRIORITY.get(f["severity"], "Low"))
    add("Category",      f["category"])
    add("Confidence",    f"{int(f['confidence'] * 100)}%")
    add("Gate Decision", f["gate_decision"])
    add("Is Blocker",    "YES — this finding blocks the PR gate"
                         if f["is_blocker"] else "No")

    if f["locations"]:
        h("Affected Locations")
        for loc in f["locations"]:
            file_  = loc.get("file", "")
            lines_ = loc.get("lines", "")
            parts.append(f"  • {file_}" + (f" (lines {lines_})" if lines_ else ""))

    if f["description"]:
        h("Description")
        parts.append(f["description"])

    if f["remediation_minimal"]:
        h("Remediation")
        add("Minimal fix", f["remediation_minimal"])
        add("Better fix",  f["remediation_better"])

    if f["tests_required"]:
        h("Required Tests")
        for t in f["tests_required"]:
            parts.append(f"  • {t}")

    if f["logging_avoid"]:
        h("Logging — Do NOT")
        for item in f["logging_avoid"]:
            parts.append(f"  ⚠ {item}")

    if f["required_human_review"]:
        h("Required Human Review")
        for rhr in f["required_human_review"]:
            area  = rhr.get("area", "")
            why   = rhr.get("why", "")
            where = "; ".join(
                f"{w.get('file', '')}:{w.get('lines', '')}"
                for w in rhr.get("where") or []
            )
            parts.append(f"  • {area}")
            if why:   parts.append(f"    Why: {why}")
            if where: parts.append(f"    Where: {where}")

    if f["followups"]:
        h("Follow-up Actions")
        for fu in f["followups"]:
            parts.append(
                f"  • [{fu.get('type','').upper()}] {fu.get('item','')}"
            )
            if fu.get("why"):
                parts.append(f"    Why: {fu['why']}")

    return "\n".join(parts).strip()


# ---------------------------------------------------------------------------
# Output: Summary report
# ---------------------------------------------------------------------------

def write_summary(all_findings: list[dict], scan_sets: list[ScanSet],
                  output_path: Path) -> None:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Aggregate stats
    sev_counts: dict[str, int] = {}
    cat_counts: dict[str, int] = {}
    blocker_count = 0
    for f in all_findings:
        sev_counts[f["severity"]] = sev_counts.get(f["severity"], 0) + 1
        cat_counts[f["category"]] = cat_counts.get(f["category"], 0) + 1
        if f["is_blocker"]:
            blocker_count += 1

    fail_count = sum(1 for ss in scan_sets if ss.gate_decision == "FAIL")
    pass_count = sum(1 for ss in scan_sets if ss.gate_decision == "PASS")

    with open(output_path, "w", encoding="utf-8") as fh:

        # ── Header ──────────────────────────────────────────────────────────
        fh.write(f"{SEP}\n")
        fh.write("SECURITY FINDINGS — CONSOLIDATED SUMMARY REPORT\n")
        fh.write(f"Generated   : {now}\n")
        fh.write(f"Scan sets   : {len(scan_sets)}  "
                 f"(FAIL: {fail_count}  PASS: {pass_count}  "
                 f"OTHER: {len(scan_sets) - fail_count - pass_count})\n")
        fh.write(f"Total       : {len(all_findings)} finding(s)  |  "
                 f"Blockers: {blocker_count}\n")
        fh.write(f"{SEP}\n\n")

        # ── Gate decisions per scan set ─────────────────────────────────────
        fh.write("GATE DECISIONS BY SCAN SET\n")
        fh.write(f"{SEP2}\n")
        fh.write(f"  {'Scan ID':<35} {'Decision':<10} {'Files Present'}\n")
        fh.write(f"  {'-'*33}  {'-'*8}  {'-'*30}\n")
        for ss in scan_sets:
            fh.write(
                f"  {ss.scan_id:<35} {ss.gate_decision:<10} "
                f"{', '.join(ss.files_present)}\n"
            )
        fh.write("\n")

        # ── Blocker summary ─────────────────────────────────────────────────
        blockers = [f for f in all_findings if f["is_blocker"]]
        if blockers:
            fh.write("BLOCKERS  (must be resolved before merge)\n")
            fh.write(f"{SEP2}\n")
            for b in blockers:
                fh.write(
                    f"  [{b['scan_id']}] {b['finding_key']} "
                    f"[{b['severity']}] {b['title']}\n"
                )
            fh.write("\n")

        # ── Severity breakdown ──────────────────────────────────────────────
        fh.write("SEVERITY BREAKDOWN\n")
        fh.write(f"{SEP2}\n")
        for sev in ["CRITICAL", "HIGH", "MEDIUM", "LOW", "INFO", "UNKNOWN"]:
            n = sev_counts.get(sev, 0)
            if n:
                fh.write(f"  {sev:<12} {n}\n")
        fh.write("\n")

        # ── Category breakdown ──────────────────────────────────────────────
        fh.write("CATEGORY BREAKDOWN\n")
        fh.write(f"{SEP2}\n")
        for cat, n in sorted(cat_counts.items()):
            fh.write(f"  {cat:<38} {n}\n")
        fh.write("\n")

        # ── Per-scan-set summary table ──────────────────────────────────────
        fh.write("PER-SCAN-SET FINDING COUNTS\n")
        fh.write(f"{SEP2}\n")
        fh.write(f"  {'Scan ID':<35} {'Total':>5}  {'Blockers':>8}  "
                 f"{'CRIT':>4}  {'HIGH':>4}  {'MED':>4}  {'LOW':>4}\n")
        fh.write(f"  {'-'*33}  {'-----':>5}  {'--------':>8}  "
                 f"{'----':>4}  {'----':>4}  {'----':>4}  {'----':>4}\n")

        by_scan: dict[str, list[dict]] = defaultdict(list)
        for f in all_findings:
            by_scan[f["scan_id"]].append(f)

        for ss in scan_sets:
            flist = by_scan.get(ss.scan_id, [])
            blk   = sum(1 for f in flist if f["is_blocker"])
            crit  = sum(1 for f in flist if f["severity"] == "CRITICAL")
            high  = sum(1 for f in flist if f["severity"] == "HIGH")
            med   = sum(1 for f in flist if f["severity"] == "MEDIUM")
            low   = sum(1 for f in flist if f["severity"] == "LOW")
            fh.write(
                f"  {ss.scan_id:<35} {len(flist):>5}  {blk:>8}  "
                f"{crit:>4}  {high:>4}  {med:>4}  {low:>4}\n"
            )
        fh.write("\n")

        # ── Findings detail (grouped by scan set) ───────────────────────────
        fh.write(f"{SEP}\n")
        fh.write("FINDINGS DETAIL  (grouped by scan set, blockers first)\n")
        fh.write(f"{SEP}\n")

        global_idx = 0
        for ss in scan_sets:
            flist = by_scan.get(ss.scan_id, [])
            if not flist:
                continue

            fh.write(f"\n{'─'*70}\n")
            fh.write(f"Scan: {ss.scan_id}\n")
            fh.write(f"Repo: {ss.repo}   PR/Scan: {ss.pr}   "
                     f"Gate: {ss.gate_decision}\n")
            fh.write(f"{'─'*70}\n\n")

            for f in flist:
                global_idx += 1
                blocker_tag = "  *** BLOCKER ***" if f["is_blocker"] else ""
                fh.write(
                    f"Finding #{global_idx:>4}  "
                    f"[{f['scan_id']}] {f['finding_key']}{blocker_tag}\n"
                )
                fh.write(f"  Title        : {f['title']}\n")
                fh.write(
                    f"  Severity     : {f['severity']}  "
                    f"(confidence {int(f['confidence']*100)}%)\n"
                )
                fh.write(f"  Category     : {f['category']}\n")
                fh.write(f"  File(s)      : {f['file_path']}\n")
                if f["line_nums"]:
                    fh.write(f"  Line(s)      : {f['line_nums']}\n")
                if f["trace"]:
                    fh.write(f"  Trace        : {f['trace']}\n")
                if f["excerpts"]:
                    fh.write("  Code excerpt :\n")
                    fh.write(wrap_block(f["excerpts"][0][:400]) + "\n")
                if f["description"]:
                    fh.write("  Description  :\n")
                    fh.write(wrap_block(f["description"]) + "\n")
                if f["remediation_minimal"]:
                    fh.write("  Fix (minimal):\n")
                    fh.write(wrap_block(f["remediation_minimal"]) + "\n")
                if f["remediation_better"]:
                    fh.write("  Fix (better) :\n")
                    fh.write(wrap_block(f["remediation_better"]) + "\n")
                if f["tests_required"]:
                    fh.write("  Tests needed :\n")
                    for t in f["tests_required"]:
                        fh.write(f"    • {t}\n")
                fh.write("\n")

        # ── Required human review (deduplicated across all scan sets) ────────
        seen_rhr: set[str] = set()
        all_rhr: list[tuple[str, dict]] = []
        for f in all_findings:
            for rhr in f["required_human_review"]:
                area = rhr.get("area", "")
                tag  = f"{f['scan_id']}::{area}"
                if tag not in seen_rhr:
                    seen_rhr.add(tag)
                    all_rhr.append((f["scan_id"], rhr))

        if all_rhr:
            fh.write(f"{SEP}\n")
            fh.write("REQUIRED HUMAN REVIEW\n")
            fh.write(f"{SEP}\n\n")
            for scan_id, rhr in all_rhr:
                fh.write(f"  Scan  : {scan_id}\n")
                fh.write(f"  Area  : {rhr.get('area', '')}\n")
                fh.write(f"  Why   : {rhr.get('why', '')}\n")
                where = rhr.get("where") or []
                if where:
                    fh.write(f"  Where : {fmt_locations(where)}\n")
                fh.write("\n")

        # ── Follow-ups (deduplicated across all scan sets) ───────────────────
        seen_fu: set[str] = set()
        all_fu: list[tuple[str, dict]] = []
        for f in all_findings:
            for fu in f["followups"]:
                item = fu.get("item", "")
                tag  = f"{f['scan_id']}::{item}"
                if tag not in seen_fu:
                    seen_fu.add(tag)
                    all_fu.append((f["scan_id"], fu))

        if all_fu:
            fh.write(f"{SEP}\n")
            fh.write("RECOMMENDED FOLLOW-UPS\n")
            fh.write(f"{SEP}\n\n")
            for scan_id, fu in all_fu:
                fh.write(
                    f"  [{scan_id}] [{fu.get('type','').upper()}] "
                    f"{fu.get('item','')}\n"
                )
                if fu.get("why"):
                    fh.write(f"    Why: {fu['why']}\n")
                fh.write("\n")

    print(f"Summary report  → {output_path}")


# ---------------------------------------------------------------------------
# Output: Jira CSV
# ---------------------------------------------------------------------------

JIRA_FIELDS = ["Summary", "Description"]


def write_jira_csv(all_findings: list[dict], output_path: Path) -> None:
    with open(output_path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=JIRA_FIELDS)
        writer.writeheader()
        for f in all_findings:
            writer.writerow({
                "Summary":     build_jira_summary(f),
                "Description": build_jira_description(f),
            })
    print(f"Jira CSV        → {output_path}")


# ---------------------------------------------------------------------------
# Output: Structured findings CSV
# ---------------------------------------------------------------------------
#
# Columns match the requested report fields exactly.
# Description and Notes are stored as separate list fields on each finding.
# When a finding has multiple values for either field, it is expanded into
# one row per unique (description, note) combination so no data is lost and
# the identity columns (Title, Severity, Category, etc.) are repeated.
# ---------------------------------------------------------------------------

STRUCTURED_CSV_FIELDS = [
    "Scan ID",
    "Finding Key",
    "Is Blocker",
    "Title",
    "Severity",
    "Confidence",
    "Category",
    "File(s)",
    "Line(s)",
    "Trace",
    "Code Excerpt",
    "Notes",
    "Fix (minimal)",
    "Fix (better)",
    "Tests Needed",
]


def _clean_description(description_raw: str) -> str:
    """
    _description_body() pre-joins Trace, Code Excerpt, and Notes into one blob.
    In the structured CSV those are separate columns, so strip all three segments
    to avoid redundancy, keeping only any freeform text that doesn't fit elsewhere.
    """
    desc = re.sub(r"(^|\n\n)Trace:.*?(?=\n\n|$)", "", description_raw, flags=re.DOTALL).strip()
    desc = re.sub(r"(^|\n\n)Code excerpt:.*?(?=\n\n|$)", "", desc, flags=re.DOTALL).strip()
    desc = re.sub(r"(^|\n\n)Notes:.*?(?=\n\n|$)", "", desc, flags=re.DOTALL).strip()
    return desc


def _split_description_notes(description_raw: str, fix_notes: list[str]) -> list[tuple[str, str]]:
    """
    Return a list of (clean_description, note) pairs — one per note value.
    If there are no notes, returns a single pair with an empty note string.
    This drives the row-expansion logic in _build_structured_rows.
    """
    desc_clean = _clean_description(description_raw)
    if not fix_notes:
        return [(desc_clean, "")]
    return [(desc_clean, note) for note in fix_notes]


def _get_fix_notes(fix_data: dict) -> list[str]:
    """Return the notes list from a fix entry, or an empty list."""
    return [str(n) for n in (fix_data.get("notes") or []) if n]


def _build_structured_rows(f: dict, fix_lookup: dict[str, dict], codescan_key: str) -> list[dict]:
    """
    Convert one finding dict into one or more CSV row dicts.
    One row is produced per Notes value; all other columns repeat.
    """
    fix_data  = fix_lookup.get(f["finding_key"], {})
    fix_notes = _get_fix_notes(fix_data)
    notes_list = fix_notes if fix_notes else [""]

    # Tests: one entry per line; " — " (em dash) separates name from proof
    # in _get_required_tests — replace it with CRLF so each part gets its own line
    tests_parts = []
    for t in f.get("tests_required", []):
        tests_parts.append(t.replace(" \u2014 ", "\r\n").replace(" \u00e2\u20ac\u201d ", "\r\n"))
    tests_str = "\r\n".join(tests_parts)

    # Code excerpt — first only, capped for cell legibility
    excerpts = f.get("excerpts") or []
    excerpt  = excerpts[0][:500] if excerpts else ""

    rows = []
    for note in notes_list:
        rows.append({
            "Scan ID":       f["scan_id"],
            "Finding Key":   codescan_key,
            "Is Blocker":    "YES" if f["is_blocker"] else "NO",
            "Title":         f["title"],
            "Severity":      f["severity"],
            "Confidence":    f"{int(f['confidence'] * 100)}%",
            "Category":      f["category"],
            "File(s)":       f["file_path"],
            "Line(s)":       f["line_nums"],
            "Trace":         f.get("trace", ""),
            "Code Excerpt":  excerpt,
            "Notes":         note,
            "Fix (minimal)": f.get("remediation_minimal", ""),
            "Fix (better)":  f.get("remediation_better", ""),
            "Tests Needed":  tests_str,
        })
    return rows


def write_structured_csv(
    all_findings: list[dict],
    scan_sets: list[ScanSet],
    output_path: Path,
) -> None:
    """
    Write the structured findings CSV.
    Finding Key is assigned as CODESCAN-001, CODESCAN-002, … globally across
    all scan sets — one number per unique original finding_key, so expanded
    Notes rows share the same CODESCAN key as their parent finding.
    """
    fix_lookups, codescan_map = _build_fix_lookups_and_codescan_map(all_findings, scan_sets)
    all_rows = _collect_structured_rows(all_findings, fix_lookups, codescan_map)

    with open(output_path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=STRUCTURED_CSV_FIELDS)
        writer.writeheader()
        writer.writerows(all_rows)

    print(f"Structured CSV  → {output_path}")


def _build_fix_lookups_and_codescan_map(
    all_findings: list[dict],
    scan_sets: list,
) -> tuple[dict, dict]:
    """Shared setup used by both CSV and JSON writers."""
    fix_lookups: dict = {}
    for ss in scan_sets:
        fix_lookups[ss.scan_id] = {
            fix.get("finding_key", ""): fix
            for fix in ss.fix.get("fixes") or []
            if fix.get("finding_key")
        }
    codescan_map: dict = {}
    counter = 0
    for f in all_findings:
        pair = (f["scan_id"], f["finding_key"])
        if pair not in codescan_map:
            counter += 1
            codescan_map[pair] = f"CODESCAN-{counter:03d}"
    return fix_lookups, codescan_map


def _collect_structured_rows(
    all_findings: list[dict],
    fix_lookups: dict,
    codescan_map: dict,
) -> list[dict]:
    """Flat list of structured rows shared by CSV and JSON writers."""
    rows = []
    for f in all_findings:
        fix_lookup   = fix_lookups.get(f["scan_id"], {})
        codescan_key = codescan_map[(f["scan_id"], f["finding_key"])]
        rows.extend(_build_structured_rows(f, fix_lookup, codescan_key))
    return rows


def write_structured_json(
    all_findings: list[dict],
    scan_sets: list,
    output_path: Path,
) -> None:
    """
    Write findings as a JSON array with the same fields as the structured CSV.
    Tests Needed is stored as a list of strings (not CRLF-joined) for clean
    iteration by JSON consumers.
    """
    fix_lookups, codescan_map = _build_fix_lookups_and_codescan_map(all_findings, scan_sets)
    rows = _collect_structured_rows(all_findings, fix_lookups, codescan_map)

    json_rows = []
    for row in rows:
        r = dict(row)
        tests_raw = r.get("Tests Needed", "")
        r["Tests Needed"] = [t for t in tests_raw.split("\r\n") if t] if tests_raw else []
        json_rows.append(r)

    output_path.write_text(
        json.dumps(json_rows, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"Structured JSON → {output_path}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description=(
            "Parse a directory of llmster pipeline scan folders and export "
            "a consolidated Jira-ready CSV and summary report."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            Examples:
              python parse_findings.py ./scan_results
              python parse_findings.py ./scan_results --output-dir ./reports
              python parse_findings.py ./scan_results --csv-file tickets.csv
        """),
    )
    p.add_argument("root_dir",
                   help="Root directory containing scan subdirectories.")
    p.add_argument("--output-dir", default=None,
                   help="Directory for output files (default: root_dir).")
    p.add_argument("--summary-file", default="findings_summary.txt",
                   help="Summary report filename (default: findings_summary.txt).")
    p.add_argument("--structured-csv-file", default="findings_structured.csv",
                   help="Structured findings CSV filename (default: findings_structured.csv).")
    p.add_argument("--json", action="store_true",
                   help="Also export findings as a JSON file.")
    p.add_argument("--json-file", default="findings_structured.json",
                   help="JSON output filename (default: findings_structured.json).")
    return p


def main() -> None:
    args     = build_parser().parse_args()
    root_dir = Path(args.root_dir).resolve()

    if not root_dir.is_dir():
        print(f"[ERROR] Not a directory: {root_dir}", file=sys.stderr)
        sys.exit(1)

    output_dir = Path(args.output_dir).resolve() if args.output_dir else root_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n{'='*60}")
    print("Security Findings Parser — llmster pipeline (multi-scan)")
    print(f"{'='*60}")
    print(f"Root directory : {root_dir}")
    print(f"Output dir     : {output_dir}\n")

    # 1. Discover scan sets
    scan_sets = find_scan_sets(root_dir)
    print(f"Scan sets found: {len(scan_sets)}")
    for ss in scan_sets:
        print(f"  [{ss.scan_id}]  files: {', '.join(ss.files_present)}")
    print()

    # 2. Extract + collect findings
    all_findings: list[dict] = []
    for ss in scan_sets:
        findings = extract_findings(ss)
        blockers = sum(1 for f in findings if f["is_blocker"])
        print(
            f"  [{ss.scan_id}]  {len(findings)} finding(s)  "
            f"blockers={blockers}  gate={ss.gate_decision}"
        )
        all_findings.extend(findings)

    print(f"\nTotal findings : {len(all_findings)}")
    total_blockers = sum(1 for f in all_findings if f["is_blocker"])
    if total_blockers:
        print(f"Total blockers : {total_blockers}")
        for f in all_findings:
            if f["is_blocker"]:
                print(
                    f"  *** [{f['scan_id']}] {f['finding_key']} "
                    f"[{f['severity']}] {f['title']}"
                )

    if not all_findings:
        print("\nNo findings to report. Exiting.")
        return

    print()
    write_summary(all_findings, scan_sets, output_dir / args.summary_file)
    write_structured_csv(all_findings, scan_sets, output_dir / args.structured_csv_file)
    if args.json:
        write_structured_json(all_findings, scan_sets, output_dir / args.json_file)
    print(f"\nDone. {len(all_findings)} finding(s) exported.\n")


if __name__ == "__main__":
    main()
