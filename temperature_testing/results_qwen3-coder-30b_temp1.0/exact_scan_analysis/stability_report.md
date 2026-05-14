# Scan stability analysis — temp=1.0

**Runs analysed:** 13  |  **Files:** 50  |  **Stability threshold:** 80%

## Summary
| File | Runs | Gate: PASS | FAIL | NEEDS_HUMAN | Gate consistency | Stable findings | Sensitive findings |
|---|---|---|---|---|---|---|---|
| `WebGoat_AddNewUser.aspx.cs` | 12 | 0 | 11 | 1 | 92% | 0 | 27 |
| `WebGoat_AddNewUser.aspx.designer.cs` | 12 | 0 | 1 | 11 | 92% | 0 | 19 |
| `WebGoat_App_Code_ConfigFile.cs` | 12 | 0 | 6 | 6 | 50% | 0 | 12 |
| `WebGoat_App_Code_CookieManager.cs` | 12 | 0 | 8 | 4 | 67% | 0 | 12 |
| `WebGoat_App_Code_CustomerLoginData.cs` | 12 | 6 | 4 | 2 | 50% | 0 | 26 |
| `WebGoat_App_Code_DB_DbConstants.cs` | 12 | 0 | 1 | 11 | 92% | 0 | 6 |
| `WebGoat_App_Code_DB_DbProviderFactory.cs` | 12 | 7 | 0 | 5 | 58% | 0 | 9 |
| `WebGoat_App_Code_DB_DummyDbProvider.cs` | 12 | 2 | 6 | 4 | 50% | 0 | 24 |
| `WebGoat_App_Code_DB_IDbProvider.cs` | 12 | 0 | 2 | 10 | 83% | 0 | 29 |
| `WebGoat_App_Code_DB_MySqlDbProvider.cs` | 12 | 0 | 10 | 0 | 83% | 0 | 48 |
| `WebGoat_App_Code_DB_SqliteDbProvider.cs` | 12 | 0 | 11 | 0 | 92% | 0 | 71 |
| `WebGoat_App_Code_Encoder.cs` | 12 | 0 | 12 | 0 | 100% | 0 | 39 |
| `WebGoat_App_Code_Settings.cs` | 12 | 1 | 2 | 9 | 75% | 0 | 11 |
| `WebGoat_App_Code_Util.cs` | 12 | 0 | 8 | 4 | 67% | 0 | 27 |
| `WebGoat_App_Code_VeryWeakRandom.cs` | 12 | 0 | 1 | 11 | 92% | 0 | 9 |
| `WebGoat_App_Code_WeakMessageDigest.cs` | 12 | 0 | 2 | 10 | 83% | 0 | 13 |
| `WebGoat_App_Code_WeakRandom.cs` | 12 | 0 | 5 | 7 | 58% | 0 | 17 |
| `WebGoat_App_Data_XmlInjectionUsers.xml` | 12 | 0 | 4 | 8 | 67% | 0 | 5 |
| `WebGoat_ChangePassword.aspx.cs` | 12 | 0 | 4 | 8 | 67% | 0 | 17 |
| `WebGoat_ChangePassword.aspx.designer.cs` | 12 | 0 | 2 | 10 | 83% | 0 | 21 |
| `WebGoat_Code_DatabaseUtilities.cs` | 12 | 0 | 11 | 0 | 92% | 0 | 31 |
| `WebGoat_Code_IOHelper.cs` | 12 | 0 | 7 | 5 | 58% | 0 | 6 |
| `WebGoat_Code_SQLiteMembershipProvider.cs` | 12 | 0 | 10 | 2 | 83% | 0 | 28 |
| `WebGoat_Code_SQLiteProfileProvider.cs` | 12 | 0 | 10 | 2 | 83% | 0 | 16 |
| `WebGoat_Code_SQLiteRoleProvider.cs` | 12 | 0 | 10 | 2 | 83% | 0 | 25 |
| `WebGoat_Configuration_Default.config` | 12 | 4 | 0 | 8 | 67% | 0 | 3 |
| `WebGoat_Content_About.aspx.cs` | 12 | 4 | 3 | 5 | 42% | 1 | 6 |
| `WebGoat_Content_About.aspx.designer.cs` | 12 | 2 | 0 | 9 | 75% | 0 | 3 |
| `WebGoat_Content_BasicAuth.aspx.cs` | 12 | 0 | 5 | 7 | 58% | 0 | 8 |
| `WebGoat_Content_BasicAuth.aspx.designer.cs` | 12 | 0 | 0 | 12 | 100% | 0 | 9 |
| `WebGoat_Content_Challenge1.aspx.cs` | 12 | 1 | 2 | 9 | 75% | 1 | 15 |
| `WebGoat_Content_Challenge1.aspx.designer.cs` | 12 | 3 | 0 | 9 | 75% | 0 | 11 |
| `WebGoat_Content_Challenge2.aspx.cs` | 12 | 0 | 3 | 9 | 75% | 0 | 14 |
| `WebGoat_Content_Challenge2.aspx.designer.cs` | 12 | 2 | 1 | 9 | 75% | 0 | 14 |
| `WebGoat_Content_Challenge3.aspx.cs` | 12 | 2 | 2 | 8 | 67% | 0 | 16 |
| `WebGoat_Content_Challenge3.aspx.designer.cs` | 12 | 1 | 0 | 11 | 92% | 0 | 13 |
| `WebGoat_Content_ChangePwd.aspx.cs` | 12 | 0 | 7 | 5 | 58% | 0 | 12 |
| `WebGoat_Default.aspx.cs` | 12 | 0 | 11 | 1 | 92% | 0 | 24 |
| `WebGoat_Default.aspx.designer.cs` | 12 | 0 | 1 | 11 | 92% | 0 | 10 |
| `WebGoat_ForgotPassword.aspx.cs` | 12 | 0 | 0 | 12 | 100% | 0 | 13 |
| `WebGoat_ForgotPassword.aspx.designer.cs` | 12 | 0 | 0 | 12 | 100% | 0 | 6 |
| `WebGoat_Global.asax.cs` | 12 | 0 | 11 | 1 | 92% | 0 | 34 |
| `WebGoat_LoginPage.aspx.cs` | 12 | 0 | 9 | 3 | 75% | 0 | 22 |
| `WebGoat_LoginPage.aspx.designer.cs` | 12 | 0 | 0 | 12 | 100% | 0 | 11 |
| `WebGoat_ProxySetup.aspx.cs` | 12 | 4 | 1 | 7 | 58% | 1 | 14 |
| `WebGoat_ProxySetup.aspx.designer.cs` | 12 | 0 | 2 | 10 | 83% | 0 | 15 |
| `WebGoat_Web.config` | 12 | 0 | 12 | 0 | 100% | 0 | 59 |
| `WebGoat_WebGoat.NET.csproj` | 12 | 1 | 9 | 2 | 75% | 0 | 29 |
| `WebGoat_dbtest.aspx.cs` | 12 | 0 | 12 | 0 | 100% | 0 | 38 |
| `WebGoat_dbtest.aspx.designer.cs` | 12 | 0 | 6 | 6 | 50% | 0 | 16 |

---

## File: `WebGoat_AddNewUser.aspx.cs`

**Runs with this file:** 12  |  **Gate consistency:** 92%  |  **Verdict distribution:** FAIL: 11  NEEDS_HUMAN: 1

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Missing Input Validation for Username and Password Allows Weak Credentials | High | 8% (1/12) | 0.90 | model inconsistency |
| Hardcoded Security Question May Aid Credential Recovery Attacks | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Improper Logging Mechanism May Reveal Sensitive Information | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Verbose Error Messages Exposed to End Users | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Weak Credential Acceptance Due to Removed Input Validation | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Missing Input Validation for Username and Password | High | 8% (1/12) | 0.85 | model inconsistency |
| Insecure Password Policy Implementation | High | 8% (1/12) | 0.75 | model inconsistency |
| Commented-Out Security Control Removal | High | 8% (1/12) | 0.90 | model inconsistency |
| Verbose Error Handling May Reveal System Information | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Username Input Injection via Missing Validation | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Weak Security Question Allows Account Recovery Exploitation | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Account Enumeration via Username Validation Bypass | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Missing Input Validation for Username | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Hardcoded Security Question | Low | 8% (1/12) | 0.90 | model inconsistency |
| Missing Authorization Check for User Account Creation | High | 8% (1/12) | 0.90 | model inconsistency |
| Arbitrary Account Creation Leading to Privilege Escalation | High | 8% (1/12) | 0.90 | model inconsistency |
| Hardcoded Security Question in Source Code | Low | 8% (1/12) | 0.90 | model inconsistency |
| Potential Hardcoded Security Question | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Hardcoded Security Question | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Input Validation Bypass Leading to Injection Risk | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Weak Credential Handling Due to Removed Validation | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Missing Authorization Check on User Account Creation | High | 8% (1/12) | 0.90 | model inconsistency |
| Input Validation Missing for Account Creation Fields | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Weak Password Validation in Account Creation | High | 8% (1/12) | 0.80 | model inconsistency |
| Privilege Escalation via Unauthorized Account Creation | High | 8% (1/12) | 0.90 | model inconsistency |
| Verbose Error Messages Exposed | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Missing Authorization Check on User Creation | High | 42% (5/12) | 0.90 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.8 | 2.2 | 4.9 | 12.9 | 0 | 0 |
| threat | 11.4 | 1.4 | 9.5 | 13.4 | 0 | 0 |
| hypotheses | 10.7 | 1.2 | 8.6 | 12.9 | 0 | 0 |
| evidence | 14.2 | 4.9 | 0.8 | 18.5 | 0 | 0 |
| fix | 14.7 | 6.8 | 2.3 | 25.2 | 0 | 0 |
| gate | 8.2 | 1.8 | 5.2 | 10.9 | 0 | 0 |
| pre_scan | 4.3 | 0.8 | 3.6 | 6.3 | 0 | 0 |

**Mean total elapsed per run:** 69s  |  Min: 42s  |  Max: 82s


---

## File: `WebGoat_AddNewUser.aspx.designer.cs`

**Runs with this file:** 12  |  **Gate consistency:** 92%  |  **Verdict distribution:** FAIL: 1  NEEDS_HUMAN: 11

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Potential Exposure of Sensitive Fields in UI | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential for SQL Injection via User Input | High | 8% (1/12) | 0.30 | borderline confidence |
| Potential Exposure of Security Question/Answer | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Input Sanitization Issues | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential for SQL Injection in User Creation | High | 8% (1/12) | 0.30 | borderline confidence |
| Sensitive Data Exposure in User Creation Form Fields | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Hardcoded Credentials or Secrets in UI Code | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Missing Authorization Controls on User Creation | High | 8% (1/12) | 0.30 | borderline confidence |
| Potential Weak Cryptographic Practices in Password Handling | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Missing Authorization Check on User Creation | High | 8% (1/12) | 0.30 | borderline confidence |
| Hardcoded Credentials or Configuration Values | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Exposure of Sensitive Data in UI Elements | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Weak Password Handling in User Creation | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Injection Vulnerability in User Creation Form | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Hardcoded Credentials or Configuration | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Insecure Transmission of User Data | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Exposure of User Input Fields | Medium | 17% (2/12) | 0.30 | borderline confidence |
| Potential SQL Injection Vulnerability in User Creation | High | 17% (2/12) | 0.30 | borderline confidence |
| Missing Authorization Check on User Creation | High | 67% (8/12) | 0.30 | borderline confidence |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 3.2 | 0.2 | 3.0 | 3.7 | 0 | 0 |
| threat | 9.5 | 1.0 | 7.6 | 11.3 | 0 | 0 |
| hypotheses | 8.6 | 1.1 | 6.5 | 10.1 | 0 | 0 |
| evidence | 10.2 | 1.2 | 7.4 | 11.9 | 0 | 0 |
| fix | 11.4 | 5.3 | 1.4 | 18.8 | 0 | 0 |
| gate | 8.5 | 1.2 | 6.3 | 10.5 | 0 | 0 |
| pre_scan | 3.1 | 0.2 | 2.6 | 3.5 | 0 | 0 |

**Mean total elapsed per run:** 54s  |  Min: 45s  |  Max: 62s


---

## File: `WebGoat_App_Code_ConfigFile.cs`

**Runs with this file:** 12  |  **Gate consistency:** 50%  |  **Verdict distribution:** FAIL: 6  NEEDS_HUMAN: 6

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Sensitive Data Exposure in Configuration Files | Medium | 8% (1/12) | 0.75 | model inconsistency |
| Injection via Unsanitized Configuration Values | High | 8% (1/12) | 0.80 | model inconsistency |
| Potential Hardcoded Credentials in Configuration File | High | 8% (1/12) | 0.90 | model inconsistency |
| Possible Sensitive Data Exposure in Configuration File | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Missing Authorization Checks on Configuration File Access | High | 8% (1/12) | 0.90 | model inconsistency |
| Insecure Configuration - No Input Validation in Config File Parser | High | 8% (1/12) | 0.85 | model inconsistency |
| Insecure Configuration - Missing Input Validation in Config File Parser | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Configuration Injection Vulnerability Through File Manipulation | High | 8% (1/12) | 0.85 | model inconsistency |
| Lack of Validation in Config Parser Allows Malformed Input Processing | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Missing Input Validation in Config File Parser | Medium | 17% (2/12) | 0.88 | model inconsistency |
| Insecure Configuration - No Input Validation in Config File Parser | Medium | 17% (2/12) | 0.88 | model inconsistency |
| Insecure Configuration - No Input Validation or Sanitization in Config File Parser | Medium | 33% (4/12) | 0.84 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 3.4 | 0.2 | 3.2 | 3.8 | 0 | 0 |
| threat | 8.3 | 1.7 | 5.3 | 11.4 | 0 | 0 |
| hypotheses | 7.9 | 2.2 | 3.5 | 10.5 | 0 | 0 |
| evidence | 11.4 | 4.7 | 5.5 | 22.9 | 0 | 0 |
| fix | 11.4 | 6.9 | 5.6 | 28.5 | 0 | 0 |
| gate | 6.9 | 1.2 | 5.8 | 9.6 | 0 | 0 |
| pre_scan | 3.9 | 0.4 | 3.4 | 4.4 | 0 | 0 |

**Mean total elapsed per run:** 53s  |  Min: 35s  |  Max: 89s


---

## File: `WebGoat_App_Code_CookieManager.cs`

**Runs with this file:** 12  |  **Gate consistency:** 67%  |  **Verdict distribution:** FAIL: 8  NEEDS_HUMAN: 4

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Missing Cookie Addition to HTTP Response | Critical | 8% (1/12) | 0.95 | model inconsistency |
| Session Persistence Failure Due to Missing Cookie Addition | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Authentication Bypass via Missing Cookie Addition | High | 8% (1/12) | 0.90 | model inconsistency |
| Hardcoded Authentication Cookie Name Exposure | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Missing Secure Flag on Authentication Cookie | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential Auth Bypass via Commented-Out Session Logic | High | 8% (1/12) | 0.80 | model inconsistency |
| Incomplete Cookie Setting Logic May Break Authentication Flow | High | 8% (1/12) | 0.90 | model inconsistency |
| Missing Authentication Cookie in HTTP Response | High | 17% (2/12) | 0.95 | model inconsistency |
| Missing Cookie Addition to HTTP Response | High | 17% (2/12) | 0.95 | model inconsistency |
| Missing Authentication Cookie Addition to HTTP Response | Critical | 17% (2/12) | 0.95 | model inconsistency |
| Missing Authentication Cookie Addition to HTTP Response | High | 17% (2/12) | 0.95 | model inconsistency |
| Authentication Cookie Missing Security Flags | High | 17% (2/12) | 0.90 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 4.5 | 0.2 | 3.9 | 4.7 | 0 | 0 |
| threat | 9.4 | 1.5 | 7.3 | 12.4 | 0 | 0 |
| hypotheses | 7.9 | 1.3 | 5.6 | 10.2 | 0 | 0 |
| evidence | 8.4 | 2.4 | 6.1 | 14.7 | 0 | 0 |
| fix | 7.5 | 4.2 | 4.8 | 20.1 | 0 | 0 |
| gate | 6.1 | 1.4 | 4.7 | 9.3 | 0 | 0 |
| pre_scan | 3.1 | 0.2 | 2.8 | 3.6 | 0 | 0 |

**Mean total elapsed per run:** 47s  |  Min: 38s  |  Max: 75s


---

## File: `WebGoat_App_Code_CustomerLoginData.cs`

**Runs with this file:** 12  |  **Gate consistency:** 50%  |  **Verdict distribution:** FAIL: 4  NEEDS_HUMAN: 2  PASS: 6

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Insecure Direct Object Reference | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Potential Injection Vulnerability via Message Property | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Missing Authorization Check | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Plain Text Password Storage | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Missing Access Control on CustomerLoginData Fields | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Improper Assignment in Message Property Setter | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Unsecured Password Storage | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Missing Authorization Check on isLoggedIn Flag | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Direct Access to Password Field May Enable Injection | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Publicly Exposed isLoggedIn Field | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Flawed Message Property Setter Logic | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Missing Authorization Check on Sensitive Data Access | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Hardcoded Sensitive Data Exposure | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Insecure Authentication State Management | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Exposed Sensitive Fields in CustomerLoginData Class | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Incorrect Message Property Assignment in CustomerLoginData | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Information Disclosure via Incorrect Message Assignment | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Hardcoded Credentials or Sensitive Data Exposure | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Improper Handling of Sensitive Message Data | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Potential Secret Exposure in CustomerLoginData Class | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Hardcoded Sensitive Data in Class Fields | Low | 8% (1/12) | 0.80 | model inconsistency |
| Missing Access Control on Sensitive Fields | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Exposure of Sensitive Credentials | High | 8% (1/12) | 0.90 | model inconsistency |
| Inconsistent Message Handling | Low | 8% (1/12) | 0.85 | model inconsistency |
| Insecure Direct Object Reference in CustomerLoginData | Medium | 17% (2/12) | 0.90 | model inconsistency |
| Potential Injection Vulnerability via Message Property Setter | Medium | 17% (2/12) | 0.88 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 3.1 | 0.2 | 2.7 | 3.4 | 0 | 0 |
| threat | 9.7 | 1.7 | 7.9 | 12.8 | 0 | 0 |
| hypotheses | 9.5 | 1.5 | 7.2 | 12.1 | 0 | 0 |
| evidence | 10.0 | 2.1 | 7.1 | 15.0 | 0 | 0 |
| fix | 10.4 | 2.9 | 6.6 | 17.4 | 0 | 0 |
| gate | 6.5 | 2.3 | 4.3 | 10.2 | 0 | 0 |
| pre_scan | 4.9 | 0.7 | 4.0 | 6.2 | 0 | 0 |

