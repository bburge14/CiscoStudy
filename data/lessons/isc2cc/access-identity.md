# Access Control Foundations & Identity Management

Access control is the heart of security: deciding *who* can do *what* to *which*
resources. Before we get into specific models, you need the foundational
vocabulary and principles, plus the identity machinery — authentication,
factors, and the AAA framework — that makes access control possible. This lesson
builds that base.

## The core elements: subject, object, access

Every access-control scenario has the same cast:

> A **subject** is the active entity requesting access (a user or a program
> acting on their behalf). An **object** is the passive resource being accessed
> (a file, a database, a printer). **Access** is what the subject is allowed to
> do to the object.

When a user runs a program that opens a document, the **user** is the subject
(acting through the program) and the **document file** is the object. Keep it
straight: the subject *acts*, the object is *acted upon*.

## Identification, authentication, authorization, accounting

Access control runs through four steps, often called **IAAA**:

1. **Identification** — the subject claims an identity (typing a username).
2. **Authentication** — the subject *proves* the claimed identity (entering a
   password). This is the step of proving you are who you say you are.
3. **Authorization** — once authenticated, the system determines *what* the
   subject is allowed to access and do.
4. **Accounting** (auditing) — the system records and logs what the authenticated
   subject actually does, creating an audit trail.

The last three are the **AAA framework: Authentication, Authorization, and
Accounting.** Don't confuse authentication (proving identity) with authorization
(deciding permissions) — a user authenticates *first*, then is authorized.

## The authentication factors

How do you *prove* an identity? With one or more **factors**, grouped into three
categories:

| Factor category | Means | Examples |
|-----------------|-------|----------|
| **Something you know** | Knowledge | Password, PIN, security question |
| **Something you have** | Possession | Hardware token, smart card, phone authenticator app |
| **Something you are** | Inherence (biometric) | Fingerprint, facial scan, iris |

> **Multifactor authentication (MFA)** requires two or more factors from
> **different categories**. Two passwords is *not* MFA — both are "something you
> know."

Classic MFA examples:

- Password **+** one-time code from an authenticator app = *know* + *have*.
- Bank card **+** PIN at an ATM = *have* + *know*.
- Password **+** fingerprint = *know* + *are*.

MFA is powerful because an attacker who steals your password still can't log in
without also stealing your second factor.

## Accountability and the account lifecycle

> **Accountability** means every action can be traced to a specific individual.
> That requires each user to have a **unique account** — never a shared login.

Shared accounts destroy accountability: if "admin" did something bad, you can't
prove *who*. Unique accounts, combined with accounting/logging, let you tie each
action to a person.

Accounts have a lifecycle you should know:

- **Provisioning** — when someone joins, you create their accounts and grant the
  access appropriate to their role.
- **Deprovisioning** — when someone is terminated, their accounts and access must
  be **disabled/revoked immediately**. A former employee with a live account is a
  serious risk — don't wait.

## The guiding principles of access control

These principles come up again and again across the whole certification.

### Least privilege

> **Least privilege** means giving each subject only the access rights needed to
> do their job — nothing more.

If an accountant only needs the accounting system, that's all they get. Least
privilege shrinks the damage any one account can do if it's compromised.

### Need to know

**Need to know** is a close cousin: even someone with the right clearance level
gets access only to the *specific* information required for their task. An analyst
with a Secret clearance still sees only the Secret files for *her* project, not
every Secret file in the building. Least privilege is about *permissions*; need to
know is about *information*.

### Separation (segregation) of duties

> **Separation of duties** splits a sensitive task so that no single person can
> complete it alone, reducing fraud and error.

One employee submits a payment request; a *different* one approves it. One
engineer writes code; a different, authorized person reviews and approves it
before deployment. No one person controls the whole risky process.

### Defense in depth

**Defense in depth** (layered security) uses several independent layers of
controls — a firewall, then network segmentation, then host hardening — so that
if one layer fails, others still protect the asset. Never rely on a single
safeguard.

### Implicit (default) deny

**Implicit deny** means anything not *explicitly* permitted is automatically
blocked. A firewall that allows only the traffic its rules name, and drops
everything else, follows implicit deny. It's a secure default posture: start
closed, open only what's needed.

### Guarding against privilege creep

> **Privilege creep** (permission creep) is the slow accumulation of access
> rights as a person changes roles, where old permissions are never removed.

After years and three department moves, an employee can end up with far more
access than their current job needs — a least-privilege violation waiting to be
abused. Regular **access reviews** catch and remove it. Related fraud-detection
practices include **job rotation** (moving staff through different duties) and
**mandatory vacation** (requiring time off), both of which make hidden misconduct
more likely to surface while someone else is doing the job.

## Exam focus

- **Subject** = active entity (user/program) requesting access; **object** =
  passive resource being accessed.
- **IAAA**: identify → **authenticate** (prove identity) → **authorize** (decide
  permissions) → **account** (log actions). The AAA framework's third "A" is
  **accounting**.
- Three factors: **something you know / have / are.** **MFA** needs two or more
  from *different* categories — two of the same type doesn't count.
- **Least privilege** = only what the job needs. **Need to know** = only the
  specific info required. **Separation of duties** = no single person completes a
  sensitive task.
- **Defense in depth** = multiple independent layers. **Implicit (default) deny**
  = block anything not explicitly allowed.
- **Privilege creep** = unremoved permissions piling up; fight it with access
  reviews, job rotation, and mandatory vacation.
- **Deprovision** (disable/revoke) a terminated user's access **immediately**;
  give every user a **unique account** for accountability.
