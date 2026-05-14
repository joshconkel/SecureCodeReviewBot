#!/usr/bin/env python3
"""
list_findings.py — Flat listing of all hypotheses and confirmed findings
across one or more scan_file.py output directories, with file locations
and line numbers for manual cross-run comparison.

Intended use: comparing runs where the same vulnerability is described
differently so the automated cluster matching in analyse_runs.py may
not have grouped them correctly. Every hypothesis and confirmed finding
is listed verbatim so you can eyeball which ones are the same thing.

Usage:
    # List one run
    python list_findings.py run_01/

    # List multiple runs side-by-side (grouped by scanned file)
    python list_findings.py run_01/ run_02/ run_03/

    # Point at a parent folder containing all runs
    python list_findings.py --runs-dir all_runs/ --pattern "run_*"

    # Filter to a specific scanned file (partial match on safe-name)
    python list_findings.py run_01/ run_02/ --file CookieManager

    # Only show confirmed findings (skip hypotheses that were refuted/inconclusive)
    python list_findings.py run_01/ run_02/ --confirmed-only

    # Write Markdown report
    python list_findings.py run_01/ run_02/ --out listing/ --md

    # Write CSV for spreadsheet comparison
    python list_findings.py run_01/ run_02/ --out listing/ --csv

Output columns (terminal and CSV):
    run | scanned_file | stage | id | severity | category |
    title | status | confidence | locations | lines | trace | priority
"""

import argparse
import csv
import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    from rich.console import Console
    from rich.table import Table
    from rich import box
    HAS_RICH = True
    console = Console()
except ImportError:
    HAS_RICH = False
    console = None


# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

def cprint(msg: str, style: str = "") -> None:
    if HAS_RICH:
        console.print(msg, style=style)
    else:
        print(re.sub(r"\[/?[a-z_ ]+\]", "", msg))


def load_json(path: Path) -> dict | list | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def fmt_locations(locations: list[dict]) -> tuple[str, str]:
    """Return (files_str, lines_str) from an evidence locations list."""
    if not locations:
        return "—", "—"
    files = []
    lines = []
    for loc in locations:
        f = loc.get("file", "?")
        l = loc.get("lines", "?")
        files.append(f)
        lines.append(str(l))
    return " | ".join(files), " | ".join(lines)


def fmt_where_to_check(where: list[dict]) -> tuple[str, str]:
    """Return (files_str, symbols_str) from a hypothesis where_to_check list."""
    if not where:
        return "—", "—"
    files   = [w.get("file", "?") for w in where]
    symbols = [w.get("symbol_or_route", "") for w in where]
    return " | ".join(files), " | ".join(s for s in symbols if s)


SEV_ORDER = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3, "?": 4}


# ─────────────────────────────────────────────────────────────────────────────
# Data model
# ─────────────────────────────────────────────────────────────────────────────

class Row:
    """One display row — either a hypothesis or a confirmed finding."""
    __slots__ = (
        "run_label", "scanned_file",
        "stage",        # "hypothesis" | "confirmed" | "inconclusive" | "refuted"
        "id",           # HYP-### or FND-###
        "hyp_id",       # source HYP-### (for confirmed findings)
        "severity",
        "category",
        "title",
        "status",       # for evidence evaluations: Confirmed/Refuted/Inconclusive
        "confidence",   # float or None
        "files",        # pipe-separated file string
        "lines",        # pipe-separated lines string
        "symbols",      # symbol/route (hypotheses only)
        "trace",        # evidence trace
        "priority",     # P0/P1/P2 (hypotheses only)
        "linked_pre_scan",
        "raw",          # original dict for JSON output
    )

    def __init__(self, **kw: Any) -> None:
        for slot in self.__slots__:
            setattr(self, slot, kw.get(slot, ""))
        if self.confidence is None:
            self.confidence = ""

    @property
    def sev_order(self) -> int:
        return SEV_ORDER.get(self.severity, 4)


# ─────────────────────────────────────────────────────────────────────────────
# Extraction
# ─────────────────────────────────────────────────────────────────────────────