**Mean total elapsed per run:** 54s  |  Min: 42s  |  Max: 75s


---

## File: `WebGoat_App_Code_DB_DbConstants.cs`

**Runs with this file:** 12  |  **Gate consistency:** 92%  |  **Verdict distribution:** FAIL: 1  NEEDS_HUMAN: 11

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Potential Hardcoded Database Credentials | High | 8% (1/12) | 0.90 | model inconsistency |
| Database Configuration Values Exposed | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Potential Exposure of Sensitive Configuration Data | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Hardcoded Database Credentials Exposed | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential Weak Cryptographic Practices | Medium | 17% (2/12) | 0.57 | borderline confidence |
| Hardcoded Database Credentials | High | 58% (7/12) | 0.64 | borderline confidence |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 3.4 | 0.3 | 3.1 | 3.9 | 0 | 0 |
| threat | 6.8 | 1.7 | 4.5 | 9.5 | 0 | 0 |
| hypotheses | 6.0 | 2.0 | 3.3 | 9.4 | 0 | 0 |
| evidence | 6.6 | 2.5 | 3.3 | 9.7 | 0 | 0 |
| fix | 6.3 | 2.4 | 1.2 | 9.9 | 0 | 0 |
| gate | 5.7 | 0.9 | 4.5 | 7.1 | 0 | 0 |
| pre_scan | 2.2 | 0.4 | 1.8 | 3.0 | 0 | 0 |

**Mean total elapsed per run:** 37s  |  Min: 22s  |  Max: 48s


---

## File: `WebGoat_App_Code_DB_DbProviderFactory.cs`

**Runs with this file:** 12  |  **Gate consistency:** 58%  |  **Verdict distribution:** NEEDS_HUMAN: 5  PASS: 7

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Configuration File Loading Without Validation | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Exposure of Internal Database Configuration via Logs | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Thread Safety Issues Leading to Race Conditions | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Potential Information Disclosure via Log Output | Medium | 17% (2/12) | 0.90 | model inconsistency |
| Information Disclosure in Log Messages | Medium | 17% (2/12) | 0.90 | model inconsistency |
| Information Disclosure via Logging | Medium | 17% (2/12) | 0.90 | model inconsistency |
| Potential SQL Injection via Dynamic Provider Selection | Medium | 17% (2/12) | 0.62 | borderline confidence |
| Information Exposure Through Logging | Medium | 17% (2/12) | 0.90 | model inconsistency |
| Potential Information Disclosure via Logging | Medium | 33% (4/12) | 0.90 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 3.5 | 0.2 | 3.0 | 3.8 | 0 | 0 |
| threat | 6.8 | 2.3 | 4.6 | 9.9 | 0 | 0 |
| hypotheses | 7.0 | 2.4 | 3.2 | 9.8 | 0 | 0 |
| evidence | 7.2 | 2.0 | 3.5 | 9.5 | 0 | 0 |
| fix | 6.5 | 3.1 | 3.6 | 14.7 | 0 | 0 |
| gate | 4.7 | 0.9 | 3.1 | 6.4 | 0 | 0 |
| pre_scan | 1.9 | 0.3 | 1.6 | 2.4 | 0 | 0 |

**Mean total elapsed per run:** 38s  |  Min: 25s  |  Max: 51s


---

## File: `WebGoat_App_Code_DB_DummyDbProvider.cs`

**Runs with this file:** 12  |  **Gate consistency:** 50%  |  **Verdict distribution:** FAIL: 6  NEEDS_HUMAN: 4  PASS: 2

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Missing Authentication Logic Implementation | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential Exposure of Customer Data via Empty Return Values | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Missing Authentication Logic in Customer Login Validation | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential Information Disclosure via Empty Return Values | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Insecure Authentication Logic | High | 8% (1/12) | 0.90 | model inconsistency |
| Hardcoded Credentials or Configuration in Dummy Implementation | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Potential Missing Authorization Checks in Dummy Methods | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Denial of Service via Improper Error Handling in Dummy Provider | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Information Disclosure via Method Signatures in Dummy Provider | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Hardcoded Credentials or Connection Strings | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Missing Authorization Checks in Database Operations | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Potential Information Disclosure in Database Methods | Low | 8% (1/12) | 0.85 | model inconsistency |
| Missing Authorization Checks in Customer Data Access Methods | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential Information Disclosure in Authentication Methods | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Missing Authorization Checks | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential Information Disclosure | High | 8% (1/12) | 0.90 | model inconsistency |
| Missing Authentication and Authorization Checks | Critical | 8% (1/12) | 0.90 | model inconsistency |
| Missing Authorization Checks in Data Access Methods | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Potential Exposure of Customer Data Access Methods | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Hardcoded Database Connection Information | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Potential Information Exposure Through Method Return Values | Low | 8% (1/12) | 0.85 | model inconsistency |
| Missing Authentication Logic | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential Information Disclosure via Method Returns | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Denial of Service via Incomplete Data Access Implementation | Medium | 8% (1/12) | 0.75 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 3.5 | 0.2 | 3.2 | 3.8 | 0 | 0 |
| threat | 10.2 | 1.0 | 9.0 | 12.5 | 0 | 0 |
| hypotheses | 9.5 | 1.2 | 7.3 | 11.2 | 0 | 0 |
| evidence | 11.7 | 2.2 | 7.9 | 14.7 | 0 | 0 |
| fix | 10.5 | 4.3 | 1.7 | 17.1 | 0 | 0 |
| gate | 6.9 | 1.4 | 5.0 | 8.7 | 0 | 0 |
| pre_scan | 3.2 | 0.3 | 2.5 | 3.5 | 0 | 0 |

**Mean total elapsed per run:** 55s  |  Min: 46s  |  Max: 65s


---

## File: `WebGoat_App_Code_DB_IDbProvider.cs`

**Runs with this file:** 12  |  **Gate consistency:** 83%  |  **Verdict distribution:** FAIL: 2  NEEDS_HUMAN: 10

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Potential Hardcoded Credentials in Database Provider Interface | High | 8% (1/12) | 0.30 | borderline confidence |
| Potential SQL Injection Vulnerability in Data Access Methods | High | 8% (1/12) | 0.30 | borderline confidence |
| Missing Cryptographic Security Controls in Authentication Methods | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Authentication Bypass via Direct Interface Usage | High | 8% (1/12) | 0.30 | borderline confidence |
| Potential Exposure of Sensitive Data Access Methods | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Missing Authorization Checks in Database Interface Methods | High | 8% (1/12) | 0.30 | borderline confidence |
| Potential Exposure of Sensitive Data Through Interface Methods | High | 8% (1/12) | 0.90 | model inconsistency |
| Unauthorized Credential Access Through Interface Methods | Critical | 8% (1/12) | 0.90 | model inconsistency |
| Potential Insecure Direct Object Reference (IDOR) in customer data access methods | High | 8% (1/12) | 0.30 | borderline confidence |
| Possible Exposure of Password Retrieval Method | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential SQL Injection Vulnerability in Parameterized Queries | High | 8% (1/12) | 0.30 | borderline confidence |
| Missing Authorization Checks on Customer Data Access | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential Authentication Bypass via Customer Login Method | Critical | 8% (1/12) | 0.90 | model inconsistency |
| Potential Data Exposure through Unauthorized Customer Data Access | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential Authentication Bypass via Missing Authorization Checks | High | 8% (1/12) | 0.30 | borderline confidence |
| Potential SQL Injection Vulnerability in Database Calls | High | 8% (1/12) | 0.30 | borderline confidence |
| Hardcoded Credentials or Connection Strings Possible in Implementations | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Missing Authorization Checks in Customer Data Access Methods | High | 8% (1/12) | 0.30 | borderline confidence |
| Potential SQL Injection Vulnerability via String Concatenation in Data Access Methods | High | 8% (1/12) | 0.30 | borderline confidence |
| Hardcoded Credentials or Connection Strings in Database Provider Interface | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential SQL Injection Vulnerability in Database Interface | High | 8% (1/12) | 0.30 | borderline confidence |
| Potential Hardcoded Credentials in Database Interface | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Missing Authorization Checks in Customer Data Access Methods | High | 8% (1/12) | 0.30 | borderline confidence |
| Potential Authentication Bypass via Weak Login Validation | High | 8% (1/12) | 0.30 | borderline confidence |
| Missing Authorization Checks on Sensitive Data Access | High | 8% (1/12) | 0.30 | borderline confidence |
| Potential Exposure of Sensitive Data via Direct Database Interface | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Hardcoded Credentials or Weak Cryptographic Practices | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Missing Authorization Controls in IDbProvider Methods | High | 8% (1/12) | 0.30 | borderline confidence |
| Customer Data Exposure Through IDbProvider Interface Methods | Medium | 8% (1/12) | 0.30 | borderline confidence |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 3.3 | 0.3 | 3.0 | 3.9 | 0 | 0 |
| threat | 11.3 | 1.8 | 9.7 | 15.3 | 0 | 0 |
| hypotheses | 11.0 | 1.3 | 8.6 | 13.4 | 0 | 0 |
| evidence | 13.5 | 1.7 | 9.8 | 17.0 | 0 | 0 |
| fix | 12.7 | 8.4 | 2.0 | 34.7 | 0 | 0 |
| gate | 9.8 | 1.6 | 7.8 | 13.2 | 0 | 0 |
| pre_scan | 4.0 | 1.0 | 3.2 | 6.5 | 0 | 0 |

**Mean total elapsed per run:** 66s  |  Min: 52s  |  Max: 86s


---

## File: `WebGoat_App_Code_DB_MySqlDbProvider.cs`

**Runs with this file:** 12  |  **Gate consistency:** 83%  |  **Verdict distribution:** FAIL: 10  UNKNOWN: 1  accept: 1

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Weak Password Handling | High | 8% (1/12) | 0.85 | model inconsistency |
| Insecure Direct Object Reference | High | 8% (1/12) | 0.30 | borderline confidence |
| SQL Injection Vulnerability | Critical | 8% (1/12) | 0.95 | model inconsistency |
| Hardcoded Secrets in Database Connection Configuration | High | 8% (1/12) | 0.20 | borderline confidence |
| Missing Authentication Boundary in Database Provider Interface | High | 8% (1/12) | 0.90 | model inconsistency |
| Insecure Password Handling with Encoding | High | 8% (1/12) | 0.85 | model inconsistency |
| Shell Injection via mysql client executable | Critical | 8% (1/12) | 0.90 | model inconsistency |
| SQL Injection | Critical | 8% (1/12) | 0.90 | model inconsistency |
| Hardcoded Database Credentials | High | 8% (1/12) | 0.90 | model inconsistency |
| SQL Injection in IsValidCustomerLogin Method | Critical | 8% (1/12) | 0.95 | model inconsistency |
| Weak Password Encoding | High | 8% (1/12) | 0.85 | model inconsistency |
| Missing Input Validation in Database Queries | High | 8% (1/12) | 0.95 | model inconsistency |
| Missing Input Validation on Database Operations | Medium | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection in GetCustomerEmail Method | High | 8% (1/12) | 0.90 | model inconsistency |
| SQL Injection in GetOrders Method | High | 8% (1/12) | 0.90 | model inconsistency |
| SQL Injection in GetProductDetails Method | Medium | 8% (1/12) | 0.80 | model inconsistency |
| SQL Injection in GetOrderDetails Method | High | 8% (1/12) | 0.90 | model inconsistency |
| SQL Injection in GetPayments Method | High | 8% (1/12) | 0.90 | model inconsistency |
| SQL Injection in GetProductsAndCategories Method | Medium | 8% (1/12) | 0.80 | model inconsistency |
| SQL Injection in GetEmailByName Method | Medium | 8% (1/12) | 0.80 | model inconsistency |
| SQL Injection in GetCustomerEmails Method | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Hardcoded Credentials in Database Connection Strings | High | 8% (1/12) | 0.90 | model inconsistency |
| SQL Injection via String Concatenation in MySqlDbProvider | Critical | 8% (1/12) | 0.95 | model inconsistency |
| Command Injection via Shell Execution in RecreateGoatDb Method | Critical | 8% (1/12) | 0.90 | model inconsistency |
| Denial of Service via Resource Exhaustion in Database Operations | High | 8% (1/12) | 0.90 | model inconsistency |
| SQL Injection Vulnerability in CustomCustomerLogin Method | Critical | 17% (2/12) | 0.95 | model inconsistency |
| SQL Injection in CustomerLogin method | Critical | 17% (2/12) | 0.95 | model inconsistency |
| SQL Injection in GetEmailByCustomerNumber method | Critical | 17% (2/12) | 0.95 | model inconsistency |
| SQL Injection in CustomerLogin Query | Critical | 25% (3/12) | 0.95 | model inconsistency |
| SQL Injection Vulnerability in CustomerLogin Method | Critical | 25% (3/12) | 0.95 | model inconsistency |
| SQL Injection Vulnerability in GetCustomerEmail Method | Critical | 25% (3/12) | 0.95 | model inconsistency |
| SQL Injection Vulnerability in GetOrders Method | Critical | 25% (3/12) | 0.95 | model inconsistency |
| SQL Injection Vulnerability in GetProductDetails Method | Critical | 25% (3/12) | 0.95 | model inconsistency |
| SQL Injection Vulnerability in GetOrderDetails Method | Critical | 25% (3/12) | 0.95 | model inconsistency |
| SQL Injection Vulnerability in GetPayments Method | Critical | 25% (3/12) | 0.95 | model inconsistency |
| SQL Injection Vulnerability in GetProductsAndCategories Method | Critical | 25% (3/12) | 0.95 | model inconsistency |
| SQL Injection Vulnerability in GetEmailByName Method | Critical | 25% (3/12) | 0.95 | model inconsistency |
| SQL Injection Vulnerability in GetCustomerEmails Method | Critical | 25% (3/12) | 0.95 | model inconsistency |
| SQL Injection Vulnerability in GetEmailByCustomerNumber Method | Critical | 25% (3/12) | 0.95 | model inconsistency |
| SQL Injection in CustomCustomerLogin method | Critical | 33% (4/12) | 0.95 | model inconsistency |
| SQL Injection in GetCustomerEmail Method | Critical | 42% (5/12) | 0.95 | model inconsistency |
| SQL Injection in GetOrders Method | Critical | 42% (5/12) | 0.95 | model inconsistency |
| SQL Injection in GetProductDetails Method | Critical | 42% (5/12) | 0.95 | model inconsistency |
| SQL Injection in GetOrderDetails Method | Critical | 42% (5/12) | 0.95 | model inconsistency |
| SQL Injection in GetPayments Method | Critical | 42% (5/12) | 0.95 | model inconsistency |
| SQL Injection in GetProductsAndCategories Method | Critical | 42% (5/12) | 0.95 | model inconsistency |
| SQL Injection in GetEmailByName Method | Critical | 42% (5/12) | 0.95 | model inconsistency |
| SQL Injection in GetCustomerEmails Method | Critical | 42% (5/12) | 0.95 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.7 | 0.4 | 5.2 | 6.4 | 0 | 0 |
| threat | 25.3 | 8.9 | 10.3 | 33.6 | 0 | 0 |
| hypotheses | 24.4 | 8.9 | 9.9 | 38.8 | 0 | 0 |
| evidence | 34.1 | 11.4 | 16.2 | 50.1 | 0 | 0 |
| fix | 35.8 | 14.1 | 12.7 | 51.1 | 0 | 0 |
| gate | 16.2 | 7.8 | 1.3 | 24.1 | 0 | 0 |
| pre_scan | 17.2 | 9.6 | 1.6 | 29.6 | 0 | 0 |

**Mean total elapsed per run:** 159s  |  Min: 67s  |  Max: 210s


---

## File: `WebGoat_App_Code_DB_SqliteDbProvider.cs`

