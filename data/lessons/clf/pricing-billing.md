# Pricing Models & Cost Management

The cloud's pay-as-you-go promise only pays off if you choose the right pricing
model and keep an eye on the bill. This lesson covers how AWS charges you, the
**purchase options** that can slash compute costs, and the **tools** for
estimating, monitoring, and controlling spend. You won't be asked exact dollar
figures — you *will* be asked which option or tool fits a situation.

## What you actually pay for

Most of your AWS bill comes down to three fundamentals:

> You generally pay for **compute** (the time your resources run), **storage** (the
> data you keep), and **data transfer** (data moving **out** of AWS).

A detail worth remembering: **data transfer *into* AWS is usually free**, while
data transfer *out* to the internet is charged. AWS wants to make it easy to bring
data in; sending lots of data out is where transfer costs appear. Beyond that, the
guiding philosophy is **pay-as-you-go** — pay only for what you use, with no
long-term contract required unless you choose one for a discount.

## EC2 purchase options

Compute is often the biggest line item, and EC2 gives you several ways to pay for
it. Matching a workload's *pattern* to the right option is the most tested idea in
this domain.

| Option | How it works | Best for |
|--------|--------------|----------|
| **On-Demand** | Pay by the second/hour, **no commitment**, no upfront cost | **Short-term, spiky, or unpredictable** workloads; getting started |
| **Reserved Instances (RIs)** | Commit to a **1- or 3-year** term for a large discount | **Steady-state, always-on** workloads (e.g. a production database) |
| **Savings Plans** | Commit to a **consistent amount of spend ($/hour)** for 1 or 3 years for a discount, with more **flexibility** than RIs | Predictable usage where you want flexibility across instance types |
| **Spot Instances** | Use AWS's **spare capacity** at a steep discount, but AWS can **reclaim it** with little notice | **Fault-tolerant, interruptible** work: batch jobs, testing |
| **Dedicated Hosts** | A **physical server** dedicated to you | Strict **compliance** or **software licensing** that requires dedicated hardware |

How to pick on the exam:

- **"Spiky / unpredictable / no commitment"** → **On-Demand.**
- **"Always-on for years, lowest steady cost"** → **Reserved Instances** (or a
  **Savings Plan** if the clue stresses flexibility).
- **"Can tolerate interruptions, wants the deepest discount"** → **Spot.**
- **"Needs dedicated physical hardware for licensing/compliance"** → **Dedicated
  Hosts.**

> The mental model: **On-Demand** is renting a car by the day (flexible, pricey per
> hour); **Reserved/Savings Plans** are a long lease (cheaper, you commit);
> **Spot** is standby airline tickets (cheap, but you might get bumped).

## The AWS Free Tier

New accounts get the **AWS Free Tier**, which comes in three forms:

- **Always free** — services with a free allowance that never expires (e.g. a
  monthly amount of Lambda requests).
- **12 months free** — free up to a limit for the first year after sign-up.
- **Trials** — short-term free trials of specific services.

The Free Tier is how you learn and experiment at no cost — but watch the limits, or
usage beyond them starts to bill.

## Estimating before you build

Smart teams forecast cost *before* launching, not after the invoice arrives.

- **AWS Pricing Calculator** — estimate the monthly cost of a **planned**
  architecture. Enter the EC2, S3, and other resources you intend to use, and it
  produces a cost estimate. The go-to tool for "how much *will* this cost before I
  build it?"

## Watching what you spend

Once you're running, three tools track and control actual spend. They're easy to
confuse, so pin down each one's job.

| Tool | Job |
|------|-----|
| **AWS Cost Explorer** | **Visualize and analyze past spend** over time, by service, and **forecast** future cost |
| **AWS Budgets** | Set a custom **threshold** and get **alerted** (e.g. email) when spend — actual or forecast — exceeds it |
| **AWS Cost and Usage Report (CUR)** | The **most detailed** billing data available, for deep analysis |

> **Cost Explorer** is for *looking at and forecasting* your spending trends.
> **Budgets** is for *being alerted* when you cross a limit you set. If the scenario
> says "**notify me** when spend exceeds X," it's **Budgets**; if it says
> "**visualize and forecast** past spend," it's **Cost Explorer**.

## Consolidated billing and cost tracking

For organizations running many accounts:

- **Consolidated billing** (through **AWS Organizations**) combines multiple
  accounts into **one bill**, and can unlock **volume discounts** because usage is
  aggregated across accounts.
- **Cost allocation tags** — label resources (by project, team, or environment) so
  you can **break the bill down** by whatever categories matter to you.
- The **AWS Billing dashboard** is the console home for viewing invoices and
  current charges.

## The whole thing in one paragraph

AWS charges mainly for **compute, storage, and data transfer out** (data *in* is
usually free), on a **pay-as-you-go** basis. For EC2 you choose a purchase option
by workload pattern: **On-Demand** (spiky, no commitment), **Reserved
Instances/Savings Plans** (always-on, committed discount), **Spot** (interruptible,
deepest discount), or **Dedicated Hosts** (licensing/compliance). The **Free Tier**
lets you start free. Estimate ahead with the **Pricing Calculator**, then track
actuals with **Cost Explorer** (visualize/forecast) and **Budgets** (alert on a
threshold), use the **Cost and Usage Report** for detail, and combine accounts with
**consolidated billing** plus **cost allocation tags** to see who spent what.

## Exam focus

- You pay for **compute, storage, and data transfer out**; **data transfer in is
  typically free**. Everything is **pay-as-you-go** by default.
- EC2 options: **On-Demand** = spiky/no commitment; **Reserved Instances** =
  always-on, 1/3-year commitment, lowest steady cost; **Savings Plans** = committed
  spend with flexibility; **Spot** = interruptible, deepest discount; **Dedicated
  Hosts** = dedicated physical hardware for licensing/compliance.
- **Free Tier** has three types: **always free**, **12 months free**, and
  **trials**.
- **Pricing Calculator** = estimate cost **before** building.
- **Cost Explorer** = **visualize and forecast** spend; **AWS Budgets** = **alert**
  when spend crosses a threshold. Match "notify me" → Budgets, "analyze/forecast" →
  Cost Explorer.
- **Consolidated billing** (via Organizations) = one bill + possible **volume
  discounts**; **cost allocation tags** break the bill down by project/team.
