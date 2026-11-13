# Managing Costs in Azure

The flip side of pay-as-you-go is that costs can creep up if nobody is watching.
Azure gives you a toolkit for the whole cost lifecycle: **estimate** before you
deploy, **track and analyze** what you are actually spending, **alert** when
spending moves unexpectedly, and **optimize** to pay less for the same work. This
lesson covers what drives cost in the first place, the tools that forecast and
monitor it, and the levers you pull to bring it down.

## What actually drives your bill

Before you can manage cost, you need to know what Azure charges for. Several
factors combine to produce the number on your invoice:

- **Resource type and settings** — a large VM costs more than a small one; a
  premium disk costs more than a standard one. The specific SKU matters.
- **Consumption / usage** — pay-as-you-go means the *amount* you use (hours a VM
  runs, gigabytes stored, number of operations) drives the charge.
- **Region** — the same resource can cost different amounts in different regions.
- **Bandwidth (data transfer)** — moving data **out** of Azure (egress) is
  generally billed, while data coming **in** (ingress) is typically free. Transfer
  between regions can also incur charges.

> Two factors that genuinely change what a resource costs are its **type/size** and
> the **region** it runs in — along with how much you **use** it and how much data
> leaves Azure. Things like the color of the portal theme or the day of the week
> do not.

This explains a tricky scenario: **the same VM, unchanged in size or
configuration, can cost more one month than the next.** Why? Because cost also
depends on **how many hours it ran**, how much **data it sent out**, and any
**regional price changes** — none of which require altering the VM itself.

## Estimating cost *before* you deploy

Two calculators help you plan, and the exam distinguishes them by their job:

> **The Azure Pricing Calculator** estimates the monthly cost of **Azure services
> you are considering**, based on the configuration, region, and expected usage you
> enter. Use it to price a future deployment.

> **The Total Cost of Ownership (TCO) tool / Azure Migrate business case** compares
> your **current on-premises costs against the equivalent Azure services**,
> producing a migration business case. Use it to justify a move to the cloud.

The tell is the comparison. If a company wants a **migration business case
comparing its existing on-premises datacenter cost to Azure**, that is the **TCO
Calculator** (modern migrations can build the same case with Azure Migrate). If it
simply wants to **estimate the price of some Azure services it plans to run**, that
is the **Pricing Calculator**.

## Tracking and controlling spend *after* you deploy

> **Microsoft Cost Management** is the service for monitoring, analyzing, and
> controlling your actual Azure spending. It shows where money is going, breaks it
> down by resource or department, and lets you set budgets and alerts.

### Budgets and alerts

A **budget** in Cost Management is a spending threshold you define for a
subscription, resource group, or other scope. The key fact the exam tests is what
a budget does when you cross it:

> **By default, exceeding a budget only triggers an alert (a notification). It does
> not automatically stop deployments or shut anything down.** Resources keep
> running; the budget warns you so a human can act.

(You *can* wire a budget to automated actions, but on its own it just notifies.)

Separately, **cost alerts** — including **anomaly alerts** — warn you about
**unexpected spikes** in spending so you can investigate a sudden jump rather than
discovering it on next month's invoice.

### Which cost tool for which job

| You want to… | Tool |
|--------------|------|
| Estimate the price of Azure services you plan to deploy | **Pricing Calculator** |
| Compare current on-premises costs against Azure (migration case) | **TCO Calculator / Azure Migrate business case** |
| Track and analyze what you are actually spending | **Microsoft Cost Management** |
| Be warned when spending crosses a threshold or spikes | **Budgets & cost alerts** |

## Optimizing: paying less for the same work

Once you can see your spend, several levers reduce it. Expect scenarios that ask
for the action that "most directly reduces cost."

- **Shut down / deallocate idle resources.** A development VM needed only during
  business hours should be **stopped (deallocated)** when not in use — you stop
  paying for its compute while it is off. This is the most direct way to cut the
  cost of a part-time workload.
- **Reservations.** Commit to a resource (such as a VM) for **one or three years**
  in exchange for a significant discount versus pay-as-you-go — ideal for steady,
  predictable workloads.
- **Azure Hybrid Benefit.** Reuse existing on-premises Windows Server or SQL Server
  licenses in Azure to avoid paying for them again.
- **Spot virtual machines.** Run interruptible workloads on Azure's spare capacity
  at a steep discount, accepting that they can be evicted when capacity is needed.
- **Right-sizing and autoscale.** Match resource size to real demand, and let
  autoscale add capacity only when it is needed and remove it when it is not.
- **Choose a cheaper region** when compliance and latency allow, since pricing
  varies by region.

A useful way to file these: **reservations, Hybrid Benefit, and spot VMs** change
*how you pay*; **shutting down, right-sizing, and autoscale** change *how much you
run*. Both lower the bill.

## The cost lifecycle in one view

Know your **cost drivers** (type, usage, region, egress). **Estimate** ahead with
the **Pricing Calculator** (future Azure costs) or the **TCO/Azure Migrate business
case** (on-prem vs Azure). **Track** real spend in **Microsoft Cost Management**,
set **budgets** (which alert, not block) and **cost/anomaly alerts** for spikes.
Then **optimize** with reservations, Hybrid Benefit, spot VMs, shutting down idle
resources, right-sizing, and autoscale.

## Exam focus

- Cost depends on **resource type/size, usage, region, and outbound data transfer
  (egress)**. Ingress is generally free. An unchanged VM can cost more month to
  month due to **hours run, egress, or regional price changes**.
- **Pricing Calculator** = estimate the cost of **future Azure services**. **TCO
  Calculator / Azure Migrate business case** = compare **on-premises vs Azure** for
  a migration.
- **Microsoft Cost Management** = analyze and control actual spend. A **budget**,
  by default, **only alerts** when exceeded — it does **not** stop resources.
  **Cost/anomaly alerts** warn about unexpected spikes.
- Cut costs by **shutting down (deallocating) idle VMs**, **reservations** (1- or
  3-year commitment discount), **Azure Hybrid Benefit** (reuse existing licenses),
  **spot VMs** (discounted interruptible capacity), and **right-sizing/autoscale**.
- The "dev VM only needed in business hours" answer is to **stop/deallocate it**
  when idle.
