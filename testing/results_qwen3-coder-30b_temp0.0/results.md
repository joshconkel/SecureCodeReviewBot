# Multi-Stage Agent Security Scan — Test Results Analysis

**Model:** `qwen3-coder-30b` · **Temperature:** `0.0` · **Passes:** 12 · **Target:** WebGoat.NET

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Test Configuration](#test-configuration)
3. [Pipeline Overview](#pipeline-overview)
4. [Hypothesis Generation](#hypothesis-generation)
5. [Confirmation Stage](#confirmation-stage)
6. [Inconclusive Findings](#inconclusive-findings)
7. [Aggregate Finding Statistics](#aggregate-finding-statistics)
8. [Confidence Score Analysis](#confidence-score-analysis)
9. [Detection Rate Analysis](#detection-rate-analysis)
10. [Gate Outcome Analysis](#gate-outcome-analysis)
11. [Cross-Run Consistency: Line-Number Keyed Analysis](#cross-run-consistency-line-number-keyed-analysis)
12. [Pass Group Structural Split](#pass-group-structural-split)
13. [Severity and Category Breakdown](#severity-and-category-breakdown)
14. [File-Level Findings](#file-level-findings)
15. [Interpretation](#interpretation)
16. [Limitations](#limitations)
17. [Recommended Next Steps](#recommended-next-steps)
18. [Appendix: Inconsistent Finding Groups](#appendix-inconsistent-finding-groups)

---

## Executive Summary

Twelve independent passes of a multi-stage security analysis agent were run against the WebGoat.NET codebase at temperature 0.0. The pipeline generated **2,424 hypotheses** across 50 source files, confirmed **1,372 findings**, and marked **900 as inconclusive** due to missing cross-reference context. After deduplication into 148 unique findings, **81 (54.7%)** achieved a detection rate of 1.0 — confirmed in every single pass. The remaining 67 findings split cleanly along a single structural boundary: a context window composition difference between passes p4–p7 and all other passes, not random model variance.

The critical diagnostic result is that **confidence score standard deviation is exactly 0.000 across every unique finding**. When the agent confirms a vulnerability, it assigns an identical confidence score in every pass that detects it. This is the expected signature of a deterministic system at temperature 0 and confirms the model itself is behaving reliably. All observed inconsistency is attributable to pipeline inputs (context window composition), not to model stochasticity.

---

## Test Configuration

| Parameter | Value |
|---|---|
| Model | `qwen3-coder-30b` |
| Temperature | `0.0` |
| Passes | 12 (`pass1` – `pass12`) |
| Target codebase | WebGoat.NET |
| Files scanned | 50 |
| Total pipeline rows | 4,696 |
| Analysis files | `findings_listing.csv`, `findings.csv` |

---

## Pipeline Overview

The agent operates in three sequential stages per file per pass:

1. **Hypothesis** — the agent reads the source file and generates candidate vulnerability hypotheses, each with a severity, category, and list of files and symbols needed for confirmation.
2. **Confirmation** — each hypothesis is verified against available context. If the required cross-reference files are present, the hypothesis is either confirmed (with a confidence score and line attribution) or rejected. If required files are absent, the finding is marked inconclusive.
3. **Gate evaluation** — confirmed findings are evaluated by a downstream gate that classifies them as `pass`, `fail`, or `needs_human` review.

```
Source file
    │
    ▼
[Hypothesis stage] ──► 2,424 hypotheses
    │
    ▼
[Confirmation stage] ──► 1,372 confirmed  │  900 inconclusive
    │
    ▼
[Gate evaluation] ──► pass / fail / needs_human
```

---

## Hypothesis Generation

Across all 12 passes and 50 files, the pipeline generated **2,424 hypotheses** — an average of **202 per pass** and **4.0 per file per pass**. Hypothesis count is perfectly stable: passes p1–p3 and p8–p12 each produced 114 confirmed findings, while p4–p7 each produced 115, a difference of one finding attributable to the context composition split discussed in [§ Pass Group Structural Split](#pass-group-structural-split).

---

## Confirmation Stage

Of the 2,424 hypotheses:

| Outcome | Count | Rate |
|---|---|---|
| Confirmed | 1,372 | 56.6% |
| Inconclusive | 900 | 37.1% |
| Rejected (implicit) | 152 | 6.3% |

The confirmation rate of **56.6%** reflects the agent's ability to validate hypotheses against available context. The high inconclusive rate (37.1%) is not a model failure — it is a direct consequence of cross-file hypotheses being generated for files whose dependencies were not included in the same context window. This is the primary structural issue identified in the consistency analysis.

Per-pass confirmed counts are nearly identical across all runs:

| Pass | Confirmed |
|---|---|
| pass1 | 114 |
| pass2 | 114 |
| pass3 | 114 |
| pass4 | 115 |
| pass5 | 115 |
| pass6 | 115 |
| pass7 | 115 |
| pass8 | 114 |
| pass9 | 114 |
| pass10 | 114 |
| pass11 | 114 |
| pass12 | 114 |

The one-finding difference between groups is deterministic and consistent — it reflects a genuine structural difference in context composition between the two pass groups, not random variation.

---

## Inconclusive Findings

**900 findings (37.1%)** were marked inconclusive, uniformly distributed across all 12 passes. Files with the highest inconclusive counts are those with the most cross-file dependencies:

| File | Inconclusive count (across 12 passes) |
|---|---|
| `App_Code/DB/IDbProvider.cs` | 48 |
| `App_Code/WeakRandom.cs` | 48 |
| `ChangePassword.aspx.cs` | 48 |
| `dbtest.aspx.designer.cs` | 48 |
| `ChangePassword.aspx.designer.cs` | 40 |
| `App_Code/CookieManager.cs` | 36 |
| `App_Code/DB/MySqlDbProvider.cs` | 36 |
| `App_Code/DB/SqliteDbProvider.cs` | 36 |
| `Code/SQLiteProfileProvider.cs` | 36 |
| `Code/SQLiteRoleProvider.cs` | 36 |

**15 files produced zero inconclusive findings**, indicating their hypotheses required no cross-file context or all required context was consistently available:

`AddNewUser.aspx.cs`, `App_Code/ConfigFile.cs`, `App_Code/CustomerLoginData.cs`, `App_Code/DB/DbProviderFactory.cs`, `App_Code/Encoder.cs`, `App_Code/Settings.cs`, `Configuration/Default.config`, `Content/About.aspx.cs`, `Content/About.aspx.designer.cs`, `Content/BasicAuth.aspx.cs`, `Content/Challenge1.aspx.cs`, `Content/Challenge1.aspx.designer.cs`, `Content/Challenge2.aspx.cs`, `Content/Challenge2.aspx.designer.cs`, `Content/Challenge3.aspx.cs`

These files are the most reliable scan targets in the current configuration and serve as a useful baseline for consistency benchmarking.

---

## Aggregate Finding Statistics

After cross-run deduplication, **148 unique findings** were identified.

| Metric | Value |
|---|---|
| Total unique findings | 148 |
| Stable (detection rate = 1.0) | 81 (54.7%) |
| Unstable (detection rate < 1.0) | 67 (45.3%) |
| Mean confidence score | 0.758 |
| Min confidence score | 0.300 |
| Max confidence score | 1.000 |
| Confidence std dev (any finding) | **0.000** |
| Files with ambiguous CI (spanning 0.5) | 67 |

The ambiguous CI count (67) matches exactly the number of unstable findings. These are findings where the 95% confidence interval straddles 0.5, meaning the true detection rate cannot be confidently placed above or below chance with 12 observations. This is addressed in detail in [§ Detection Rate Analysis](#detection-rate-analysis).

---

## Confidence Score Analysis

### Key finding: complete confidence determinism

The most diagnostic result in the dataset is the confidence standard deviation. For every unique finding across all 148 rows in `findings.csv`:

```
conf_std = 0.000  (universal — no exceptions)
conf_min = conf_max  (for every finding)
```

This means that when the agent confirms a finding, it assigns an **identical confidence score in every pass that detects it**. There is zero intra-finding confidence variance. This is the expected behavior of a deterministic inference system at temperature 0 and provides strong evidence that the model component of the pipeline is operating correctly.

### Confidence distribution

| Confidence value | Number of findings |
|---|---|
| 0.90 | 62 |
| 0.30 | 33 |
| 0.95 | 28 |
| 0.85 | 14 |
| 0.80 | 5 |
| 0.75 | 3 |
| 0.40 | 2 |
| 1.00 | 1 |

The bimodal distribution — with peaks at 0.90–0.95 and at 0.30 — reflects a structural pattern: findings confirmed from files that required cross-file context consistently receive confidence 0.30, while findings confirmed from self-contained context receive 0.85–0.95. The 0.30 cluster represents findings where the confirmation stage completed but with limited supporting evidence (the cross-reference file was in context for the batch, but only partially). This confidence split is itself consistent and deterministic across runs.

---

## Detection Rate Analysis

Only three detection rate values appear across all 148 findings: exactly 1.0, 0.6667 (8/12), and 0.3333 (4/12). The clean 1:2:3 ratio is not coincidental — it reflects the structured split between two pass groups identified in [§ Pass Group Structural Split](#pass-group-structural-split).

| Detection rate | Count | 95% CI lower | 95% CI upper | Stable? |
|---|---|---|---|---|
| 1.0000 (12/12) | 81 | 0.7575 | 1.0000 | Yes |
| 0.6667 (8/12) | 33 | 0.3906 | 0.8619 | No |
| 0.3333 (4/12) | 34 | 0.1381 | 0.6094 | No |

The wide confidence intervals for the 0.67 and 0.33 groups are a consequence of small-sample binomial estimation at n=12. With 12 observations, a true detection rate of 1.0 cannot be distinguished from 0.75 with certainty. Increasing the number of passes to 24 or 36 would narrow these intervals substantially and allow clearer discrimination between genuinely stable and genuinely marginal findings.

### Severity-stratified stability

Stability rates vary by severity, with Low-severity findings paradoxically achieving 100% stability:

| Severity | Total findings | Stable (100% det.) | Stability rate |
|---|---|---|---|
| Critical | 5 | 2 | 40.0% |
| High | 76 | 46 | 60.5% |
| Medium | 61 | 27 | 44.3% |
| Low | 6 | 6 | 100.0% |

The high stability of Low-severity findings reflects that these are typically self-contained observations (verbose error handling, debug logging) that require no cross-file validation. The lower stability of Critical findings reflects their dependence on multi-file confirmation paths that are subject to context window availability.

---

## Gate Outcome Analysis

Confirmed findings are evaluated by a downstream gate. Outcomes aggregated across all 148 findings × 12 runs (1,776 total evaluations):

| Gate outcome | Count | Percentage |
|---|---|---|
| Pass | 48 | 2.7% |
| Fail | 1,160 | 65.3% |
| Needs human | 568 | 32.0% |

The low pass rate (2.7%) reflects strict gate criteria. This is not evidence of excessive false positives from the confirmation stage — rather, the gate is functioning as a precision filter that escalates most findings to human review rather than auto-resolving them. The 65.3% fail rate warrants closer inspection: these represent findings that the confirmation stage endorsed but the gate subsequently rejected. Depending on gate logic, this may indicate overly conservative gate thresholds, findings that are technically real but contextually low risk, or genuine false positives from the confirmation stage.

### Gate consistency

**84.5% of findings (125/148)** have `gate_consistency = 1.0`, meaning the gate reaches an identical verdict in every pass that detects the finding. The remaining 23 findings have `gate_consistency = 0.6667`, corresponding exactly to the 8/12 pass group — the gate's verdict variance is entirely explained by the same context composition split that drives detection rate variance.

---

## Cross-Run Consistency: Line-Number Keyed Analysis

### Methodology

To test whether the pipeline finds the same vulnerabilities consistently across runs, confirmed findings were keyed by `(scanned_file, line_number)` with a ±2-line fuzzy match window. Line clusters within ±2 lines of each other were merged into a single group using the minimum line number as the representative. This produces a set of canonical `(file, line-cluster)` groups that are then checked for presence across all 12 runs.

- **Total groups identified:** 93
- **Confirmed findings with line attribution:** 1,324 / 1,372 (96.5%)
- **Confirmed findings without line numbers:** 48 (3.5%)

### Results

| Group category | Count | Percentage |
|---|---|---|
| Consistent across all 12 runs | 75 | 80.6% |
| Inconsistent (not all runs) | 18 | 19.4% |

Of the 18 inconsistent groups, **none show random or unpredictable absence patterns**. Every inconsistent group is missing from exactly one of two pass groups (see [§ Pass Group Structural Split](#pass-group-structural-split)), and every missing finding in one group has a complementary confirmed finding in the other. Within each pass group, consistency is 100%.

### No-line findings

48 confirmed findings carry no line number attribution. These cannot be included in the line-keyed consistency analysis. They are distributed across the two pass groups in the same structured pattern as line-keyed findings:

| Finding | Pass group | Runs |
|---|---|---|
| `ChangePassword.aspx.cs` — possible sensitive data exposure | Group A | 8/12 |
| `ChangePassword.aspx.designer.cs` — missing auth check on password change | Group A | 8/12 |
| `ChangePassword.aspx.designer.cs` — potential exposure of password change UI elements | Group A | 8/12 |
| `AddNewUser.aspx.designer.cs` — missing authorization check on user creation | Group B | 4/12 |
| `AddNewUser.aspx.designer.cs` — potential SQL injection in user creation | Group B | 4/12 |
| `AddNewUser.aspx.designer.cs` — hardcoded credentials or connection strings | Group B | 4/12 |
| `ChangePassword.aspx.cs` — potential exposure of sensitive user data | Group B | 4/12 |
| `LoginPage.aspx.designer.cs` — potential missing auth check on admin login | Group B | 4/12 |
| `LoginPage.aspx.designer.cs` — missing authorization check for admin functionality | Group B | 4/12 |

The structured grouping of no-line findings further confirms that absence is context-driven, not stochastic.

---

## Pass Group Structural Split

### The p4–p7 boundary

All 18 cross-run inconsistencies resolve to a single structural difference: passes p4–p7 received a different composition of cross-reference files in their context windows compared to passes p1–p3 and p8–p12.

**Group A** (passes p1, p2, p3, p8, p9, p10, p11, p12 — 8 passes):
- Confirms 10 findings not confirmed by Group B
- For `ForgotPassword.aspx.cs`, `Global.asax.cs`, and `Web.config`: marks certain hypotheses as **inconclusive** (`file_not_in_context`)
- These 10 Group-A-only findings cluster in `AddNewUser.aspx.cs`, `AddNewUser.aspx.designer.cs`, `dbtest.aspx.cs`, `Default.aspx.cs`, `LoginPage.aspx.designer.cs`, `ProxySetup.aspx.cs`, `Web.config`

**Group B** (passes p4, p5, p6, p7 — 4 passes):
- Confirms 8 findings not confirmed by Group A
- For `ForgotPassword.aspx.cs`, `Global.asax.cs`, and `Web.config`: confirms findings that Group A marks inconclusive
- These 8 Group-B-only findings cluster in `ChangePassword.aspx.designer.cs`, `dbtest.aspx.cs`, `Default.aspx.cs`, `ProxySetup.aspx.cs`, `ProxySetup.aspx.designer.cs`, `Web.config`

### Complementarity

The two groups are exact complements: every finding absent from Group B is present in Group A, and vice versa. No finding is undetected in both groups. This means the union of findings across all 12 passes covers all real vulnerabilities that either context configuration can see. The split does not indicate false positives — it indicates that two different valid context bundles produce two slightly different but internally consistent views of the same codebase.

This is a **batching artifact**, not a model artifact. The model produces deterministic output for a given input; the variation originates upstream in how context windows are assembled.

---

## Severity and Category Breakdown

### Confirmed findings by severity (findings_listing.csv, all passes)

| Severity | Confirmed count | Percentage |
|---|---|---|
| High | 728 | 53.1% |
| Medium | 528 | 38.5% |
| Critical | 44 | 3.2% |
| Low | 72 | 5.2% |

### Confirmed findings by category (findings_listing.csv, all passes)

| Category | Count | Percentage |
|---|---|---|
| Injection | 396 | 28.9% |
| AuthZ | 352 | 25.6% |
| DataLeak | 264 | 19.2% |
| Secrets | 108 | 7.9% |
| AuthN | 88 | 6.4% |
| Crypto | 68 | 5.0% |
| Other | 60 | 4.4% |
| BusinessLogic | 20 | 1.5% |
| Deserialization | 12 | 0.9% |
| DoS | 4 | 0.3% |

Injection and authorization findings dominate, consistent with WebGoat.NET's intentional vulnerability profile. The high AuthZ count partly reflects the pipeline flagging missing authorization checks in generated `.aspx.designer.cs` files — a known false-positive pattern discussed in [§ Interpretation](#interpretation).

---

## File-Level Findings

Files with the highest unique confirmed finding counts (across `findings.csv`):

| File | Unique findings |
|---|---|
| `App_Code/DB/SqliteDbProvider.cs` | 10 |
| `Web.config` | 10 |
| `dbtest.aspx.cs` | 9 |
| `AddNewUser.aspx.cs` | 6 |
| `Global.asax.cs` | 6 |
| `LoginPage.aspx.cs` | 6 |
| `AddNewUser.aspx.designer.cs` | 5 |
| `App_Code/Util.cs` | 5 |
| `Code/DatabaseUtilities.cs` | 5 |
| `Default.aspx.cs` | 5 |

`SqliteDbProvider.cs` and `DatabaseUtilities.cs` findings are all SQL injection via string concatenation, confirmed with high confidence (0.95) across all 12 passes — the most reliable findings in the dataset. `Web.config` findings are split across the two pass groups, accounting for its disproportionate share of cross-run variation.

---

## Interpretation

### What the data supports

**The multi-stage agent pipeline is operating correctly at temperature 0.** The three primary evidence points are:

1. **Confidence determinism is absolute.** `conf_std = 0.000` universally. The model assigns the same confidence score to the same finding in every pass that detects it. This is the defining characteristic of temperature-0 inference and confirms the model component introduces no stochasticity.

2. **Inconsistency is structured, not random.** All 18 cross-run inconsistencies follow a single, identifiable pattern (p4–p7 vs. all others). There is no finding that appears inconsistently within a pass group. Inconsistency is entirely explained by pipeline inputs, not model behavior.

3. **Per-pass confirmed counts are nearly identical.** The difference between pass groups is one finding (114 vs. 115 confirmed per pass), reflecting the complementary nature of the context composition split rather than any meaningful variance in model output.

### What the data does not confirm

**Detection rate ≠ ground truth.** A detection rate of 0.67 or 0.33 does not mean the finding is a false positive. In every case examined, the non-detecting passes were marking the relevant hypothesis as *inconclusive* (context gap), not *rejected* (negative evidence). The appropriate interpretation is that the finding is real but the pipeline lacked necessary context in some passes to confirm it, not that the model changed its assessment.

**The 0.30 confidence cluster is not low-quality evidence.** Findings confirmed from `.aspx.designer.cs` files consistently receive 0.30 confidence. This reflects the confirmation stage's appropriate epistemic humility when validating structural findings from generated code files — these files define UI control scaffolding without containing business logic, so findings about authorization or injection in them require the corresponding code-behind file to fully substantiate. Confidence 0.30 means "I can see the exposure surface but cannot confirm exploitability from available context," which is a correct and useful signal.

### The designer.cs confidence floor

All confirmed findings from `.aspx.designer.cs` files carry confidence 0.30. This is a systematic pattern: these are generated files that define ASP.NET control declarations without executable logic, so the agent can identify missing authorization patterns in the control surface but cannot confirm them as exploitable without seeing the corresponding `.aspx.cs` code-behind. These findings should be triaged differently from 0.90+ findings — they are accurate signals about exposure but require co-analysis with the paired code-behind file before prioritization.

---

## Limitations

**Small n for binomial estimation.** With 12 passes, the 95% confidence intervals for 8/12 (0.39–0.86) and 4/12 (0.14–0.61) are too wide to distinguish a true 0.67 detection rate from 0.50 or 0.83 with statistical confidence. The current pass count is sufficient to identify the structural split but not to characterize the detection probability of borderline findings precisely.

**Context window non-uniformity.** The p4–p7 split is the dominant source of variance in the dataset. Until context window composition is standardized across all passes, the effective sample size for borderline findings is 4 or 8, not 12.

**Title fragmentation inflates finding count.** Several underlying vulnerabilities appear as two separate finding keys because the hypothesis stage generated slightly different titles across passes, which the confirmation stage propagated. `Web.config` verbose logging appears at both line 14 and line 24 with different titles; the hardcoded credentials finding appears as both "Hardcoded Credentials in Clear Text" (Critical, 8/12) and "Hardcoded User Credentials in Clear Text" (Critical, 4/12). After semantic deduplication, the true unique finding count is lower than 148.

**Gate failure rate requires further investigation.** The 65.3% gate failure rate is high and its driver is not fully characterized by available data. It is unclear whether this reflects gate thresholds that are too strict, a specific category of finding that the gate consistently rejects, or a calibration issue between confirmation confidence scores and gate acceptance criteria.

**No-line findings cannot be consistency-checked.** The 48 confirmed findings without line attribution (3.5% of confirmed) are excluded from the line-keyed analysis. Requiring line attribution as a confirmation gate condition would make the full finding set amenable to consistency analysis.

---

## Recommended Next Steps

The following improvements are ordered by expected impact on cross-run consistency.

### 1. Standardize context window composition across all passes *(highest priority)*

The single root cause of all 18 cross-run inconsistencies is that passes p4–p7 received a different file set than the other 8 passes. Before running any hypothesis or confirmation stage, a pre-pass dependency resolution step should identify all files referenced in cross-file hypothesis traces and assemble them into a complete context bundle. All passes for a given source file should receive an identical context bundle. This eliminates the context composition split entirely and would bring the consistency rate from 80.6% to 100% for line-keyed findings.

### 2. Add a post-confirmation deduplication and merge stage

Title fragmentation is splitting single real vulnerabilities across multiple finding keys, artificially inflating the finding count and depressing apparent detection rates. A merge pass after confirmation should apply fuzzy string similarity to finding titles (threshold ~0.85 Jaccard or cosine on token sets) combined with line proximity (±10 lines) and matching category. This would collapse pairs like the verbose logging and hardcoded credentials variants in `Web.config` into single canonical findings, converting several 0.67+0.33 pairs into clean 1.0 findings.

### 3. Enforce line attribution as a hard gate for confirmation

Confirmed findings without line numbers cannot be keyed, deduplicated, or consistency-checked. The confirmation stage should reject any finding that cannot cite a specific line range in the target file. If the evidence is strong enough to confirm a vulnerability, it is strong enough to locate it. Enforcing this as a required output field would bring the no-line rate from 3.5% to 0% and make the full finding set available to consistency analysis.

### 4. Introduce a controlled vocabulary for finding titles and severity

Free-text title generation is the proximate cause of title fragmentation. Providing the confirmation stage with a structured output schema — a fixed severity enum, a mandatory category tag from a controlled list, and a title template tied to category — would eliminate title-level variation entirely. Confidence scores are already perfectly stable (conf_std = 0 universally); titles require the same treatment. The category taxonomy already exists in the data (`Injection`, `AuthZ`, `DataLeak`, etc.) and can be used to constrain title generation.

### 5. Separate inconclusive from negative in detection rate calculation

The current detection rate denominator counts all passes, treating inconclusive outcomes the same as non-detections. A finding that is confirmed in 8 passes and inconclusive in 4 (due to context gaps) has a materially different meaning than one confirmed in 8 passes and explicitly rejected in 4. Introducing a three-way outcome (`confirmed` / `inconclusive` / `not_found`) and computing detection rate only over passes that reached a definitive outcome would produce more accurate stability estimates and correctly attribute borderline detection rates to their cause.

### 6. Increase pass count to 24 for borderline finding characterization

With 12 passes, the 95% confidence intervals for 8/12 and 4/12 detection rates span 0.47 and 0.46 width respectively — too wide to characterize borderline findings reliably. Increasing to 24 passes (after context window standardization) would narrow intervals to approximately ±0.20, sufficient to discriminate between a true 0.50 and a true 0.75 detection rate with reasonable confidence. This is particularly important for the 67 findings currently straddling the 0.5 threshold whose true stability cannot be determined from the current dataset.

### 7. Feed prior-pass confirmed findings as soft context

Once context window composition is standardized, confirmed findings from earlier passes can be injected into subsequent passes as structured priors — not to force agreement, but to give the hypothesis stage a starting set that reduces the probability of missing borderline findings. This is particularly valuable for findings that depend on cross-file context that varies by batch. A structured prior ("this file was previously found to contain a SQL injection at line 47 with confidence 0.95") reduces the cognitive load on the confirmation stage and improves recall for findings near the confirmation threshold.

### 8. Investigate gate failure rate

The 65.3% gate failure rate requires root-cause analysis before the gate can be considered well-calibrated. Recommended approach: sample 50 gate-fail findings across severity tiers and manually assess whether each represents a true positive, a true false positive, or a genuine ambiguity. This will establish whether the gate is appropriately strict, overly conservative, or miscalibrated for specific finding categories.

---

## Appendix: Inconsistent Finding Groups

All 18 (file, line-cluster) groups with detection rates below 1.0, showing which pass group detects each and the corresponding pass group that marks it inconclusive or absent.

### Group A only — present in p1–p3, p8–p12; absent in p4–p7

| File | Line cluster | Title(s) | Confidence | Lines |
|---|---|---|---|---|
| `AddNewUser.aspx.cs` | 70 | Authentication Bypass via Username Validation Bypass | 0.85 | 70–97 |
| `AddNewUser.aspx.designer.cs` | 24 | Missing Authorization Check on User Creation; Potential Input Sanitization Issues in User Fields | 0.30 | 24–29, 24–37 |
| `AddNewUser.aspx.designer.cs` | 30 | Potential Exposure of Security Question/Answer | 0.30 | 30–32 |
| `dbtest.aspx.cs` | 69 | Unrestricted Database Rebuild Access | 0.95 | 69–90 |
| `dbtest.aspx.cs` | 92 | Potential SQL Injection via Configuration File Updates; Insecure Direct Object Reference in Configuration Handling | 0.85–0.90 | 92–135 |
| `dbtest.aspx.cs` | 124 | Hardcoded Database Connection Strings in Configuration Files | 0.90 | 124–132 |
| `Default.aspx.cs` | 15 | Missing Authorization Check on Database Rebuild Functionality | 0.75 | 15 |
| `LoginPage.aspx.designer.cs` | 26 | Potential Missing Authentication Check on Admin Login Button; Missing Authorization Check for Admin Functionality | 0.30 | 26 |
| `ProxySetup.aspx.cs` | 15 | Potential XSS Vulnerability via txtName.Text Input; Potential String Manipulation Vulnerability in txtName.Text; Misuse of String Reversal Functionality | 0.90 | 15, 17, 15,21–27 |
| `Web.config` | 14 | Verbose Logging Enabled in Production | 0.90 | 14 |

### Group B only — present in p4–p7; absent in p1–p3, p8–p12

| File | Line cluster | Title(s) | Confidence | Lines |
|---|---|---|---|---|
| `ChangePassword.aspx.designer.cs` | 1 | Missing Authorization Check on Password Change; Potential Exposure of Password Change Functionality | 0.30 | 1–37 |
| `dbtest.aspx.cs` | 46 | Lack of Input Validation in Configuration Updates; Denial of Service via Malformed Configuration Inputs | 0.90 | 46–67 |
| `Default.aspx.cs` | 37 | Session Identifier Exposure in ViewState; Session Hijacking via ViewState Session ID Storage | 0.90 | 37 |
| `ProxySetup.aspx.cs` | 12 | Potential String Manipulation Vulnerability | 0.90 | 12–14 |
| `ProxySetup.aspx.designer.cs` | 22 | Hardcoded Configuration Values in UI Controls | 0.40 | 22–25 |
| `ProxySetup.aspx.designer.cs` | 26 | Potential Command Injection via TextBox Input; Missing Authorization Check on Sensitive Operation | 0.30 | 26, 28 |
| `Web.config` | 24 | Verbose Logging Enabled in Production Environment | 0.80 | 24 |
| `Web.config` | 47 | Header Injection Vulnerability Due to Disabled Header Checking | 0.90 | 47 |

> **Note on `Web.config` verbose logging:** The Group A finding at line 14 and the Group B finding at line 24 represent the same underlying vulnerability (verbose logging enabled in production) with a slightly different title and a different specific configuration line cited. They fall 10 lines apart, outside the ±2 fuzzy match window, and are counted as two separate groups. After title normalization and a wider merge window, these would collapse into a single 12/12 finding.

---

*Analysis generated from `findings_listing.csv` (4,696 rows) and `findings.csv` (148 unique findings) covering 12 passes of `qwen3-coder-30b` at temperature 0.0 against the WebGoat.NET codebase.*
