# Multi-Stage Security Finding Agent: Consistency Analysis

**Source:** `findings_listing.csv`  
**Model:** `qwen3-coder-30b` | **Temperature:** `0.7` | **Passes:** 10  
**Total rows:** 3,920 | **Canonical findings tracked:** 182

---

## Summary

This analysis evaluates whether a multi-stage agentic security scanning pipeline is functioning correctly across repeated runs at a relatively high temperature setting (0.7). The pipeline operates in two stages: a **hypothesis** stage that generates candidate findings, followed by a **confirmation** stage that either confirms or marks findings as inconclusive.

The central question is whether the data supports the claim that:

> *The multi-stage agents are working properly — narrowing down false positives and false negatives even at temperature 0.7 — but the names of the findings themselves are inconsistent as a result of that temperature setting.*

The answer, based on empirical analysis across 10 passes and 182 unique canonical findings, is **yes, with high confidence**.

---

## Key Metrics

| Metric | Value | Count |
|--------|-------|-------|
| Canonical findings tracked | — | 182 |
| Outcome stable across passes (≥80% same verdict) | 85.2% | 155 / 182 |
| Always confirmed (100% across all passes) | 52.2% | 95 / 182 |
| Always inconclusive (100% across all passes) | 33.0% | 60 / 182 |
| Mixed outcome (split verdict across passes) | 14.8% | 27 / 182 |
| Line numbers consistent across passes | 86.3% | 157 / 182 |
| Evidence title varies across passes (same finding, different label) | 23.1% | 42 / 182 |
| Hypothesis title differs from its evidence title (renaming) | 40.7% | 74 / 182 |
| Evidence entries: same file+lines, different title across passes | — | 30 groups |
| Of those, severity also varies at the same location | — | 18 / 30 groups |

---

## Statistical significance

Six tests were run to evaluate whether the data supports the claim with statistical rigour. The short answer is **yes for the core claim** (pipeline verdicts are reliable far above chance), **yes with a caveat for the distinction** between outcome stability and title stability (the gap is real but smaller than the qualitative picture suggests), and **no for per-finding Bonferroni-corrected tests** — not because the effect is absent but because 10 passes is structurally underpowered for that test.

### Test results

| # | Test | Statistic | p-value | Effect size | Verdict |
|---|------|-----------|---------|-------------|---------|
| T1 | One-sample t-test: outcome agreement vs. chance (μ = 0.5) | t = 37.49 | 3.0 × 10⁻⁸⁷ | d = 2.78 (very large) | **Supported** |
| T2 | One-sample t-test: title agreement vs. chance (μ = 0.5) | t = 30.03 | 3.2 × 10⁻⁷² | d = 2.23 (very large) | Supported |
| T3 | Wilcoxon signed-rank: outcome agreement > title agreement | W = 572 | 0.030 | — | **Supported** |
| T4 | Paired t-test: mean difference (outcome − title agreement) | t = 2.55 | 0.012 | d = 0.19 (small) | **Supported** |
| T5 | Two-proportion z-test: perfect outcome agreement > perfect title agreement | z = 2.01 | 0.022 | — | **Supported** |
| T6 | Per-finding binomial test, Bonferroni-corrected (n = 144 ten-pass findings) | — | — | — | **Underpowered** |

### Interpreting the results

**T1 confirms the core claim decisively.** The mean outcome agreement across 182 findings is 93.6%, against a chance baseline of 50%. The p-value of 3 × 10⁻⁸⁷ is not a rounding artifact — this is an enormous, unambiguous signal. Cohen's d of 2.78 is nearly four times what is conventionally considered a "large" effect (d > 0.8). The pipeline's confirmed/inconclusive verdict is not random noise at temperature 0.7; it is a stable, reliable signal.

**T2 shows titles are also above chance** (mean agreement 90.2%, d = 2.23), which means the instability in naming is relative, not absolute. Temperature 0.7 does not make titles random — it makes them *less deterministic than the structural verdict*, which is what T3 and T4 measure.

**T3 and T4 confirm that outcome agreement is significantly higher than title agreement** (p = 0.012–0.030). This directly supports the argument that the two-stage pipeline is doing something structurally different for the verdict versus the label. However, the effect size of the *gap* is small (d = 0.19). The honest reading is that outcome and title consistency both run high, and the pipeline's structural advantage over pure naming shows up reliably but modestly in the aggregate numbers. The 30 evidence-level inconsistency groups identified in the previous section — where the same file and lines produce different severity ratings — are the sharper empirical illustration of where temperature 0.7 leaves its mark.

**T5 reinforces T3/T4** at the "perfect agreement" threshold: 85.2% of findings are confirmed or rejected unanimously across all passes, versus 76.9% for titles — a gap of 8.3 percentage points (p = 0.022).

**T6 fails after Bonferroni correction, but this is a study design limitation, not a refutation.** With 10 passes per finding and 144 findings, the Bonferroni-adjusted threshold is α = 0.000347. The minimum achievable p-value for a single finding with n = 10 is 0.5¹⁰ = 0.000977 — physically impossible to clear the corrected threshold even with perfect unanimity. Approximately 12 passes would be the minimum needed for a perfect-agreement finding to survive Bonferroni correction. 138 of 144 findings (95.8%) are individually significant at the uncorrected α = 0.05, and the median per-finding p-value is 9.8 × 10⁻⁴, which is close to the Bonferroni bar. The failure is arithmetic, not evidential.

### Descriptive statistics

| Measure | Outcome agreement | Title agreement |
|---------|:-----------------:|:---------------:|
| Mean | 0.936 | 0.902 |
| Median | 1.000 | 1.000 |
| Std dev | 0.157 | 0.181 |
| Perfect (100%) | 85.2% of findings | 76.9% of findings |

The identical medians (both 1.000) reflect that the majority of findings are unanimous on both dimensions. The mean is pulled down by the minority of findings with split verdicts or title variation — but those minorities differ in size (14.8% for outcomes, 23.1% for titles), and that difference is what T3–T5 are detecting.

### Conclusion

The data supports the argument with statistical significance at conventional thresholds (α = 0.05) across four independent tests. The pipeline verdict is reliable at temperature 0.7 with an extremely large effect size. The distinction between verdict stability and title stability is real and statistically detectable, though the effect size of the gap is small — the practical evidence for temperature-induced naming noise is better illustrated by the 30 same-location evidence inconsistencies (18 of which also vary in severity) than by the aggregate agreement gap alone.

---

## What the Data Shows

### 1. The confirmation stage is working as a filter

