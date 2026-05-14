# Scan stability analysis — temp=0.0

**Runs analysed:** 12  |  **Files:** 50  |  **Stability threshold:** 80%

> **Identity matching:** Findings are matched across runs via the hypothesis chain (`hypotheses.json -> HYP-### title -> evidence hypothesis_id`). Titles that differ by paraphrase are clustered using fuzzy matching (SequenceMatcher ratio >= 0.72) so the same vulnerability detected with different wording counts as a single finding.\n
## Summary
| File | Runs | Gate: PASS | FAIL | NEEDS_HUMAN | Gate consistency | Stable findings | Sensitive findings |
|---|---|---|---|---|---|---|---|
| `WebGoat_AddNewUser.aspx.cs` | 12 | 0 | 8 | 4 | 67% | 0 | 6 |
| `WebGoat_AddNewUser.aspx.designer.cs` | 12 | 0 | 4 | 8 | 67% | 1 | 4 |
| `WebGoat_App_Code_ConfigFile.cs` | 12 | 0 | 0 | 12 | 100% | 1 | 0 |
| `WebGoat_App_Code_CookieManager.cs` | 12 | 0 | 0 | 12 | 100% | 1 | 0 |
| `WebGoat_App_Code_CustomerLoginData.cs` | 12 | 12 | 0 | 0 | 100% | 2 | 0 |
| `WebGoat_App_Code_DB_DbConstants.cs` | 12 | 0 | 0 | 12 | 100% | 0 | 0 |
| `WebGoat_App_Code_DB_DbProviderFactory.cs` | 12 | 12 | 0 | 0 | 100% | 2 | 0 |
| `WebGoat_App_Code_DB_DummyDbProvider.cs` | 12 | 0 | 0 | 12 | 100% | 3 | 0 |
| `WebGoat_App_Code_DB_IDbProvider.cs` | 12 | 0 | 0 | 12 | 100% | 3 | 0 |
| `WebGoat_App_Code_DB_MySqlDbProvider.cs` | 12 | 0 | 12 | 0 | 100% | 3 | 0 |
| `WebGoat_App_Code_DB_SqliteDbProvider.cs` | 12 | 0 | 12 | 0 | 100% | 3 | 0 |
| `WebGoat_App_Code_Encoder.cs` | 12 | 0 | 12 | 0 | 100% | 3 | 0 |
| `WebGoat_App_Code_Settings.cs` | 12 | 0 | 0 | 12 | 100% | 1 | 0 |
| `WebGoat_App_Code_Util.cs` | 12 | 0 | 12 | 0 | 100% | 5 | 0 |
| `WebGoat_App_Code_VeryWeakRandom.cs` | 12 | 0 | 0 | 12 | 100% | 1 | 0 |
| `WebGoat_App_Code_WeakMessageDigest.cs` | 12 | 0 | 0 | 12 | 100% | 1 | 0 |
| `WebGoat_App_Code_WeakRandom.cs` | 12 | 0 | 12 | 0 | 100% | 1 | 0 |
| `WebGoat_App_Data_XmlInjectionUsers.xml` | 12 | 0 | 12 | 0 | 100% | 2 | 0 |
| `WebGoat_ChangePassword.aspx.cs` | 12 | 0 | 0 | 12 | 100% | 2 | 0 |
| `WebGoat_ChangePassword.aspx.designer.cs` | 12 | 0 | 0 | 12 | 100% | 1 | 2 |
| `WebGoat_Code_DatabaseUtilities.cs` | 12 | 0 | 12 | 0 | 100% | 3 | 0 |
| `WebGoat_Code_IOHelper.cs` | 12 | 0 | 0 | 12 | 100% | 2 | 0 |
| `WebGoat_Code_SQLiteMembershipProvider.cs` | 12 | 0 | 12 | 0 | 100% | 3 | 0 |
| `WebGoat_Code_SQLiteProfileProvider.cs` | 12 | 0 | 12 | 0 | 100% | 2 | 0 |
| `WebGoat_Code_SQLiteRoleProvider.cs` | 12 | 0 | 12 | 0 | 100% | 3 | 0 |
| `WebGoat_Configuration_Default.config` | 12 | 0 | 0 | 12 | 100% | 0 | 0 |
| `WebGoat_Content_About.aspx.cs` | 12 | 0 | 0 | 12 | 100% | 1 | 0 |
| `WebGoat_Content_About.aspx.designer.cs` | 12 | 0 | 0 | 12 | 100% | 0 | 0 |
| `WebGoat_Content_BasicAuth.aspx.cs` | 12 | 0 | 12 | 0 | 100% | 2 | 0 |
| `WebGoat_Content_BasicAuth.aspx.designer.cs` | 12 | 0 | 0 | 12 | 100% | 0 | 0 |
| `WebGoat_Content_Challenge1.aspx.cs` | 12 | 0 | 12 | 0 | 100% | 2 | 0 |
| `WebGoat_Content_Challenge1.aspx.designer.cs` | 12 | 0 | 0 | 12 | 100% | 2 | 0 |
| `WebGoat_Content_Challenge2.aspx.cs` | 12 | 0 | 12 | 0 | 100% | 2 | 0 |
| `WebGoat_Content_Challenge2.aspx.designer.cs` | 12 | 0 | 0 | 12 | 100% | 2 | 0 |
| `WebGoat_Content_Challenge3.aspx.cs` | 12 | 0 | 0 | 12 | 100% | 2 | 0 |
| `WebGoat_Content_Challenge3.aspx.designer.cs` | 12 | 0 | 0 | 12 | 100% | 1 | 0 |
| `WebGoat_Content_ChangePwd.aspx.cs` | 12 | 0 | 12 | 0 | 100% | 2 | 0 |
| `WebGoat_Default.aspx.cs` | 12 | 0 | 12 | 0 | 100% | 1 | 3 |
| `WebGoat_Default.aspx.designer.cs` | 12 | 0 | 0 | 12 | 100% | 2 | 0 |
| `WebGoat_ForgotPassword.aspx.cs` | 12 | 0 | 8 | 4 | 67% | 2 | 0 |
| `WebGoat_ForgotPassword.aspx.designer.cs` | 12 | 0 | 0 | 12 | 100% | 0 | 0 |
| `WebGoat_Global.asax.cs` | 12 | 0 | 12 | 0 | 100% | 2 | 3 |
| `WebGoat_LoginPage.aspx.cs` | 12 | 0 | 12 | 0 | 100% | 0 | 6 |
| `WebGoat_LoginPage.aspx.designer.cs` | 12 | 0 | 0 | 12 | 100% | 2 | 0 |
| `WebGoat_ProxySetup.aspx.cs` | 12 | 0 | 0 | 12 | 100% | 1 | 1 |
| `WebGoat_ProxySetup.aspx.designer.cs` | 12 | 0 | 4 | 8 | 67% | 0 | 3 |
| `WebGoat_Web.config` | 12 | 0 | 12 | 0 | 100% | 3 | 5 |
| `WebGoat_WebGoat.NET.csproj` | 12 | 0 | 12 | 0 | 100% | 3 | 0 |
| `WebGoat_dbtest.aspx.cs` | 12 | 0 | 12 | 0 | 100% | 2 | 5 |
| `WebGoat_dbtest.aspx.designer.cs` | 12 | 0 | 8 | 4 | 67% | 1 | 4 |

---

## File: `WebGoat_AddNewUser.aspx.cs`

**Runs with this file:** 12  |  **Gate consistency:** 67%  |  **Verdict distribution:** FAIL: 8  NEEDS_HUMAN: 4

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Missing Input Validation for Username in User Registration | Medium | 33% (4/12) | 0.90 | model inconsistency |
| Weak Password Validation Allows Credential Compromise | Medium | 33% (4/12) | 0.85 | model inconsistency |
| Unrestricted Account Creation Enables Unauthorized Access | Medium | 33% (4/12) | 0.90 | model inconsistency |
| Username Input Validation Bypass Leading to Injection Vulnerability | High | 67% (8/12) | 0.90 | model inconsistency |
| Hardcoded Security Question Exposure | Medium | 67% (8/12) | 0.90 | model inconsistency |
| Authentication Bypass via Username Validation Bypass | High | 67% (8/12) | 0.85 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 9.3 | 9.4 | 5.2 | 29.8 | 0 | 0 |
| threat | 20.7 | 23.3 | 9.4 | 72.4 | 0 | 0 |
| hypotheses | 24.2 | 31.7 | 9.4 | 92.1 | 0 | 0 |
| evidence | 28.0 | 36.8 | 10.5 | 107.0 | 0 | 0 |
| fix | 34.3 | 42.7 | 12.0 | 125.4 | 0 | 0 |
| gate | 19.4 | 28.8 | 6.9 | 81.1 | 0 | 0 |
| pre_scan | 7.1 | 7.5 | 3.6 | 23.8 | 0 | 0 |

