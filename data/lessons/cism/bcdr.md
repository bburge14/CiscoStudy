# Business Continuity & Disaster Recovery

Some incidents are big enough to threaten the organization's ability to operate
at all — a data-center fire, a region-wide outage, a crippling ransomware event.
Business continuity and disaster recovery are how a manager prepares the
organization to *survive* such disruptions and come back. The exam tests the
vocabulary precisely — RTO, RPO, MTD, BIA — and the manager's instinct that
continuity is a *business* decision driven by business impact, not a purely
technical one. This lesson closes the incident-management domain.

## Two related but distinct plans

People use "BCP" and "DRP" loosely; the exam does not. Keep them separate.

> **Business Continuity Planning (BCP)** keeps the organization's **essential
> business functions running** (or quickly resumed) during a disruption — the
> whole business, including people, facilities, and processes.
>
> **Disaster Recovery Planning (DRP)** is the subset focused on **restoring IT
> systems, data, and infrastructure** after a disaster. DRP is the technical
> engine inside the broader BCP.

The relationship: BCP is the big picture — *how does the business keep serving
customers?* — and DRP is one critical piece of it — *how do we get the systems
back?* If a question is about keeping the *business* alive, think BCP; if it's
about recovering *IT*, think DRP.

## The business impact analysis drives everything

Before you can plan recovery, you have to know what matters most. That's the job
of the **business impact analysis**, and it is the foundation of the whole
discipline.

> The **PRIMARY purpose of a business impact analysis (BIA)** is to **identify
> critical business processes and determine recovery priorities and objectives**
> such as RTO and RPO. It measures the impact of disruption over time.

The BIA answers: *Which processes are critical? How much does an outage of each
cost per hour or day? What depends on what?* From those answers, leadership sets
recovery priorities — which systems come back first — and the recovery objectives
below. Crucially, the BIA is a **business-led** exercise: the process owners, not
IT, tell you how long they can survive without a function. This is continuity's
version of "the business owns the decision."

## The recovery objectives — know these cold

This cluster of acronyms is the most heavily tested part of BC/DR. Learn each
precisely, and learn how they relate.

> - **RTO (Recovery Time Objective)** — the **target time to restore** a process
>   or system after disruption. "We must be back within 4 hours."
> - **RPO (Recovery Point Objective)** — the **maximum acceptable data loss**,
>   measured as a point in *time*. "We can lose no more than 15 minutes of data."
> - **MTD (Maximum Tolerable Downtime)** — the **longest** an outage can last
>   before the organization suffers unacceptable harm. The hard ceiling.
> - **WRT (Work Recovery Time)** — the time to **verify, re-enter data, and get
>   the restored system back to normal business use** after it's technically up.

The two most confused are RTO and RPO. Anchor them to *direction in time* around
the moment of disaster:

- **RPO looks backward** — how far back must the last good data be? It sets your
  **backup frequency.** A 15-minute RPO means backing up at least every 15
  minutes. *"How much data can we lose?" → RPO.*
- **RTO looks forward** — how fast must we be running again? It sets your
  **recovery capability** (and spending). *"How long until we're back?" → RTO.*

And the relationship that ties them together:

> **RTO + WRT ≤ MTD.** Technical recovery (RTO) plus the work to resume normal
> operations (WRT) must fit *inside* the maximum tolerable downtime. If your best
> achievable recovery exceeds the MTD, you have an unacceptable gap to close.

| Objective | Question it answers | Drives |
|-----------|---------------------|--------|
| **RTO** | How fast must we be back? | Recovery speed/spend |
| **RPO** | How much data can we lose? | Backup frequency |
| **MTD** | How long before fatal harm? | The ceiling RTO+WRT must fit under |

A tighter RTO or RPO costs more. The manager's job is to set each at the level the
BIA justifies — tight enough to survive, loose enough to afford — not to gold-plate
every system to zero downtime.

## Recovery strategies and sites

To meet the RTO, the organization pre-arranges somewhere and some way to recover.
The classic **alternate site** options trade cost against speed:

> - **Hot site** — a fully equipped, running duplicate with current data; recovery
>   in minutes to hours. Most expensive.
> - **Warm site** — hardware and connectivity in place but data/config must be
>   loaded; recovery in hours to a day. Middle cost.
> - **Cold site** — space and power only; everything must be brought in and set
>   up; recovery in days. Cheapest.

The choice follows the RTO: a process with a very short RTO needs a hot site; one
that can wait days can use a cold site. (Cloud-based recovery and active-active
designs now blur these categories, but the cost-vs-speed logic is unchanged.)
Backups underpin all of it, and the RPO dictates how often they run and how
quickly they must be restorable.

## Test it, or it isn't real

A continuity plan that's never exercised is a guess. Just as with incident
response, **testing** is what turns a document into a capability — and it's a
manager's responsibility to ensure it happens, from low-impact to realistic:

- **Tabletop / walkthrough** — talk through the plan against a scenario.
- **Simulation** — act out the response without touching production.
- **Parallel test** — bring up recovery systems alongside production to confirm
  they work.
- **Full interruption** — actually fail over to recovery (highest confidence,
  highest risk).

Each test should feed lessons back into the plan — the same improvement loop you
saw in the post-incident review. Plans also need regular review as the business
and its systems change; a BIA from three years ago describes a business that may
no longer exist.

## The manager's reflex

- **BCP keeps the business running; DRP restores IT.** DRP sits inside BCP.
- The **BIA** identifies **critical processes and sets recovery priorities and
  objectives** — and it's business-led.
- **RTO = time to restore; RPO = acceptable data loss; MTD = the ceiling**, with
  **RTO + WRT ≤ MTD.** Tighter objectives cost more.
- Match **site type (hot/warm/cold) to the RTO**, and **test** the plan.

## Exam focus

- **BCP** keeps **essential business functions** operating; **DRP** restores **IT
  systems and data.** DRP is a subset of BCP.
- The **BIA's PRIMARY purpose is to identify critical processes and determine
  recovery priorities and objectives (RTO, RPO).** It's driven by the business.
- **RTO** = target **time to recover**; **RPO** = maximum acceptable **data loss**
  (in time, setting backup frequency); **MTD** = **maximum tolerable downtime**
  (the ceiling). Remember **RTO + WRT ≤ MTD.** "How much data can we lose?" = RPO;
  "how fast are we back?" = RTO.
- **Site types track cost vs. speed: hot (fast, costly) → warm → cold (slow,
  cheap)**; choose by the RTO the BIA justifies.
- **Test continuity/DR plans** (tabletop, simulation, parallel, full
  interruption) and **feed results back** into the plan; keep the BIA current.