**Runs with this file:** 12  |  **Gate consistency:** 92%  |  **Verdict distribution:** FAIL: 11  accept: 1

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| SQL Injection in Customer Login | Critical | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection in GetCustomerEmail | High | 8% (1/12) | 0.90 | model inconsistency |
| SQL Injection in GetOrders | High | 8% (1/12) | 0.90 | model inconsistency |
| SQL Injection in GetProductDetails | Medium | 8% (1/12) | 0.80 | model inconsistency |
| SQL Injection in GetOrderDetails | Medium | 8% (1/12) | 0.80 | model inconsistency |
| SQL Injection in GetPayments | Medium | 8% (1/12) | 0.80 | model inconsistency |
| SQL Injection in GetProductsAndCategories | Medium | 8% (1/12) | 0.80 | model inconsistency |
| SQL Injection in GetEmailByName | Medium | 8% (1/12) | 0.80 | model inconsistency |
| SQL Injection in GetEmailByCustomerNumber | Medium | 8% (1/12) | 0.80 | model inconsistency |
| SQL Injection in GetCustomerEmails | Medium | 8% (1/12) | 0.80 | model inconsistency |
| SQL Injection in IsValidCustomerLogin due to String Concatenation | Critical | 8% (1/12) | 0.90 | model inconsistency |
| SQL Injection in CustomCustomerLogin due to String Concatenation | Critical | 8% (1/12) | 0.90 | model inconsistency |
| SQL Injection in Customer Login Query | High | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection in Customer Email Retrieval | High | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection in Order Details Query | High | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection in Product Details Query | High | 8% (1/12) | 0.95 | model inconsistency |
| Potential Data Exposure Through Insecure Query Construction | High | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection in CustomerLogin Validation | High | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection in GetCustomerEmail Method | High | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection in GetCustomerDetails Method | High | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection in GetOrders Method | High | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection in GetProductDetails Method | High | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection in GetPayments Method | High | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection in GetEmailByCustomerNumber Method | High | 8% (1/12) | 0.95 | model inconsistency |
| Missing Input Validation in Login Flow | High | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection in GetCustomerDetails Method | Critical | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection in Customer Login Query | Critical | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection in CustomerLogin Validation via String Concatenation | Critical | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection in CustomCustomerLogin via String Concatenation | Critical | 8% (1/12) | 0.95 | model inconsistency |
| Inverted Authentication Logic in IsValidCustomerLogin Method | Critical | 8% (1/12) | 0.90 | model inconsistency |
| Potential Information Disclosure in Error Handling | High | 8% (1/12) | 0.85 | model inconsistency |
| SQL Injection in Customer Login Validation | Critical | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection in Customer Email Retrieval | Critical | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection in Order Retrieval | Critical | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection in Product Details Retrieval | Critical | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection in Order Details Retrieval | Critical | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection in Payment Retrieval | Critical | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection in Product and Category Retrieval | Critical | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection in Employee Email Retrieval | Critical | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection in Customer Number Email Retrieval | Critical | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection in Customer Email Search | Critical | 8% (1/12) | 0.95 | model inconsistency |
| Error Message Exposure with Raw Exceptions | Medium | 8% (1/12) | 1.00 | model inconsistency |
| Unauthorized Data Enumeration via SQL Injection | High | 8% (1/12) | 1.00 | model inconsistency |
| Business Logic Exploitation via Data Manipulation | High | 8% (1/12) | 1.00 | model inconsistency |
| SQL Injection via String Concatenation in SqliteDbProvider | Critical | 8% (1/12) | 0.95 | model inconsistency |
| Command Injection via External Process Execution | Critical | 8% (1/12) | 0.90 | model inconsistency |
| SQL Injection in CustomerLogin and Related Methods | Critical | 8% (1/12) | 0.95 | model inconsistency |
| Weak Password Encoding in CustomerLogin Methods | High | 8% (1/12) | 0.90 | model inconsistency |
| Insecure Direct Object Reference (IDOR) in GetEmailByCustomerNumber | High | 8% (1/12) | 0.90 | model inconsistency |
| Insecure Direct Object Reference (IDOR) in GetCustomerEmail | High | 8% (1/12) | 0.90 | model inconsistency |
| SQL Injection in Customer Login Method | Critical | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection in GetProductDetails Method (First Query) | Critical | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection in GetProductDetails Method (Second Query) | Critical | 8% (1/12) | 0.95 | model inconsistency |
| Missing Input Validation for Database Queries | High | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection in CustomerLogin Method | Critical | 8% (1/12) | 0.95 | model inconsistency |
| Insecure Direct Object Reference in GetCustomerDetails Method | High | 8% (1/12) | 0.90 | model inconsistency |
| SQL Injection in GetEmailByName Method | High | 17% (2/12) | 0.95 | model inconsistency |
| SQL Injection in GetCustomerEmails Method | High | 17% (2/12) | 0.95 | model inconsistency |
| SQL Injection in GetProductsAndCategories Method | High | 17% (2/12) | 0.95 | model inconsistency |
| SQL Injection in GetOrderDetails Method | High | 17% (2/12) | 0.95 | model inconsistency |
| SQL Injection in IsValidCustomerLogin Method | Critical | 17% (2/12) | 0.97 | model inconsistency |
| SQL Injection in CustomCustomerLogin Method | Critical | 17% (2/12) | 0.97 | model inconsistency |
| SQL Injection in GetProductDetails Method | Critical | 25% (3/12) | 0.95 | model inconsistency |
| SQL Injection in GetOrders Method | Critical | 33% (4/12) | 0.95 | model inconsistency |
| SQL Injection in GetPayments Method | Critical | 33% (4/12) | 0.95 | model inconsistency |
| SQL Injection in GetEmailByCustomerNumber Method | Critical | 33% (4/12) | 0.95 | model inconsistency |
| SQL Injection in GetCustomerEmail Method | Critical | 33% (4/12) | 0.96 | model inconsistency |
| SQL Injection in GetOrderDetails Method | Critical | 42% (5/12) | 0.96 | model inconsistency |
| SQL Injection in GetProductsAndCategories Method | Critical | 42% (5/12) | 0.96 | model inconsistency |
| SQL Injection in GetEmailByName Method | Critical | 42% (5/12) | 0.96 | model inconsistency |
| SQL Injection in GetCustomerEmails Method | Critical | 42% (5/12) | 0.96 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 6.8 | 1.1 | 5.5 | 8.2 | 0 | 0 |
| threat | 24.4 | 7.9 | 12.0 | 32.5 | 0 | 0 |
| hypotheses | 22.9 | 7.0 | 12.2 | 31.1 | 0 | 0 |
| evidence | 33.8 | 8.7 | 18.9 | 45.0 | 0 | 0 |
| fix | 37.6 | 16.2 | 10.1 | 67.1 | 0 | 0 |
| gate | 16.7 | 7.7 | 1.1 | 27.8 | 0 | 0 |
| pre_scan | 14.4 | 9.7 | 0.6 | 24.4 | 0 | 0 |

**Mean total elapsed per run:** 157s  |  Min: 70s  |  Max: 204s


---

## File: `WebGoat_App_Code_Encoder.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 12

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Predictable Salt in Encryption | High | 8% (1/12) | 0.90 | model inconsistency |
| Use of Default Block Size in RijndaelManaged | Medium | 8% (1/12) | 0.75 | model inconsistency |
| Insecure Authentication Ticket Handling | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Use of Deprecated RijndaelManaged Encryption Algorithm | High | 8% (1/12) | 0.90 | model inconsistency |
| Hardcoded Salt in PBKDF2 Key Derivation Reduces Cryptographic Security | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Potential Authentication Bypass in FormsAuthenticationTicket Encoding | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Weak Cryptographic Implementation with Hardcoded Salt | High | 8% (1/12) | 0.90 | model inconsistency |
| JSON Injection Vulnerability in ToJSONString Method | Medium | 8% (1/12) | 0.85 | model inconsistency |
| JSON Injection Vulnerability in ToJSONSAutocompleteString Method | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Use of Deprecated RijndaelManaged Algorithm in Encryption Implementation | High | 8% (1/12) | 0.95 | model inconsistency |
| Hardcoded Salt Value in Key Derivation Process | High | 8% (1/12) | 0.95 | model inconsistency |
| Hardcoded Salt May Be Sensitive Information for Cryptographic Attacks | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Use of Weak Encryption Algorithm (RijndaelManaged) | High | 8% (1/12) | 0.95 | model inconsistency |
| Hardcoded Salt in Encryption Implementation | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Insecure Authentication Ticket Generation with Fixed User Data | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Use of Default Encryption Settings May Lead to Vulnerabilities | High | 8% (1/12) | 0.90 | model inconsistency |
| Hardcoded Salt Reduces Key Derivation Security | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Improper JSON Encoding May Allow Script Injection | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Unvalidated UserData in Forms Authentication Ticket | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Privilege Escalation via Tampered Authentication Tickets | High | 8% (1/12) | 0.90 | model inconsistency |
| Data Exfiltration Through Unsanitized JSON Output | High | 8% (1/12) | 0.85 | model inconsistency |
| Hardcoded Credentials in Encoder.cs | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Hardcoded Salt in Key Derivation | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Potential Injection in JSON Serialization | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Predictable Salt in Key Derivation | High | 8% (1/12) | 0.90 | model inconsistency |
| Use of Deprecated Encryption Algorithm | High | 8% (1/12) | 0.90 | model inconsistency |
| Hardcoded Salt Value as Potential Secret Exposure | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Potential Data Table JSON Injection Risk | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Hardcoded Salt in Encryption | High | 8% (1/12) | 0.95 | model inconsistency |
| Potential Insecure Block Size Configuration | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Use of Deprecated Cryptographic Algorithm | High | 8% (1/12) | 0.95 | model inconsistency |
| Hardcoded Salt Value | High | 8% (1/12) | 0.90 | model inconsistency |
| Insecure Key Derivation Due to Predictable Salt | High | 8% (1/12) | 0.90 | model inconsistency |
| Hardcoded Salt in Encryption Key Derivation | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Potential Insecure Direct Object Reference in Authentication | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Use of Deprecated RijndaelManaged Algorithm | High | 8% (1/12) | 0.95 | model inconsistency |
| Hardcoded Salt in Key Derivation Process | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Insecure Session Token Handling via FormsAuthenticationTicket | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Use of Deprecated Encryption Algorithm (RijndaelManaged) | High | 17% (2/12) | 0.93 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 4.5 | 0.4 | 3.9 | 5.0 | 0 | 0 |
| threat | 11.3 | 1.0 | 10.2 | 13.7 | 0 | 0 |
| hypotheses | 12.0 | 1.9 | 9.8 | 16.7 | 0 | 0 |
| evidence | 17.0 | 3.7 | 13.1 | 27.7 | 0 | 0 |
| fix | 16.8 | 5.0 | 12.8 | 31.5 | 0 | 0 |
| gate | 10.0 | 2.6 | 7.0 | 15.1 | 0 | 0 |
| pre_scan | 7.5 | 1.0 | 5.9 | 9.8 | 0 | 0 |

**Mean total elapsed per run:** 79s  |  Min: 67s  |  Max: 119s


---

## File: `WebGoat_App_Code_Settings.cs`

**Runs with this file:** 12  |  **Gate consistency:** 75%  |  **Verdict distribution:** FAIL: 2  NEEDS_HUMAN: 9  PASS: 1

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Sensitive Environment Variables Logged | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Potential Information Disclosure via Debug Logging | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Exposure of Sensitive Environment Variables in Logs | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Logging of Sensitive Environment Variables | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Information Disclosure via Debug Logs | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Information Disclosure via Unrestricted Environment Variable Logging | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Information Disclosure via Debug Logging | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Information Disclosure via Debug Logging and Database Access | Critical | 8% (1/12) | 0.85 | model inconsistency |
| Debug Logging of Environment Variables | Medium | 17% (2/12) | 0.90 | model inconsistency |
| Debug Logging of Sensitive Environment Variables | Medium | 17% (2/12) | 0.90 | model inconsistency |
| Information Disclosure in Debug Logs | Medium | 17% (2/12) | 0.90 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 4.2 | 1.0 | 1.4 | 5.4 | 0 | 0 |
| threat | 9.9 | 1.0 | 8.7 | 12.1 | 0 | 0 |
| hypotheses | 8.4 | 1.7 | 6.6 | 11.8 | 0 | 0 |
| evidence | 9.1 | 1.6 | 7.1 | 12.3 | 0 | 0 |
| fix | 6.0 | 1.5 | 4.9 | 9.8 | 0 | 0 |
| gate | 6.2 | 1.1 | 4.7 | 8.3 | 0 | 0 |
| pre_scan | 3.4 | 0.1 | 3.2 | 3.7 | 0 | 0 |

**Mean total elapsed per run:** 47s  |  Min: 41s  |  Max: 56s


---

## File: `WebGoat_App_Code_Util.cs`

**Runs with this file:** 12  |  **Gate consistency:** 67%  |  **Verdict distribution:** FAIL: 8  NEEDS_HUMAN: 4

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| OS Command Injection via Process StartInfo | High | 8% (1/12) | 0.95 | model inconsistency |
| Sensitive Data Exposure in Logs via Input File Processing | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Command Injection via Shell Execution with Unsanitized Input | High | 8% (1/12) | 0.95 | model inconsistency |
| Potential Sensitive Data Exposure via Log Redaction Inadequacy | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Potential Command Execution via StandardInput | High | 8% (1/12) | 0.90 | model inconsistency |
| Missing Authorization Check on Process Execution | High | 8% (1/12) | 0.80 | model inconsistency |
| Command Execution via StandardInput in RunProcessWithInput | High | 8% (1/12) | 0.90 | model inconsistency |
| OS Command Injection via ProcessStartInfo.FileName | High | 8% (1/12) | 0.90 | model inconsistency |
| OS Command Injection via ProcessStartInfo.Arguments | High | 8% (1/12) | 0.90 | model inconsistency |
| Sensitive Data Exposure in Log Files | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Command Injection via Process.Start with User Input | High | 8% (1/12) | 0.95 | model inconsistency |
| OS Command Injection via StandardInput Stream | High | 8% (1/12) | 0.90 | model inconsistency |
| Information Disclosure via Unsanitized Logging | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Potential OS Command Injection via Process.Start | High | 8% (1/12) | 0.90 | model inconsistency |
| Command Injection via StandardInput Write | High | 8% (1/12) | 0.90 | model inconsistency |
| Chained Command Injection Exploitation | Critical | 8% (1/12) | 0.85 | model inconsistency |
| OS Command Injection via ProcessStartInfo | Critical | 8% (1/12) | 0.95 | model inconsistency |
| Sensitive Data Exposure in Logs | High | 8% (1/12) | 0.85 | model inconsistency |
| Uncontrolled Data Written to Process Standard Input | High | 8% (1/12) | 0.90 | model inconsistency |
| Sensitive Data Exposure in Logs via Process Execution | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Chained Command Injection via ProcessStartInfo and StandardInput | High | 8% (1/12) | 0.80 | model inconsistency |
| Sensitive Data Exposure via Logging of Input File Contents | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Command Line Argument Injection via User Input File | High | 8% (1/12) | 0.90 | model inconsistency |
| OS Command Injection via Process.StartInfo | High | 17% (2/12) | 0.95 | model inconsistency |
| OS Command Injection via ProcessStartInfo | High | 17% (2/12) | 0.95 | model inconsistency |
| Potential OS Command Injection via ProcessStartInfo | High | 25% (3/12) | 0.90 | model inconsistency |
| Sensitive Data Exposure in Logs | Medium | 33% (4/12) | 0.80 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 3.6 | 0.4 | 3.1 | 4.3 | 0 | 0 |
| threat | 10.0 | 1.4 | 7.9 | 12.5 | 0 | 0 |
| hypotheses | 9.7 | 1.0 | 8.2 | 11.1 | 0 | 0 |
| evidence | 13.5 | 2.6 | 9.9 | 18.6 | 0 | 0 |
| fix | 15.5 | 6.1 | 9.2 | 32.1 | 0 | 0 |
| gate | 8.6 | 1.7 | 6.4 | 11.6 | 0 | 0 |
| pre_scan | 5.1 | 0.9 | 3.4 | 6.5 | 0 | 0 |

**Mean total elapsed per run:** 66s  |  Min: 51s  |  Max: 92s


---

## File: `WebGoat_App_Code_VeryWeakRandom.cs`

**Runs with this file:** 12  |  **Gate consistency:** 92%  |  **Verdict distribution:** FAIL: 1  NEEDS_HUMAN: 11

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Use of Weak Random Number Generator for Session Token Creation | High | 8% (1/12) | 0.30 | borderline confidence |
| Use of Insecure Random Number Generator in Session Management | High | 8% (1/12) | 0.90 | model inconsistency |
| Use of Cryptographically Weak Random Number Generator | High | 8% (1/12) | 0.95 | model inconsistency |
| Use of Predictable Random Generator | High | 8% (1/12) | 0.95 | model inconsistency |
| Insecure Random Number Generation Used for Security Purposes | High | 8% (1/12) | 0.95 | model inconsistency |
| Use of Very Weak Random Number Generator in Cryptographic Operations | High | 8% (1/12) | 0.95 | model inconsistency |
| Use of Weak Random Number Generator | High | 8% (1/12) | 0.95 | model inconsistency |
| Hardcoded Secrets in VeryWeakRandom Class | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Use of Very Weak Random Number Generator | High | 33% (4/12) | 0.95 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 3.1 | 0.3 | 2.7 | 3.5 | 0 | 0 |
| threat | 9.4 | 1.7 | 4.7 | 10.8 | 0 | 0 |
| hypotheses | 8.0 | 2.2 | 3.5 | 10.9 | 0 | 0 |
| evidence | 9.8 | 2.0 | 5.5 | 12.1 | 0 | 0 |
| fix | 7.3 | 0.9 | 5.9 | 9.4 | 0 | 0 |
| gate | 7.2 | 1.3 | 4.8 | 9.1 | 0 | 0 |
| pre_scan | 3.1 | 0.1 | 3.0 | 3.4 | 0 | 0 |

**Mean total elapsed per run:** 48s  |  Min: 32s  |  Max: 53s


---

## File: `WebGoat_App_Code_WeakMessageDigest.cs`

**Runs with this file:** 12  |  **Gate consistency:** 83%  |  **Verdict distribution:** FAIL: 2  NEEDS_HUMAN: 10

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Use of Weak Hashing Algorithm | High | 8% (1/12) | 0.95 | model inconsistency |
| Custom Weak Hash Implementation | High | 8% (1/12) | 0.95 | model inconsistency |
| Weak Message Digest Used in Authentication Context | High | 8% (1/12) | 0.30 | borderline confidence |
| Potential Data Integrity Compromise via Weak Digest | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Misuse of Weak Digest in Business Logic Validation | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Risk of Information Disclosure via Weak Digest Usage | Low | 8% (1/12) | 0.30 | borderline confidence |
| Custom Weak Hashing Implementation | High | 8% (1/12) | 0.95 | model inconsistency |
| Use of Weak Cryptographic Hash Function for Data Integrity | High | 8% (1/12) | 0.95 | model inconsistency |
| Use of Weak Cryptographic Algorithm in Authentication Flow | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential Data Integrity Compromise via Predictable Digests | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Use of Weak Cryptographic Algorithm in Message Digest | High | 17% (2/12) | 0.95 | model inconsistency |
| Use of Weak Cryptographic Algorithm | High | 17% (2/12) | 0.95 | model inconsistency |
| Use of Weak Cryptographic Algorithm for Message Digest | High | 17% (2/12) | 0.95 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 3.3 | 0.3 | 2.9 | 3.7 | 0 | 0 |
| threat | 8.8 | 1.7 | 5.7 | 10.7 | 0 | 0 |
| hypotheses | 7.6 | 1.7 | 5.1 | 10.3 | 0 | 0 |
| evidence | 11.0 | 2.9 | 7.7 | 17.8 | 0 | 0 |
| fix | 9.6 | 4.3 | 7.3 | 22.5 | 0 | 0 |
| gate | 7.1 | 1.6 | 5.5 | 11.7 | 0 | 0 |
| pre_scan | 3.3 | 0.1 | 3.1 | 3.5 | 0 | 0 |

