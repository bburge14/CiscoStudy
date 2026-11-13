# Identity Protection & Governance

Granting access correctly on day one is not enough. Attackers try to compromise
identities every day, and the access you granted drifts out of date as people
change jobs and projects end. This lesson covers the tools that keep identity
*healthy over time*: **Microsoft Entra ID Protection** (detecting compromised
identities) and **Microsoft Entra ID Governance** (making sure access stays
appropriate and privileged access is tightly controlled).

## Microsoft Entra ID Protection

Some sign-ins are suspicious — a login from an impossible location, a password
seen in a known breach, an anonymous IP. Catching these automatically, at scale,
is the job of ID Protection.

> **Microsoft Entra ID Protection** uses signals and **machine learning** to
> detect, investigate and remediate identity-based risks. It evaluates **risky
> sign-ins** (is *this sign-in* suspicious?) and **risky users** (is *this
> account* likely compromised?) and can respond automatically.

ID Protection assigns a **risk level** (low/medium/high) and surfaces **risk
detections** such as anonymous IP use, atypical travel, leaked credentials, or
password-spray patterns. You then act on that risk with **risk-based policies**,
usually enforced through Conditional Access:

- **Sign-in risk policy** — e.g. *if a sign-in is high risk, block it or require
  MFA.*
- **User risk policy** — e.g. *if a user is flagged high risk, require a secure
  password change.*

This is the engine that feeds the "real-time risk" signal into Conditional
Access, closing the loop between detection and enforcement.

## Microsoft Entra ID Governance

Over time, people accumulate access they no longer need — a security problem
called **privilege creep**. **Microsoft Entra ID Governance** is a set of
capabilities that answer four questions: *Which identities have access to what?
What are they doing with it? Is that access still appropriate? Are there
effective controls on it?* Its headline features are entitlement management,
access reviews, lifecycle workflows and Privileged Identity Management.

### Entitlement management

> **Entitlement management** bundles resources — groups, applications and
> SharePoint sites — into **access packages** that users (including external
> partners) can **request**. Requests go through **approval workflows** and the
> access can **automatically expire.**

Instead of an admin manually wiring up access, you define an access package once
("New-hire marketing bundle") and let people request it. Approvals, time limits
and automatic removal are built in — governance by self-service.

### Access reviews

> **Access reviews** periodically ask the right people (managers or the users
> themselves) to **confirm whether each person still needs** their current group
> memberships, roles or app access, and automatically remove those who do not.

Access reviews are the direct cure for privilege creep. For example: every quarter
a manager reviews who is still in the "Finance App Users" group and removes anyone
who has moved on.

### Lifecycle workflows

**Lifecycle workflows** automate the "joiner-mover-leaver" process — provisioning
access when someone joins, adjusting it when they change roles, and removing it
when they leave — so access tracks employment automatically instead of relying on
someone remembering to flip switches.

### Privileged Identity Management (PIM)

The riskiest accounts are the privileged ones. Leaving someone a **standing**
Global Administrator is a standing invitation to attackers. PIM fixes that.

> **Privileged Identity Management (PIM)** provides **just-in-time**,
> **time-limited** activation of privileged roles, with **approval**, MFA and
> **auditing** — so admins hold elevated rights only when they actually need
> them, not permanently.

With PIM, a user is *eligible* for a role rather than permanently assigned. When
they need it, they **activate** it for a set window (say, two hours), often with
justification and approval, and it is logged. This directly enforces **least
privilege** and **assume breach**: there is no always-on admin account for an
attacker to steal.

| Capability | What it does |
|------------|--------------|
| **Entitlement management** | Access packages users request, with approval and expiry |
| **Access reviews** | Periodic recertification of who still needs access |
| **Lifecycle workflows** | Automate joiner/mover/leaver access changes |
| **PIM** | Just-in-time, time-limited, audited privileged access |
| **ID Protection** | ML-based detection of risky sign-ins and users |

## How it all fits together

ID Protection watches for compromised identities and feeds risk into Conditional
Access. ID Governance makes sure the access people hold stays correct —
entitlement management grants it cleanly, access reviews prune it, lifecycle
workflows keep it in step with employment, and PIM keeps the powerful roles under
lock and key. Everything here is an expression of **least privilege** and
**assume breach** from the Zero Trust lesson.

## The whole thing in one paragraph

**Microsoft Entra ID Protection** uses machine learning to detect **risky
sign-ins** and **risky users** and remediate them with **risk-based policies**
(usually via Conditional Access). **Microsoft Entra ID Governance** keeps access
appropriate over time: **entitlement management** delivers requestable **access
packages** with approvals and expiry, **access reviews** recertify who still
needs access, **lifecycle workflows** automate joiner/mover/leaver changes, and
**Privileged Identity Management (PIM)** grants privileged roles **just in time**,
time-limited and audited — enforcing least privilege for admins.

## Exam focus

- **Microsoft Entra ID Protection** = **ML-based** detection of **risky sign-ins
  and risky users**, remediated with **risk-based policies** (can auto-require MFA
  or block).
- **Privileged Identity Management (PIM)** = **just-in-time, time-limited,
  approved, audited** activation of privileged roles. The answer whenever a
  scenario wants to avoid **standing** admin access.
- **Access reviews** = periodically **confirm access is still needed** and remove
  what isn't (fights privilege creep).
- **Entitlement management** = **access packages** users request, with approval
  workflows and automatic expiration; works for external partners too.
- All of these live under **Microsoft Entra ID Governance** and enforce **least
  privilege**.
