# Microsoft Entra ID & Identity Types

Now we move from concepts to Microsoft's actual products. The foundation of the
whole security stack is **Microsoft Entra** — Microsoft's family of identity and
network-access products. At its heart is **Microsoft Entra ID**, the cloud
identity provider that decides who can sign in and what they can reach. This
lesson explains what Entra ID is and the different **identity types** it manages.

## What is Microsoft Entra ID?

> **Microsoft Entra ID** is Microsoft's cloud-based **identity and access
> management** service. It was **formerly known as Azure Active Directory (Azure
> AD)**. It authenticates users and applications and controls their access to
> resources such as Microsoft 365, the Azure portal and thousands of SaaS apps.

Entra ID is the IdP from the previous lesson, made real. It is also part of a
larger **Microsoft Entra** product family that includes, among others:

- **Microsoft Entra ID** — core identity and access management.
- **Microsoft Entra ID Governance** — entitlement management, access reviews and
  Privileged Identity Management (covered in a later lesson).
- **Microsoft Entra ID Protection** — risk-based detection of risky sign-ins and
  users.
- **Microsoft Entra External ID** — identity for external users (customers and
  partners).
- **Global Secure Access** — identity-centric network access (Entra Internet
  Access and Entra Private Access).

For this lesson, focus on Entra ID and the kinds of identities it holds.

## Human identities: users

The most familiar identity is a **user**. Entra ID distinguishes two kinds based
on where the account comes from:

- **Member** — an internal user, typically an employee, whose account lives in
  your organization's tenant.
- **Guest** — an external user from another organization, invited to collaborate
  (through B2B collaboration). Their home account stays in their own directory.

A **tenant** is your organization's dedicated, isolated instance of Entra ID —
think of it as your own private directory in Microsoft's cloud.

## Groups: managing access at scale

Assigning rights to users one at a time does not scale. **Groups** let you assign
access to many users at once.

> A **group** collects users (and sometimes devices) so that access can be
> assigned to the group rather than to each member individually. Add a user to
> the group and they inherit its access; remove them and it is revoked.

Entra ID has **security groups** (used to grant access to resources) and
**Microsoft 365 groups** (which also provide shared mailboxes, calendars and
files for collaboration). Membership can be assigned manually or **dynamic** —
driven automatically by user attributes such as department.

## Workload identities: software that needs access

People are not the only things that sign in. Apps, scripts and services need
identities too. These are **workload identities**.

> A **workload identity** is an identity used by software — an application,
> service or automation tool — rather than a human, so it can authenticate and
> access resources. The two main types are **service principals** and **managed
> identities**.

### Service principals

A **service principal** is the local representation of an application in your
tenant — it defines what the app can do and what it can access. When you register
an app in Entra ID, it gets a service principal to act under.

### Managed identities

Managed identities solve a real headache: credentials in code. If an app needs to
reach, say, Azure Key Vault, someone has to store and rotate a secret — and
secrets in source code leak.

> A **managed identity** is a special workload identity that Azure **creates and
> manages for you**, so your app can authenticate to services **without any
> developer storing, rotating or handling credentials in code.**

There are two flavors:

- **System-assigned** — tied to a single Azure resource; created and deleted with
  that resource.
- **User-assigned** — a standalone identity you create once and share across
  multiple resources.

If a question describes an app that must access a resource "without storing
credentials," the answer is a **managed identity**.

## Device identities

Devices can have identities too, which lets policies consider whether a laptop or
phone is known and healthy. Common states:

- **Registered** — a (often personal, BYOD) device known to Entra ID.
- **Entra joined** — a device joined directly to Entra ID (cloud).
- **Hybrid joined** — joined to both on-premises AD and Entra ID.

Device identity is what lets **Conditional Access** say "only allow this app from
a managed, compliant device."

## Hybrid and external identities

Two more situations round out the picture:

- **Hybrid identity** — many organizations still run on-premises Active Directory.
  By synchronizing it to Entra ID (using **Microsoft Entra Connect**), a single
  identity works both on-premises and in the cloud. Users get one set of
  credentials for everything.
- **External identities** — collaboration and customer scenarios. **B2B
  collaboration** invites partners as **guests** using their own credentials.
  **Microsoft Entra External ID** is Microsoft's platform for giving external
  users (customers and partners) secure, branded sign-in — it is the successor to
  the older Azure AD B2C/External Identities offerings.

## The whole thing in one paragraph

**Microsoft Entra ID** (formerly **Azure AD**) is the cloud identity and access
service at the center of the Microsoft Entra family. It manages several identity
types: **users** (internal **members** and external **guests**), **groups** for
assigning access at scale, **workload identities** for software — namely
**service principals** and **managed identities** (which let apps authenticate
with no credentials in code) — and **device identities**. **Hybrid identity**
syncs on-premises Active Directory into Entra ID so one identity works
everywhere, and **External ID** / B2B handle customers and partners.

## Exam focus

- **Microsoft Entra ID = formerly Azure Active Directory (Azure AD)**, a
  **cloud** identity and access management service and identity provider.
- Identity types: **users** (member vs. guest), **groups**, **workload
  identities** (service principals, managed identities), and **devices**.
- A **managed identity** lets an app authenticate to Azure services **without
  developers managing credentials in code** — system-assigned (tied to one
  resource) or user-assigned (shared).
- Use a **group** to assign the same access to many users at once.
- **Hybrid identity** connects on-premises AD to Entra ID (via **Entra
  Connect**); **B2B / Microsoft Entra External ID** cover external guests and
  customers.
