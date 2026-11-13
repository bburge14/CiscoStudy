# Hacking Web Applications & the OWASP Top 10

Web applications are custom code, and custom code has custom bugs. This is the
richest vulnerability area on the exam, organized for years around the **OWASP Top
10** — a community list of the most critical web application security risks. We
teach every class by *definition and fix*, never as a working exploit: knowing what
SSRF or XSS *is* and how to prevent it is exactly what the exam and the job require.

## The OWASP Top 10

> **The OWASP Top 10 is a regularly updated, consensus list of the most critical
> web application security risks.** It is a prioritization guide, not an exhaustive
> standard.

The list is periodically revised. The current edition is **2025**; the long-lived
**2021** edition is what older courseware (CEH v13 included) often cites, so know
both mappings.

| # | OWASP Top 10 **2025** (current) | OWASP Top 10 **2021** |
|---|----------------------------------|------------------------|
| A01 | Broken Access Control | Broken Access Control |
| A02 | Security Misconfiguration | Cryptographic Failures |
| A03 | Software Supply Chain Failures | Injection |
| A04 | Cryptographic Failures | Insecure Design |
| A05 | Injection | Security Misconfiguration |
| A06 | Insecure Design | Vulnerable and Outdated Components |
| A07 | Authentication Failures | Identification and Authentication Failures |
| A08 | Software or Data Integrity Failures | Software and Data Integrity Failures |
| A09 | Security Logging and Alerting Failures | Security Logging and Monitoring Failures |
| A10 | Mishandling of Exceptional Conditions | Server-Side Request Forgery (SSRF) |

Two notes that are easy exam points: **Broken Access Control is #1 in both
editions**, and in **2025 SSRF was folded into Broken Access Control** while two
new categories appeared — **Software Supply Chain Failures** and **Mishandling of
Exceptional Conditions**.

## The flaw classes you must define

### Broken access control

Users doing things they should not be allowed to do. A common instance is **IDOR
(Insecure Direct Object Reference)** — changing an identifier in a request to reach
another user's record. *Fix:* enforce authorization **server-side** on every
request; deny by default.

### Injection

Untrusted input is interpreted as code or commands:

- **Cross-Site Scripting (XSS)** — injecting script that runs in another user's
  browser. It comes in **stored**, **reflected**, and **DOM-based** forms. *Fix:*
  **output encoding** plus a **Content-Security-Policy (CSP)**.
- **OS command injection** — user input is passed unsanitized into a server-side
  shell call, letting an attacker run system commands on the host. *Fix:* avoid
  shell calls; use safe APIs and strict input validation.
- **SQL injection** gets its own lesson next.

### Server-Side Request Forgery (SSRF)

> **SSRF abuses a vulnerable feature to make the server itself fetch a URL of the
> attacker's choosing**, reaching internal-only services or a **cloud metadata
> endpoint** (the link-local `169.254.169.254` address) to steal credentials.

*Fix:* validate and allowlist outbound destinations, block link-local/internal
ranges, and require authentication on internal services.

### Cross-Site Request Forgery (CSRF)

Tricking a logged-in user's browser into submitting an unwanted request. *Fix:*
**anti-CSRF tokens** and the **`SameSite`** cookie attribute.

### The rest, briefly

- **Security misconfiguration** — insecure defaults, verbose errors, open cloud
  storage. *Fix:* hardening baselines.
- **Cryptographic failures** — weak or missing encryption of data in transit/at
  rest. *Fix:* strong TLS and algorithms.
- **Authentication failures** — weak passwords, broken session handling. *Fix:*
  MFA, secure session management.
- **Software supply chain / vulnerable components** — flaws in third-party
  dependencies. *Fix:* inventory (SBOM), patching, verified sources.
- **Insecure design** — missing security at the design stage. *Fix:* threat
  modeling and a secure SDLC.
- **Unrestricted file upload** — accepting executable or malicious files. *Fix:*
  validate type/content, store outside the web root, never execute uploads.

## Tools for recognition

**Burp Suite** and **OWASP ZAP** are intercepting proxies and scanners used in
authorized testing to observe and manipulate requests. Name them for what they are:
assessment tools, used with permission.

## The unifying defenses

Most of the list collapses into a short list of habits:

- **Validate input, encode output** — the core of stopping injection and XSS.
- **Parameterized queries** — for database access (next lesson).
- **Enforce authorization server-side** — for access control.
- **Security headers** — CSP, HSTS, `X-Frame-Options`, and `SameSite` cookies.
- **Least privilege** — for the app's database and service accounts.
- **A secure SDLC** — threat modeling, dependency management, and testing baked in.
- **A WAF** — as defense-in-depth, not a substitute for fixing the code.

## Exam focus

- **OWASP Top 10** = the top web app risk categories; **Broken Access Control is
  #1** in both the current **2025** and the **2021** editions. In **2025**, **SSRF
  moved into Broken Access Control**, and **Software Supply Chain Failures** and
  **Mishandling of Exceptional Conditions** are the new entries.
- **SSRF** = make the **server** fetch an attacker-chosen URL, often the **cloud
  metadata endpoint (169.254.169.254)**; fix with outbound allowlisting.
- **OS command injection** = unsanitized input reaches a server shell; fix with
  safe APIs and validation.
- **XSS** (stored/reflected/DOM) → **output encoding + CSP**; **CSRF** →
  **anti-CSRF tokens + SameSite**; **IDOR** → **server-side authorization**.
- **Burp Suite / OWASP ZAP** are authorized testing proxies.
- The master defenses: **validate input, encode output, parameterize queries,
  enforce authz server-side, and use security headers**.