**Mean total elapsed per run:** 51s  |  Min: 40s  |  Max: 76s


---

## File: `WebGoat_App_Code_WeakRandom.cs`

**Runs with this file:** 12  |  **Gate consistency:** 58%  |  **Verdict distribution:** FAIL: 5  NEEDS_HUMAN: 7

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Use of Weak Random Number Generator in Security-Sensitive Contexts | High | 8% (1/12) | 0.95 | model inconsistency |
| Use of Weak Random Number Generator in Session Token Generation | High | 8% (1/12) | 0.30 | borderline confidence |
| Use of Weak Random Number Generator in CSRF Token Generation | High | 8% (1/12) | 0.30 | borderline confidence |
| Use of Weak Random Number Generator in Cryptographic Key Generation | Critical | 8% (1/12) | 0.30 | borderline confidence |
| Predictable Random Values Enable Combined Session Hijacking and CSRF Bypass | Critical | 8% (1/12) | 0.30 | borderline confidence |
| Potential Exposure of Secrets Through Weak Random Number Usage | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Predictable Random Number Generation Used in Security Context | High | 8% (1/12) | 0.95 | model inconsistency |
| Use of Predictable Random Number Generator in Session Management | High | 8% (1/12) | 0.90 | model inconsistency |
| Session Hijacking Through Predictable Session ID Generation | High | 8% (1/12) | 0.90 | model inconsistency |
| Insecure Random Number Generation Used for Security Token Generation | High | 8% (1/12) | 0.95 | model inconsistency |
| Use of Insecure Random Number Generator for Session Tokens | High | 8% (1/12) | 0.30 | borderline confidence |
| Predictable CSRF Tokens Due to Weak Random Generation | High | 8% (1/12) | 0.30 | borderline confidence |
| Cryptographic Key Generation Vulnerable to Predictability | High | 8% (1/12) | 0.30 | borderline confidence |
| Denial of Service via Predictable Random Number Manipulation | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Session Hijacking Enabled by Predictable Random Generation | High | 8% (1/12) | 0.30 | borderline confidence |
| Use of Weak Random Number Generator in Security Context | High | 17% (2/12) | 0.95 | model inconsistency |
| Use of Weak Random Number Generator | High | 33% (4/12) | 0.95 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 3.2 | 0.3 | 2.7 | 3.6 | 0 | 0 |
| threat | 9.4 | 1.5 | 6.0 | 11.0 | 0 | 0 |
| hypotheses | 8.2 | 2.0 | 3.5 | 10.3 | 0 | 0 |
| evidence | 10.7 | 3.6 | 6.6 | 18.6 | 0 | 0 |
| fix | 9.4 | 5.2 | 5.1 | 22.8 | 0 | 0 |
| gate | 7.9 | 2.6 | 6.0 | 13.5 | 0 | 0 |
| pre_scan | 3.1 | 0.1 | 3.0 | 3.4 | 0 | 0 |

**Mean total elapsed per run:** 52s  |  Min: 39s  |  Max: 82s


---

## File: `WebGoat_App_Data_XmlInjectionUsers.xml`

**Runs with this file:** 12  |  **Gate consistency:** 67%  |  **Verdict distribution:** FAIL: 4  NEEDS_HUMAN: 8

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| XML External Entity (XXE) Injection | High | 8% (1/12) | 0.85 | model inconsistency |
| Potential XXE Vulnerability in XML Parsing | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential XXE Injection in XML Parsing | High | 8% (1/12) | 0.85 | model inconsistency |
| XML External Entity (XXE) Injection Vulnerability | High | 42% (5/12) | 0.86 | model inconsistency |
| XML Injection Vulnerability | High | 42% (5/12) | 0.92 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 3.0 | 0.3 | 2.5 | 3.5 | 0 | 0 |
| threat | 6.8 | 1.9 | 4.8 | 10.2 | 0 | 0 |
| hypotheses | 6.0 | 2.4 | 3.6 | 9.5 | 0 | 0 |
| evidence | 6.9 | 2.8 | 3.9 | 11.9 | 0 | 0 |
| fix | 5.6 | 1.3 | 4.7 | 9.5 | 0 | 0 |
| gate | 5.7 | 1.1 | 4.4 | 7.9 | 0 | 0 |
| pre_scan | 3.3 | 0.2 | 3.0 | 3.8 | 0 | 0 |

**Mean total elapsed per run:** 38s  |  Min: 29s  |  Max: 51s


---

## File: `WebGoat_ChangePassword.aspx.cs`

**Runs with this file:** 12  |  **Gate consistency:** 67%  |  **Verdict distribution:** FAIL: 4  NEEDS_HUMAN: 8

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Potential Exposure of Sensitive Data in Page Inheritance | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Missing Authorization Check on Password Change Page | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential Exposure of Sensitive Data via Debug Mode or Error Handling | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Missing Authorization Check in Password Change Module | High | 8% (1/12) | 0.90 | model inconsistency |
| Missing Input Validation and CSRF Protection in ChangePassword Page | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential Session Management Vulnerability | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Potential Exposure of Sensitive Data in Page Implementation | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Missing Authorization Check | High | 8% (1/12) | 0.90 | model inconsistency |
| Missing Authorization Check in Password Change Page | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential Exposure of Sensitive User Data via Password Change Page | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Exposure of Sensitive User Data in Page Context | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Missing Authorization Check in Password Change Page | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential Exposure of Sensitive Functionality Without Input Validation | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Potential Exposure of Sensitive Functionality | Medium | 17% (2/12) | 0.90 | model inconsistency |
| Missing Authorization Check in Change Password Page | High | 17% (2/12) | 0.90 | model inconsistency |
| Potential Exposure of Sensitive User Data | Medium | 17% (2/12) | 0.60 | borderline confidence |
| Missing Authorization Check on Password Change Functionality | High | 42% (5/12) | 0.78 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 4.1 | 0.2 | 3.7 | 4.5 | 0 | 0 |
| threat | 9.0 | 1.3 | 7.1 | 10.8 | 0 | 0 |
| hypotheses | 9.8 | 1.5 | 6.9 | 12.0 | 0 | 0 |
| evidence | 9.8 | 1.1 | 7.7 | 11.9 | 0 | 0 |
| fix | 9.2 | 2.8 | 5.1 | 12.9 | 0 | 0 |
| gate | 7.3 | 1.0 | 5.9 | 8.8 | 0 | 0 |
| pre_scan | 2.4 | 0.1 | 2.3 | 2.6 | 0 | 0 |

**Mean total elapsed per run:** 52s  |  Min: 43s  |  Max: 60s


---

## File: `WebGoat_ChangePassword.aspx.designer.cs`

**Runs with this file:** 12  |  **Gate consistency:** 83%  |  **Verdict distribution:** FAIL: 2  NEEDS_HUMAN: 10

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Potential Insecure Error Handling in Password Change | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Hardcoded Credentials in Password Change Logic | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Insecure Error Handling in Password Change Flow | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Hardcoded Credentials in Web Configuration | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Verbose Error Handling in Password Change Page | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Authentication Bypass Risk in Password Change Functionality | Critical | 8% (1/12) | 0.30 | borderline confidence |
| Potential for Password Input Injection | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Missing Authorization Check on Password Change Functionality | High | 8% (1/12) | 0.30 | borderline confidence |
| Potential Exposure of Password Change Control with No Logging or Error Handling | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Exposure of Password Change Failure Messages | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Information Disclosure in Password Change Failure Messages | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Exposure of Sensitive Data in UI Controls | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential SQL Injection via Password Change Implementation | High | 8% (1/12) | 0.30 | borderline confidence |
| Hardcoded Password Policies or Secrets in Page Implementation | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Missing Authorization Check on Password Change | High | 8% (1/12) | 0.30 | borderline confidence |
| Potential SQL Injection via ChangePassword Control | High | 8% (1/12) | 0.30 | borderline confidence |
| Hardcoded Encryption Keys or Passwords | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential SQL Injection in Password Change Logic | High | 8% (1/12) | 0.30 | borderline confidence |
| Verbose Error Handling in Password Change Control | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Missing Authorization Check on Password Change | High | 33% (4/12) | 0.30 | borderline confidence |
| Missing Authorization Check on Password Change Functionality | High | 42% (5/12) | 0.30 | borderline confidence |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 3.2 | 0.2 | 3.0 | 3.7 | 0 | 0 |
| threat | 8.7 | 1.0 | 7.1 | 10.4 | 0 | 0 |
| hypotheses | 7.7 | 1.1 | 6.0 | 9.5 | 0 | 0 |
| evidence | 9.3 | 1.8 | 6.3 | 11.8 | 0 | 0 |
| fix | 12.2 | 2.0 | 9.5 | 15.3 | 0 | 0 |
| gate | 8.4 | 1.5 | 4.9 | 10.6 | 0 | 0 |
| pre_scan | 2.8 | 0.4 | 2.4 | 3.5 | 0 | 0 |

**Mean total elapsed per run:** 52s  |  Min: 41s  |  Max: 61s


---

## File: `WebGoat_Code_DatabaseUtilities.cs`

**Runs with this file:** 12  |  **Gate consistency:** 92%  |  **Verdict distribution:** FAIL: 11  approve: 1

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Unauthorized Access to Database Operations | High | 8% (1/12) | 0.80 | model inconsistency |
| Potential Data Exposure via Unrestricted Database Access | High | 8% (1/12) | 0.80 | model inconsistency |
| Unauthorized Access to Database Operations Without Authentication | High | 8% (1/12) | 0.90 | model inconsistency |
| SQL Injection in DatabaseUtilities.cs - Combined with Unauthorized Access | Critical | 8% (1/12) | 0.95 | model inconsistency |
| Potential Data Exposure via SQL Injection | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential data leakage from user email and posting data due to SQL injection vulnerabilities | High | 8% (1/12) | 0.95 | model inconsistency |
| Unauthorized Data Retrieval via SQL Injection | High | 8% (1/12) | 0.95 | model inconsistency |
| Data Manipulation in MailingList Table via SQL Injection | Medium | 8% (1/12) | 0.95 | model inconsistency |
| Fake Posting Creation via SQL Injection | Medium | 8% (1/12) | 0.95 | model inconsistency |
| Multiple SQL Injection vulnerabilities in DatabaseUtilities.cs | High | 8% (1/12) | 0.95 | model inconsistency |
| Lack of input validation and sanitization in database utility methods | Medium | 8% (1/12) | 0.95 | model inconsistency |
| Unvalidated Input Leading to Potential Data Exposure | High | 8% (1/12) | 0.95 | model inconsistency |
| Lack of Authentication and Authorization Controls in DatabaseUtilities | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential Exposure of User Data Due to Lack of Input Validation and SQL Injection | High | 8% (1/12) | 0.90 | model inconsistency |
| SQL Injection via Direct String Concatenation in GetEmailByUserID | High | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection via Direct String Concatenation in GetMailingListInfoByEmailAddress | High | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection via Direct String Concatenation in AddToMailingList | High | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection via Direct String Concatenation in AddNewPosting | High | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection via Direct String Concatenation in GetPostingByID | High | 8% (1/12) | 0.95 | model inconsistency |
| Denial of Service via SQL Injection | High | 8% (1/12) | 0.90 | model inconsistency |
| Unauthorized Data Exposure via Direct Query Construction | High | 8% (1/12) | 0.90 | model inconsistency |
| SQL Injection Vulnerability in GetEmailByUserID Method | High | 33% (4/12) | 0.95 | model inconsistency |
| SQL Injection Vulnerability in GetMailingListInfoByEmailAddress Method | High | 33% (4/12) | 0.95 | model inconsistency |
| SQL Injection Vulnerability in AddToMailingList Method | High | 33% (4/12) | 0.95 | model inconsistency |
| SQL Injection Vulnerability in AddNewPosting Method | High | 33% (4/12) | 0.95 | model inconsistency |
| SQL Injection Vulnerability in GetPostingByID Method | High | 33% (4/12) | 0.95 | model inconsistency |
| SQL Injection in GetEmailByUserID method | High | 58% (7/12) | 0.95 | model inconsistency |
| SQL Injection in GetMailingListInfoByEmailAddress method | High | 58% (7/12) | 0.95 | model inconsistency |
| SQL Injection in AddToMailingList method | High | 58% (7/12) | 0.95 | model inconsistency |
| SQL Injection in AddNewPosting method | High | 58% (7/12) | 0.95 | model inconsistency |
| SQL Injection in GetPostingByID method | High | 58% (7/12) | 0.95 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 4.7 | 0.6 | 4.1 | 6.5 | 0 | 0 |
| threat | 17.0 | 1.5 | 13.8 | 19.0 | 0 | 0 |
| hypotheses | 16.1 | 2.0 | 12.2 | 18.7 | 0 | 0 |
| evidence | 29.4 | 6.1 | 21.0 | 38.0 | 0 | 0 |
| fix | 31.4 | 11.4 | 21.1 | 64.2 | 0 | 0 |
| gate | 16.5 | 5.8 | 0.8 | 24.7 | 0 | 0 |
| pre_scan | 10.8 | 0.6 | 9.5 | 11.6 | 0 | 0 |

**Mean total elapsed per run:** 126s  |  Min: 103s  |  Max: 151s


---

## File: `WebGoat_Code_IOHelper.cs`

**Runs with this file:** 12  |  **Gate consistency:** 58%  |  **Verdict distribution:** FAIL: 7  NEEDS_HUMAN: 5

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Path Traversal via File Path Manipulation | High | 8% (1/12) | 0.90 | model inconsistency |
| Directory Traversal via File Path Manipulation | High | 8% (1/12) | 0.90 | model inconsistency |
| Sensitive Data Exposure via Direct File Read Access | High | 8% (1/12) | 0.90 | model inconsistency |
| Path Traversal Vulnerability in File Reading Utility | High | 8% (1/12) | 0.90 | model inconsistency |
| Insecure Direct Object Reference (IDOR) in ReadAllFromFile | High | 33% (4/12) | 0.93 | model inconsistency |
| Insecure Direct Object Reference (IDOR) in file reading function | High | 50% (6/12) | 0.92 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 3.2 | 0.2 | 2.7 | 3.5 | 0 | 0 |
| threat | 7.2 | 1.5 | 5.0 | 9.8 | 0 | 0 |
| hypotheses | 6.7 | 1.8 | 3.5 | 9.3 | 0 | 0 |
| evidence | 7.0 | 1.7 | 4.1 | 9.7 | 0 | 0 |
| fix | 8.8 | 4.2 | 6.7 | 22.0 | 0 | 0 |
| gate | 5.6 | 1.1 | 4.7 | 8.7 | 0 | 0 |
| pre_scan | 3.1 | 0.1 | 2.8 | 3.4 | 0 | 0 |

**Mean total elapsed per run:** 42s  |  Min: 31s  |  Max: 62s


---

## File: `WebGoat_Code_SQLiteMembershipProvider.cs`

**Runs with this file:** 12  |  **Gate consistency:** 83%  |  **Verdict distribution:** FAIL: 10  NEEDS_HUMAN: 2

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Use of SHA1 Hashing Algorithm for Password Storage | High | 8% (1/12) | 0.95 | model inconsistency |
| Potential SQL Injection Due to Inconsistent Parameterization in Dynamic Queries | High | 8% (1/12) | 0.90 | model inconsistency |
| Use of SHA1 Hashing Without Proper Salt Implementation | High | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection Through String Concatenation | High | 8% (1/12) | 0.90 | model inconsistency |
| Missing Authorization on User Data Retrieval | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Insecure Default Password Policies | Low | 8% (1/12) | 0.70 | model inconsistency |
| Potential User Enumeration via Email Lookup | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Hardcoded Security Configuration Values | Medium | 8% (1/12) | 0.85 | model inconsistency |
| SQL Injection Vulnerability in User Lookup Methods | High | 8% (1/12) | 0.90 | model inconsistency |
| Use of SHA1 for Password Hashing | High | 8% (1/12) | 0.95 | model inconsistency |
| Missing Authorization Check in Email Lookup | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Hardcoded Database Path in Connection String | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Potential Exposure of User Email Addresses | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Use of Insecure SHA1 Hashing for Password Storage | High | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection Vulnerability in GetApplicationId Method | High | 8% (1/12) | 0.90 | model inconsistency |
| Missing Authorization Controls in User Management Functions | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Hardcoded or Misconfigured Connection String Handling | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Use of Insecure Password Hashing Algorithm | High | 8% (1/12) | 0.95 | model inconsistency |
| Potential SQL Injection Vulnerability via String Concatenation | High | 8% (1/12) | 0.85 | model inconsistency |
| Hardcoded Constants in Membership Provider Configuration | Medium | 8% (1/12) | 0.75 | model inconsistency |
| Use of Weak Hashing Algorithm (MD5) for Password Storage | High | 8% (1/12) | 0.90 | model inconsistency |
| Weak Password Hashing Algorithm Used in Membership Provider | High | 8% (1/12) | 0.90 | model inconsistency |
| SQL Injection Vulnerability in Dynamic Query Construction | High | 8% (1/12) | 0.90 | model inconsistency |
| Insecure Random Number Generation for Salt Values | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Missing Authorization Checks in Database Access Methods | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Use of Weak Password Hashing Algorithm in Membership Provider | High | 8% (1/12) | 0.95 | model inconsistency |
| Weak Password Hashing Algorithm Used | High | 17% (2/12) | 0.93 | model inconsistency |
| Use of Weak Hashing Algorithm for Password Storage | High | 17% (2/12) | 0.95 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 6.8 | 0.8 | 5.8 | 8.8 | 0 | 0 |
| threat | 11.4 | 1.7 | 7.9 | 13.8 | 0 | 0 |
| hypotheses | 10.8 | 1.6 | 8.1 | 13.6 | 0 | 0 |
| evidence | 16.8 | 3.2 | 10.2 | 20.1 | 0 | 0 |
| fix | 15.6 | 6.4 | 7.2 | 24.3 | 0 | 0 |
| gate | 9.5 | 2.4 | 6.4 | 12.9 | 0 | 0 |
| pre_scan | 7.3 | 1.9 | 4.4 | 10.0 | 0 | 0 |

