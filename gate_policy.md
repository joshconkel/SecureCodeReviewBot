# Gate Policy File — Reference & Examples

The gate policy file is a plain-text file passed to the pipeline via `--policy`:

```bash
python scan_file.py "C:\path\to\code" --policy gate_policy.txt
```

When supplied, its contents replace the built-in default policy **entirely** — the gate
agent applies only the rules in your file. If omitted, the built-in default policy in
`agents.yaml → agents.gate.user_template` is used instead.

The gate agent reads the file as plain text injected into its prompt verbatim. Write rules
in the same imperative style as the default policy. The model copies the `policy_version`
string into `gate.json → audit.policy_version` and sets `policy_source: "caller_supplied"`
so you can tell from the artifact which policy was active during a scan.

---

## File format

```
POLICY VERSION: <identifier>

STEP 1 — EVALUATE FINDINGS (apply in order, stop at first match per finding):
- FAIL if: <condition>
- FAIL if: <condition>
- NEEDS_HUMAN if: <condition>
- PASS otherwise — ONLY if no FAIL or NEEDS_HUMAN conditions are met above

IMPORTANT: fixes_json contains PROPOSED fixes, not applied fixes. A finding with a
proposed fix is still an open finding. PASS must never be issued when a Critical or
High confirmed finding exists, regardless of whether a fix was proposed.

STEP 2 — INTER-AGENT VALIDATION (always check all, flag violations in warnings):
- Every FND-### in fixes_json must have a matching entry in evidence_json confirmed_findings_minimal.
  Flag orphaned fix IDs as type "orphaned_id" in warnings.
- Every blocker must reference a real FND-### from evidence. Flag orphaned IDs in warnings.
- All inconclusive_high_severity entries must appear in required_human_review.
- All uncovered_pre_scan_findings must appear in required_human_review unless Refuted.
- Any PRE-### not linked to a FND-### and not Refuted must be flagged in warnings
  as type "unreconciled_pre_scan_finding".
- Any Confirmed Critical or High FND-### with no entry in fixes_json must be flagged
  as type "unaddressed_finding" in warnings with the finding_key and severity.

PRE-SCAN RECONCILIATION — populate audit.pre_scan_coverage:
- covered:   PRE-### IDs that map to a FND-### in confirmed_findings_minimal
- refuted:   PRE-### IDs explicitly Refuted by the evidence agent
- uncovered: PRE-### IDs in neither category above (must trigger NEEDS_HUMAN)
```

**Rules:**
- Always include `POLICY VERSION:` — the gate agent copies this string into `audit.policy_version`
- Always include `STEP 2` and `PRE-SCAN RECONCILIATION` unchanged — these are structural invariants the gate needs regardless of your STEP 1 rules
- Only `STEP 1` rules should vary between policy files
- Use severity values exactly: `Critical`, `High`, `Medium`, `Low`
- Use category values exactly: `AuthN`, `AuthZ`, `Injection`, `SSRF`, `Deserialization`, `Crypto`, `Secrets`, `DataLeak`, `BusinessLogic`, `DoS`, `SupplyChain`, `Other`
- Confidence thresholds must be decimals: `0.7`, `0.8`, `0.9` — not percentages

---

## Decision semantics

| Decision | Meaning |
|---|---|
| `FAIL` | Do not merge. One or more blocking findings must be resolved and re-scanned. |
| `NEEDS_HUMAN` | Automated analysis is insufficient. A security engineer must review before merge. |
| `PASS` | No blocking findings detected in the code provided. Does **not** mean the code is secure — only that no findings met the block threshold given what was visible to the pipeline. |

---

## Example: default policy (mirrors built-in)

Use this as your starting point. Save as `gate_policy_default.txt`.

