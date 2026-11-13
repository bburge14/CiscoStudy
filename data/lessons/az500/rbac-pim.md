# Azure RBAC, Entra Roles & Privileged Identity Management

Authentication proved who the user is. **Authorization** decides what they may
do, and in Azure that means two separate permission systems plus a tool for
handing out privilege only when it's actually needed. Confusing the two systems is
the single most common AZ-500 mistake, so we draw the line sharply.

## Two different role systems

> **Azure roles (Azure RBAC)** control access to **Azure resources** — VMs,
> storage accounts, virtual networks — through Azure Resource Manager.
> **Microsoft Entra roles** control access to **directory objects** — users,
> groups, app registrations — inside Entra ID.

They are managed in different places and do not grant each other's permissions.

| | **Azure RBAC roles** | **Entra roles** |
|---|---|---|
| Governs | Azure resources | Identity/directory objects |
| Example role | Contributor, Storage Blob Data Reader | Global Administrator, User Administrator |
| Scope levels | Management group → subscription → resource group → resource | Tenant, administrative unit, or single object |
| Managed in | Subscription / resource **Access control (IAM)** | Entra admin center → Roles |

A crucial consequence: by default a **Global Administrator does not have access to
Azure resources**, and an Azure **Owner** does not administer the directory.
(A Global Admin *can* elevate access to manage all subscriptions, but that is a
deliberate, auditable exception, not the normal state.)

## How Azure RBAC works

RBAC answers "who can do what, where" with three pieces:

1. **Security principal** — *who*: a user, group, service principal, or managed
   identity.
2. **Role definition** — *what*: a named collection of permissions.
3. **Scope** — *where*: the level at which the role applies.

A **role assignment** binds those three together.

### Scope and inheritance

Scope is hierarchical, and assignments **inherit downward**:

```
Management group  →  Subscription  →  Resource group  →  Resource
```

Grant Reader at a subscription and the principal can read every resource group and
resource beneath it. This makes scope your primary least-privilege lever: assign
at the **narrowest** scope that does the job.

### Built-in roles you must know

- **Owner** — full access *including* the right to grant access to others.
- **Contributor** — full access to manage resources, but **cannot** grant access
  to others (can't change role assignments).
- **Reader** — view only.
- **User Access Administrator** — manage *access* (role assignments) but not the
  resources themselves.

There are also hundreds of narrow roles (e.g. **Storage Blob Data Contributor**,
**Virtual Machine Contributor**) — prefer these over broad Contributor/Owner.

### Custom roles and how permissions combine

When no built-in role fits, define a **custom role**. A role definition lists:

- **Actions / NotActions** — management-plane operations allowed / subtracted.
- **DataActions / NotDataActions** — data-plane operations (e.g. reading blob
  contents, not just the storage account's properties).

Multiple assignments are **additive** — the user gets the union of all their
roles. The exception is a **deny assignment**, which explicitly blocks actions
and **wins over any allow** (deny assignments are created by Azure itself, for
example by Blueprints or managed apps, not by hand).

## Privileged Identity Management (PIM)

Standing administrative access is a liability: an always-on Global Admin or
subscription Owner is a permanent target. **Privileged Identity Management (PIM)**
replaces standing access with **just-in-time, time-bound** privilege.

> With PIM, an admin is made **eligible** for a role rather than permanently
> **active**. When they need it, they **activate** the role for a limited window,
> and the activation can require **MFA, a justification, and approval**.

Key PIM concepts:

- **Eligible vs active** — eligible means "may activate when needed"; active means
  "currently holding the role." The goal is to keep powerful roles eligible, not
  active.
- **Activation controls** — require MFA at activation, a business justification, a
  ticket number, and/or approval by a designated approver.
- **Time-bound assignments** — both eligibility and activation can have start/end
  dates, so temporary access expires automatically.
- **Access reviews** — periodic attestations where owners confirm who still needs
  a role; stale access is removed.
- **Alerts and audit** — PIM logs every activation and can alert on risky
  configurations (too many Global Admins, admins without MFA).

PIM works for **both** Entra roles and Azure resource roles, and it requires a
**Microsoft Entra ID P2** license. It is the practical embodiment of least
privilege for privileged accounts.

## Putting it together

Azure has **two** authorization systems: **Azure RBAC** for resources (scoped from
management group down to a single resource, inherited downward) and **Entra roles**
for the directory. Grant the **narrowest built-in role at the narrowest scope**,
reach for **custom roles** only when needed, and remember assignments are additive
with **deny** winning. Then layer **PIM** on top so that powerful roles are
**eligible, not active** — activated just-in-time with MFA, justification, and
approval, reviewed regularly, and expiring on their own.

## Exam focus

- **Azure RBAC = resources; Entra roles = directory objects.** They are separate;
  a **Global Administrator has no Azure resource access by default**, and an Owner
  doesn't run the directory.
- RBAC assignment = **principal + role definition + scope**. Scope runs
  **management group → subscription → resource group → resource** and **inherits
  downward**; assign at the narrowest scope.
- **Owner** grants access to others; **Contributor** manages resources but
  **cannot** change access; **User Access Administrator** manages access only;
  **Reader** is view-only.
- Custom roles use **Actions/NotActions** (management plane) and
  **DataActions/NotDataActions** (data plane). Assignments are **additive**; a
  **deny assignment overrides allows**.
- **PIM** gives **just-in-time, time-bound** privilege: roles are **eligible**
  until **activated** (with MFA, justification, approval). It covers Entra *and*
  Azure roles and needs **P2**. Pair it with **access reviews** to prune stale
  access.
