# Security Controls & Third-Party Risk Management

A program delivers protection through **controls** — the safeguards that reduce
risk — and increasingly through the discipline of managing the **third parties**
who now hold your data and run your systems. This lesson gives you the manager's
working vocabulary of control types, then turns to one of the fastest-growing
exposures every security manager faces: the vendors, cloud providers, and
suppliers in your supply chain. Both topics reward thinking about *function and
assurance*, not product features.

## What a control is

> A **security control** is any safeguard or countermeasure — a policy, process,
> or technology — put in place to reduce risk by preventing, detecting, or
> correcting undesirable events.

Controls are how residual risk gets pulled down toward the organization's
appetite. The exam classifies them two ways at once: by **what they do**
(function) and by **how they're implemented** (category/nature). You must be
fluent in both.

## Controls by function: what they do

This is the classification the exam tests most. Picture a sequence around an
event — before, during, and after.

> - **Preventive** — stops an incident before it happens.
> - **Detective** — identifies and signals an incident that is occurring or has
>   occurred.
> - **Corrective** — fixes or restores after an incident, limiting damage.
> - **Deterrent** — discourages an attacker from trying.
> - **Compensating** — an alternative control when the primary one isn't feasible.
> - **Directive** — directs behavior through instruction (policy, signage).
> - **Recovery** — restores systems/operations to normal after disruption.

Match the clues the exam uses:

| Example | Functional type |
|---------|-----------------|
| Firewall blocking unauthorized traffic | **Preventive** |
| IDS alerting analysts to suspicious activity | **Detective** |
| Restoring from backup after ransomware | **Corrective / Recovery** |
| "Warning: monitored premises" sign | **Deterrent** |
| Extra monitoring because you can't patch a legacy app | **Compensating** |
| A policy telling staff how to handle data | **Directive** |

The two that anchor the question bank: a **firewall is preventive** (it blocks
before harm), and an **IDS is detective** (it alerts; it doesn't block). If it
*stops* the thing, preventive; if it *tells you* about the thing, detective.

## Controls by category: how they're implemented

> - **Technical (logical)** — enforced by technology: encryption, access control
>   lists, firewalls, MFA.
> - **Administrative (managerial)** — enforced through management action:
>   policies, risk assessments, training, hiring procedures.
> - **Physical** — tangible protections: locks, fences, guards, cameras.

Function and category are independent axes. A locked server-room door is
*physical* in category and *preventive* in function. A security-awareness class
is *administrative* in category and *preventive* (and *directive*) in function.
Expect the exam to ask for one axis while describing the other.

## Defense in depth

No single control is perfect, so managers stack them.

> **Defense in depth (layered security)** uses multiple, overlapping controls of
> different types so that if one fails, others still protect the asset.

If a phishing email slips past the mail filter (preventive), endpoint detection
(detective) and least-privilege access (preventive) still limit the damage. A
manager designs for failure of any single layer — the opposite of betting
everything on one "silver bullet" product.

## Third-party risk: your risk leaves the building

Modern organizations run on outsiders — SaaS platforms, cloud hosts, payroll
processors, contractors. Each one you hand data or access to can become your
breach. The governing truth:

> You can **outsource the work, but not the accountability.** When a vendor
> mishandles your data, it is still *your* incident, your regulator's call, and
> your customers' trust at stake.

That single idea drives every third-party management practice the exam tests.

### Before you onboard: due diligence first

The classic scenario: a vendor will process sensitive customer data. What do you
do FIRST? Not "sign the contract," not "give them access."

> Before onboarding a third party that will handle sensitive data, **FIRST
> perform a due-diligence assessment of the vendor's security posture against
> your organization's requirements.** You must know their risk before you accept
> it.

Due diligence might review the vendor's certifications (e.g., ISO/IEC 27001), an
independent audit report (such as a **SOC 2**), questionnaires, and evidence of
controls. The point is to assess *before* commitment, when you still have
leverage.

### Bake it into the contract

A handshake isn't a control. The mechanism that holds a provider to agreed
security is contractual.

> The BEST way to hold a service provider to agreed security and to verify
> ongoing compliance is through **contractual security requirements, SLAs, and a
> right-to-audit clause.**

Each piece earns its place:

- **Security requirements** in the contract make specific controls mandatory, not
  optional.
- **SLAs (service-level agreements)** set measurable commitments (uptime,
  breach-notification timelines) with consequences for missing them.
- A **right-to-audit clause** lets you *verify* — the difference between trusting
  and confirming.

### Keep watching: ongoing monitoring

Due diligence at onboarding is a snapshot; vendor risk changes. Managers require
**ongoing monitoring** — periodic reassessments, reviews of audit reports, and
attention to the vendor's own subcontractors (**fourth-party / supply-chain
risk**). A vendor that was solid at signing can degrade, get acquired, or suffer
its own breach. The relationship is managed for its whole lifecycle, through to
secure offboarding and return or destruction of your data.

## The manager's reflex

- Classify a control on **both** axes: **function** (preventive/detective/…) and
  **category** (technical/administrative/physical).
- **Firewall = preventive; IDS = detective.** Stops it vs. tells you about it.
- Design **defense in depth**, never a single point of failure.
- For a new vendor: **due-diligence assessment FIRST**, then **contract +
  SLAs + right-to-audit**, then **ongoing monitoring.** Accountability stays with
  you.

## Exam focus

- Controls classify by **function** — **preventive** (stops), **detective**
  (alerts), **corrective/recovery** (restores), **deterrent** (discourages),
  **compensating** (alternative), **directive** (instructs) — and by **category**
  — **technical/logical, administrative/managerial, physical.** The two axes are
  independent.
- A **firewall is preventive**; an **IDS is detective.** This exact pairing shows
  up repeatedly.
- **Defense in depth** layers overlapping controls so one failure isn't fatal.
- **Outsourcing transfers work, not accountability.** When you outsource, the
  risk — and the blame — stays yours.
- **FIRST step before onboarding a vendor = due-diligence security assessment**
  against your requirements (SOC 2 reports, certifications, questionnaires).
- Hold vendors accountable with **contractual security requirements, SLAs, and a
  right-to-audit clause**, plus **ongoing monitoring** and attention to
  **fourth-party/supply-chain** risk.
