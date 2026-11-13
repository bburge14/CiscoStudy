# Security Principles, Terminology & Risk

Before you can defend a network you have to be able to *name* what you are
defending and what you are defending against. This first lesson builds the
vocabulary the rest of the course leans on: the three goals every control
ultimately serves, the design principles that shape a good defense, and the
risk words — threat, vulnerability, exploit, risk — that analysts throw around
all day and must use precisely.

## The CIA triad: the three goals of security

Every security control you will ever meet exists to protect one or more of three
properties. Together they are the **CIA triad**, and they are the yardstick for
"is this secure?"

> **Confidentiality** keeps information from being seen by those who shouldn't
> see it. **Integrity** keeps information from being altered by those who
> shouldn't alter it (so you can trust it is accurate). **Availability** keeps
> information and systems reachable by those who legitimately need them.

A quick way to feel the difference:

- **Confidentiality** — encrypting a database so a stolen copy is unreadable.
  Broken by eavesdropping, theft, or a careless disclosure.
- **Integrity** — a file hash or a digital signature that proves a record was
  not tampered with. Broken by unauthorized modification.
- **Availability** — redundant servers and backups so a service stays up.
  Broken by a denial-of-service attack, hardware failure, or ransomware.

The triad is a lens, not a checklist. When you triage an alert, ask *which
property is threatened?* A data-exfiltration alert is a confidentiality problem;
a defaced web page is integrity; a flood of SYN packets is availability.

## Defense in depth: never rely on one wall

No single control is perfect, so good architecture layers them. **Defense in
depth** (also called a layered defense) assumes that any one safeguard can fail
and places others behind it.

> **Defense in depth** is the practice of layering independent, overlapping
> controls so that if one fails, another still stands between the attacker and
> the asset.

Picture a medieval castle: a moat, then walls, then a locked keep, then guards.
An attacker who swims the moat still faces the wall. In a network the layers
might be a perimeter firewall, network segmentation, host hardening, endpoint
detection, least-privilege accounts, and user training — each catching what the
layer before it missed. The lesson for an analyst: a successful attack usually
means *several* controls were bypassed, and your job is to find where the chain
held and where it broke.

## Core security principles and terms

A handful of design principles come up constantly, both on the job and on the
exam. Learn them as crisp one-liners:

- **Principle of least privilege** — every user, process, and service gets only
  the access its job requires, and nothing more. A SOC analyst who only needs to
  read logs should not hold domain-admin rights.
- **Separation of duties** — split a sensitive task so no single person can
  complete it alone (and quietly abuse it). The person who requests a payment
  cannot also approve it.
- **Dual control / two-person rule** — two people must act together for a
  critical operation (think of two keys to launch).
- **Need to know** — access is limited to the specific information a person
  needs for a task, a tighter idea than least privilege applied to data.
- **Non-repudiation** — strong proof that a specific party performed an action,
  so they cannot credibly deny it (digital signatures provide this).
- **Authentication, authorization, accounting (AAA)** — *prove who you are*,
  *decide what you may do*, *record what you did*.

These principles are *how* we reach the CIA goals. Least privilege and
separation of duties shrink what a compromised account can do; accounting and
non-repudiation support integrity and investigations.

## The language of risk

Analysts must separate four words that casual speech blurs together. Get these
exactly right.

> A **threat** is a potential danger. A **vulnerability** is a weakness that a
> threat could use. An **exploit** is the actual tool or technique that takes
> advantage of a vulnerability. **Risk** is the likelihood that a threat
> exploits a vulnerability, combined with the impact if it does.

| Term | Plain meaning | Example |
|------|---------------|---------|
| **Asset** | Something of value you protect | A customer database |
| **Vulnerability** | A weakness that could be exploited | An unpatched web server |
| **Threat** | A potential cause of harm | A ransomware gang |
| **Threat actor** | The entity behind a threat | The gang's operators |
| **Exploit** | The means of abusing a vulnerability | The code that triggers the flaw |
| **Risk** | Likelihood × impact | The chance that gang encrypts the database, and what it would cost |

A useful sentence that ties them together: *a **threat actor** uses an
**exploit** against a **vulnerability** in an **asset**, and the **risk** is how
likely that is and how badly it would hurt.* Notice that **risk only exists when
a threat and a vulnerability meet**. A flaw nobody can reach, or a threat with
no weakness to target, carries little risk — which is exactly why we both patch
vulnerabilities (remove the weakness) and monitor for threats (catch the actor).

A few more terms you will hear:

- **Exploit vs. zero-day** — a **zero-day** is a vulnerability with no patch
  available yet, so defenders have had "zero days" to fix it.
- **Threat intelligence** — curated information about active threats and their
  techniques, used to anticipate and detect attacks.
- **Indicator of compromise (IOC)** — an observable clue that a system was
  attacked (a malicious hash, IP, or domain). We will use IOCs throughout the
  host- and network-analysis units.

## Putting it together

A SOC analyst thinks in these terms all day. An alert arrives; you ask which
**CIA** property is at stake, you map the event to the **vulnerability** it
abused and the **threat actor** likely behind it, you judge the **risk** to
decide urgency, and you trust that **defense in depth** gave you more than one
chance to catch it. Everything later in this course — monitoring data, host
artifacts, packet analysis, incident response — is built on this foundation.

## Exam focus

- **CIA triad**: confidentiality = no unauthorized *viewing*; integrity = no
  unauthorized *altering* (data is accurate and trustworthy); availability =
  legitimate users can *reach* it. Match the scenario to the property.
- **Defense in depth** = layered, overlapping, independent controls; one layer
  failing does not mean the asset is lost.
- **Least privilege** = only the access the job needs. **Separation of duties**
  = no single person can complete and abuse a sensitive task alone.
- Keep the risk words straight: **threat** (potential danger) vs.
  **vulnerability** (the weakness) vs. **exploit** (the technique that abuses it)
  vs. **risk** (likelihood × impact). **Risk requires both a threat and a
  vulnerability.**
- A **zero-day** has no patch yet. An **IOC** is an observable sign of
  compromise. **Non-repudiation** = proof an action can't be denied.
