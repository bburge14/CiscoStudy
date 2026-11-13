# Backup, Recovery & Disaster Recovery

Business continuity planning sets the objectives — *how fast must we recover* and
*how much data can we lose*. **Disaster recovery (DR)** is the IT capability that
actually delivers on those objectives when systems go down. Backups are the raw
material of recovery; recovery sites and tested plans are how a backup becomes a
running business again. This lesson covers both, and the findings that should
worry an auditor most.

## Backups: the foundation of recovery

You cannot restore what you never copied. Backup strategy balances how much data
to copy, how often, and how fast it can be restored.

The three backup types differ in what they copy — and the exam tests the
difference between the two "partial" types directly:

| Backup type | Copies… | Restore | Backup speed |
|-------------|---------|---------|--------------|
| **Full** | Everything, every time | Fastest (one set) | Slowest |
| **Differential** | All changes since the last **full** | Full + one differential | Grows over the week |
| **Incremental** | All changes since the last **backup of any kind** | Full + every incremental in order | Fastest to back up |

> **Differential = changes since the last FULL backup. Incremental = changes since
> the last backup of ANY kind.** Incrementals are quickest to create but slowest
> to restore (you need the full plus every incremental in sequence); differentials
> are the reverse.

A classic media rotation scheme keeps multiple generations:

> The **Grandfather-Father-Son (GFS)** scheme keeps **daily (son)**, **weekly
> (father)**, and **monthly (grandfather)** backup sets — layered generations that
> let you recover from different points in time.

Good practice also keeps copies **offsite** (so a site disaster doesn't destroy
the backups too), often summarized as the **3-2-1 rule** (three copies, two media
types, one offsite). But the single most important control is testing:

> The backup finding that should concern an IS auditor **most** is that
> **restoration has never been tested**. A backup you cannot actually restore is
> worthless — and you only discover that at the worst possible moment unless you
> test restores regularly.

## Recovery sites: where you run after a disaster

If a facility is lost, operations must resume somewhere. Recovery sites trade
**cost** against **recovery speed**, and the choice is driven by the **RTO** set
in the BIA.

> - A **hot site** is fully equipped and ready to run almost immediately
>   (hardware, software, and current data). It is the most expensive but supports
>   the **shortest RTO**.
> - A **warm site** has the space, power, and some equipment, but needs
>   configuration and data restored before use — a middle ground.
> - A **cold site** provides only space, power, and environmental support (HVAC)
>   with **no installed computing equipment**. It is the cheapest but the slowest
>   to bring online.

> **Match the site to the RTO.** A very short RTO (say, two hours) demands a **hot
> site**; a longer tolerable outage can be met by a **warm** or **cold** site at
> lower cost.

Two more arrangements appear on the exam:

- **Mirrored site** — a fully redundant, real-time duplicate; the fastest and
  costliest option.
- **Reciprocal agreement** — a mutual-aid pact where two organizations agree to
  host each other in a disaster.

> A **reciprocal agreement** is cheap, but its main weakness is **unreliability**:
> when a disaster actually strikes, the partner may **lack the capacity or a
> compatible configuration** to host you, and the agreement can be hard to
> enforce. Attractive on paper, risky in practice.

Cloud-based DR (recovering into a cloud provider) has become a common modern
alternative, offering hot-site-like speed without owning a second data center.

## The DR plan and testing it

Equipment and backups are inert without a plan that tells people what to do. A DR
plan documents recovery procedures, roles, priorities (from the BIA), and the
sequence for restoring systems. And like backups, a plan is only trustworthy once
it has been **tested**. DR tests escalate in realism and risk:

- **Checklist / desk review** — read through the plan for completeness.
- **Walkthrough / tabletop** — the team talks through a scenario together.
- **Simulation** — act out a disaster scenario without touching production.
- **Parallel test** — recovery systems are brought up and run **alongside**
  production, comparing results (no disruption to live operations).
- **Full interruption** — production is actually switched to the recovery site.
  The most thorough and realistic, but the **riskiest** because a failure affects
  live operations.

The auditor checks that the plan exists, reflects the current environment and the
BIA's priorities, and — above all — is **tested regularly** with results feeding
back into improvements. An untested DR plan is the recovery-site version of an
untested backup: assumed to work, proven only in the disaster you can't afford to
fail.

## How it all connects

Trace the chain: the **BIA** (Domain 2) names critical processes and sets **RTO**
and **RPO**; the **RPO** dictates how frequent your backups or replication must be;
the **RTO** dictates which **recovery site** you need; and **testing** — of both
backups and the DR plan — is what turns all of it from paperwork into genuine
resilience.

## Exam focus

- **Differential** = changes since last **full**; **incremental** = changes since
  last **any** backup. Incremental is fast to back up, slow to restore.
- **GFS** = daily (son) / weekly (father) / monthly (grandfather) generations;
  keep copies **offsite**.
- The worst backup finding is **restoration never tested** — an untested backup is
  worthless.
- **Hot site** = ready now (shortest RTO, costliest); **warm** = partial; **cold**
  = space/power/HVAC only (cheapest, slowest). **Match the site to the RTO.**
- A **reciprocal agreement** is cheap but **unreliable** (capacity/compatibility/
  enforceability). **DR plans must be tested**; a **full-interruption** test is the
  most realistic and the riskiest.