def extract_rows(
    run_label: str,
    scanned_file: str,
    hyp_data: dict | None,
    ev_data: dict | None,
    confirmed_only: bool,
) -> list[Row]:
    rows: list[Row] = []

    # ── Build HYP-id → hypothesis lookup ──
    hyp_lookup: dict[str, dict] = {}
    if hyp_data:
        for h in hyp_data.get("hypotheses", []):
            hid = h.get("id", "")
            if hid:
                hyp_lookup[hid] = h

    # ── Hypotheses ──
    if not confirmed_only and hyp_data:
        for h in hyp_data.get("hypotheses", []):
            files_str, symbols_str = fmt_where_to_check(h.get("where_to_check", []))
            rows.append(Row(
                run_label    = run_label,
                scanned_file = scanned_file,
                stage        = "hypothesis",
                id           = h.get("id", "?"),
                hyp_id       = h.get("id", "?"),
                severity     = h.get("severity_if_true", "?"),
                category     = h.get("category", "?"),
                title        = h.get("title", "?"),
                status       = "—",
                confidence   = "",
                files        = files_str,
                lines        = "—",
                symbols      = symbols_str,
                trace        = " | ".join(h.get("evidence_needed", [])),
                priority     = h.get("priority", "?"),
                linked_pre_scan = h.get("linked_pre_scan_id") or "—",
                raw          = h,
            ))

    # ── Evidence evaluations (all statuses) ──
    ev_eval_by_hyp: dict[str, dict] = {}
    if ev_data:
        for ev in ev_data.get("evaluations", []):
            hid = ev.get("hypothesis_id", "")
            if hid:
                ev_eval_by_hyp[hid] = ev

    # ── Confirmed findings (with full evidence detail) ──
    if ev_data:
        confirmed_ids: set[str] = set()

        for f in ev_data.get("confirmed_findings_minimal", []):
            hid             = f.get("hypothesis_id", "")
            ev_detail       = ev_eval_by_hyp.get(hid, {})
            ev_evidence     = ev_detail.get("evidence") or f.get("evidence") or {}
            locations       = ev_evidence.get("locations", [])
            files_str, lines_str = fmt_locations(locations)
            trace           = ev_evidence.get("trace", "")
            confirmed_ids.add(hid)

            rows.append(Row(
                run_label    = run_label,
                scanned_file = scanned_file,
                stage        = "confirmed",
                id           = f.get("finding_key", f.get("id", "FND-?")),
                hyp_id       = hid,
                severity     = f.get("severity", "?"),
                category     = f.get("category", "?"),
                title        = f.get("title", "?"),
                status       = "Confirmed",
                confidence   = f.get("confidence", ""),
                files        = files_str,
                lines        = lines_str,
                symbols      = "",
                trace        = trace,
                priority     = "",
                linked_pre_scan = f.get("linked_pre_scan_id") or "—",
                raw          = f,
            ))

        # ── Inconclusive high-severity (always show — relevant for comparison) ──
        if not confirmed_only:
            for inc in ev_data.get("inconclusive_high_severity", []):
                hid  = inc.get("hypothesis_id", "")
                hyp  = hyp_lookup.get(hid, {})
                files_str, symbols_str = fmt_where_to_check(hyp.get("where_to_check", []))

                rows.append(Row(
                    run_label    = run_label,
                    scanned_file = scanned_file,
                    stage        = "inconclusive",
                    id           = hid,
                    hyp_id       = hid,
                    severity     = inc.get("severity_if_true", hyp.get("severity_if_true", "?")),
                    category     = hyp.get("category", "?"),
                    title        = hyp.get("title", inc.get("blocking_gap", "?")),
                    status       = "Inconclusive",
                    confidence   = "",
                    files        = files_str,
                    lines        = "—",
                    symbols      = symbols_str,
                    trace        = inc.get("blocking_gap", ""),
                    priority     = hyp.get("priority", "?"),
                    linked_pre_scan = hyp.get("linked_pre_scan_id") or "—",
                    raw          = inc,
                ))

        # ── Refuted (show source hypothesis info for completeness) ──
        if not confirmed_only:
            for hid, ev in ev_eval_by_hyp.items():
                if ev.get("status") == "Refuted":
                    hyp        = hyp_lookup.get(hid, {})
                    ev_evidence = ev.get("evidence") or {}
                    locations   = ev_evidence.get("locations", [])
                    files_str, lines_str = fmt_locations(locations)

                    rows.append(Row(
                        run_label    = run_label,
                        scanned_file = scanned_file,
                        stage        = "refuted",
                        id           = hid,
                        hyp_id       = hid,
                        severity     = hyp.get("severity_if_true", "?"),
                        category     = hyp.get("category", "?"),
                        title        = hyp.get("title", "?"),
                        status       = "Refuted",
                        confidence   = ev.get("confidence", ""),
                        files        = files_str,
                        lines        = lines_str,
                        symbols      = "",
                        trace        = ev.get("refutation_evidence", ""),
                        priority     = hyp.get("priority", "?"),
                        linked_pre_scan = hyp.get("linked_pre_scan_id") or "—",
                        raw          = ev,
                    ))

    return rows


