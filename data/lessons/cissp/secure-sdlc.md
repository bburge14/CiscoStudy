# Secure SDLC & DevSecOps

Software is where most breaches ultimately live, and the cheapest place to fix a
security flaw is before it ships. Domain 8 asks you to think like a manager who
builds security *into* the way software is made rather than bolting it on
afterward. This lesson covers securing the software development lifecycle and the
DevSecOps practices that carry that discipline into modern, fast-moving pipelines.

## Security across the SDLC

The **Software Development Lifecycle (SDLC)** is the sequence from idea to
retirement. Security belongs in **every** phase, not a single gate at the end.

| Phase | Security activity |
|-------|-------------------|
| **Requirements** | Define security and privacy requirements alongside functional ones |
| **Design** | **Threat modeling**, secure architecture, attack-surface review |
| **Development** | Secure coding standards, SAST, peer review |
| **Testing** | DAST, fuzzing, security test cases |
| **Deployment** | Secure configuration, hardening, change control |
| **Operations / maintenance** | Patching, monitoring, vulnerability management |
| **Disposal** | Secure decommissioning, data sanitization |

> The governing principle is **shift left**: the earlier a flaw is caught, the
> cheaper it is to fix. A security requirement missed in design can cost orders of
> magnitude more to remedy once the software is in production.

**Threat modeling** in the design phase is the highest-leverage activity. The
**STRIDE** framework enumerates threat categories: **S**poofing, **T**ampering,
**R**epudiation, **I**nformation disclosure, **D**enial of service, and
**E**levation of privilege. Modeling these against the design surfaces risks while
they are still cheap to address.

## Development models and environment separation

Development methodologies shape how security is applied, not whether it's needed:

- **Waterfall** — sequential phases; security gates fit naturally but late feedback
  is costly.
- **Agile** — iterative sprints; security must be woven into each iteration
  (security user stories, definition of done).
- **Spiral** — risk-driven iterations.
- **DevOps / DevSecOps** — continuous integration and delivery with security
  automated into the pipeline.

A non-negotiable, heavily tested control is **environment separation**:

> Keep **development, testing, and production** environments **separate**. Changes
> are built and verified in dev/test and then **promoted to production through
> change control**. Developers must **never debug directly on live production using
> real customer data** — it risks outages, bypasses review, and exposes sensitive
> data in an uncontrolled place.

## Maturity models

How mature is an organization's software-security practice? Maturity models
benchmark it:

- **CMMI (Capability Maturity Model Integration)** — five levels from *Initial*
  (ad hoc) to *Optimizing* (continuous improvement); a general process-maturity
  model.
- **OWASP SAMM (Software Assurance Maturity Model)** and **BSIMM** — specifically
  measure and guide software-security maturity.

These let management answer "how disciplined are we, and what should we improve
next?" rather than guessing.

## DevSecOps and the software supply chain

**DevSecOps** integrates security directly into the **CI/CD pipeline** so that
security checks run automatically on every build — not as a quarterly audit.
Hallmarks:

- **Automated security testing** (SAST, DAST, dependency scanning) gating the
  pipeline.
- **Security as code / policy as code** — security rules versioned and enforced
  automatically.
- **Infrastructure as Code (IaC)** scanning — catch insecure cloud configurations
  before they deploy.
- **Secrets management** — keep credentials out of source code; use a vault.

The modern frontier is **software supply-chain security**, now prominent enough to
be its own OWASP Top 10 category. The key artifact:

> An **SBOM (Software Bill of Materials)** is a formal, often machine-readable
> **inventory of every component and version** in an application. When a new
> vulnerability is disclosed in a library (think Log4j), the SBOM lets you instantly
> determine whether — and where — you are exposed.

Supporting practices: **Software Composition Analysis (SCA)** scans third-party and
open-source dependencies for known vulnerabilities and license issues, and
**dependency pinning plus provenance/signing** guard against tampered or malicious
packages entering the build.

> The managerial takeaway: you are responsible for the security of code you didn't
> write but did ship. Visibility into dependencies (via an SBOM and SCA) is what
> turns an unknowable supply chain into a manageable risk.

## Acquired and third-party software

Not all code is written in house. Commercial off-the-shelf (COTS), open-source, and
outsourced software carry risk you must manage without owning the source.

- **Vendor assessment** — evaluate a supplier's security practices before buying
  (review their SOC 2 report, security questionnaires, track record).
- **Source code escrow** — a neutral third party holds the source so you can
  maintain the product if the vendor goes out of business or is acquired.
- **Contractual security requirements** — write patching commitments, vulnerability
  disclosure, and right-to-audit clauses into the contract.
- **Ongoing monitoring** — a vendor's posture at signing is not its posture
  forever; reassess periodically.

> The managerial point: outsourcing the work does **not** outsource the
> accountability. You still own the risk of software you ship, so due diligence on
> suppliers is part of the secure SDLC.

## Exam focus

- Build security into **every SDLC phase**; **shift left** because early fixes are
  far cheaper. **Threat model** in design using **STRIDE** (Spoofing, Tampering,
  Repudiation, Information disclosure, DoS, Elevation of privilege).
- **Separate dev/test/production**; promote changes through **change control**;
  **never debug on production with real data**.
- Maturity models: **CMMI** (general, 5 levels), **OWASP SAMM / BSIMM**
  (software-security specific).
- **DevSecOps** automates security into **CI/CD** (SAST/DAST/SCA gates, IaC
  scanning, secrets management, security as code).
- **SBOM** = component/version inventory for **supply-chain** impact analysis;
  **SCA** scans dependencies for known vulnerabilities. You own the risk of the
  components you ship.
- For **acquired/third-party software**: **vendor assessment**, **source code
  escrow**, and **contractual security requirements** — outsourcing the work
  doesn't outsource the accountability.