**Mean total elapsed per run:** 78s  |  Min: 50s  |  Max: 97s


---

## File: `WebGoat_Code_SQLiteProfileProvider.cs`

**Runs with this file:** 12  |  **Gate consistency:** 83%  |  **Verdict distribution:** FAIL: 10  NEEDS_HUMAN: 2

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Use of BinaryFormatter in Profile Property Serialization | Critical | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection Vulnerability via String Concatenation | High | 8% (1/12) | 0.90 | model inconsistency |
| BinaryFormatter Usage in Profile Provider | High | 8% (1/12) | 0.95 | model inconsistency |
| Potential SQL Injection in Profile Queries | High | 8% (1/12) | 0.90 | model inconsistency |
| Use of BinaryFormatter for deserialization | High | 8% (1/12) | 0.95 | model inconsistency |
| Potential SQL injection via string concatenation | High | 8% (1/12) | 0.85 | model inconsistency |
| Potential SQL Injection via Dynamic Query Building | High | 8% (1/12) | 0.90 | model inconsistency |
| Missing Encryption for Profile Data | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Insecure Deserialization via BinaryFormatter in Profile Provider | High | 8% (1/12) | 0.95 | model inconsistency |
| Use of BinaryFormatter in profile serialization | Critical | 8% (1/12) | 0.95 | model inconsistency |
| SQL Injection vulnerability via user-controlled input | Critical | 8% (1/12) | 0.90 | model inconsistency |
| Potential insecure direct object reference | High | 8% (1/12) | 0.75 | model inconsistency |
| Potential SQL Injection in GetPropertyValuesFromDatabase method | High | 8% (1/12) | 0.75 | model inconsistency |
| Insecure Deserialization via BinaryFormatter | High | 17% (2/12) | 0.95 | model inconsistency |
| Use of BinaryFormatter in profile serialization | High | 17% (2/12) | 0.95 | model inconsistency |
| Use of BinaryFormatter in Profile Provider | High | 17% (2/12) | 0.95 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 6.0 | 0.5 | 5.2 | 6.7 | 0 | 0 |
| threat | 9.6 | 2.8 | 1.2 | 12.7 | 0 | 0 |
| hypotheses | 10.9 | 1.0 | 9.5 | 12.9 | 0 | 0 |
| evidence | 15.4 | 2.7 | 10.5 | 19.7 | 0 | 0 |
| fix | 13.5 | 6.9 | 9.2 | 27.9 | 0 | 0 |
| gate | 8.1 | 2.2 | 5.4 | 13.0 | 0 | 0 |
| pre_scan | 6.1 | 1.9 | 4.5 | 10.0 | 0 | 0 |

**Mean total elapsed per run:** 70s  |  Min: 55s  |  Max: 98s


---

## File: `WebGoat_Code_SQLiteRoleProvider.cs`

**Runs with this file:** 12  |  **Gate consistency:** 83%  |  **Verdict distribution:** FAIL: 10  NEEDS_HUMAN: 2

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Incomplete Role Management Authorization Chain | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential SQL Injection Vulnerability in Dynamic Query Building | High | 8% (1/12) | 0.85 | model inconsistency |
| Insecure Direct Object Reference in FindUsersInRole | High | 8% (1/12) | 0.90 | model inconsistency |
| Insecure Configuration Handling in Initialize Method | Medium | 8% (1/12) | 0.75 | model inconsistency |
| SQL Injection Vulnerability via String Concatenation | High | 8% (1/12) | 0.85 | model inconsistency |
| Insecure Default Configuration for Database Connection String | Medium | 8% (1/12) | 0.75 | model inconsistency |
| Insecure Direct Object Reference in Role Queries | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Privilege Escalation through Chained Threats | Critical | 8% (1/12) | 0.85 | model inconsistency |
| Potential SQL Injection via Dynamic Query Construction | High | 8% (1/12) | 0.85 | model inconsistency |
| Insufficient Validation of Database Connection Configuration | Medium | 8% (1/12) | 0.70 | model inconsistency |
| Insecure Direct Object Reference in Role Existence Validation | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Missing Authorization Check in RemoveUsersFromRoles Method | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential SQL Injection in Role Management Queries | Critical | 8% (1/12) | 0.90 | model inconsistency |
| Insecure Error Handling with Exception Rethrowing | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Insecure Direct Object Reference in Role Management Methods | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential SQL Injection Vulnerability in Role Management Methods | High | 8% (1/12) | 0.80 | model inconsistency |
| Potential SQL Injection Vulnerability in Role Provider | High | 8% (1/12) | 0.90 | model inconsistency |
| Privilege Escalation via Role Management API | Critical | 8% (1/12) | 0.90 | model inconsistency |
| Insecure Direct Object Reference in Role Operations | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Missing Authorization Checks in Role Management Methods | High | 17% (2/12) | 0.93 | model inconsistency |
| Missing Authorization in Role Management Methods | High | 17% (2/12) | 0.90 | model inconsistency |
| SQL Injection Vulnerability via String Concatenation | Critical | 17% (2/12) | 0.93 | model inconsistency |
| Missing Authorization Controls in Role Management Operations | High | 17% (2/12) | 0.90 | model inconsistency |
| Missing Authorization Check in Role Management Methods | High | 25% (3/12) | 0.92 | model inconsistency |
| Missing Authorization Check in AddUsersToRoles Method | High | 33% (4/12) | 0.90 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 6.3 | 0.5 | 5.5 | 7.2 | 0 | 0 |
| threat | 11.0 | 1.6 | 7.9 | 13.9 | 0 | 0 |
| hypotheses | 10.2 | 1.4 | 7.6 | 12.9 | 0 | 0 |
| evidence | 17.9 | 3.8 | 12.4 | 23.8 | 0 | 0 |
| fix | 22.9 | 8.1 | 9.9 | 39.3 | 0 | 0 |
| gate | 9.2 | 1.6 | 6.3 | 11.9 | 0 | 0 |
| pre_scan | 7.5 | 1.6 | 4.8 | 9.0 | 0 | 0 |

**Mean total elapsed per run:** 85s  |  Min: 63s  |  Max: 110s


---

## File: `WebGoat_Configuration_Default.config`

**Runs with this file:** 12  |  **Gate consistency:** 67%  |  **Verdict distribution:** NEEDS_HUMAN: 8  PASS: 4

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Hardcoded Database Type Configuration | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Hardcoded Database Configuration | Low | 8% (1/12) | 0.70 | model inconsistency |
| Hardcoded Database Configuration | Medium | 50% (6/12) | 0.90 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 3.0 | 0.2 | 2.7 | 3.5 | 0 | 0 |
| threat | 5.5 | 1.6 | 4.2 | 9.0 | 0 | 0 |
| hypotheses | 4.6 | 1.8 | 3.3 | 8.0 | 0 | 0 |
| evidence | 3.9 | 1.3 | 3.0 | 6.3 | 0 | 0 |
| fix | 4.3 | 1.4 | 1.2 | 5.8 | 0 | 0 |
| gate | 4.2 | 0.5 | 3.4 | 5.0 | 0 | 0 |
| pre_scan | 1.9 | 0.1 | 1.8 | 2.1 | 0 | 0 |

**Mean total elapsed per run:** 27s  |  Min: 21s  |  Max: 38s


---

## File: `WebGoat_Content_About.aspx.cs`

**Runs with this file:** 12  |  **Gate consistency:** 42%  |  **Verdict distribution:** FAIL: 3  NEEDS_HUMAN: 5  PASS: 4

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Potential Missing Authorization Check | Medium | 100% (12/12) | [0.76, 1.00] | 0.85 | 0.173 |

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Unauthenticated Access to About Page Allows Unauthorized Data Exposure | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Hardcoded Configuration Values | Medium | 8% (1/12) | 0.30 | borderline confidence |
| No Explicit Security Controls | Low | 8% (1/12) | 0.80 | model inconsistency |
| Verbose Error Handling Potential | Low | 8% (1/12) | 0.85 | model inconsistency |
| Verbose Error Handling | Low | 17% (2/12) | 0.82 | model inconsistency |
| Verbose Error Handling Possible | Low | 33% (4/12) | 0.70 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 4.0 | 0.2 | 3.8 | 4.5 | 0 | 0 |
| threat | 8.2 | 1.2 | 7.0 | 11.3 | 0 | 0 |
| hypotheses | 6.9 | 1.8 | 4.7 | 10.6 | 0 | 0 |
| evidence | 7.1 | 2.0 | 5.1 | 11.1 | 0 | 0 |
| fix | 8.3 | 2.0 | 4.4 | 10.4 | 0 | 0 |
| gate | 5.3 | 1.3 | 3.6 | 7.1 | 0 | 0 |
| pre_scan | 2.2 | 0.2 | 2.0 | 2.8 | 0 | 0 |

**Mean total elapsed per run:** 42s  |  Min: 35s  |  Max: 56s


---

## File: `WebGoat_Content_About.aspx.designer.cs`

**Runs with this file:** 12  |  **Gate consistency:** 75%  |  **Verdict distribution:** NEEDS_HUMAN: 9  PASS: 2  UNKNOWN: 1

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Potential Exposure of Sensitive Data in UI Controls | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Missing Authorization Checks on UI Elements | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Exposure of Sensitive UI Elements | Medium | 8% (1/12) | 0.50 | borderline confidence |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 3.1 | 0.1 | 2.9 | 3.3 | 0 | 0 |
| threat | 4.6 | 1.1 | 2.4 | 7.1 | 0 | 0 |
| hypotheses | 4.4 | 1.4 | 3.2 | 8.7 | 0 | 0 |
| evidence | 4.0 | 1.6 | 3.2 | 8.9 | 0 | 0 |
| fix | 2.8 | 2.7 | 1.2 | 9.5 | 0 | 0 |
| gate | 4.1 | 0.8 | 3.5 | 6.0 | 1 | 0 |
| pre_scan | 1.8 | 0.2 | 1.6 | 2.2 | 0 | 0 |

**Mean total elapsed per run:** 24s  |  Min: 16s  |  Max: 44s


---

## File: `WebGoat_Content_BasicAuth.aspx.cs`

**Runs with this file:** 12  |  **Gate consistency:** 58%  |  **Verdict distribution:** FAIL: 5  NEEDS_HUMAN: 7

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Missing Secure Flag on Authentication Cookies | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Unintended Access to Protected Functionality | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential Business Logic Flaw in Page Access Control | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Unauthorized Access to Authentication Page Due to Missing AuthZ Controls | High | 8% (1/12) | 0.90 | model inconsistency |
| Lack of Authentication Mechanism Implementation | High | 17% (2/12) | 0.90 | model inconsistency |
| Potential Missing Authentication Check | High | 25% (3/12) | 0.90 | model inconsistency |
| Potential Missing Authorization Check | Medium | 33% (4/12) | 0.90 | model inconsistency |
| Potential Missing Authorization Check | High | 42% (5/12) | 0.78 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 9.4 | 19.0 | 3.6 | 69.6 | 0 | 0 |
| threat | 20.8 | 41.3 | 5.1 | 151.7 | 0 | 0 |
| hypotheses | 31.8 | 80.5 | 3.9 | 287.2 | 0 | 0 |
| evidence | 32.1 | 80.5 | 5.7 | 287.7 | 0 | 0 |
| fix | 24.2 | 55.6 | 5.8 | 200.5 | 0 | 0 |
| gate | 24.1 | 54.8 | 4.6 | 198.0 | 0 | 0 |
| pre_scan | 7.5 | 18.7 | 1.5 | 66.8 | 0 | 0 |

**Mean total elapsed per run:** 150s  |  Min: 38s  |  Max: 1262s


---

## File: `WebGoat_Content_BasicAuth.aspx.designer.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 12

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Authentication Implementation Not Visible | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Possible Hardcoded Credentials or Configuration | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Possible Debug/Development Configuration | Low | 8% (1/12) | 0.90 | model inconsistency |
| Verbose Error Handling or Debug Output | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Missing Authentication Mechanism | High | 8% (1/12) | 0.30 | borderline confidence |
| Possible Authentication Bypass Vulnerability | Critical | 8% (1/12) | 0.30 | borderline confidence |
| Possible Hardcoded Credentials in Generated Code | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Missing Authorization Checks | High | 25% (3/12) | 0.30 | borderline confidence |
| Potential Missing Authorization Check | High | 25% (3/12) | 0.30 | borderline confidence |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 7.2 | 13.8 | 3.0 | 51.1 | 0 | 0 |
| threat | 19.2 | 42.9 | 3.3 | 155.5 | 0 | 0 |
| hypotheses | 22.6 | 55.3 | 5.8 | 198.2 | 0 | 0 |
| evidence | 19.6 | 44.0 | 4.4 | 159.1 | 0 | 0 |
| fix | 12.4 | 22.9 | 1.5 | 84.2 | 0 | 0 |
| gate | 14.9 | 29.8 | 4.7 | 109.6 | 0 | 0 |
| pre_scan | 6.8 | 14.7 | 2.0 | 53.3 | 0 | 0 |

**Mean total elapsed per run:** 103s  |  Min: 29s  |  Max: 811s


---

## File: `WebGoat_Content_Challenge1.aspx.cs`

**Runs with this file:** 12  |  **Gate consistency:** 75%  |  **Verdict distribution:** FAIL: 2  NEEDS_HUMAN: 9  PASS: 1

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Potential Missing Authorization Check | Medium | 83% (10/12) | [0.55, 0.95] | 0.90 | — |

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Verbose Error Handling or Debug Mode Enabled | Low | 8% (1/12) | 0.30 | borderline confidence |
| Verbose Error Handling Possible | Low | 8% (1/12) | 0.85 | model inconsistency |
| Potential for Unauthorized Access to Security Challenge Functionality | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Possible Insecure Direct Object Reference | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Missing Authorization Check in Challenge1 Page | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Potential Debug Information Exposure | Low | 8% (1/12) | 0.30 | borderline confidence |
| Verbose Error Handling | Low | 8% (1/12) | 0.90 | model inconsistency |
| Lack of Input Validation and Sanitization | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Unrestricted Access to Challenge1 Page Allows Business Logic Abuse | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Chained Attack Vector: Unauthorized Access + Injection Exploitation | High | 8% (1/12) | 0.90 | model inconsistency |
| Verbose Error Handling or Debug Mode | Low | 8% (1/12) | 0.30 | borderline confidence |
| Missing Authorization Check on Sensitive Operation | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential Insecure Direct Object Reference Vulnerability | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Debug or Verbose Error Exposure | Low | 17% (2/12) | 0.55 | borderline confidence |
| Lack of Input Validation | Medium | 17% (2/12) | 0.88 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 9.3 | 17.9 | 3.8 | 66.0 | 0 | 0 |
| threat | 22.6 | 47.5 | 6.9 | 173.3 | 0 | 0 |
| hypotheses | 26.4 | 59.8 | 5.2 | 216.1 | 0 | 0 |
| evidence | 25.2 | 55.3 | 6.2 | 200.8 | 0 | 0 |
| fix | 26.2 | 59.2 | 5.4 | 213.5 | 0 | 0 |
| gate | 22.3 | 55.5 | 4.9 | 198.6 | 0 | 0 |
| pre_scan | 7.2 | 15.0 | 2.1 | 54.7 | 0 | 0 |

**Mean total elapsed per run:** 139s  |  Min: 35s  |  Max: 1123s


---

## File: `WebGoat_Content_Challenge1.aspx.designer.cs`

**Runs with this file:** 12  |  **Gate consistency:** 75%  |  **Verdict distribution:** NEEDS_HUMAN: 9  PASS: 3

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Possible Debug/Development Artifact | Low | 8% (1/12) | 0.90 | model inconsistency |
| Potential Missing Authorization Check | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Verbose Error Handling or Debug Information | Low | 8% (1/12) | 0.30 | borderline confidence |
| Potential Missing Authorization Check | High | 8% (1/12) | 0.00 | borderline confidence |
| Hardcoded Configuration Values | Medium | 8% (1/12) | 0.00 | borderline confidence |
| Possible Debug/Verbose Error Exposure | Low | 8% (1/12) | 0.90 | model inconsistency |
| Possible Debug/Verbose Error Output | Low | 8% (1/12) | 0.80 | model inconsistency |
| Possible Debug/Verbose Error Exposure | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Verbose Error Handling or Debug Output | Low | 8% (1/12) | 0.90 | model inconsistency |
| Verbose Error Handling or Debug Mode Enabled | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Possible Debug/Development Configuration | Low | 17% (2/12) | 0.90 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 4.2 | 3.6 | 2.8 | 15.5 | 0 | 0 |
| threat | 23.6 | 60.5 | 2.4 | 215.5 | 0 | 0 |
| hypotheses | 24.1 | 60.7 | 5.4 | 216.7 | 0 | 0 |
| evidence | 20.7 | 48.8 | 4.5 | 175.7 | 0 | 0 |
| fix | 23.7 | 61.5 | 1.5 | 218.9 | 0 | 0 |
| gate | 23.6 | 63.0 | 3.6 | 223.6 | 0 | 0 |
| pre_scan | 6.7 | 14.5 | 2.2 | 52.6 | 0 | 0 |

**Mean total elapsed per run:** 127s  |  Min: 25s  |  Max: 1118s


---

## File: `WebGoat_Content_Challenge2.aspx.cs`

