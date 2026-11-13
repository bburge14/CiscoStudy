# Resilient Storage

Storage is where resilience either holds or quietly fails. A compute tier can be
rebuilt from an image in minutes; lost data is gone forever. The exam tests two
ideas constantly: the difference between **durability** (will I lose the data?) and
**availability** (can I reach it right now?), and which storage service survives an
Availability Zone — or a Region — going dark. This lesson sorts the object, block,
and file services by how much failure each one tolerates.

## Durability versus availability

> **Durability is the probability that a stored object is *not lost* over a year.
> S3 Standard is designed for 99.999999999% — eleven nines — of durability,
> achieved by storing data redundantly across multiple Availability Zones.
> Availability is whether you can *access* it at a given moment (S3 Standard targets
> 99.99%).**

Eleven nines of durability does not mean eleven nines of uptime; it means that if
you store ten million objects, you would expect to lose one roughly every ten
thousand years. The redundancy across multiple AZs is what earns it.

## Object storage resilience

- **S3 Standard** stores objects redundantly across **three or more AZs** out of the
  box — the default for durable, highly available object storage.
- **S3 One Zone-IA** keeps data in a **single AZ**. It is cheaper, but if that AZ is
  destroyed the data is gone, so it is only for **easily reproducible**,
  infrequently accessed data.
- **S3 Versioning** keeps multiple variants of an object so you can recover from
  accidental overwrites or deletes. Add **MFA Delete** to require a multi-factor
  token before anyone can permanently delete a version — protection against both
  mistakes and an attacker with stolen credentials.

## Block storage resilience (EBS and instance store)

**Amazon EBS** volumes live within a single AZ, so resilience comes from snapshots:

> **EBS snapshots are stored durably in S3 and can be restored to a *new volume in
> a different AZ*. Copy a snapshot to a second Region to protect against a
> Region-level event.** Snapshots give you both AZ and Region resilience for
> block data.

By contrast, **EC2 instance store** is local disk physically attached to the host.
It is fast but **ephemeral** — data is lost when the instance stops or fails. If a
team loses data written to instance store, the fix is to store persistent data on
**EBS, EFS, or S3** instead. Never put data you cannot lose on instance store.

## File storage resilience (EFS and FSx)

Shared file systems need their own resilience story because many instances mount
them at once.

| Service | Protocol | Resilience |
|---------|----------|-----------|
| **Amazon EFS** | NFS (Linux) | Standard classes store data across **multiple AZs**; elastic capacity; many instances across AZs read/write concurrently |
| **FSx for Windows File Server** | SMB (Windows, AD) | **Multi-AZ** deployment keeps a standby in a second AZ |

- **EFS** is the answer when several Linux instances across AZs need a shared,
  highly available, elastic file system. Its Standard storage classes are already
  multi-AZ, so it survives the loss of an AZ.
- **FSx for Windows File Server (Multi-AZ)** is the answer for a highly available
  **SMB** share for Windows servers that integrates with Active Directory.

## Removing single points of failure

Resilience is a property of the *whole* architecture, not one component. For a
three-tier web app, the standard moves are:

- Deploy the **web/app tier across multiple AZs behind a load balancer**.
- Enable **Multi-AZ** for the relational database.
- Keep persistent data on **EBS/EFS/S3**, not instance store, and back up EBS with
  snapshots copied to a second Region.

Each move eliminates one thing whose failure would otherwise take the app down.

## A worked example

An architect needs durable object storage that survives an AZ outage with no
configuration work: **S3 Standard** (multi-AZ, eleven nines). The same app's Linux
processing fleet, spread over two AZs, needs a shared file system: **Amazon EFS**.
Its EC2 instances use fast local scratch space that can be lost safely: **instance
store** — but anything that must persist goes to **EBS**, snapshotted and copied to
a second Region for DR.

## How far does each service survive?

A useful way to lock this lesson in is to ask, for each storage service, "what is
the largest failure it survives on its own?"

| Service | Survives on its own |
|---------|---------------------|
| **EC2 instance store** | Nothing — lost on stop/terminate |
| **Single EBS volume** | Disk failure within its AZ (not AZ loss) |
| **EBS + snapshots** | AZ loss (restore elsewhere); Region loss if copied |
| **EFS / FSx Multi-AZ** | Loss of an Availability Zone |
| **S3 Standard** | Loss of an Availability Zone (multi-AZ by default) |
| **S3 One Zone-IA** | Disk/hardware failure, but **not** AZ loss |
| **S3 with CRR** | Region loss (a copy exists in another Region) |

The pattern: object storage (S3 Standard) and multi-AZ file systems are resilient
out of the box; block storage and instance store need *you* to add redundancy
(snapshots, Multi-AZ databases, cross-Region copies). When a stem says "survive an
AZ failure," eliminate single-AZ answers like one EBS volume, instance store, and
One Zone-IA first.

## Exam focus

- **Durability** = won't lose data (S3 = **eleven nines**, via redundancy across
  **multiple AZs**); **availability** = can access it now. Don't conflate them.
- **S3 Standard** = multi-AZ by default. **S3 One Zone-IA** = single AZ, only for
  reproducible data. **S3 Versioning (+ MFA Delete)** = recover from accidental and
  malicious deletes.
- **EBS snapshots** (stored in S3) restore to any AZ; **copy to another Region** for
  Region resilience. **Instance store is ephemeral** — put persistent data on
  EBS/EFS/S3.
- **EFS** = multi-AZ shared NFS for Linux across AZs; **FSx for Windows File Server
  (Multi-AZ)** = highly available SMB share with AD integration.
- Remove single points of failure: **web/app across AZs behind a load balancer +
  Multi-AZ database + durable backed-up storage**.