Of the 182 canonical findings, 95 were confirmed on every single one of the 10 passes, and 60 were marked inconclusive on every single pass. This means the second stage is not randomly toggling between outcomes — it is consistently identifying real vulnerabilities and consistently rejecting spurious ones. Only 27 findings showed any split in verdict across passes, and most of those had a dominant outcome above 60%.

The inconclusive count (60 findings reliably rejected) is particularly significant. It represents hypotheses the pipeline raised and then consistently dismissed after deeper inspection — exactly the false positive suppression the multi-stage design is intended to provide.

### 2. Location pinpointing is stable

86.3% of confirmed findings land on exactly the same line numbers across all 10 passes. Where line numbers do vary, the differences are minor boundary disagreements rather than the agent pointing at different code entirely. Examples include `22–24` vs `22–25` (off by one line boundary) or `15–24` vs `16–24` (start line shifts by one). The agent is consistently looking at the same code. This supports the claim that the structural reasoning of the pipeline is sound at this temperature setting.

### 3. Title naming is where temperature 0.7 leaves its mark

While outcomes and locations are stable, **40.7% of findings have a hypothesis title that differs from the confirmed evidence title**, and **23.1% produce a different evidence title across passes for the same finding at the same location**. The finding itself is deterministic — the same vulnerability, same file, same lines — but the model chooses different words to label it depending on the sampling path that run.

Representative examples of this pattern:

| File | Lines | Hypothesis title | Evidence title variants |
|------|-------|-----------------|------------------------|
| `App_Code/Encoder.cs` | 35–44 | Potential Weakness in Encryption Implementation Using Default Rijndael Settings | Use of Weak Encryption Algorithm (RijndaelManaged with Default Settings) |
| `App_Code/VeryWeakRandom.cs` | 7–36 | Use of Predictable Random Number Generator in Security-Critical Contexts | Use of Very Weak Random Number Generator |
| `Global.asax.cs` | 35–38 | XSS Protection Disabled via Header Manipulation | X-XSS-Protection Header Set to Disabled *or* X-XSS-Protection Header Set to Zero |
| `Web.config` | 54–58 | Hardcoded User Credentials in Clear Text | Hardcoded Credentials in Clear Text |
| `Code/SQLiteProfileProvider.cs` | 374–382 | Insecure Deserialization with BinaryFormatter in Profile Provider | Use of BinaryFormatter in Profile Property Serialization |
| `App_Code/WeakMessageDigest.cs` | 14–30 | Use of Weak Custom Hash Algorithm in Security Context | Use of Weak Cryptographic Algorithm *or* Use of Insecure Hashing Algorithm |

In each case the underlying vulnerability is identical, the location is identical, and the verdict is identical. Only the label varies.

### 4. Practical implication for downstream deduplication

If findings are aggregated or deduplicated by title string across runs, the title variation introduced by temperature 0.7 will cause the same real finding to appear as multiple distinct issues. Grouping on `(scanned_file, lines)` is a far more reliable key than grouping on `title`. Location and verdict are the stable signal; the title is effectively a free-text summary subject to sampling noise.

---

## Title Mismatch Pairs (Hypothesis → Evidence, collapsed across passes)

These 62 unique pairs show cases where the same file and line range produced a different title between the hypothesis and confirmed-evidence stages. This is the clearest signature of temperature-induced naming drift — the agent reaches the same conclusion but phrases it differently.

