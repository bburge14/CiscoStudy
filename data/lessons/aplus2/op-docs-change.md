# Documentation & Change Management

The operational side of IT is less about wires and more about **writing things
down** and **changing things carefully**. This lesson covers the documents a
well-run shop keeps, and the process that keeps a change from taking down
production. The exam tests whether you can name the right document and the right
change-process step for a given situation.

## Documentation: the right document for the job

A help-desk ticket has a predictable life, and the **documentation types** each
answer a different question.

### Inside a ticket

A good ticket records the **problem description**, **categories/severity**, and —
the part the exam asks about — **progress notes**: a **running, timestamped account
of each action** taken while the issue is being worked. When the ticket closes,
the **resolution** is written up.

> A **running, timestamped log of actions** on a ticket = **progress notes**.

### Standing documents

| Document | What it is | Telltale phrase |
|----------|-----------|-----------------|
| **Standard Operating Procedure (SOP)** | exact, repeatable **step-by-step** instructions for a task | "the steps we always follow to image and configure a laptop" |
| **Knowledge base** | a **searchable repository** of write-ups/solutions | "added the fix to a shared, searchable repository so colleagues can find it" |
| **Asset management** | an inventory database with **asset tags**, serials, purchase dates, warranty | "a barcoded label on every laptop, tracked centrally" |
| **Password policy** | rules for **length, complexity, and change frequency** | "minimum length, required complexity, how often users must change" |
| **Acceptable Use Policy (AUP)** | what users may/may not do with company IT | "rules for acceptable use of company devices" |
| **Network topology diagram** | a map of how devices connect | "a diagram of the network layout" |

Read the telltale phrases against the stems and the answers fall out:

- "The exact, repeatable **step-by-step** instructions the team follows to image and
  configure a new laptop" → a **Standard Operating Procedure (SOP)**.
- "Attach a unique **barcoded label** to every laptop and record serial, purchase
  date, and warranty in a central database" → **asset management** (with asset
  tags).
- "Minimum length, required complexity, and how often users must change their
  credentials" → the **password policy**.
- "Write up the symptoms and fix and add it to a shared, **searchable repository**"
  → the **knowledge base**.

### Other records worth naming

A few more documents round out a shop's paperwork:

- **Incident reports** — a written record of a security or safety incident: what
  happened, when, who was involved, and how it was handled.
- **Regulatory / compliance policy** — rules the organization must follow because of
  law or industry standards (HIPAA, PCI-DSS, and the like).
- **Inventory lists / procurement life cycle** — part of asset management, tracking
  a device from purchase through retirement and disposal.
- **New-user setup / end-of-life checklists** — standardized onboarding and
  offboarding steps so nothing is missed.

The common thread: documentation turns one person's knowledge into something the
whole team can repeat, audit, and improve.

## Change management: don't break production

Change management is the discipline of making changes **predictably and
reversibly**. A formal process runs a change through documentation, review,
testing, and approval before anyone touches production.

### The pieces the exam names

- **Change request / documented business process** — a formal request stating the
  **purpose, scope, and risk analysis** of the change.
- **Change Advisory Board (CAB)** — the **group that reviews a proposed change and
  formally approves or rejects it** before implementation. If a stem asks *who
  approves* a change, it's the **CAB**.
- **Rollback (backout) plan** — the predefined steps to **revert** if the change
  **fails in production**. When management asks "what will you do if the upgrade
  breaks?", they're asking for the **rollback plan**.
- **Sandbox testing** — apply and test the change first in an **isolated
  environment that mirrors production but can't affect it**. That's where you catch
  problems safely.
- **End-user acceptance** — confirmation that the **affected department has reviewed
  and agreed** to the change before it's scheduled.

> **Four quick matches:** "what if it fails?" = **rollback plan**; "who approves?" =
> **CAB**; "test it safely first" = **sandbox**; "did the users sign off?" =
> **end-user acceptance**.

### Why the order matters

The pieces aren't busywork — they form a safety net. You **document** the change so
everyone understands it, **test in a sandbox** so surprises happen off-production,
get the **CAB's approval** and **end-user acceptance** so it's authorized and
expected, and keep a **rollback plan** so a bad outcome is recoverable in minutes
instead of hours. Skipping any one of them is how a routine upgrade becomes an
outage.

Walk one through. A team wants to upgrade a production server:

> 1. They write a **change request** describing the purpose, scope, and risk.
> 2. They apply and test it in a **sandbox** that mirrors production.
> 3. The **CAB** reviews the request and approves it.
> 4. The affected department signs off — **end-user acceptance**.
> 5. A **rollback plan** is documented in case the upgrade fails.
> 6. Only then is the change **scheduled and implemented**, with a review after.

Pull any step out and you can name it from the gap it leaves — that's exactly how
the exam phrases these questions.

## The whole thing in one paragraph

Pick the document by its job: **progress notes** are the timestamped action log on a
ticket; an **SOP** is the exact step-by-step procedure; a **knowledge base** is the
searchable solution repository; **asset management** tracks tagged hardware with
serials/warranty; and the **password policy** sets length/complexity/change rules.
Change management keeps production safe with a documented **change request**, a
**CAB** that approves or rejects it, **sandbox testing** in an isolated mirror of
production, documented **end-user acceptance**, and a **rollback plan** to revert if
the change fails.

## On the exam

- **SOP** = repeatable step-by-step instructions; **knowledge base** = searchable
  repository; **asset management/tag** = tracked inventory; **password policy** =
  length/complexity/expiration rules; **progress notes** = the timestamped action
  log in a ticket.
- Change-process matches: **"what if it fails?" → rollback/backout plan**; **"who
  approves?" → Change Advisory Board (CAB)**; **"test safely first" → sandbox**;
  **"did affected users agree?" → end-user acceptance**.
- A formal change is **documented, tested, approved, and reversible** — expect
  questions that name one missing piece and ask what it is.