**Runs with this file:** 12  |  **Gate consistency:** 75%  |  **Verdict distribution:** FAIL: 3  NEEDS_HUMAN: 9

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Potential Missing Authorization Check | High | 8% (1/12) | 0.90 | model inconsistency |
| Lack of Input Validation on Challenge2 Page | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Possible Debug or Verbose Error Exposure | Low | 8% (1/12) | 0.85 | model inconsistency |
| Potential Debug/Verbose Error Exposure | Low | 8% (1/12) | 0.85 | model inconsistency |
| Lack of Input Validation | Medium | 8% (1/12) | 0.90 | model inconsistency |
| No Authentication Controls Implemented | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Potential Debug Mode or Verbose Error Output Enabled | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Information Disclosure in Page Structure | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Missing Authorization Check on Challenge2 Page | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential Input Validation Vulnerability in Challenge2 | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential Exception Handling Without Error Logging | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Verbose Error Handling | Low | 17% (2/12) | 0.82 | model inconsistency |
| Missing Authorization Check on Sensitive Operation | High | 17% (2/12) | 0.90 | model inconsistency |
| Potential Missing Authorization Check | Medium | 67% (8/12) | 0.90 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 9.8 | 19.4 | 3.9 | 71.4 | 0 | 0 |
| threat | 23.8 | 53.9 | 7.2 | 194.9 | 0 | 0 |
| hypotheses | 25.8 | 61.4 | 5.4 | 220.5 | 0 | 0 |
| evidence | 22.1 | 47.7 | 5.4 | 173.4 | 0 | 0 |
| fix | 17.1 | 24.7 | 5.6 | 95.0 | 0 | 0 |
| gate | 19.6 | 43.3 | 5.3 | 156.9 | 0 | 0 |
| pre_scan | 6.6 | 14.8 | 2.2 | 53.6 | 0 | 0 |

**Mean total elapsed per run:** 125s  |  Min: 36s  |  Max: 966s


---

## File: `WebGoat_Content_Challenge2.aspx.designer.cs`

**Runs with this file:** 12  |  **Gate consistency:** 75%  |  **Verdict distribution:** FAIL: 1  NEEDS_HUMAN: 9  PASS: 2

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Debug Information Exposure | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Possible Debug or Development Configuration | Low | 8% (1/12) | 0.90 | model inconsistency |
| Hardcoded File Path in Autogenerated Comment | Low | 8% (1/12) | 0.90 | model inconsistency |
| Potential Missing Authorization Checks | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Debug/Verbose Error Output Enabled | Low | 8% (1/12) | 0.30 | borderline confidence |
| Verbose Error Handling or Debug Information | Low | 8% (1/12) | 0.90 | model inconsistency |
| Possible Debug/Development Configuration | Low | 8% (1/12) | 0.90 | model inconsistency |
| Possible Debug/Verbose Logging Enabled | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Potential Missing Authorization Checks | High | 8% (1/12) | 0.30 | borderline confidence |
| Hardcoded Credentials in Source Code | High | 8% (1/12) | 0.30 | borderline confidence |
| Verbose Error Output or Debug Mode Enabled | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Possible Exposure of Sensitive Data in UI Controls | Low | 8% (1/12) | 0.30 | borderline confidence |
| Possible Debug or Verbose Error Output | Low | 8% (1/12) | 0.85 | model inconsistency |
| Potential Missing Authorization Check | Medium | 17% (2/12) | 0.60 | borderline confidence |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 6.3 | 11.1 | 2.7 | 41.7 | 0 | 0 |
| threat | 16.2 | 29.5 | 6.0 | 109.7 | 0 | 0 |
| hypotheses | 15.5 | 30.3 | 5.2 | 111.5 | 0 | 0 |
| evidence | 15.2 | 29.0 | 5.4 | 107.1 | 0 | 0 |
| fix | 13.7 | 20.1 | 1.7 | 76.8 | 0 | 0 |
| gate | 14.7 | 30.6 | 3.8 | 111.9 | 0 | 0 |
| pre_scan | 5.9 | 12.6 | 2.1 | 46.0 | 0 | 0 |

**Mean total elapsed per run:** 88s  |  Min: 33s  |  Max: 605s


---

## File: `WebGoat_Content_Challenge3.aspx.cs`

**Runs with this file:** 12  |  **Gate consistency:** 67%  |  **Verdict distribution:** FAIL: 2  NEEDS_HUMAN: 8  PASS: 2

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| No Input Validation or Sanitization | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Verbose Error Handling or Debug Mode Enabled | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Potential Debug/Verbose Error Exposure | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Lack of Input Validation and CSRF Protection | Medium | 8% (1/12) | 0.90 | model inconsistency |
| No Authentication Boundary Enforcement for Challenge3 Page | High | 8% (1/12) | 0.90 | model inconsistency |
| Incomplete Page Implementation | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Incomplete Security Controls Implementation | Low | 8% (1/12) | 0.80 | model inconsistency |
| Potential Insecure Direct Object Reference | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Lack of Input Validation and Sanitization | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Potential Direct Object Access Vulnerability | High | 8% (1/12) | 0.90 | model inconsistency |
| Lack of Input Validation or Sanitization | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Potential Information Disclosure | Low | 8% (1/12) | 0.90 | model inconsistency |
| Missing Authorization Check on Sensitive Operation | High | 17% (2/12) | 0.90 | model inconsistency |
| Potential Missing Authorization Check | High | 25% (3/12) | 0.90 | model inconsistency |
| Lack of Input Validation | Medium | 25% (3/12) | 0.90 | model inconsistency |
| Potential Missing Authorization Check | Medium | 58% (7/12) | 0.90 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 8.3 | 14.2 | 3.9 | 53.5 | 0 | 0 |
| threat | 20.0 | 37.4 | 8.2 | 138.7 | 0 | 0 |
| hypotheses | 23.1 | 48.9 | 7.4 | 178.4 | 0 | 0 |
| evidence | 18.8 | 34.7 | 6.7 | 128.9 | 0 | 0 |
| fix | 24.9 | 47.9 | 6.6 | 176.9 | 0 | 0 |
| gate | 24.1 | 60.3 | 4.1 | 215.6 | 0 | 0 |
| pre_scan | 5.8 | 11.7 | 2.2 | 42.9 | 0 | 0 |

**Mean total elapsed per run:** 125s  |  Min: 42s  |  Max: 935s


---

## File: `WebGoat_Content_Challenge3.aspx.designer.cs`

**Runs with this file:** 12  |  **Gate consistency:** 92%  |  **Verdict distribution:** NEEDS_HUMAN: 11  PASS: 1

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Hardcoded Configuration Values | Low | 8% (1/12) | 0.30 | borderline confidence |
| Potential Missing Authorization Checks | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Possible Debug/Development Configuration Exposure | Low | 8% (1/12) | 0.90 | model inconsistency |
| Possible Debug/Verbose Logging Enabled | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Potential Debug/Verbose Logging Enabled | Low | 8% (1/12) | 0.90 | model inconsistency |
| Potential Missing Authorization Controls | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Possible Incomplete Implementation | Low | 8% (1/12) | 0.30 | borderline confidence |
| Potential Exposure of Sensitive UI Elements | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Hardcoded Credentials or Configuration | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Hardcoded Credentials in Source Code | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Missing Authorization Check | Medium | 17% (2/12) | 0.30 | borderline confidence |
| Verbose Error Handling or Debug Output | Low | 17% (2/12) | 0.60 | borderline confidence |
| Potential Missing Authorization Check | High | 17% (2/12) | 0.30 | borderline confidence |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 6.5 | 11.4 | 3.0 | 42.7 | 0 | 0 |
| threat | 18.2 | 35.5 | 6.9 | 130.9 | 0 | 0 |
| hypotheses | 16.3 | 32.1 | 5.5 | 118.2 | 0 | 0 |
| evidence | 13.8 | 22.9 | 5.6 | 86.4 | 0 | 0 |
| fix | 8.9 | 3.9 | 1.5 | 18.0 | 0 | 0 |
| gate | 12.4 | 21.7 | 4.6 | 81.3 | 0 | 0 |
| pre_scan | 7.4 | 16.9 | 2.1 | 61.1 | 0 | 0 |

**Mean total elapsed per run:** 83s  |  Min: 33s  |  Max: 539s


---

## File: `WebGoat_Content_ChangePwd.aspx.cs`

**Runs with this file:** 12  |  **Gate consistency:** 58%  |  **Verdict distribution:** FAIL: 7  NEEDS_HUMAN: 5

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Potential Exposure of Sensitive Functionality | Medium | 8% (1/12) | 0.40 | borderline confidence |
| Business Logic Flaw - Forced Password Change Without Authorization | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential Authentication Bypass in Password Change Flow | Critical | 8% (1/12) | 0.90 | model inconsistency |
| Potential Exposure of Sensitive Data in Page Code | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Potential Exposure of Sensitive User Data | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Sensitive Password Change Functionality Exposed to Unauthenticated Users | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Potential Information Disclosure in Error Handling | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Potential for Sensitive Data Exposure in Password Change Page | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Missing Authentication Check in Password Change Page | High | 17% (2/12) | 0.90 | model inconsistency |
| Potential Authentication Bypass in Password Change Page | Critical | 33% (4/12) | 0.90 | model inconsistency |
| Missing Authorization Check in Password Change Functionality | High | 33% (4/12) | 0.90 | model inconsistency |
| Missing Authorization Check on Password Change Functionality | High | 50% (6/12) | 0.90 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 8.5 | 14.8 | 4.1 | 55.5 | 0 | 0 |
| threat | 21.9 | 42.3 | 7.3 | 156.2 | 0 | 0 |
| hypotheses | 27.5 | 60.8 | 8.4 | 220.5 | 0 | 0 |
| evidence | 28.8 | 62.5 | 9.6 | 227.2 | 0 | 0 |
| fix | 25.1 | 54.7 | 4.7 | 198.8 | 0 | 0 |
| gate | 25.2 | 62.3 | 5.0 | 222.9 | 0 | 0 |
| pre_scan | 5.9 | 11.7 | 2.2 | 43.1 | 0 | 0 |

**Mean total elapsed per run:** 143s  |  Min: 45s  |  Max: 1124s


---

## File: `WebGoat_Default.aspx.cs`

**Runs with this file:** 12  |  **Gate consistency:** 92%  |  **Verdict distribution:** FAIL: 11  NEEDS_HUMAN: 1

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Information Exposure via ViewState | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Missing Authentication Check on Database Rebuild | High | 8% (1/12) | 0.90 | model inconsistency |
| Information Disclosure via Cookie | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Information Disclosure via ViewState | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Missing Secure Flags on Authentication Cookies | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Information Disclosure via Server Name in Cookie | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Lack of Authorization Check for Rebuild Functionality | High | 8% (1/12) | 0.90 | model inconsistency |
| Server Name Exposure in HTTP Cookie | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Lack of Authorization Check on Database Rebuild | High | 8% (1/12) | 0.90 | model inconsistency |
| Lack of Authentication Check on Database Rebuild | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential Information Disclosure via ViewState | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Information Disclosure in HTTP Cookie | High | 8% (1/12) | 0.90 | model inconsistency |
| Session ID Exposure via ViewState | High | 8% (1/12) | 0.90 | model inconsistency |
| Information Leak via Unprotected Session Data in ViewState | High | 8% (1/12) | 0.90 | model inconsistency |
| ViewState Written to Screen | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Potential Reconnaissance via Cookie Information Leak | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Session Hijacking Potential via ViewState SessionID Storage | High | 8% (1/12) | 0.90 | model inconsistency |
| Information Disclosure via Cookie | High | 8% (1/12) | 0.90 | model inconsistency |
| Missing Authorization Check for RebuildDatabase Page | Critical | 8% (1/12) | 0.90 | model inconsistency |
| Session Management Flaw | High | 8% (1/12) | 0.85 | model inconsistency |
| Information Disclosure via Server Name in HTTP Cookie | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Lack of Authorization Check for Database Rebuild Functionality | High | 8% (1/12) | 0.90 | model inconsistency |
| Missing Authorization Check on Database Rebuild | High | 25% (3/12) | 0.85 | model inconsistency |
| Information Exposure Through Cookie | Medium | 50% (6/12) | 0.89 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 4.8 | 0.3 | 4.2 | 5.3 | 0 | 0 |
| threat | 11.5 | 1.7 | 8.0 | 13.9 | 0 | 0 |
| hypotheses | 10.8 | 1.3 | 8.9 | 12.5 | 0 | 0 |
| evidence | 11.8 | 1.8 | 9.1 | 14.3 | 0 | 0 |
| fix | 9.7 | 1.6 | 7.9 | 12.8 | 0 | 0 |
| gate | 7.0 | 1.0 | 5.3 | 8.7 | 0 | 0 |
| pre_scan | 4.6 | 0.4 | 3.8 | 5.4 | 0 | 0 |

**Mean total elapsed per run:** 60s  |  Min: 50s  |  Max: 70s


---

## File: `WebGoat_Default.aspx.designer.cs`

**Runs with this file:** 12  |  **Gate consistency:** 92%  |  **Verdict distribution:** FAIL: 1  NEEDS_HUMAN: 11

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Potential Sensitive Data Exposure in UI Controls | Medium | 8% (1/12) | 0.50 | borderline confidence |
| Potential Exposure of Sensitive UI Elements | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Missing Authorization Check | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Possible Debug/Verbose Error Output | Low | 8% (1/12) | 0.30 | borderline confidence |
| Missing Authorization Checks | High | 8% (1/12) | 0.30 | borderline confidence |
| Potential Information Disclosure | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Sensitive Data Exposure via Label Control | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Possible Sensitive Data Exposure | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Sensitive Data Exposure | Medium | 17% (2/12) | 0.30 | borderline confidence |
| Potential Missing Authorization Check | High | 42% (5/12) | 0.30 | borderline confidence |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 3.0 | 0.1 | 2.8 | 3.2 | 0 | 0 |
| threat | 6.4 | 2.1 | 2.2 | 8.0 | 0 | 0 |
| hypotheses | 5.7 | 1.1 | 3.4 | 7.6 | 0 | 0 |
| evidence | 6.2 | 1.3 | 3.8 | 7.6 | 0 | 0 |
| fix | 7.2 | 4.3 | 1.5 | 13.2 | 0 | 0 |
| gate | 6.3 | 1.1 | 3.8 | 8.2 | 0 | 0 |
| pre_scan | 2.2 | 0.2 | 1.8 | 2.5 | 0 | 0 |

**Mean total elapsed per run:** 37s  |  Min: 22s  |  Max: 48s


---

## File: `WebGoat_ForgotPassword.aspx.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 12

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Possible Sensitive Data Exposure in Password Reset Flow | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Information Disclosure in Password Reset Process | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Lack of Input Validation for Password Reset Tokens | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Exposure of User Data in Password Reset Process | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Possible Exposure of Sensitive User Data in Password Reset Flow | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Exposure of User Account Information | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Possible Exposure of Sensitive User Information During Password Reset | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Missing Authentication Check in Password Reset Feature | High | 8% (1/12) | 0.30 | borderline confidence |
| Potential Hardcoded Credentials or Configuration in Page | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Possible Hardcoded Credentials or Configuration Values | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Improper Error Handling or Debug Information Exposure | Low | 8% (1/12) | 0.30 | borderline confidence |
| Missing Authorization Check in Password Reset Functionality | High | 17% (2/12) | 0.30 | borderline confidence |
| Potential Missing Authorization Check in Password Reset Functionality | High | 42% (5/12) | 0.30 | borderline confidence |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 3.8 | 0.3 | 3.5 | 4.4 | 0 | 0 |
| threat | 9.8 | 1.6 | 8.2 | 12.7 | 0 | 0 |
| hypotheses | 9.6 | 2.0 | 6.8 | 13.2 | 0 | 0 |
| evidence | 10.6 | 1.7 | 8.2 | 14.1 | 0 | 0 |
| fix | 9.0 | 4.8 | 1.5 | 14.6 | 0 | 0 |
| gate | 7.3 | 1.2 | 5.7 | 10.0 | 0 | 0 |
| pre_scan | 2.5 | 0.3 | 2.1 | 3.0 | 0 | 0 |

**Mean total elapsed per run:** 53s  |  Min: 44s  |  Max: 68s


---

## File: `WebGoat_ForgotPassword.aspx.designer.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 12

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Potential Missing Authentication in Password Reset Functionality | High | 8% (1/12) | 0.30 | borderline confidence |
| Potential SQL Injection Vector in Password Reset Logic | High | 8% (1/12) | 0.30 | borderline confidence |
| Hardcoded Credentials or Keys in Password Reset Logic | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Possible Debug/Verbose Logging Enabled | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Potential Missing Authentication Check in Password Reset Functionality | High | 8% (1/12) | 0.30 | borderline confidence |
| Insecure Direct Object Reference in Password Reset Flow | High | 8% (1/12) | 0.30 | borderline confidence |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 3.0 | 0.2 | 2.6 | 3.2 | 0 | 0 |
| threat | 7.5 | 1.7 | 2.8 | 9.6 | 0 | 0 |
| hypotheses | 6.7 | 1.7 | 3.9 | 10.1 | 0 | 0 |
| evidence | 6.2 | 2.4 | 4.1 | 10.8 | 0 | 0 |
| fix | 4.0 | 4.1 | 1.2 | 12.4 | 0 | 0 |
| gate | 6.3 | 1.7 | 4.6 | 10.2 | 0 | 0 |
| pre_scan | 2.6 | 0.9 | 2.2 | 5.3 | 0 | 0 |

**Mean total elapsed per run:** 36s  |  Min: 27s  |  Max: 56s


---

## File: `WebGoat_Global.asax.cs`