**Mean total elapsed per run:** 143s  |  Min: 57s  |  Max: 531s


---

## File: `WebGoat_AddNewUser.aspx.designer.cs`

**Runs with this file:** 12  |  **Gate consistency:** 67%  |  **Verdict distribution:** FAIL: 4  NEEDS_HUMAN: 8

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Missing Authorization Check on User Creation | High | 100% (12/12) | [0.76, 1.00] | 0.30 | — | HYP-001 |

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Potential SQL Injection Vulnerability in User Creation | High | 33% (4/12) | 0.30 | borderline confidence |
| Hardcoded Credentials or Connection Strings | Medium | 33% (4/12) | 0.30 | borderline confidence |
| Potential Exposure of Security Question/Answer | Medium | 67% (8/12) | 0.30 | borderline confidence |
| Potential Input Sanitization Issues in User Fields | Medium | 67% (8/12) | 0.30 | borderline confidence |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.4 | 5.0 | 3.2 | 16.1 | 0 | 0 |
| threat | 16.6 | 17.4 | 7.9 | 54.0 | 0 | 0 |
| hypotheses | 17.2 | 20.5 | 8.2 | 61.1 | 0 | 0 |
| evidence | 19.2 | 21.7 | 9.6 | 65.7 | 0 | 0 |
| fix | 24.7 | 27.0 | 12.3 | 82.7 | 0 | 0 |
| gate | 18.2 | 23.2 | 6.9 | 67.8 | 0 | 0 |
| pre_scan | 7.9 | 11.0 | 3.1 | 31.6 | 0 | 0 |

**Mean total elapsed per run:** 109s  |  Min: 55s  |  Max: 379s


---

## File: `WebGoat_App_Code_ConfigFile.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Insecure Configuration - No Input Validation or Sanitization in Config File Parser | Medium | 100% (12/12) | [0.76, 1.00] | 0.75 | — | HYP-001 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.6 | 5.7 | 3.1 | 17.8 | 0 | 0 |
| threat | 10.1 | 9.9 | 5.8 | 31.4 | 0 | 0 |
| hypotheses | 9.9 | 11.4 | 4.9 | 34.5 | 0 | 0 |
| evidence | 16.5 | 19.3 | 8.2 | 58.0 | 0 | 0 |
| fix | 19.8 | 20.0 | 11.2 | 62.8 | 0 | 0 |
| gate | 13.6 | 18.4 | 5.7 | 53.2 | 0 | 0 |
| pre_scan | 6.5 | 6.5 | 3.7 | 20.4 | 0 | 0 |

**Mean total elapsed per run:** 82s  |  Min: 43s  |  Max: 278s


---

## File: `WebGoat_App_Code_CookieManager.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Missing Authentication Cookie Addition to HTTP Response | High | 100% (12/12) | [0.76, 1.00] | 0.95 | 0.000 | HYP-001 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 7.2 | 6.5 | 4.4 | 21.3 | 0 | 0 |
| threat | 13.5 | 13.5 | 7.6 | 42.5 | 0 | 0 |
| hypotheses | 18.1 | 21.3 | 8.9 | 63.8 | 0 | 0 |
| evidence | 18.0 | 20.4 | 9.2 | 61.9 | 0 | 0 |
| fix | 13.1 | 13.4 | 7.3 | 42.0 | 0 | 0 |
| gate | 15.9 | 20.4 | 7.1 | 59.6 | 0 | 0 |
| pre_scan | 6.6 | 8.5 | 2.9 | 24.8 | 0 | 0 |

**Mean total elapsed per run:** 92s  |  Min: 47s  |  Max: 316s


---

## File: `WebGoat_App_Code_CustomerLoginData.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** PASS: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Insecure Direct Object Reference in CustomerLoginData | Medium | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-001 |
| Potential Injection Vulnerability via Message Property Setter | Medium | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-002 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.1 | 4.6 | 3.1 | 15.1 | 0 | 0 |
| threat | 14.5 | 14.8 | 8.1 | 46.3 | 0 | 0 |
| hypotheses | 14.7 | 17.7 | 7.1 | 52.7 | 0 | 0 |
| evidence | 14.8 | 16.4 | 7.6 | 50.0 | 0 | 0 |
| fix | 15.5 | 15.3 | 8.8 | 48.4 | 0 | 0 |
| gate | 10.5 | 14.4 | 4.3 | 41.3 | 0 | 0 |
| pre_scan | 10.7 | 14.2 | 4.5 | 41.2 | 0 | 0 |

**Mean total elapsed per run:** 86s  |  Min: 44s  |  Max: 295s


---

## File: `WebGoat_App_Code_DB_DbConstants.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 12

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.8 | 5.4 | 3.4 | 17.3 | 0 | 0 |
| threat | 7.7 | 7.5 | 4.5 | 23.9 | 0 | 0 |
| hypotheses | 6.6 | 7.6 | 3.3 | 22.8 | 0 | 0 |
| evidence | 7.1 | 7.7 | 3.8 | 23.6 | 0 | 0 |
| fix | 2.7 | 2.8 | 1.5 | 8.6 | 0 | 0 |
| gate | 8.6 | 9.3 | 4.6 | 28.5 | 0 | 0 |
| pre_scan | 4.1 | 5.6 | 1.7 | 16.2 | 0 | 0 |

**Mean total elapsed per run:** 43s  |  Min: 23s  |  Max: 141s


---

## File: `WebGoat_App_Code_DB_DbProviderFactory.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** PASS: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Potential Information Disclosure via Logging | Medium | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-001 |
| Infrastructure Enumeration via Logging of Database Type | Medium | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-004 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.7 | 5.2 | 3.4 | 16.8 | 0 | 0 |
| threat | 13.5 | 13.0 | 7.8 | 41.5 | 0 | 0 |
| hypotheses | 17.7 | 20.9 | 8.7 | 62.6 | 0 | 0 |
| evidence | 20.6 | 26.1 | 9.3 | 76.7 | 0 | 0 |
| fix | 18.4 | 18.5 | 9.7 | 58.2 | 0 | 0 |
| gate | 17.8 | 17.6 | 9.1 | 55.6 | 0 | 0 |
| pre_scan | 4.6 | 5.6 | 2.2 | 16.7 | 0 | 0 |

**Mean total elapsed per run:** 98s  |  Min: 50s  |  Max: 328s


---

## File: `WebGoat_App_Code_DB_DummyDbProvider.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Potential Hardcoded Credentials or Configuration Values | Medium | 100% (12/12) | [0.76, 1.00] | 0.30 | — | HYP-001 |
| Missing Authorization Checks in Database Methods | Medium | 100% (12/12) | [0.76, 1.00] | 0.30 | — | HYP-002 |
| Potential SQL Injection Vulnerability in Database Methods | Medium | 100% (12/12) | [0.76, 1.00] | 0.30 | — | HYP-003 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 6.0 | 6.0 | 3.4 | 19.0 | 0 | 0 |
| threat | 19.0 | 18.9 | 10.7 | 59.7 | 0 | 0 |
| hypotheses | 17.9 | 22.0 | 8.5 | 65.1 | 0 | 0 |
| evidence | 24.7 | 29.9 | 11.8 | 89.0 | 0 | 0 |
| fix | 24.2 | 26.1 | 12.9 | 80.4 | 0 | 0 |
| gate | 15.2 | 21.5 | 6.0 | 61.3 | 0 | 0 |
| pre_scan | 8.7 | 11.7 | 3.6 | 33.8 | 0 | 0 |

**Mean total elapsed per run:** 116s  |  Min: 57s  |  Max: 408s


---

## File: `WebGoat_App_Code_DB_IDbProvider.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Potential Authentication Bypass via Missing Authorization Checks | High | 100% (12/12) | [0.76, 1.00] | 0.30 | — | HYP-001 |
| Potential SQL Injection Vulnerability in Database Methods | High | 100% (12/12) | [0.76, 1.00] | 0.30 | — | HYP-002 |
| Hardcoded Credentials or Connection Strings in Database Interface | Medium | 100% (12/12) | [0.76, 1.00] | 0.30 | — | HYP-003 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.2 | 4.8 | 3.1 | 15.5 | 0 | 0 |
| threat | 17.1 | 16.9 | 9.8 | 53.5 | 0 | 0 |
| hypotheses | 23.7 | 28.3 | 11.5 | 84.5 | 0 | 0 |
| evidence | 26.8 | 31.6 | 13.1 | 94.6 | 0 | 0 |
| fix | 22.0 | 24.2 | 11.5 | 74.0 | 0 | 0 |
| gate | 37.1 | 50.0 | 15.5 | 144.3 | 0 | 0 |
| pre_scan | 8.6 | 12.1 | 3.4 | 34.6 | 0 | 0 |

