# Business Continuity & Disaster Recovery

When a fire, flood, outage, or attack strikes, two related plans determine whether
the organization survives. **Business continuity (BC)** keeps the essential work
going *through* the disruption; **disaster recovery (DR)** restores the technology
*after* it. They overlap, but they are not the same thing, and the exam cares
about the difference.

## Business continuity: keep the lights on

> **Business continuity** focuses on keeping an organization's essential (critical)
> business functions operating during and after a disruption.

The emphasis is on the *business function*, not the hardware. During a flood,
leadership's first concern is that orders keep getting processed — maybe from an
alternate location — not yet rebuilding the damaged data center. Keeping a
fully staffed backup call center running so customer support never stops is pure
business continuity.

### The business impact analysis (BIA)

Before you can write a continuity plan, you have to know what matters most.

> A **business impact analysis (BIA)** identifies the organization's critical
> functions and the consequences of losing each one. It drives the recovery
> priorities and objectives.

The BIA answers "which functions are essential, and how badly does it hurt — and
how fast — if we lose them?" Because resources after a disaster are limited, you
can't restore everything at once, so the BIA tells you **what to restore first:
the most critical functions**.

### Key continuity concepts

- **Business continuity plan (BCP)** — the document that lays out how the
  organization will sustain essential operations during and after a disruption.
- **Maximum Tolerable Downtime (MTD)** — the longest a critical function can be
  unavailable before the harm becomes unacceptable or irreparable. All recovery
  objectives must fit *inside* the MTD.
- **Senior management sponsorship** — a continuity program only succeeds if
  executive leadership visibly backs it and funds it. Without that sponsorship it
  won't be resourced or taken seriously.
- **Tabletop exercise** — a discussion-based walkthrough where the team gathers
  and talks step by step through a hypothetical scenario to find gaps in the
  plan, *without* touching live systems. It's the safest way to test a plan.

## Disaster recovery: restore the technology

> **Disaster recovery** is the set of processes and tools used to restore IT
> systems, data, and operations after a disruptive event, so normal service can
> resume.

If business continuity is about keeping the business *functioning*, disaster
recovery is about getting the *computers, networks, and data* back. DR is, in a
sense, the IT-focused subset that supports the broader continuity goal.

### Alternate processing sites

A core DR decision is where you'll run if your primary site is destroyed. There
are three classic options, trading cost against speed of recovery:

| Site | What's ready | Recovery speed | Cost |
|------|--------------|----------------|------|
| **Hot site** | Fully equipped: hardware, current data, connectivity | Fastest — take over almost immediately | Highest |
| **Warm site** | Hardware and connectivity in place, but current data must be loaded | Middle ground | Medium |
| **Cold site** | Only space, power, and cooling — no equipment | Slowest — must install and configure everything | Lowest |

The trade-off is a straight line: the more you pay to keep a site ready, the
faster you can fail over to it. A **hot site** is fastest and priciest; a **cold
site** is cheapest and slowest; a **warm site** sits in between.

### Recovery objectives: RTO and RPO

Two metrics define the recovery targets, and students mix them up constantly.
Keep them straight by what each one measures — **time** versus **data**.

> **RTO (Recovery Time Objective)** is the target *time* to restore a system
> after an outage. **RPO (Recovery Point Objective)** is the maximum acceptable
> amount of *data loss*, expressed as a point in time.

- "Email must be back within **4 hours**" → that 4 hours is the **RTO** (how long
  until it's running again).
- "We can tolerate losing at most **15 minutes** of transactions" → that 15
  minutes is the **RPO** (how much data we can afford to lose, which drives how
  often we back up).

Memory hook: **RT**O = **R**ecovery **T**ime (how long down); **RP**O =
**R**ecovery **P**oint (how much data).

### Backups

Backups are the backbone of recovery. Three common strategies differ in what they
copy and how a restore works:

| Backup type | Copies | Restore requires | Speed to back up |
|-------------|--------|------------------|------------------|
| **Full** | All selected data every time | Just that one backup set | Slowest, most storage |
| **Incremental** | Only data changed since the *last backup of any kind* | The full backup **plus every incremental**, in order | Fastest to create |
| **Differential** | Only data changed since the *last full backup* | The full backup **plus the latest differential** | Grows over time |

The trade-off is between backup speed and restore simplicity. **Full** backups
are slow to make but trivial to restore. **Incremental** backups are quickest to
make but need the full plus *every* incremental to restore. **Differential**
backups sit in between — each one grows larger, but a restore needs only the full
plus the most recent differential.

> Always keep backup copies **off-site**, at a geographically distant location.
> If backups sit next to the servers, a single fire or flood can destroy both the
> production data and its only copy.

## BC vs. DR in one line

- **Business continuity** keeps essential *business functions* operating through a
  disruption.
- **Disaster recovery** restores *IT systems and data* after the disruption.

Both are driven by the **BIA**, both need senior-management support, and both
should be tested (for example, with tabletop exercises) before a real disaster
puts them to use.

## Exam focus

- **BC** = keep essential functions running *during/after* disruption; **DR** =
  restore *IT systems and data*. If the stem is about the business operating, it's
  BC; if it's about rebuilding technology, it's DR.
- The **BIA** identifies critical functions and sets recovery priorities —
  restore the **most critical functions first**.
- **MTD** = longest tolerable downtime; recovery objectives must fit within it.
  A **tabletop exercise** tests a plan through discussion, without touching
  production.
- Sites by cost/speed: **hot** (ready, fastest, costliest) → **warm** (partly
  ready) → **cold** (space only, cheapest, slowest).
- **RTO** = time to restore; **RPO** = acceptable data loss. Don't swap them.
- Backups: **full** (easy restore), **incremental** (full + all incrementals),
  **differential** (full + latest differential). Store copies **off-site**.
