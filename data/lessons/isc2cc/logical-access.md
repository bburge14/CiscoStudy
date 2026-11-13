# Logical Access Controls

Physical controls guard doors; **logical (technical) access controls** guard the
data and systems themselves, enforced by software. A username-and-password login
on a workstation is a logical control, not a physical one. This lesson covers the
access-control **models** that decide who may do what on a system, plus the
structures (ACLs, matrices) and conveniences (SSO) that implement them.

## Logical vs. physical — a quick reminder

> A **logical (technical) access control** is enforced by hardware or software —
> a login, a file permission, an access control list. A **physical** control is
> something tangible like a lock or a guard.

If the safeguard lives in the operating system or an application, it's logical.
Keep that split in mind; the exam sometimes just asks you to classify one.

## The four main access control models

How a system decides access falls into a handful of well-known models. These are
heavily tested, so learn the one-line essence and the giveaway clue of each.

### Discretionary Access Control (DAC)

> In **DAC**, each object's **owner** personally decides who may access it.

On a typical file server, the person who creates a file sets its permissions —
choosing which other users may read or edit it. DAC is flexible and common, but
its weakness is exactly that flexibility: access depends on each owner's
judgment, so a careless owner — or malware running with the owner's rights — can
grant access far too broadly. The clue word is **owner decides**.

### Mandatory Access Control (MAC)

> In **MAC**, the **system** enforces access using labels and clearances; users
> cannot change the rules.

Every object carries a sensitivity **label** (e.g., Confidential, Secret) and
every subject a **clearance**. The operating system — not any user — decides
access by comparing them. MAC is the most rigid model and is used in
classified/government and other high-security environments. The clue is
**labels + clearances, system-enforced, users can't override**.

### Role-Based Access Control (RBAC)

> In **RBAC**, permissions are attached to **roles** (job functions), and users
> get access by being assigned to a role.

Hire someone as an "Accountant" and the system automatically grants them the
permissions tied to that role. When they change jobs, you change their role and
their access updates consistently. RBAC shines in large organizations with
constant staff changes because it makes administration simple and keeps access
aligned to the job. The clue is **access follows the job role**.

### Attribute-Based Access Control (ABAC)

> In **ABAC**, access is decided by evaluating multiple **attributes** together.

An ABAC system weighs attributes of the user (department, clearance), the
resource (classification), the action, and the environment (device security
posture, time of day, location) to reach a decision. It's the most granular and
context-aware model. The clue is **many attributes evaluated together**.

### Rule-Based Access Control

Don't confuse this with role-based. **Rule-based** access control applies
system-wide **rules** uniformly to everyone — for example, "no one may log in
between midnight and 5 a.m.," or firewall rules that filter traffic the same way
for all users. The clue is **blanket rules applied to all**, regardless of
individual identity or role.

### Model comparison at a glance

| Model | Who decides access | Clue words |
|-------|--------------------|-----------|
| **DAC** | The object's owner | "owner sets permissions" |
| **MAC** | The system, via labels & clearances | "classified, labels, system-enforced" |
| **RBAC** | Based on the user's role/job | "permissions by job role" |
| **ABAC** | Based on multiple attributes | "department + device + time of day" |
| **Rule-based** | System-wide rules for everyone | "no logins after midnight" |

## Structures that implement access control

Models are the policy; these are some of the structures that carry them out.

- **Access control list (ACL)** — a list attached to an **object** specifying
  which users or groups may read, write, or execute it. Think of it as the
  object's guest list. (Firewalls and routers use ACLs too, to permit or deny
  traffic.)
- **Access control matrix** — a table whose rows are **subjects** (users) and
  columns are **objects** (resources), with each cell listing that user's
  permissions on that resource. It's the full picture; an ACL is essentially one
  column of the matrix (the permissions on one object).

## Single sign-on (SSO)

> **Single sign-on (SSO)** lets a user authenticate **once** and then reach
> multiple systems without re-entering credentials.

A user logs in in the morning and then reaches email, the HR portal, and the file
share without logging in again. SSO improves convenience and can strengthen
security (fewer passwords to manage and reuse), but it concentrates risk: if that
one login is compromised, the attacker reaches everything, which is why SSO is
often paired with MFA.

## Exam focus

- A login or file permission is a **logical (technical)** control; a lock or guard
  is **physical**.
- **DAC** = the **owner** decides (weakness: depends on owner judgment; malware
  with owner rights can over-share). **MAC** = **system-enforced labels and
  clearances**, users can't change it (classified environments, most rigid).
- **RBAC** = permissions follow the **role/job** — ideal for big organizations
  with frequent staff changes. **ABAC** = decision from **multiple attributes**
  (user, resource, device, time). **Rule-based** = uniform **rules for everyone**.
- An **ACL** is attached to an object and lists who may read/write/execute it; an
  **access control matrix** is the subjects-by-objects table of all permissions.
- **SSO** = authenticate once, reach many systems; convenient but concentrates
  risk, so pair it with MFA.
