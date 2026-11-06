# Compliance, Privacy, Audits & Awareness

The last lesson of the track covers how an organization proves it's doing the
right things and keeps its people sharp. **Compliance and privacy** are about
obeying the rules (and the consequences of not). **Audits and assessments** are
how you *verify* security objectively. And **security awareness** is how you turn
your riskiest asset — people — into a line of defense.

## Compliance: obeying the rules

**Compliance** means meeting the laws, regulations, and standards that apply to
your organization (PCI DSS for card data, HIPAA for health data, GDPR for EU
privacy, and many more). It's not optional, and it's not just paperwork.

### Reporting and monitoring compliance

- **Compliance reporting** comes in two flavors: **internal** (to your own
  leadership) and **external** (to regulators or auditors).
- **Compliance monitoring** keeps you continuously in line. Its building blocks:
  - **Due diligence** — doing the homework to understand your obligations.
  - **Due care** — actually taking reasonable steps to meet them.
  - **Attestation and acknowledgement** — formally stating (and having staff
    confirm) that requirements are understood and met.
  - **Internal and external** monitoring, increasingly backed by **automation**.

> A useful pairing: **due diligence** is *investigating* what you need to do; **due
> care** is *doing* it. Diligence is the research; care is the action.

### Consequences of non-compliance

Ignoring the rules is expensive. The exam lists: **fines**, **sanctions**,
**reputational damage**, **loss of license** (you may be barred from operating),
and **contractual impacts** (breaching agreements with partners). These are why
compliance gets executive attention.

## Privacy: protecting personal data

**Privacy** is the slice of security focused on **personal data** — information
about identifiable people. It overlaps with compliance but has its own vocabulary.

### Legal reach

Privacy law applies at **local/regional**, **national**, and **global** levels,
and often reaches across borders. GDPR, for instance, protects EU residents'
data no matter where the company is.

### Key privacy roles and rights

- **Data subject** — the person the data is about. (You are the data subject of
  your own medical records.)
- **Controller** — decides *why and how* personal data is processed.
- **Processor** — processes the data *on behalf of* the controller.
- **Ownership** — who is accountable for the data.
- **Data inventory and retention** — knowing what personal data you hold and
  keeping it only as long as needed (and legally required).
- **Right to be forgotten** — a data subject's right to have their personal data
  erased on request.

> **Controller vs. processor** shows up in both privacy and governance questions:
> the **controller** calls the shots on *why/how*; the **processor** merely acts on
> the controller's instructions.

## Audits and assessments: proving it objectively

You don't get to just *say* you're secure — you prove it through **audits** and
**assessments**. The exam distinguishes who performs them.

- **Attestation** — a formal, often signed statement that something is true (e.g.
  "we meet this standard").
- **Internal audits** — performed by your own organization: **compliance** checks,
  an **audit committee**, and **self-assessments**. Cheaper and more frequent, but
  less independent.
- **External audits** — performed by outsiders: **regulatory** bodies,
  **examinations**, **assessments**, and **independent third-party audits**. More
  credible precisely *because* they're independent.

### Penetration testing

A **penetration test** goes beyond a scan: testers actively try to break in to
prove real-world impact. Know the dimensions:

- **Environments / knowledge levels:**
  - **Known environment** (white box) — testers get full information. Fast,
    thorough.
  - **Unknown environment** (black box) — testers get nothing, mimicking a real
    outside attacker. Realistic, slower.
  - **Partially known environment** (gray box) — some information; a middle ground.
- **Reconnaissance:**
  - **Passive recon** — gather info *without* touching the target (public records,
    OSINT). Quiet and undetectable.
  - **Active recon** — directly probe the target (scanning). Informative but
    detectable.
- **Postures:** **offensive** (red team, attacking), **defensive** (blue team,
  defending), and **integrated** (purple team, both working together); tests may
  also be **physical**.

> **Known vs. unknown environment** tracks how much the testers are told; **passive
> vs. active recon** tracks whether they touch the target. Passive = invisible,
> active = detectable.

## Security awareness: strengthening the human firewall

People cause most incidents, so training them is one of the highest-value controls
there is. A **security awareness program** builds secure habits across the
workforce.

### What to teach

- **Phishing** — run **campaigns** (simulated phishing emails), teach staff to
  **recognize** attempts, and give a clear way to **report** suspicious messages.
- **Anomalous behavior recognition** — spotting **risky**, **unexpected**, and
  **unintentional** behavior (in themselves and others).
- **User guidance and training** on **policies/handbooks**, **situational
  awareness**, **insider threat**, **password management**, **removable media and
  cables** (don't plug in that found USB), **social engineering**, **operational
  security (OPSEC)**, and **hybrid/remote work** safety.

### Running the program

Awareness isn't a one-time slideshow. It has a lifecycle:

- **Development** — build the program and materials.
- **Execution** — deliver the training.
- **Reporting and monitoring** — measure results, both **initial** (at onboarding)
  and **recurring** (ongoing refreshers), and track metrics like phishing
  click-through rates to see if it's working.

> The most effective awareness programs are **recurring and measured**, not a
> single annual video. People forget; reinforcement and metrics are what change
> behavior.

## The whole thing in one paragraph

**Compliance** means meeting laws and standards, proven through **internal/
external reporting** and **monitoring** (built on **due diligence** = research and
**due care** = action, plus attestation), with real **consequences** for failure
(fines, sanctions, reputational damage, loss of license, contractual impacts).
**Privacy** protects personal data across local/national/global law, with roles
like **data subject**, **controller** (decides why/how) and **processor** (acts for
the controller), plus **data inventory/retention** and the **right to be
forgotten**. **Audits and assessments** verify security — **internal** (cheaper,
self-run) vs. **external** (independent, credible), backed by **attestation** —
and **penetration testing** across **known/partially-known/unknown** environments
with **passive vs. active** recon and offensive/defensive/integrated postures.
Finally, **security awareness** turns people into defenders through phishing
campaigns, anomalous-behavior recognition, and broad user training, run as a
**recurring, measured** program (development, execution, monitoring).

## On the exam

- **Due diligence vs. due care:** diligence = *investigating* your obligations;
  care = *acting* to meet them. Research vs. action.
- **Controller vs. processor:** the controller decides the **why and how**; the
  processor just **acts on instructions**. The **data subject** is the person the
  data is about.
- **Right to be forgotten** = a data subject's right to have their data erased.
- **Internal vs. external audit:** external is more **independent and credible**;
  internal is cheaper and more frequent. **Attestation** is a formal signed
  statement of truth.
- Pen-test terms: **known = white box** (full info), **unknown = black box** (no
  info), **partially known = gray box**. **Passive recon** doesn't touch the
  target (undetectable); **active recon** does (detectable).
- Simulated **phishing campaigns** are the classic awareness tool; the best
  programs are **recurring and measured** (e.g. tracking click rates), not
  one-and-done.
- Found-USB and "don't plug in unknown media" scenarios map to **removable media**
  training under security awareness.