# ─────────────────────────────────────────────────────────────────────────────
# Directory walking
# ─────────────────────────────────────────────────────────────────────────────

def load_run(
    run_dir: Path,
    file_filter: str,
    confirmed_only: bool,
) -> list[Row]:
    all_rows: list[Row] = []
    run_label = run_dir.name

    for child in sorted(run_dir.iterdir()):
        if not child.is_dir() or child.name.startswith("_"):
            continue
        if file_filter and file_filter.lower() not in child.name.lower():
            continue

        hyp_data = load_json(child / "hypotheses.json")
        ev_data  = load_json(child / "evidence.json")

        rows = extract_rows(
            run_label    = run_label,
            scanned_file = child.name,
            hyp_data     = hyp_data,
            ev_data      = ev_data,
            confirmed_only = confirmed_only,
        )
        all_rows.extend(rows)

    return all_rows


# ─────────────────────────────────────────────────────────────────────────────
# Display helpers
# ─────────────────────────────────────────────────────────────────────────────

STAGE_COLOUR = {
    "hypothesis":   "dim",
    "confirmed":    "green",
    "inconclusive": "yellow",
    "refuted":      "red",
}

SEV_COLOUR = {
    "Critical": "bold red",
    "High":     "yellow",
    "Medium":   "cyan",
    "Low":      "dim",
}

STATUS_SYMBOL = {
    "hypothesis":   "HYP",
    "confirmed":    "✓",
    "inconclusive": "?",
    "refuted":      "✕",
}


def display_terminal(
    rows: list[Row],
    group_by_file: bool = True,
) -> None:
    """Print a rich table (or plain text) to stdout."""

    if not rows:
        cprint("[yellow]No rows to display.[/yellow]")
        return

    if not group_by_file:
        _render_table(rows, title="All findings")
        return

    # Group by scanned_file
    file_groups: dict[str, list[Row]] = {}
    for r in rows:
        file_groups.setdefault(r.scanned_file, []).append(r)

    for fname, frows in sorted(file_groups.items()):
        # Sub-group by run within each file
        run_groups: dict[str, list[Row]] = {}
        for r in frows:
            run_groups.setdefault(r.run_label, []).append(r)

        if len(run_groups) == 1:
            run_label = next(iter(run_groups))
            _render_table(frows, title=f"{fname}  [{run_label}]")
        else:
            # Multiple runs — show one table per run for easy side-by-side reading
            cprint(f"\n[bold underline]{fname}[/bold underline]")
            for run_label, rrows in sorted(run_groups.items()):
                _render_table(rrows, title=f"  {run_label}")