**Runs with this file:** 12  |  **Gate consistency:** 92%  |  **Verdict distribution:** FAIL: 11  NEEDS_HUMAN: 1

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Potential Debug Mode Enabled in Production | Medium | 8% (1/12) | 0.90 | model inconsistency |
| X-XSS-Protection Header Set to Disabled | Critical | 8% (1/12) | 1.00 | model inconsistency |
| Potential Chained Attack: Reflected XSS with Privilege Escalation | Critical | 8% (1/12) | 0.90 | model inconsistency |
| Unvalidated Forms Authentication Ticket May Allow Identity Spoofing | High | 8% (1/12) | 0.90 | model inconsistency |
| X-XSS-Protection Header Disabled, Increasing XSS Vulnerability | Medium | 8% (1/12) | 1.00 | model inconsistency |
| Improper Role Data Handling May Lead to Privilege Escalation | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential Weak Authentication Cookie Handling | Medium | 8% (1/12) | 0.70 | model inconsistency |
| Possible Information Disclosure in Error Handling | Low | 8% (1/12) | 0.90 | model inconsistency |
| Potential Exposure of Role Data via Forms Authentication Ticket | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Possible Insecure Direct Object Reference (IDOR) Risk in Role Handling | High | 8% (1/12) | 0.90 | model inconsistency |
| Insecure HTTP Header Configuration - X-XSS-Protection Disabled | Critical | 8% (1/12) | 0.90 | model inconsistency |
| Use of Weak Cookie Handling for Authentication | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Potential Debug Mode Enabled via log4net Configuration | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Forms Authentication Ticket UserData Role Parsing Without Validation | High | 8% (1/12) | 0.90 | model inconsistency |
| XSS Vulnerability Due to Disabled X-XSS-Protection Header | High | 8% (1/12) | 0.90 | model inconsistency |
| Privilege Escalation Through Manipulated Forms Authentication Ticket | Critical | 8% (1/12) | 0.90 | model inconsistency |
| Possible Weak Forms Authentication Implementation | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Potential Information Disclosure via Debug Mode | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Debug Mode Configuration in Production Code | Low | 8% (1/12) | 0.90 | model inconsistency |
| Potential Weak Authentication Ticket Handling | Medium | 8% (1/12) | 0.80 | model inconsistency |
| XSS Protection Disabled via Security Header | High | 8% (1/12) | 0.90 | model inconsistency |
| Forms Authentication Ticket UserData Handling | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Potential Insecure Direct Object Reference | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential Debug Mode Configuration | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Insecure Role Handling in Forms Authentication | High | 8% (1/12) | 0.90 | model inconsistency |
| X-XSS-Protection Header Disabled | High | 8% (1/12) | 1.00 | model inconsistency |
| Debug Mode Configuration Detected | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Insecure X-XSS-Protection Header Set to 0 | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Potential Sensitive Data Exposure via Logging Configuration | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Insecure Session Management Due to Missing Authorization Enforcement | High | 8% (1/12) | 0.90 | model inconsistency |
| X-XSS-Protection Header Set to Zero | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Potential Insecure Role Assignment | High | 17% (2/12) | 0.90 | model inconsistency |
| X-XSS-Protection Header Disabled | Medium | 33% (4/12) | 0.93 | model inconsistency |
| Potential Role-Based Access Control Bypass | High | 42% (5/12) | 0.86 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 8.2 | 0.6 | 7.1 | 9.0 | 0 | 0 |
| threat | 12.4 | 1.0 | 10.0 | 13.7 | 0 | 0 |
| hypotheses | 10.7 | 1.0 | 9.1 | 12.6 | 0 | 0 |
| evidence | 15.2 | 1.9 | 12.3 | 18.3 | 0 | 0 |
| fix | 14.9 | 2.3 | 11.6 | 19.2 | 0 | 0 |
| gate | 10.5 | 2.6 | 6.5 | 13.8 | 0 | 0 |
| pre_scan | 3.8 | 0.4 | 2.8 | 4.3 | 0 | 0 |

**Mean total elapsed per run:** 76s  |  Min: 68s  |  Max: 84s


---

## File: `WebGoat_LoginPage.aspx.cs`

**Runs with this file:** 12  |  **Gate consistency:** 75%  |  **Verdict distribution:** FAIL: 9  NEEDS_HUMAN: 3

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Bypassable Authentication Logic | Critical | 8% (1/12) | 0.95 | model inconsistency |
| Missing Authorization Check on Redirect | High | 8% (1/12) | 0.90 | model inconsistency |
| Missing Authentication Logic | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential Insecure Direct Object Reference | Medium | 8% (1/12) | 0.40 | borderline confidence |
| Unconditional Redirect Without Authentication Validation | Critical | 8% (1/12) | 0.90 | model inconsistency |
| Incomplete Admin Login Implementation | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Potential Bypass of Authentication Mechanism via Commented-out Code | Critical | 8% (1/12) | 0.90 | model inconsistency |
| Missing Input Validation for Login Credentials | High | 8% (1/12) | 0.90 | model inconsistency |
| Unvalidated Redirect Vulnerability | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Commented-out Authentication Logic | High | 8% (1/12) | 0.95 | model inconsistency |
| Missing Authentication Implementation | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential Insecure Redirect | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Bypassable Authentication Flow | High | 8% (1/12) | 0.90 | model inconsistency |
| Unvalidated Redirect Leading to Potential Phishing or Data Exposure | High | 8% (1/12) | 0.90 | model inconsistency |
| Removal of Core Authentication Logic May Allow Unauthorized Access | High | 8% (1/12) | 0.90 | model inconsistency |
| Authentication Bypass via Redirect | Critical | 8% (1/12) | 0.90 | model inconsistency |
| Missing Authorization Check in Admin Login | High | 8% (1/12) | 0.90 | model inconsistency |
| Incomplete Input Validation on Login Form | High | 8% (1/12) | 0.90 | model inconsistency |
| Unauthorized Access to Protected Resources via Authentication Bypass | Critical | 8% (1/12) | 0.90 | model inconsistency |
| Potential Denial of Service through Unhandled Login Logic | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Bypassable Authentication Logic | High | 17% (2/12) | 0.93 | model inconsistency |
| Authentication Bypass via Redirect | High | 42% (5/12) | 0.92 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.1 | 0.6 | 4.3 | 6.2 | 0 | 0 |
| threat | 10.4 | 1.0 | 8.6 | 11.6 | 0 | 0 |
| hypotheses | 9.8 | 1.5 | 6.7 | 11.9 | 0 | 0 |
| evidence | 11.5 | 3.3 | 5.9 | 18.3 | 0 | 0 |
| fix | 12.5 | 7.2 | 5.6 | 30.6 | 0 | 0 |
| gate | 8.2 | 2.4 | 4.7 | 13.9 | 0 | 0 |
| pre_scan | 3.2 | 0.3 | 2.8 | 3.7 | 0 | 0 |

**Mean total elapsed per run:** 61s  |  Min: 42s  |  Max: 93s


---

## File: `WebGoat_LoginPage.aspx.designer.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** NEEDS_HUMAN: 12

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Potential Missing Authentication Controls | High | 8% (1/12) | 0.30 | borderline confidence |
| Missing Authorization Checks | High | 8% (1/12) | 0.30 | borderline confidence |
| Potential Information Disclosure via Error Handling | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Missing Authorization Check for Admin Functionality | High | 8% (1/12) | 0.30 | borderline confidence |
| Possible Information Disclosure via Error Handling | Low | 8% (1/12) | 0.30 | borderline confidence |
| Missing Authorization Checks for Sensitive Operations | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Insecure Error Handling or Logging | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Missing Authentication Logic in Login Page | High | 17% (2/12) | 0.30 | borderline confidence |
| Potential Insecure Direct Object Reference | Medium | 17% (2/12) | 0.30 | borderline confidence |
| Potential Missing Authentication Check on Admin Login Button | High | 17% (2/12) | 0.30 | borderline confidence |
| Verbose Error Handling or Debug Information Exposure | Medium | 17% (2/12) | 0.85 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 3.3 | 0.4 | 3.0 | 4.3 | 0 | 0 |
| threat | 8.5 | 1.9 | 6.6 | 12.5 | 0 | 0 |
| hypotheses | 9.0 | 2.3 | 5.6 | 14.0 | 0 | 0 |
| evidence | 8.5 | 2.3 | 5.4 | 15.0 | 0 | 0 |
| fix | 10.1 | 7.1 | 1.8 | 25.9 | 0 | 0 |
| gate | 6.8 | 1.3 | 5.0 | 9.3 | 0 | 0 |
| pre_scan | 2.6 | 0.3 | 2.3 | 3.0 | 0 | 0 |

**Mean total elapsed per run:** 49s  |  Min: 34s  |  Max: 73s


---

## File: `WebGoat_ProxySetup.aspx.cs`

**Runs with this file:** 12  |  **Gate consistency:** 58%  |  **Verdict distribution:** FAIL: 1  NEEDS_HUMAN: 7  PASS: 4

### Stable findings  (detection rate ≥ 80%)

| Finding | Severity | Detection rate | 95% CI | Conf mean | Conf std |
|---|---|---|---|---|---|
| Potential String Manipulation Vulnerability | Medium | 83% (10/12) | [0.55, 0.95] | 0.88 | 0.063 |

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Potential String Manipulation via User Input | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Potential Misuse of Proxy Configuration Functionality | High | 8% (1/12) | 0.90 | model inconsistency |
| Information Exposure via Output Field | Low | 8% (1/12) | 0.85 | model inconsistency |
| Potential XSS Vulnerability Due to Unsanitized Input Reflection | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential Input Validation Vulnerability in Proxy Setup Logic | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Information Exposure in Response | Low | 8% (1/12) | 0.90 | model inconsistency |
| Manipulation of Proxy Settings via User Input | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Exposure of Internal Data Through Response Echoing | Low | 8% (1/12) | 0.90 | model inconsistency |
| Output of User Input in Response | Medium | 8% (1/12) | 0.90 | model inconsistency |
| User Input Exposed in Response | Low | 8% (1/12) | 0.90 | model inconsistency |
| User Input Displayed in Output Without Sanitization | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Potential XSS via Unsantized Output Reflection | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Information Exposure via User Input | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Potential Exposure of Sensitive Configuration Data | Medium | 8% (1/12) | 0.90 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 4.1 | 0.2 | 3.8 | 4.5 | 0 | 0 |
| threat | 10.4 | 1.3 | 7.0 | 12.4 | 0 | 0 |
| hypotheses | 11.1 | 2.4 | 6.7 | 14.5 | 0 | 0 |
| evidence | 11.9 | 3.5 | 8.4 | 20.2 | 0 | 0 |
| fix | 9.6 | 3.5 | 4.9 | 18.3 | 0 | 0 |
| gate | 5.9 | 1.4 | 3.7 | 9.2 | 0 | 0 |
| pre_scan | 2.1 | 0.3 | 1.7 | 2.5 | 0 | 0 |

**Mean total elapsed per run:** 55s  |  Min: 44s  |  Max: 73s


---

## File: `WebGoat_ProxySetup.aspx.designer.cs`

**Runs with this file:** 12  |  **Gate consistency:** 83%  |  **Verdict distribution:** FAIL: 2  NEEDS_HUMAN: 10

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Potential Information Disclosure in Label Output | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Hardcoded Configuration Values in Source Code | Low | 8% (1/12) | 0.30 | borderline confidence |
| Potential Command Injection Vulnerability | High | 8% (1/12) | 0.30 | borderline confidence |
| Potential Information Exposure in UI Controls | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Missing Authorization Check on Sensitive Operation | Critical | 8% (1/12) | 0.30 | borderline confidence |
| Potential Information Disclosure via Output Label | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Information Disclosure via lblOutput | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Exposure of Sensitive Data in Label Output | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Exposure of Sensitive Data in Output Label | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Missing Authorization Check | Medium | 17% (2/12) | 0.30 | borderline confidence |
| Potential Input Sanitization Issue | Medium | 17% (2/12) | 0.30 | borderline confidence |
| Missing Authorization Check on Sensitive Operation | High | 25% (3/12) | 0.30 | borderline confidence |
| Potential SQL Injection via TextBox Input | High | 25% (3/12) | 0.30 | borderline confidence |
| Potential Command Injection via TextBox Input | High | 33% (4/12) | 0.30 | borderline confidence |
| Missing Authorization Check on Sensitive Operation | Medium | 33% (4/12) | 0.30 | borderline confidence |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 3.2 | 0.1 | 3.0 | 3.4 | 0 | 0 |
| threat | 8.7 | 1.9 | 4.0 | 11.0 | 0 | 0 |
| hypotheses | 7.7 | 1.0 | 5.9 | 8.7 | 0 | 0 |
| evidence | 8.9 | 1.5 | 6.8 | 10.8 | 0 | 0 |
| fix | 11.5 | 6.1 | 1.8 | 25.3 | 0 | 0 |
| gate | 8.3 | 1.9 | 5.9 | 12.2 | 0 | 0 |
| pre_scan | 2.8 | 0.3 | 2.2 | 3.1 | 0 | 0 |

**Mean total elapsed per run:** 51s  |  Min: 34s  |  Max: 71s


---

## File: `WebGoat_Web.config`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 12

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Incomplete Authorization Rules for Verb Tampering Attack | High | 8% (1/12) | 0.90 | model inconsistency |
| Exposure of Detailed Error Messages in Production | High | 8% (1/12) | 0.90 | model inconsistency |
| Insecure Session Cookie Handling | High | 8% (1/12) | 0.90 | model inconsistency |
| Verbose Logging Configuration May Expose Sensitive Data | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Potential Secret Exposure in Forms Authentication Configuration | High | 8% (1/12) | 0.90 | model inconsistency |
| Incomplete Access Control for Admin-Only Resources | High | 8% (1/12) | 0.90 | model inconsistency |
| Hardcoded Administrative Credentials | Critical | 8% (1/12) | 1.00 | model inconsistency |
| Insecure Session Cookie Handling | Medium | 8% (1/12) | 0.95 | model inconsistency |
| Exposure of Internal System Information | High | 8% (1/12) | 0.90 | model inconsistency |
| Insecure Authorization Rule Configuration | High | 8% (1/12) | 0.95 | model inconsistency |
| Hardcoded Passwords in Configuration | Critical | 8% (1/12) | 0.95 | model inconsistency |
| Exposed Error Details in Production | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Disabled Header Validation | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Weak Authentication with Clear Text Passwords | Critical | 8% (1/12) | 0.95 | model inconsistency |
| Hardcoded Credentials in Configuration File | Critical | 8% (1/12) | 0.95 | model inconsistency |
| Detailed Error Messages Enabled in Production | High | 8% (1/12) | 0.90 | model inconsistency |
| Insecure Cookie Settings | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Header Checking Disabled | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Hardcoded Credentials with Potential Privilege Escalation | Critical | 8% (1/12) | 0.95 | model inconsistency |
| Hardcoded Credentials Stored in Plain Text | Critical | 8% (1/12) | 1.00 | model inconsistency |
| Session Cookies Missing Security Flags | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Debug Mode Active in Production Configuration | High | 8% (1/12) | 0.90 | model inconsistency |
| Excessive Logging in Production Environment | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Hardcoded Credentials in Source Code | Critical | 8% (1/12) | 1.00 | model inconsistency |
| Misconfigured Authorization Rules | High | 8% (1/12) | 0.95 | model inconsistency |
| Insecure Session Cookies | High | 8% (1/12) | 0.90 | model inconsistency |
| Exposure of Detailed Error Messages | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Verbose Logging in Production | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Header Injection Vulnerability Due to Disabled Header Checking | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Exposure of Sensitive Debug Information in Production | High | 8% (1/12) | 0.95 | model inconsistency |
| Verbose Logging May Expose Sensitive Data in Logs | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Hardcoded Authentication Credentials | Critical | 8% (1/12) | 1.00 | model inconsistency |
| Incomplete Authorization Policy Definition | High | 8% (1/12) | 0.95 | model inconsistency |
| Detailed Error Messages Exposed in Production | High | 8% (1/12) | 0.90 | model inconsistency |
| Insecure Session Cookie Settings | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Disabled HTTP Header Validation | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Hardcoded Clear Text Passwords in Authentication Configuration | Critical | 8% (1/12) | 1.00 | model inconsistency |
| Insecure Direct Object Reference in Verb Tampering Attack | High | 8% (1/12) | 0.95 | model inconsistency |
| Debug Mode Enabled in Production Configuration | High | 8% (1/12) | 0.90 | model inconsistency |
| Detailed Error Messages Enabled in Production | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Permissive Authorization Rules in Default Context | High | 8% (1/12) | 0.90 | model inconsistency |
| Insecure Session Cookie Configuration | High | 8% (1/12) | 0.90 | model inconsistency |
| Verbose Logging May Expose Sensitive Information | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Debug Mode Enabled in Production | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Verbose Error Messages Enabled | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Improper Verb-Based Authorization | High | 8% (1/12) | 0.90 | model inconsistency |
| Unrestricted Authorization Rules | High | 8% (1/12) | 0.90 | model inconsistency |
| Insecure Session Cookie Settings | High | 8% (1/12) | 0.90 | model inconsistency |
| Insecure Authorization Configuration | Critical | 8% (1/12) | 0.95 | model inconsistency |
| Detailed Error Messages Exposed to Users | High | 8% (1/12) | 0.90 | model inconsistency |
| Debug Logging Enabled with Sensitive Data Exposure | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Hardcoded Credentials in Clear Text | Critical | 17% (2/12) | 0.95 | model inconsistency |
| Sensitive Data Exposure in Logs | Medium | 17% (2/12) | 0.82 | model inconsistency |
| Inconsistent Authorization Controls | High | 17% (2/12) | 0.90 | model inconsistency |
| Verbose Logging Enabled in Production | Medium | 17% (2/12) | 0.80 | model inconsistency |
| Inconsistent Authorization Rules for VerbTamperingAttack.aspx | High | 17% (2/12) | 0.90 | model inconsistency |
| Hardcoded Clear Text Credentials | Critical | 17% (2/12) | 0.97 | model inconsistency |
| Insecure Session Cookie Configuration | Medium | 25% (3/12) | 0.87 | model inconsistency |
| Debug Mode Enabled in Production | High | 25% (3/12) | 0.90 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 7.4 | 0.7 | 6.6 | 8.5 | 0 | 0 |
| threat | 17.3 | 1.7 | 13.7 | 19.2 | 0 | 0 |
| hypotheses | 15.6 | 2.3 | 12.3 | 19.9 | 0 | 0 |
| evidence | 19.2 | 6.5 | 1.4 | 28.8 | 0 | 0 |
| fix | 21.6 | 6.4 | 9.0 | 37.0 | 0 | 0 |
| gate | 11.9 | 3.0 | 7.2 | 18.4 | 0 | 0 |
| pre_scan | 12.2 | 1.9 | 10.0 | 15.7 | 0 | 0 |

**Mean total elapsed per run:** 105s  |  Min: 76s  |  Max: 142s


---

## File: `WebGoat_WebGoat.NET.csproj`

