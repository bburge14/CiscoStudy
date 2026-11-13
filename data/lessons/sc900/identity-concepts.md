# Identity Concepts

For decades, security meant guarding the network perimeter — the firewall was the
castle wall. But when your apps live in the cloud and your people work from
anywhere on any device, there is no single wall left to defend. What every request
still has in common is an **identity**. This lesson explains why identity is now
the perimeter, the difference between proving who you are and what you may do, and
the services that make identity work.

## Identity is the new primary security perimeter

> When users, apps and data are spread across on-premises and many clouds, the
> thing you can consistently check on every request is **identity**. That is why
> modern security treats **identity as the primary security perimeter** rather
> than the network boundary.

If identity is the perimeter, then the quality of your identity controls — strong
authentication, least-privilege access, continuous verification — becomes the main
thing standing between an attacker and your data. This is exactly why Zero Trust
starts with "verify explicitly."

An identity can belong to more than just people. The four common kinds:

- **Users** — humans (employees, partners, customers).
- **Applications and service principals** — software identities for apps and
  services.
- **Devices** — laptops, phones, servers registered to the organization.
- **Other resources** — anything that needs to be authenticated and authorized.

## Authentication vs. authorization

These two words sound alike and are constantly confused, so nail the difference.

> **Authentication (AuthN)** verifies **who you are** — it proves your identity.
> **Authorization (AuthZ)** determines **what you are allowed to do** once your
> identity is proven.

- You walk up to a building. Showing your badge to prove you are an employee is
  **authentication**. The door system then deciding which floors your badge opens
  is **authorization**.
- Authentication always comes **first**; authorization is the second step, and
  only happens after you have authenticated.

A simple sign-in shows both: you type your password (authentication), then the
app checks your permissions to decide which files you can open (authorization).

## The identity provider and single sign-on

Instead of every application storing its own usernames and passwords, modern
systems centralize identity in an **identity provider**.

> An **identity provider (IdP)** creates, stores and manages identities, and
> offers **authentication** (and often authorization) services to applications
> that trust it. **Microsoft Entra ID** is a cloud identity provider.

Centralizing identity in an IdP unlocks **single sign-on**:

> **Single sign-on (SSO)** lets a user authenticate **once** and then access many
> different applications without being prompted to sign in again for each one.

SSO is not just convenient — it is more secure. Fewer passwords means fewer
chances for weak or reused credentials, and the organization can enforce strong
authentication (like MFA) in one place rather than hoping each app does it right.

## Directory services and Active Directory

An IdP needs somewhere to keep all those identities. That is a **directory
service** — a structured database of users, groups, devices and their attributes.

- **Active Directory Domain Services (AD DS)** is Microsoft's long-standing
  **on-premises** directory. It organizes a company's internal network into
  domains and uses protocols like Kerberos and LDAP. It was built for the era of
  company-owned PCs on a corporate LAN.
- **Microsoft Entra ID** is the **cloud-based** identity and access service
  (formerly named Azure Active Directory). It is designed for internet-facing
  apps, mobile devices and SaaS, speaking modern protocols like SAML, OAuth 2.0
  and OpenID Connect.

They are **not the same product**, and Entra ID is not simply "AD in the cloud."
Many organizations run both and link them — a **hybrid identity** setup — so a
single identity works both on-premises and in the cloud.

## Federation

Sometimes you need to trust identities from a *different* organization or system
without creating accounts for them. That is **federation**.

> **Federation** is a trust relationship between two identity systems that lets
> users authenticated in one domain access resources in another, **without a
> separate account** in the second domain.

A useful picture: a driver's license issued by one state is accepted by another
state's police because the states trust each other's issuing process. You did not
get a second license — the trust is federated.

- Federation lets users sign in with their **home** identity provider and still
  reach a partner's application that trusts that provider.
- It is how you collaborate with partners, or sign into a third-party app "with"
  your work or school account. SAML and OpenID Connect are common federation
  protocols.

Do not confuse federation with SSO: **SSO** signs you into many apps within a
trust boundary with one authentication; **federation** extends trust *across*
organizational or system boundaries so authentication in one place is accepted in
another.

## The whole thing in one paragraph

Because people, apps and data are everywhere, **identity is the primary security
perimeter**. **Authentication** proves who you are; **authorization** (which
comes second) decides what you may do. An **identity provider** such as
**Microsoft Entra ID** centralizes identities and enables **single sign-on** —
authenticate once, reach many apps. Identities live in a **directory service**:
**Active Directory Domain Services** on-premises, **Microsoft Entra ID** in the
cloud (and hybrid links the two). Finally, **federation** builds trust between
separate identity systems so a user authenticated in one can access resources in
another without a second account.

## Exam focus

- **Identity = the primary security perimeter** in the modern, cloud-and-mobile
  world; the network edge is no longer the main boundary.
- **Authentication (AuthN) = who you are; authorization (AuthZ) = what you can
  do.** Authentication always happens first.
- An **identity provider (IdP)** creates/stores/manages identities and provides
  authentication; **Microsoft Entra ID** is the IdP. **SSO** = authenticate once,
  access many apps.
- **Active Directory Domain Services** is **on-premises**; **Microsoft Entra ID**
  is **cloud** (formerly Azure AD). They are different products; hybrid identity
  links them.
- **Federation** = a **trust between two identity systems** so a user from one
  can access the other **without a separate account**. Don't confuse it with SSO.
