# Disaster Recovery & Operational Resilience

Business continuity planning (Domain 1) decides *how fast* you must recover and
*how much* data you can lose. Disaster recovery is the operational machinery that
makes those targets achievable: the backups, redundant hardware, recovery sites,
and plan testing that get IT back online. This lesson covers the mechanics — and
the testing — of recovery, which the exam tests with crisp technical distinctions.

## Backups: the foundation

If you can restore the data, most disasters are survivable. Know the three backup
types and their trade-offs cold.

| Type | What it copies | Backup speed | Restore speed | Archive bit |
|------|----------------|--------------|---------------|-------------|
| **Full** | Everything | Slowest | Fastest (one set) | Clears it |
| **Incremental** | Changes since the **last backup of any kind** | Fastest | Slowest (full + every incremental) | Clears it |
| **Differential** | Changes since the **last full** | Medium (grows daily) | Fast (full + one differential) | Leaves it |

> The exam trade-off: **incremental** backups are **fast to create but slow to
> restore** (you need the full plus every incremental in order); **differential**
> backups are **slower to create but fast to restore** (just the full plus the most
> recent differential).

Beyond type, know the **3-2-1 rule**: keep **3** copies of data, on **2** different
media types, with **1** copy **offsite** (or in the cloud). Offsite storage is what
saves you when the whole site is lost. Rotation schemes like **Grandfather-Father-
Son** balance how many versions you keep against media cost. Critically — **backups
must be tested by restoring them**; an untested backup is a hope, not a control.

## RAID: availability, not backup

**RAID (Redundant Array of Independent Disks)** keeps systems running through a
drive failure. Know the common levels and how many failures each survives.

- **RAID 0** — striping only. Fast, but **no redundancy** (one drive dies, all data
  is lost). Not a resilience control.
- **RAID 1** — mirroring. Survives **one** drive failure; 50% capacity overhead.
- **RAID 5** — striping with **single distributed parity**. Survives **one** drive
  failure; needs at least 3 disks.
- **RAID 6** — striping with **dual distributed parity**. Survives the
  **simultaneous failure of two** drives — valuable because a second drive can fail
  during the long rebuild after the first.
- **RAID 10 (1+0)** — mirrored then striped; high performance and redundancy.

> If a scenario needs to survive **two simultaneous drive failures**, the answer is
> **RAID 6** (dual parity). RAID 5 and a single mirror each survive only **one**.

> The most important conceptual point: **RAID is high availability, not a backup.**
> It protects against hardware failure, not against deletion, corruption, or
> ransomware — those propagate instantly across a mirror. You still need backups.

## Recovery sites and high availability

If the facility itself is lost, operations move to a recovery site — ranked by cost
and speed: **hot** (ready in minutes, most expensive) → **warm** (hardware ready,
data to be loaded) → **cold** (space and power only, slowest, cheapest). A
**reciprocal agreement** is cheap but unreliable in a regional disaster.

For continuous uptime, **high-availability** techniques keep services running
without a disruptive failover: **clustering** (servers acting as one, failing over
automatically), **load balancing** (spreading work and removing single points of
failure), **redundancy** of components and network paths, and **geographic
diversity** so one region's disaster doesn't take everything down. Distinguish a
**failover** (automatic switch to a standby) from a **failback** (returning to the
primary once it's healthy).

## Testing the DR plan

A plan never tested is a plan that fails when it matters. DR tests escalate from
cheap-and-safe to thorough-but-risky:

1. **Read-through / checklist** — individuals review the plan for completeness and
   currency. No systems touched.
2. **Structured walkthrough / tabletop** — the team talks through a scenario
   together to find gaps.
3. **Simulation** — act out a scenario with simulated conditions, without affecting
   production.
4. **Parallel test** — recovery systems are **brought up alongside production**;
   you verify they work **without shutting production down** (low risk).
5. **Full-interruption test** — production is actually **switched over** to the
   recovery capability. The **most thorough and the most risky**, since a failure
   becomes a real outage; done rarely and with great care.

> Two tested distinctions: a **parallel test** runs recovery **next to** production
> without disruption, while a **full-interruption test** actually fails production
> over — most realistic, highest risk. And the **return to normal operations**
> (moving back to the primary site) is often the **most dangerous phase**: restore
> the **least-critical** systems first to validate the process before trusting it
> with the crown jewels.

## Measuring reliability: MTBF, MTTR, MTTF

DR planning uses reliability metrics to decide when to repair or replace hardware
and how much redundancy to buy.

- **MTBF (Mean Time Between Failures)** — the average runtime a *repairable*
  component gives between failures; **higher is better**.
- **MTTR (Mean Time To Repair)** — the average time to restore a failed component;
  **lower is better**.
- **MTTF (Mean Time To Failure)** — the expected lifetime of a *non-repairable*
  component before it fails.

A component with a short MTBF and a long MTTR is a reliability liability — exactly
the case that argues for redundancy (RAID, clustering) or outright replacement to
meet your RTO.

## Exam focus

- Backups: **incremental = fast backup, slow restore** (full + all incrementals);
  **differential = slower backup, fast restore** (full + latest differential).
  Follow **3-2-1** (3 copies, 2 media, 1 offsite) and **test restores**.
- RAID survivability: **RAID 5 = one** drive failure (single parity), **RAID 6 =
  two** simultaneous failures (dual parity), **RAID 1 = one** (mirror), **RAID 0 =
  none**. **RAID is availability, not backup** — it won't save you from deletion or
  ransomware.
- Sites by speed/cost: **hot → warm → cold.** High availability uses **clustering,
  load balancing, redundancy, and geographic diversity**; know **failover** vs
  **failback**.
- DR test rigor, low to high: **checklist → walkthrough/tabletop → simulation →
  parallel → full-interruption.** **Parallel** doesn't disrupt production;
  **full-interruption** is most realistic and riskiest. Restore **least-critical
  systems first** when returning to normal.
- Reliability metrics: **MTBF** (time between failures, higher is better),
  **MTTR** (time to repair, lower is better), **MTTF** (lifetime of a
  non-repairable part).
