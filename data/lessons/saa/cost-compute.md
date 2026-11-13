# Cost-Optimized Compute

Compute is usually the biggest line on an AWS bill, so the Cost Optimization pillar
leans hard on choosing the right *purchase model* for each workload's behavior. The
exam gives you a usage pattern — steady 24/7, interruptible batch, spiky and
unpredictable, idle most of the time — and asks for the cheapest option that still
meets the requirement. The core skill is matching commitment to predictability.

## The four purchase models

> **On-Demand** = pay by the second, no commitment, highest per-hour price — for
> short-term, unpredictable, or spiky workloads.
> **Reserved Instances / Savings Plans** = commit for 1 or 3 years for a large
> discount — for steady, predictable baseline load.
> **Spot** = use spare capacity for up to ~90% off, but AWS can reclaim it with a
> two-minute warning — for fault-tolerant, interruptible work.

Mapping the stem to the model is almost mechanical:

- "Fault-tolerant batch job that can be interrupted and resumed, lowest cost" →
  **Spot**.
- "Runs 24/7 at a predictable, steady level for three years" → **Reserved Instance
  or Savings Plan**.
- "Short-term and unpredictable" → **On-Demand**.

## Savings Plans: Compute vs EC2 Instance

Savings Plans commit you to an hourly spend for 1 or 3 years. Two flavors, and the
exam tests the trade-off:

| Plan | Flexibility | Discount | Covers |
|------|-------------|----------|--------|
| **Compute Savings Plans** | Any instance family, Region, OS | Up to ~66% | EC2 **plus Fargate and Lambda** |
| **EC2 Instance Savings Plans** | One family in one Region | Up to ~72% | EC2 in that family/Region |

> **Choose Compute Savings Plans for flexibility across families, Regions, and even
> Fargate/Lambda. Choose EC2 Instance Savings Plans (or Standard RIs) for the
> *largest* discount when you can commit to one family in one Region.**

Standard Reserved Instances reach a similar ~72% to EC2 Instance Savings Plans but
are less flexible; Savings Plans are generally the simpler modern choice.

## Spending less per instance: Graviton and right-sizing

- **AWS Graviton** — AWS's ARM-based processors, which typically give better
  price-performance and lower cost than comparable x86 instances. If a modern Linux
  stack can be recompiled for ARM, migrating to Graviton cuts cost while keeping or
  improving performance.
- **Right-sizing** — when instances sit at 10–15% utilization, move to smaller
  instance types and let **Auto Scaling** add capacity for peaks, rather than paying
  for idle headroom.

## Combining models and going serverless

Real fleets blend purchase models:

- **Auto Scaling mixed-instances policy** — keep a guaranteed baseline on
  **On-Demand** (or Reserved) and run the elastic, scalable portion on cheaper
  **Spot** instances. This gives a stable floor plus cheap burst capacity.
- **Fargate Spot** — stateless, fault-tolerant containers that tolerate
  interruption run cheapest on Fargate Spot.
- **Re-architect to Lambda** — a lightly used internal service that runs 24/7 but is
  invoked only occasionally wastes money sitting idle. Moving it to **Lambda** means
  paying only per invocation, often far cheaper than a mostly-idle instance.

## A worked example

A company's steady production database tier runs 24/7, so it buys a **3-year
Reserved Instance or EC2 Instance Savings Plan** for the deepest discount. The
web fleet in an Auto Scaling group keeps a small **On-Demand** baseline and bursts
on **Spot** via a mixed-instances policy. A nightly, interruptible image-processing
batch runs entirely on **Spot**. A rarely used admin tool is rewritten as a
**Lambda** function so it costs nothing when idle, and the whole Linux fleet is
migrated to **Graviton** for better price-performance.

## Reading the keywords

Cost-compute questions are keyword games. Train yourself to spot the trigger word
and the model it maps to:

- "interruptible," "can be resumed," "fault-tolerant batch" → **Spot**.
- "steady," "predictable," "24/7," "for the next 1 or 3 years" → **Savings Plan /
  Reserved Instance**.
- "unpredictable," "short-lived," "can't commit" → **On-Demand**.
- "flexible across families and Regions," "also covers Lambda/Fargate" → **Compute
  Savings Plans**.
- "ARM," "can recompile the stack" → **Graviton**.
- "runs only occasionally," "idle most of the time" → **Lambda**.

Two options appear as *distractors* in cost questions, so know why they are usually
wrong:

- **Dedicated Hosts** give you a physical server for licensing (bring-your-own
  per-socket/per-core licenses) or hard compliance isolation — not a general
  cost-savings lever.
- **On-Demand Capacity Reservations** guarantee capacity in an AZ but give **no
  discount** by themselves; they are about availability, not price. (You can pair
  them with a Savings Plan to get both.)

## Exam focus

- **On-Demand** = short/unpredictable; **Reserved/Savings Plans** = steady, long-
  running baseline; **Spot** = interruptible, fault-tolerant, up to ~90% off (two-
  minute reclaim warning).
- **Compute Savings Plans** = flexible across family/Region and cover **Fargate and
  Lambda**; **EC2 Instance Savings Plans** (or Standard RIs) = largest discount for
  one committed family/Region.
- **Graviton** (ARM) = lower cost / better price-performance for compatible
  workloads. **Right-size + Auto Scaling** for chronically underutilized instances.
- **Mixed-instances policy** = On-Demand baseline + Spot burst. **Fargate Spot** =
  cheap interruptible containers. **Re-architect an idle 24/7 service to Lambda** to
  pay only per use.
