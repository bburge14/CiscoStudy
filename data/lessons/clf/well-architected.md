# The AWS Well-Architected Framework

Anyone can launch a server. Building a workload that stays secure, survives
failure, performs well, and doesn't waste money is harder — and it's easy to only
notice the gaps after something breaks. AWS distilled years of reviewing customer
architectures into a checklist for getting this right: the **Well-Architected
Framework**. This lesson covers what it is and the six pillars you must know by
name.

## What the framework is

> The **AWS Well-Architected Framework** is a set of best practices and guiding
> questions, organized into **six pillars**, that help you design and continually
> improve secure, high-performing, resilient, and efficient cloud workloads.

Two things to be clear about:

- It is **guidance, not a product you deploy.** You don't "turn on"
  Well-Architected; you use it to *review* and *improve* an architecture.
- It is meant to be used **over time.** Architecture isn't a one-time decision —
  you re-review as the workload and your needs change.

AWS also offers the **AWS Well-Architected Tool**, a free service in the
Management Console that walks you through the pillar questions, records your
answers, and produces a report of risks and improvement suggestions. The
**framework** is the ideas; the **tool** is the questionnaire that applies them.

## The six pillars

Memorize these six. A classic exam question gives a one-line description and asks
which pillar it belongs to.

| Pillar | Core concern | Giveaway words in a question |
|--------|--------------|------------------------------|
| **Operational Excellence** | Run, monitor, and continually improve systems and processes | monitoring, automation, runbooks, small frequent changes |
| **Security** | Protect data, systems, and assets | least privilege, encryption, IAM, traceability |
| **Reliability** | Recover from failure and meet demand consistently | failover, auto-recovery, tested backups, horizontal scaling |
| **Performance Efficiency** | Use resources efficiently and pick the right ones | right resource type, latency, serverless, experimentation |
| **Cost Optimization** | Deliver value at the lowest price | eliminate waste, right-size, pick the right pricing model |
| **Sustainability** | Minimize the environmental impact of workloads | energy, efficiency, utilization, reduce resources |

A memory hook for the order: **O-S-R-P-C-S** — "Operations Secure Reliable
Performant Cheap Sustainable." Let's look at each.

### Operational Excellence

This pillar is about *running* the workload well and getting better at it. Think
monitoring, logging, and automation: perform operations as code, make **frequent,
small, reversible changes** so mistakes are easy to undo, and learn from every
event so you don't repeat it. If a question is about observing systems, responding
to events, or improving procedures, it's Operational Excellence.

### Security

Protecting information, systems, and assets. The headline practices: build a
**strong identity foundation** with least-privilege access, enable
**traceability** (log and monitor actions), apply security **at every layer**,
protect data **in transit and at rest** with encryption, and prepare for security
events. Anything about IAM, encryption, or who-can-do-what points here.

### Reliability

A reliable workload does its job correctly and consistently, and recovers when
things go wrong. Key ideas: **automatically recover from failure**, **test your
recovery procedures** (don't just assume backups work), **scale horizontally** to
add redundancy, and **stop guessing capacity**. Failover to a standby, multiple
Availability Zones, and tested disaster recovery are all Reliability.

> Reliability and Performance Efficiency are easy to confuse. Reliability is about
> *staying up and recovering* (availability, failover). Performance Efficiency is
> about *using the right resources well* (speed, efficiency). "Recovers from
> failure" → Reliability; "selects the right instance type for the job" →
> Performance Efficiency.

### Performance Efficiency

Using computing resources efficiently and keeping it that way as demand and
technology change. Practices include choosing the **right resource type and size**
for the job, making **data-driven decisions** through monitoring, going
**serverless** where it fits, and experimenting to find what performs best.

### Cost Optimization

Running systems to deliver business value at the lowest price point. This means
**avoiding unneeded costs**, understanding where the money goes, picking the right
**pricing model** (On-Demand vs. Reserved vs. Spot), **right-sizing**, and turning
off or scaling down what you aren't using. Note the contrast with Performance
Efficiency: both care about resource choice, but Cost Optimization optimizes for
*price* while Performance Efficiency optimizes for *speed and fit*.

### Sustainability

The newest pillar, added in 2021. It's about minimizing the **environmental
impact** of running cloud workloads: reduce energy consumption, maximize the
utilization of the resources you provision (idle capacity still draws power),
choose efficient Regions and instance types, and lean on **managed and serverless
services** that AWS runs at high efficiency. Sustainability has its own shared
responsibility: AWS works on sustainability *of* the cloud (efficient data
centers, renewable energy), and you work on sustainability *in* the cloud
(efficient workloads).

## How the pillars work together

The pillars often pull in different directions, and that's the point — they make
the trade-offs visible so you choose deliberately. Running three redundant copies
of everything is great for **Reliability** but costs more, which **Cost
Optimization** and **Sustainability** would question. A Well-Architected review
doesn't tell you there's one right answer; it makes sure you've weighed security,
resilience, performance, cost, and sustainability instead of discovering a gap
during an outage.

A few general design principles echo across the framework and are worth
recognizing:

- **Stop guessing capacity** — scale with demand rather than over-provisioning.
- **Test at production scale**, then tear the test environment down.
- **Automate** to make architectural experimentation easier and changes safer.
- **Design for failure** — assume components will fail and plan the recovery.
- **Drive architecture with data** instead of hunches.

## The whole thing in one paragraph

The **Well-Architected Framework** is best-practice *guidance* (not a deployable
service) organized into **six pillars** — **Operational Excellence, Security,
Reliability, Performance Efficiency, Cost Optimization, and Sustainability** — that
you use with the free **Well-Architected Tool** to review and keep improving a
workload. Each pillar owns a concern: operations and improvement, protecting data,
recovering from failure, using the right resources well, spending the least, and
minimizing environmental impact. They deliberately trade off against each other so
you make conscious decisions rather than discover weaknesses in an incident.

## Exam focus

- The framework has **six pillars**: **Operational Excellence, Security,
  Reliability, Performance Efficiency, Cost Optimization, Sustainability.** Know
  each by a one-line description.
- It is **guidance to review and improve architectures over time**, not a service
  you deploy. The **Well-Architected Tool** is the free console questionnaire that
  applies it.
- **Reliability** = recover from failure, failover, tested backups, meet demand.
  **Performance Efficiency** = pick the right resource type/size, use resources
  efficiently. Don't swap them.
- **Cost Optimization** optimizes for *price* (eliminate waste, right-size, right
  pricing model); **Performance Efficiency** optimizes for *fit and speed*.
- **Security** = least privilege, encryption in transit and at rest,
  traceability. **Operational Excellence** = monitoring, automation, small
  reversible changes.
- **Sustainability** (added 2021) = reduce energy use and maximize utilization to
  cut environmental impact.
