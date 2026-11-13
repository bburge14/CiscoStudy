# IT Risk Management & Business Continuity Planning

Governance decides direction; risk management decides how much uncertainty the
organization will tolerate while pursuing it, and business continuity planning
decides how the organization survives when something goes badly wrong. Both are
management responsibilities that the IS auditor evaluates. This lesson covers the
risk management lifecycle and the planning that keeps critical operations alive.

## The language of risk

A handful of terms underpins every risk question. Get them exact.

> - A **threat** is something that could cause harm (a hacker, a flood, a
>   careless employee).
> - A **vulnerability** is a weakness a threat can exploit (an unpatched server,
>   a missing control).
> - **Risk** is the combination of **likelihood** and **impact** — how probable a
>   harmful event is and how bad it would be. A threat with no matching
>   vulnerability, or an asset of no value, carries little risk.

Two flavors of risk matter for the audit:

- **Inherent risk** — the risk present *before* controls are applied.
- **Residual risk** — the risk that **remains after** controls and
  countermeasures are in place. Controls reduce inherent risk down to residual
  risk; they rarely eliminate it entirely.

> **Residual risk = inherent risk reduced by the effect of controls.** Management
> must decide whether the residual risk is acceptable — and it is management, not
> the auditor, that owns that decision.

## The risk management process

Risk management is a cycle: identify, assess, respond, and monitor. The order of
the first steps is testable.

> A risk assessment begins by **identifying and valuing the information assets**.
> You cannot protect — or sensibly spend to protect — what you have not
> identified and whose worth you do not understand.

After assets are identified and valued, you identify threats and vulnerabilities,
estimate likelihood and impact, and rank the risks so the biggest get attention
first. This ranking is exactly what feeds the risk-based audit planning from
Domain 1.

### Four ways to respond to risk

Once a risk is understood, management chooses a response. Memorize all four and
their trigger words.

| Response | What it means | Classic example |
|----------|---------------|-----------------|
| **Mitigate (reduce)** | Apply controls to lower likelihood or impact | Install a firewall, add MFA |
| **Transfer (share)** | Shift the financial burden to another party | Buy **cyber insurance**, outsource |
| **Avoid** | Stop doing the risky activity altogether | Cancel a risky product line |
| **Accept** | Knowingly take no action and bear the risk | Document and accept a low risk |

> **Insurance = transfer/share.** Stopping the activity = **avoid**. Doing nothing
> on purpose = **accept**. Adding controls = **mitigate**. The exam tests these by
> scenario, so map the action to the word.

Management records decisions in a **risk register** and judges them against the
organization's **risk appetite** — the amount of risk it is willing to take in
pursuit of its objectives. The auditor checks that the register is maintained and
that accepted risks really are within appetite and signed off at the right level.

## Business continuity planning

Even well-managed risk can still materialize — a fire, a ransomware outbreak, a
regional outage. **Business continuity planning (BCP)** keeps the organization's
essential functions running (or quickly restored) through such disruption. It is
a governance-level responsibility because it protects the whole enterprise, not
just IT.

### The business impact analysis

Everything in continuity planning starts with one study.

> A **business impact analysis (BIA)** identifies the organization's **critical
> business processes** and the **impact of their disruption** over time, and uses
> that to set **recovery priorities** and timing objectives. The BIA, not a
> technology choice, drives the continuity strategy.

From the BIA come the two objectives you must know cold:

> - **Recovery Time Objective (RTO)** — the **maximum acceptable time** to restore
>   a process after a disruption. It answers *how fast must we be back?*
> - **Recovery Point Objective (RPO)** — the **maximum acceptable amount of data
>   loss**, measured as a point in time. It answers *how much data can we afford
>   to lose?*

A memory hook: **RTO = time** (how long down), **RPO = data** (how much lost).
They drive very different investments:

- A **near-zero RPO** means almost no data loss is tolerable, which demands
  **near-continuous replication or mirroring** — frequent, expensive data
  protection.
- A **very short RTO** means the business must resume almost immediately, which
  demands fast recovery capability.

A related term is **maximum tolerable downtime (MTD)** — the absolute longest a
process can be unavailable before the damage is unrecoverable; the RTO must be
shorter than the MTD. The actual *recovery strategies* that satisfy these
objectives — alternate sites, backups, and failover — are implemented through
disaster recovery, which belongs to IT operations and is covered later. Here the
key point is that the **BIA sets the objectives**, and everything downstream must
honor them.

## Exam focus

- **Threat** exploits a **vulnerability**; **risk = likelihood × impact**.
  **Residual risk** is what **remains after controls**; management owns accepting
  it.
- A risk assessment's **first step** is to **identify and value the information
  assets**.
- Four risk responses: **mitigate** (add controls), **transfer/share**
  (insurance/outsource), **avoid** (stop the activity), **accept** (bear it).
  Match the scenario to the word.
- The **BIA** identifies **critical processes and disruption impact** and sets
  **recovery priorities, RTO, and RPO**.
- **RTO = maximum acceptable downtime (time); RPO = maximum acceptable data loss
  (data).** A near-zero RPO implies **continuous replication/mirroring**.
