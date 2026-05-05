# Scan stability analysis — Qwen3-Coder-30b temp=0.7

**Runs analysed:** 10  |  **Files:** 50  |  **Stability threshold:** 80%

## Summary
| File | Runs | Gate: PASS | FAIL | NEEDS_HUMAN | Gate consistency | Stable findings | Sensitive findings |
|---|---|---|---|---|---|---|---|
| `WebGoat_AddNewUser.aspx.cs` | 10 | 0 | 6 | 4 | 60% | 0 | 6 |
| `WebGoat_AddNewUser.aspx.designer.cs` | 10 | 0 | 4 | 6 | 60% | 1 | 4 |
| `WebGoat_App_Code_ConfigFile.cs` | 10 | 0 | 0 | 10 | 100% | 1 | 0 |
| `WebGoat_App_Code_CookieManager.cs` | 10 | 0 | 0 | 10 | 100% | 1 | 0 |
| `WebGoat_App_Code_CustomerLoginData.cs` | 10 | 10 | 0 | 0 | 100% | 2 | 0 |
| `WebGoat_App_Code_DB_DbConstants.cs` | 10 | 0 | 0 | 10 | 100% | 0 | 0 |
| `WebGoat_App_Code_DB_DbProviderFactory.cs` | 10 | 10 | 0 | 0 | 100% | 2 | 0 |
| `WebGoat_App_Code_DB_DummyDbProvider.cs` | 10 | 0 | 0 | 10 | 100% | 3 | 0 |
| `WebGoat_App_Code_DB_IDbProvider.cs` | 10 | 0 | 0 | 10 | 100% | 3 | 0 |
| `WebGoat_App_Code_DB_MySqlDbProvider.cs` | 10 | 0 | 10 | 0 | 100% | 3 | 0 |
| `WebGoat_App_Code_DB_SqliteDbProvider.cs` | 10 | 0 | 10 | 0 | 100% | 10 | 0 |
| `WebGoat_App_Code_Encoder.cs` | 10 | 0 | 10 | 0 | 100% | 3 | 0 |
| `WebGoat_App_Code_Settings.cs` | 10 | 0 | 0 | 10 | 100% | 1 | 0 |
| `WebGoat_App_Code_Util.cs` | 10 | 0 | 10 | 0 | 100% | 5 | 0 |
| `WebGoat_App_Code_VeryWeakRandom.cs` | 10 | 0 | 0 | 10 | 100% | 1 | 0 |
| `WebGoat_App_Code_WeakMessageDigest.cs` | 10 | 0 | 0 | 10 | 100% | 1 | 0 |
| `WebGoat_App_Code_WeakRandom.cs` | 10 | 0 | 10 | 0 | 100% | 1 | 0 |
| `WebGoat_App_Data_XmlInjectionUsers.xml` | 10 | 0 | 10 | 0 | 100% | 2 | 0 |
| `WebGoat_ChangePassword.aspx.cs` | 10 | 0 | 0 | 10 | 100% | 0 | 4 |
| `WebGoat_ChangePassword.aspx.designer.cs` | 10 | 0 | 0 | 10 | 100% | 0 | 4 |
| `WebGoat_Code_DatabaseUtilities.cs` | 10 | 0 | 10 | 0 | 100% | 5 | 0 |
| `WebGoat_Code_IOHelper.cs` | 10 | 0 | 0 | 10 | 100% | 2 | 0 |
| `WebGoat_Code_SQLiteMembershipProvider.cs` | 10 | 0 | 10 | 0 | 100% | 3 | 0 |
| `WebGoat_Code_SQLiteProfileProvider.cs` | 10 | 0 | 10 | 0 | 100% | 2 | 0 |
| `WebGoat_Code_SQLiteRoleProvider.cs` | 10 | 0 | 10 | 0 | 100% | 3 | 0 |
| `WebGoat_Configuration_Default.config` | 10 | 0 | 0 | 10 | 100% | 0 | 0 |
| `WebGoat_Content_About.aspx.cs` | 10 | 0 | 0 | 10 | 100% | 1 | 0 |
| `WebGoat_Content_About.aspx.designer.cs` | 10 | 0 | 0 | 10 | 100% | 0 | 0 |
| `WebGoat_Content_BasicAuth.aspx.cs` | 10 | 0 | 10 | 0 | 100% | 2 | 0 |
| `WebGoat_Content_BasicAuth.aspx.designer.cs` | 10 | 0 | 0 | 10 | 100% | 0 | 0 |
| `WebGoat_Content_Challenge1.aspx.cs` | 10 | 0 | 10 | 0 | 100% | 2 | 0 |
| `WebGoat_Content_Challenge1.aspx.designer.cs` | 10 | 0 | 0 | 10 | 100% | 2 | 0 |
| `WebGoat_Content_Challenge2.aspx.cs` | 10 | 0 | 10 | 0 | 100% | 2 | 0 |
| `WebGoat_Content_Challenge2.aspx.designer.cs` | 10 | 0 | 0 | 10 | 100% | 2 | 0 |
| `WebGoat_Content_Challenge3.aspx.cs` | 10 | 0 | 0 | 10 | 100% | 2 | 0 |
| `WebGoat_Content_Challenge3.aspx.designer.cs` | 10 | 0 | 0 | 10 | 100% | 1 | 0 |
| `WebGoat_Content_ChangePwd.aspx.cs` | 10 | 0 | 10 | 0 | 100% | 2 | 0 |
| `WebGoat_Default.aspx.cs` | 10 | 0 | 10 | 0 | 100% | 0 | 5 |
| `WebGoat_Default.aspx.designer.cs` | 10 | 0 | 0 | 10 | 100% | 2 | 0 |
| `WebGoat_ForgotPassword.aspx.cs` | 10 | 0 | 6 | 4 | 60% | 0 | 4 |
| `WebGoat_ForgotPassword.aspx.designer.cs` | 10 | 0 | 0 | 10 | 100% | 0 | 0 |
| `WebGoat_Global.asax.cs` | 10 | 0 | 10 | 0 | 100% | 1 | 5 |
| `WebGoat_LoginPage.aspx.cs` | 10 | 0 | 10 | 0 | 100% | 0 | 6 |
| `WebGoat_LoginPage.aspx.designer.cs` | 10 | 0 | 0 | 10 | 100% | 2 | 0 |
| `WebGoat_ProxySetup.aspx.cs` | 10 | 0 | 0 | 10 | 100% | 0 | 4 |
| `WebGoat_ProxySetup.aspx.designer.cs` | 10 | 0 | 4 | 6 | 60% | 0 | 3 |
| `WebGoat_Web.config` | 10 | 0 | 10 | 0 | 100% | 1 | 9 |
| `WebGoat_WebGoat.NET.csproj` | 10 | 0 | 10 | 0 | 100% | 3 | 0 |
| `WebGoat_dbtest.aspx.cs` | 10 | 0 | 10 | 0 | 100% | 0 | 9 |
| `WebGoat_dbtest.aspx.designer.cs` | 10 | 0 | 6 | 4 | 60% | 1 | 4 |

---

## File: `WebGoat_AddNewUser.aspx.cs`

**Runs with this file:** 10  |  **Gate consistency:** 60%  |  **Verdict distribution:** FAIL: 6  NEEDS_HUMAN: 4

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Missing Input Validation for Username in User Registration | Medium | 40% (4/10) | 0.90 | model inconsistency |
| Weak Password Validation Allows Credential Compromise | Medium | 40% (4/10) | 0.85 | model inconsistency |
| Unrestricted Account Creation Enables Unauthorized Access | Medium | 40% (4/10) | 0.90 | model inconsistency |
| Username Input Validation Bypass Leading to Injection Vulnerability | High | 60% (6/10) | 0.90 | model inconsistency |
| Hardcoded Security Question Exposure | Medium | 60% (6/10) | 0.90 | model inconsistency |
| Authentication Bypass via Username Validation Bypass | High | 60% (6/10) | 0.85 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 10.1 | 10.2 | 5.2 | 29.8 | 0 | 0 |
| threat | 22.5 | 25.4 | 9.4 | 72.4 | 0 | 0 |
| hypotheses | 26.8 | 34.4 | 9.4 | 92.1 | 0 | 0 |
| evidence | 30.9 | 40.0 | 10.5 | 107.0 | 0 | 0 |
| fix | 37.4 | 46.5 | 12.0 | 125.4 | 0 | 0 |
| gate | 21.9 | 31.2 | 6.9 | 81.1 | 0 | 0 |
| pre_scan | 7.7 | 8.1 | 3.6 | 23.8 | 0 | 0 |

**Mean total elapsed per run:** 157s  |  Min: 57s  |  Max: 531s


---

## File: `WebGoat_AddNewUser.aspx.designer.cs`