**Mean total elapsed per run:** 140s  |  Min: 68s  |  Max: 501s


---

## File: `WebGoat_App_Code_DB_MySqlDbProvider.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| SQL Injection via String Concatenation in MySqlDbProvider | Critical | 100% (12/12) | [0.76, 1.00] | 0.95 | 0.000 | HYP-001 |
| Hardcoded Database Credentials in Configuration Files | High | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-004 |
| Information Disclosure via Misconfigured Configuration Files | Medium | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-006 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 14.3 | 18.7 | 6.2 | 54.5 | 0 | 0 |
| threat | 21.3 | 21.9 | 11.8 | 68.3 | 0 | 0 |
| hypotheses | 28.7 | 35.7 | 13.3 | 105.5 | 0 | 0 |
| evidence | 51.3 | 66.6 | 22.6 | 194.2 | 0 | 0 |
| fix | 33.2 | 41.3 | 15.5 | 122.1 | 0 | 0 |
| gate | 31.5 | 46.1 | 11.7 | 130.3 | 0 | 0 |
| pre_scan | 6.8 | 9.3 | 2.8 | 26.8 | 0 | 0 |

**Mean total elapsed per run:** 187s  |  Min: 84s  |  Max: 702s


---

## File: `WebGoat_App_Code_DB_SqliteDbProvider.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| SQL Injection in CustomerLogin Query | High | 100% (12/12) | [0.76, 1.00] | 0.95 | 0.000 | HYP-001 |
| SQL Injection in GetCustomerEmail Method | High | 100% (12/12) | [0.76, 1.00] | 0.95 | 0.000 | HYP-002, HYP-003, HYP-004, HYP-005, HYP-006, HYP-008, HYP-009, HYP-010 |
| SQL Injection in GetProductsAndCategories Method | High | 100% (12/12) | [0.76, 1.00] | 0.95 | 0.000 | HYP-007 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 12.9 | 17.0 | 5.6 | 49.4 | 0 | 0 |
| threat | 62.5 | 81.7 | 27.4 | 237.9 | 0 | 0 |
| hypotheses | 76.4 | 115.6 | 26.8 | 324.3 | 0 | 0 |
| evidence | 102.9 | 154.8 | 36.5 | 434.9 | 0 | 0 |
| fix | 90.8 | 126.7 | 36.2 | 362.7 | 0 | 0 |
| gate | 72.9 | 123.1 | 20.1 | 336.7 | 0 | 0 |
| pre_scan | 57.5 | 85.5 | 20.7 | 241.0 | 0 | 0 |

**Mean total elapsed per run:** 476s  |  Min: 174s  |  Max: 1987s


---

## File: `WebGoat_App_Code_Encoder.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Use of Weak Encryption Algorithm (RijndaelManaged with Default Settings) | High | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-001 |
| Hardcoded Salt in Encryption Implementation | Medium | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-002 |
| Potential Insecure Direct Object Reference in Forms Authentication Ticket Handling | Medium | 100% (12/12) | [0.76, 1.00] | 0.80 | 0.000 | HYP-003 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 10.0 | 12.2 | 4.8 | 36.2 | 0 | 0 |
| threat | 18.7 | 20.2 | 9.9 | 62.2 | 0 | 0 |
| hypotheses | 22.3 | 27.9 | 10.2 | 82.3 | 0 | 0 |
| evidence | 34.9 | 45.9 | 15.1 | 133.4 | 0 | 0 |
| fix | 33.5 | 38.1 | 17.0 | 115.4 | 0 | 0 |
| gate | 22.3 | 33.1 | 8.1 | 93.3 | 0 | 0 |
| pre_scan | 19.5 | 27.5 | 7.7 | 78.5 | 0 | 0 |

**Mean total elapsed per run:** 161s  |  Min: 73s  |  Max: 601s


---

## File: `WebGoat_App_Code_Settings.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Environment Variable Exposure in Logs | Medium | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-001 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 6.6 | 6.6 | 3.8 | 20.7 | 0 | 0 |
| threat | 17.3 | 17.2 | 9.8 | 54.3 | 0 | 0 |
| hypotheses | 16.8 | 20.2 | 8.0 | 60.3 | 0 | 0 |
| evidence | 18.7 | 22.2 | 9.2 | 66.5 | 0 | 0 |
| fix | 10.9 | 11.2 | 6.1 | 35.0 | 0 | 0 |
| gate | 10.9 | 14.2 | 4.8 | 41.3 | 0 | 0 |
| pre_scan | 6.0 | 6.0 | 3.3 | 18.9 | 0 | 0 |

**Mean total elapsed per run:** 87s  |  Min: 45s  |  Max: 297s


---

## File: `WebGoat_App_Code_Util.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| OS Command Injection via ProcessStartInfo | High | 100% (12/12) | [0.76, 1.00] | 0.95 | 0.000 | HYP-001 |
| Command Line Injection via File Input | High | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-002 |
| Sensitive Data Exposure via Logging | Medium | 100% (12/12) | [0.76, 1.00] | 0.85 | — | HYP-003 |
| Chained Command Injection Attack | High | 100% (12/12) | [0.76, 1.00] | 0.80 | 0.000 | HYP-004 |
| Sensitive Data Exposure Through Process Output Logs | Medium | 100% (12/12) | [0.76, 1.00] | 0.85 | — | HYP-006 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 6.9 | 6.7 | 3.9 | 21.4 | 0 | 0 |
| threat | 18.6 | 19.4 | 10.2 | 60.4 | 0 | 0 |
| hypotheses | 23.9 | 29.5 | 11.2 | 87.1 | 0 | 0 |
| evidence | 40.5 | 50.6 | 18.7 | 149.3 | 0 | 0 |
| fix | 59.7 | 74.3 | 27.6 | 219.4 | 0 | 0 |
| gate | 32.0 | 49.7 | 10.6 | 138.6 | 0 | 0 |
| pre_scan | 10.8 | 13.7 | 4.9 | 40.2 | 0 | 0 |

**Mean total elapsed per run:** 192s  |  Min: 87s  |  Max: 716s


---

## File: `WebGoat_App_Code_VeryWeakRandom.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Use of Very Weak Random Number Generator | High | 100% (12/12) | [0.76, 1.00] | 0.95 | 0.000 | HYP-001 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.4 | 4.8 | 3.3 | 15.8 | 0 | 0 |
| threat | 17.8 | 17.6 | 10.2 | 55.8 | 0 | 0 |
| hypotheses | 15.3 | 18.6 | 7.3 | 55.2 | 0 | 0 |
| evidence | 18.3 | 19.9 | 9.6 | 61.0 | 0 | 0 |
| fix | 16.4 | 17.2 | 9.0 | 53.4 | 0 | 0 |
| gate | 18.0 | 23.5 | 7.9 | 68.5 | 0 | 0 |
| pre_scan | 9.8 | 15.1 | 3.3 | 42.3 | 0 | 0 |

**Mean total elapsed per run:** 101s  |  Min: 51s  |  Max: 352s


---

## File: `WebGoat_App_Code_WeakMessageDigest.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Use of Weak Cryptographic Algorithm | High | 100% (12/12) | [0.76, 1.00] | 0.95 | 0.000 | HYP-001 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.8 | 5.5 | 3.3 | 17.5 | 0 | 0 |
| threat | 13.3 | 13.0 | 7.6 | 41.3 | 0 | 0 |
| hypotheses | 11.5 | 13.6 | 5.6 | 40.6 | 0 | 0 |
| evidence | 15.7 | 17.4 | 8.1 | 53.1 | 0 | 0 |
| fix | 12.7 | 12.7 | 7.2 | 40.0 | 0 | 0 |
| gate | 11.7 | 15.2 | 5.2 | 44.3 | 0 | 0 |
| pre_scan | 8.0 | 10.8 | 3.3 | 31.2 | 0 | 0 |

**Mean total elapsed per run:** 79s  |  Min: 40s  |  Max: 268s


---

