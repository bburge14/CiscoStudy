# Azure Storage & Identity

This lesson covers two foundations that nearly every workload depends on: where
your data lives (**storage**) and who is allowed in (**identity**). They are
distinct topics, so we take them in turn — first the storage services and the
redundancy and tier choices that go with them, then Microsoft Entra ID and the
authentication concepts that protect access.

## Part 1: Azure Storage

### The storage account and its services

Most Azure storage lives inside a **storage account**, which offers several data
services. The four you should recognize:

> - **Blob storage** holds massive amounts of **unstructured** data — files,
>   images, video, backups — as "objects." It is the go-to for large files.
> - **Azure Files** provides fully managed **file shares** you can mount over the
>   **SMB** protocol from many VMs *and* on-premises machines at once.
> - **Queue storage** holds messages for applications to process asynchronously.
> - **Table storage** stores **structured, non-relational (NoSQL)** data as
>   key/attribute pairs with a schemaless design, cheaply and at scale.

Two more data options come up:

- **Managed disks** are **block-level** storage volumes attached to a VM that
  behave like a physical hard drive — the VM's operating system and data disks.
- **Azure SQL Database** is a fully managed **relational (PaaS) database** where
  Microsoft handles patching, backups, and the underlying OS; you just use the
  database.

Match the scenario to the service:

| Scenario | Service |
|----------|---------|
| Block volume that acts like a physical disk attached to a VM | **Managed disk** |
| Managed file share mounted over SMB by VMs and on-prem machines | **Azure Files** |
| Large unstructured objects (video, backups, images) | **Blob storage** |
| Structured NoSQL key/attribute data, schemaless, low cost | **Table storage** |
| Fully managed relational SQL database, no OS to patch | **Azure SQL Database** |

### Redundancy: how many copies, and where

Azure always keeps multiple copies of your data, but *where* those copies sit
determines what kind of failure you can survive. From least to most resilient:

> - **LRS (Locally Redundant Storage)** keeps copies within a **single datacenter**
>   in the primary region. Cheapest, but a datacenter-wide disaster could lose it.
> - **ZRS (Zone-Redundant Storage)** spreads copies across **availability zones**
>   in the primary region, surviving the loss of one zone.
> - **GRS (Geo-Redundant Storage)** keeps LRS copies in the primary region *and*
>   asynchronously replicates to a **paired secondary region** hundreds of miles
>   away — surviving a complete regional outage.
> - **GZRS (Geo-Zone-Redundant Storage)** combines ZRS in the primary region with
>   geo-replication to a secondary region — the most resilient option.

When a requirement says data must **survive a complete regional outage by
replicating to the paired region**, you need a **geo-redundant** option — **GRS**
or **GZRS**. The read-access variants **RA-GRS** and **RA-GZRS** add the ability to
*read* from the secondary region (otherwise the secondary copy is for recovery
only).

### Access tiers: pay less for cooler data

Blob storage lets you match cost to how often data is touched. There are four
tiers, and the minimum storage duration rises as the data gets "colder":

| Tier | Best for | Minimum stay |
|------|----------|--------------|
| **Hot** | Frequently accessed data; highest storage cost, lowest access cost | — |
| **Cool** | Infrequently accessed data kept at least a month | 30 days |
| **Cold** | Rarely accessed data that still needs fast retrieval | 90 days |
| **Archive** | Long-term data accessed almost never; **offline** | 180 days |

> The **Archive** tier is **offline**: a blob must be **rehydrated** (moved to an
> online tier) before you can read it, which takes time. Hot, cool, and cold are
> all online and immediately readable.

A classic scenario: monthly backups that are **accessed only occasionally but must
stay immediately available**, kept for at least 30 days → the **Cool** tier. If
the data were essentially never read and could tolerate a retrieval delay, that
would point to **Archive** instead.

## Part 2: Identity — Microsoft Entra ID

### What Entra ID is (and is not)

