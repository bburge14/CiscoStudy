# Project Management & the Business Case

Most new systems arrive through projects, and projects are where money, time, and
risk collide. An IS auditor reviews projects to confirm they are justified,
controlled, and on track — and to catch trouble early, when it is still cheap to
fix. This lesson covers how a project is justified, organized, and scheduled, and
what the auditor watches for.

## Justifying the project: business case and feasibility

No project should start on enthusiasm alone. Two documents force a sober look
before resources are committed.

> A **business case** sets out the justification for the project — the problem,
> the proposed solution, the expected benefits, costs, and risks. It is revisited
> throughout the project to confirm the investment still makes sense.

> A **feasibility study**, conducted at the start, determines whether the proposed
> solution is **viable and worth pursuing** before the organization commits
> serious resources. It weighs technical, economic, operational, and schedule
> feasibility.

The feasibility study is the gate that asks *should we even do this?* — and the
answer "no" is a perfectly good outcome if the numbers or risks don't hold up.
The auditor checks that a real business case existed, was approved at the right
level, and is kept current rather than filed and forgotten.

## Organizing the project

Clear roles keep accountability from evaporating:

- **Project sponsor** — the senior business owner who champions the project,
  secures funding, and owns the benefits. The sponsor is accountable for the
  project delivering value.
- **Steering committee** — provides executive oversight, approves major decisions,
  and keeps the project aligned with business priorities.
- **Project manager** — plans, schedules, and runs the day-to-day work, managing
  scope, time, cost, and quality.
- **User/business representatives** — define requirements and ultimately accept
  the delivered system.

Projects are commonly framed through the **project management triangle** of
**scope, time, and cost** (with quality at the center): change one and the others
move. A disciplined project controls all three against a baseline.

## Scheduling and estimation

Once the work is defined, it must be broken down, sequenced, and estimated. The
exam tests a few specific techniques.

> A **work breakdown structure (WBS)** decomposes the project into manageable
> tasks. A **Gantt chart** then displays those tasks as horizontal bars on a
> timeline, showing start/finish and overlap — good for tracking progress at a
> glance.

The scheduling concept CISA tests most is the **critical path**.

> The **critical path** is the **longest sequence of dependent activities** in the
> project. It has **zero float (slack)** and therefore **determines the shortest
> possible overall duration**. Any delay on a critical-path task delays the whole
> project.

**Float (or slack)** is how long a non-critical task can slip without pushing out
the finish date; critical-path tasks have none. For estimating uncertain
durations, know **PERT**:

> **PERT (Program Evaluation and Review Technique)** uses **three time estimates —
> optimistic, most likely, and pessimistic** — to account for uncertainty in how
> long an activity will take, producing a weighted expected duration.

A quick comparison of the scheduling tools:

| Tool | What it shows |
|------|---------------|
| **WBS** | Hierarchical breakdown of the work into tasks |
| **Gantt chart** | Tasks on a calendar timeline, progress and overlap |
| **CPM / critical path** | The longest, zero-float path that sets minimum duration |
| **PERT** | Three-point estimates for uncertain activity durations |

Other estimation approaches include **function point analysis** (sizing software
by its functionality rather than lines of code) and comparison to similar past
projects.

## Watching for trouble

The auditor's advisory role in a project is to review controls and risks at each
stage *without* taking over management decisions — exactly the independence
posture from Domain 1. Common red flags:

- **Scope creep** — uncontrolled growth of requirements without matching
  adjustments to time and budget. The remedy is a disciplined **change control**
  process for requirements.
- **No baseline** — if scope, schedule, and budget were never baselined, there is
  nothing to measure slippage against.
- **Optimistic single-point estimates** on uncertain tasks, with no allowance for
  risk.
- **A sponsor in name only** — no active business owner steering benefits and
  decisions.

Methodologies such as **PMBOK** and **PRINCE2** provide the structured processes
that make this control possible; the auditor doesn't require a specific one, but
does expect disciplined planning, monitoring, and change control to be present.

## Exam focus

- A **feasibility study** decides whether the solution is **viable/worth
  pursuing** before committing resources; the **business case** justifies the
  investment and is kept current.
- The **project sponsor** (senior business owner) is accountable for benefits; the
  **steering committee** gives oversight; the **project manager** runs delivery.
- The **critical path** is the **longest, zero-float sequence** and sets the
  **minimum project duration**; a slip on it slips the whole project. **Float/
  slack** is spare time on non-critical tasks.
- **PERT** = **three-point** (optimistic/most likely/pessimistic) estimates for
  uncertainty; a **Gantt chart** shows tasks on a timeline; a **WBS** decomposes
  the work.
- **Scope creep** is uncontrolled requirement growth — control it with change
  control. The auditor advises on controls at each stage but never makes
  management's decisions.