```
POLICY VERSION: default-v1

STEP 1 — EVALUATE FINDINGS (apply in order, stop at first match per finding):
- FAIL if: any Confirmed FND-### with severity Critical AND confidence >= 0.7
- FAIL if: any Confirmed AuthN or AuthZ FND-### with severity High AND confidence >= 0.8
- FAIL if: any Confirmed FND-### with severity Critical or High has NO matching entry
  in fixes_json (finding is confirmed but unaddressed — proposed fix does not count
  as resolution; fixes_json existing only means a fix was proposed, not applied)
- NEEDS_HUMAN if: any entry in inconclusive_high_severity with severity_if_true Critical or High
- NEEDS_HUMAN if: any Confirmed FND-### with severity High AND confidence between 0.5 and 0.79
- NEEDS_HUMAN if: any Confirmed FND-### with severity Critical AND confidence between 0.5 and 0.69
- NEEDS_HUMAN if: any uncovered_pre_scan_findings where reason_not_covered != "out_of_diff_scope"
- PASS otherwise — ONLY if no FAIL or NEEDS_HUMAN conditions are met above

IMPORTANT: fixes_json contains PROPOSED fixes, not applied fixes. A finding with a
proposed fix is still an open finding. PASS must never be issued when a Critical or
High confirmed finding exists, regardless of whether a fix was proposed.

STEP 2 — INTER-AGENT VALIDATION (always check all, flag violations in warnings):
- Every FND-### in fixes_json must have a matching entry in evidence_json confirmed_findings_minimal.
  Flag orphaned fix IDs as type "orphaned_id" in warnings.
- Every blocker must reference a real FND-### from evidence. Flag orphaned IDs in warnings.
- All inconclusive_high_severity entries must appear in required_human_review.
- All uncovered_pre_scan_findings must appear in required_human_review unless Refuted.
- Any PRE-### not linked to a FND-### and not Refuted must be flagged in warnings
  as type "unreconciled_pre_scan_finding".
- Any Confirmed Critical or High FND-### with no entry in fixes_json must be flagged
  as type "unaddressed_finding" in warnings with the finding_key and severity.

PRE-SCAN RECONCILIATION — populate audit.pre_scan_coverage:
- covered:   PRE-### IDs that map to a FND-### in confirmed_findings_minimal
- refuted:   PRE-### IDs explicitly Refuted by the evidence agent
- uncovered: PRE-### IDs in neither category above (must trigger NEEDS_HUMAN)
```

---

## Example: strict policy

Blocks on any High finding regardless of category or confidence. Suitable for
security-critical codebases (auth services, payment processing, PII handlers).
Save as `gate_policy_strict.txt`.

```
POLICY VERSION: strict-v1

STEP 1 — EVALUATE FINDINGS (apply in order, stop at first match per finding):
- FAIL if: any Confirmed FND-### with severity Critical AND confidence >= 0.5
- FAIL if: any Confirmed FND-### with severity High AND confidence >= 0.5
- FAIL if: any Confirmed FND-### with severity Critical or High has NO matching entry
  in fixes_json (finding is confirmed but unaddressed)
- FAIL if: any entry in inconclusive_high_severity with severity_if_true Critical or High
- NEEDS_HUMAN if: any Confirmed FND-### with severity Medium AND confidence >= 0.7
- NEEDS_HUMAN if: any Confirmed FND-### with severity Critical AND confidence between 0.3 and 0.49
- NEEDS_HUMAN if: any Confirmed FND-### with severity High AND confidence between 0.3 and 0.49
- NEEDS_HUMAN if: any uncovered_pre_scan_findings where reason_not_covered != "out_of_diff_scope"
- PASS otherwise — ONLY if no FAIL or NEEDS_HUMAN conditions are met above

IMPORTANT: fixes_json contains PROPOSED fixes, not applied fixes. A finding with a
proposed fix is still an open finding. PASS must never be issued when a Critical or
High confirmed finding exists, regardless of whether a fix was proposed.

STEP 2 — INTER-AGENT VALIDATION (always check all, flag violations in warnings):
- Every FND-### in fixes_json must have a matching entry in evidence_json confirmed_findings_minimal.
  Flag orphaned fix IDs as type "orphaned_id" in warnings.
- Every blocker must reference a real FND-### from evidence. Flag orphaned IDs in warnings.
- All inconclusive_high_severity entries must appear in required_human_review.
- All uncovered_pre_scan_findings must appear in required_human_review unless Refuted.
- Any PRE-### not linked to a FND-### and not Refuted must be flagged in warnings
  as type "unreconciled_pre_scan_finding".
- Any Confirmed Critical or High FND-### with no entry in fixes_json must be flagged
  as type "unaddressed_finding" in warnings with the finding_key and severity.

PRE-SCAN RECONCILIATION — populate audit.pre_scan_coverage:
- covered:   PRE-### IDs that map to a FND-### in confirmed_findings_minimal
- refuted:   PRE-### IDs explicitly Refuted by the evidence agent
- uncovered: PRE-### IDs in neither category above (must trigger NEEDS_HUMAN)
```

