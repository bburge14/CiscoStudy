# Asset, Change & Configuration Management

Most security failures are not clever zero-day exploits. They are far more boring:
a server nobody knew existed, a change that quietly opened a port, a device whose
configuration drifted away from the hardened baseline. This lesson is about the
disciplined, unglamorous processes that keep an environment *known* and *stable* —
because you cannot protect what you cannot see, and you cannot trust what you
cannot account for.

## Asset management: you can't protect what you can't see

An **asset** is anything of value to the organization — servers, laptops,
software licenses, data, even people. **Asset management** is the practice of
knowing what you have, where it is, and who is responsible for it.

> An **asset inventory** is a complete, maintained list of the organization's
> hardware, software, and data assets. It is the foundation of every other
> control: patching, access control, and incident response all depend on knowing
> the asset exists.

Key ideas the exam tests:

- Every asset should have an **owner** — the person accountable for its
  protection and for decisions about it.
- Assets move through a **lifecycle**: acquisition -> deployment -> operation and
  maintenance -> **secure disposal**. Disposal matters as much as acquisition; a
  decommissioned drive full of data is a breach waiting to happen.
- **Shadow IT** — hardware or cloud services deployed without approval — is
  dangerous precisely because it is *not* in the inventory and therefore not
  patched, monitored, or governed.

## Configuration management: keeping systems in a known-good state

Where asset management tracks *what you have*, **configuration management** tracks
*how each thing is set up* and keeps it that way.

> A **configuration item (CI)** is any component under configuration control — a
> server, an application, a network device, and its documented settings. The
> **Configuration Management Database (CMDB)** is the repository that records all
> CIs, their attributes, and the relationships between them.

- A **baseline** is a documented, approved standard configuration — the
  known-good state every system of a given type must match (for example, every
  web server has logging on, unused services off, and the current patch level).
- **Configuration drift** is the gradual, unapproved divergence of a live system
  from its baseline. Drift is how a hardened system slowly becomes vulnerable.
  Detecting and correcting drift is a core operational control.
- **Secure baselines** and drift detection are what let you say, with evidence,
  that a system is configured the way policy requires.

## Change management: don't let good intentions break security

The **change management** process ensures that modifications to systems are
reviewed, approved, tested, and reversible — so a well-meaning update doesn't
become an outage or a security hole. A single ad-hoc change by a well-meaning
admin causes more incidents than most attackers do.

The formal flow, and the terms you must recognize:

1. **Request for Change (RFC)** — the first formal step. It documents what is
   being changed, why, and its scope. No RFC, no change.
2. **Impact analysis** — what could this break, including security effects and
   dependencies on other systems?
3. **Approval** — a **Change Advisory Board (CAB)** or designated approver signs
   off. Changes are not made on a whim.
4. **Testing** — prove the change works in a test environment before it touches
   production.
5. **Back-out (rollback) plan** — a documented way to undo the change if it goes
   wrong. This is required *before* implementation, so you can always return to
   the prior known-good state.
6. **Implementation in a maintenance window** — a scheduled, low-impact time.
7. **Documentation and review** — update diagrams, the CMDB, and procedures so
   the records stay truthful.

> The **back-out plan** is the answer whenever the concern is "how do we undo this
> if it fails?" The **maintenance window** is "when do we do it with the least
> disruption?" These two show up constantly on the exam.

A table to keep the roles straight:

| Term | What it is |
|------|-----------|
| **RFC / change request** | The formal document that initiates a change |
| **CAB** | The board that reviews and approves changes |
| **Impact analysis** | Assessment of what a change could affect |
| **Back-out plan** | Documented procedure to revert a failed change |
| **Maintenance window** | Scheduled time to apply changes with least impact |
| **Emergency change** | An expedited process for urgent fixes, reviewed after the fact |

Change management is a **managerial/operational** control, not a technical one —
it governs *how* changes happen rather than enforcing them in software. A related
discipline, **patch management**, is really change management applied to updates:
test the patch, schedule it, deploy it, and keep a way to roll it back.

## Why these processes are security controls

It's tempting to file asset and change management under "IT operations" and move
on. Resist that. An untracked asset can't be patched. A system that has drifted
from its baseline has unknown weaknesses. An unreviewed change can silently
disable logging or open a firewall. Each of these processes directly reduces risk,
which is exactly what a security control does — they are the quiet backbone that
every flashier control stands on.

## Exam focus

- **Asset inventory** is foundational: you can't protect, patch, or monitor what
  you don't know you have. Every asset has an **owner**; secure **disposal** is
  part of the lifecycle; **shadow IT** is risky because it's uninventoried.
- The **CMDB** records **configuration items (CIs)** and their relationships. A
  **baseline** is the approved known-good config; **configuration drift** is
  unapproved divergence from it.
- Change management flow: **RFC -> impact analysis -> CAB approval -> test ->
  back-out plan -> maintenance window -> document.**
- The **back-out/rollback plan** answers "how do we undo it"; the **maintenance
  window** answers "when do we do it with least impact." A back-out plan must
  exist **before** the change.
- Change and patch management are **administrative/operational** controls that
  govern how changes happen.