**Runs with this file:** 10  |  **Gate consistency:** 60%  |  **Verdict distribution:** FAIL: 4  NEEDS_HUMAN: 6

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Missing Authorization Check on User Creation | High | 100% (10/10) | [0.72, 1.00] | 0.30 | — |

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Potential SQL Injection Vulnerability in User Creation | High | 40% (4/10) | 0.30 | borderline confidence |
| Hardcoded Credentials or Connection Strings | Medium | 40% (4/10) | 0.30 | borderline confidence |
| Potential Exposure of Security Question/Answer | Medium | 60% (6/10) | 0.30 | borderline confidence |
| Potential Input Sanitization Issues in User Fields | Medium | 60% (6/10) | 0.30 | borderline confidence |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.8 | 5.4 | 3.2 | 16.1 | 0 | 0 |
| threat | 17.9 | 18.9 | 7.9 | 54.0 | 0 | 0 |
| hypotheses | 18.9 | 22.2 | 8.2 | 61.1 | 0 | 0 |
| evidence | 21.0 | 23.5 | 9.6 | 65.7 | 0 | 0 |
| fix | 26.9 | 29.3 | 12.3 | 82.7 | 0 | 0 |
| gate | 20.5 | 25.0 | 6.9 | 67.8 | 0 | 0 |
| pre_scan | 8.9 | 12.0 | 3.1 | 31.6 | 0 | 0 |

**Mean total elapsed per run:** 120s  |  Min: 55s  |  Max: 379s


---

## File: `WebGoat_App_Code_ConfigFile.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Insecure Configuration - No Input Validation or Sanitization in Config File Parser | Medium | 100% (10/10) | [0.72, 1.00] | 0.75 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 6.1 | 6.2 | 3.1 | 17.8 | 0 | 0 |
| threat | 10.9 | 10.7 | 5.8 | 31.4 | 0 | 0 |
| hypotheses | 10.9 | 12.4 | 4.9 | 34.5 | 0 | 0 |
| evidence | 18.2 | 20.9 | 8.2 | 58.0 | 0 | 0 |
| fix | 21.5 | 21.6 | 11.2 | 62.8 | 0 | 0 |
| gate | 15.2 | 20.0 | 5.7 | 53.2 | 0 | 0 |
| pre_scan | 7.0 | 7.0 | 3.7 | 20.4 | 0 | 0 |

**Mean total elapsed per run:** 90s  |  Min: 43s  |  Max: 278s


---

## File: `WebGoat_App_Code_CookieManager.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Missing Authentication Cookie Addition to HTTP Response | High | 100% (10/10) | [0.72, 1.00] | 0.95 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 7.8 | 7.1 | 4.4 | 21.3 | 0 | 0 |
| threat | 14.6 | 14.6 | 7.6 | 42.5 | 0 | 0 |
| hypotheses | 19.9 | 23.0 | 8.9 | 63.8 | 0 | 0 |
| evidence | 19.8 | 22.1 | 9.2 | 61.9 | 0 | 0 |
| fix | 14.3 | 14.5 | 7.3 | 42.0 | 0 | 0 |
| gate | 17.7 | 22.1 | 7.1 | 59.6 | 0 | 0 |
| pre_scan | 7.3 | 9.2 | 2.9 | 24.8 | 0 | 0 |

**Mean total elapsed per run:** 101s  |  Min: 47s  |  Max: 316s


---

## File: `WebGoat_App_Code_CustomerLoginData.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** PASS: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Insecure Direct Object Reference in CustomerLoginData | Medium | 100% (10/10) | [0.72, 1.00] | 0.90 | — |
| Potential Injection Vulnerability via Message Property Setter | Medium | 100% (10/10) | [0.72, 1.00] | 0.90 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.5 | 5.0 | 3.1 | 15.1 | 0 | 0 |
| threat | 15.8 | 16.0 | 8.1 | 46.3 | 0 | 0 |
| hypotheses | 16.2 | 19.1 | 7.1 | 52.7 | 0 | 0 |
| evidence | 16.2 | 17.8 | 7.6 | 50.0 | 0 | 0 |
| fix | 16.8 | 16.6 | 8.8 | 48.4 | 0 | 0 |
| gate | 11.7 | 15.6 | 4.3 | 41.3 | 0 | 0 |
| pre_scan | 11.9 | 15.4 | 4.5 | 41.2 | 0 | 0 |

**Mean total elapsed per run:** 94s  |  Min: 44s  |  Max: 295s


---

## File: `WebGoat_App_Code_DB_DbConstants.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 10

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 6.2 | 5.8 | 3.4 | 17.3 | 0 | 0 |
| threat | 8.4 | 8.1 | 4.5 | 23.9 | 0 | 0 |
| hypotheses | 7.2 | 8.2 | 3.3 | 22.8 | 0 | 0 |
| evidence | 7.8 | 8.3 | 3.8 | 23.6 | 0 | 0 |
| fix | 2.9 | 3.0 | 1.5 | 8.6 | 0 | 0 |
| gate | 9.4 | 10.0 | 4.6 | 28.5 | 0 | 0 |
| pre_scan | 4.6 | 6.1 | 1.7 | 16.2 | 0 | 0 |

**Mean total elapsed per run:** 46s  |  Min: 23s  |  Max: 141s


---

## File: `WebGoat_App_Code_DB_DbProviderFactory.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** PASS: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Potential Information Disclosure via Logging | Medium | 100% (10/10) | [0.72, 1.00] | 0.90 | — |
| Infrastructure Enumeration via Logging of Database Type | Medium | 100% (10/10) | [0.72, 1.00] | 0.90 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 6.1 | 5.6 | 3.4 | 16.8 | 0 | 0 |
| threat | 14.6 | 14.1 | 7.8 | 41.5 | 0 | 0 |
| hypotheses | 19.5 | 22.7 | 8.7 | 62.6 | 0 | 0 |
| evidence | 22.8 | 28.3 | 9.3 | 76.7 | 0 | 0 |
| fix | 19.8 | 20.1 | 9.7 | 58.2 | 0 | 0 |
| gate | 18.8 | 19.2 | 9.1 | 55.6 | 0 | 0 |
| pre_scan | 5.1 | 6.1 | 2.2 | 16.7 | 0 | 0 |

**Mean total elapsed per run:** 107s  |  Min: 50s  |  Max: 328s


---

## File: `WebGoat_App_Code_DB_DummyDbProvider.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Potential Hardcoded Credentials or Configuration Values | Medium | 100% (10/10) | [0.72, 1.00] | 0.30 | — |
| Missing Authorization Checks in Database Methods | Medium | 100% (10/10) | [0.72, 1.00] | 0.30 | — |
| Potential SQL Injection Vulnerability in Database Methods | Medium | 100% (10/10) | [0.72, 1.00] | 0.30 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 6.5 | 6.6 | 3.4 | 19.0 | 0 | 0 |
| threat | 20.6 | 20.5 | 10.7 | 59.7 | 0 | 0 |
| hypotheses | 19.8 | 23.8 | 8.5 | 65.1 | 0 | 0 |
| evidence | 27.3 | 32.4 | 11.8 | 89.0 | 0 | 0 |
| fix | 26.5 | 28.3 | 12.9 | 80.4 | 0 | 0 |
| gate | 17.1 | 23.3 | 6.0 | 61.3 | 0 | 0 |
| pre_scan | 9.7 | 12.7 | 3.6 | 33.8 | 0 | 0 |

**Mean total elapsed per run:** 127s  |  Min: 57s  |  Max: 408s


---

## File: `WebGoat_App_Code_DB_IDbProvider.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Potential Authentication Bypass via Missing Authorization Checks | High | 100% (10/10) | [0.72, 1.00] | 0.30 | — |
| Potential SQL Injection Vulnerability in Database Methods | High | 100% (10/10) | [0.72, 1.00] | 0.30 | — |
| Hardcoded Credentials or Connection Strings in Database Interface | Medium | 100% (10/10) | [0.72, 1.00] | 0.30 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.6 | 5.2 | 3.1 | 15.5 | 0 | 0 |
| threat | 18.6 | 18.3 | 9.8 | 53.5 | 0 | 0 |
| hypotheses | 26.1 | 30.7 | 11.5 | 84.5 | 0 | 0 |
| evidence | 29.5 | 34.2 | 13.1 | 94.6 | 0 | 0 |
| fix | 24.0 | 26.2 | 11.5 | 74.0 | 0 | 0 |
| gate | 41.4 | 54.2 | 15.5 | 144.3 | 0 | 0 |
| pre_scan | 9.6 | 13.1 | 3.4 | 34.6 | 0 | 0 |

**Mean total elapsed per run:** 155s  |  Min: 68s  |  Max: 501s


---

