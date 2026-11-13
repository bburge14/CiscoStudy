# Mitigation, Secure Coding & the SDLC

Finding a vulnerability is only half the job; the organization judges you on
whether it gets *fixed* — safely, verifiably, and without breaking the business.
This lesson covers the two ways weaknesses get closed: operational mitigation
(patch, compensate, or formally accept the risk) and secure coding (writing
software that isn't vulnerable in the first place). The framing throughout is
defensive — we name attacks only to describe the control that stops them.

## The four risk responses

Every finding ends in one of four decisions:

> **Mitigate** (reduce the risk with a control), **transfer** (shift the financial
> loss, e.g., buy **cyber insurance** to cover residual loss), **accept** (live
> with it, documented), or **avoid** (stop doing the risky thing).

- **Risk transference** is exactly the cyber-insurance case: you've mitigated what
  you can and insure the rest.
- **Formal risk acceptance** applies when a fix would cost far more than the asset
  is worth — but it must be **documented and signed off by the business owner**,
  never an analyst's silent decision.

## Patching done safely

When a tested vendor patch exists and nothing blocks deployment, **apply it
through the change-management process** — that is the most effective remediation.
But "just patch" has guardrails:

- **Test first.** Before rolling a patch to production ERP or kernel-critical
  servers, test it in a **staging / non-production environment** so you don't
  trade a vulnerability for an outage.
- **Phased (ring / canary) deployment.** Deploy a critical update to a small pilot
  group, watch for problems, then expand — so a bad patch can't take the whole
  fleet down at once.
- **Rollback (backout) plan.** The change ticket documents the exact steps to
  restore the previous state if the update fails.
- **Validate.** After the patch team reports a flaw fixed, **perform a validation
  rescan** of the affected hosts to confirm the vulnerability is actually gone —
  "reported fixed" is not "verified fixed."

## When you can't patch: compensating controls

Legacy, end-of-life, and operational-technology systems often *can't* take the
patch. You reduce risk around them instead:

- **Compensating controls** — for a revenue-critical app on an unpatchable EOL OS,
  wrap it in **isolation, a WAF, and strict access limits with monitoring**.
- **Network segmentation** — unpatchable ICS/SCADA devices that must stay online
  should be **segmented off the corporate LAN** so a compromise can't reach them.
- **Interim controls while a patch is pending** — a public-facing service that
  can't be patched for two weeks can be shielded with a **WAF or IPS signature**
  to block known exploit traffic and **firewall/ACL rules** restricting access.
- **Configuration hardening** — newly provisioned servers flagged for unnecessary
  services and lingering default accounts get the straightforward fix: **disable
  unneeded services and apply a secure baseline such as a CIS Benchmark**.

## Secure coding: stop the vulnerability at the source

The cheapest vulnerability is the one never written. CySA+ expects you to match a
web weakness to its *remediation*.

### Injection and SQL injection

> **Parameterized queries (prepared statements)** are the single most reliable fix
> for SQL injection: the database treats user input strictly as *data*, never as
> part of the SQL command, so a tautology like "make the WHERE clause always true"
> simply can't alter the query's logic.

Reinforce it with **least-privilege** database accounts and **server-side input
validation against an allowlist**. Under the **OWASP Top 10**, SQL injection and
similar flaws fall under **Injection**.

### Input validation and output encoding

- **Allowlist (whitelist) validation** — accept only the known-good set (e.g.,
  valid two-letter US state codes) and reject everything else. Allowlisting beats
  denylisting, which always misses a case.
- **Context-aware output encoding**, reinforced by a **Content Security Policy
  (CSP)**, is the direct fix for **cross-site scripting (XSS)** — encode
  user-supplied text so the browser renders it as text, not script.
- Know the XSS flavors: **stored (persistent) XSS** is saved on the server and
  served to every visitor (e.g., a poisoned comment field); **reflected XSS**
  bounces a single crafted request back into the response.

### The other usual suspects

- **CSRF (Cross-Site Request Forgery)** — stopped by **SameSite cookie
  attributes** and **per-session anti-CSRF (synchronizer) tokens**.
- **SSRF (Server-Side Request Forgery)** — an app fetching a user-supplied URL can
  be tricked into hitting internal targets like the cloud metadata endpoint
  (`169.254.169.254`) to steal instance credentials. Fix it by **validating/allowlisting
  outbound destinations and blocking the metadata endpoint**. SSRF is its own
  category (**A10**) in the OWASP Top 10 (2021).
- **Broken Access Control** — changing a numeric `account_id` in a URL to view
  another customer's data (an *insecure direct object reference*) is **Broken
  Access Control**, the **A01** category.
- **Hardcoded secrets** — a database password or API key committed in source code
  should be **removed from code, loaded at runtime from a secrets manager/vault,
  and the exposed credential rotated**.

### Build security into the SDLC

Don't bolt security on at the end — **shift left**. Integrating **SAST as a gate
in the CI/CD pipeline** (failing the build on high-severity findings) catches
vulnerabilities as early and cheaply as possible. Threat modeling during design
and secure-coding standards complete the picture.

> **Currency note:** CS0-003 references the **OWASP Top 10 (2021)** — A01 Broken
> Access Control through A10 SSRF. OWASP has since published a **2025** edition
> that reshuffles the list (for example, Security Misconfiguration rises and a
> Software Supply Chain Failures category is added). Learn the **2021** order for
> the exam, and recognize the 2025 update exists in practice.

## Exam focus

- Four risk responses: **mitigate, transfer** (cyber insurance), **accept**
  (documented, business-owner sign-off), **avoid**.
- Patch **through change management**, **test in staging**, use **ring/canary**
  rollout, keep a **backout plan**, and **validation-rescan** to confirm the fix.
- Can't patch? **Compensating controls** (isolation, WAF, strict access +
  monitoring), **network segmentation** for ICS/OT, **WAF/IPS + ACLs** as interim
  controls, **CIS Benchmark** hardening.
- **Parameterized queries** fix SQL injection (+ least-privilege DB, server-side
  allowlist validation); **allowlist** input validation beats denylist.
- **Context-aware output encoding + CSP** fix XSS; know **stored** vs **reflected**.
  **SameSite + anti-CSRF tokens** fix CSRF. **SSRF** → allowlist outbound + block
  the metadata endpoint.
- Map OWASP: **Injection** (SQLi), **Broken Access Control** (IDOR), **SSRF** (A10).
- Remove hardcoded secrets to a **vault** and **rotate** them; **shift left** by
  gating **SAST** in CI/CD.
