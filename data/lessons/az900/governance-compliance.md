# Governance & Compliance

Governance is how an organization keeps a sprawling Azure estate *consistent,
compliant, and safe from accidents*. Instead of trusting every engineer to do the
right thing by hand, you encode the rules once and let Azure enforce them. This
lesson covers the main governance controls — Azure Policy, role-based access
control, resource locks, tags, and management groups — and the compliance
resources Microsoft provides to prove it is all above board.

## Azure Policy: enforce the rules automatically

> **Azure Policy evaluates your resources against rules you define and enforces
> them — flagging or blocking anything that does not comply.** It keeps resources
> aligned with corporate and regulatory standards.

Each policy has an **effect** that decides what happens to a non-compliant
resource. The one the exam tests most is **Deny**:

> The **Deny** effect **stops a non-compliant resource from being created or
> updated at deployment time.** If a policy says "only these VM sizes are allowed,"
> Deny blocks anyone from deploying a disallowed size in the first place.

Other effects include **Audit** (allow it but record it as non-compliant) and
**Append/Modify** (add or change properties, such as a required tag). Related
pieces:

- **Initiatives** group many policies together so you can assign a whole standard
  (for example, a regulatory baseline) in one step.
- Policy assignments can be made at any scope — and assigning at a **management
  group** applies the rule to **every subscription beneath it at once** (more on
  that below).

## Role-based access control (RBAC): who can do what

> **Azure RBAC grants permissions by assigning roles to users, groups, or
> applications at a particular scope** (management group, subscription, resource
> group, or resource). It implements least privilege — people get only the access
> their job needs.

Where **Azure Policy** governs *what resources may exist and how they are
configured*, **RBAC** governs *who is allowed to perform which actions*. They are
complementary: policy controls the resources, RBAC controls the people.

## Resource locks: prevent costly accidents

> **A resource lock protects a resource from accidental change or deletion, even by
> someone who otherwise has permission.** There are two kinds:
> - **CanNotDelete** — you can read and modify the resource, but **not delete** it.
> - **ReadOnly** — you can **view** the resource but **not modify or delete** it.

Two points the exam presses on:

- Locks **inherit downward**. A lock applied at the **resource group** scope
  protects **all the resources inside that group**, not just the group object.
- A **ReadOnly** lock is the answer when a finished resource "must not be modified
  or deleted by anyone, though it can still be viewed." A **CanNotDelete** lock is
  the answer when the only concern is preventing deletion.

Locks are deliberately separate from RBAC: even an owner is stopped by a lock until
the lock is removed, which is exactly why they guard against human error.

## Tags: organize and track at scale

> **Tags are name/value pairs you attach to resources** (for example,
> `Environment = Production` or `CostCenter = Finance`) to organize them, report on
> cost, and drive automation.

Tags don't enforce anything by themselves, but combined with Azure Policy you can
*require* specific tags, and combined with Cost Management you can break down
spending by department or project.

## Management groups: govern many subscriptions at once

Most of the controls above are far more powerful when applied broadly.

> **A management group is a container above subscriptions.** Assign a policy, an
> RBAC role, or a standard to a management group and it applies to **every
> subscription under it simultaneously.**

So when a governance team must apply the **same tagging policy consistently across
twenty subscriptions at once**, the right place to assign it is the **management
group** that contains them — not each subscription one by one.

### The governance controls at a glance

| Control | What it governs |
|---------|-----------------|
| **Azure Policy** | What resources may exist and how they're configured (Deny blocks them) |
| **RBAC** | Who may perform which actions, by role and scope |
| **Resource locks** | Protection from accidental change/delete (CanNotDelete, ReadOnly) |
| **Tags** | Organization, cost reporting, and automation metadata |
| **Management groups** | Applying the above across many subscriptions at once |

## Compliance: proving you meet the standards

Governance controls keep *your* house in order; compliance resources let you show
that **Azure itself** meets external standards, and help you track your own.

> **The Service Trust Portal is where you obtain Microsoft's independent audit
> reports and compliance certifications for Azure — such as SOC 1/2/3 and ISO
> standards.** When an auditor asks for proof that Azure meets a certification,
> this is the source.

Two more compliance tools to recognize:

- **Microsoft Purview** — a data governance and compliance family that helps you
  discover, classify, and protect data across your estate.
- **Compliance Manager** (in the Service Trust Portal / Purview) — helps you assess
  and track your own compliance against regulations with a scored dashboard.

## A note on Azure Blueprints (being retired)

You may still see **Azure Blueprints** mentioned. It bundled governance artifacts —
ARM templates, policy assignments, and role assignments — into repeatable
environment definitions. **Microsoft is retiring Azure Blueprints (retirement is
set for early 2027),** and splits its job across two replacements:

- **Template Specs** (or a Git repository) take over **storing and versioning** the
  deployment artifacts.
- **Azure Deployment Stacks** take over **deploying, managing the lifecycle of, and
  locking** a group of resources (including deny-style protection).

In practice the two are used together. If a question notes that Blueprints packaged
governance artifacts but is being retired, the forward-looking answer is **Template
Specs plus deployment stacks**.

## Pulling it together

Govern *configuration* with **Azure Policy** (Deny blocks bad deployments),
*access* with **RBAC**, and guard against *accidents* with **resource locks**
(CanNotDelete, ReadOnly) that inherit to everything in scope. Organize and report
with **tags**, and apply all of it at scale from a **management group**. Prove
compliance through the **Service Trust Portal** (audit reports and
certifications), with **Purview** and **Compliance Manager** for your own posture —
and remember that **Blueprints** is giving way to **Template Specs + deployment
stacks**.

## Exam focus

- **Azure Policy** enforces configuration rules; the **Deny** effect **blocks a
  disallowed resource at deployment** (e.g., a forbidden VM size). **RBAC** controls
  **who** can do what by assigning **roles** at a scope.
- **Resource locks**: **CanNotDelete** (modify but not delete) and **ReadOnly**
  (view only). A lock at a **resource group** scope protects **all resources in the
  group** — locks inherit downward.
- **Tags** = name/value pairs for organization, cost reporting, and automation.
- **Management group** = apply a policy/role to **many subscriptions at once**; the
  right scope for enforcing one standard across twenty subscriptions.
- **Service Trust Portal** = get Microsoft's **audit reports and certifications**
  (SOC, ISO). **Microsoft Purview** / **Compliance Manager** = assess your own
  compliance.
- **Azure Blueprints** is **being retired** → **Template Specs** (store/version) +
  **Azure Deployment Stacks** (deploy, manage lifecycle, lock).
