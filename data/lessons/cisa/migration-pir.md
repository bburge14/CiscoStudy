# System Migration & Post-Implementation Review

The last stretch of a project is deceptively dangerous. Moving data from an old
system to a new one, and switching users over, is where integrity can quietly be
lost and where a rushed cutover can take down the business. And once the system
is live, someone has to ask the honest question: *did it actually deliver what we
promised?* This lesson covers migration and conversion controls and the
post-implementation review.

## Data conversion: move it completely and accurately

When data moves from a legacy system to a new one, the auditor's chief worry is
**integrity** — that every record arrives, unchanged and correctly mapped.

> The control that **best** proves a conversion was **complete and accurate** is
> **reconciling record counts and control totals between the source and target
> systems**. If the old system held 1,000,000 customer records summing to a known
> control total, the new system must show the same count and the same totals.

Supporting conversion controls include:

- **Validation and edit checks** on the imported data to catch malformed or
  out-of-range values.
- **Reconciliation of key totals** (balances, hash totals of important fields),
  not just row counts.
- **Exception handling** — records that fail conversion go to a **suspense/error
  log** for correction and re-processing, never silently dropped.
- **Reviewing and cleansing data before conversion**, since migrating bad data
  just moves the problem.

The principle: you prove completeness and accuracy by **comparing old against new
with independent totals**, not by assuming the migration tool worked.

## Changeover: how to switch over

Once data is ready, the organization must move users from the old system to the
new. The method chosen is a direct trade-off between **risk** and **cost**.

> - **Parallel** changeover runs the **old and new systems simultaneously** and
>   compares their output before retiring the old one. It gives the **greatest
>   assurance** and a built-in fallback — but it is the **most expensive** and
>   labor-intensive.
> - **Direct (big-bang)** changeover **switches entirely to the new system on a
>   single date with no fallback**. It is the **cheapest and fastest** but carries
>   the **highest risk**, because if the new system fails there is nothing to fall
>   back to.

| Approach | How it works | Risk |
|----------|--------------|------|
| **Parallel** | Run old + new together, compare, then cut over | Lowest (fallback exists) — but costly |
| **Phased** | Migrate in stages (module by module or group by group) | Moderate |
| **Pilot** | Roll out to one site/group first, then the rest | Moderate (limited blast radius) |
| **Direct / big-bang** | One-shot switch, no parallel run | **Highest** (no fallback) |

When a question describes running both systems and comparing results, the answer
is **parallel**; when it describes a single cutover with no fallback, the answer
is **direct/big-bang = highest risk**.

### Deciding to go live

The actual cutover should not happen on momentum. A formal **go/no-go decision**
confirms the organization is genuinely ready, and the auditor checks that real
criteria — not optimism — drove it:

- **Testing is complete**, including **user acceptance testing** sign-off from the
  business.
- **Data conversion was validated** (counts and control totals reconciled).
- A **fallback/rollback plan** exists in case the new system fails on day one.
- **Users are trained** and **support is ready** to handle the first-day surge.

> The safest cutovers keep a **way back**. Choosing a direct/big-bang approach is
> legitimate, but it means consciously **accepting the risk of no fallback** —
> that should be an informed management decision, not an accident of a missed
> deadline.

## Post-implementation review

After the dust settles, the project isn't truly finished until someone checks
whether it worked. That check is the **post-implementation review (PIR)**.

> The primary objective of a **PIR** is to determine whether the system **met its
> objectives and delivered the expected benefits** (the benefits in the original
> business case) and to **capture lessons learned** for future projects.

Two details are heavily tested — *when* and *by whom*:

> - **Timing:** a PIR is conducted **after the system has been in production long
>   enough to stabilize**, so real performance and benefits can actually be
>   measured. Review it too early and there is nothing meaningful to assess.
> - **Objectivity:** the PIR is best conducted by an **independent party not
>   involved in the system's development**. People who built the system can't
>   objectively judge whether it succeeded.

A thorough PIR looks at whether the promised benefits materialized, whether the
project stayed within cost and schedule, how well the system performs in real
use, and what should be done differently next time. Notice the recurring theme:
**independence drives objectivity**. Just as an auditor shouldn't audit their own
work, the developers shouldn't be the ones certifying that their own project was a
success.

## The auditor's view of the cutover

Migration and cutover concentrate risk into a short window, so the auditor checks
that the organization didn't trade away its safety net for speed. That means
confirming reconciliation controls proved the data moved intact, that a realistic
fallback existed for the changeover (or that leadership consciously accepted the
risk of not having one), and that an independent PIR honestly assessed the
result. A project that "went live on time" but corrupted data or can't show it met
its objectives is not a success the auditor will sign off on.

## Exam focus

- Prove a data conversion is **complete and accurate** by **reconciling record
  counts and control totals** between source and target; send failures to a
  **suspense/error log** for follow-up.
- **Parallel** changeover (run old + new, compare) gives the **greatest assurance**
  but is **costliest**; **direct/big-bang** (one-shot, no fallback) is the
  **highest risk**. **Phased** and **pilot** sit in between.
- A **PIR** determines whether the system **met its objectives and delivered the
  expected benefits**, plus **lessons learned**.
- Conduct the PIR **after the system has stabilized in production**, and have it
  performed by someone **independent of the development** for objectivity.
