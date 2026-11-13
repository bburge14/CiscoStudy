# Backup & Disaster Recovery

Disaster recovery (DR) planning starts with two numbers and ends with a strategy
that balances them against cost. The exam tests whether you can read a requirement
("we can lose at most 15 minutes of data"), map it to the right metric, and pick
the DR approach and AWS features that meet it without overspending. This lesson
covers the metrics, the four classic strategies, and the replication and backup
tools that implement them.

## The two metrics: RTO and RPO

> **RPO (Recovery Point Objective) is how much *data* you can afford to lose,
> measured in time — "at most 15 minutes" is an RPO. RTO (Recovery Time Objective)
> is how *long* you can be down before recovering.**

Lower RPO means more frequent/continuous replication; lower RTO means more
standby capacity ready to take over. Both cost money, so the architecture follows
the numbers.

## The four DR strategies, cheapest to fastest

AWS frames DR as a spectrum. As you move down the list, RTO and RPO shrink and cost
rises.

| Strategy | What runs in the recovery Region | RTO / RPO | Cost |
|----------|----------------------------------|-----------|------|
| **Backup & restore** | Nothing; restore from backups on demand | Hours | Lowest |
| **Pilot light** | A minimal core (e.g., a replicated database) only | Tens of minutes | Low |
| **Warm standby** | A scaled-down but *fully functional* copy, always running | Minutes | Medium |
| **Multi-site active/active** | Full capacity serving live traffic in both Regions | Near zero | Highest |

Read the stem carefully:

- "Near-zero downtime and near-zero data loss even if a Region fails, cost is
  secondary" → **multi-site active/active**.
- "A minimal core such as a replicated database runs; the rest is created on
  recovery" → **pilot light**.
- "A scaled-down but fully functional copy runs continuously and scales up on
  disaster" → **warm standby**.
- "Cheapest, and we can tolerate a long recovery" → **backup & restore**.

## Replicating data across Regions

Low RPO depends on getting data to the recovery site continuously.

- **S3 Cross-Region Replication (CRR)** — keeps a continuously updated copy of S3
  objects in a *second Region* for DR and compliance.
- **S3 Same-Region Replication (SRR)** — automatically copies objects to another
  bucket in the *same Region* (for example, aggregating logs into one account).
- **Aurora Global Database** — replicates an Aurora cluster to other Regions with
  *very low* replication lag and lets you promote a secondary Region quickly; the
  answer for cross-Region DR of an Aurora workload with minimal data loss.

## Backing up at scale

- **AWS Backup** — the centralized, policy-based backup service that manages
  backups across many services, including EBS, RDS, DynamoDB, and EFS, from one
  place with defined schedules and retention.
- **Amazon Data Lifecycle Manager (DLM)** — automates creation, retention, and
  cross-Region copy of **EBS snapshots** on a schedule, without custom scripts.
- **RDS automated backups** — enable point-in-time recovery (**PITR**) so you can
  restore a database to the exact state it was in a few minutes before a bad change,
  within the retention window.

## Making backups survive an attacker

Backups are only useful if an attacker — or a mistaken admin — cannot destroy them.

> **AWS Backup Vault Lock in *compliance* mode makes backups immutable: they cannot
> be deleted or altered before their retention expires, even by an account
> administrator or root.** This is the defense against ransomware and malicious
> insiders.

For blast-radius isolation, use a **cross-account backup copy** to a dedicated,
isolated backup account via AWS Organizations: even if a workload account is fully
compromised, the copies in the separate account remain intact. (The S3 equivalent
of immutability, **S3 Object Lock**, appears in the data-protection lesson.)

## A worked example

A business states an RPO of 15 minutes and an RTO of a few minutes for a critical
app, and cost matters. A **warm standby** in a second Region — a small but complete
copy kept current by continuous replication (Aurora Global Database for the
database, CRR for object data) and scaled up on failover — meets tight RTO/RPO
without paying for full active/active capacity. Layer **AWS Backup** with **Vault
Lock** and a **cross-account copy** so the backups themselves survive ransomware.

## Exam focus

- **RPO = data loss tolerance** (in time); **RTO = downtime tolerance**. Lowest
  RTO/RPO → **multi-site active/active**; cheapest/slowest → **backup & restore**;
  in between, **pilot light** < **warm standby** in cost and speed.
- Continuous S3 copy to another Region → **CRR**; same Region → **SRR**.
  Cross-Region Aurora DR with low lag and fast promotion → **Aurora Global
  Database**.
- Centralized backups across EBS/RDS/DynamoDB/EFS → **AWS Backup**. Scheduled EBS
  snapshots + cross-Region copy → **Data Lifecycle Manager**. Restore RDS to a
  moment before a bad change → **automated backups / PITR**.
- Immutable, ransomware-proof backups → **AWS Backup Vault Lock (compliance
  mode)**; isolate them in a separate account → **cross-account backup copy via
  Organizations**.