## File: `WebGoat_App_Code_DB_MySqlDbProvider.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| SQL Injection via String Concatenation in MySqlDbProvider | Critical | 100% (10/10) | [0.72, 1.00] | 0.95 | — |
| Hardcoded Database Credentials in Configuration Files | High | 100% (10/10) | [0.72, 1.00] | 0.90 | — |
| Information Disclosure via Misconfigured Configuration Files | Medium | 100% (10/10) | [0.72, 1.00] | 0.90 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 15.9 | 20.3 | 6.2 | 54.5 | 0 | 0 |
| threat | 23.1 | 23.7 | 11.8 | 68.3 | 0 | 0 |
| hypotheses | 31.8 | 38.7 | 13.3 | 105.5 | 0 | 0 |
| evidence | 56.9 | 72.1 | 22.6 | 194.2 | 0 | 0 |
| fix | 36.8 | 44.8 | 15.5 | 122.1 | 0 | 0 |
| gate | 35.5 | 49.9 | 11.7 | 130.3 | 0 | 0 |
| pre_scan | 7.6 | 10.1 | 2.8 | 26.8 | 0 | 0 |

**Mean total elapsed per run:** 208s  |  Min: 84s  |  Max: 702s


---

## File: `WebGoat_App_Code_DB_SqliteDbProvider.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| SQL Injection in CustomerLogin Query | High | 100% (10/10) | [0.72, 1.00] | 0.95 | — |
| SQL Injection in GetCustomerEmail Method | High | 100% (10/10) | [0.72, 1.00] | 0.95 | — |
| SQL Injection in GetOrders Method | High | 100% (10/10) | [0.72, 1.00] | 0.95 | — |
| SQL Injection in GetProductDetails Method | High | 100% (10/10) | [0.72, 1.00] | 0.95 | — |
| SQL Injection in GetOrderDetails Method | High | 100% (10/10) | [0.72, 1.00] | 0.95 | — |
| SQL Injection in GetPayments Method | High | 100% (10/10) | [0.72, 1.00] | 0.95 | — |
| SQL Injection in GetProductsAndCategories Method | High | 100% (10/10) | [0.72, 1.00] | 0.95 | — |
| SQL Injection in GetEmailByName Method | High | 100% (10/10) | [0.72, 1.00] | 0.95 | — |
| SQL Injection in GetEmailByCustomerNumber Method | High | 100% (10/10) | [0.72, 1.00] | 0.95 | — |
| SQL Injection in GetCustomerEmails Method | High | 100% (10/10) | [0.72, 1.00] | 0.95 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 14.3 | 18.4 | 5.6 | 49.4 | 0 | 0 |
| threat | 69.5 | 88.5 | 27.4 | 237.9 | 0 | 0 |
| hypotheses | 86.3 | 125.2 | 26.8 | 324.3 | 0 | 0 |
| evidence | 116.1 | 167.7 | 36.5 | 434.9 | 0 | 0 |
| fix | 101.5 | 137.3 | 36.2 | 362.7 | 0 | 0 |
| gate | 83.5 | 133.3 | 20.1 | 336.7 | 0 | 0 |
| pre_scan | 64.8 | 92.6 | 20.7 | 241.0 | 0 | 0 |

**Mean total elapsed per run:** 536s  |  Min: 174s  |  Max: 1987s


---

## File: `WebGoat_App_Code_Encoder.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Use of Weak Encryption Algorithm (RijndaelManaged with Default Settings) | High | 100% (10/10) | [0.72, 1.00] | 0.90 | — |
| Hardcoded Salt in Encryption Implementation | Medium | 100% (10/10) | [0.72, 1.00] | 0.90 | — |
| Potential Insecure Direct Object Reference in Forms Authentication Ticket Handling | Medium | 100% (10/10) | [0.72, 1.00] | 0.80 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 11.1 | 13.2 | 4.8 | 36.2 | 0 | 0 |
| threat | 20.4 | 21.9 | 9.9 | 62.2 | 0 | 0 |
| hypotheses | 24.7 | 30.3 | 10.2 | 82.3 | 0 | 0 |
| evidence | 38.8 | 49.7 | 15.1 | 133.4 | 0 | 0 |
| fix | 36.8 | 41.3 | 17.0 | 115.4 | 0 | 0 |
| gate | 25.1 | 35.9 | 8.1 | 93.3 | 0 | 0 |
| pre_scan | 21.9 | 29.8 | 7.7 | 78.5 | 0 | 0 |

**Mean total elapsed per run:** 179s  |  Min: 73s  |  Max: 601s


---

## File: `WebGoat_App_Code_Settings.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Environment Variable Exposure in Logs | Medium | 100% (10/10) | [0.72, 1.00] | 0.90 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 7.2 | 7.1 | 3.8 | 20.7 | 0 | 0 |
| threat | 18.7 | 18.7 | 9.8 | 54.3 | 0 | 0 |
| hypotheses | 18.5 | 21.9 | 8.0 | 60.3 | 0 | 0 |
| evidence | 20.6 | 24.1 | 9.2 | 66.5 | 0 | 0 |
| fix | 11.9 | 12.1 | 6.1 | 35.0 | 0 | 0 |
| gate | 12.1 | 15.3 | 4.8 | 41.3 | 0 | 0 |
| pre_scan | 6.5 | 6.5 | 3.3 | 18.9 | 0 | 0 |

**Mean total elapsed per run:** 96s  |  Min: 45s  |  Max: 297s


---

## File: `WebGoat_App_Code_Util.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| OS Command Injection via ProcessStartInfo | High | 100% (10/10) | [0.72, 1.00] | 0.95 | — |
| Command Line Injection via File Input | High | 100% (10/10) | [0.72, 1.00] | 0.90 | — |
| Sensitive Data Exposure via Logging | Medium | 100% (10/10) | [0.72, 1.00] | 0.85 | — |
| Chained Command Injection Attack | High | 100% (10/10) | [0.72, 1.00] | 0.80 | — |
| Sensitive Data Exposure Through Process Output Logs | Medium | 100% (10/10) | [0.72, 1.00] | 0.85 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 7.4 | 7.3 | 3.9 | 21.4 | 0 | 0 |
| threat | 20.3 | 21.1 | 10.2 | 60.4 | 0 | 0 |
| hypotheses | 26.4 | 31.9 | 11.2 | 87.1 | 0 | 0 |
| evidence | 44.8 | 54.9 | 18.7 | 149.3 | 0 | 0 |
| fix | 66.0 | 80.5 | 27.6 | 219.4 | 0 | 0 |
| gate | 36.2 | 53.8 | 10.6 | 138.6 | 0 | 0 |
| pre_scan | 12.0 | 14.8 | 4.9 | 40.2 | 0 | 0 |

**Mean total elapsed per run:** 213s  |  Min: 87s  |  Max: 716s


---

## File: `WebGoat_App_Code_VeryWeakRandom.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Use of Very Weak Random Number Generator | High | 100% (10/10) | [0.72, 1.00] | 0.95 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.8 | 5.2 | 3.3 | 15.8 | 0 | 0 |
| threat | 19.3 | 19.1 | 10.2 | 55.8 | 0 | 0 |
| hypotheses | 16.9 | 20.1 | 7.3 | 55.2 | 0 | 0 |
| evidence | 20.0 | 21.5 | 9.6 | 61.0 | 0 | 0 |
| fix | 17.9 | 18.6 | 9.0 | 53.4 | 0 | 0 |
| gate | 20.0 | 25.5 | 7.9 | 68.5 | 0 | 0 |
| pre_scan | 11.1 | 16.4 | 3.3 | 42.3 | 0 | 0 |

**Mean total elapsed per run:** 111s  |  Min: 51s  |  Max: 352s


---

## File: `WebGoat_App_Code_WeakMessageDigest.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Use of Weak Cryptographic Algorithm | High | 100% (10/10) | [0.72, 1.00] | 0.95 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 6.2 | 5.9 | 3.3 | 17.5 | 0 | 0 |
| threat | 14.4 | 14.1 | 7.6 | 41.3 | 0 | 0 |
| hypotheses | 12.6 | 14.7 | 5.6 | 40.6 | 0 | 0 |
| evidence | 17.1 | 18.9 | 8.1 | 53.1 | 0 | 0 |
| fix | 13.8 | 13.7 | 7.2 | 40.0 | 0 | 0 |
| gate | 13.0 | 16.5 | 5.2 | 44.3 | 0 | 0 |
| pre_scan | 8.9 | 11.7 | 3.3 | 31.2 | 0 | 0 |

**Mean total elapsed per run:** 86s  |  Min: 40s  |  Max: 268s


---

## File: `WebGoat_App_Code_WeakRandom.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Use of Weak Random Number Generator | High | 100% (10/10) | [0.72, 1.00] | 0.95 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.8 | 5.3 | 3.2 | 15.9 | 0 | 0 |
| threat | 16.3 | 15.9 | 8.7 | 46.7 | 0 | 0 |
| hypotheses | 19.2 | 22.3 | 8.6 | 61.6 | 0 | 0 |
| evidence | 20.8 | 23.0 | 9.8 | 64.6 | 0 | 0 |
| fix | 11.8 | 12.3 | 5.9 | 35.2 | 0 | 0 |
| gate | 17.5 | 21.6 | 7.2 | 58.5 | 0 | 0 |
| pre_scan | 7.5 | 9.7 | 2.8 | 26.0 | 0 | 0 |

