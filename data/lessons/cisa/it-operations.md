# IT Operations, Incident & Problem Management

Once systems are live, someone has to run them day after day — schedule the jobs,
watch the consoles, keep capacity ahead of demand, and respond when things break.
This is **IT operations and service management**, and it is the largest-weighted
territory on the CISA exam. The auditor's focus here is whether operations are
controlled, logged, and recoverable rather than improvised.

## Running operations under control

Routine operations carry quiet risks: an unauthorized job, an operator overstepping,
capacity running out at month-end. Controls keep these in check.

- **Job scheduling** — production jobs run on an approved schedule; the auditor
  checks that unauthorized or ad-hoc jobs can't simply be inserted.
- **Operator/console logs** — records of operator actions on systems.

> An IS auditor reviews **computer operator console logs** primarily to **detect
> unauthorized or unusual operator actions**. Log review is a **detective**
> control — it finds problems after they occur, which is exactly why the logs must
> be protected from the operators they monitor.

- **Capacity management** keeps resources ahead of need.

> **Capacity management** ensures computing resources are **sufficient to meet
> current and anticipated future business demand** — matching resources to demand
> so performance doesn't degrade and growth doesn't cause outages.

Operations also live or die by **change management**, the discipline that keeps
well-meaning changes from becoming incidents. Changes should be requested,
assessed for impact, approved, tested, and backed by a rollback plan. Emergencies
are the tricky case:

> **Emergency changes** are permitted — you can't always wait for a committee
> while production burns — but the **minimum acceptable control** is that they are
> **documented and reviewed/approved after the fact (retroactively authorized)**.
> A change made and then never reviewed is the finding.

Finally, **service-level agreements (SLAs)** define the service levels operations
must deliver (availability, response times), giving the auditor a yardstick to
measure performance against.

## IT service management: incident, problem, change

Modern IT operations are usually organized around **ITIL**-style service
management processes. CISA tests the distinctions between them relentlessly,
because the names sound similar but the goals differ.

> - **Incident management** aims to **restore normal service operation as quickly
>   as possible** and minimize business impact. Speed of restoration is the goal —
>   even a temporary workaround counts if it gets the business running.
> - **Problem management** aims to **identify and remove the underlying root
>   cause** of incidents, especially recurring ones, to stop them from happening
>   again.
> - **Change management** controls how modifications are made to the environment,
>   so changes are assessed, approved, and reversible.

The cleanest way to hold them apart:

| Process | Core goal | Mindset |
|---------|-----------|---------|
| **Incident** | Restore service **fast** | "Get it working now" |
| **Problem** | Eliminate the **root cause** | "Stop it recurring" |
| **Change** | Control **modifications** | "Do it safely and reversibly" |

An analogy: if a pipe bursts, **incident management** mops the floor and stops the
water so the business can operate; **problem management** investigates *why* the
pipe burst and replaces the faulty section; **change management** governs how that
replacement is approved and installed without causing a new leak.

When problem management can't fully fix a root cause right away, it records a
**known error** — a documented problem with a known cause — and often a
**workaround** that lets incident handlers restore service quickly in the
meantime. A **service desk** sits at the front, logging and routing incidents and
acting as the single point of contact for users. Underpinning all of it are
**SLAs** (and internal **OLAs**, operating-level agreements between internal
teams), which set the targets — response and resolution times, availability — that
these processes are measured against.

### What the auditor worries about most

> An IS auditor reviewing incident management is **most concerned if incidents are
> not recorded/logged**. Without logging there is **no tracking, no trend
> analysis, and no accountability** — you cannot manage, measure, or learn from
> what you never recorded.

Good incident handling also includes **classification and prioritization** (by
impact and urgency), **escalation** paths, and feeding recurring incidents into
problem management so the root cause finally gets fixed. A related operational
concept is **configuration management**, which maintains an accurate record of
assets and their relationships (a configuration management database) so that
changes and incidents can be understood in context.

## Tying it together

Notice how operations reuses the control vocabulary from the audit domains. Log
review is **detective**; change approval and segregation of the release path are
**preventive**; a rollback plan and incident restoration are **corrective**.
Emergency-change and privileged-activity reviews are **compensating** oversight
where prevention isn't possible. The auditor evaluating operations is really
checking that each of these layers exists, is logged, and is independently
reviewed — because an operations function that can act without a trace is one the
auditor cannot rely on.

## Exam focus

- **Console/operator log review** is a **detective** control used to **spot
  unauthorized/unusual operator actions**; protect the logs from those being
  monitored.
- **Capacity management** matches resources to **current and future demand**.
- **Emergency changes** are allowed but must be **documented and reviewed/approved
  after the fact (retroactive authorization)** — that is the minimum control.
- **Incident management = restore service fast; problem management = remove the
  root cause; change management = control modifications.** Don't swap them.
- The auditor's biggest incident-management concern is **incidents not being
  logged**, which kills tracking, trends, and accountability.
