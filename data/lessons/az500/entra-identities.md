# Microsoft Entra ID: Tenants, Users & Groups

In Azure, identity is the real security perimeter. A virtual machine can sit
behind firewalls, but if an attacker holds a valid credential they walk in the
front door. That is why AZ-500 opens with the directory service that every other
Azure control leans on: **Microsoft Entra ID**.

> **Name change you must know:** what used to be called **Azure Active Directory
> (Azure AD)** was renamed **Microsoft Entra ID** in 2023. The capabilities,
> APIs, and sign-in endpoints did not change — only the name. Exam items and the
> portal now say "Entra ID," so that is the term used throughout these lessons.
> (Windows Server Active Directory, the on-premises domain service, keeps its own
> name and is a different product.)

## What a tenant is

A **tenant** is a single, dedicated instance of Entra ID that an organization
gets when it signs up for a Microsoft cloud service. It is the container for your
users, groups, and app registrations, and it is identified by a **tenant ID** (a
GUID) and one or more domains such as `contoso.onmicrosoft.com`.

The relationship between the directory and your resources trips people up, so be
precise:

- **Entra ID is not Azure.** The directory holds identities. **Azure
  subscriptions** hold resources (VMs, storage, networks) and billing.
- One Entra tenant can **trust many subscriptions**, but each subscription trusts
  exactly **one** tenant at a time for authentication. Moving a subscription to a
  different tenant breaks all its existing role assignments.
- Signing in proves *who you are* (authentication, handled by Entra ID). What you
  may *do* to resources is a separate step (authorization, handled by Azure RBAC —
  a later lesson).

## Users: members and guests

Every person who signs in is represented by a **user object**. Two kinds matter:

- **Member users** are the organization's own accounts, usually created directly
  in the tenant or synchronized from on-premises Active Directory with **Microsoft
  Entra Connect**.
- **Guest users** are external people invited through **B2B collaboration**. Their
  `userType` is *Guest*, their UPN is stamped with `#EXT#`, and they authenticate
  against their home directory, not yours. Guests get deliberately limited default
  directory permissions.

Accounts that come from on-premises sync are governed partly by the sync engine:
you typically manage them in AD and let **password hash synchronization**,
**pass-through authentication**, or **federation** carry the sign-in. Cloud-only
accounts are managed entirely in Entra ID.

## Groups: how you assign at scale

You almost never assign access to individuals — you assign it to **groups** and
manage membership. Know the two group types and the two membership models:

| Dimension | Options | Notes |
|-----------|---------|-------|
| **Type** | **Security** vs **Microsoft 365** | Security groups grant access to resources and roles; M365 groups also create a shared mailbox and SharePoint site |
| **Membership** | **Assigned** vs **Dynamic** | Assigned = you add members by hand; dynamic = membership is computed from a rule |

**Dynamic groups** are powerful for security: you write a membership rule over
user or device attributes — for example, `user.department -eq "Finance"` — and
Entra ID adds or removes members automatically as attributes change. Dynamic
membership requires a **Microsoft Entra ID P1** license.

## Administrative units: scoping admin power

By default a directory role (like Helpdesk Administrator) applies to the **entire
tenant**. An **administrative unit (AU)** carves the directory into a scope — say,
one region or business unit — so you can grant an admin authority over *only* the
users, groups, or devices in that AU. This is how a large organization delegates
helpdesk or password-reset duties without handing out tenant-wide power. AUs
support the principle of least privilege for directory administration.

## External identities

Collaborating with partners and customers without creating shadow accounts is the
job of **Microsoft Entra External ID**, the current umbrella for external-facing
identity:

- **B2B collaboration** invites partner users as guests so they can access your
  apps using their own credentials. You control them with Conditional Access and
  guest-access settings, and **cross-tenant access settings** govern which outside
  organizations you trust inbound and outbound.
- **Customer-facing (CIAM) scenarios** — letting your customers sign up and sign
  in to an app you publish — are handled by the newer **External ID** external
  tenant model, the successor to the older Azure AD B2C service.

## Device identity

Devices are identities too, and registering them unlocks Conditional Access rules
like "only compliant devices may connect":

- **Entra registered** — typically personal (BYOD) devices given a lightweight
  identity in the directory.
- **Entra joined** — corporate devices joined directly to the cloud directory
  (no on-premises domain).
- **Hybrid Entra joined** — devices joined to on-premises AD *and* registered in
  Entra ID, for organizations mid-migration.

## Licensing tiers at a glance

Many security features are gated by license, and the exam expects you to know
roughly where the line sits:

- **Free** — core user/group management, SSO, basic security defaults.
- **Entra ID P1** — Conditional Access, dynamic groups, self-service password
  reset with writeback, basic Privileged Identity Management is *not* here.
- **Entra ID P2** — adds **Entra ID Protection** (risk-based policies) and
  **Privileged Identity Management (PIM)**.

## Putting it together

Entra ID is the directory that authenticates every identity in your Azure estate.
A **tenant** holds your users and groups; **subscriptions** hold resources and
each trusts one tenant. You represent people as **member** or **guest** users,
assign access through **security groups** (assigned or dynamic), delegate admin
power narrowly with **administrative units**, bring in partners and customers
through **External ID**, and register **devices** so they can become a signal for
access decisions. Everything in the rest of this unit — MFA, Conditional Access,
RBAC, PIM — builds on these objects.

## Exam focus

- **Azure AD is now Microsoft Entra ID** — same service, new name. Expect the new
  terminology; Windows Server Active Directory is a separate, on-premises product.
- A **tenant** is one directory instance; a **subscription** trusts exactly one
  tenant. Identities live in the tenant, resources live in the subscription.
- **Guest users** (`#EXT#`, userType Guest) come from **B2B collaboration** and
  authenticate in their home tenant. Customer sign-up/sign-in uses **External ID**
  (successor to Azure AD B2C).
- **Dynamic groups** compute membership from an attribute rule and need **P1**;
  use them to keep access aligned with changing user or device attributes.
- An **administrative unit** scopes a directory role to a subset of the tenant —
  the tool for least-privilege, delegated directory administration.
- Device states: **Entra registered** (BYOD), **Entra joined** (cloud corporate),
  **hybrid Entra joined** (cloud + on-prem AD).
- **Entra ID Protection** and **PIM** require a **P2** license; Conditional Access
  and dynamic groups require **P1**.