def _render_table(rows: list[Row], title: str = "") -> None:
    # Sort: severity, then stage (confirmed first), then id
    rows = sorted(rows, key=lambda r: (r.sev_order, r.stage != "confirmed", r.id))

    if HAS_RICH:
        t = Table(
            title       = title,
            box         = box.SIMPLE_HEAD,
            header_style= "bold",
            show_edge   = False,
            padding     = (0, 1),
            expand      = False,
        )
        t.add_column("Stage",    width=12,  no_wrap=True)
        t.add_column("ID",       width=9,   no_wrap=True)
        t.add_column("HYP src",  width=9,   no_wrap=True)
        t.add_column("Sev",      width=9,   no_wrap=True)
        t.add_column("Cat",      width=14,  no_wrap=True)
        t.add_column("Title",    max_width=44)
        t.add_column("Conf",     width=5,   no_wrap=True)
        t.add_column("Files",    max_width=30)
        t.add_column("Lines",    max_width=20)
        t.add_column("Symbols / Trace", max_width=36)
        t.add_column("Pri",      width=4,   no_wrap=True)
        t.add_column("PRE",      width=8,   no_wrap=True)

        for r in rows:
            sc  = STAGE_COLOUR.get(r.stage, "")
            svc = SEV_COLOUR.get(r.severity, "")
            sym = STATUS_SYMBOL.get(r.stage, r.stage)
            cf  = f"{float(r.confidence):.2f}" if r.confidence != "" else "—"

            detail = r.symbols if r.stage == "hypothesis" else r.trace

            t.add_row(
                f"[{sc}]{sym}[/{sc}]"        if sc else sym,
                r.id,
                r.hyp_id if r.hyp_id != r.id else "—",
                f"[{svc}]{r.severity}[/{svc}]" if svc else r.severity,
                r.category,
                r.title,
                cf,
                r.files,
                r.lines,
                (detail or "")[:80],
                r.priority or "—",
                r.linked_pre_scan,
            )

        console.print(t)

    else:
        # Plain text fallback
        print(f"\n{'─'*120}")
        print(f"  {title}")
        print(f"{'─'*120}")
        hdr = f"{'Stage':<13} {'ID':<9} {'HYP':<9} {'Sev':<9} {'Cat':<14} {'Conf':<5} {'Title':<44} {'Files':<30} {'Lines':<18}"
        print(hdr)
        print("─" * 120)
        for r in rows:
            sym = STATUS_SYMBOL.get(r.stage, r.stage)
            cf  = f"{float(r.confidence):.2f}" if r.confidence != "" else "—"
            hyp = r.hyp_id if r.hyp_id != r.id else "—"
            print(
                f"{sym:<13} {r.id:<9} {hyp:<9} {r.severity:<9} {r.category:<14} "
                f"{cf:<5} {r.title[:44]:<44} {r.files[:30]:<30} {r.lines[:18]:<18}"
            )


# ─────────────────────────────────────────────────────────────────────────────
# Cross-run diff view
# ─────────────────────────────────────────────────────────────────────────────

