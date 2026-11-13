# Microsoft Purview, Zero Trust & Privacy

Protecting identities and endpoints is only half of security. The other half is
governing **data** — classifying it, preventing its leakage, retaining it, and
proving you handle it responsibly — and understanding the **model and principles**
that tie everything together. This lesson covers **Microsoft Purview** for
compliance and the **Zero Trust** model and **privacy** commitments behind
Microsoft 365.

## Microsoft Purview: governance and compliance

> **Microsoft Purview** is Microsoft's unified brand for **data governance, risk,
> and compliance**. It brings capabilities for classifying, protecting, retaining,
> and investigating data under one roof (it replaced the older Microsoft 365
> compliance center).

Purview is a suite of solutions, each answering a different compliance question.
The exam tests whether you can match the need to the solution:

- **Compliance Manager** — a dashboard that **scores your compliance posture**,
  **maps controls to regulations** like GDPR and ISO 27001, and hands you prioritized
  **improvement actions**. If a scenario wants a compliance *score* against
  regulations, it's Compliance Manager.
- **Sensitivity labels (Information Protection)** — **classify and protect** data
  by applying labels (e.g. *Confidential*) that can **encrypt**, watermark, or
  restrict a file wherever it travels.
- **Data Loss Prevention (DLP)** — automatically **detect and block the sharing of
  sensitive information** (credit-card or ID numbers) across email, Teams, and
  endpoints.
- **Insider Risk Management** — detect and investigate **risky internal activity**,
  such as a **departing employee** quietly copying confidential files.
- **Communication Compliance** — **monitor messages** in Teams and email for policy
  violations like **harassment** or sharing of sensitive content.
- **Records Management / retention** — declare documents as immutable **records**,
  and set **retention and deletion** policies so data is kept exactly as long as
  the rules require — no longer, no shorter.
- **eDiscovery** — **find, collect, and preserve** content across Microsoft 365 for
  a legal case or investigation.
- **Audit** — a searchable **log of user and admin activities** for investigations
  and compliance evidence.

> A quick decoder: **"score us against regulations"** = Compliance Manager;
> **"stop sensitive data from leaving"** = DLP; **"watch for a departing employee
> stealing files"** = Insider Risk Management; **"keep records for X years"** =
> Records Management.

## Zero Trust: the guiding model

All of these protections serve a single strategy. The old model trusted anything
inside the corporate network; Zero Trust throws that assumption out.

> **Zero Trust** assumes no request is trusted by default — not even one from
> inside the network. It rests on **three principles**: **verify explicitly**, use
> **least-privilege access**, and **assume breach**.

The three principles, in plain terms:

1. **Verify explicitly** — authenticate and authorize **every** request using all
   available signals (identity, device health, location, behavior). Nothing is
   waved through because of where it came from.
2. **Use least-privilege access** — give users only the access they need, for only
   as long as they need it (just-enough and just-in-time access), limiting the
   blast radius of any one account.
3. **Assume breach** — design as if attackers are already inside: **segment**
   access, **encrypt** data, and monitor everything, so a compromise is **contained**
   rather than catastrophic.

A closely related idea is **defense in depth** — stacking **multiple independent
layers** of protection (physical, identity, network, application, and data) so that
if one layer fails, others still stand. Zero Trust and defense in depth work
together: verify at every layer, and never rely on a single wall.

## Privacy and trust

Customers won't move their data to the cloud unless they trust how it's handled, so
Microsoft publishes its commitments openly. You should recognize these resources
and the principles behind them.

- **Microsoft's privacy principles** — Microsoft states that **you control your
  data**, it's handled with **transparency**, it's **protected by strong security
  and encryption**, Microsoft provides **strong legal protections**, your content
  is **not used for advertising**, and any data use **benefits you**.
- **The Microsoft Trust Center** — a **public website** that explains, in plain
  terms, how Microsoft approaches **privacy, security, and compliance** across its
  services. It's the "here's how we protect you" front door.
- **The Service Trust Portal (STP)** — the place to obtain Microsoft's
  **independent audit reports, certifications, and compliance documentation** (SOC,
  ISO, and others) that you can show your own auditors.
- **The Microsoft Privacy Statement** — the formal document describing what data
  Microsoft collects and how it's used.

The distinction the exam likes: the **Trust Center** *explains* the approach in
plain language, while the **Service Trust Portal** *delivers the evidence* (the
audit reports and certifications).

## The whole thing in one paragraph

**Microsoft Purview** unifies data governance and compliance: **Compliance Manager**
scores your posture against regulations, **sensitivity labels** classify and
encrypt data, **DLP** blocks sensitive-data sharing, **Insider Risk Management**
catches risky insiders, **Communication Compliance** monitors messages, **Records
Management** enforces retention, and **eDiscovery** and **Audit** support
investigations. It all serves **Zero Trust** — **verify explicitly**, **least-
privilege access**, **assume breach** — reinforced by **defense in depth**
(layered protection). Microsoft backs this with published **privacy principles**,
the plain-language **Trust Center**, and the **Service Trust Portal** for audit
reports and certifications.

## Exam focus

- **Microsoft Purview** = the unified **compliance/data-governance** brand. Match
  the solution: **Compliance Manager** (score vs. regulations), **DLP** (block
  sensitive-data sharing), **sensitivity labels** (classify/encrypt), **Insider
  Risk Management** (risky insiders/departing employee), **Communication
  Compliance** (monitor messages), **Records Management** (retention/records),
  **eDiscovery** (legal content search).
- **Zero Trust = three principles: verify explicitly, use least-privilege access,
  assume breach.** "Use all signals to authorize every request" = **verify
  explicitly**; "contain the damage if they get in" = **assume breach**.
- **Defense in depth** = **multiple independent layers** of protection.
- **Trust Center** = plain-language explanation of privacy/security/compliance;
  **Service Trust Portal** = the **audit reports and certifications** themselves.