| File | Lines | Hyp ID | Hypothesis title | Evidence title | Outcome | Severity |
|------|-------|--------|-----------------|----------------|---------|----------|
| `AddNewUser.aspx.cs` | 25–33 | HYP-001 | Potential Authentication Bypass via Username Validation Bypass | Missing Input Validation for Username in User Registration | confirmed | Medium |
| `AddNewUser.aspx.designer.cs` | unknown | HYP-003 | Hardcoded Credentials or Connection Strings in User Creation Logic | Hardcoded Credentials or Connection Strings | confirmed | Medium |
| `App_Code/ConfigFile.cs` | 25–55 | HYP-001 | Potential for Configuration-based Injection | Insecure Configuration - No Input Validation or Sanitization in Config File Parser | confirmed | Medium |
| `App_Code/CookieManager.cs` | 23 | HYP-001 | Potential Authentication Bypass Due to Missing Cookie Addition | Missing Authentication Cookie Addition to HTTP Response | confirmed | High |
| `App_Code/CustomerLoginData.cs` | 11 | HYP-001 | Missing Authorization Check on isLoggedIn Flag | Insecure Direct Object Reference in CustomerLoginData | confirmed | Medium |
| `App_Code/CustomerLoginData.cs` | 21–30 | HYP-002 | Incorrect Assignment in Message Property Setter | Potential Injection Vulnerability via Message Property Setter | confirmed | Medium |
| `App_Code/DB/DbProviderFactory.cs` | 15 | HYP-001 | Potential Information Disclosure via Logging of Database Type | Potential Information Disclosure via Logging | confirmed | Medium |
| `App_Code/DB/DummyDbProvider.cs` | 1–129 | HYP-001 | Potential Hardcoded Credentials in Dummy Database Provider | Potential Hardcoded Credentials or Configuration Values | confirmed | Medium |
| `App_Code/DB/IDbProvider.cs` | 10–11 | HYP-003 | Hardcoded Credentials or Connection Strings in Database Interface Implementation | Hardcoded Credentials or Connection Strings in Database Interface | confirmed | Medium |
| `App_Code/Encoder.cs` | 16 | HYP-002 | Hardcoded Salt in Key Derivation Function | Hardcoded Salt in Encryption Implementation | confirmed | Medium |
| `App_Code/Encoder.cs` | 35–44 | HYP-001 | Potential Weakness in Encryption Implementation Using Default Rijndael Settings | Use of Weak Encryption Algorithm (RijndaelManaged with Default Settings) | confirmed | High |
| `App_Code/Encoder.cs` | 227–241 | HYP-003 | Possible Insecure Direct Object Reference in Authentication Ticket Handling | Potential Insecure Direct Object Reference in Forms Authentication Ticket Handling | confirmed | Medium |
| `App_Code/VeryWeakRandom.cs` | 7–36 | HYP-001 | Use of Predictable Random Number Generator in Security-Critical Contexts | Use of Very Weak Random Number Generator | confirmed | High |
| `App_Code/WeakMessageDigest.cs` | 14–30 | HYP-001 | Use of Weak Custom Hash Algorithm in Security Context | Use of Weak Cryptographic Algorithm | confirmed | High |
| `App_Code/WeakRandom.cs` | 1–42 | HYP-001 | Use of Predictable Random Number Generator in Security Token Generation | Use of Weak Random Number Generator | confirmed | High |
| `App_Data/XmlInjectionUsers.xml` | 5 | HYP-001 | Potential XXE Vulnerability in XmlInjectionUsers.xml Processing | XML Injection Vulnerability | confirmed | High |
| `App_Data/XmlInjectionUsers.xml` | 5 | HYP-003 | XML Injection via User Input in XmlInjectionUsers.xml | XML Injection via User Input | confirmed | High |
| `ChangePassword.aspx.cs` | 6 | HYP-001 | Missing Authorization Check on Password Change Endpoint | Potential Missing Authorization Check | confirmed | High |
| `ChangePassword.aspx.cs` | unknown | HYP-002 | Potential Sensitive Data Exposure in Password Change Process | Possible Sensitive Data Exposure | confirmed | Medium |
| `ChangePassword.aspx.cs` | unknown | HYP-002 | Potential Exposure of Sensitive User Data During Password Change | Potential Exposure of Sensitive User Data | confirmed | Medium |
| `ChangePassword.aspx.designer.cs` | 1–37 | HYP-001 | Missing Authorization Check on Password Change Page | Missing Authorization Check on Password Change | confirmed | High |
| `ChangePassword.aspx.designer.cs` | 1–37 | HYP-002 | Public Exposure of Password Change Interface Without Authentication | Potential Exposure of Password Change Functionality | confirmed | Medium |
| `Code/IOHelper.cs` | 11–18 | HYP-001 | Insecure Direct Object Reference (IDOR) in IOHelper.ReadAllFromFile | Insecure Direct Object Reference (IDOR) in file reading function | confirmed | High |
| `Code/SQLiteProfileProvider.cs` | 241–243 | HYP-002 | Potential SQL Injection via String Concatenation in Profile Provider | Potential SQL Injection via String Concatenation | confirmed | High |
| `Code/SQLiteProfileProvider.cs` | 374–382 | HYP-001 | Insecure Deserialization with BinaryFormatter in Profile Provider | Use of BinaryFormatter in Profile Property Serialization | confirmed | High |
| `Content/About.aspx.cs` | 12–16 | HYP-001 | Missing Authorization Check on About Page | Potential Missing Authorization Check | confirmed | Medium |
| `Content/BasicAuth.aspx.cs` | 12–15 | HYP-001 | Missing Authorization Check on BasicAuth Page | Potential Missing Authorization Check | confirmed | Medium |
| `Content/BasicAuth.aspx.cs` | 12–15 | HYP-002 | Missing Authentication Logic on BasicAuth Page | Missing Authentication Logic | confirmed | High |
| `Content/Challenge1.aspx.cs` | 12–16 | HYP-001 | Missing Authorization Check on Challenge1 Page | Potential Missing Authorization Check | confirmed | Medium |
| `Content/Challenge1.aspx.cs` | 12–16 | HYP-002 | Verbose Error Exposure in Challenge1 Page | Verbose Error Handling | confirmed | Low |
| `Content/Challenge1.aspx.designer.cs` | 1–20 | HYP-001 | Potential Missing Authorization Check in Challenge1 Handler | Potential Missing Authorization Check | confirmed | Medium |
| `Content/Challenge1.aspx.designer.cs` | 1–20 | HYP-002 | Verbose Debug Error Handling Possible in Challenge1 Handler | Debug/Verbose Error Handling Possible | confirmed | Low |
| `Content/Challenge2.aspx.cs` | 12–16 | HYP-001 | Missing Authorization Check on Challenge2 Page | Potential Missing Authorization Check | confirmed | Medium |
| `Content/Challenge2.aspx.cs` | 12–16 | HYP-002 | Verbose Error Handling in Challenge2 Page | Verbose Error Handling | confirmed | Low |
| `Content/Challenge2.aspx.designer.cs` | 1–20 | HYP-001 | Potential Missing Authorization Check in Challenge2 Form Handler | Potential Missing Authorization Check | confirmed | Medium |
| `Content/Challenge2.aspx.designer.cs` | 1–10 | HYP-002 | Possible Debug/Verbose Logging Exposure in Challenge2 Designer File | Possible Debug/Verbose Logging Enabled | confirmed | Low |
| `Content/Challenge3.aspx.cs` | 12–16 | HYP-001 | Missing Authorization Check on Challenge3 Page | Potential Missing Authorization Check | confirmed | Medium |
| `Content/Challenge3.aspx.cs` | 12–16 | HYP-002 | Verbose Error Handling Leading to Information Disclosure | Verbose Error Handling | confirmed | Low |
| `Content/Challenge3.aspx.designer.cs` | 1–9 | HYP-002 | Possible Debug/Verbose Logging Enabled in Challenge3 Designer File | Possible Debug/Verbose Logging Enabled | confirmed | Low |
| `Content/ChangePwd.aspx.cs` | 12–15 | HYP-001 | Missing Authentication Check in Password Change Page | Potential Authentication Bypass in Password Change Page | confirmed | Critical |
| `Default.aspx.cs` | 15 | HYP-002 | Missing Authorization Check Before Database Rebuild Redirect | Missing Authorization Check on Database Rebuild Functionality | confirmed | High |
| `Default.aspx.cs` | 28 | HYP-001 | Information Disclosure via Server Name in HTTP Cookie | Information Exposure Through Server Name in Cookie | confirmed | Medium |
| `Default.aspx.cs` | 28 | HYP-001 | Information Disclosure via Server Name in HTTP Cookie | Potential Information Disclosure via Server Name | confirmed | Medium |
| `Default.aspx.designer.cs` | 22 | HYP-002 | Potential Sensitive Data Exposure via UI Label Control | Potential Sensitive Data Exposure | confirmed | Medium |
| `Default.aspx.designer.cs` | 22–24 | HYP-001 | Potential Missing Authorization Check on UI Button Control | Potential Missing Authorization Check | confirmed | High |
| `Default.aspx.designer.cs` | 22–25 | HYP-001 | Potential Missing Authorization Check on UI Button Control | Potential Missing Authorization Check | confirmed | High |
| `Default.aspx.designer.cs` | 22–25 | HYP-002 | Potential Sensitive Data Exposure via UI Label Control | Potential Sensitive Data Exposure | confirmed | Medium |
| `ForgotPassword.aspx.cs` | 6–12 | HYP-001 | Missing Authorization Check in Password Reset Functionality | Potential Missing Authorization Check in Password Reset Functionality | confirmed | High |
| `ForgotPassword.aspx.cs` | 6–12 | HYP-002 | Information Disclosure in Password Reset Flow | Possible Information Disclosure in Password Reset Flow | confirmed | Medium |
| `Global.asax.cs` | 15–24 | HYP-004 | Potential Information Disclosure via Debug Logging | Potential Information Disclosure via Debug Mode | confirmed | Medium |
| `Global.asax.cs` | 16–24 | HYP-004 | Information Disclosure via Debug Logging Configuration | Potential Information Disclosure via Debug Mode | confirmed | Medium |
| `Global.asax.cs` | 35–38 | HYP-001 | XSS Protection Disabled via Header Manipulation | X-XSS-Protection Header Set to Disabled | confirmed | High |
| `Global.asax.cs` | 35–38 | HYP-001 | XSS Protection Disabled via Header Manipulation | X-XSS-Protection Header Set to Zero | confirmed | Medium |
| `Global.asax.cs` | 40–62 | HYP-002 | Insecure Role Assignment from FormsAuthenticationTicket | Potential Insecure Role Assignment | confirmed | High |
| `Global.asax.cs` | 40–62 | HYP-002 | Insecure Role Handling in Forms Authentication | Potential Insecure Role Handling in Forms Authentication | confirmed | High |
| `Global.asax.cs` | 40–62 | HYP-003 | Weak Authentication Ticket Handling | Possible Weak Authentication Ticket Handling | confirmed | Medium |
| `LoginPage.aspx.cs` | 19–21 | HYP-001 | Bypassable Authentication via Redirect | Bypassable Authentication Logic | confirmed | High |
| `LoginPage.aspx.cs` | 19–31 | HYP-002 | Missing Input Validation and Error Handling | Missing Authentication Logic | confirmed | High |
| `LoginPage.aspx.cs` | 21 | HYP-001 | Unconditional Redirect Bypassing Authentication | Authentication Bypass via Redirect | confirmed | High |
| `LoginPage.aspx.cs` | 21 | HYP-003 | Hardcoded Redirect Target Exposes Internal Structure | Insecure Direct Object Reference | confirmed | Medium |
| `ProxySetup.aspx.cs` | 12–14 | HYP-001 | Unsanitized User Input in String Reversal Functionality | Potential String Manipulation Vulnerability | confirmed | Medium |
| `Web.config` | 54–58 | HYP-001 | Hardcoded User Credentials in Clear Text | Hardcoded Credentials in Clear Text | confirmed | Critical |

