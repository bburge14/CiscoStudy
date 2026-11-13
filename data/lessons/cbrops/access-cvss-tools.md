# Access Control Models, CVSS & SOC Tooling

This lesson covers three practical skills. First, how systems decide *who may
touch what* — the four access-control models. Second, how the industry puts a
number on *how bad a vulnerability is* — the Common Vulnerability Scoring System
(CVSS). Third, the two platforms that sit at the center of a modern security
operations center — the **SIEM** and the **SOAR**.

## Access control models

When a subject (a user or process) asks to use an object (a file, a service),
something has to decide yes or no. *How* that decision is made defines the
**access control model**. Four show up on the exam.

> **DAC** lets the resource **owner** set permissions. **MAC** enforces
> system-wide **labels** no user can override. **RBAC** grants access by
> **role/job function**. **ABAC** decides from **attributes** (of the user,
> resource, and context).

- **Discretionary Access Control (DAC)** — the *owner* of a resource decides who
  else may use it and sets the permissions directly. The file permissions you
  set on your own documents are DAC: flexible, but only as disciplined as the
  owner. "Discretionary" = at the owner's discretion.
- **Mandatory Access Control (MAC)** — the *system* enforces access from
  security **labels** (for example *Confidential*, *Secret*, *Top Secret*).
  Users cannot change the labels or hand out access, even to files they created.
  Rigid and high-assurance; think military and classified systems.
- **Role-Based Access Control (RBAC)** — permissions attach to **roles** (job
  functions), and users inherit them by being assigned a role. A new analyst
  added to the "SOC Tier 1" role instantly gets exactly that role's access.
  Easy to administer at scale; most enterprises use it.
- **Attribute-Based Access Control (ABAC)** — a policy engine evaluates
  **attributes** — who the user is, what the resource is, time of day, device
  posture, location — and decides dynamically. "Allow finance staff to open
  payroll files only from a managed device during business hours" is ABAC.

A fifth term, **rule-based access control**, applies the *same* rules to
everyone regardless of identity — a firewall ACL that blocks a port for all
users is the classic example. Don't confuse it with *role*-based.

The quickest exam discriminator: *who holds the power?* Owner → **DAC**. System
labels → **MAC**. Job role → **RBAC**. A bundle of attributes/conditions →
**ABAC**.

## CVSS: scoring vulnerability severity

When a vulnerability is published, teams need a consistent way to compare "how
urgent is this one?" The **Common Vulnerability Scoring System (CVSS)**,
maintained by FIRST, produces a **0.0–10.0** score from a set of defined
metrics. CBROPS is built around **CVSS v3.1**, so learn its structure well.

> A CVSS score is built from three metric groups: the **Base** group (the
> intrinsic, unchanging characteristics of the flaw), the **Temporal** group
> (characteristics that change over time), and the **Environmental** group (how
> the flaw matters in *your* specific environment). Only the Base group is
> required; it yields the headline score.

### The Base metrics (v3.1)

The Base group has two halves — **exploitability** and **impact**:

| Metric | What it captures | Values |
|--------|------------------|--------|
| **Attack Vector (AV)** | How "remote" the attack can be | Network, Adjacent, Local, Physical |
| **Attack Complexity (AC)** | Conditions outside the attacker's control | Low, High |
| **Privileges Required (PR)** | Account level the attacker must already hold | None, Low, High |
| **User Interaction (UI)** | Must a victim do something? | None, Required |
| **Scope (S)** | Can the flaw affect resources beyond its own security authority? | Unchanged, Changed |
| **Confidentiality / Integrity / Availability (C/I/A)** | Impact on each CIA property | None, Low, High |

**Scope** trips people up: it is **Changed** when exploiting the component lets
the attacker impact a *different* security authority — for example a VM escape,
where a guest VM breaks out to affect the host/hypervisor beyond it.

### Severity bands

The numeric score maps to a qualitative rating. Memorize these ranges — they are
tested directly:

| Score | Rating |
|-------|--------|
| 0.0 | None |
| 0.1 – 3.9 | Low |
| 4.0 – 6.9 | Medium |
| 7.0 – 8.9 | High |
| 9.0 – 10.0 | Critical |

So a published base score of **9.8** is **Critical**; **5.4** is **Medium**. The
bands are inclusive at the low end of each range — 7.0 is already High.

The **Temporal** group adjusts for things like whether reliable exploit code
exists or an official patch is out. The **Environmental** group lets *you*
re-weight the score for your own deployment (a flaw in software you don't run is
irrelevant to you). *Current note:* **CVSS v4.0** (published 2023) refines this —
it adds an **Attack Requirements (AT)** base metric, renames Temporal to
**Threat**, and adds an optional **Supplemental** group — but the v3.1 structure
above is the model CBROPS tests.

## The SOC's core tooling: SIEM and SOAR

A SOC drowns in data unless something collects and makes sense of it. Two
platforms do that.

> A **SIEM** (Security Information and Event Management) **ingests, normalizes,
> and correlates** logs from across the environment to surface prioritized
> alerts. A **SOAR** (Security Orchestration, Automation, and Response) adds
> **automated, playbook-driven response** on top.

- **SIEM** — pulls logs from firewalls, servers, endpoints, IDS and more into
  one place, puts them in a common format, and **correlates** events across
  sources so a pattern no single log would reveal becomes one alert. It is the
  analyst's primary console for detection and investigation. Splunk, Elastic,
  and Microsoft Sentinel are examples.
- **SOAR** — takes the next step: when an alert fires, SOAR can **orchestrate**
  tools and run an automated **playbook** — enrich the alert with threat intel,
  open a ticket, isolate a host, or block an IP — reducing the manual toil of
  repetitive response. We return to playbooks and automation in the final unit.

The relationship is a pipeline: raw logs → **SIEM** detects and prioritizes →
analyst (or **SOAR**) responds. A SIEM tells you *something happened*; a SOAR
helps you *do something about it* consistently and fast.

## Exam focus

- Access-control models by *who decides*: **DAC** = owner sets permissions; **MAC**
  = system-enforced labels users can't override; **RBAC** = access by job role;
  **ABAC** = decided from attributes/conditions. **Rule-based** applies one rule
  to everyone (e.g., a firewall ACL).
- **CVSS** scores run **0.0–10.0** across three groups: **Base** (required,
  intrinsic), **Temporal** (changes over time), **Environmental** (your
  deployment). Know the Base metrics: **AV, AC, PR, UI, Scope, C/I/A**.
- **Scope = Changed** when the flaw affects a resource beyond its own security
  authority (e.g., VM escape).
- Severity bands: **0 None, 0.1–3.9 Low, 4.0–6.9 Medium, 7.0–8.9 High, 9.0–10.0
  Critical.** A 9.8 is Critical.
- **SIEM** = collect, normalize, **correlate** logs into alerts. **SOAR** = adds
  **automation/orchestration** and playbook-driven response.