## File: `WebGoat_App_Code_WeakRandom.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Use of Weak Random Number Generator | High | 100% (12/12) | [0.76, 1.00] | 0.95 | 0.000 | HYP-001 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.3 | 4.9 | 3.2 | 15.9 | 0 | 0 |
| threat | 15.0 | 14.7 | 8.7 | 46.7 | 0 | 0 |
| hypotheses | 17.4 | 20.5 | 8.6 | 61.6 | 0 | 0 |
| evidence | 19.0 | 21.2 | 9.8 | 64.6 | 0 | 0 |
| fix | 10.9 | 11.4 | 5.9 | 35.2 | 0 | 0 |
| gate | 15.8 | 19.9 | 7.2 | 58.5 | 0 | 0 |
| pre_scan | 6.7 | 9.0 | 2.8 | 26.0 | 0 | 0 |

**Mean total elapsed per run:** 90s  |  Min: 46s  |  Max: 308s


---

## File: `WebGoat_App_Data_XmlInjectionUsers.xml`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| XML Injection Vulnerability | High | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-001 |
| XML Injection via User Input | High | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-003 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 4.9 | 4.3 | 3.0 | 14.2 | 0 | 0 |
| threat | 14.3 | 14.0 | 8.2 | 44.4 | 0 | 0 |
| hypotheses | 14.1 | 16.5 | 6.9 | 49.6 | 0 | 0 |
| evidence | 14.9 | 15.8 | 8.0 | 48.9 | 0 | 0 |
| fix | 13.3 | 13.3 | 7.5 | 41.9 | 0 | 0 |
| gate | 16.0 | 20.3 | 7.2 | 59.5 | 0 | 0 |
| pre_scan | 5.7 | 4.7 | 3.3 | 15.6 | 0 | 0 |

**Mean total elapsed per run:** 83s  |  Min: 44s  |  Max: 274s


---

## File: `WebGoat_ChangePassword.aspx.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Potential Missing Authorization Check | High | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-001 |
| Possible Sensitive Data Exposure | Medium | 100% (12/12) | [0.76, 1.00] | 0.30 | — | HYP-002 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 7.2 | 6.2 | 4.5 | 20.4 | 0 | 0 |
| threat | 16.9 | 16.6 | 9.4 | 52.6 | 0 | 0 |
| hypotheses | 21.9 | 26.8 | 9.6 | 79.5 | 0 | 0 |
| evidence | 21.8 | 24.2 | 11.2 | 73.8 | 0 | 0 |
| fix | 10.0 | 10.6 | 5.1 | 32.8 | 0 | 0 |
| gate | 17.8 | 23.2 | 7.0 | 67.6 | 0 | 0 |
| pre_scan | 5.7 | 7.8 | 2.3 | 22.4 | 0 | 0 |

**Mean total elapsed per run:** 101s  |  Min: 51s  |  Max: 349s


---

## File: `WebGoat_ChangePassword.aspx.designer.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Missing Authorization Check on Password Change Functionality | High | 100% (12/12) | [0.76, 1.00] | 0.30 | — | HYP-001 |

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Potential Exposure of Password Change Functionality | Medium | 33% (4/12) | 0.30 | borderline confidence |
| Potential Exposure of Password Change UI Elements | Medium | 67% (8/12) | 0.30 | borderline confidence |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.1 | 4.7 | 3.0 | 15.3 | 0 | 0 |
| threat | 13.6 | 12.3 | 7.6 | 40.0 | 0 | 0 |
| hypotheses | 19.8 | 22.9 | 9.6 | 69.0 | 0 | 0 |
| evidence | 21.7 | 24.6 | 10.9 | 74.5 | 0 | 0 |
| fix | 19.7 | 21.2 | 10.2 | 65.3 | 0 | 0 |
| gate | 19.7 | 25.4 | 8.2 | 74.1 | 0 | 0 |
| pre_scan | 5.6 | 7.5 | 2.3 | 21.6 | 0 | 0 |

**Mean total elapsed per run:** 105s  |  Min: 53s  |  Max: 360s


---

## File: `WebGoat_Code_DatabaseUtilities.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| SQL Injection in GetEmailByUserID Method | High | 100% (12/12) | [0.76, 1.00] | 0.95 | 0.000 | HYP-001, HYP-003, HYP-005 |
| SQL Injection in GetMailingListInfoByEmailAddress Method | High | 100% (12/12) | [0.76, 1.00] | 0.95 | 0.000 | HYP-002 |
| SQL Injection in AddNewPosting Method | High | 100% (12/12) | [0.76, 1.00] | 0.95 | 0.000 | HYP-004 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 9.8 | 12.3 | 4.5 | 36.2 | 0 | 0 |
| threat | 28.6 | 33.0 | 14.4 | 99.6 | 0 | 0 |
| hypotheses | 34.7 | 46.7 | 14.6 | 134.9 | 0 | 0 |
| evidence | 59.5 | 84.2 | 23.3 | 240.1 | 0 | 0 |
| fix | 62.0 | 79.2 | 27.9 | 232.0 | 0 | 0 |
| gate | 47.0 | 74.4 | 14.9 | 206.5 | 0 | 0 |
| pre_scan | 26.8 | 35.4 | 11.5 | 102.8 | 0 | 0 |

**Mean total elapsed per run:** 268s  |  Min: 111s  |  Max: 1052s


---

## File: `WebGoat_Code_IOHelper.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Insecure Direct Object Reference (IDOR) in file reading function | High | 100% (12/12) | [0.76, 1.00] | 0.95 | 0.000 | HYP-001 |
| Potential Information Disclosure via Path Traversal | High | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-002 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.2 | 4.6 | 3.2 | 15.0 | 0 | 0 |
| threat | 15.2 | 14.9 | 8.7 | 47.1 | 0 | 0 |
| hypotheses | 14.0 | 16.7 | 6.8 | 49.9 | 0 | 0 |
| evidence | 17.3 | 18.5 | 9.2 | 57.0 | 0 | 0 |
| fix | 22.7 | 23.7 | 12.4 | 73.6 | 0 | 0 |
| gate | 17.5 | 23.6 | 7.3 | 68.2 | 0 | 0 |
| pre_scan | 5.2 | 4.6 | 3.2 | 15.2 | 0 | 0 |

**Mean total elapsed per run:** 97s  |  Min: 51s  |  Max: 326s


---

## File: `WebGoat_Code_SQLiteMembershipProvider.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Use of Weak Hashing Algorithm for Password Storage | High | 100% (12/12) | [0.76, 1.00] | 0.95 | 0.000 | HYP-001 |
| SQL Injection Vulnerability in Application ID Retrieval | High | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-002 |
| Missing Authorization Check on User Data Access | Medium | 100% (12/12) | [0.76, 1.00] | 0.85 | — | HYP-003 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 14.9 | 20.6 | 6.0 | 59.0 | 0 | 0 |
| threat | 18.7 | 20.2 | 9.9 | 62.0 | 0 | 0 |
| hypotheses | 21.2 | 26.7 | 9.6 | 78.6 | 0 | 0 |
| evidence | 35.1 | 46.5 | 15.1 | 134.9 | 0 | 0 |
| fix | 26.4 | 29.6 | 13.6 | 90.1 | 0 | 0 |
| gate | 24.8 | 35.6 | 9.5 | 101.0 | 0 | 0 |
| pre_scan | 22.8 | 33.4 | 8.5 | 94.5 | 0 | 0 |

**Mean total elapsed per run:** 164s  |  Min: 72s  |  Max: 620s


---

## File: `WebGoat_Code_SQLiteProfileProvider.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Use of BinaryFormatter in Profile Property Serialization | High | 100% (12/12) | [0.76, 1.00] | 0.95 | 0.000 | HYP-001 |
| Potential SQL Injection via String Concatenation | High | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-002 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 15.5 | 21.2 | 6.4 | 61.0 | 0 | 0 |
| threat | 18.8 | 20.0 | 10.1 | 62.1 | 0 | 0 |
| hypotheses | 24.5 | 30.5 | 11.3 | 90.0 | 0 | 0 |
| evidence | 31.0 | 40.8 | 13.4 | 118.6 | 0 | 0 |
| fix | 17.4 | 18.9 | 9.2 | 58.0 | 0 | 0 |
| gate | 17.8 | 24.4 | 7.3 | 70.2 | 0 | 0 |
| pre_scan | 16.3 | 22.0 | 6.8 | 63.5 | 0 | 0 |

**Mean total elapsed per run:** 141s  |  Min: 65s  |  Max: 523s


---