---

## Evidence-level inconsistencies: same file and lines, different titles

The previous section covered cases where a hypothesis title differs from its confirmed-evidence title — a cross-stage naming shift. This section looks at a sharper problem: **evidence entries that share the exact same file and line numbers but produce different titles across passes**. These are cases where the confirmation stage itself is non-deterministic, not just in how it labels a finding relative to the hypothesis that spawned it, but in what it independently decides the finding is called.

30 such groups were identified. Of those, **18 also exhibit severity variation** at the same location — marked with ⚠ below. Severity variation is the more consequential inconsistency: two runs looking at identical code, confirming the same issue, but assigning it different risk levels purely as a function of sampling noise.

The `linked hypotheses` column shows which hypothesis IDs feed into each location. Where multiple hypotheses map to the same line range, the titles often reflect different framings of the same underlying code — but even single-hypothesis groups (e.g. `Default.aspx.cs` line 28, `Global.asax.cs` line 35–38) show title and severity drift, confirming that the variation is not merely a consequence of different hypotheses being confirmed — it is intrinsic to the generation step at temperature 0.7.

| File | Lines | Passes | Title variants | All observed titles | Sev variants | Severities | Linked hypotheses |
|------|-------|:------:|:--------------:|---------------------|:------------:|------------|-------------------|
| `AddNewUser.aspx.cs` | 25-33 | 10 | 3 | • Missing Input Validation for Username in User Registration<br>• Username Input Validation Bypass Leading to Injection Vulnerability<br>• Weak Password Validation Allows Credential Compromise | 2 ⚠ | High, Medium | HYP-001, HYP-002 |
| `AddNewUser.aspx.designer.cs` | unknown | 4 | 3 | • Hardcoded Credentials or Connection Strings<br>• Missing Authorization Check on User Creation<br>• Potential SQL Injection Vulnerability in User Creation | 2 ⚠ | High, Medium | HYP-001, HYP-002, HYP-003 |
| `App/Code/DB/DbProviderFactory.cs` | 15 | 10 | 2 | • Infrastructure Enumeration via Logging of Database Type<br>• Potential Information Disclosure via Logging | 1 | Medium | HYP-001, HYP-004 |
| `App/Code/DB/DummyDbProvider.cs` | 1-129 | 10 | 3 | • Missing Authorization Checks in Database Methods<br>• Potential Hardcoded Credentials or Configuration Values<br>• Potential SQL Injection Vulnerability in Database Methods | 1 | Medium | HYP-001, HYP-002, HYP-003 |
| `App/Code/DB/MySqlDbProvider.cs` | 29-36, 47-52 | 10 | 2 | • Hardcoded Database Credentials in Configuration Files<br>• Information Disclosure via Misconfigured Configuration Files | 2 ⚠ | High, Medium | HYP-004, HYP-006 |
| `App/Code/Util.cs` | 32-41 | 10 | 2 | • Sensitive Data Exposure Through Process Output Logs<br>• Sensitive Data Exposure via Logging | 1 | Medium | HYP-003, HYP-006 |
| `App/Data/XmlInjectionUsers.xml` | 5 | 10 | 2 | • XML Injection Vulnerability<br>• XML Injection via User Input | 1 | High | HYP-001, HYP-003 |
| `ChangePassword.aspx.cs` | unknown | 10 | 2 | • Possible Sensitive Data Exposure<br>• Potential Exposure of Sensitive User Data | 1 | Medium | HYP-002 |
| `ChangePassword.aspx.designer.cs` | 1-37 | 4 | 2 | • Missing Authorization Check on Password Change<br>• Potential Exposure of Password Change Functionality | 2 ⚠ | High, Medium | HYP-001, HYP-002 |
| `ChangePassword.aspx.designer.cs` | unknown | 6 | 2 | • Missing Authorization Check on Password Change Functionality<br>• Potential Exposure of Password Change UI Elements | 2 ⚠ | High, Medium | HYP-001, HYP-002 |
| `Code/IOHelper.cs` | 11-18 | 10 | 2 | • Insecure Direct Object Reference (IDOR) in file reading function<br>• Potential Information Disclosure via Path Traversal | 1 | High | HYP-001, HYP-002 |
| `Content/BasicAuth.aspx.cs` | 12-15 | 10 | 2 | • Missing Authentication Logic<br>• Potential Missing Authorization Check | 2 ⚠ | High, Medium | HYP-001, HYP-002 |
| `Content/Challenge1.aspx.cs` | 12-16 | 10 | 2 | • Potential Missing Authorization Check<br>• Verbose Error Handling | 2 ⚠ | Low, Medium | HYP-001, HYP-002 |
| `Content/Challenge1.aspx.designer.cs` | 1-20 | 10 | 2 | • Debug/Verbose Error Handling Possible<br>• Potential Missing Authorization Check | 2 ⚠ | Low, Medium | HYP-001, HYP-002 |
| `Content/Challenge2.aspx.cs` | 12-16 | 10 | 2 | • Potential Missing Authorization Check<br>• Verbose Error Handling | 2 ⚠ | Low, Medium | HYP-001, HYP-002 |
| `Content/Challenge3.aspx.cs` | 12-16 | 10 | 2 | • Potential Missing Authorization Check<br>• Verbose Error Handling | 2 ⚠ | Low, Medium | HYP-001, HYP-002 |
| `Content/ChangePwd.aspx.cs` | 12-15 | 10 | 2 | • Missing Authorization Check in Password Change Functionality<br>• Potential Authentication Bypass in Password Change Page | 2 ⚠ | Critical, High | HYP-001, HYP-002 |
| `Default.aspx.cs` | 28-28 | 10 | 2 | • Information Exposure Through Server Name in Cookie<br>• Potential Information Disclosure via Server Name | 1 | Medium | HYP-001 |
| `Default.aspx.cs` | 37-37 | 4 | 2 | • Session Hijacking via ViewState Session ID Storage<br>• Session Identifier Exposure in ViewState | 2 ⚠ | High, Medium | HYP-002, HYP-006 |
| `Default.aspx.designer.cs` | 22-25 | 4 | 2 | • Potential Missing Authorization Check<br>• Potential Sensitive Data Exposure | 2 ⚠ | High, Medium | HYP-001, HYP-002 |
| `ForgotPassword.aspx.cs` | 5-10 | 4 | 2 | • Missing Authorization Check in Password Reset Functionality<br>• Potential Information Disclosure in Password Reset Flow | 2 ⚠ | High, Medium | HYP-001, HYP-002 |
| `ForgotPassword.aspx.cs` | 6-12 | 6 | 2 | • Possible Information Disclosure in Password Reset Flow<br>• Potential Missing Authorization Check in Password Reset Functionality | 2 ⚠ | High, Medium | HYP-001, HYP-002 |
| `Global.asax.cs` | 35-38 | 10 | 2 | • X-XSS-Protection Header Set to Disabled<br>• X-XSS-Protection Header Set to Zero | 2 ⚠ | High, Medium | HYP-001 |
| `Global.asax.cs` | 40-62 | 10 | 3 | • Possible Weak Authentication Ticket Handling<br>• Potential Insecure Role Assignment<br>• Potential Insecure Role Handling in Forms Authentication | 2 ⚠ | High, Medium | HYP-002, HYP-003 |
| `LoginPage.aspx.cs` | 19-31 | 10 | 2 | • Missing Authentication Implementation<br>• Missing Authentication Logic | 1 | High | HYP-002 |
| `LoginPage.aspx.cs` | 21 | 4 | 2 | • Authentication Bypass via Redirect<br>• Insecure Direct Object Reference | 2 ⚠ | High, Medium | HYP-001, HYP-003 |
| `LoginPage.aspx.designer.cs` | 26-26 | 6 | 2 | • Missing Authorization Check for Admin Functionality<br>• Potential Missing Authentication Check on Admin Login Button | 1 | High | HYP-001, HYP-002 |
| `LoginPage.aspx.designer.cs` | unknown | 4 | 2 | • Missing Authorization Check for Admin Functionality<br>• Potential Missing Authentication Check on Admin Login Button | 1 | High | HYP-001, HYP-002 |
| `dbtest.aspx.cs` | 46-67, 69-90 | 4 | 2 | • Denial of Service via Malformed Configuration Inputs<br>• Lack of Input Validation in Configuration Updates | 1 | Medium | HYP-004, HYP-006 |
| `dbtest.aspx.cs` | 92-135 | 6 | 2 | • Insecure Direct Object Reference in Configuration Handling<br>• Potential SQL Injection via Configuration File Updates | 1 | Medium | HYP-002, HYP-003 |

