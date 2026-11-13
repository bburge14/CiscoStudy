# Secure Coding & Software Vulnerabilities

Most application breaches trace back to a handful of recurring mistakes. A CISSP
doesn't have to write the patch, but must recognize the vulnerability class, know
its root cause, and name the right defense. This lesson covers secure coding
practices and the vulnerability catalog — anchored on the OWASP Top 10 — that the
exam expects you to identify on sight.

## Secure coding practices

A few disciplined habits prevent the majority of application flaws.

- **Input validation** — treat all input as hostile. Prefer **allow-listing**
  (accept only known-good patterns) over deny-listing (blocking known-bad, which
  attackers evade). This is the first line against injection and many other attacks.
- **Parameterized queries / prepared statements** — the definitive fix for SQL
  injection; they separate code from data so user input can never be executed as a
  command.
- **Output encoding** — encode data for its context (HTML, URL, JS) so that
  attacker-supplied content is displayed, not executed — the core defense against
  cross-site scripting.
- **Least privilege** — run the app and its database account with only the rights
  they need, so a compromise is contained.
- **Secure defaults and fail-secure** — ship locked down; on error, deny rather
  than allow.
- **Safe error handling** — return generic errors to users; detailed stack traces
  belong in logs, not on screen where they leak internals.
- **Session management** — issue strong, random session tokens; expire and
  regenerate them; protect cookies.
- **Secrets management** — never hardcode credentials; load them from a vault.

> The through-line of secure coding: **never trust input, and never let data become
> code.** Most of the OWASP list is a variation on one of those two failures.

## The OWASP Top 10

The **OWASP Top 10** is the industry's reference list of the most critical web
application risks. The current edition is **OWASP Top 10:2025** (finalized in early
2026), the first update since the widely cited **2021** list. You should know both,
since the stable concepts carry across editions.

| 2025 rank | Category |
|-----------|----------|
| **A01** | **Broken Access Control** (now also absorbs SSRF) |
| A02 | Security Misconfiguration |
| A03 | **Software Supply Chain Failures** *(new, expands "vulnerable components")* |
| A04 | Cryptographic Failures |
| A05 | Injection |
| A06 | Insecure Design |
| A07 | Authentication Failures |
| A08 | Software or Data Integrity Failures |
| A09 | Logging & Alerting Failures |
| A10 | **Mishandling of Exceptional Conditions** *(new)* |

> **Broken Access Control remained #1 in both 2021 and 2025.** The 2025 update
> notably promoted **Security Misconfiguration** and added a dedicated **Software
> Supply Chain Failures** category — reflecting how much risk now comes from
> dependencies rather than your own code.

## The vulnerability catalog

Recognize each by its behavior and know its fix.

- **Injection (e.g., SQL injection)** — untrusted input is interpreted as a command.
  **Fix: parameterized queries + input validation.**
- **Cross-Site Scripting (XSS)** — attacker script runs in a victim's browser
  (stored, reflected, or DOM-based). **Fix: output encoding + a Content Security
  Policy.**
- **Broken access control / Insecure Direct Object Reference (IDOR)** — the app
  returns another user's record just by changing an ID in the URL because it never
  checks ownership. **Fix: enforce server-side, per-object authorization on every
  request.** This is the #1 risk.
- **Cross-Site Request Forgery (CSRF)** — a victim's browser is tricked into
  submitting an authenticated action they didn't intend. **Fix: anti-CSRF tokens,
  SameSite cookies.**
- **Server-Side Request Forgery (SSRF)** — the server is tricked into making
  attacker-chosen requests, classically to the cloud metadata endpoint
  (`169.254.169.254`) to steal instance credentials. **Fix: allow-list outbound
  destinations and block internal/metadata addresses.** (In 2025 OWASP folds SSRF
  under Broken Access Control.)
- **Buffer overflow** — writing beyond a buffer's bounds to corrupt memory or run
  code, common in C/C++. **Fix: bounds checking, memory-safe languages, and OS
  defenses — ASLR, DEP/NX, stack canaries.**
- **Insecure deserialization** — untrusted serialized data is reconstructed into
  objects, enabling code execution. **Fix: avoid deserializing untrusted data;
  validate and sign it.**
- **XML External Entity (XXE)** — a parser processes malicious external entity
  references to read files or reach internal systems. **Fix: disable external
  entity resolution.**
- **Race conditions (TOCTOU)** — a state change between a check and its use (see the
  architecture lesson). **Fix: locking, atomic operations.**

> Exam pattern: when a stem shows "change the ID in the URL to see someone else's
> data," the answer is **broken access control / IDOR**, fixed by **server-side
> authorization checks** — not by hiding the ID or using client-side controls,
> which attackers simply bypass.

## Client-side vs server-side: the golden rule

A recurring exam trap offers "fix it with client-side validation." Client-side
checks (JavaScript in the browser) improve the user experience by catching typos
early, but they provide **zero security** — an attacker simply bypasses the browser
and sends crafted requests straight to the server.

> **Every security decision — input validation, authorization, business rules —
> must be enforced on the server.** Client-side controls are a convenience, never a
> trust boundary. If an answer relies on hiding or validating something only in the
> browser (or on obscuring a URL parameter), it is wrong.

This is the same lesson that sinks IDOR: the server, not the client, must decide
what each authenticated user is allowed to see and do.

## Exam focus

- Secure coding rests on two ideas: **never trust input** (validate, prefer
  allow-lists) and **never let data become code** (parameterized queries, output
  encoding).
- The **OWASP Top 10:2025** is current (first update since **2021**).
  **Broken Access Control is #1 in both**; 2025 added **Software Supply Chain
  Failures** and **Mishandling of Exceptional Conditions**, promoted **Security
  Misconfiguration**, and absorbed **SSRF** into Broken Access Control.
- Map vulnerability → fix: **SQLi → parameterized queries**; **XSS → output
  encoding + CSP**; **IDOR/broken access control → server-side per-object authz**;
  **CSRF → anti-CSRF tokens**; **SSRF → allow-list outbound, block metadata
  `169.254.169.254`**; **buffer overflow → bounds checking + ASLR/DEP/canaries**.
- "Change the ID in the URL to read others' data" = **broken access control
  (IDOR)**, fixed server-side.
- **Enforce security on the server**, never client-side: browser validation is for
  UX only and is trivially bypassed.