**Runs with this file:** 12  |  **Gate consistency:** 75%  |  **Verdict distribution:** FAIL: 9  NEEDS_HUMAN: 2  PASS: 1

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Verbose Environment Variables Set in Debug Configuration | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Use of Outdated MySQL Data Provider | High | 8% (1/12) | 0.90 | model inconsistency |
| Verbose Environment Variables for Mono Debugging | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Outdated MySQL Connector Version Referenced | High | 8% (1/12) | 0.80 | model inconsistency |
| Unsafe Code Blocks Enabled in Build Configuration | High | 8% (1/12) | 0.90 | model inconsistency |
| Hardcoded Environment Variables for Mono Logging | Medium | 8% (1/12) | 0.75 | model inconsistency |
| Potential Buffer Overflow Risk from Unsafe Code Usage | High | 8% (1/12) | 0.90 | model inconsistency |
| Unsafe Code Blocks Allowed in Compilation | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Outdated MySQL Connector Version May Contain Known Vulnerabilities | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Verbose Environment Variables in Build Configuration May Leak System Information | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Unsafe Block Usage Enabled | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Potential Missing Authentication Checks on Web Pages | High | 8% (1/12) | 0.75 | model inconsistency |
| Environment Variables for Debug Logging Enabled | Medium | 8% (1/12) | 0.75 | model inconsistency |
| Environment Variables with Debug Logging Enabled | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Use of Outdated MySQL.Data Library | Medium | 8% (1/12) | 0.75 | model inconsistency |
| Use of Outdated log4net Library | Medium | 8% (1/12) | 0.75 | model inconsistency |
| Verbose Logging Configuration May Expose Sensitive Data | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Missing Authorization Controls in WebGoatCoins Module | High | 8% (1/12) | 0.75 | model inconsistency |
| Potential SQL Injection Vulnerabilities via Database Providers | High | 8% (1/12) | 0.80 | model inconsistency |
| Verbose Environment Variables in Debug Config | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Use of Outdated MySQL Provider | Medium | 8% (1/12) | 0.75 | model inconsistency |
| Use of Outdated Sqlite Provider | Medium | 8% (1/12) | 0.75 | model inconsistency |
| Sensitive Data Exposure via Debug Logging | High | 8% (1/12) | 0.80 | model inconsistency |
| Verbose Environment Variables for Mono Logging | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Hardcoded Environment Variables for Mono Logging | Low | 8% (1/12) | 0.85 | model inconsistency |
| Unsafe Code Blocks Enabled in MSBuild Configuration | Medium | 17% (2/12) | 0.90 | model inconsistency |
| Debug Mode Enabled in MSBuild Configuration | High | 25% (3/12) | 0.95 | model inconsistency |
| Debug Mode Enabled in MSBuild Configuration | Medium | 33% (4/12) | 0.88 | model inconsistency |
| Debug Mode Enabled in Build Configuration | High | 42% (5/12) | 0.95 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 7.7 | 1.0 | 6.5 | 9.5 | 0 | 0 |
| threat | 14.4 | 2.1 | 12.0 | 18.2 | 0 | 0 |
| hypotheses | 14.2 | 1.8 | 12.1 | 18.5 | 0 | 0 |
| evidence | 17.3 | 2.8 | 14.4 | 23.0 | 0 | 0 |
| fix | 16.3 | 8.2 | 7.6 | 37.1 | 0 | 0 |
| gate | 10.0 | 2.3 | 7.1 | 14.7 | 0 | 0 |
| pre_scan | 9.5 | 1.6 | 6.8 | 11.8 | 0 | 0 |

**Mean total elapsed per run:** 90s  |  Min: 72s  |  Max: 128s


---

## File: `WebGoat_dbtest.aspx.cs`

**Runs with this file:** 12  |  **Gate consistency:** 100%  |  **Verdict distribution:** FAIL: 12

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Missing Authorization Check on Database Reconfiguration | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential SQL Injection via Configuration Values | Medium | 8% (1/12) | 0.70 | model inconsistency |
| Insecure Configuration Management with Hardcoded Keys | Medium | 8% (1/12) | 0.70 | model inconsistency |
| Missing Authentication for Sensitive Database Reconfiguration Operations | High | 8% (1/12) | 0.90 | model inconsistency |
| Lack of Input Sanitization in Configuration Updates | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Sensitive Configuration Details Exposed in Error Messages | Medium | 8% (1/12) | 0.70 | model inconsistency |
| Unrestricted Access to Rebuild Database Functionality | High | 8% (1/12) | 0.90 | model inconsistency |
| Missing Authentication for Database Reconfiguration | High | 8% (1/12) | 0.95 | model inconsistency |
| Configuration Input Sanitization Missing | High | 8% (1/12) | 0.85 | model inconsistency |
| Lack of Access Control for Configuration Reading | Medium | 8% (1/12) | 0.75 | model inconsistency |
| Unrestricted Database Rebuild Functionality | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential SQL Injection via Configuration File Updates | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Uncontrolled Database Rebuild Functionality | High | 8% (1/12) | 0.90 | model inconsistency |
| Potential SQL Injection via Configuration Updates | High | 8% (1/12) | 0.85 | model inconsistency |
| Sensitive Data Exposure in Configuration File | High | 8% (1/12) | 0.90 | model inconsistency |
| Missing Authorization for Database Rebuild Functionality | High | 8% (1/12) | 0.95 | model inconsistency |
| Potential Credential Exposure in Configuration Updates | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Unrestricted Database Rebuild with Potential for Data Loss | High | 8% (1/12) | 0.90 | model inconsistency |
| Direct Write of User Input to Configuration File Without Validation | High | 8% (1/12) | 0.90 | model inconsistency |
| Exposure of Sensitive Database Configuration Data to Unauthenticated Users | High | 8% (1/12) | 0.90 | model inconsistency |
| Unrestricted Access to Database Configuration Rebuild Functionality | High | 8% (1/12) | 0.90 | model inconsistency |
| Missing Authorization on Sensitive Configuration Rebuild Functionality | High | 8% (1/12) | 0.95 | model inconsistency |
| Potential SQL Injection through Configuration File Manipulation | High | 8% (1/12) | 0.85 | model inconsistency |
| Clear Text Storage of Database Credentials | High | 8% (1/12) | 0.90 | model inconsistency |
| Missing Authorization Check on Database Reconfiguration Page | High | 8% (1/12) | 0.95 | model inconsistency |
| Unsanitized Configuration Input Leads to Potential Code Injection | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Unauthenticated Database Rebuild Functionality Could Cause Service Disruption | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Database Credentials Stored in Plain Text Configuration File | High | 8% (1/12) | 0.90 | model inconsistency |
| Lack of Input Validation on Database Configuration Fields | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Potential Insecure Direct Object Reference in Configuration Handling | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Exposure of Sensitive Configuration Data in Session State | Medium | 8% (1/12) | 0.80 | model inconsistency |
| Potential Input Sanitization Issues in Configuration Updates | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Verbose Error Handling May Reveal System Details | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Potential Exposure of Hardcoded Credentials or Secrets in Configuration | Medium | 8% (1/12) | 0.90 | model inconsistency |
| Potential SQL Injection Vulnerability via Configuration Update | High | 8% (1/12) | 0.85 | model inconsistency |
| Lack of Authorization Checks on Configuration Updates | Medium | 8% (1/12) | 0.85 | model inconsistency |
| Missing Authentication Check on Database Reconfiguration | Critical | 17% (2/12) | 0.95 | model inconsistency |
| Missing Authentication Check on Database Reconfiguration | High | 33% (4/12) | 0.94 | model inconsistency |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 5.6 | 0.6 | 4.8 | 6.8 | 0 | 0 |
| threat | 11.6 | 1.2 | 10.0 | 14.0 | 0 | 0 |
| hypotheses | 11.2 | 1.2 | 8.9 | 12.8 | 0 | 0 |
| evidence | 17.4 | 5.0 | 12.0 | 27.5 | 0 | 0 |
| fix | 22.5 | 10.6 | 12.8 | 45.3 | 0 | 0 |
| gate | 10.3 | 1.9 | 7.8 | 13.4 | 0 | 0 |
| pre_scan | 6.6 | 0.8 | 5.1 | 7.5 | 0 | 0 |

**Mean total elapsed per run:** 85s  |  Min: 64s  |  Max: 119s


---

## File: `WebGoat_dbtest.aspx.designer.cs`

**Runs with this file:** 12  |  **Gate consistency:** 50%  |  **Verdict distribution:** FAIL: 6  NEEDS_HUMAN: 6

### ⚠ Temperature-sensitive findings  (detection rate < 80%)

| Finding | Severity | Detection rate | Conf mean | Notes |
|---|---|---|---|---|
| Potential Exposure of Sensitive Data via UI Controls | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential SQL Injection via Database Configuration | High | 8% (1/12) | 0.30 | borderline confidence |
| Potential Hardcoded Sensitive Data in UI Controls | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Exposure of Sensitive Configuration Data via UI Controls | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential Exposure of Sensitive Data in UI Elements | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Hardcoded Credentials in UI Controls | High | 8% (1/12) | 0.30 | borderline confidence |
| Missing Authorization Checks on Sensitive Operations | High | 8% (1/12) | 0.30 | borderline confidence |
| Potential Sensitive Data Exposure in UI Controls | Medium | 8% (1/12) | 0.30 | borderline confidence |
| Potential SQL Injection Vector via Database Configuration | High | 8% (1/12) | 0.30 | borderline confidence |
| Missing Authorization Checks on Database Rebuild Functionality | Critical | 8% (1/12) | 0.30 | borderline confidence |
| Potential SQL Injection via Database Configuration Inputs | High | 8% (1/12) | 0.30 | borderline confidence |
| Missing Authorization Check on Database Rebuild Functionality | Critical | 17% (2/12) | 0.30 | borderline confidence |
| Potential Hardcoded Credentials in UI Controls | Medium | 17% (2/12) | 0.30 | borderline confidence |
| Missing Authorization Checks on Database Rebuild Functionality | High | 17% (2/12) | 0.30 | borderline confidence |
| Missing Authorization Check on Database Rebuild Functionality | High | 42% (5/12) | 0.30 | borderline confidence |
| Hardcoded Database Credentials in UI Controls | High | 58% (7/12) | 0.30 | borderline confidence |

### Agent timing

| Agent | Mean (s) | Std dev | Min | Max | Failures | Truncations |
|---|---|---|---|---|---|---|
| scope | 3.9 | 0.1 | 3.8 | 4.1 | 0 | 0 |
| threat | 9.3 | 1.0 | 8.0 | 10.8 | 0 | 0 |
| hypotheses | 8.7 | 1.6 | 5.2 | 10.5 | 0 | 0 |
| evidence | 11.6 | 2.3 | 7.7 | 14.6 | 0 | 0 |
| fix | 11.1 | 3.7 | 1.9 | 15.6 | 0 | 0 |
| gate | 9.0 | 1.4 | 6.5 | 10.9 | 0 | 0 |
| pre_scan | 3.9 | 0.5 | 3.2 | 4.4 | 0 | 0 |

**Mean total elapsed per run:** 58s  |  Min: 43s  |  Max: 68s


---

## Gate verdict detail per run


### `WebGoat_AddNewUser.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass9 | FAIL |

### `WebGoat_AddNewUser.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass9 | NEEDS_HUMAN |

### `WebGoat_App_Code_ConfigFile.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass9 | FAIL |

### `WebGoat_App_Code_CookieManager.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass9 | FAIL |

### `WebGoat_App_Code_CustomerLoginData.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | PASS |
| results_qwen3-coder-30b_temp1.0_pass10 | PASS |
| results_qwen3-coder-30b_temp1.0_pass11 | PASS |
| results_qwen3-coder-30b_temp1.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass2 | PASS |
| results_qwen3-coder-30b_temp1.0_pass3 | PASS |
| results_qwen3-coder-30b_temp1.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass6 | PASS |
| results_qwen3-coder-30b_temp1.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass9 | NEEDS_HUMAN |

### `WebGoat_App_Code_DB_DbConstants.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass9 | NEEDS_HUMAN |

### `WebGoat_App_Code_DB_DbProviderFactory.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | PASS |
| results_qwen3-coder-30b_temp1.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass11 | PASS |
| results_qwen3-coder-30b_temp1.0_pass12 | PASS |
| results_qwen3-coder-30b_temp1.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass3 | PASS |
| results_qwen3-coder-30b_temp1.0_pass4 | PASS |
| results_qwen3-coder-30b_temp1.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass6 | PASS |
| results_qwen3-coder-30b_temp1.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass9 | PASS |

### `WebGoat_App_Code_DB_DummyDbProvider.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass12 | PASS |
| results_qwen3-coder-30b_temp1.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass7 | PASS |
| results_qwen3-coder-30b_temp1.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass9 | FAIL |

### `WebGoat_App_Code_DB_IDbProvider.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass9 | NEEDS_HUMAN |

### `WebGoat_App_Code_DB_MySqlDbProvider.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass12 | accept |
| results_qwen3-coder-30b_temp1.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass7 | UNKNOWN |
| results_qwen3-coder-30b_temp1.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass9 | FAIL |

### `WebGoat_App_Code_DB_SqliteDbProvider.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass2 | accept |
| results_qwen3-coder-30b_temp1.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass9 | FAIL |

### `WebGoat_App_Code_Encoder.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass9 | FAIL |

### `WebGoat_App_Code_Settings.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass4 | PASS |
| results_qwen3-coder-30b_temp1.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass9 | FAIL |

### `WebGoat_App_Code_Util.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass9 | NEEDS_HUMAN |

### `WebGoat_App_Code_VeryWeakRandom.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass9 | NEEDS_HUMAN |

### `WebGoat_App_Code_WeakMessageDigest.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass9 | FAIL |

### `WebGoat_App_Code_WeakRandom.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass9 | FAIL |

### `WebGoat_App_Data_XmlInjectionUsers.xml`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass9 | NEEDS_HUMAN |

### `WebGoat_ChangePassword.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass9 | NEEDS_HUMAN |

### `WebGoat_ChangePassword.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass9 | FAIL |

### `WebGoat_Code_DatabaseUtilities.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass10 | approve |
| results_qwen3-coder-30b_temp1.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass9 | FAIL |

### `WebGoat_Code_IOHelper.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass9 | FAIL |

### `WebGoat_Code_SQLiteMembershipProvider.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass9 | NEEDS_HUMAN |

### `WebGoat_Code_SQLiteProfileProvider.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass9 | FAIL |

### `WebGoat_Code_SQLiteRoleProvider.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass9 | FAIL |

### `WebGoat_Configuration_Default.config`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass2 | PASS |
| results_qwen3-coder-30b_temp1.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass5 | PASS |
| results_qwen3-coder-30b_temp1.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass7 | PASS |
| results_qwen3-coder-30b_temp1.0_pass8 | PASS |
| results_qwen3-coder-30b_temp1.0_pass9 | NEEDS_HUMAN |

### `WebGoat_Content_About.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | PASS |
| results_qwen3-coder-30b_temp1.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass11 | PASS |
| results_qwen3-coder-30b_temp1.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass8 | PASS |
| results_qwen3-coder-30b_temp1.0_pass9 | PASS |

### `WebGoat_Content_About.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | PASS |
| results_qwen3-coder-30b_temp1.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass11 | UNKNOWN |
| results_qwen3-coder-30b_temp1.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass3 | PASS |
| results_qwen3-coder-30b_temp1.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass9 | NEEDS_HUMAN |

### `WebGoat_Content_BasicAuth.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass9 | FAIL |

### `WebGoat_Content_BasicAuth.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass9 | NEEDS_HUMAN |

### `WebGoat_Content_Challenge1.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass4 | PASS |
| results_qwen3-coder-30b_temp1.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass9 | NEEDS_HUMAN |

### `WebGoat_Content_Challenge1.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | PASS |
| results_qwen3-coder-30b_temp1.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass4 | PASS |
| results_qwen3-coder-30b_temp1.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass7 | PASS |
| results_qwen3-coder-30b_temp1.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass9 | NEEDS_HUMAN |

### `WebGoat_Content_Challenge2.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass9 | NEEDS_HUMAN |

### `WebGoat_Content_Challenge2.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass10 | PASS |
| results_qwen3-coder-30b_temp1.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass8 | PASS |
| results_qwen3-coder-30b_temp1.0_pass9 | NEEDS_HUMAN |

### `WebGoat_Content_Challenge3.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass12 | PASS |
| results_qwen3-coder-30b_temp1.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass8 | PASS |
| results_qwen3-coder-30b_temp1.0_pass9 | NEEDS_HUMAN |

### `WebGoat_Content_Challenge3.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass12 | PASS |
| results_qwen3-coder-30b_temp1.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass9 | NEEDS_HUMAN |

### `WebGoat_Content_ChangePwd.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass9 | FAIL |

### `WebGoat_Default.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass9 | FAIL |

### `WebGoat_Default.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass9 | NEEDS_HUMAN |

### `WebGoat_ForgotPassword.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass9 | NEEDS_HUMAN |

### `WebGoat_ForgotPassword.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass9 | NEEDS_HUMAN |

### `WebGoat_Global.asax.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass9 | FAIL |

### `WebGoat_LoginPage.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass9 | NEEDS_HUMAN |

### `WebGoat_LoginPage.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass9 | NEEDS_HUMAN |

### `WebGoat_ProxySetup.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass10 | PASS |
| results_qwen3-coder-30b_temp1.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass4 | PASS |
| results_qwen3-coder-30b_temp1.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass6 | PASS |
| results_qwen3-coder-30b_temp1.0_pass7 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass8 | PASS |
| results_qwen3-coder-30b_temp1.0_pass9 | NEEDS_HUMAN |

### `WebGoat_ProxySetup.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass12 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass2 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass8 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass9 | NEEDS_HUMAN |

### `WebGoat_Web.config`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass9 | FAIL |

### `WebGoat_WebGoat.NET.csproj`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass4 | PASS |
| results_qwen3-coder-30b_temp1.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass9 | NEEDS_HUMAN |

### `WebGoat_dbtest.aspx.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass10 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass11 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass3 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass4 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass5 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass6 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass9 | FAIL |

### `WebGoat_dbtest.aspx.designer.cs`

| Run | Verdict |
|---|---|
| results_qwen3-coder-30b_temp1.0_pass1 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass10 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass11 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass12 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass2 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass3 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass4 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass5 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass6 | NEEDS_HUMAN |
| results_qwen3-coder-30b_temp1.0_pass7 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass8 | FAIL |
| results_qwen3-coder-30b_temp1.0_pass9 | FAIL |