**Mean total elapsed per run:** 99s  |  Min: 46s  |  Max: 308s


---

## File: `WebGoat_App_Data_XmlInjectionUsers.xml`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| XML Injection Vulnerability | High | 100% (10/10) | [0.72, 1.00] | 0.90 | — |
| XML Injection via User Input | High | 100% (10/10) | [0.72, 1.00] | 0.90 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.2 | 4.7 | 3.0 | 14.2 | 0 | 0 |
| threat | 15.5 | 15.1 | 8.2 | 44.4 | 0 | 0 |
| hypotheses | 15.5 | 17.9 | 6.9 | 49.6 | 0 | 0 |
| evidence | 16.2 | 17.2 | 8.0 | 48.9 | 0 | 0 |
| fix | 14.4 | 14.4 | 7.5 | 41.9 | 0 | 0 |
| gate | 17.7 | 22.0 | 7.2 | 59.5 | 0 | 0 |
| pre_scan | 5.8 | 5.1 | 3.3 | 15.6 | 0 | 0 |

**Mean total elapsed per run:** 90s  |  Min: 44s  |  Max: 274s


---

## File: `WebGoat_ChangePassword.aspx.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 10

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Missing Authorization Check on Password Change Functionality | High | 40% (4/10) | 0.90 | model inconsistency |
| Potential Exposure of Sensitive User Data | Medium | 40% (4/10) | 0.30 | borderline confidence |
| Potential Missing Authorization Check | High | 60% (6/10) | 0.90 | model inconsistency |
| Possible Sensitive Data Exposure | Medium | 60% (6/10) | 0.30 | borderline confidence |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 7.7 | 6.7 | 4.5 | 20.4 | 0 | 0 |
| threat | 18.4 | 17.9 | 9.4 | 52.6 | 0 | 0 |
| hypotheses | 24.1 | 29.1 | 9.6 | 79.5 | 0 | 0 |
| evidence | 23.9 | 26.2 | 11.2 | 73.8 | 0 | 0 |
| fix | 10.9 | 11.5 | 5.1 | 32.8 | 0 | 0 |
| gate | 19.7 | 25.2 | 7.0 | 67.6 | 0 | 0 |
| pre_scan | 6.4 | 8.4 | 2.3 | 22.4 | 0 | 0 |

**Mean total elapsed per run:** 111s  |  Min: 51s  |  Max: 349s


---

## File: `WebGoat_ChangePassword.aspx.designer.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 10

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Missing Authorization Check on Password Change | High | 40% (4/10) | 0.30 | borderline confidence |
| Potential Exposure of Password Change Functionality | Medium | 40% (4/10) | 0.30 | borderline confidence |
| Missing Authorization Check on Password Change Functionality | High | 60% (6/10) | 0.30 | borderline confidence |
| Potential Exposure of Password Change UI Elements | Medium | 60% (6/10) | 0.30 | borderline confidence |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.5 | 5.1 | 3.0 | 15.3 | 0 | 0 |
| threat | 14.8 | 13.2 | 7.6 | 40.0 | 0 | 0 |
| hypotheses | 21.7 | 24.8 | 9.6 | 69.0 | 0 | 0 |
| evidence | 23.8 | 26.7 | 10.9 | 74.5 | 0 | 0 |
| fix | 21.5 | 23.0 | 10.2 | 65.3 | 0 | 0 |
| gate | 22.0 | 27.4 | 8.2 | 74.1 | 0 | 0 |
| pre_scan | 6.2 | 8.1 | 2.3 | 21.6 | 0 | 0 |

**Mean total elapsed per run:** 115s  |  Min: 53s  |  Max: 360s


---

## File: `WebGoat_Code_DatabaseUtilities.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| SQL Injection in GetEmailByUserID Method | High | 100% (10/10) | [0.72, 1.00] | 0.95 | — |
| SQL Injection in GetMailingListInfoByEmailAddress Method | High | 100% (10/10) | [0.72, 1.00] | 0.95 | — |
| SQL Injection in AddToMailingList Method | High | 100% (10/10) | [0.72, 1.00] | 0.95 | — |
| SQL Injection in AddNewPosting Method | High | 100% (10/10) | [0.72, 1.00] | 0.95 | — |
| SQL Injection in GetPostingByID Method | High | 100% (10/10) | [0.72, 1.00] | 0.95 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 10.8 | 13.4 | 4.5 | 36.2 | 0 | 0 |
| threat | 31.4 | 35.8 | 14.4 | 99.6 | 0 | 0 |
| hypotheses | 38.7 | 50.6 | 14.6 | 134.9 | 0 | 0 |
| evidence | 66.7 | 91.2 | 23.3 | 240.1 | 0 | 0 |
| fix | 68.8 | 85.8 | 27.9 | 232.0 | 0 | 0 |
| gate | 53.3 | 80.6 | 14.9 | 206.5 | 0 | 0 |
| pre_scan | 29.8 | 38.4 | 11.5 | 102.8 | 0 | 0 |

**Mean total elapsed per run:** 299s  |  Min: 111s  |  Max: 1052s


---

## File: `WebGoat_Code_IOHelper.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Insecure Direct Object Reference (IDOR) in file reading function | High | 100% (10/10) | [0.72, 1.00] | 0.95 | — |
| Potential Information Disclosure via Path Traversal | High | 100% (10/10) | [0.72, 1.00] | 0.90 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.6 | 4.9 | 3.2 | 15.0 | 0 | 0 |
| threat | 16.4 | 16.1 | 8.7 | 47.1 | 0 | 0 |
| hypotheses | 15.4 | 18.1 | 6.8 | 49.9 | 0 | 0 |
| evidence | 18.9 | 20.0 | 9.2 | 57.0 | 0 | 0 |
| fix | 24.6 | 25.7 | 12.4 | 73.6 | 0 | 0 |
| gate | 19.5 | 25.6 | 7.3 | 68.2 | 0 | 0 |
| pre_scan | 5.6 | 5.0 | 3.2 | 15.2 | 0 | 0 |

**Mean total elapsed per run:** 106s  |  Min: 51s  |  Max: 326s


---

## File: `WebGoat_Code_SQLiteMembershipProvider.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Use of Weak Hashing Algorithm for Password Storage | High | 100% (10/10) | [0.72, 1.00] | 0.95 | — |
| SQL Injection Vulnerability in Application ID Retrieval | High | 100% (10/10) | [0.72, 1.00] | 0.90 | — |
| Missing Authorization Check on User Data Access | Medium | 100% (10/10) | [0.72, 1.00] | 0.85 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 16.7 | 22.3 | 6.0 | 59.0 | 0 | 0 |
| threat | 20.4 | 21.9 | 9.9 | 62.0 | 0 | 0 |
| hypotheses | 23.5 | 29.0 | 9.7 | 78.6 | 0 | 0 |
| evidence | 39.0 | 50.4 | 15.1 | 134.9 | 0 | 0 |
| fix | 28.9 | 32.1 | 13.6 | 90.1 | 0 | 0 |
| gate | 27.8 | 38.6 | 9.5 | 101.0 | 0 | 0 |
| pre_scan | 25.7 | 36.2 | 8.5 | 94.5 | 0 | 0 |

**Mean total elapsed per run:** 182s  |  Min: 72s  |  Max: 620s


---

## File: `WebGoat_Code_SQLiteProfileProvider.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Use of BinaryFormatter in Profile Property Serialization | High | 100% (10/10) | [0.72, 1.00] | 0.95 | — |
| Potential SQL Injection via String Concatenation | High | 100% (10/10) | [0.72, 1.00] | 0.90 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 17.3 | 23.0 | 6.4 | 61.0 | 0 | 0 |
| threat | 20.6 | 21.6 | 10.1 | 62.1 | 0 | 0 |
| hypotheses | 27.1 | 33.1 | 11.3 | 90.0 | 0 | 0 |
| evidence | 34.5 | 44.2 | 13.4 | 118.6 | 0 | 0 |
| fix | 19.1 | 20.4 | 9.2 | 58.0 | 0 | 0 |
| gate | 19.9 | 26.4 | 7.3 | 70.2 | 0 | 0 |
| pre_scan | 18.2 | 23.8 | 6.8 | 63.5 | 0 | 0 |

**Mean total elapsed per run:** 157s  |  Min: 65s  |  Max: 523s


---