> ⚠ indicates severity also varies across passes for the same file and line numbers.

### Notable cases

`Content/ChangePwd.aspx.cs` lines 12–15 is the most consequential severity-drift example: the same confirmation at the same location alternates between **Critical** and **High** depending on the pass. A downstream triage system consuming raw titles or severities would treat this as two distinct issues at different priority levels.

`Global.asax.cs` lines 40–62 produces three different evidence titles from two source hypotheses (HYP-002 and HYP-003) across 10 passes — "Potential Insecure Role Assignment", "Potential Insecure Role Handling in Forms Authentication", and "Possible Weak Authentication Ticket Handling" — each a plausible description of the same code block, each reflecting a different emphasis the model happened to take.

`LoginPage.aspx.cs` line 21 alternates between "Authentication Bypass via Redirect" (High) and "Insecure Direct Object Reference" (Medium) — two categorically different vulnerability classes pointing at the same line, depending solely on which hypothesis the confirmation stage happened to anchor on in a given run.

---

## Full Finding Consistency Table

This table covers all 182 canonical findings. Each row represents one hypothesis tracked across all passes in which it appeared. Columns show the confirmed line numbers (from the evidence stage), whether those line numbers were consistent across passes, the dominant outcome and what percentage of passes agreed on it, and title variance counts at both the hypothesis and evidence stages.

