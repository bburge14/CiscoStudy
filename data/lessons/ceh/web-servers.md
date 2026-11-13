# Hacking Web Servers

A web application has two layers an attacker can target: the **server** that hosts
it and the **application code** that runs on it. This lesson is about the server —
the Apache, Nginx, or IIS software and its configuration. Server attacks rarely
need clever code; they feed on defaults left on, patches not applied, and features
nobody turned off. The good news is that the same facts make the defenses obvious.

## Server vs application

> The **web server** is the platform software and its configuration that delivers
> content over HTTP/S. The **web application** is the custom code running on top.
> This lesson covers the server; the next covers the app.

Knowing which layer a flaw lives in matters: a server flaw is usually fixed by
**patching and configuration**, while an app flaw is fixed in **code**.

## Where web servers go wrong

### Misconfiguration

The leading cause of web-server compromise is misconfiguration:

- **Default accounts and passwords** left enabled.
- **Directory listing** turned on, exposing files when no index page exists.
- **Verbose error messages** that leak paths, versions, and stack traces.
- **Unnecessary modules, sample apps, and admin consoles** left installed.

### Unpatched software

Running a known-vulnerable version invites exploitation of a published **CVE**.
Attackers fingerprint the server version (via banners and headers) and look up
matching flaws — which is why **banner/version disclosure** is itself a weakness.

### Dangerous HTTP methods

HTTP defines methods beyond GET and POST. Some are risky if left enabled:

> If **PUT** and **DELETE** are unnecessarily enabled, an attacker may be able to
> **upload or delete files** on the server. **TRACE** can enable cross-site tracing
> (XST). Disable any method the application does not require.

### Directory (path) traversal

> **Directory traversal** abuses insufficient input handling to escape the web
> root (using `../`-style sequences) and read files elsewhere on the server, such
> as configuration or password files.

Teach it by definition and fix: the server and app must **canonicalize and
validate paths** and never pass user input straight to the filesystem.

### Defacement and disclosure

> **Website defacement** is altering the visual content of an organization's public
> pages to display the attacker's message — primarily to embarrass the victim and
> damage its reputation.

Servers also leak through **misconfigured permissions**, exposed backup files, and
**WebDAV** left open for writing.

## Tools for recognition

- **Nikto** — scans a web server for known misconfigurations, dangerous methods,
  outdated software, and default files.
- **Banner grabbing** — reading the `Server` header and error pages to identify
  version and platform.

These *identify* weaknesses; they are reconnaissance and assessment aids, not
exploitation engines.

## Hardening a web server

Every issue above has a direct control:

- **Patch promptly** — keep the server software and modules current.
- **Harden the configuration** — disable directory listing, remove sample content
  and default accounts, and show generic error pages.
- **Disable unused HTTP methods** (especially **PUT/DELETE/TRACE**) and unneeded
  modules.
- **Suppress version banners** so fingerprinting is harder.
- **Run the service as a least-privilege account**, not root/SYSTEM.
- **Enforce TLS** for all traffic.
- **Validate and canonicalize file paths** to stop traversal.
- **Put a WAF in front** to filter known attack patterns.
- **File integrity monitoring** to detect defacement and unauthorized changes fast.

> The pattern to internalize: web-server security is overwhelmingly about *reducing
> surface and keeping current* — turn off what you do not need, hide what you do
> not have to reveal, and patch the rest.

## The hardening mindset

Notice the pattern in every fix above: web-server security is mostly *subtraction*.
You are not adding clever defenses so much as removing what should never have been
exposed — default accounts, sample apps, verbose errors, unused methods, version
banners, and write access. A practical baseline captures this as a repeatable
checklist applied to every new server, so hardening is neither reinvented nor
forgotten each time.

### Keeping it hardened

Hardening is not a one-time event. New modules, quick fixes, and emergency changes
erode a baseline over time — configuration **drift**. **File integrity monitoring**
and periodic re-scans with a tool like Nikto catch both an attacker's changes and an
administrator's well-meaning ones, so the server that was hardened on day one is
still hardened on day ninety.

## Exam focus

- Distinguish **web server** (platform/config, fixed by patching/hardening) from
  **web application** (custom code, fixed in code).
- **Website defacement** = changing public page content to embarrass the victim.
- **PUT and DELETE** are the dangerous HTTP methods that can let an attacker
  **upload or delete files** — disable methods the app does not need (watch for
  "choose two").
- **Directory/path traversal** uses `../` to read files outside the web root; fix
  with **path validation/canonicalization**.
- **Misconfiguration, default credentials, unpatched versions, and banner
  disclosure** are the core server weaknesses.
- **Nikto** is the go-to **web-server scanner**; defenses are **patch, harden,
  disable unused methods/modules, least privilege, TLS, and a WAF**.