## File: `WebGoat_Code_SQLiteRoleProvider.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Missing Authorization Check in Role Management Methods | High | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-001 |
| Potential SQL Injection Vulnerability in FindUsersInRole | High | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-002 |
| Insecure Direct Object Reference in Role Management | High | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-003 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 15.1 | 20.7 | 6.2 | 59.6 | 0 | 0 |
| threat | 27.0 | 29.7 | 14.1 | 90.8 | 0 | 0 |
| hypotheses | 30.8 | 40.4 | 13.4 | 117.5 | 0 | 0 |
| evidence | 63.1 | 85.7 | 26.2 | 247.0 | 0 | 0 |
| fix | 58.7 | 76.5 | 25.7 | 222.8 | 0 | 0 |
| gate | 38.4 | 60.8 | 12.3 | 168.7 | 0 | 0 |
| pre_scan | 20.0 | 26.8 | 8.4 | 77.6 | 0 | 0 |

**Mean total elapsed per run:** 253s  |  Min: 106s  |  Max: 984s


---

## File: `WebGoat_Configuration_Default.config`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 12

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 4.5 | 3.9 | 2.8 | 13.0 | 0 | 0 |
| threat | 7.6 | 7.2 | 4.5 | 23.2 | 0 | 0 |
| hypotheses | 6.6 | 7.4 | 3.3 | 22.6 | 0 | 0 |
| evidence | 5.5 | 5.6 | 3.1 | 17.7 | 0 | 0 |
| fix | 7.6 | 6.6 | 4.7 | 21.8 | 0 | 0 |
| gate | 8.0 | 9.4 | 3.9 | 28.2 | 0 | 0 |
| pre_scan | 3.2 | 2.9 | 1.9 | 9.5 | 0 | 0 |

**Mean total elapsed per run:** 43s  |  Min: 24s  |  Max: 136s


---

## File: `WebGoat_Content_About.aspx.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Potential Missing Authorization Check | Medium | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-001 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 6.1 | 5.2 | 3.9 | 17.2 | 0 | 0 |
| threat | 13.0 | 12.8 | 7.4 | 40.6 | 0 | 0 |
| hypotheses | 12.2 | 14.8 | 5.8 | 44.0 | 0 | 0 |
| evidence | 10.6 | 13.2 | 4.9 | 38.9 | 0 | 0 |
| fix | 10.5 | 9.6 | 6.3 | 31.2 | 0 | 0 |
| gate | 11.8 | 14.2 | 5.7 | 42.4 | 0 | 0 |
| pre_scan | 4.2 | 4.7 | 2.1 | 14.3 | 0 | 0 |

**Mean total elapsed per run:** 68s  |  Min: 36s  |  Max: 229s


---

## File: `WebGoat_Content_About.aspx.designer.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 12

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.0 | 4.5 | 3.1 | 14.7 | 0 | 0 |
| threat | 7.9 | 7.5 | 4.6 | 24.0 | 0 | 0 |
| hypotheses | 7.9 | 8.9 | 4.1 | 27.0 | 0 | 0 |
| evidence | 6.5 | 7.0 | 3.5 | 21.5 | 0 | 0 |
| fix | 8.2 | 7.1 | 5.0 | 23.5 | 0 | 0 |
| gate | 8.8 | 10.3 | 4.3 | 31.0 | 0 | 0 |
| pre_scan | 3.6 | 4.6 | 1.6 | 13.5 | 0 | 0 |

**Mean total elapsed per run:** 48s  |  Min: 26s  |  Max: 155s


---

## File: `WebGoat_Content_BasicAuth.aspx.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Potential Missing Authorization Check | Medium | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-001 |
| Missing Authentication Logic | High | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-002 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.7 | 5.0 | 3.5 | 16.5 | 0 | 0 |
| threat | 12.1 | 11.8 | 7.0 | 37.6 | 0 | 0 |
| hypotheses | 14.9 | 17.5 | 7.4 | 52.5 | 0 | 0 |
| evidence | 15.3 | 19.2 | 7.0 | 56.6 | 0 | 0 |
| fix | 15.8 | 15.4 | 9.0 | 48.9 | 0 | 0 |
| gate | 13.3 | 19.6 | 4.9 | 55.2 | 0 | 0 |
| pre_scan | 4.5 | 5.4 | 2.2 | 16.0 | 0 | 0 |

**Mean total elapsed per run:** 82s  |  Min: 41s  |  Max: 283s


---

## File: `WebGoat_Content_BasicAuth.aspx.designer.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 12

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 4.9 | 4.3 | 3.0 | 14.2 | 0 | 0 |
| threat | 16.4 | 16.0 | 9.5 | 50.9 | 0 | 0 |
| hypotheses | 17.0 | 20.2 | 8.3 | 60.4 | 0 | 0 |
| evidence | 15.5 | 17.0 | 8.2 | 52.1 | 0 | 0 |
| fix | 3.5 | 4.1 | 1.7 | 12.2 | 0 | 0 |
| gate | 14.0 | 16.4 | 7.0 | 49.2 | 0 | 0 |
| pre_scan | 6.0 | 7.4 | 2.8 | 21.8 | 0 | 0 |

**Mean total elapsed per run:** 77s  |  Min: 40s  |  Max: 261s


---

## File: `WebGoat_Content_Challenge1.aspx.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Potential Missing Authorization Check | Medium | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-001 |
| Verbose Error Handling | Low | 100% (12/12) | [0.76, 1.00] | 0.85 | — | HYP-002 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 6.8 | 5.9 | 4.2 | 19.6 | 0 | 0 |
| threat | 13.2 | 13.1 | 7.5 | 41.5 | 0 | 0 |
| hypotheses | 16.7 | 19.5 | 8.2 | 58.6 | 0 | 0 |
| evidence | 13.0 | 14.1 | 6.9 | 43.3 | 0 | 0 |
| fix | 16.4 | 16.0 | 9.5 | 50.9 | 0 | 0 |
| gate | 13.2 | 17.2 | 5.8 | 50.1 | 0 | 0 |
| pre_scan | 5.0 | 6.4 | 2.3 | 18.7 | 0 | 0 |

**Mean total elapsed per run:** 84s  |  Min: 45s  |  Max: 283s


---

## File: `WebGoat_Content_Challenge1.aspx.designer.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Potential Missing Authorization Check | Medium | 100% (12/12) | [0.76, 1.00] | 0.30 | — | HYP-001 |
| Debug/Verbose Error Handling Possible | Low | 100% (12/12) | [0.76, 1.00] | 0.30 | — | HYP-002 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.3 | 4.7 | 3.3 | 15.5 | 0 | 0 |
| threat | 13.3 | 12.9 | 7.7 | 41.1 | 0 | 0 |
| hypotheses | 12.4 | 14.5 | 6.1 | 43.5 | 0 | 0 |
| evidence | 11.4 | 12.0 | 6.1 | 37.3 | 0 | 0 |
| fix | 16.6 | 16.1 | 9.7 | 51.2 | 0 | 0 |
| gate | 12.3 | 15.9 | 5.4 | 46.4 | 0 | 0 |
| pre_scan | 5.1 | 6.6 | 2.2 | 19.3 | 0 | 0 |

**Mean total elapsed per run:** 76s  |  Min: 41s  |  Max: 254s


---

## File: `WebGoat_Content_Challenge2.aspx.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Potential Missing Authorization Check | Medium | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-001 |
| Verbose Error Handling | Low | 100% (12/12) | [0.76, 1.00] | 0.85 | — | HYP-002 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 6.7 | 5.8 | 4.1 | 19.2 | 0 | 0 |
| threat | 12.6 | 12.5 | 7.2 | 39.5 | 0 | 0 |
| hypotheses | 16.2 | 18.8 | 8.1 | 56.6 | 0 | 0 |
| evidence | 13.0 | 14.0 | 6.9 | 43.0 | 0 | 0 |
| fix | 17.1 | 16.7 | 9.8 | 53.1 | 0 | 0 |
| gate | 23.3 | 29.3 | 10.7 | 86.3 | 0 | 0 |
| pre_scan | 5.1 | 6.5 | 2.2 | 19.0 | 0 | 0 |

**Mean total elapsed per run:** 94s  |  Min: 49s  |  Max: 317s


---

## File: `WebGoat_Content_Challenge2.aspx.designer.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Potential Missing Authorization Check | Medium | 100% (12/12) | [0.76, 1.00] | 0.30 | — | HYP-001 |
| Possible Debug/Verbose Logging Enabled | Low | 100% (12/12) | [0.76, 1.00] | 0.40 | 0.000 | HYP-002 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.1 | 4.6 | 3.1 | 14.9 | 0 | 0 |
| threat | 11.6 | 11.2 | 6.8 | 35.7 | 0 | 0 |
| hypotheses | 11.1 | 12.7 | 5.6 | 38.4 | 0 | 0 |
| evidence | 11.2 | 11.8 | 6.1 | 36.6 | 0 | 0 |
| fix | 13.4 | 12.9 | 7.8 | 41.1 | 0 | 0 |
| gate | 13.2 | 18.8 | 5.2 | 53.5 | 0 | 0 |
| pre_scan | 5.3 | 7.2 | 2.2 | 20.7 | 0 | 0 |

