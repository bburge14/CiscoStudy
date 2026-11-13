# Access Control Models & Federated Identity

Once a subject is authenticated, the system must decide *what it may do* — that's
the job of an access control model. And when identity must span organizations (log
in once, reach many partner apps), that's federation. This lesson covers the four
classic access control models and the federation protocols — SAML, OAuth, and
OIDC — that CISSP expects you to tell apart precisely.

## The access control models

Each model answers "who decides access, and based on what?" Know the decider and
the basis for each.

> **DAC (Discretionary Access Control)** — the **data owner** decides who gets
> access, at their discretion, usually via **ACLs**. Flexible but prone to sprawl.
> Standard in commercial file systems (Windows, Linux file permissions).

> **MAC (Mandatory Access Control)** — the **system** enforces access by comparing
> a subject's **clearance** to an object's **classification label**. Users
> **cannot** change labels or grant access to others. Rigid and strong — used in
> military and high-security systems.

> **RBAC (Role-Based Access Control)** — access is granted to **roles**, and users
> inherit it by holding a role. Scales beautifully in large enterprises because you
> manage a few roles instead of thousands of individual grants.

> **ABAC (Attribute-Based Access Control)** — decisions use **attributes and policy**
> (user department, device health, time of day, location). The most granular and
> context-aware; the engine behind modern zero-trust and risk-adaptive access.

A couple more to recognize:

- **Rule-based access control** — applies global rules regardless of identity (a
  firewall ACL, "no access after 6 pm"). Often layered on RBAC.
- **Risk-based / adaptive** — adjusts requirements based on real-time risk signals
  (step-up MFA from a new country).

The tested cue for **MAC**: "the system enforces clearance vs classification and
ordinary users cannot alter labels or share access." The cue for **RBAC**: "access
assigned by job function" and "scales for a large organization." For **DAC**: "the
owner grants access at their discretion."

### Authorization mechanisms

Underlying these are three ways to represent permissions:

- **Access control matrix** — the full table of subjects × objects.
- **ACL (Access Control List)** — a matrix column: who may act on *this object*.
- **Capability table** — a matrix row: what *this subject* may touch (Kerberos
  tickets are capability-like).

## Federated identity

**Federation** lets identities from one trust domain be accepted in another, so a
user authenticates at their home **Identity Provider (IdP)** and accesses
**Service Providers (SPs)** elsewhere without new credentials. Three protocols
dominate, and the exam's favorite task is distinguishing them.

### SAML — enterprise web SSO

> **SAML (Security Assertion Markup Language)** uses **XML-based assertions**
> exchanged between an **IdP** and **SPs** to deliver cross-domain **web single
> sign-on**. It handles **authentication** (and conveys attributes/authorization
> data).

If a scenario says "XML assertions," "IdP to SP," and "enterprise/partner web SSO,"
the answer is **SAML**.

### OAuth 2.0 — delegated authorization

> **OAuth 2.0** is an **authorization** framework (not authentication). It lets a
> user grant one app limited access to their resources on another **without sharing
> their password**, using **access tokens** with specific scopes.

Think of OAuth as a **valet key**: it lets an app do one narrow thing (read your
calendar) without handing over full control. OAuth answers "*what may this app do
on my behalf?*", not "*who are you?*".

### OpenID Connect — authentication on top of OAuth

> **OpenID Connect (OIDC)** is a thin **identity (authentication) layer built on
> OAuth 2.0.** It adds an **ID token** (a JWT) that proves *who* the user is. It
> powers "log in with Google/Microsoft."

The clean trio to memorize:

| Protocol | Purpose | Format |
|----------|---------|--------|
| **SAML** | Authentication + SSO (enterprise web) | XML assertions |
| **OAuth 2.0** | **Authorization** (delegated access) | Access tokens |
| **OIDC** | **Authentication** (identity, on OAuth) | ID token (JWT) |

### FIDO2 and provisioning standards

**FIDO2 / WebAuthn** enables **passwordless, phishing-resistant** authentication
using public-key credentials bound to the device (passkeys) — increasingly paired
with federation to kill passwords entirely. For automated account **provisioning**
across federated systems, **SCIM** (and the older SPML) synchronize identities so
joiners and leavers propagate automatically.

> Federation's payoff is also its risk: trust is transitive. If the IdP is
> compromised, every SP that trusts it is exposed — so the IdP must be a hardened,
> well-monitored crown jewel, and the federation trust relationships must be
> governed deliberately.

## Exam focus

- **DAC** = owner decides (ACLs); **MAC** = system enforces clearance vs label,
  users can't change it (military); **RBAC** = access by **role** (scales in large
  orgs); **ABAC** = **attribute/policy**-based, context-aware (zero trust).
- Permissions are modeled as an **access control matrix**; an **ACL** is the
  object's view, a **capability** is the subject's view.
- Federation trio: **SAML** = XML assertions for enterprise web **SSO
  (authentication)**; **OAuth 2.0** = **delegated authorization** (access tokens, a
  "valet key"); **OIDC** = **authentication** layer on OAuth (ID token / JWT, social
  login).
- **FIDO2/WebAuthn** = passwordless, phishing-resistant passkeys; **SCIM** automates
  cross-domain provisioning.
- Federation concentrates trust in the **IdP** — protect it accordingly.