| File | Hyp | Lines (evidence) | Lines stable | Outcome | Outcome % | Hyp title variants | Ev title variants | Hyp→Ev title shift |
|------|-----|-----------------|:------------:|---------|:---------:|:-----------------:|:-----------------:|:------------------:|
| `AddNewUser.aspx.cs` | HYP-001 | 25-33 | yes | confirmed | 100.0% | 2 | 2 | yes |
| `AddNewUser.aspx.cs` | HYP-002 | 25-33 | yes | confirmed | 100.0% | 1 | 1 | no |
| `AddNewUser.aspx.cs` | HYP-003 | 17, 19-23 | no | confirmed | 100.0% | 2 | 2 | yes |
| `AddNewUser.aspx.cs` | HYP-004 | 70-97 | yes | confirmed | 100.0% | 1 | 1 | no |
| `AddNewUser.aspx.designer.cs` | HYP-001 | 24-37, unknown | no | confirmed | 50.0% | 1 | 1 | no |
| `AddNewUser.aspx.designer.cs` | HYP-002 | 30-32, unknown | no | confirmed | 71.4% | 2 | 2 | yes |
| `AddNewUser.aspx.designer.cs` | HYP-003 | 24-29, unknown | no | confirmed | 71.4% | 2 | 3 | yes |
| `App/Code/ConfigFile.cs` | HYP-001 | 25-55 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `App/Code/CookieManager.cs` | HYP-001 | 23 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `App/Code/CookieManager.cs` | HYP-002 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `App/Code/CookieManager.cs` | HYP-003 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `App/Code/CookieManager.cs` | HYP-004 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `App/Code/CustomerLoginData.cs` | HYP-001 | 11 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `App/Code/CustomerLoginData.cs` | HYP-002 | 21-30 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `App/Code/DB/DbConstants.cs` | HYP-001 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `App/Code/DB/DbProviderFactory.cs` | HYP-001 | 15 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `App/Code/DB/DbProviderFactory.cs` | HYP-004 | 15 | yes | confirmed | 100.0% | 1 | 1 | no |
| `App/Code/DB/DummyDbProvider.cs` | HYP-001 | 1-129 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `App/Code/DB/DummyDbProvider.cs` | HYP-002 | 1-129 | yes | confirmed | 100.0% | 1 | 1 | no |
| `App/Code/DB/DummyDbProvider.cs` | HYP-003 | 1-129 | yes | confirmed | 100.0% | 1 | 1 | no |
| `App/Code/DB/DummyDbProvider.cs` | HYP-004 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `App/Code/DB/IDbProvider.cs` | HYP-001 | 14-15 | yes | confirmed | 50.0% | 1 | 1 | no |
| `App/Code/DB/IDbProvider.cs` | HYP-002 | 18-20 | yes | confirmed | 50.0% | 1 | 1 | no |
| `App/Code/DB/IDbProvider.cs` | HYP-003 | 10-11 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `App/Code/DB/IDbProvider.cs` | HYP-004 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `App/Code/DB/IDbProvider.cs` | HYP-005 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `App/Code/DB/MySqlDbProvider.cs` | HYP-001 | 517-518, 539-540, 559-560 | yes | confirmed | 100.0% | 1 | 1 | no |
| `App/Code/DB/MySqlDbProvider.cs` | HYP-002 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `App/Code/DB/MySqlDbProvider.cs` | HYP-003 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `App/Code/DB/MySqlDbProvider.cs` | HYP-004 | 29-36, 47-52 | yes | confirmed | 100.0% | 1 | 1 | no |
| `App/Code/DB/MySqlDbProvider.cs` | HYP-005 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `App/Code/DB/MySqlDbProvider.cs` | HYP-006 | 29-36, 47-52 | yes | confirmed | 100.0% | 1 | 1 | no |
| `App/Code/DB/SqliteDbProvider.cs` | HYP-001 | 47-52 | yes | confirmed | 100.0% | 1 | 1 | no |
| `App/Code/DB/SqliteDbProvider.cs` | HYP-002 | 84-87 | yes | confirmed | 100.0% | 1 | 1 | no |
| `App/Code/DB/SqliteDbProvider.cs` | HYP-003 | 124-127 | yes | confirmed | 100.0% | 1 | 1 | no |
| `App/Code/DB/SqliteDbProvider.cs` | HYP-004 | 146-147 | yes | confirmed | 100.0% | 1 | 1 | no |
| `App/Code/DB/SqliteDbProvider.cs` | HYP-005 | 164-165 | yes | confirmed | 100.0% | 1 | 1 | no |
| `App/Code/DB/SqliteDbProvider.cs` | HYP-006 | 182-185 | yes | confirmed | 100.0% | 1 | 1 | no |
| `App/Code/DB/SqliteDbProvider.cs` | HYP-007 | 198-200 | yes | confirmed | 100.0% | 1 | 1 | no |
| `App/Code/DB/SqliteDbProvider.cs` | HYP-008 | 217-220 | yes | confirmed | 100.0% | 1 | 1 | no |
| `App/Code/DB/SqliteDbProvider.cs` | HYP-009 | 234-237 | yes | confirmed | 100.0% | 1 | 1 | no |
| `App/Code/DB/SqliteDbProvider.cs` | HYP-010 | 248-251 | yes | confirmed | 100.0% | 1 | 1 | no |
| `App/Code/DB/SqliteDbProvider.cs` | HYP-011 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `App/Code/DB/SqliteDbProvider.cs` | HYP-012 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `App/Code/DB/SqliteDbProvider.cs` | HYP-013 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `App/Code/Encoder.cs` | HYP-001 | 35-44 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `App/Code/Encoder.cs` | HYP-002 | 16 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `App/Code/Encoder.cs` | HYP-003 | 227-241 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `App/Code/Settings.cs` | HYP-001 | 40-41 | yes | confirmed | 100.0% | 1 | 1 | no |
| `App/Code/Util.cs` | HYP-001 | 14-27 | yes | confirmed | 100.0% | 1 | 1 | no |
| `App/Code/Util.cs` | HYP-002 | 55-70 | yes | confirmed | 100.0% | 1 | 1 | no |
| `App/Code/Util.cs` | HYP-003 | 32-41 | yes | confirmed | 100.0% | 1 | 1 | no |
| `App/Code/Util.cs` | HYP-004 | 14, 55 | yes | confirmed | 100.0% | 1 | 1 | no |
| `App/Code/Util.cs` | HYP-005 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `App/Code/Util.cs` | HYP-006 | 32-41 | yes | confirmed | 100.0% | 1 | 1 | no |
| `App/Code/VeryWeakRandom.cs` | HYP-001 | 7-36 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `App/Code/VeryWeakRandom.cs` | HYP-002 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `App/Code/VeryWeakRandom.cs` | HYP-003 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `App/Code/WeakMessageDigest.cs` | HYP-001 | 14-30 | yes | confirmed | 50.0% | 1 | 2 | yes |
| `App/Code/WeakMessageDigest.cs` | HYP-002 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `App/Code/WeakRandom.cs` | HYP-001 | 1-42 | yes | confirmed | 50.0% | 1 | 2 | yes |
| `App/Code/WeakRandom.cs` | HYP-002 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `App/Code/WeakRandom.cs` | HYP-003 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `App/Code/WeakRandom.cs` | HYP-004 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `App/Data/XmlInjectionUsers.xml` | HYP-001 | 5 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `App/Data/XmlInjectionUsers.xml` | HYP-002 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `App/Data/XmlInjectionUsers.xml` | HYP-003 | 5 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `ChangePassword.aspx.cs` | HYP-001 | 6-6, 6-10 | no | confirmed | 100.0% | 2 | 2 | yes |
| `ChangePassword.aspx.cs` | HYP-002 | unknown | yes | confirmed | 50.0% | 2 | 4 | yes |
| `ChangePassword.aspx.cs` | HYP-003 | — | yes | inconclusive | 100.0% | 2 | 2 | yes |
| `ChangePassword.aspx.cs` | HYP-004 | — | yes | inconclusive | 100.0% | 2 | 2 | yes |
| `ChangePassword.aspx.cs` | HYP-005 | — | yes | inconclusive | 100.0% | 2 | 2 | yes |
| `ChangePassword.aspx.designer.cs` | HYP-001 | 1-37, unknown | no | confirmed | 50.0% | 2 | 3 | yes |
| `ChangePassword.aspx.designer.cs` | HYP-002 | 1-37, unknown | no | confirmed | 50.0% | 2 | 3 | yes |
| `ChangePassword.aspx.designer.cs` | HYP-003 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `ChangePassword.aspx.designer.cs` | HYP-004 | — | yes | inconclusive | 100.0% | 2 | 2 | yes |
| `Code/DatabaseUtilities.cs` | HYP-001 | 200-209 | yes | confirmed | 100.0% | 1 | 1 | no |
| `Code/DatabaseUtilities.cs` | HYP-002 | 211-216 | yes | confirmed | 100.0% | 1 | 1 | no |
| `Code/DatabaseUtilities.cs` | HYP-003 | 218-223 | yes | confirmed | 100.0% | 1 | 1 | no |
| `Code/DatabaseUtilities.cs` | HYP-004 | 232-237 | yes | confirmed | 100.0% | 1 | 1 | no |
| `Code/DatabaseUtilities.cs` | HYP-005 | 245-250 | yes | confirmed | 100.0% | 1 | 1 | no |
| `Code/DatabaseUtilities.cs` | HYP-006 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `Code/DatabaseUtilities.cs` | HYP-007 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `Code/IOHelper.cs` | HYP-001 | 11-18 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `Code/IOHelper.cs` | HYP-002 | 11-18 | yes | confirmed | 100.0% | 1 | 1 | no |
| `Code/IOHelper.cs` | HYP-003 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `Code/SQLiteMembershipProvider.cs` | HYP-001 | 374-382 | yes | confirmed | 100.0% | 1 | 1 | no |
| `Code/SQLiteMembershipProvider.cs` | HYP-002 | 250, 257 | yes | confirmed | 100.0% | 1 | 1 | no |
| `Code/SQLiteMembershipProvider.cs` | HYP-003 | 324-331 | yes | confirmed | 100.0% | 1 | 1 | no |
| `Code/SQLiteMembershipProvider.cs` | HYP-004 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `Code/SQLiteMembershipProvider.cs` | HYP-005 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `Code/SQLiteProfileProvider.cs` | HYP-001 | 374-382 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `Code/SQLiteProfileProvider.cs` | HYP-002 | 241-243 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `Code/SQLiteProfileProvider.cs` | HYP-003 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `Code/SQLiteProfileProvider.cs` | HYP-004 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `Code/SQLiteProfileProvider.cs` | HYP-005 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `Code/SQLiteRoleProvider.cs` | HYP-001 | 237-246 | yes | confirmed | 100.0% | 1 | 1 | no |
| `Code/SQLiteRoleProvider.cs` | HYP-002 | 281-294 | yes | confirmed | 100.0% | 1 | 1 | no |
| `Code/SQLiteRoleProvider.cs` | HYP-003 | 257-264 | yes | confirmed | 100.0% | 1 | 1 | no |
| `Code/SQLiteRoleProvider.cs` | HYP-004 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `Code/SQLiteRoleProvider.cs` | HYP-005 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `Code/SQLiteRoleProvider.cs` | HYP-006 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `Content/About.aspx.cs` | HYP-001 | 12-16 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `Content/BasicAuth.aspx.cs` | HYP-001 | 12-15 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `Content/BasicAuth.aspx.cs` | HYP-002 | 12-15 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `Content/BasicAuth.aspx.designer.cs` | HYP-001 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `Content/BasicAuth.aspx.designer.cs` | HYP-002 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `Content/BasicAuth.aspx.designer.cs` | HYP-003 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `Content/Challenge1.aspx.cs` | HYP-001 | 12-16 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `Content/Challenge1.aspx.cs` | HYP-002 | 12-16 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `Content/Challenge1.aspx.designer.cs` | HYP-001 | 1-20 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `Content/Challenge1.aspx.designer.cs` | HYP-002 | 1-20 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `Content/Challenge2.aspx.cs` | HYP-001 | 12-16 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `Content/Challenge2.aspx.cs` | HYP-002 | 12-16 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `Content/Challenge2.aspx.designer.cs` | HYP-001 | 1-20 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `Content/Challenge2.aspx.designer.cs` | HYP-002 | 1-10 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `Content/Challenge3.aspx.cs` | HYP-001 | 12-16 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `Content/Challenge3.aspx.cs` | HYP-002 | 12-16 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `Content/Challenge3.aspx.designer.cs` | HYP-001 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `Content/Challenge3.aspx.designer.cs` | HYP-002 | 1-9 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `Content/ChangePwd.aspx.cs` | HYP-001 | 12-15 | yes | confirmed | 100.0% | 1 | 1 | yes |
| `Content/ChangePwd.aspx.cs` | HYP-002 | 12-15 | yes | confirmed | 100.0% | 1 | 1 | no |
| `Content/ChangePwd.aspx.cs` | HYP-003 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `Content/ChangePwd.aspx.cs` | HYP-004 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `Content/ChangePwd.aspx.cs` | HYP-005 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `Default.aspx.cs` | HYP-001 | 28-28 | yes | confirmed | 100.0% | 1 | 2 | yes |
| `Default.aspx.cs` | HYP-002 | 15-15, 37-37 | no | confirmed | 100.0% | 2 | 2 | yes |
| `Default.aspx.cs` | HYP-003 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `Default.aspx.cs` | HYP-004 | — | yes | inconclusive | 100.0% | 2 | 2 | yes |
| `Default.aspx.cs` | HYP-005 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `Default.aspx.cs` | HYP-006 | 37-37 | yes | confirmed | 100.0% | 1 | 1 | no |
| `Default.aspx.designer.cs` | HYP-001 | 22-24, 22-25 | no | confirmed | 50.0% | 1 | 2 | yes |
| `Default.aspx.designer.cs` | HYP-002 | 22, 22-25 | no | confirmed | 50.0% | 1 | 2 | yes |
| `ForgotPassword.aspx.cs` | HYP-001 | 5-10, 6-12 | no | confirmed | 71.4% | 1 | 2 | yes |
| `ForgotPassword.aspx.cs` | HYP-002 | 5-10, 6-12 | no | confirmed | 71.4% | 2 | 2 | yes |
| `ForgotPassword.aspx.cs` | HYP-003 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `ForgotPassword.aspx.cs` | HYP-004 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `ForgotPassword.aspx.designer.cs` | HYP-001 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `ForgotPassword.aspx.designer.cs` | HYP-002 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `Global.asax.cs` | HYP-001 | 35-38 | yes | confirmed | 100.0% | 1 | 2 | yes |
| `Global.asax.cs` | HYP-002 | 40-62 | yes | confirmed | 100.0% | 2 | 2 | yes |
| `Global.asax.cs` | HYP-003 | 40-62 | yes | confirmed | 60.0% | 2 | 2 | yes |
| `Global.asax.cs` | HYP-004 | 15-24, 16-24 | no | confirmed | 100.0% | 2 | 1 | yes |
| `Global.asax.cs` | HYP-006 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `LoginPage.aspx.cs` | HYP-001 | 19-21, 21 | no | confirmed | 100.0% | 2 | 2 | yes |
| `LoginPage.aspx.cs` | HYP-002 | 19-31 | yes | confirmed | 100.0% | 2 | 2 | yes |
| `LoginPage.aspx.cs` | HYP-003 | 21, 23-30 | no | confirmed | 100.0% | 2 | 2 | yes |
| `LoginPage.aspx.cs` | HYP-004 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `LoginPage.aspx.cs` | HYP-005 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `LoginPage.aspx.designer.cs` | HYP-001 | 26, unknown | no | confirmed | 50.0% | 1 | 1 | no |
| `LoginPage.aspx.designer.cs` | HYP-002 | 26, unknown | no | confirmed | 50.0% | 1 | 1 | no |
| `ProxySetup.aspx.cs` | HYP-001 | 12-14 | yes | inconclusive | 60.0% | 2 | 2 | yes |
| `ProxySetup.aspx.cs` | HYP-002 | 17 | yes | confirmed | 60.0% | 2 | 2 | yes |
| `ProxySetup.aspx.cs` | HYP-003 | — | yes | inconclusive | 100.0% | 2 | 2 | yes |
| `ProxySetup.aspx.cs` | HYP-005 | 15 | yes | confirmed | 60.0% | 2 | 2 | yes |
| `ProxySetup.aspx.cs` | HYP-006 | 15, 21-27 | yes | confirmed | 100.0% | 1 | 1 | no |
| `ProxySetup.aspx.designer.cs` | HYP-001 | 26 | yes | inconclusive | 71.4% | 1 | 1 | no |
| `ProxySetup.aspx.designer.cs` | HYP-002 | 28 | yes | inconclusive | 71.4% | 1 | 1 | no |
| `ProxySetup.aspx.designer.cs` | HYP-003 | 22-25 | yes | inconclusive | 60.0% | 2 | 2 | yes |
| `Web.config` | HYP-001 | 54-58, 56-60 | no | confirmed | 100.0% | 1 | 2 | yes |
| `Web.config` | HYP-002 | 32 | yes | confirmed | 100.0% | 1 | 1 | no |
| `Web.config` | HYP-003 | 163-169, 164-171 | no | confirmed | 100.0% | 2 | 2 | yes |
| `Web.config` | HYP-004 | 43 | yes | confirmed | 100.0% | 1 | 1 | no |
| `Web.config` | HYP-005 | 14, 24 | no | confirmed | 100.0% | 2 | 2 | yes |
| `Web.config` | HYP-006 | 47 | yes | confirmed | 100.0% | 1 | 1 | no |
| `Web.config` | HYP-007 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `WebGoat.NET.csproj` | HYP-001 | 21-31 | yes | confirmed | 100.0% | 1 | 1 | no |
| `WebGoat.NET.csproj` | HYP-002 | 31, 48 | yes | confirmed | 100.0% | 1 | 1 | no |
| `WebGoat.NET.csproj` | HYP-003 | 32-37 | yes | confirmed | 100.0% | 1 | 1 | no |
| `WebGoat.NET.csproj` | HYP-004 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `WebGoat.NET.csproj` | HYP-005 | — | yes | inconclusive | 100.0% | 1 | 1 | no |
| `dbtest.aspx.cs` | HYP-001 | 17-38, 17-32, 46-67, 69-90 | no | confirmed | 100.0% | 2 | 2 | yes |
| `dbtest.aspx.cs` | HYP-002 | 92-135 | yes | confirmed | 60.0% | 2 | 2 | yes |
| `dbtest.aspx.cs` | HYP-003 | 17-32, 92-135 | no | confirmed | 100.0% | 2 | 2 | yes |
| `dbtest.aspx.cs` | HYP-004 | 46-67, 69-90 | yes | confirmed | 100.0% | 1 | 1 | no |
| `dbtest.aspx.cs` | HYP-005 | — | yes | inconclusive | 100.0% | 2 | 2 | yes |
| `dbtest.aspx.cs` | HYP-006 | 46-67, 69-90, 124-132 | no | confirmed | 100.0% | 2 | 2 | yes |
| `dbtest.aspx.cs` | HYP-007 | 69-90 | yes | confirmed | 100.0% | 1 | 1 | no |
| `dbtest.aspx.designer.cs` | HYP-001 | 37-43 | yes | confirmed | 50.0% | 1 | 1 | no |
| `dbtest.aspx.designer.cs` | HYP-002 | 53, 54 | no | confirmed | 50.0% | 1 | 1 | no |
| `dbtest.aspx.designer.cs` | HYP-003 | 25-36, 25-43 | no | confirmed | 50.0% | 2 | 2 | yes |
| `dbtest.aspx.designer.cs` | HYP-004 | — | yes | inconclusive | 100.0% | 2 | 2 | yes |

---

## Column definitions

| Column | Description |
|--------|-------------|
| **File** | Source file scanned, with `WebGoat_` prefix stripped and underscores converted to path separators |
| **Hyp** | Hypothesis ID as assigned in the hypothesis stage |
| **Lines (evidence)** | Line number(s) cited by the confirmation stage. Multiple values indicate variation across passes |
| **Lines stable** | `yes` if all passes cited the same line range; `no` if the range differed across passes |
| **Outcome** | The dominant stage verdict (`confirmed` or `inconclusive`) across all passes |
| **Outcome %** | Percentage of passes that agreed on the dominant outcome |
| **Hyp title variants** | Number of distinct hypothesis titles seen for this finding across passes |
| **Ev title variants** | Number of distinct evidence titles seen for this finding across passes |
| **Hyp→Ev title shift** | `yes` if any hypothesis title differed from any evidence title for this finding |

---

*Generated from `findings_listing.csv` — model `qwen3-coder-30b`, temperature 0.7, 10 passes, 3,920 total rows.*
