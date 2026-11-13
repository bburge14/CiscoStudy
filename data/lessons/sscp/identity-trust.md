# Identity Lifecycle & Trust Architectures

An account is not a one-time thing you create and forget. It is born, it changes
as a person's job changes, and it must die cleanly when they leave. This lesson
covers that **identity lifecycle** and then widens out to **trust
architectures** — the relationships that let separate domains and even separate
organizations accept each other's identities. Both topics are really about one
idea: making sure access always matches current, legitimate need.

## The identity lifecycle

> The **identity lifecycle** is the end-to-end management of an account from
> **provisioning** (creation and initial access) through ongoing **changes** to
> final **deprovisioning** (disabling and removal).

A common shorthand is **JML — Joiner, Mover, Leaver:**

- **Joiner (provisioning)** — when a new hire arrives, create the account and
  grant access. The twin principles here are **least privilege** (only the access
  the role requires) and **need-to-know** (only the specific data the task
  requires). Grant the minimum; you can always add more.
- **Mover (modification)** — when someone changes roles, their access must be
  *re-evaluated*, not merely added to. The classic failure is **privilege creep
  (authorization creep)**: a long-tenured employee accumulates rights from every
  past role and ends up massively over-privileged.
- **Leaver (deprovisioning)** — when someone is terminated, **promptly disabling
  their accounts and revoking all access is the single most critical action.** A
  lingering active account for a former (possibly disgruntled) employee is a
  serious, easily exploited risk. For an involuntary termination, access should
  be cut at or before the moment of notification.

Two ongoing practices keep the lifecycle honest:

- **Access recertification (access review / attestation)** — a periodic process
  where managers confirm each user's current access still matches their job and
  remove what no longer applies. This is the primary cure for privilege creep.
- **Separation of duties (SoD)** — split a sensitive process so no one person
  controls it end to end (the person who requests a payment can't also approve
  it). SoD limits fraud and error. A related control, **job rotation**, moves
  people through roles to expose collusion and reduce dependence on any one
  person.

> **Least privilege** limits *how much* access; **need-to-know** limits access to
> *specific data*; **separation of duties** limits *how much control* one person
> has over a whole process. The exam tests all three as distinct ideas.

## Trust architectures: extending identity across boundaries

A single domain can manage its own identities. The moment two domains — or two
companies — need to share resources, you need a **trust relationship** that says
"I will accept identities authenticated over there."

### Trust between domains

> A **trust** is an agreement by which one domain accepts authentications
> performed by another.

- **One-way trust** — Domain A trusts Domain B, but not vice versa. Users in B can
  be granted access to resources in A, but not the reverse. The direction of trust
  is **opposite** to the direction of access, which trips people up.
- **Two-way (bidirectional) trust** — each domain trusts the other.
- **Transitive trust** — trust that flows along a chain: if A trusts B and B
  trusts C, then A automatically trusts C *without a direct relationship being
  configured.* Active Directory uses transitive trusts within a forest. A
  **non-transitive** trust stops at the two domains it connects.

### Federation: trust between organizations

**Federated identity** extends this idea across organizational boundaries, so a
user authenticated by their *home* organization can access a *partner's*
application without a separate account there. Two roles define it:

> The **Identity Provider (IdP)** authenticates the user and asserts their
> identity. The **Service Provider (SP)** / relying party consumes that assertion
> and grants access. The user's credentials never leave the IdP.

The protocols that carry these assertions — know what each is for:

| Protocol | Purpose |
|----------|---------|
| **SAML** (Security Assertion Markup Language) | XML-based; the workhorse of enterprise web SSO and federation — the IdP sends the SP a signed assertion |
| **OAuth 2.0** | **Authorization** — delegates access to resources (e.g., "let this app read my calendar") via tokens; it is *not* an authentication protocol by itself |
| **OpenID Connect (OIDC)** | An **authentication** layer built on top of OAuth 2.0, common for consumer "log in with..." |

A frequent exam scenario: "employees sign in to a third-party SaaS app using their
corporate identity; the corporate IdP sends the app a signed assertion." That is
**SAML-based federation**. Keep the OAuth-vs-OIDC distinction sharp: **OAuth is
authorization (delegated access); OIDC adds authentication (who you are).**

## Privileged accounts need extra care

Not all identities are equal. **Privileged accounts** — administrators, root,
service accounts — are the keys to the kingdom, so they get tighter controls than
ordinary users:

> **Privileged Access Management (PAM)** is the set of controls for securing
> high-privilege accounts: vaulting their credentials, granting elevated rights
> **just-in-time** for a limited window rather than permanently, enforcing MFA, and
> recording privileged sessions for audit.

Practices that reduce privileged-account risk:

- **Credential vaulting** — admins check out a password from a vault that rotates
  it after use, so the actual password is never known or reused.
- **Just-in-time (JIT) access** — elevate a user to admin only for the task at
  hand, then automatically revoke it, shrinking the window of standing privilege.
- **Separate admin accounts** — administrators use a distinct, non-email account
  for privileged work, never their everyday login.
- **Session monitoring/recording** — privileged sessions are logged for
  accountability.

These apply the same lifecycle discipline — least privilege, review, prompt
revocation — with the volume turned up, because a compromised admin account is
far more damaging than a compromised standard one.

## Exam focus

- The identity lifecycle = **provision (joiner) -> modify (mover) ->
  deprovision (leaver).** Provision with **least privilege** and **need-to-know**.
- On termination, **disable accounts and revoke access promptly** — the top
  priority for a leaver.
- **Privilege creep** = access accumulating across role changes; the cure is
  **periodic access recertification / attestation**.
- **Separation of duties** splits a sensitive process so no one person controls it;
  **job rotation** exposes collusion. Distinguish these from least privilege.
- **One-way trust**: trust direction is opposite to access direction. **Transitive
  trust**: A trusts B, B trusts C, so A trusts C with no direct link.
- **Federation**: **IdP** authenticates and asserts; **SP** consumes the assertion.
  **SAML** = enterprise SSO assertions; **OAuth** = delegated **authorization**;
  **OIDC** = **authentication** on top of OAuth.
