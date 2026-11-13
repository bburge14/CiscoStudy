# Organizational Structure, Roles & Segregation of Duties

How an organization divides up responsibility is itself a control. When the right
jobs are kept in different hands, no single person can commit and conceal an
error or fraud. When roles blur, the auditor's antennae should go up. This lesson
covers the key IT roles, the principle of **segregation of duties (SoD)**, and
what to do when perfect separation isn't possible.

## Knowing who is responsible for what

Clear roles prevent gaps ("everyone thought someone else was doing it") and
overlaps (too much power in one place). CISA expects you to distinguish a few
data-related roles precisely.

> - The **data owner** — usually a business manager — **classifies** the data and
>   **authorizes** who may access it. Ownership is a business accountability, not
>   an IT one.
> - The **data custodian** — often IT — **safeguards and maintains** the data
>   (backups, storage, applying the owner's access decisions). The custodian
>   protects; it does not decide classification.
> - The **user** operates within the access rights they have been granted and is
>   expected to follow policy.

Other roles the exam references include the **security officer** (defines and
monitors the security program), the **database administrator** (manages the
database and holds powerful privileges), and **senior management** (sets tone and
approves policy). The recurring trap is mixing up **owner** (decides) and
**custodian** (protects): if a question asks who classifies data or approves
access, it is the **owner**.

## Segregation of duties

> **Segregation of duties** means dividing a sensitive process so that **no
> single individual controls it end to end**. The classic incompatible functions
> are **authorization**, **custody** of assets, **recording** (bookkeeping), and
> **reconciliation/verification**. Keeping these apart means fraud or error
> generally requires **collusion** to succeed and to stay hidden.

The most tested IT example is unmistakable:

> A person who **develops** application code **and** has **update access to the
> production environment** is a classic SoD violation. The same hands that write
> code could push unauthorized or malicious changes straight to live systems with
> nobody to catch it.

Developers work in development and test; a separate function promotes approved
code to production. Other incompatible pairings to watch for:

- A programmer who can also authorize and release their own changes.
- A person who both initiates payments and reconciles the bank statement.
- A user who can grant their own access rights (self-approval).
- An operator who can modify the very logs that would record their actions.

The auditor's job is to look for these combinations in access rights and workflow
— the finding is the *combination*, even if each individual permission looks
reasonable on its own.

### Separating the IT functions

Beyond individual duties, whole IT **functions** are kept apart so one group can't
both make and conceal changes:

- **Development** is separated from **operations** — those who write code don't run
  production, and those who run production don't alter code.
- **Security administration** (setting access rights) is separated from the **data
  owners** who authorize access and from the users who hold it.
- **Information security** is ideally independent of the IT functions it oversees,
  so it isn't reviewing its own work — governance's version of auditor
  independence.

The auditor also watches for the opposite problem: over-concentration in one
person creates a **single point of failure**. Cross-training and documented
procedures reduce the risk that a key person's absence halts operations — while
job rotation and mandatory vacations (below) keep that cross-training honest.

## When segregation isn't practical: compensating controls

In a small IT department, there simply aren't enough people to separate every
duty. SoD is an ideal, not always an achievable one — so the organization
substitutes **compensating controls**.

> When full segregation of duties is impractical, the **best compensating
> controls** are **increased management supervision** and **independent review of
> activity logs** — someone outside the role regularly checks what was done.

A toolbox of compensating controls:

- **Supervisory review** — a manager reviews and approves sensitive actions.
- **Independent log review** — someone not performing the activity examines the
  audit trail for anything unusual. (This is also how you control powerful
  accounts like the DBA: **log their activity and have it reviewed independently**.)
- **Job rotation** — moving people between duties so a scheme can't run quietly
  for years, and so irregularities surface when a new person takes over.
- **Mandatory vacations** — requiring staff to be away long enough that someone
  else must cover their work, exposing anything hidden.
- **Dual control** — requiring two people to complete a single sensitive action
  (think two keys for one safe).

The through-line: if you cannot *prevent* one person from controlling a process,
you *detect* misuse through independent oversight and make concealment harder.
Prevention is better, but a well-run detective-and-oversight layer is a
legitimate answer when prevention isn't feasible.

## The auditor's lens

Organizational structure matters to the auditor because it determines whether
controls can even work. A beautiful control procedure means little if one person
can perform, record, and review their own work. So the auditor maps who can do
what, looks for toxic combinations of access, and — where separation is
impossible — checks that real compensating controls (supervision, independent
review, rotation, mandatory vacations) are genuinely operating, not just written
on paper.

## Exam focus

- **Data owner classifies data and authorizes access** (a business role); **data
  custodian safeguards/maintains** it (often IT); **users** operate within
  granted rights. Owner *decides*, custodian *protects*.
- **Segregation of duties** keeps **authorization, custody, recording, and
  reconciliation** in different hands so misuse needs **collusion**.
- **Developer + update access to production** is the textbook **SoD violation**;
  watch for anyone who can both perform and approve/record their own actions.
- When SoD is **impractical**, compensate with **management supervision and
  independent log review**; also **job rotation**, **mandatory vacations**, and
  **dual control**.
- Powerful privileged accounts (e.g., **DBA**) are controlled by **logging their
  activity and reviewing it independently**.