---

## Example: lenient policy

Allows High findings through with a warning. Suitable for development branches or
legacy codebases being incrementally hardened. Save as `gate_policy_lenient.txt`.

```
POLICY VERSION: lenient-v1

STEP 1 — EVALUATE FINDINGS (apply in order, stop at first match per finding):
- FAIL if: any Confirmed FND-### with severity Critical AND confidence >= 0.9
- FAIL if: any Confirmed AuthN or AuthZ FND-### with severity Critical AND confidence >= 0.7
- FAIL if: any Confirmed FND-### with severity Critical has NO matching entry in fixes_json
- NEEDS_HUMAN if: any Confirmed FND-### with severity Critical AND confidence between 0.5 and 0.89
- NEEDS_HUMAN if: any Confirmed AuthN or AuthZ FND-### with severity High AND confidence >= 0.8
- NEEDS_HUMAN if: any entry in inconclusive_high_severity with severity_if_true Critical
- NEEDS_HUMAN if: any uncovered_pre_scan_findings where reason_not_covered != "out_of_diff_scope"
- PASS otherwise — ONLY if no FAIL or NEEDS_HUMAN conditions are met above

IMPORTANT: fixes_json contains PROPOSED fixes, not applied fixes. A finding with a
proposed fix is still an open finding. PASS must never be issued when a Critical
confirmed finding exists, regardless of whether a fix was proposed.

STEP 2 — INTER-AGENT VALIDATION (always check all, flag violations in warnings):
- Every FND-### in fixes_json must have a matching entry in evidence_json confirmed_findings_minimal.
  Flag orphaned fix IDs as type "orphaned_id" in warnings.
- Every blocker must reference a real FND-### from evidence. Flag orphaned IDs in warnings.
- All inconclusive_high_severity entries must appear in required_human_review.
- All uncovered_pre_scan_findings must appear in required_human_review unless Refuted.
- Any PRE-### not linked to a FND-### and not Refuted must be flagged in warnings
  as type "unreconciled_pre_scan_finding".
- Any Confirmed Critical FND-### with no entry in fixes_json must be flagged
  as type "unaddressed_finding" in warnings with the finding_key and severity.

PRE-SCAN RECONCILIATION — populate audit.pre_scan_coverage:
- covered:   PRE-### IDs that map to a FND-### in confirmed_findings_minimal
- refuted:   PRE-### IDs explicitly Refuted by the evidence agent
- uncovered: PRE-### IDs in neither category above (must trigger NEEDS_HUMAN)
```

---

## Choosing a policy

| Codebase type | Recommended policy |
|---|---|
| Auth service, payment, PII handler | `strict-v1` |
| General production service | `default-v1` |
| Internal tooling, low-risk surface | `default-v1` with lenient confidence thresholds |
| Legacy codebase being incrementally hardened | `lenient-v1` |
| Development / feature branch pre-review | `lenient-v1` |

---

## What the gate.json audit block records

When you supply a policy file, `gate.json` will contain:

```json
"audit": {
  "policy_version": "strict-v1",
  "policy_source": "caller_supplied",
  "inputs_used": ["scope", "context_fetcher", "threat", "hypotheses", "evidence", "fixes", "pre_scan"],
  "inputs_missing": [],
  "pre_scan_coverage": {
    "covered":   ["PRE-001"],
    "refuted":   [],
    "uncovered": []
  }
}
```

`policy_source: "default"` means `--policy` was not supplied and the built-in policy from
`agents.yaml` was used. `policy_source: "caller_supplied"` means your file was active.
Use `policy_version` to correlate scan results with the policy that produced them.
