# Governance, Risk & Third-Party Risk

The final domain steps back from the technical controls and asks: *how is security
run as a business function?* That's **governance** (the rules and who sets them),
**risk management** (deciding which risks to accept, avoid, transfer, or reduce),
and **third-party risk** (managing the vendors and partners you depend on). This
is the "GRC" side of security, and it's heavier on process than on packets.

## Security governance: the rules and who makes them

**Governance** is the framework of policies, roles, and oversight that steers an
organization's security. It answers "who decides, and by what rules?"

### The documents, from firm to flexible

Security+ wants you to tell these apart — they differ in how binding they are:

| Document | What it is | Binding? |
|----------|-----------|----------|
| **Policy** | High-level statement of intent/goals | Mandatory |
| **Standard** | Specific mandatory requirements to meet a policy | Mandatory |
| **Procedure** | Step-by-step instructions to do a task | Mandatory |
| **Guideline** | Recommended best practice | Advisory (optional) |

> The hierarchy flows **policy → standard → procedure**, each more specific than
> the last. A **guideline** is the odd one out: it only *recommends*, it doesn't
> *require*.

Common **policies** include the **AUP (Acceptable Use Policy)**, information
security policy, **business continuity**, **disaster recovery**, **incident
response**, **SDLC (Software Development Life Cycle)**, and **change management**.
Common **procedures** include **change management**, **onboarding/offboarding**,
and **playbooks** (step-by-step responses to specific incidents).

### Who governs, and who owns the data

- **Governance structures** — oversight comes from **boards**, **committees**, and
  **government entities**, and can be **centralized** (one authority) or
  **decentralized** (spread across units).
- **External considerations** — **regulatory**, **legal**, **industry**, and
  the **local / regional / national / global** context all shape what you must do.
- **Roles for systems and data** (memorize these — the exam loves them):
  - **Owner** — accountable for the data; sets its classification.
  - **Controller** — decides *why and how* personal data is processed.
  - **Processor** — processes data *on behalf of* the controller.
  - **Custodian / steward** — handles day-to-day protection and management.

Governance isn't set-and-forget: **monitoring and revision** keep policies current
as the business and threats change.

## Risk management: deciding what to do about uncertainty

**Risk** is the chance that a threat exploits a vulnerability and causes harm.
**Risk management** is the structured process of identifying it, sizing it, and
deciding what to do.

### Identify, assess, analyze

- **Risk identification** — find the risks.
- **Risk assessment** — can be **ad hoc**, **recurring**, **one-time**, or
  **continuous**, depending on how often you look.
- **Risk analysis** — size the risk, two ways:
  - **Qualitative** — rate risks subjectively (high/medium/low). Fast, but fuzzy.
  - **Quantitative** — put real dollar figures on it, using this key chain:

> **SLE (Single Loss Expectancy)** = asset value × **exposure factor** (the % lost
> per incident). **ARO (Annualized Rate of Occurrence)** = how many times per year
> you expect it. **ALE (Annualized Loss Expectancy)** = **SLE × ARO** — your
> expected yearly loss.

A worked example makes it stick:

> A laptop worth \$2,000 has a 50% chance of theft loss per incident (exposure
> factor 0.5), so **SLE = \$1,000**. You expect it twice a year (**ARO = 2**).
> Then **ALE = \$1,000 × 2 = \$2,000/year.** If a \$1,500/year control would stop
> it, it's worth buying; a \$3,000 one isn't.

### The risk register and appetite

The **risk register** is the master list of risks, each with a **risk owner**, a
**risk threshold**, and **key risk indicators (KRIs)**. Two terms to separate:

- **Risk appetite** — how much risk the organization is *willing* to take overall.
  It can be **expansionary** (willing to take more for growth), **conservative**
  (cautious), or **neutral**.
- **Risk tolerance** — how much variation from the target it can *withstand* for a
  specific risk.

### The four responses to risk

Every identified risk gets one of four treatments:

