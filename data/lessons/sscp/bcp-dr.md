# Business Continuity & Disaster Recovery

Incident response handles the attack; **business continuity** and **disaster
recovery** handle the *consequences* — fire, flood, ransomware, a datacenter
outage. BCP keeps the business running through a disruption; DR restores the
technology afterward. This lesson covers the analysis that drives both, the
recovery metrics the exam loves to test, and the sites, backups, and tests that
make recovery real.

## BCP vs DR: two related plans

> **Business Continuity Planning (BCP)** is the broad, business-wide plan to keep
> **essential functions** operating during and after a disruption. **Disaster
> Recovery (DR)** is the subset focused on **restoring IT systems and data** after
> a disaster.

Think of it this way: BCP keeps the *business* alive (alternate work sites, manual
procedures, communications); DR brings the *systems* back (servers, data,
networks). DR is a component of the larger BCP.

## The Business Impact Analysis

Everything starts with understanding what you stand to lose.

> A **Business Impact Analysis (BIA)** identifies the organization's **critical
> business functions**, the resources they depend on, and the **impact over time**
> of their disruption. It is the foundation on which the whole plan is built.

The BIA prioritizes what to recover first and sets the recovery targets below. It
quantifies impact (financial, operational, reputational, legal) as a function of
*downtime* — some functions can be down for days, others for only minutes.

## The recovery metrics — know these cold

These acronyms are among the most tested items in the entire domain. Learn exactly
what each measures and the difference between the two headliners:

> **RTO (Recovery Time Objective)** = the maximum tolerable **time** to restore a
> function after a disruption. It answers *"how fast must we be back?"*
> **RPO (Recovery Point Objective)** = the maximum tolerable amount of **data
> loss**, measured in time. It answers *"how much data can we afford to lose?"*

The clean way to keep them apart:

- **RPO looks backward** to the last good backup — "we can lose at most 15 minutes
  of transactions" is an **RPO** of 15 minutes, and it dictates **backup
  frequency** (to lose no more than 15 minutes, back up at least every 15
  minutes).
- **RTO looks forward** from the disruption — "the order system must be back within
  2 hours" is an **RTO**, and it dictates your recovery **capability** (hot site,
  failover).

Two more that complete the picture:

| Metric | Meaning |
|--------|---------|
| **MTD (Maximum Tolerable Downtime)** | The absolute longest a function can be down before the damage is unrecoverable; **RTO must be less than MTD** |
| **WRT (Work Recovery Time)** | Time after systems are restored to verify data and resume normal operations (RTO + WRT must fit within MTD) |
| **MTBF** | Mean Time Between Failures — reliability of a component |
| **MTTR** | Mean Time To Repair/Recover — how long repairs take |

## Recovery sites

If the primary site is gone, you need somewhere to run. The three classic
alternate sites trade **cost against recovery speed**:

> A **hot site** is fully equipped and running, with near-real-time data — switch
> over in minutes to hours (most expensive). A **warm site** has hardware and
> connectivity but needs data restored and setup — recovery in hours to days
> (moderate cost). A **cold site** is just space and power — days to weeks to make
> operational (cheapest).

Pick the site type by your **RTO**: a tight RTO demands a hot site; a relaxed RTO
makes a cold site economical. Other options include **mobile sites** (equipment in
a trailer) and **reciprocal/mutual-aid agreements** (two organizations agree to
host each other), plus modern **cloud-based DR**, which has largely reshaped this
space by letting you spin up recovery capacity on demand.

## Backups: your last line of defense

A backup you can't restore isn't a backup. Know the three backup types and the
guiding rule:

| Backup type | What it copies | Restore effort | Backup speed |
|-------------|----------------|----------------|--------------|
| **Full** | Everything | Simplest (one set) | Slowest |
| **Incremental** | Only data changed since the **last backup of any kind** | Slowest (full + every increment) | Fastest |
| **Differential** | Only data changed since the **last full backup** | Moderate (full + latest differential) | Moderate |

The widely cited **3-2-1 rule**: keep **3** copies of data, on **2** different
media types, with **1** copy **offsite**. A modern extension adds "**1** offline/
immutable" copy specifically to survive ransomware, which hunts down and encrypts
reachable backups. **RAID** provides disk redundancy for availability but is **not
a backup** — RAID survives a *drive* failure, not an accidental deletion, a
ransomware event, or a site loss.

## Testing the plan

An untested plan is a hopeful guess. Tests run from least to most disruptive:

- **Read-through / checklist** — review the plan documents for completeness.
- **Tabletop / walkthrough** — talk through a scenario in a room, no systems
  touched.
- **Simulation** — act out the response against a mock scenario.
- **Parallel test** — bring up the recovery site **alongside** production without
  taking production down.
- **Full-interruption test** — actually fail over to recovery (most realistic,
  most risky).

Test regularly and after major changes, and feed the findings back into the plan.

## Exam focus

- **BCP** keeps the **business** running; **DR** restores **IT systems/data**. DR
  is a subset of BCP. The **BIA** identifies critical functions and drives the
  recovery priorities and metrics.
- **RTO = max time to restore** (how fast back); **RPO = max data loss** (how much
  data lost, sets backup frequency). "Lose at most 15 minutes of data" = **RPO**.
- **MTD** is the absolute downtime limit; **RTO (+ WRT) must be less than MTD.**
- Recovery sites by speed/cost: **hot** (ready, pricey) > **warm** > **cold** (just
  space, cheap). Match the site to your **RTO**.
- Backups: **full/incremental/differential** — incremental restores slowest,
  differential is in between. Follow **3-2-1** (plus an offline/immutable copy vs
  ransomware). **RAID is redundancy, not a backup.**
- Test with **tabletop -> simulation -> parallel -> full-interruption** (least to
  most disruptive).
