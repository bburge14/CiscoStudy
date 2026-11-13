# High-Performing Storage

Storage performance questions reward matching the *shape* of the I/O to the right
service and settings. Is it random small reads from a database, or huge sequential
streams from a log pipeline? One volume shared by a cluster, or scratch space you
can throw away? Global uploads of giant files? Each has a best answer. This lesson
covers EBS volume types, EC2 instance store, S3 throughput techniques, and the
high-performance file systems.

## EBS volume types

**Amazon EBS** provides block storage for EC2. Four current-generation types matter here (AWS offers six in total), split into SSD
(random IOPS) and HDD (sequential throughput).

| Type | Class | Strength | Typical use |
|------|-------|----------|-------------|
| **gp3** | SSD | 3,000 IOPS / 125 MiB/s baseline, scalable to 80,000 IOPS / 2,000 MiB/s | General purpose; default |
| **io2 / io2 Block Express** | SSD | Highest, most consistent IOPS; 99.999% durability | Critical, latency-sensitive databases |
| **st1** | HDD | High sequential throughput | Big data, log processing, data warehouses |
| **sc1** | HDD | Lowest cost | Cold, rarely accessed data |

Key distinctions the exam tests:

> **gp3 lets you raise IOPS and throughput *independently of volume size*. With the
> older gp2, IOPS scaled with size, so teams over-provisioned capacity just to get
> IOPS.** Migrating gp2 → gp3 is the standard fix for "we had to buy a bigger
> volume just for IOPS."

- A critical production database needing **very high, consistent IOPS** and the
  highest durability → **io2 / io2 Block Express**.
- A big-data workload streaming **large sequential** reads/writes → **st1**.

Two EBS features also appear:

- **EBS Multi-Attach** on an io2 volume lets a *single* volume attach to multiple
  EC2 instances in the **same AZ** for a clustered application that coordinates
  writes.
- An **EBS-optimized instance** gives dedicated bandwidth to EBS so storage
  throughput does not contend with the instance's regular network traffic.

## Instance store: fastest but ephemeral

**EC2 instance store** is local disk (NVMe SSD on most current families) physically attached to the host. It delivers
the **highest possible I/O** for temporary scratch data — a cache or buffer — but it
is **lost when the instance stops**. Use it only for data you can regenerate.

## Getting more performance out of S3

S3 scales massively, but a few techniques raise what a single client or bucket
achieves:

- **Key prefixes** — S3 request throughput scales per prefix. Spreading objects
  across **many key prefixes** lets requests parallelize across S3 partitions,
  raising the achievable GET/PUT rate.
- **Multipart upload** — split a multi-gigabyte object into parts uploaded in
  parallel; if a part fails you retry only that part instead of restarting. The
  answer for uploading large objects fast and reliably.
- **S3 Transfer Acceleration** — routes uploads through the nearest CloudFront edge
  location and over the AWS backbone, speeding transfers for users uploading large
  files over **long distances** to a bucket in a single Region.

## High-performance file systems

When a workload needs a *shared* file system with serious performance:

> **Amazon FSx for Lustre delivers very high throughput and sub-millisecond latency
> for HPC and machine-learning workloads, and can link directly to an S3 data set.**

For general Linux sharing with unpredictable load, **Amazon EFS** offers an
**Elastic throughput** mode that scales throughput automatically for spiky,
unpredictable demand without paying for provisioned throughput you don't use.

## A worked example

A latency-sensitive transactional database on EC2 gets an **io2 Block Express**
volume on an **EBS-optimized** instance so storage I/O never competes with network
traffic. Its nightly export streams to a log-analytics pipeline on **st1** HDD
volumes tuned for sequential throughput. Clients around the world upload large media
files to S3 using **multipart upload** with **Transfer Acceleration**, and the ML
training cluster reads the resulting data set at high throughput through **FSx for
Lustre** linked to the bucket.

## Matching the I/O pattern

Two quick heuristics resolve most storage-performance questions:

- **Random vs sequential.** Small random reads/writes (databases, boot volumes)
  want **SSD** (gp3, io2). Large sequential streams (logs, big-data scans) want
  **throughput HDD** (st1). If the stem says "IOPS," think SSD; if it says
  "throughput" or "sequential," think HDD.
- **Shared vs attached.** One instance → an **EBS** volume. Many instances sharing
  a file system → **EFS** (Linux/NFS) or **FSx**. A single block volume shared by a
  cluster in one AZ → the special case of **EBS Multi-Attach**.

The FSx family is worth a glance so you can spot the right one:

| FSx flavor | Built for |
|------------|-----------|
| **FSx for Lustre** | HPC/ML, highest throughput, sub-ms latency, S3-linked |
| **FSx for Windows File Server** | Windows SMB shares with Active Directory |
| **FSx for NetApp ONTAP / OpenZFS** | Feature-rich managed NAS for existing workloads |

For the performance domain, **FSx for Lustre** is the headline answer: whenever a
question pairs "HPC" or "machine learning" with "very high throughput" and an S3
data set, it is Lustre.

## Exam focus

- **gp3** = general-purpose SSD; raise IOPS/throughput **independent of size**
  (migrate from gp2 to stop over-provisioning). **io2 / io2 Block Express** =
  highest, most consistent IOPS for critical databases.
- **st1** = sequential/throughput HDD (big data, logs); **sc1** = cheapest cold HDD.
- **EBS Multi-Attach** (io2) = one volume, multiple instances in the same AZ.
  **EBS-optimized instance** = dedicated EBS bandwidth.
- **Instance store** = highest I/O but ephemeral; scratch only.
- S3 throughput: spread across **key prefixes**; **multipart upload** for large
  objects (retry parts); **Transfer Acceleration** for long-distance uploads.
- Shared high-performance file systems: **FSx for Lustre** (HPC/ML, sub-ms, S3-
  linked); **EFS Elastic throughput** for spiky Linux workloads.