def display_cross_run_diff(
    all_rows: list[Row],
    runs: list[str],
) -> None:
    """
    For each scanned file, show a pivot: one row per unique title, one
    column per run, showing the status in each run. Useful for spotting
    findings present in some runs but absent or differently named in others.
    """
    cprint("\n[bold]Cross-run comparison (status per run)[/bold]")

    # Group by scanned_file
    file_groups: dict[str, list[Row]] = {}
    for r in all_rows:
        file_groups.setdefault(r.scanned_file, []).append(r)

    for fname, frows in sorted(file_groups.items()):
        # Build pivot: title_key → {run → list[Row]}
        # title_key = (stage_bucket, severity, title[:60])
        # We use the raw title here deliberately — this view is for manual
        # inspection of titles that are different across runs.
        pivot: dict[tuple, dict[str, list[Row]]] = {}
        for r in frows:
            # Group hypothesis and confirmed under the same HYP id so the
            # relationship is visible
            key = (r.hyp_id, r.stage, r.severity, r.title[:60])
            pivot.setdefault(key, {}).setdefault(r.run_label, []).append(r)

        if not pivot:
            continue

        cprint(f"\n[bold underline]{fname}[/bold underline]")

        if HAS_RICH:
            t = Table(
                box         = box.SIMPLE_HEAD,
                header_style= "bold",
                show_edge   = False,
                padding     = (0, 1),
            )
            t.add_column("HYP src",  width=9,  no_wrap=True)
            t.add_column("Stage",    width=12, no_wrap=True)
            t.add_column("Sev",      width=9,  no_wrap=True)
            t.add_column("Title",    max_width=44)
            t.add_column("Files",    max_width=28)
            t.add_column("Lines",    max_width=18)
            for run in sorted(runs):
                t.add_column(run[:14], width=10, no_wrap=True)

            # Sort by severity then hyp_id
            sorted_keys = sorted(
                pivot.keys(),
                key=lambda k: (SEV_ORDER.get(k[2], 4), k[0], k[1])
            )

            for key in sorted_keys:
                hyp_id, stage, sev, title = key
                run_map = pivot[key]

                # Collect files/lines from any run that has this row
                sample_rows = [r for rrows in run_map.values() for r in rrows]
                sample = sample_rows[0] if sample_rows else None
                files  = sample.files if sample else "—"
                lines  = sample.lines if sample else "—"

                sc  = STAGE_COLOUR.get(stage, "")
                svc = SEV_COLOUR.get(sev, "")
                sym = STATUS_SYMBOL.get(stage, stage)

                run_cells = []
                for run in sorted(runs):
                    if run in run_map:
                        cell_rows = run_map[run]
                        # Show confidence if confirmed
                        confs = [
                            f"{float(cr.confidence):.2f}"
                            for cr in cell_rows
                            if cr.confidence != ""
                        ]
                        cell = sym + (f" {confs[0]}" if confs else "")
                        cell_colour = STAGE_COLOUR.get(stage, "")
                        run_cells.append(
                            f"[{cell_colour}]{cell}[/{cell_colour}]"
                            if cell_colour else cell
                        )
                    else:
                        run_cells.append("[dim]—[/dim]")

                t.add_row(
                    hyp_id,
                    f"[{sc}]{sym}[/{sc}]" if sc else sym,
                    f"[{svc}]{sev}[/{svc}]" if svc else sev,
                    title,
                    files[:28],
                    lines[:18],
                    *run_cells,
                )

            console.print(t)

        else:
            print(f"\n  {'HYP':<9} {'Stage':<13} {'Sev':<9} {'Title':<44} " +
                  "  ".join(f"{r[:10]:<10}" for r in sorted(runs)))
            print("  " + "─" * 100)
            for key in sorted(pivot.keys(), key=lambda k: (SEV_ORDER.get(k[2], 4), k[0])):
                hyp_id, stage, sev, title = key
                run_map = pivot[key]
                sym = STATUS_SYMBOL.get(stage, stage)
                run_cells = [
                    (sym if run in run_map else "—") for run in sorted(runs)
                ]
                print(
                    f"  {hyp_id:<9} {sym:<13} {sev:<9} {title[:44]:<44} " +
                    "  ".join(f"{c:<10}" for c in run_cells)
                )


# ─────────────────────────────────────────────────────────────────────────────
# Markdown output
# ─────────────────────────────────────────────────────────────────────────────