> **Microsoft Entra ID (formerly Azure Active Directory) is Azure's cloud-based
> identity and access management service.** It is where you create users and
> groups, and it authenticates people and applications for cloud resources,
> Microsoft 365, and thousands of third-party apps.

A common misconception the exam targets: **Entra ID is not simply on-premises
Active Directory running in the cloud.** On-premises Active Directory Domain
Services was built for managing Windows networks with organizational units, group
policy, and protocols like Kerberos and LDAP. Entra ID is a **flat, cloud-first**
identity service designed for web and cloud applications, using internet protocols
such as SAML, OAuth, and OpenID Connect. They solve related problems in very
different environments and can be connected, but they are not the same product.

> Entra ID is for **identity**, not bulk data. If someone suggests using Entra ID
> to store large video files, that is the **wrong tool** — it manages users and
> access, not files. Video belongs in **Blob storage**.

### Authentication vs authorization

These two words sound similar and are constantly confused, so pin them down:

> **Authentication (AuthN)** verifies *who you are* by checking your credentials.
> **Authorization (AuthZ)** determines *what you are allowed to do* once your
> identity is confirmed.

Showing a password or a fingerprint to prove your identity is **authentication**.
Being granted (or denied) access to a particular resource afterward is
**authorization**. Authentication always comes first.

### Multi-factor authentication (MFA)

> **Multi-factor authentication requires two or more different types of proof** —
> drawn from something you **know** (a password), something you **have** (a phone
> or token), and something you **are** (a fingerprint or face).

Requiring a **password plus a one-time code from a phone** is textbook MFA. It
blunts stolen-password attacks because the attacker still lacks the second factor.

### Conditional Access

> **Conditional Access** applies identity policies based on real-time signals —
> the user, their location, device health, and sign-in risk — to decide whether to
> allow access, block it, or require extra verification.

Conditional Access is how you prompt for **MFA only when a sign-in looks risky**
(for example, from an unfamiliar location) rather than on every single login. It
makes security adaptive instead of all-or-nothing.

### A few more identity features

- **Single sign-on (SSO)** lets a user authenticate once and then reach many
  applications without signing in again.
- **Self-service password reset (SSPR)** lets users securely reset their own
  passwords after verifying their identity, cutting help-desk calls.
- **Role-based access control (RBAC)** is the authorization model: you grant roles
  (collections of permissions) to users at a chosen scope, giving people only the
  access their job requires.

## Bringing it together

For storage, pick the **service** by data shape (blobs for unstructured objects,
Files for SMB shares, Table for NoSQL, managed disks for VM volumes, Azure SQL for
relational), the **redundancy** by the failure you must survive (LRS in one
datacenter → ZRS across zones → GRS/GZRS across regions), and the **tier** by
access frequency (hot → cool → cold → archive). For identity, **Entra ID** manages
users and access in the cloud; **authentication** proves identity while
**authorization** grants permissions; and **MFA**, **Conditional Access**, **SSO**,
**SSPR**, and **RBAC** are the tools that keep sign-ins both secure and usable.

## Exam focus

- **Blob** = unstructured objects/files; **Azure Files** = managed SMB file share
  for VMs and on-prem; **Table** = NoSQL key/attribute data; **managed disk** =
  block volume for a VM; **Azure SQL Database** = managed relational database.
- Redundancy: **LRS** (one datacenter) → **ZRS** (zones in a region) → **GRS/GZRS**
  (replicate to a **paired region**, survive a regional outage). **RA-** variants
  add read access to the secondary.
- Access tiers: **Hot** (frequent), **Cool** (30-day min), **Cold** (90-day min),
  **Archive** (offline, 180-day min, must rehydrate). "Occasional but immediately
  available, ~30 days" = **Cool**.
- **Microsoft Entra ID** (formerly Azure AD) = cloud identity service; **not** the
  same as on-prem Active Directory, and **not** for storing files.
- **Authentication** = who you are; **authorization** = what you may do. **MFA** =
  two or more factor types (password + phone code). **Conditional Access** = require
  MFA only on risky sign-ins. Know **SSO**, **SSPR**, and **RBAC** by name.
