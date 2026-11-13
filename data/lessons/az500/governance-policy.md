# Governance with Azure Policy

RBAC decides *who* can act on resources. **Governance** decides *what those
resources are allowed to be* — which regions they deploy to, whether encryption is
required, which SKUs are permitted — and proves, continuously, that the estate
stays compliant. The primary tool is **Azure Policy**, reinforced by **management
groups**, **resource locks**, and **tags**. Keeping Policy and RBAC straight is a
recurring AZ-500 theme.

## Policy vs RBAC — a clean split

> **Azure RBAC** governs **actions and identities** — *who* may do *what* to
> resources. **Azure Policy** governs **resource properties and state** —
> *what configurations are allowed*, regardless of who is deploying. They work
> together: RBAC lets you create a VM; Policy can still deny it if it's in a
> banned region or missing encryption.

## How Azure Policy works

Azure Policy evaluates resources against rules and reports or enforces compliance.
The pieces:

1. **Policy definition** — a rule, e.g. "storage accounts must deny public blob
   access" or "allowed locations = West Europe, North Europe."
2. **Initiative (policy set)** — a bundle of related definitions managed as one
   (for example, a whole regulatory standard).
3. **Assignment** — applying a definition or initiative at a **scope**
   (management group, subscription, or resource group). Assignments **inherit
   downward**, and you can set **exclusions**.

### Effects — what a policy does when it matches

The **effect** is the exam favorite. Know what each does:

| Effect | Behavior |
|--------|----------|
| **Deny** | **Blocks** a non-compliant create/update outright |
| **Audit** | **Allows** it but flags it non-compliant (visibility, no block) |
| **Append** | Adds fields to a resource during creation |
| **Modify** | Changes/adds properties (e.g. tags) on create/update and can remediate existing ones |
| **DeployIfNotExists (DINE)** | Deploys a related resource/config if missing (e.g. enable diagnostic settings) |
| **AuditIfNotExists** | Audits when a related resource/config is missing |
| **Disabled** | Turns the rule off |

> **Deny prevents; Audit only reports.** If a question wants to *stop*
> non-compliant resources, the answer is **Deny**; if it wants to *report without
> blocking*, it's **Audit**.

### Remediation and exemptions

- **DeployIfNotExists** and **Modify** can fix resources that are already
  non-compliant through a **remediation task** — which runs under a **managed
  identity** that Azure Policy uses to make the change, so it needs the right RBAC
  role.
- An **exemption** formally waives specific resources from a policy or initiative
  (with a reason and expiry) — cleaner and more auditable than editing exclusions.

## Organizing scope with management groups

**Management groups** sit **above subscriptions** in a hierarchy. Assign a policy
(or an RBAC role) at a management group and it **flows down to every subscription
and resource beneath it** — so you enforce "all production subscriptions must
require encryption" in one place instead of per subscription. This inheritance is
the backbone of enterprise-scale governance.

## Built-in compliance and Defender for Cloud

Azure Policy is also how posture standards are enforced. The **Microsoft Cloud
Security Benchmark** that drives Defender for Cloud's secure score is a built-in
**policy initiative**, and the **regulatory compliance dashboard** (ISO 27001, PCI
DSS, NIST) is built from policy initiatives too. Assigning a regulatory initiative
makes Azure Policy continuously audit your estate against that standard.

## Resource locks and tags

Two lightweight governance tools round things out:

- **Resource locks** protect against accidental change or deletion, independent of
  RBAC:
  - **CanNotDelete** — you can read and modify, but **not delete**.
  - **ReadOnly** — you can read, but **not modify or delete**.
  Locks apply to everyone, even subscription Owners, until removed.
- **Tags** are name/value metadata for organizing and governing resources (cost
  center, environment, data classification). Policy can **require** tags and
  **Modify** can apply them — the basis for tag-driven governance and reporting.

## A note on Azure Blueprints

You may still see **Azure Blueprints**, which packaged policies, RBAC, and ARM
templates into a repeatable "environment in a box." It is **deprecated (preview)
and being retired** (final retirement January 31, 2027, with phased changes
beginning mid-2026). Microsoft's guidance is to use **Deployment Stacks** (for
assignment, lifecycle, and locking) together with **template specs** (for storing
and versioning artifacts). Recognize the term, but treat Policy, management groups,
and these newer tools as the current approach.

## Putting it together

**Azure Policy** enforces what resources are allowed to be, through **definitions**
and **initiatives** **assigned** at a scope, with **effects** that range from
**Deny** (block) to **Audit** (report) to **DeployIfNotExists/Modify** (fix,
via a remediation task running under a managed identity). **Management groups**
let that governance **inherit** across many subscriptions; built-in initiatives
tie Policy to the **Microsoft Cloud Security Benchmark** and **regulatory
compliance**. **Resource locks** stop accidental deletion/modification even by
Owners, and **tags** enable metadata-driven governance. Keep the core distinction:
**RBAC = who can act; Policy = what resources may be.**

## Exam focus

- **RBAC governs actions/identities (who can do what); Azure Policy governs
  resource configuration (what's allowed).** They complement each other.
- Policy structure: **definition → initiative (set) → assignment** at a scope;
  assignments **inherit downward** and support **exclusions/exemptions**.
- Effects: **Deny** (block non-compliant), **Audit** (report only), **Append**,
  **Modify**, **DeployIfNotExists (DINE)**, **AuditIfNotExists**, **Disabled**.
  "Prevent" ⇒ Deny; "report without blocking" ⇒ Audit.
- **DINE/Modify** fix existing resources via a **remediation task** that runs under
  a **managed identity** (needs RBAC).
- **Management groups** sit above subscriptions; policy/RBAC assigned there flows
  down — the tool for enterprise-wide governance.
- The **Microsoft Cloud Security Benchmark** and the **regulatory compliance
  dashboard** are built-in **policy initiatives**.
- **Resource locks**: **CanNotDelete** and **ReadOnly** apply to everyone,
  including Owners. **Tags** enable metadata governance (Policy can require them).
- **Azure Blueprints is deprecated/retiring**; the replacement is **Deployment
  Stacks + template specs**.
