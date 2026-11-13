# Cost-Optimized Storage

Storage cost optimization is about paying for the access pattern you actually have,
not the one you provisioned for. Data that is hot today may be cold in a month, and
paying S3 Standard prices for data nobody reads is pure waste. The exam tests
whether you can match data to the cheapest storage class or tier that still meets
its retrieval requirement, and whether you can automate the move. The watchword is:
**cheaper storage usually trades away instant retrieval.**

## The S3 storage class spectrum

S3 classes trade storage price against retrieval speed, retrieval cost, and minimum
storage duration.

| Class | Access pattern | Retrieval | Min duration |
|-------|----------------|-----------|--------------|
| **S3 Standard** | Frequent | Instant | None |
| **S3 Intelligent-Tiering** | **Unknown / changing** | Instant | None |
| **Standard-IA** | ~Monthly, needs ms access | Instant | 30 days |
| **One Zone-IA** | Infrequent, reproducible, single AZ | Instant | 30 days |
| **Glacier Instant Retrieval** | Archive, rare, ms access | Instant | 90 days |
| **Glacier Flexible Retrieval** | Archive, minutes–hours OK | Minutes–hours | 90 days |
| **Glacier Deep Archive** | Cold archive, 12 h OK | ~12–48 h | 180 days |

> **When access patterns are unknown or change over time, choose S3 Intelligent-
> Tiering: it moves objects between tiers automatically to minimize cost, with no
> retrieval fees for moving between the frequent and infrequent tiers and no
> performance impact.** It is the "set it and forget it" answer.

Match the stem to the class:

- Accessed ~monthly but must come back in **milliseconds**, cheaper than Standard →
  **Standard-IA**.
- Retained ~10 years, almost never read, **12-hour** retrieval acceptable, lowest
  cost → **Glacier Deep Archive**.

## Automate movement with lifecycle policies

> **S3 Lifecycle policies transition objects to cheaper classes as they age and
> expire them when no longer needed — all automatically.** For logs accessed for 30
> days, rarely after, and archived cheaply for 7 years, a lifecycle rule transitions
> them to Glacier and later expires them.

Lifecycle rules also clean up hidden waste in **versioned** buckets:

- **Expire noncurrent versions** so old object versions don't accumulate forever.
- **Abort incomplete multipart uploads** so half-finished uploads stop being billed.

To decide *what* to transition, **S3 Storage Class Analysis** reports which objects
are accessed frequently versus rarely, informing your Standard-IA lifecycle rules.

## Glacier retrieval: pay less by waiting

When restoring from Glacier Flexible Retrieval, you choose a retrieval speed, and
cost falls as you accept more delay:

- **Expedited** (1–5 minutes) — most expensive.
- **Standard** (3–5 hours).
- **Bulk** (5–12 hours) — the **lowest retrieval cost** when you can wait.

If a question says "lowest retrieval cost and we can wait several hours," the answer
is **Bulk**.

## EBS and EFS cost levers

Block and file storage have their own optimizations:

- **gp2 → gp3** — migrating general-purpose SSD volumes from gp2 to **gp3** lowers
  cost while keeping or improving baseline performance; a straightforward win.
- **EBS Snapshots Archive** — move snapshots you keep for compliance but almost
  never restore to the **Archive tier** for cheaper storage, accepting a longer
  restore time.
- **EFS Lifecycle Management** — automatically moves files not accessed for a set
  period into the **EFS Infrequent Access (IA)** storage class, cutting cost without
  changing how the application reads them.

## A worked example

A company's S3 bucket holds logs that are hot for 30 days and cold afterward: a
**lifecycle policy** transitions them to Glacier and expires them at 7 years. Some
data has unpredictable access, so it goes to **Intelligent-Tiering**. Compliance
archives that are read maybe once a year with hours of tolerance sit in **Glacier
Deep Archive**, restored via **Bulk** retrieval. The team migrates EBS volumes to
**gp3**, archives old snapshots to the **Snapshots Archive** tier, and enables
**EFS Lifecycle Management** so stale files drop to EFS IA automatically.

## Watch the minimum-duration trap

Cheaper S3 classes carry a **minimum storage duration** — 30 days for the IA
classes, 90 days for Glacier Instant and Flexible Retrieval, 180 days for Deep
Archive. If you store an object in a class and delete or transition it *before* that
minimum, you are still billed for the full minimum period. The practical lesson:

> **Do not transition short-lived data into IA or Glacier. Moving an object that
> lives only a few days into Standard-IA can cost *more* than leaving it in
> Standard, because of the 30-day minimum plus a per-GB retrieval charge.**

So lifecycle rules should transition data only once it has genuinely gone cold. The
IA and Glacier classes also add small per-object overhead and (for IA) retrieval
fees, which is exactly why **Intelligent-Tiering** exists: it makes the tiering
decision for you and charges no retrieval fee between its frequent and infrequent
tiers, so it is the safe default when you are unsure.

## Exam focus

- Unknown/changing access patterns, auto cost-optimize, no inter-tier retrieval fees
  → **S3 Intelligent-Tiering**.
- ~Monthly access with millisecond retrieval → **Standard-IA**; ~10-year cold
  archive, hours OK, cheapest → **Glacier Deep Archive**.
- **S3 Lifecycle policies** transition and expire objects automatically, including
  **expiring noncurrent versions** and **aborting incomplete multipart uploads**;
  **Storage Class Analysis** tells you what to transition.
- Glacier **Bulk** retrieval = lowest retrieval cost when you can wait hours.
- **gp2 → gp3** cuts EBS cost; **EBS Snapshots Archive** for rarely restored
  snapshots; **EFS Lifecycle Management → EFS IA** for infrequently accessed files.
