# Access Control Models: DAC, MAC, RBAC & ABAC

Once a user is authenticated, the system must decide *what they are allowed to
do*. That decision is governed by an **access control model** — the rulebook for
granting and denying access to objects. The exam gives you a scenario and asks
which model is in play, so this lesson is really about pattern recognition: learn
the tell for each model and the matching becomes automatic.

## Subjects, objects, and the vocabulary

> A **subject** is an active entity that requests access — a user, process, or
> device. An **object** is the passive resource being accessed — a file,
> database record, or printer. Access control decides which subjects may perform
> which actions on which objects.

Two principles run through every model:

- **Least privilege** — grant only the access a subject needs to do its job, and
  no more.
- **Need-to-know** — grant access to specific data only when the subject requires
  it for a task, even within their clearance level.

These are the principles; the models below are the mechanisms that enforce them.

## The four core models

### Discretionary Access Control (DAC)

> In **DAC**, the **owner** of an object decides who may access it, at their own
> discretion, typically via an **access control list (ACL)**.

The giveaway is **owner control**: "the owner of each file personally decides who
may read or modify it." Standard file permissions on Windows and Linux are DAC.
It's flexible but weak — a careless or compromised owner can over-share, and
there's no central enforcement of a security policy.

### Mandatory Access Control (MAC)

> In **MAC**, access is enforced by the **system** based on **security labels**
> (classifications like Secret, Top Secret) and matching **clearances**. Users
> cannot change the labels or override the rules.

The giveaway is **labels and clearances enforced by the system**, not the owner.
MAC is used in government, military, and high-security systems. It is rigid and
secure precisely because no individual can loosen it. MAC is built on a
**lattice** of classification levels (see Bell-LaPadula below).

### Role-Based Access Control (RBAC)

> In **RBAC**, permissions are assigned to **roles** (job functions), and users
> inherit permissions by being placed in a role.

The giveaway is **by job function/group**: "every account in the Nurse group
automatically gets the same predefined rights." RBAC scales beautifully in large
organizations — you manage a handful of roles instead of thousands of individual
grants — and it maps cleanly to least privilege. Don't confuse **role**-based with
**rule**-based.

### Attribute-Based Access Control (ABAC)

> In **ABAC**, access decisions are made dynamically by evaluating **attributes**
> of the subject, object, action, and environment against a policy (e.g., "allow
> if department = Finance AND time is business hours AND device is managed").

The giveaway is **multiple conditions/attributes combined in a policy**. ABAC is
the most granular and flexible model, powering modern cloud and zero-trust
systems, but it's also the most complex to design and audit.

A fifth you should recognize: **Rule-Based Access Control** applies global
**rules** (if-then conditions) regardless of identity — a firewall ACL that blocks
a port for everyone is rule-based.

| Model | Decision made by | Tell-tale phrase |
|-------|------------------|------------------|
| **DAC** | The object's **owner** | "owner decides," "ACL on the file" |
| **MAC** | The **system**, via labels | "clearance," "Secret/Top Secret," "labels" |
| **RBAC** | Role / group membership | "by job function," "the Nurse group" |
| **ABAC** | Policy over attributes | "if department AND time AND device..." |
| **Rule-based** | Global if-then rules | "block this for everyone" |

## Formal models: Bell-LaPadula vs Biba

Two lattice-based models underpin MAC and are perennial exam favorites because
they are easy to mix up. One protects **confidentiality**, the other protects
**integrity** — and their rules are mirror images.

> **Bell-LaPadula (confidentiality):** **Simple Security Property = "no read up"**
> (you can't read data above your clearance). **\* (Star) Property = "no write
> down"** (you can't write to a lower level and leak secrets). Slogan: **read
> down, write up.**

> **Biba (integrity):** **Simple Integrity Property = "no read down"** (don't
> ingest lower-integrity data). **\* (Star) Integrity Property = "no write up"**
> (you can't raise the integrity of data by writing above your level). Slogan:
> **read up, write down.**

Memory anchor: **Bell-LaPadula = Confidentiality** (both start with a hard "C"
concept — it stops secrets flowing *down* to the unauthorized), and its headline
rule is **no write down**. **Biba = Integrity**, and its headline rule is **no
write up** — a low-integrity subject can't corrupt high-integrity data. If a
question says "no write up," it's **Biba/integrity**; "no write down," it's
**Bell-LaPadula/confidentiality**. A third model, **Clark-Wilson**, also addresses
integrity through well-formed transactions and separation of duties.

## Exam focus

- **DAC** = **owner** decides (ACLs); flexible but weak. **MAC** = **system**
  enforces via **labels/clearances**; rigid and high-security. **RBAC** = by
  **role/job function**; scales for large orgs. **ABAC** = dynamic decisions over
  **attributes**; most granular, used in cloud/zero trust.
- Watch **role-based vs rule-based**: roles map to people's jobs; rules are global
  if-then conditions applied to everyone.
- **Least privilege** (only what's needed) and **need-to-know** (only the specific
  data required) are the guiding principles behind the models.
- **Bell-LaPadula = confidentiality**: **no read up, no write down.**
- **Biba = integrity**: **no read down, no write up.** If you see "**no write
  up**," think **Biba/integrity**; "**no write down**," think **Bell-LaPadula/
  confidentiality**.