- **Mitigate** — reduce it with controls (the most common).
- **Transfer** — shift it to someone else (buy **insurance**, outsource).
- **Avoid** — stop doing the risky activity entirely.
- **Accept** — knowingly live with it (sometimes via a documented **exemption/
  exception**).

### Business impact analysis (BIA)

A **BIA** figures out how badly a disruption would hurt and how fast you must
recover. Its key metrics:

| Metric | Meaning |
|--------|---------|
| **RTO** (Recovery Time Objective) | How quickly you must be back up |
| **RPO** (Recovery Point Objective) | How much data loss is tolerable (how far back) |
| **MTTR** (Mean Time To Repair) | Average time to fix a failed component |
| **MTBF** (Mean Time Between Failures) | Average time a component runs before failing |

> **RTO = time** (how long down is acceptable). **RPO = data** (how much you can
> lose). They're a favorite trap — don't swap them.

## Third-party risk: you inherit your vendors' weaknesses

Most organizations depend on outside vendors, and each one extends your attack
surface. **Third-party risk management** keeps that trust honest.

### Assessing and selecting vendors

- **Vendor assessment** tools: **penetration testing**, a **right-to-audit
  clause** (you may inspect them), **evidence of internal audits**, **independent
  assessments**, and **supply chain analysis**.
- **Vendor selection**: **due diligence** (investigate before signing) and
  checking for **conflicts of interest**.
- **Questionnaires** and **rules of engagement** set expectations up front.

### The alphabet soup of agreements

The exam tests these contract types — know what each is for:

| Agreement | Purpose |
|-----------|---------|
| **SLA** (Service Level Agreement) | Guarantees a level of service (uptime, response time) |
| **MOU / MOA** (Memorandum of Understanding/Agreement) | A less formal statement of intent to work together |
| **MSA** (Master Service Agreement) | Overarching terms for an ongoing relationship |
| **SOW / WO** (Statement/Work Order) | The specifics of a particular job under an MSA |
| **NDA** (Non-Disclosure Agreement) | Keeps shared information confidential |
| **BPA** (Business Partners Agreement) | Terms between business partners |

Finally, **vendor monitoring** keeps watching them *after* signing — relationships
and their risks change over time.

## The whole thing in one paragraph

**Governance** sets the rules through a hierarchy of mandatory **policies**,
**standards**, and **procedures** plus advisory **guidelines**, overseen by boards
and committees, shaped by external regulatory/legal context, and assigned to clear
**roles** (owner, controller, processor, custodian). **Risk management**
identifies and assesses risk, analyzes it **qualitatively** or **quantitatively**
(**SLE = value × exposure factor**, **ALE = SLE × ARO**), tracks it in a **risk
register** governed by **risk appetite/tolerance**, and treats each risk by
**mitigate, transfer, avoid, or accept** — with a **BIA** setting **RTO** (time),
**RPO** (data), **MTTR**, and **MTBF**. And **third-party risk** manages the
vendors you depend on through assessments (right-to-audit, pen tests, supply-chain
analysis), due-diligence selection, the right **agreements** (SLA, MOU/MOA, MSA,
SOW, NDA, BPA), and ongoing monitoring.

## On the exam

- Document hierarchy: **policy → standard → procedure** are all **mandatory**; a
  **guideline** is only a recommendation. That "mandatory vs. optional" line is
  the usual question.
- Quantitative risk math: **SLE = asset value × exposure factor**, **ALE = SLE ×
  ARO**. A control is worth buying only if it costs less than the ALE it prevents.
- **RTO vs. RPO:** RTO is **how long** you can be down; RPO is **how much data**
  you can lose. Don't confuse them.
- The four risk responses are **mitigate, transfer, avoid, accept**. Buying
  **insurance** is **transfer**; a documented decision to live with a risk is
  **accept**.
- Know the data roles, especially **controller** (decides the why/how of
  processing) vs. **processor** (acts for the controller) — they recur in privacy
  questions too.
- Match agreements fast: uptime guarantee = **SLA**, confidentiality = **NDA**,
  informal intent = **MOU**, job specifics = **SOW**.
- A **right-to-audit clause** is the answer for "verify a vendor's security after
  signing."