**Mean total elapsed per run:** 71s  |  Min: 37s  |  Max: 241s


---

## File: `WebGoat_Content_Challenge3.aspx.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Potential Missing Authorization Check | Medium | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-001 |
| Verbose Error Handling | Low | 100% (12/12) | [0.76, 1.00] | 0.85 | — | HYP-002 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 6.8 | 5.8 | 4.2 | 19.3 | 0 | 0 |
| threat | 14.1 | 14.1 | 8.0 | 44.4 | 0 | 0 |
| hypotheses | 18.7 | 22.0 | 9.2 | 65.9 | 0 | 0 |
| evidence | 16.0 | 17.5 | 8.5 | 53.5 | 0 | 0 |
| fix | 17.8 | 18.1 | 10.0 | 56.7 | 0 | 0 |
| gate | 12.8 | 17.0 | 5.4 | 49.4 | 0 | 0 |
| pre_scan | 8.5 | 5.9 | 4.1 | 20.9 | 0 | 0 |

**Mean total elapsed per run:** 95s  |  Min: 50s  |  Max: 310s


---

## File: `WebGoat_Content_Challenge3.aspx.designer.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Possible Debug/Verbose Logging Enabled | Low | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-002 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.3 | 4.7 | 3.2 | 15.4 | 0 | 0 |
| threat | 11.8 | 11.4 | 6.8 | 36.2 | 0 | 0 |
| hypotheses | 11.1 | 12.8 | 5.5 | 38.5 | 0 | 0 |
| evidence | 11.0 | 11.5 | 6.0 | 35.8 | 0 | 0 |
| fix | 8.0 | 7.7 | 4.6 | 24.6 | 0 | 0 |
| gate | 12.0 | 14.3 | 5.8 | 42.8 | 0 | 0 |
| pre_scan | 5.1 | 6.7 | 2.2 | 19.5 | 0 | 0 |

**Mean total elapsed per run:** 64s  |  Min: 34s  |  Max: 213s


---

## File: `WebGoat_Content_ChangePwd.aspx.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Potential Authentication Bypass in Password Change Page | Critical | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-001 |
| Missing Authorization Check in Password Change Functionality | High | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-002 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 6.5 | 5.7 | 4.0 | 18.7 | 0 | 0 |
| threat | 23.3 | 23.5 | 13.0 | 73.8 | 0 | 0 |
| hypotheses | 20.2 | 25.2 | 9.2 | 74.3 | 0 | 0 |
| evidence | 19.8 | 21.4 | 10.5 | 65.8 | 0 | 0 |
| fix | 21.4 | 22.7 | 11.6 | 70.2 | 0 | 0 |
| gate | 15.4 | 21.0 | 6.4 | 60.5 | 0 | 0 |
| pre_scan | 4.9 | 6.1 | 2.2 | 18.0 | 0 | 0 |

**Mean total elapsed per run:** 111s  |  Min: 57s  |  Max: 381s


---

## File: `WebGoat_Default.aspx.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Information Exposure Through Server Name in Cookie | Medium | 100% (12/12) | [0.76, 1.00] | 0.87 | 0.025 | HYP-001 |

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Session Identifier Exposure in ViewState | Medium | 33% (4/12) | 0.90 | model inconsistency |
| Session Hijacking via ViewState Session ID Storage | High | 33% (4/12) | 0.90 | model inconsistency |
| Missing Authorization Check on Database Rebuild Functionality | High | 67% (8/12) | 0.75 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 7.4 | 6.7 | 4.5 | 21.9 | 0 | 0 |
| threat | 18.8 | 18.5 | 9.9 | 58.5 | 0 | 0 |
| hypotheses | 21.0 | 24.9 | 9.6 | 74.4 | 0 | 0 |
| evidence | 21.1 | 22.6 | 9.9 | 69.5 | 0 | 0 |
| fix | 16.0 | 15.9 | 8.5 | 50.1 | 0 | 0 |
| gate | 14.9 | 19.0 | 6.1 | 55.7 | 0 | 0 |
| pre_scan | 12.5 | 18.3 | 4.5 | 51.9 | 0 | 0 |

**Mean total elapsed per run:** 112s  |  Min: 53s  |  Max: 382s


---

## File: `WebGoat_Default.aspx.designer.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Potential Missing Authorization Check | High | 100% (12/12) | [0.76, 1.00] | 0.30 | — | HYP-001 |
| Potential Sensitive Data Exposure | Medium | 100% (12/12) | [0.76, 1.00] | 0.30 | — | HYP-002 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 4.9 | 4.4 | 3.0 | 14.5 | 0 | 0 |
| threat | 13.5 | 13.0 | 7.8 | 41.5 | 0 | 0 |
| hypotheses | 12.3 | 14.1 | 6.0 | 42.5 | 0 | 0 |
| evidence | 12.9 | 13.4 | 7.0 | 41.8 | 0 | 0 |
| fix | 18.1 | 18.0 | 9.9 | 56.8 | 0 | 0 |
| gate | 15.4 | 19.8 | 6.8 | 57.9 | 0 | 0 |
| pre_scan | 5.5 | 7.4 | 2.2 | 21.4 | 0 | 0 |

**Mean total elapsed per run:** 83s  |  Min: 43s  |  Max: 276s


---

## File: `WebGoat_ForgotPassword.aspx.cs`

**Runs with this file:** 12  |  **Gate consistency:** 67%  |  **Verdict distribution:** FAIL: 8  NEEDS_HUMAN: 4

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Potential Missing Authorization Check in Password Reset Functionality | High | 100% (12/12) | [0.76, 1.00] | 0.70 | 0.295 | HYP-001 |
| Possible Information Disclosure in Password Reset Flow | Medium | 100% (12/12) | [0.76, 1.00] | 0.70 | 0.295 | HYP-002 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.6 | 4.9 | 3.5 | 16.1 | 0 | 0 |
| threat | 13.9 | 13.6 | 8.0 | 43.1 | 0 | 0 |
| hypotheses | 19.9 | 23.9 | 8.6 | 71.3 | 0 | 0 |
| evidence | 18.5 | 19.3 | 9.5 | 59.8 | 0 | 0 |
| fix | 18.2 | 18.7 | 10.0 | 58.4 | 0 | 0 |
| gate | 15.9 | 19.0 | 6.2 | 56.4 | 0 | 0 |
| pre_scan | 5.2 | 6.8 | 2.2 | 19.9 | 0 | 0 |

**Mean total elapsed per run:** 97s  |  Min: 50s  |  Max: 325s


---

## File: `WebGoat_ForgotPassword.aspx.designer.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 12

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.1 | 4.6 | 3.1 | 15.0 | 0 | 0 |
| threat | 11.9 | 13.0 | 4.6 | 39.8 | 0 | 0 |
| hypotheses | 11.5 | 14.6 | 4.0 | 42.8 | 0 | 0 |
| evidence | 10.5 | 12.2 | 4.2 | 36.7 | 0 | 0 |
| fix | 4.4 | 3.3 | 1.5 | 10.1 | 0 | 0 |
| gate | 10.9 | 12.4 | 5.4 | 37.6 | 0 | 0 |
| pre_scan | 5.5 | 7.3 | 2.3 | 21.1 | 0 | 0 |

**Mean total elapsed per run:** 60s  |  Min: 29s  |  Max: 203s


---

## File: `WebGoat_Global.asax.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Potential Insecure Role Assignment | High | 100% (12/12) | [0.76, 1.00] | 0.85 | — | HYP-002 |
| Potential Information Disclosure via Debug Mode | Medium | 100% (12/12) | [0.76, 1.00] | 0.80 | 0.000 | HYP-004 |

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| X-XSS-Protection Header Set to Zero | Medium | 33% (4/12) | 0.90 | model inconsistency |
| X-XSS-Protection Header Set to Disabled | High | 67% (8/12) | 0.90 | model inconsistency |
| Possible Weak Authentication Ticket Handling | Medium | 67% (8/12) | 0.80 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 14.3 | 13.6 | 8.5 | 43.5 | 0 | 0 |
| threat | 24.5 | 27.9 | 12.1 | 84.4 | 0 | 0 |
| hypotheses | 26.6 | 34.0 | 11.3 | 99.6 | 0 | 0 |
| evidence | 34.5 | 39.4 | 15.8 | 119.0 | 0 | 0 |
| fix | 36.7 | 43.4 | 17.5 | 129.9 | 0 | 0 |
| gate | 28.5 | 43.3 | 9.7 | 121.4 | 0 | 0 |
| pre_scan | 8.6 | 10.7 | 4.0 | 31.5 | 0 | 0 |