## File: `WebGoat_Code_SQLiteRoleProvider.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Missing Authorization Check in Role Management Methods | High | 100% (10/10) | [0.72, 1.00] | 0.90 | — |
| Potential SQL Injection Vulnerability in FindUsersInRole | High | 100% (10/10) | [0.72, 1.00] | 0.90 | — |
| Insecure Direct Object Reference in Role Management | High | 100% (10/10) | [0.72, 1.00] | 0.90 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 16.9 | 22.5 | 6.2 | 59.6 | 0 | 0 |
| threat | 29.6 | 32.2 | 14.1 | 90.8 | 0 | 0 |
| hypotheses | 34.2 | 43.7 | 13.4 | 117.5 | 0 | 0 |
| evidence | 70.5 | 92.8 | 26.2 | 247.0 | 0 | 0 |
| fix | 65.2 | 82.8 | 25.7 | 222.8 | 0 | 0 |
| gate | 43.6 | 65.8 | 12.3 | 168.7 | 0 | 0 |
| pre_scan | 22.3 | 29.1 | 8.4 | 77.6 | 0 | 0 |

**Mean total elapsed per run:** 282s  |  Min: 106s  |  Max: 984s


---

## File: `WebGoat_Configuration_Default.config`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 10

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 4.8 | 4.3 | 2.8 | 13.0 | 0 | 0 |
| threat | 8.2 | 7.8 | 4.5 | 23.2 | 0 | 0 |
| hypotheses | 7.2 | 8.1 | 3.3 | 22.6 | 0 | 0 |
| evidence | 6.0 | 6.1 | 3.1 | 17.7 | 0 | 0 |
| fix | 8.1 | 7.1 | 4.7 | 21.8 | 0 | 0 |
| gate | 8.8 | 10.2 | 3.9 | 28.2 | 0 | 0 |
| pre_scan | 3.4 | 3.2 | 1.9 | 9.5 | 0 | 0 |

**Mean total elapsed per run:** 47s  |  Min: 24s  |  Max: 136s


---

## File: `WebGoat_Content_About.aspx.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Potential Missing Authorization Check | Medium | 100% (10/10) | [0.72, 1.00] | 0.90 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 6.6 | 5.6 | 3.9 | 17.2 | 0 | 0 |
| threat | 14.1 | 13.9 | 7.4 | 40.6 | 0 | 0 |
| hypotheses | 13.4 | 16.1 | 5.8 | 44.0 | 0 | 0 |
| evidence | 11.7 | 14.3 | 4.9 | 38.9 | 0 | 0 |
| fix | 11.3 | 10.4 | 6.3 | 31.2 | 0 | 0 |
| gate | 13.0 | 15.4 | 5.7 | 42.4 | 0 | 0 |
| pre_scan | 4.6 | 5.1 | 2.1 | 14.3 | 0 | 0 |

**Mean total elapsed per run:** 75s  |  Min: 36s  |  Max: 229s


---

## File: `WebGoat_Content_About.aspx.designer.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 10

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.4 | 4.8 | 3.1 | 14.7 | 0 | 0 |
| threat | 8.5 | 8.1 | 4.6 | 24.0 | 0 | 0 |
| hypotheses | 8.7 | 9.6 | 4.1 | 27.0 | 0 | 0 |
| evidence | 7.1 | 7.6 | 3.5 | 21.5 | 0 | 0 |
| fix | 8.8 | 7.7 | 5.1 | 23.5 | 0 | 0 |
| gate | 9.7 | 11.2 | 4.3 | 31.0 | 0 | 0 |
| pre_scan | 4.0 | 5.0 | 1.6 | 13.5 | 0 | 0 |

**Mean total elapsed per run:** 52s  |  Min: 26s  |  Max: 155s


---

## File: `WebGoat_Content_BasicAuth.aspx.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Potential Missing Authorization Check | Medium | 100% (10/10) | [0.72, 1.00] | 0.90 | — |
| Missing Authentication Logic | High | 100% (10/10) | [0.72, 1.00] | 0.90 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 6.1 | 5.4 | 3.5 | 16.5 | 0 | 0 |
| threat | 13.1 | 12.8 | 7.0 | 37.6 | 0 | 0 |
| hypotheses | 16.4 | 18.9 | 7.4 | 52.5 | 0 | 0 |
| evidence | 17.0 | 20.8 | 7.0 | 56.6 | 0 | 0 |
| fix | 17.1 | 16.7 | 9.0 | 48.9 | 0 | 0 |
| gate | 15.0 | 21.2 | 4.9 | 55.2 | 0 | 0 |
| pre_scan | 5.0 | 5.8 | 2.2 | 16.0 | 0 | 0 |

**Mean total elapsed per run:** 90s  |  Min: 41s  |  Max: 283s


---

## File: `WebGoat_Content_BasicAuth.aspx.designer.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 10

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.2 | 4.7 | 3.0 | 14.2 | 0 | 0 |
| threat | 17.8 | 17.3 | 9.5 | 50.9 | 0 | 0 |
| hypotheses | 18.7 | 21.9 | 8.3 | 60.4 | 0 | 0 |
| evidence | 17.0 | 18.4 | 8.2 | 52.1 | 0 | 0 |
| fix | 3.8 | 4.4 | 1.7 | 12.2 | 0 | 0 |
| gate | 15.4 | 17.7 | 7.0 | 49.2 | 0 | 0 |
| pre_scan | 6.6 | 8.0 | 2.8 | 21.8 | 0 | 0 |

**Mean total elapsed per run:** 85s  |  Min: 40s  |  Max: 261s


---

## File: `WebGoat_Content_Challenge1.aspx.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Potential Missing Authorization Check | Medium | 100% (10/10) | [0.72, 1.00] | 0.90 | — |
| Verbose Error Handling | Low | 100% (10/10) | [0.72, 1.00] | 0.85 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 7.3 | 6.4 | 4.2 | 19.6 | 0 | 0 |
| threat | 14.3 | 14.2 | 7.5 | 41.5 | 0 | 0 |
| hypotheses | 18.3 | 21.1 | 8.2 | 58.6 | 0 | 0 |
| evidence | 14.2 | 15.3 | 6.9 | 43.3 | 0 | 0 |
| fix | 17.8 | 17.4 | 9.5 | 50.9 | 0 | 0 |
| gate | 14.7 | 18.6 | 5.8 | 50.1 | 0 | 0 |
| pre_scan | 5.6 | 6.9 | 2.3 | 18.7 | 0 | 0 |

**Mean total elapsed per run:** 92s  |  Min: 45s  |  Max: 283s


---

## File: `WebGoat_Content_Challenge1.aspx.designer.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Potential Missing Authorization Check | Medium | 100% (10/10) | [0.72, 1.00] | 0.30 | — |
| Debug/Verbose Error Handling Possible | Low | 100% (10/10) | [0.72, 1.00] | 0.30 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.7 | 5.1 | 3.3 | 15.5 | 0 | 0 |
| threat | 14.4 | 13.9 | 7.7 | 41.1 | 0 | 0 |
| hypotheses | 13.6 | 15.7 | 6.1 | 43.5 | 0 | 0 |
| evidence | 12.4 | 13.0 | 6.1 | 37.3 | 0 | 0 |
| fix | 18.0 | 17.4 | 9.7 | 51.2 | 0 | 0 |
| gate | 13.7 | 17.2 | 5.4 | 46.4 | 0 | 0 |
| pre_scan | 5.6 | 7.2 | 2.2 | 19.3 | 0 | 0 |

**Mean total elapsed per run:** 83s  |  Min: 41s  |  Max: 254s


---

## File: `WebGoat_Content_Challenge2.aspx.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Potential Missing Authorization Check | Medium | 100% (10/10) | [0.72, 1.00] | 0.90 | — |
| Verbose Error Handling | Low | 100% (10/10) | [0.72, 1.00] | 0.85 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 7.2 | 6.3 | 4.1 | 19.2 | 0 | 0 |
| threat | 13.6 | 13.6 | 7.2 | 39.5 | 0 | 0 |
| hypotheses | 17.8 | 20.4 | 8.1 | 56.6 | 0 | 0 |
| evidence | 14.2 | 15.1 | 6.9 | 43.0 | 0 | 0 |
| fix | 18.5 | 18.1 | 9.8 | 53.1 | 0 | 0 |
| gate | 25.8 | 31.8 | 10.7 | 86.3 | 0 | 0 |
| pre_scan | 5.6 | 7.0 | 2.2 | 19.0 | 0 | 0 |

**Mean total elapsed per run:** 103s  |  Min: 49s  |  Max: 317s


---

## File: `WebGoat_Content_Challenge2.aspx.designer.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Potential Missing Authorization Check | Medium | 100% (10/10) | [0.72, 1.00] | 0.30 | — |
| Possible Debug/Verbose Logging Enabled | Low | 100% (10/10) | [0.72, 1.00] | 0.40 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.4 | 4.9 | 3.1 | 14.9 | 0 | 0 |
| threat | 12.6 | 12.1 | 6.8 | 35.7 | 0 | 0 |
| hypotheses | 12.2 | 13.8 | 5.6 | 38.4 | 0 | 0 |
| evidence | 12.2 | 12.8 | 6.1 | 36.6 | 0 | 0 |
| fix | 14.5 | 14.0 | 7.8 | 41.1 | 0 | 0 |
| gate | 14.9 | 20.3 | 5.2 | 53.5 | 0 | 0 |
| pre_scan | 5.9 | 7.8 | 2.2 | 20.7 | 0 | 0 |