def build_markdown(
    all_rows: list[Row],
    runs: list[str],
    confirmed_only: bool,
) -> str:
    md: list[str] = []
    md.append("# Hypothesis and findings listing")
    md.append(f"\n**Runs:** {', '.join(runs)}  |  "
              f"**Total rows:** {len(all_rows)}  |  "
              f"**Mode:** {'confirmed only' if confirmed_only else 'all stages'}\n")

    # Group by scanned_file
    file_groups: dict[str, list[Row]] = {}
    for r in all_rows:
        file_groups.setdefault(r.scanned_file, []).append(r)

    for fname, frows in sorted(file_groups.items()):
        md.append(f"\n---\n\n## {fname}\n")

        # Sub-group by run
        run_groups: dict[str, list[Row]] = {}
        for r in frows:
            run_groups.setdefault(r.run_label, []).append(r)

        for run_label, rrows in sorted(run_groups.items()):
            md.append(f"\n### Run: {run_label}\n")
            md.append("| Stage | ID | HYP src | Sev | Category | Title | "
                      "Conf | Files | Lines | Symbols / Trace | Pri | PRE |")
            md.append("|---|---|---|---|---|---|---|---|---|---|---|---|")

            rrows_sorted = sorted(
                rrows,
                key=lambda r: (r.sev_order, r.stage != "confirmed", r.id),
            )
            for r in rrows_sorted:
                sym  = STATUS_SYMBOL.get(r.stage, r.stage)
                cf   = f"{float(r.confidence):.2f}" if r.confidence != "" else "—"
                hyp  = r.hyp_id if r.hyp_id != r.id else "—"
                det  = (r.symbols if r.stage == "hypothesis" else r.trace) or "—"
                # Escape pipe chars inside cell content
                def esc(s: str) -> str:
                    return str(s).replace("|", "╎").replace("\n", " ")
                md.append(
                    f"| {sym} | {esc(r.id)} | {esc(hyp)} | {esc(r.severity)} | "
                    f"{esc(r.category)} | {esc(r.title)} | {cf} | "
                    f"{esc(r.files)} | {esc(r.lines)} | {esc(det[:80])} | "
                    f"{r.priority or '—'} | {esc(r.linked_pre_scan)} |"
                )

    # Cross-run diff section if multiple runs
    if len(runs) > 1:
        md.append("\n---\n\n## Cross-run status pivot\n")
        md.append("One row per (HYP-id, stage, severity, title). "
                  "Columns show status per run.\n")

        file_groups2: dict[str, list[Row]] = {}
        for r in all_rows:
            file_groups2.setdefault(r.scanned_file, []).append(r)

        for fname, frows in sorted(file_groups2.items()):
            md.append(f"\n### {fname}\n")
            header_runs = " | ".join(sorted(runs))
            md.append(f"| HYP src | Stage | Sev | Title | Files | Lines | {header_runs} |")
            md.append("|---|---|---|---|---|---|" + "|---|" * len(runs))

            pivot: dict[tuple, dict[str, list[Row]]] = {}
            for r in frows:
                key = (r.hyp_id, r.stage, r.severity, r.title[:60])
                pivot.setdefault(key, {}).setdefault(r.run_label, []).append(r)

            for key in sorted(pivot.keys(),
                               key=lambda k: (SEV_ORDER.get(k[2], 4), k[0])):
                hyp_id, stage, sev, title = key
                run_map = pivot[key]
                sym  = STATUS_SYMBOL.get(stage, stage)

                sample_rows = [r for rr in run_map.values() for r in rr]
                sample = sample_rows[0] if sample_rows else None
                files  = (sample.files if sample else "—").replace("|", "╎")
                lines  = (sample.lines if sample else "—").replace("|", "╎")

                run_cells = []
                for run in sorted(runs):
                    if run in run_map:
                        confs = [
                            f"{float(cr.confidence):.2f}"
                            for cr in run_map[run]
                            if cr.confidence != ""
                        ]
                        run_cells.append(sym + (f" {confs[0]}" if confs else ""))
                    else:
                        run_cells.append("—")

                run_cols = " | ".join(run_cells)
                md.append(
                    f"| {hyp_id} | {sym} | {sev} | {title[:60]} | "
                    f"{files[:28]} | {lines[:18]} | {run_cols} |"
                )

    return "\n".join(md)


# ─────────────────────────────────────────────────────────────────────────────
# CSV output
# ─────────────────────────────────────────────────────────────────────────────

def build_csv_rows(all_rows: list[Row]) -> list[dict]:
    out = []
    for r in all_rows:
        out.append({
            "run":            r.run_label,
            "scanned_file":   r.scanned_file,
            "stage":          r.stage,
            "id":             r.id,
            "hyp_src":        r.hyp_id,
            "severity":       r.severity,
            "category":       r.category,
            "title":          r.title,
            "status":         r.status,
            "confidence":     r.confidence,
            "files":          r.files,
            "lines":          r.lines,
            "symbols_route":  r.symbols,
            "trace":          r.trace,
            "priority":       r.priority,
            "linked_pre_scan": r.linked_pre_scan,
        })
    return out


# ─────────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────────

