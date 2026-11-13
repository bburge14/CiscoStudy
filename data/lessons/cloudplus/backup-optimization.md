# Backup, Disaster Recovery & Cost Optimization

Two operations topics that keep the business safe and solvent: **backup and
disaster recovery** make sure a failure doesn't become a catastrophe, and **cost
optimization** — the discipline the industry now calls **FinOps** — makes sure the
cloud bill reflects value rather than waste. Both are governed by numbers you must
know cold.

## Backup fundamentals

A **backup** is a copy of data you can restore from. The copy *type* trades backup
speed against restore speed and storage:

| Type | Copies | Backup speed | Restore |
|------|--------|-------------|---------|
| **Full** | Everything, every time | Slowest, most storage | Fastest — one set |
| **Incremental** | Only what changed since the *last backup of any kind* | Fastest, least storage | Slowest — need full + every increment in order |
| **Differential** | Everything changed since the last *full* | Middle | Middle — need full + one differential |

> Remember the restore chain: an **incremental** restore needs the last full plus
> *every* incremental in sequence; a **differential** restore needs only the last
> full plus the *latest* differential.

The widely taught **3-2-1 rule**: keep **3** copies of data, on **2** different
media types, with **1** copy off-site (in the cloud, another region). A backup you
have never test-restored is not a backup — **restore testing** is mandatory,
because the day you discover a corrupt or incomplete backup should not be the day
you need it.

**Snapshots** give fast point-in-time rollback but usually live in the same system
as the source, so they complement — not replace — true off-site backups.

## RPO and RTO: the two DR numbers

Disaster recovery planning is anchored by two objectives, and mixing them up is
the classic exam trap.

> **RPO (Recovery Point Objective)** = how much *data* you can afford to lose,
> measured in time. It sets how often you back up or replicate. A 15-minute RPO
> means backups/replication at least every 15 minutes.
>
> **RTO (Recovery Time Objective)** = how long you can afford to be *down* before
> service is restored. It drives the recovery *strategy* you can afford.

A memory hook: **RPO looks backward** (how far back is my last good copy?); **RTO
looks forward** (how fast can I be running again?). Two related metrics: **MTTR**
(mean time to repair) and **MTBF** (mean time between failures) describe
reliability over time, and a **business impact analysis (BIA)** is what sets the
RPO/RTO targets by ranking which functions are critical.

## Disaster recovery strategies

Cheaper strategies accept a longer RTO; expensive ones keep RTO near zero. From
cheapest/slowest to priciest/fastest:

- **Backup and restore** — restore from backups into a new environment after a
  disaster. Lowest cost, longest RTO (hours+).
- **Pilot light** — a minimal core (e.g., a replicated database) runs cold;
  everything else is scaled up when needed. Low cost, moderate RTO.
- **Warm standby** — a smaller but running copy of the whole stack you scale up on
  failover. Higher cost, short RTO.
- **Hot site / active-active (multi-site)** — full capacity running in a second
  location, serving traffic or ready instantly. Highest cost, near-zero RTO/RPO.

**Failover** is switching to the recovery environment; **failback** is returning to
primary once it's healthy. **DRaaS** (DR as a service) outsources this to a
provider. The right strategy is simply the cheapest one that still meets the BIA's
RTO/RPO for that workload.

## Cost optimization (FinOps)

The cloud's pay-as-you-go model means waste is silent and continuous. **FinOps** is
the practice of giving engineering, finance, and business shared ownership of cloud
cost, making spend visible and tying it to value.

### Pricing models

- **On-demand** — pay per hour/second, no commitment. Flexible, most expensive per
  unit; for spiky or short-lived workloads.
- **Reserved instances / savings plans / committed use** — commit to 1–3 years for
  a large discount. Best for steady, predictable baseline load.
- **Spot / preemptible** — deeply discounted spare capacity the provider can
  reclaim with little notice. Great for fault-tolerant, interruptible batch work;
  never for a stateful database.

The pattern: cover your steady baseline with **reservations**, absorb spikes with
**on-demand**, and run interruptible batch on **spot**.

### Finding and removing waste

- **Right-sizing** — downsize over-provisioned instances to match real usage (the
  biggest single lever).
- **Eliminate idle / orphaned resources** — stopped instances still billing for
  attached volumes, unattached IPs, forgotten dev environments, old snapshots.
- **Scheduling** — turn off non-production environments nights and weekends.
- **Storage tiering & lifecycle policies** — age cold data to cheaper tiers.
- **Autoscaling** — scale in when demand drops so you don't pay for peak capacity
  around the clock.

### Seeing the spend

- **Tagging** every resource with an owner/cost-center enables **cost allocation**.
- **Showback** reports each team's spend for visibility; **chargeback** actually
  bills it back to them, which changes behavior.
- **Budgets and cost alerts** warn when spend trends past a threshold *before* the
  invoice shocks anyone.

## Exam focus

- **Full** = everything (slow backup, fast restore); **incremental** = since last
  backup of any type (fast backup, restore needs full + all increments in order);
  **differential** = since last full (restore needs full + latest differential).
  Follow **3-2-1** and always **test restores**.
- **RPO = acceptable data loss** (sets backup/replication frequency, looks
  backward); **RTO = acceptable downtime** (sets recovery strategy, looks forward).
  The **BIA** defines these targets; don't confuse them.
- DR strategies by cost/RTO: **backup-restore** (cheapest, slowest) → **pilot
  light** → **warm standby** → **hot/active-active** (priciest, near-zero).
  **Failover** to recovery, **failback** to primary.
- Pricing: **on-demand** (flexible, dear), **reserved/committed** (steady baseline,
  discounted), **spot** (interruptible batch only, cheapest). Cover baseline with
  reservations, spikes on-demand, batch on spot.
- Cut waste with **right-sizing, idle-resource cleanup, scheduling, tiering, and
  autoscaling**; see spend with **tagging**, **showback/chargeback**, and
  **budgets/alerts**. This whole discipline is **FinOps**.