**Mean total elapsed per run:** 78s  |  Min: 37s  |  Max: 241s


---

## File: `WebGoat_Content_Challenge3.aspx.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Potential Missing Authorization Check | Medium | 100% (10/10) | [0.72, 1.00] | 0.90 | — |
| Verbose Error Handling | Low | 100% (10/10) | [0.72, 1.00] | 0.85 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 7.3 | 6.3 | 4.2 | 19.3 | 0 | 0 |
| threat | 15.3 | 15.2 | 8.0 | 44.4 | 0 | 0 |
| hypotheses | 20.6 | 23.8 | 9.2 | 65.9 | 0 | 0 |
| evidence | 17.5 | 18.9 | 8.5 | 53.5 | 0 | 0 |
| fix | 19.4 | 19.6 | 10.0 | 56.7 | 0 | 0 |
| gate | 14.3 | 18.5 | 5.5 | 49.4 | 0 | 0 |
| pre_scan | 8.7 | 6.5 | 4.1 | 20.9 | 0 | 0 |

**Mean total elapsed per run:** 103s  |  Min: 50s  |  Max: 310s


---

## File: `WebGoat_Content_Challenge3.aspx.designer.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Possible Debug/Verbose Logging Enabled | Low | 100% (10/10) | [0.72, 1.00] | 0.90 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.7 | 5.1 | 3.2 | 15.4 | 0 | 0 |
| threat | 12.8 | 12.3 | 6.8 | 36.2 | 0 | 0 |
| hypotheses | 12.1 | 13.8 | 5.5 | 38.5 | 0 | 0 |
| evidence | 12.0 | 12.5 | 6.0 | 35.8 | 0 | 0 |
| fix | 8.6 | 8.4 | 4.6 | 24.6 | 0 | 0 |
| gate | 13.2 | 15.5 | 5.8 | 42.8 | 0 | 0 |
| pre_scan | 5.7 | 7.3 | 2.2 | 19.5 | 0 | 0 |

**Mean total elapsed per run:** 70s  |  Min: 34s  |  Max: 213s


---

## File: `WebGoat_Content_ChangePwd.aspx.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Potential Authentication Bypass in Password Change Page | Critical | 100% (10/10) | [0.72, 1.00] | 0.90 | — |
| Missing Authorization Check in Password Change Functionality | High | 100% (10/10) | [0.72, 1.00] | 0.90 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 7.0 | 6.1 | 4.0 | 18.7 | 0 | 0 |
| threat | 25.3 | 25.5 | 13.0 | 73.8 | 0 | 0 |
| hypotheses | 22.3 | 27.3 | 9.2 | 74.3 | 0 | 0 |
| evidence | 21.6 | 23.2 | 10.5 | 65.8 | 0 | 0 |
| fix | 23.3 | 24.6 | 11.6 | 70.2 | 0 | 0 |
| gate | 17.2 | 22.8 | 6.4 | 60.5 | 0 | 0 |
| pre_scan | 5.4 | 6.6 | 2.2 | 18.0 | 0 | 0 |

**Mean total elapsed per run:** 122s  |  Min: 57s  |  Max: 381s


---

## File: `WebGoat_Default.aspx.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 10

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Potential Information Disclosure via Server Name | Medium | 40% (4/10) | 0.90 | model inconsistency |
| Session Identifier Exposure in ViewState | Medium | 40% (4/10) | 0.90 | model inconsistency |
| Session Hijacking via ViewState Session ID Storage | High | 40% (4/10) | 0.90 | model inconsistency |
| Information Exposure Through Server Name in Cookie | Medium | 60% (6/10) | 0.85 | model inconsistency |
| Missing Authorization Check on Database Rebuild Functionality | High | 60% (6/10) | 0.75 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 8.0 | 7.3 | 4.5 | 21.9 | 0 | 0 |
| threat | 20.6 | 19.9 | 9.9 | 58.5 | 0 | 0 |
| hypotheses | 23.2 | 26.9 | 9.6 | 74.4 | 0 | 0 |
| evidence | 23.3 | 24.3 | 9.9 | 69.5 | 0 | 0 |
| fix | 17.5 | 17.1 | 8.5 | 50.1 | 0 | 0 |
| gate | 16.6 | 20.5 | 6.2 | 55.7 | 0 | 0 |
| pre_scan | 14.1 | 19.8 | 4.5 | 51.9 | 0 | 0 |

**Mean total elapsed per run:** 123s  |  Min: 53s  |  Max: 382s


---

## File: `WebGoat_Default.aspx.designer.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Potential Missing Authorization Check | High | 100% (10/10) | [0.72, 1.00] | 0.30 | — |
| Potential Sensitive Data Exposure | Medium | 100% (10/10) | [0.72, 1.00] | 0.30 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.3 | 4.8 | 3.0 | 14.5 | 0 | 0 |
| threat | 14.6 | 14.1 | 7.8 | 41.5 | 0 | 0 |
| hypotheses | 13.5 | 15.3 | 6.0 | 42.5 | 0 | 0 |
| evidence | 14.1 | 14.6 | 7.0 | 41.8 | 0 | 0 |
| fix | 19.5 | 19.5 | 9.9 | 56.8 | 0 | 0 |
| gate | 17.1 | 21.5 | 6.8 | 57.9 | 0 | 0 |
| pre_scan | 6.1 | 8.0 | 2.2 | 21.4 | 0 | 0 |

**Mean total elapsed per run:** 90s  |  Min: 43s  |  Max: 276s


---

## File: `WebGoat_ForgotPassword.aspx.cs`

**Runs with this file:** 10  |  **Gate consistency:** 60%  |  **Verdict distribution:** FAIL: 6  NEEDS_HUMAN: 4

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Missing Authorization Check in Password Reset Functionality | High | 40% (4/10) | 0.30 | borderline confidence |
| Potential Information Disclosure in Password Reset Flow | Medium | 40% (4/10) | 0.30 | borderline confidence |
| Potential Missing Authorization Check in Password Reset Functionality | High | 60% (6/10) | 0.90 | model inconsistency |
| Possible Information Disclosure in Password Reset Flow | Medium | 60% (6/10) | 0.90 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 6.0 | 5.3 | 3.5 | 16.1 | 0 | 0 |
| threat | 15.1 | 14.7 | 8.0 | 43.1 | 0 | 0 |
| hypotheses | 21.8 | 26.0 | 8.6 | 71.3 | 0 | 0 |
| evidence | 20.2 | 20.8 | 9.5 | 59.8 | 0 | 0 |
| fix | 19.9 | 20.2 | 10.0 | 58.4 | 0 | 0 |
| gate | 17.8 | 20.4 | 6.2 | 56.4 | 0 | 0 |
| pre_scan | 5.8 | 7.4 | 2.2 | 19.9 | 0 | 0 |

**Mean total elapsed per run:** 107s  |  Min: 50s  |  Max: 325s


---

## File: `WebGoat_ForgotPassword.aspx.designer.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 10

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.5 | 5.0 | 3.1 | 15.0 | 0 | 0 |
| threat | 12.8 | 14.2 | 4.6 | 39.8 | 0 | 0 |
| hypotheses | 12.6 | 15.9 | 4.0 | 42.8 | 0 | 0 |
| evidence | 11.4 | 13.3 | 4.2 | 36.7 | 0 | 0 |
| fix | 4.9 | 3.4 | 1.5 | 10.1 | 0 | 0 |
| gate | 11.9 | 13.5 | 5.4 | 37.6 | 0 | 0 |
| pre_scan | 6.1 | 7.9 | 2.3 | 21.1 | 0 | 0 |

**Mean total elapsed per run:** 65s  |  Min: 29s  |  Max: 203s


---

## File: `WebGoat_Global.asax.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Potential Information Disclosure via Debug Mode | Medium | 100% (10/10) | [0.72, 1.00] | 0.80 | — |

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| X-XSS-Protection Header Set to Zero | Medium | 40% (4/10) | 0.90 | model inconsistency |
| Potential Insecure Role Handling in Forms Authentication | High | 40% (4/10) | 0.85 | model inconsistency |
| X-XSS-Protection Header Set to Disabled | High | 60% (6/10) | 0.90 | model inconsistency |
| Potential Insecure Role Assignment | High | 60% (6/10) | 0.85 | model inconsistency |
| Possible Weak Authentication Ticket Handling | Medium | 60% (6/10) | 0.80 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 15.5 | 14.7 | 8.5 | 43.5 | 0 | 0 |
| threat | 26.8 | 30.2 | 12.1 | 84.4 | 0 | 0 |
| hypotheses | 29.7 | 36.8 | 11.3 | 99.6 | 0 | 0 |
| evidence | 38.2 | 42.5 | 15.8 | 119.0 | 0 | 0 |
| fix | 40.3 | 47.0 | 17.5 | 129.9 | 0 | 0 |
| gate | 32.2 | 46.9 | 9.7 | 121.4 | 0 | 0 |
| pre_scan | 9.5 | 11.6 | 4.0 | 31.5 | 0 | 0 |

