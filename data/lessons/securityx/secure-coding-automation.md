# Secure Coding & Security Automation

Software is where most vulnerabilities are born, and automation is how a modern
security team keeps up with the scale and speed of that software. This lesson joins
**secure coding / DevSecOps** — baking security into the development pipeline — with
**security automation and orchestration** — using code and playbooks to enforce and
respond faster than humans can. Both reflect a shift-left, build-it-in philosophy.

## Secure coding and the secure SDLC

The cheapest vulnerability to fix is the one caught before it ships. A **secure
software development lifecycle (SDLC)** embeds security at every phase — threat
modeling in design, secure coding standards in development, security testing in QA,
and hardening in deployment. **DevSecOps** operationalizes this by integrating
security directly into the CI/CD pipeline so it runs automatically on every change.

### The testing tools: SAST, DAST, IAST, SCA

Know these four by *what they analyze and when* — the exam pairs the description to
the acronym constantly.

| Tool | What it does | When |
|------|--------------|------|
| **SAST** | **Static** analysis of **source code without executing it** | Earliest — IDE, pull request |
| **DAST** | **Dynamic** testing of a **running** application from the outside | Later — running/staged app |
| **IAST** | **Interactive** — instruments the app to analyze from inside during tests | During functional/QA testing |
| **SCA** | **Software Composition Analysis** — scans **open-source dependencies** for known **CVEs** and risky licenses | Continuous, in the build |

> **SAST** = analyze source **without running it**, early and in the IDE/PR. **DAST**
> = test the **running** app from outside. **SCA** = flag **known-vulnerable
> dependencies/licenses** in third-party libraries. If the pipeline pulls hundreds
> of open-source packages, **SCA** is what catches the vulnerable ones.

### Hardening the CI/CD supply chain

A build pipeline is a high-value target: compromise it and you poison everything it
ships (the supply-chain attack pattern). The practices that most directly reduce the
risk of malicious code or secrets entering a build:

- **Secrets management** — never hardcode credentials; pull them from a **vault** at
  runtime, and scan commits to block secret leakage.
- **Signed commits and artifact/code signing** with provenance (e.g., attestations)
  so only verified builds are promoted.
- **Dependency pinning and verification** (lockfiles, checksums) and a **private,
  curated registry** to resist dependency-confusion and typosquatting.
- **Least-privilege pipeline identities** and **protected branches** with mandatory
  review.
- **SCA + SAST gates** that fail the build on critical findings.

> Two practices that most directly cut supply-chain risk in CI/CD: **manage secrets
> in a vault (no hardcoding)** and **verify dependencies / sign artifacts**.

### The classes of bug to design out

Secure coding targets the usual suspects (the **OWASP Top 10** mindset):
**injection** (parameterized queries/prepared statements defeat SQLi), **cross-site
scripting** (output encoding + CSP), **broken access control**, **insecure
deserialization**, and **SSRF**. The unifying rule is **validate all input and
encode all output**, and treat every external input as hostile.

## Security automation and orchestration

Automation turns repeatable security work into code, cutting response time from
hours to seconds and removing human error from routine tasks.

### SOAR: the response engine

**SOAR (Security Orchestration, Automation, and Response)** integrates the security
toolset and executes **playbooks** — automated, repeatable response sequences. A
confirmed-phishing alert can automatically pull the message from every mailbox,
block the sender, and open a ticket, all without an analyst clicking through five
consoles. SOAR is the answer for "a platform that integrates tools and runs
automated response playbooks to accelerate incident handling."

> **SOAR** = integrate security tools + run automated **playbooks** to speed
> response. It sits on top of the SIEM and acts on what detection surfaces.

### Infrastructure as Code and policy as code

- **Infrastructure as Code (IaC)** — define the environment (networks, VMs, policy)
  in version-controlled templates so every deployment is **identical** and security
  baselines are enforced automatically. **Drift** — unplanned divergence from the
  defined state — is detected and auto-corrected back to the template. IaC is the
  answer for "every cloud environment deployed identically with baselines enforced
  and drift corrected."
- **Policy as Code / guardrails** — express compliance rules as code that blocks
  non-compliant deployments *before* they reach production.

### Automation's own risks

Automation is powerful enough to cause harm at machine speed. Leadership's worry is
legitimate: an auto-containment rule that isolates any confirmed-malware host could
mistakenly **isolate a critical production server** and cause an outage. The mature
mitigations:

- **Human-in-the-loop approval** for high-impact actions (a tiered model: auto-
  contain low-risk hosts, require approval for critical ones).
- **Allowlists/exclusions** that protect critical assets from automated containment.
- **Thorough testing** of playbooks, **change control**, and **logging/rollback**.

> Automated containment can take down a critical system by mistake. The fix is not
> to abandon automation but to add **human approval for high-impact actions** and
> **exclude critical assets** — tiered automation, not all-or-nothing.

## Exam focus

- **SAST** = static, source, no execution, early; **DAST** = dynamic, running app,
  outside-in; **IAST** = instrumented during tests; **SCA** = known-vulnerable
  **open-source dependencies/licenses**.
- Harden CI/CD against supply-chain attacks with **vaulted secrets (no
  hardcoding)**, **signed/verified artifacts and dependencies**, least-privilege
  pipeline identities, and SAST/SCA build gates.
- Secure coding rule of thumb: **validate input, encode output**; parameterized
  queries defeat SQL injection.
- **SOAR** integrates tools and runs **playbooks** to automate/accelerate response
  (sits above the SIEM).
- **IaC** gives identical, baseline-enforced deployments and **drift** correction;
  **policy as code** blocks non-compliant deploys.
- Guard automation itself with **human-in-the-loop approval for high-impact
  actions** and **exclusions for critical assets** so auto-containment can't take
  down production.