**Mean total elapsed per run:** 174s  |  Min: 81s  |  Max: 629s


---

## File: `WebGoat_LoginPage.aspx.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 12

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Authentication Bypass via Redirect | High | 33% (4/12) | 0.95 | model inconsistency |
| Missing Authentication Logic | High | 33% (4/12) | 0.90 | model inconsistency |
| Insecure Direct Object Reference | Medium | 33% (4/12) | 0.85 | model inconsistency |
| Bypassable Authentication Logic | High | 67% (8/12) | 0.90 | model inconsistency |
| Missing Authentication Implementation | High | 67% (8/12) | 0.90 | model inconsistency |
| Commented-Out Security Controls | Medium | 67% (8/12) | 0.90 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 9.2 | 8.1 | 5.6 | 26.7 | 0 | 0 |
| threat | 17.3 | 18.4 | 9.1 | 56.8 | 0 | 0 |
| hypotheses | 21.2 | 26.4 | 9.4 | 77.8 | 0 | 0 |
| evidence | 28.6 | 35.0 | 11.0 | 103.6 | 0 | 0 |
| fix | 38.5 | 49.7 | 12.2 | 144.9 | 0 | 0 |
| gate | 21.0 | 32.2 | 6.3 | 90.0 | 0 | 0 |
| pre_scan | 9.8 | 14.4 | 3.5 | 40.7 | 0 | 0 |

**Mean total elapsed per run:** 146s  |  Min: 57s  |  Max: 540s


---

## File: `WebGoat_LoginPage.aspx.designer.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Potential Missing Authentication Check on Admin Login Button | High | 100% (12/12) | [0.76, 1.00] | 0.30 | — | HYP-001 |
| Missing Authorization Check for Admin Functionality | High | 100% (12/12) | [0.76, 1.00] | 0.30 | — | HYP-002 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.1 | 4.6 | 3.1 | 15.0 | 0 | 0 |
| threat | 11.5 | 10.9 | 6.6 | 35.0 | 0 | 0 |
| hypotheses | 12.7 | 14.7 | 6.0 | 44.4 | 0 | 0 |
| evidence | 13.7 | 14.9 | 7.1 | 45.7 | 0 | 0 |
| fix | 18.9 | 19.0 | 10.5 | 59.8 | 0 | 0 |
| gate | 15.0 | 19.9 | 6.2 | 57.7 | 0 | 0 |
| pre_scan | 6.6 | 9.6 | 2.4 | 27.3 | 0 | 0 |

**Mean total elapsed per run:** 84s  |  Min: 42s  |  Max: 285s


---

## File: `WebGoat_ProxySetup.aspx.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Misuse of String Reversal Functionality | Medium | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-001, HYP-006 |

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Potential XSS Vulnerability via txtName.Text Input | Medium | 67% (8/12) | 0.90 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 7.3 | 6.4 | 4.5 | 21.1 | 0 | 0 |
| threat | 15.2 | 15.1 | 8.4 | 47.6 | 0 | 0 |
| hypotheses | 24.7 | 29.5 | 11.7 | 88.1 | 0 | 0 |
| evidence | 30.3 | 36.3 | 13.4 | 108.3 | 0 | 0 |
| fix | 27.8 | 36.8 | 7.3 | 106.4 | 0 | 0 |
| gate | 18.1 | 25.4 | 6.7 | 72.6 | 0 | 0 |
| pre_scan | 4.3 | 5.7 | 1.8 | 16.5 | 0 | 0 |

**Mean total elapsed per run:** 128s  |  Min: 55s  |  Max: 460s


---

## File: `WebGoat_ProxySetup.aspx.designer.cs`

**Runs with this file:** 12  |  **Gate consistency:** 67%  |  **Verdict distribution:** FAIL: 4  NEEDS_HUMAN: 8

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Potential Command Injection via TextBox Input | High | 33% (4/12) | 0.30 | borderline confidence |
| Missing Authorization Check on Sensitive Operation | High | 33% (4/12) | 0.30 | borderline confidence |
| Hardcoded Configuration Values in UI Controls | Medium | 33% (4/12) | 0.40 | borderline confidence |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.4 | 4.9 | 3.2 | 15.9 | 0 | 0 |
| threat | 16.3 | 16.0 | 9.3 | 50.7 | 0 | 0 |
| hypotheses | 17.2 | 20.9 | 7.7 | 62.1 | 0 | 0 |
| evidence | 13.9 | 14.2 | 6.7 | 44.4 | 0 | 0 |
| fix | 7.5 | 5.8 | 2.0 | 13.6 | 0 | 0 |
| gate | 15.6 | 17.2 | 7.7 | 52.6 | 0 | 0 |
| pre_scan | 7.7 | 10.9 | 3.0 | 31.0 | 0 | 0 |

**Mean total elapsed per run:** 84s  |  Min: 41s  |  Max: 269s


---

## File: `WebGoat_Web.config`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Hardcoded Credentials in Clear Text | Critical | 100% (12/12) | [0.76, 1.00] | 0.93 | 0.049 | HYP-001 |
| Debug Mode Enabled in Production Configuration | High | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-004 |
| Verbose Logging Enabled in Production | Medium | 100% (12/12) | [0.76, 1.00] | 0.87 | 0.049 | HYP-005 |

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Insecure Session Cookie Configuration | High | 33% (4/12) | 0.90 | model inconsistency |
| Inconsistent Authorization Controls on Sensitive Resource | High | 33% (4/12) | 0.90 | model inconsistency |
| Header Injection Vulnerability Due to Disabled Header Checking | High | 33% (4/12) | 0.90 | model inconsistency |
| Insecure Session Cookie Configuration | Medium | 67% (8/12) | 0.90 | model inconsistency |
| Inconsistent Authorization Policy for VerbTamperingAttack.aspx | High | 67% (8/12) | 0.90 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 14.7 | 18.5 | 6.7 | 54.4 | 0 | 0 |
| threat | 33.8 | 38.7 | 16.5 | 116.9 | 0 | 0 |
| hypotheses | 32.0 | 43.6 | 13.0 | 125.6 | 0 | 0 |
| evidence | 41.2 | 55.4 | 16.8 | 160.2 | 0 | 0 |
| fix | 37.9 | 43.8 | 18.8 | 132.0 | 0 | 0 |
| gate | 27.5 | 39.5 | 9.3 | 112.2 | 0 | 0 |
| pre_scan | 24.8 | 33.3 | 10.4 | 96.3 | 0 | 0 |

**Mean total elapsed per run:** 212s  |  Min: 92s  |  Max: 798s


---

## File: `WebGoat_WebGoat.NET.csproj`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Debug Mode Enabled in MSBuild Configuration | High | 100% (12/12) | [0.76, 1.00] | 0.95 | 0.000 | HYP-001 |
| Unsafe Code Blocks Enabled | Medium | 100% (12/12) | [0.76, 1.00] | 0.85 | — | HYP-002 |
| Hardcoded Environment Variables for Mono Logging | Medium | 100% (12/12) | [0.76, 1.00] | 0.75 | — | HYP-003 |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 18.0 | 25.3 | 7.1 | 72.3 | 0 | 0 |
| threat | 24.7 | 27.3 | 12.8 | 83.3 | 0 | 0 |
| hypotheses | 23.7 | 31.1 | 10.4 | 90.5 | 0 | 0 |
| evidence | 31.8 | 42.4 | 13.5 | 122.7 | 0 | 0 |
| fix | 30.4 | 33.7 | 15.8 | 103.0 | 0 | 0 |
| gate | 25.8 | 37.2 | 9.8 | 105.6 | 0 | 0 |
| pre_scan | 21.7 | 30.0 | 8.8 | 86.2 | 0 | 0 |

**Mean total elapsed per run:** 176s  |  Min: 78s  |  Max: 664s


---