**Mean total elapsed per run:** 192s  |  Min: 81s  |  Max: 629s


---

## File: `WebGoat_LoginPage.aspx.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 10

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Authentication Bypass via Redirect | High | 40% (4/10) | 0.95 | model inconsistency |
| Missing Authentication Logic | High | 40% (4/10) | 0.90 | model inconsistency |
| Insecure Direct Object Reference | Medium | 40% (4/10) | 0.85 | model inconsistency |
| Bypassable Authentication Logic | High | 60% (6/10) | 0.90 | model inconsistency |
| Missing Authentication Implementation | High | 60% (6/10) | 0.90 | model inconsistency |
| Commented-Out Security Controls | Medium | 60% (6/10) | 0.90 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 9.8 | 8.8 | 5.6 | 26.7 | 0 | 0 |
| threat | 18.8 | 19.9 | 9.1 | 56.8 | 0 | 0 |
| hypotheses | 23.4 | 28.6 | 9.4 | 77.8 | 0 | 0 |
| evidence | 31.2 | 38.1 | 11.0 | 103.6 | 0 | 0 |
| fix | 42.1 | 54.1 | 12.2 | 144.9 | 0 | 0 |
| gate | 23.6 | 34.9 | 6.3 | 90.0 | 0 | 0 |
| pre_scan | 11.0 | 15.6 | 3.5 | 40.7 | 0 | 0 |

**Mean total elapsed per run:** 160s  |  Min: 57s  |  Max: 540s


---

## File: `WebGoat_LoginPage.aspx.designer.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Potential Missing Authentication Check on Admin Login Button | High | 100% (10/10) | [0.72, 1.00] | 0.30 | — |
| Missing Authorization Check for Admin Functionality | High | 100% (10/10) | [0.72, 1.00] | 0.30 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.5 | 5.0 | 3.1 | 15.0 | 0 | 0 |
| threat | 12.5 | 11.8 | 6.6 | 35.0 | 0 | 0 |
| hypotheses | 13.9 | 16.0 | 6.0 | 44.4 | 0 | 0 |
| evidence | 15.0 | 16.1 | 7.1 | 45.7 | 0 | 0 |
| fix | 20.5 | 20.6 | 10.5 | 59.8 | 0 | 0 |
| gate | 16.7 | 21.6 | 6.2 | 57.7 | 0 | 0 |
| pre_scan | 7.4 | 10.5 | 2.4 | 27.3 | 0 | 0 |

**Mean total elapsed per run:** 91s  |  Min: 42s  |  Max: 285s


---

## File: `WebGoat_ProxySetup.aspx.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 10

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Potential String Manipulation Vulnerability | Medium | 40% (4/10) | 0.90 | model inconsistency |
| Potential XSS Vulnerability via txtName.Text Input | Medium | 60% (6/10) | 0.90 | model inconsistency |
| Potential String Manipulation Vulnerability in txtName.Text | Medium | 60% (6/10) | 0.90 | model inconsistency |
| Misuse of String Reversal Functionality | Medium | 60% (6/10) | 0.90 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 7.8 | 7.0 | 4.5 | 21.1 | 0 | 0 |
| threat | 16.4 | 16.4 | 8.4 | 47.6 | 0 | 0 |
| hypotheses | 27.2 | 32.0 | 11.7 | 88.1 | 0 | 0 |
| evidence | 33.2 | 39.4 | 13.4 | 108.3 | 0 | 0 |
| fix | 30.3 | 40.1 | 7.3 | 106.4 | 0 | 0 |
| gate | 20.3 | 27.5 | 6.7 | 72.6 | 0 | 0 |
| pre_scan | 4.8 | 6.2 | 1.8 | 16.5 | 0 | 0 |

**Mean total elapsed per run:** 140s  |  Min: 55s  |  Max: 460s


---

## File: `WebGoat_ProxySetup.aspx.designer.cs`

**Runs with this file:** 10  |  **Gate consistency:** 60%  |  **Verdict distribution:** FAIL: 4  NEEDS_HUMAN: 6

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Potential Command Injection via TextBox Input | High | 40% (4/10) | 0.30 | borderline confidence |
| Missing Authorization Check on Sensitive Operation | High | 40% (4/10) | 0.30 | borderline confidence |
| Hardcoded Configuration Values in UI Controls | Medium | 40% (4/10) | 0.40 | borderline confidence |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.8 | 5.3 | 3.2 | 15.9 | 0 | 0 |
| threat | 17.6 | 17.4 | 9.3 | 50.7 | 0 | 0 |
| hypotheses | 18.9 | 22.7 | 7.7 | 62.1 | 0 | 0 |
| evidence | 15.2 | 15.3 | 6.7 | 44.4 | 0 | 0 |
| fix | 8.7 | 5.7 | 2.0 | 13.6 | 0 | 0 |
| gate | 17.2 | 18.6 | 7.8 | 52.6 | 0 | 0 |
| pre_scan | 8.6 | 11.8 | 3.0 | 31.0 | 0 | 0 |

**Mean total elapsed per run:** 92s  |  Min: 41s  |  Max: 269s


---

## File: `WebGoat_Web.config`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Debug Mode Enabled in Production Configuration | High | 100% (10/10) | [0.72, 1.00] | 0.90 | — |

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Hardcoded User Credentials in Clear Text | Critical | 40% (4/10) | 1.00 | model inconsistency |
| Insecure Session Cookie Configuration | High | 40% (4/10) | 0.90 | model inconsistency |
| Inconsistent Authorization Controls on Sensitive Resource | High | 40% (4/10) | 0.90 | model inconsistency |
| Verbose Logging Enabled in Production Environment | Medium | 40% (4/10) | 0.80 | model inconsistency |
| Header Injection Vulnerability Due to Disabled Header Checking | High | 40% (4/10) | 0.90 | model inconsistency |
| Hardcoded Credentials in Clear Text | Critical | 60% (6/10) | 0.90 | model inconsistency |
| Insecure Session Cookie Configuration | Medium | 60% (6/10) | 0.90 | model inconsistency |
| Inconsistent Authorization Policy for VerbTamperingAttack.aspx | High | 60% (6/10) | 0.90 | model inconsistency |
| Verbose Logging Enabled in Production | Medium | 60% (6/10) | 0.90 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 16.3 | 20.0 | 6.7 | 54.4 | 0 | 0 |
| threat | 37.2 | 41.9 | 16.5 | 116.9 | 0 | 0 |
| hypotheses | 35.7 | 47.3 | 13.0 | 125.6 | 0 | 0 |
| evidence | 46.1 | 60.0 | 16.9 | 160.2 | 0 | 0 |
| fix | 41.7 | 47.4 | 18.8 | 132.0 | 0 | 0 |
| gate | 31.1 | 42.7 | 9.3 | 112.2 | 0 | 0 |
| pre_scan | 27.6 | 36.1 | 10.4 | 96.3 | 0 | 0 |

**Mean total elapsed per run:** 236s  |  Min: 92s  |  Max: 798s


---

## File: `WebGoat_WebGoat.NET.csproj`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 10

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Debug Mode Enabled in MSBuild Configuration | High | 100% (10/10) | [0.72, 1.00] | 0.95 | — |
| Unsafe Code Blocks Enabled | Medium | 100% (10/10) | [0.72, 1.00] | 0.85 | — |
| Hardcoded Environment Variables for Mono Logging | Medium | 100% (10/10) | [0.72, 1.00] | 0.75 | — |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 20.1 | 27.4 | 7.1 | 72.3 | 0 | 0 |
| threat | 27.0 | 29.6 | 12.8 | 83.3 | 0 | 0 |
| hypotheses | 26.4 | 33.7 | 10.4 | 90.5 | 0 | 0 |
| evidence | 35.4 | 45.9 | 13.5 | 122.7 | 0 | 0 |
| fix | 33.3 | 36.5 | 15.8 | 103.0 | 0 | 0 |
| gate | 28.9 | 40.3 | 9.8 | 105.6 | 0 | 0 |
| pre_scan | 24.3 | 32.6 | 8.8 | 86.2 | 0 | 0 |

**Mean total elapsed per run:** 195s  |  Min: 78s  |  Max: 664s


---

## File: `WebGoat_dbtest.aspx.cs`

