# System Interfaces & Database Management

Data rarely lives in one place. It flows between applications through
**interfaces**, and it rests in **databases**. Both are places where
*integrity* — the accuracy and completeness of data — can be silently
compromised. This lesson covers the controls that keep data correct as it moves
between systems and as it is stored, updated, and accessed.

## System interfaces: moving data between applications

When two applications exchange transactions automatically — an ordering system
feeding billing, say — the connection between them is an **interface**. The
auditor's central concern is simple to state.

> The primary risk of an automated interface is that data is transferred
> **incompletely or inaccurately**, compromising **integrity**. Transactions
> could be dropped, duplicated, or corrupted in transit without anyone noticing.

The control that best addresses this risk is reconciliation:

> To confirm that **all** transactions sent by the source were received and
> processed by the target — completely and accurately — **reconcile transaction
> counts and control totals** between the two systems. If the source sent 5,000
> records totaling a known amount, the target must show the same.

Interfaces also need disciplined handling of records that fail validation:

> Transactions that **fail an interface's edit/validation checks** should be
> **written to a suspense (error) file** and **followed up for correction and
> reprocessing** — never silently **deleted** and never **forced through** without
> correction.

Supporting interface controls include **sequence checks** (to catch missing or
duplicate records), **hash totals** on key fields, **acknowledgment/confirmation**
messages between systems, and **automated alerts** when reconciliations don't
balance. The theme is constant: prove the data arrived whole, and give failed
items a safe place to wait for correction.

Interfaces come in different shapes, and the shape affects the controls. **Batch**
interfaces move data in scheduled bulk transfers (reconciliation and sequence
checks fit naturally). **Real-time** interfaces (often via **APIs** or
**middleware/EAI** platforms) pass transactions continuously, so controls lean on
per-message acknowledgments, timeouts, and retry logic. Whichever the style, the
auditor's question is the same: can the organization prove every transaction was
transferred **once, completely, and accurately**?

## Database fundamentals

A **database management system (DBMS)** stores and controls access to shared data.
Most enterprise data lives in **relational** databases — tables of rows and
columns, linked by keys. A few concepts carry the integrity load.

> **Normalization** organizes a relational database to **reduce data redundancy**
> and the update **anomalies** that redundancy causes. Less duplicated data means
> fewer chances for copies to disagree — so normalization **improves data
> integrity**.

> **Referential integrity** ensures that a **foreign key** value in one table
> always corresponds to an **existing primary key** in the related table — so you
> can't have an "orphan" record (an order pointing to a customer who doesn't
> exist).

Two more properties the exam expects you to recognize:

- **ACID** — the guarantees that keep transactions reliable: **Atomicity** (all or
  nothing), **Consistency** (valid state to valid state), **Isolation**
  (concurrent transactions don't corrupt each other), and **Durability**
  (committed data survives failure).
- **Concurrency controls** (such as **locking**) prevent two simultaneous
  transactions from interfering — for example, both updating the same balance and
  one overwriting the other.

**Database views** are a useful access control: a view exposes only certain rows
or columns, so a user can be given exactly the slice of data they need and nothing
more — an application of least privilege at the data layer.

## Controlling the database administrator

The person who runs the database holds extraordinary power, and that power is a
control problem.

> A **database administrator (DBA)** holds powerful, privileged access that can
> **bypass application controls** — reading or changing data directly. Because you
> often cannot fully *prevent* this, the **best control is to log DBA activities
> and have those logs independently reviewed** by someone outside the DBA
> function.

This is the same compensating-control logic you saw with segregation of duties:
when a role is too powerful to split, you **detect** misuse through independent
oversight of a protected audit trail. The auditor checks that DBA actions are
logged, that the DBA cannot alter their own logs, and that someone independent
actually reviews them — not just that the logging feature is switched on.

Other database controls the auditor looks for include **access controls and
granular permissions** on tables and views, **encryption** of sensitive data at
rest, regular **backups** with tested restores, and **change control** over
database schema and configuration.

## Why this pairs together

Interfaces and databases share one worry above all: **integrity**. An interface
can lose or mangle data on the way in; a database can let it drift through
redundancy, orphaned keys, concurrent-update clashes, or an unmonitored
super-user. The controls rhyme, too — reconciliations and totals prove
completeness, validation and referential integrity keep data well-formed, and
independent log review watches the one account powerful enough to bypass
everything else.

## Exam focus

- The main interface risk is **incomplete/inaccurate transfer** (integrity);
  **reconcile transaction counts and control totals** to prove data moved whole.
- Transactions failing validation go to a **suspense/error file** for correction
  and reprocessing — **never deleted or forced through**.
- **Normalization** reduces redundancy and anomalies (improving integrity);
  **referential integrity** means every **foreign key points to a valid primary
  key** (no orphans).
- Know **ACID** (atomicity, consistency, isolation, durability) and that
  **concurrency/locking** prevents simultaneous updates from corrupting data.
- The **DBA**'s privileged access can bypass application controls, so **log DBA
  activity and review it independently** — the DBA must not control their own
  logs.