## File: `WebGoat_dbtest.aspx.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 12

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Missing Authentication Check on Database Reconfiguration | High | 100% (12/12) | [0.76, 1.00] | 0.93 | 0.025 | HYP-001 |
| Insecure Direct Object Reference in Configuration Handling | Medium | 100% (12/12) | [0.76, 1.00] | 0.90 | — | HYP-003 |

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Lack of Input Validation in Configuration Updates | Medium | 33% (4/12) | 0.90 | model inconsistency |
| Denial of Service via Malformed Configuration Inputs | Medium | 33% (4/12) | 0.90 | model inconsistency |
| Potential SQL Injection via Configuration File Updates | Medium | 67% (8/12) | 0.85 | model inconsistency |
| Hardcoded Database Connection Strings in Configuration Files | High | 67% (8/12) | 0.90 | model inconsistency |
| Unrestricted Database Rebuild Access | High | 67% (8/12) | 0.95 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 9.7 | 10.1 | 5.3 | 31.4 | 0 | 0 |
| threat | 27.7 | 31.9 | 12.5 | 96.2 | 0 | 0 |
| hypotheses | 30.5 | 40.6 | 12.6 | 117.6 | 0 | 0 |
| evidence | 40.0 | 52.3 | 17.2 | 152.2 | 0 | 0 |
| fix | 41.6 | 49.3 | 20.2 | 147.5 | 0 | 0 |
| gate | 27.3 | 42.0 | 8.3 | 117.3 | 0 | 0 |
| pre_scan | 16.6 | 22.8 | 6.5 | 65.6 | 0 | 0 |

**Mean total elapsed per run:** 193s  |  Min: 84s  |  Max: 728s


---

## File: `WebGoat_dbtest.aspx.designer.cs`

**Runs with this file:** 12  |  **Gate consistency:** 67%  |  **Verdict distribution:** FAIL: 8  NEEDS_HUMAN: 4

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std | Source HYP(s) |
|---|---|---|---|---|---|---|
| Hardcoded Database Credentials in UI Controls | High | 100% (12/12) | [0.76, 1.00] | 0.30 | — | HYP-001 |

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Missing Authorization Check on Database Rebuild Functionality | High | 33% (4/12) | 0.30 | borderline confidence |
| Potential SQL Injection Vulnerability via User Input | High | 33% (4/12) | 0.30 | borderline confidence |
| Missing Authorization Check on Database Rebuild Functionality | Critical | 67% (8/12) | 0.30 | borderline confidence |
| Potential Exposure of Sensitive Data via UI Controls | Medium | 67% (8/12) | 0.30 | borderline confidence |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 7.8 | 9.2 | 3.8 | 27.5 | 0 | 0 |
| threat | 16.4 | 16.1 | 9.5 | 51.1 | 0 | 0 |
| hypotheses | 17.8 | 21.2 | 8.6 | 63.3 | 0 | 0 |
| evidence | 28.0 | 35.3 | 12.5 | 103.8 | 0 | 0 |
| fix | 23.8 | 27.0 | 11.2 | 81.8 | 0 | 0 |
| gate | 22.3 | 30.2 | 9.0 | 87.2 | 0 | 0 |
| pre_scan | 13.7 | 22.3 | 4.1 | 61.5 | 0 | 0 |

**Mean total elapsed per run:** 130s  |  Min: 59s  |  Max: 476s


---

## Gate verdict detail per run


### `WebGoat_AddNewUser.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass9 | FAIL |

### `WebGoat_AddNewUser.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass9 | NEEDS_HUMAN |

### `WebGoat_App_Code_ConfigFile.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass9 | NEEDS_HUMAN |

### `WebGoat_App_Code_CookieManager.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass9 | NEEDS_HUMAN |

### `WebGoat_App_Code_CustomerLoginData.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | PASS |
| results_qwen3-coder-30b_temp0.0_pass10 | PASS |
| results_qwen3-coder-30b_temp0.0_pass11 | PASS |
| results_qwen3-coder-30b_temp0.0_pass12 | PASS |
| results_qwen3-coder-30b_temp0.0_pass2 | PASS |
| results_qwen3-coder-30b_temp0.0_pass3 | PASS |
| results_qwen3-coder-30b_temp0.0_pass4 | PASS |
| results_qwen3-coder-30b_temp0.0_pass5 | PASS |
| results_qwen3-coder-30b_temp0.0_pass6 | PASS |
| results_qwen3-coder-30b_temp0.0_pass7 | PASS |
| results_qwen3-coder-30b_temp0.0_pass8 | PASS |
| results_qwen3-coder-30b_temp0.0_pass9 | PASS |

### `WebGoat_App_Code_DB_DbConstants.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass9 | NEEDS_HUMAN |

### `WebGoat_App_Code_DB_DbProviderFactory.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | PASS |
| results_qwen3-coder-30b_temp0.0_pass10 | PASS |
| results_qwen3-coder-30b_temp0.0_pass11 | PASS |
| results_qwen3-coder-30b_temp0.0_pass12 | PASS |
| results_qwen3-coder-30b_temp0.0_pass2 | PASS |
| results_qwen3-coder-30b_temp0.0_pass3 | PASS |
| results_qwen3-coder-30b_temp0.0_pass4 | PASS |
| results_qwen3-coder-30b_temp0.0_pass5 | PASS |
| results_qwen3-coder-30b_temp0.0_pass6 | PASS |
| results_qwen3-coder-30b_temp0.0_pass7 | PASS |
| results_qwen3-coder-30b_temp0.0_pass8 | PASS |
| results_qwen3-coder-30b_temp0.0_pass9 | PASS |

### `WebGoat_App_Code_DB_DummyDbProvider.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass9 | NEEDS_HUMAN |

### `WebGoat_App_Code_DB_IDbProvider.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass9 | NEEDS_HUMAN |

### `WebGoat_App_Code_DB_MySqlDbProvider.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass9 | FAIL |

### `WebGoat_App_Code_DB_SqliteDbProvider.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass9 | FAIL |

### `WebGoat_App_Code_Encoder.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass9 | FAIL |

### `WebGoat_App_Code_Settings.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass9 | NEEDS_HUMAN |

### `WebGoat_App_Code_Util.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass9 | FAIL |

### `WebGoat_App_Code_VeryWeakRandom.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass9 | NEEDS_HUMAN |

### `WebGoat_App_Code_WeakMessageDigest.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass9 | NEEDS_HUMAN |

### `WebGoat_App_Code_WeakRandom.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass9 | FAIL |

### `WebGoat_App_Data_XmlInjectionUsers.xml`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass9 | FAIL |

### `WebGoat_ChangePassword.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass9 | NEEDS_HUMAN |

### `WebGoat_ChangePassword.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass9 | NEEDS_HUMAN |

### `WebGoat_Code_DatabaseUtilities.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass9 | FAIL |

### `WebGoat_Code_IOHelper.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass9 | NEEDS_HUMAN |

### `WebGoat_Code_SQLiteMembershipProvider.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass9 | FAIL |

### `WebGoat_Code_SQLiteProfileProvider.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass9 | FAIL |

### `WebGoat_Code_SQLiteRoleProvider.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass9 | FAIL |

### `WebGoat_Configuration_Default.config`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass9 | NEEDS_HUMAN |

### `WebGoat_Content_About.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass9 | NEEDS_HUMAN |

### `WebGoat_Content_About.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass9 | NEEDS_HUMAN |

### `WebGoat_Content_BasicAuth.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass9 | FAIL |

### `WebGoat_Content_BasicAuth.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass9 | NEEDS_HUMAN |

### `WebGoat_Content_Challenge1.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass9 | FAIL |

### `WebGoat_Content_Challenge1.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass9 | NEEDS_HUMAN |

### `WebGoat_Content_Challenge2.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass9 | FAIL |

### `WebGoat_Content_Challenge2.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass9 | NEEDS_HUMAN |

### `WebGoat_Content_Challenge3.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass9 | NEEDS_HUMAN |

### `WebGoat_Content_Challenge3.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass9 | NEEDS_HUMAN |

### `WebGoat_Content_ChangePwd.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass9 | FAIL |

### `WebGoat_Default.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass9 | FAIL |

### `WebGoat_Default.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass9 | NEEDS_HUMAN |

### `WebGoat_ForgotPassword.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass9 | FAIL |

### `WebGoat_ForgotPassword.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass9 | NEEDS_HUMAN |

### `WebGoat_Global.asax.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass9 | FAIL |

### `WebGoat_LoginPage.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass9 | FAIL |

### `WebGoat_LoginPage.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass9 | NEEDS_HUMAN |

### `WebGoat_ProxySetup.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass9 | NEEDS_HUMAN |

### `WebGoat_ProxySetup.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass9 | NEEDS_HUMAN |

### `WebGoat_Web.config`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass9 | FAIL |

### `WebGoat_WebGoat.NET.csproj`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass9 | FAIL |

### `WebGoat_dbtest.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass9 | FAIL |

### `WebGoat_dbtest.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.0_pass9 | FAIL |