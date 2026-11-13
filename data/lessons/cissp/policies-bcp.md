# Security Policies, Agreements & Business Continuity

Governance only becomes real when it is written down and when the organization has
a plan to keep operating through disaster. This lesson covers two practical halves
of Domain 1: the hierarchy of governance documents (and the agreements that bind
outside parties), and the business continuity and disaster recovery *planning* that
decides how fast you must recover and how much data you can afford to lose.

## The policy framework

Programs express management's intent through a layered set of documents. People
confuse these constantly, so learn the exact authority level of each.

> A **policy** states management's high-level intent (*what* and *why*). A
> **standard** makes a requirement specific and **mandatory** (*which* technology
> or setting). A **procedure** gives the exact, ordered steps (*how*). A
> **baseline** sets the mandatory minimum configuration. A **guideline** is
> **optional**, recommended advice.

| Document | Mandatory? | What it does | Example |
|----------|-----------|--------------|---------|
| **Policy** | Yes | High-level intent and expectations | "We protect customer data." |
| **Standard** | Yes | Specific required rule | "Laptops use AES-256 full-disk encryption." |
| **Baseline** | Yes | Minimum security configuration for a system class | "All servers meet the CIS Level 1 benchmark." |
| **Procedure** | Yes | Step-by-step instructions | "Steps to provision a new account." |
| **Guideline** | No | Optional best-practice advice | "Consider a passphrase of several words." |

> The single biggest tell on the exam: **only guidelines are optional.** Policies,
> standards, baselines, and procedures are all mandatory. If the stem says
> "recommended but not required," the answer is **guideline**.

An **Acceptable Use Policy (AUP)** defines how employees may use company systems.
Policies are approved and endorsed by **senior management**, which gives them
authority even though security staff draft them.

## Agreements with outside parties

When you work with partners, vendors, or interconnected systems, the right
*document* is a favorite exam question. Match the need precisely.

- **SLA (Service Level Agreement)** — commits a provider to measurable service
  levels (uptime, response time) with penalties for missing them.
- **MOU / MOA (Memorandum of Understanding / Agreement)** — a relatively informal
  statement of intent to cooperate; not as enforceable as a contract.
- **ISA (Interconnection Security Agreement)** — specifies the **technical and
  security requirements** for connecting two systems or networks.
- **BPA (Business Partnership Agreement)** — governs a business partnership
  (responsibilities, profit sharing).
- **OLA (Operational Level Agreement)** — an internal agreement between teams that
  supports an SLA.
- **NDA (Non-Disclosure Agreement)** — binds parties to confidentiality.

The classic distinction: two organizations wiring their networks together and
needing the *security terms* of that link want an **ISA**; a promise about
*service quality* is an **SLA**; a loose intent to cooperate is an **MOU**;
confidentiality is an **NDA**.

## Business continuity vs disaster recovery

These two are related but not identical, and the exam separates them.

> **Business Continuity Planning (BCP)** is the broad, business-focused effort to
> keep *essential functions* running during and after a disruption — it is
> strategic and includes people, processes, and communications. **Disaster
> Recovery Planning (DRP)** is the narrower, technical subset focused on
> **restoring IT systems and data** after a disaster.

BCP is the umbrella; DRP lives underneath it. BCP asks "how does the business keep
serving customers?"; DRP asks "how do we get the data center back?"

## The Business Impact Analysis and its metrics

The **Business Impact Analysis (BIA)** is the cornerstone of continuity planning.
It identifies the organization's critical business functions, the resources they
depend on, and the impact over time if they stop. From the BIA come the recovery
metrics you must know cold:

| Metric | Question it answers |
|--------|---------------------|
| **MTD / MTPD** (Maximum Tolerable Downtime) | How long can this function be down before the damage is unacceptable? |
| **RTO** (Recovery Time Objective) | How quickly must we restore the function/system? |
| **WRT** (Work Recovery Time) | After the system is back, how long to verify data and resume normal work? |
| **RPO** (Recovery Point Objective) | How much data (measured in time) can we afford to lose? |

> The relationship that shows up again and again: **RTO + WRT must not exceed the
> MTD.** If MTD is 8 hours, your recovery (RTO) plus the work to get back to
> business (WRT) together have to fit inside those 8 hours. **RPO is a separate
> axis** — it governs *data loss* (backup frequency), not downtime. A 1-hour RPO
> means backups at least hourly.

A lower RTO or RPO costs more. The planner's job is to balance the cost of
recovery capability against the cost of downtime the BIA revealed.

## Recovery sites

If a facility is lost, where do operations resume? Know the trade-off between cost
and speed:

- **Hot site** — fully equipped, data mirrored, ready in minutes to hours. Most
  expensive; lowest RTO.
- **Warm site** — hardware and connectivity in place but data must be loaded;
  ready in hours to days. Middle ground.
- **Cold site** — space and power only; everything else must be brought in and
  configured; days to weeks. Cheapest; longest RTO.
- **Mobile site** — a transportable unit (trailer) for field recovery.
- **Cloud / redundant site** — increasingly the default; recovery capacity on
  demand.

A **reciprocal (mutual-aid) agreement** — two firms agreeing to host each other in
a disaster — is cheap but its drawbacks are the tested point: during a *regional*
disaster the partner may have no spare capacity, enforceability is weak, and
hosting a competitor's systems raises serious **confidentiality** concerns. It is
rarely the BEST answer when reliability matters.

## Exam focus

- Document hierarchy: **policy** (intent) → **standard** (mandatory specifics) →
  **baseline** (mandatory minimum) → **procedure** (mandatory steps) →
  **guideline** (**optional** advice). "Recommended but not required" = guideline.
  **Senior management approves policy.**
- Pick the agreement: **ISA** = technical/security terms of an interconnection,
  **SLA** = service levels, **MOU/MOA** = informal intent, **BPA** = partnership,
  **OLA** = internal supporting agreement, **NDA** = confidentiality.
- **BCP** is the broad business umbrella; **DRP** is the IT-restoration subset.
- The **BIA** identifies critical functions and produces **MTD, RTO, WRT, RPO**.
  Remember **MTD = RTO + WRT**, and **RPO measures tolerable data loss** (drives
  backup frequency) — a different axis from downtime.
- Sites by cost/speed: **hot** (fast, costly) → **warm** → **cold** (cheap, slow).
  A **reciprocal agreement** is cheap but unreliable in a regional disaster and
  raises confidentiality concerns — rarely the BEST choice.