**Runs with this file:** 10  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 10

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Missing Authentication for Sensitive Database Operations | High | 40% (4/10) | 0.90 | model inconsistency |
| Insecure Direct Object Reference in Configuration Access | Medium | 40% (4/10) | 0.90 | model inconsistency |
| Lack of Input Validation in Configuration Updates | Medium | 40% (4/10) | 0.90 | model inconsistency |
| Denial of Service via Malformed Configuration Inputs | Medium | 40% (4/10) | 0.90 | model inconsistency |
| Missing Authentication Check on Database Reconfiguration | High | 60% (6/10) | 0.95 | model inconsistency |
| Potential SQL Injection via Configuration File Updates | Medium | 60% (6/10) | 0.85 | model inconsistency |
| Insecure Direct Object Reference in Configuration Handling | Medium | 60% (6/10) | 0.90 | model inconsistency |
| Hardcoded Database Connection Strings in Configuration Files | High | 60% (6/10) | 0.90 | model inconsistency |
| Unrestricted Database Rebuild Access | High | 60% (6/10) | 0.95 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 10.5 | 11.0 | 5.3 | 31.4 | 0 | 0 |
| threat | 30.2 | 34.7 | 12.5 | 96.2 | 0 | 0 |
| hypotheses | 33.9 | 44.0 | 12.6 | 117.6 | 0 | 0 |
| evidence | 44.5 | 56.6 | 17.2 | 152.2 | 0 | 0 |
| fix | 45.8 | 53.4 | 20.2 | 147.5 | 0 | 0 |
| gate | 30.8 | 45.6 | 8.3 | 117.3 | 0 | 0 |
| pre_scan | 18.6 | 24.7 | 6.5 | 65.6 | 0 | 0 |

**Mean total elapsed per run:** 214s  |  Min: 84s  |  Max: 728s


---

## File: `WebGoat_dbtest.aspx.designer.cs`

**Runs with this file:** 10  |  **Gate consistency:** 60%  |  **Verdict distribution:** FAIL: 6  NEEDS_HUMAN: 4

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Hardcoded Database Credentials in UI Controls | High | 100% (10/10) | [0.72, 1.00] | 0.30 | — |

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Missing Authorization Check on Database Rebuild Functionality | High | 40% (4/10) | 0.30 | borderline confidence |
| Potential SQL Injection Vulnerability via User Input | High | 40% (4/10) | 0.30 | borderline confidence |
| Missing Authorization Check on Database Rebuild Functionality | Critical | 60% (6/10) | 0.30 | borderline confidence |
| Potential Exposure of Sensitive Data via UI Controls | Medium | 60% (6/10) | 0.30 | borderline confidence |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 8.5 | 10.0 | 3.8 | 27.5 | 0 | 0 |
| threat | 17.8 | 17.5 | 9.5 | 51.1 | 0 | 0 |
| hypotheses | 19.6 | 22.9 | 8.6 | 63.3 | 0 | 0 |
| evidence | 30.9 | 38.3 | 12.5 | 103.8 | 0 | 0 |
| fix | 26.0 | 29.3 | 11.2 | 81.8 | 0 | 0 |
| gate | 25.0 | 32.7 | 9.0 | 87.2 | 0 | 0 |
| pre_scan | 15.6 | 24.2 | 4.1 | 61.5 | 0 | 0 |

**Mean total elapsed per run:** 143s  |  Min: 59s  |  Max: 476s


---

## Gate verdict detail per run


### `WebGoat_AddNewUser.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass9 | FAIL |

### `WebGoat_AddNewUser.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass9 | NEEDS_HUMAN |

### `WebGoat_App_Code_ConfigFile.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass9 | NEEDS_HUMAN |

### `WebGoat_App_Code_CookieManager.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass9 | NEEDS_HUMAN |

### `WebGoat_App_Code_CustomerLoginData.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | PASS |
| results_qwen3-coder-30b_temp0.7_pass10 | PASS |
| results_qwen3-coder-30b_temp0.7_pass2 | PASS |
| results_qwen3-coder-30b_temp0.7_pass3 | PASS |
| results_qwen3-coder-30b_temp0.7_pass4 | PASS |
| results_qwen3-coder-30b_temp0.7_pass5 | PASS |
| results_qwen3-coder-30b_temp0.7_pass6 | PASS |
| results_qwen3-coder-30b_temp0.7_pass7 | PASS |
| results_qwen3-coder-30b_temp0.7_pass8 | PASS |
| results_qwen3-coder-30b_temp0.7_pass9 | PASS |

### `WebGoat_App_Code_DB_DbConstants.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass9 | NEEDS_HUMAN |

### `WebGoat_App_Code_DB_DbProviderFactory.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | PASS |
| results_qwen3-coder-30b_temp0.7_pass10 | PASS |
| results_qwen3-coder-30b_temp0.7_pass2 | PASS |
| results_qwen3-coder-30b_temp0.7_pass3 | PASS |
| results_qwen3-coder-30b_temp0.7_pass4 | PASS |
| results_qwen3-coder-30b_temp0.7_pass5 | PASS |
| results_qwen3-coder-30b_temp0.7_pass6 | PASS |
| results_qwen3-coder-30b_temp0.7_pass7 | PASS |
| results_qwen3-coder-30b_temp0.7_pass8 | PASS |
| results_qwen3-coder-30b_temp0.7_pass9 | PASS |

### `WebGoat_App_Code_DB_DummyDbProvider.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass9 | NEEDS_HUMAN |

### `WebGoat_App_Code_DB_IDbProvider.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass9 | NEEDS_HUMAN |

### `WebGoat_App_Code_DB_MySqlDbProvider.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass9 | FAIL |

### `WebGoat_App_Code_DB_SqliteDbProvider.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass9 | FAIL |

### `WebGoat_App_Code_Encoder.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass9 | FAIL |

### `WebGoat_App_Code_Settings.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass9 | NEEDS_HUMAN |

### `WebGoat_App_Code_Util.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass9 | FAIL |

### `WebGoat_App_Code_VeryWeakRandom.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass9 | NEEDS_HUMAN |

### `WebGoat_App_Code_WeakMessageDigest.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass9 | NEEDS_HUMAN |

### `WebGoat_App_Code_WeakRandom.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass9 | FAIL |

### `WebGoat_App_Data_XmlInjectionUsers.xml`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass9 | FAIL |

### `WebGoat_ChangePassword.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass9 | NEEDS_HUMAN |

### `WebGoat_ChangePassword.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass9 | NEEDS_HUMAN |

### `WebGoat_Code_DatabaseUtilities.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass9 | FAIL |

### `WebGoat_Code_IOHelper.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass9 | NEEDS_HUMAN |

### `WebGoat_Code_SQLiteMembershipProvider.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass9 | FAIL |

### `WebGoat_Code_SQLiteProfileProvider.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass9 | FAIL |

### `WebGoat_Code_SQLiteRoleProvider.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass9 | FAIL |

### `WebGoat_Configuration_Default.config`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass9 | NEEDS_HUMAN |

### `WebGoat_Content_About.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass9 | NEEDS_HUMAN |

### `WebGoat_Content_About.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass9 | NEEDS_HUMAN |

### `WebGoat_Content_BasicAuth.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass9 | FAIL |

### `WebGoat_Content_BasicAuth.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass9 | NEEDS_HUMAN |

### `WebGoat_Content_Challenge1.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass9 | FAIL |

### `WebGoat_Content_Challenge1.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass9 | NEEDS_HUMAN |

### `WebGoat_Content_Challenge2.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass9 | FAIL |

### `WebGoat_Content_Challenge2.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass9 | NEEDS_HUMAN |

### `WebGoat_Content_Challenge3.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass9 | NEEDS_HUMAN |

### `WebGoat_Content_Challenge3.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass9 | NEEDS_HUMAN |

### `WebGoat_Content_ChangePwd.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass9 | FAIL |

### `WebGoat_Default.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass9 | FAIL |

### `WebGoat_Default.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass9 | NEEDS_HUMAN |

### `WebGoat_ForgotPassword.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass9 | FAIL |

### `WebGoat_ForgotPassword.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass9 | NEEDS_HUMAN |

### `WebGoat_Global.asax.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass9 | FAIL |

### `WebGoat_LoginPage.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass9 | FAIL |

### `WebGoat_LoginPage.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass9 | NEEDS_HUMAN |

### `WebGoat_ProxySetup.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass9 | NEEDS_HUMAN |

### `WebGoat_ProxySetup.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass9 | NEEDS_HUMAN |

### `WebGoat_Web.config`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass9 | FAIL |

### `WebGoat_WebGoat.NET.csproj`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass9 | FAIL |

### `WebGoat_dbtest.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass4 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass5 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass6 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass7 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass9 | FAIL |

### `WebGoat_dbtest.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp0.7_pass1 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass10 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass2 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass3 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp0.7_pass8 | FAIL |
| results_qwen3-coder-30b_temp0.7_pass9 | FAIL |