def collect_run_dirs(args: argparse.Namespace) -> list[Path]:
    dirs: list[Path] = []

    if getattr(args, "runs_dir", ""):
        base = Path(args.runs_dir)
        if not base.is_dir():
            sys.exit(f"ERROR: --runs-dir not found: {base}")
        pattern = getattr(args, "pattern", "*") or "*"
        dirs = sorted(
            c for c in base.glob(pattern)
            if c.is_dir() and not c.name.startswith("_")
        )

    for d in getattr(args, "run_dirs", []) or []:
        p = Path(d)
        if not p.is_dir():
            sys.exit(f"ERROR: run directory not found: {p}")
        dirs.append(p)

    if not dirs:
        sys.exit(
            "ERROR: no run directories found.\n"
            "Pass them as positional args or use --runs-dir."
        )
    return dirs


def main() -> None:
    ap = argparse.ArgumentParser(
        description=(
            "Flat listing of all hypotheses and confirmed findings across "
            "scan_file.py output directories, with file locations and line "
            "numbers for manual cross-run comparison."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    ap.add_argument(
        "run_dirs", nargs="*",
        help="One or more scan output directories (one per run).",
    )
    ap.add_argument(
        "--runs-dir", default="",
        help="Parent directory containing all run subdirectories.",
    )
    ap.add_argument(
        "--pattern", default="*",
        help="Glob pattern for run dirs under --runs-dir (default: *).",
    )
    ap.add_argument(
        "--file", default="",
        dest="file_filter",
        help="Only show results for scanned files whose safe-name contains this string.",
    )
    ap.add_argument(
        "--confirmed-only", action="store_true", default=False,
        help="Only list confirmed findings (skip hypotheses, refuted, inconclusive).",
    )
    ap.add_argument(
        "--diff", action="store_true", default=False,
        help=(
            "Show cross-run pivot table after the per-run listing — "
            "one row per (HYP-id, stage, title), one column per run, "
            "showing status in each run."
        ),
    )
    ap.add_argument(
        "--out", default="",
        help="Output directory for --md and --csv files.",
    )
    ap.add_argument(
        "--md", action="store_true", default=False,
        help="Write a Markdown report to --out/findings_listing.md.",
    )
    ap.add_argument(
        "--csv", action="store_true", default=False,
        help="Write a CSV to --out/findings_listing.csv.",
    )
    ap.add_argument(
        "--no-terminal", action="store_true", default=False,
        help="Suppress terminal output (useful when only --md or --csv is needed).",
    )

    args = ap.parse_args()

    run_dirs = collect_run_dirs(args)
    run_labels = [d.name for d in run_dirs]

    cprint(f"\n[bold]Loading {len(run_dirs)} run(s)...[/bold]")
    all_rows: list[Row] = []
    for d in run_dirs:
        cprint(f"  [dim]→ {d.name}[/dim]")
        rows = load_run(d, args.file_filter, args.confirmed_only)
        all_rows.extend(rows)
        cprint(f"    {len(rows)} row(s) loaded")

    if not all_rows:
        cprint("[yellow]No findings found — check directory structure.[/yellow]")
        sys.exit(0)

    cprint(f"\n[bold]Total rows:[/bold] {len(all_rows)}\n")

    # Terminal output
    if not args.no_terminal:
        display_terminal(all_rows, group_by_file=True)
        if args.diff and len(run_dirs) > 1:
            display_cross_run_diff(all_rows, run_labels)

    # File outputs
    if args.md or args.csv:
        if not args.out:
            args.out = "findings_listing"
        out_dir = Path(args.out)
        out_dir.mkdir(parents=True, exist_ok=True)

        if args.md:
            md_path = out_dir / "findings_listing.md"
            md_path.write_text(
                build_markdown(all_rows, run_labels, args.confirmed_only),
                encoding="utf-8",
            )
            cprint(f"\n[green]✓[/green] Markdown written → {md_path}")

        if args.csv:
            csv_path = out_dir / "findings_listing.csv"
            csv_rows = build_csv_rows(all_rows)
            with csv_path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=list(csv_rows[0].keys()))
                writer.writeheader()
                writer.writerows(csv_rows)
            cprint(f"[green]✓[/green] CSV written → {csv_path}")

    cprint("\n[bold]Done.[/bold]\n")


if __name__ == "__main__":
    main()
