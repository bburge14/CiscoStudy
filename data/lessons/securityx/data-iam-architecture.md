# Data Protection & Enterprise IAM Architecture

Two architectural pillars decide whether data stays safe when systems are
inevitably exposed: how you **protect the data itself**, and how you **control
identity and access** at the scale of thousands of users, services, and
privileged accounts. SecurityX tests both as design decisions, not product
features.

## Protecting data across its states

Data must be protected in three states, each with its own controls:

- **At rest** — stored on disk, in databases, in object storage. Protect with
  **encryption** (full-disk, file, database/TDE) and strong key management.
- **In transit** — moving across a network. Protect with **TLS 1.3**, IPsec, and
  mutual authentication.
- **In use** — loaded in memory and being processed. The hardest state; addressed
  by **confidential computing**.

### Encryption's data-protection toolkit

Beyond plain encryption, an architect chooses among techniques by *what the
business still needs to do with the data*:

- **Tokenization** — replace a sensitive value (a credit-card number) with a
  non-sensitive **token**, keeping the real value in a separate secured vault. The
  token has no mathematical relationship to the original, so a breach of the
  token store reveals nothing. Tokenization is the go-to for **removing stored card
  numbers to shrink PCI DSS scope** while staff still reference a stand-in.
- **Data masking** — obscure part of a value (show only the last four digits) so it
  can be displayed or used in lower environments without exposing the whole.
- **Anonymization** (irreversible) vs **pseudonymization** (reversible with a key) —
  used for analytics and privacy compliance.
- **Hashing** — one-way; for integrity and password storage, not for data you need
  to recover.

> **Tokenization** swaps the value for a meaningless token held elsewhere — ideal
> for taking card data out of a database to **reduce PCI scope**. **Masking** hides
> part of a value for display. They solve different problems.

### Protecting data in use: confidential computing

To run analytics on highly sensitive data in an **untrusted cloud without ever
exposing plaintext**, two advanced options appear:

- **Confidential computing** — a hardware **Trusted Execution Environment (TEE)**
  (a secure enclave) that keeps data encrypted even in memory, so the cloud
  provider cannot read it.
- **Homomorphic encryption** — allows computation **directly on ciphertext**, with
  the result decrypting to the correct answer, so plaintext never appears at all.

### Key custody: the HSM

Encryption is only as strong as key protection. A **Hardware Security Module
(HSM)** is a dedicated, tamper-resistant appliance that **generates, stores, and
protects keys** and performs crypto operations so keys never leave in plaintext.
Cloud providers offer managed HSM/KMS equivalents. For the highest assurance, keys
are generated and used inside the HSM boundary and never exported.

## Data Loss Prevention (DLP)

**DLP** inspects and controls data to prevent exfiltration. It operates at three
chokepoints: **endpoint DLP** (USB, local copy), **network DLP** (email, web
uploads), and **cloud/storage DLP** (SaaS and repositories, often via a CASB). DLP
works off **classification** and content patterns, and can block, quarantine, or
alert. It is the primary control when the concern is sensitive data *leaving* the
organization.

## Enterprise IAM architecture

IAM at enterprise scale is about **federation**, **standards-based protocols**, and
**governing privilege** — not local accounts on each app.

### The identity protocols

Know which protocol does which job; stems often pair two requirements:

| Protocol | Purpose |
|----------|---------|
| **SAML 2.0** | Browser-based **SSO** to enterprise/SaaS apps using **XML assertions** |
| **OIDC (OpenID Connect)** | Modern **authentication** layer built on OAuth 2.0 (JSON/JWT) |
| **OAuth 2.0** | Delegated **authorization** — grant an app limited, revocable access without sharing the password |
| **SCIM** | Automated **provisioning/deprovisioning** of user accounts across apps |
| **Kerberos / LDAP** | On-prem directory authentication |

> **SAML** = XML-based browser SSO; **OIDC** = modern authentication on top of
> OAuth; **OAuth** = delegated *authorization* (access, not login). If a stem wants
> "SSO to a SaaS app with XML assertions" plus "delegated API access," the pair is
> **SAML + OAuth** (with OIDC for the login layer).

### Federation and SSO

**Federated identity** lets users from one trust domain access another's resources
using their *home* identity provider (IdP). The **IdP** authenticates; the **SP
(service provider / relying party)** trusts the IdP's assertion. Benefits: users
keep one identity; the SP never stores partner passwords; deprovisioning at the IdP
revokes access everywhere. **SSO** reduces password fatigue but raises the stakes of
that one credential — so it is paired with strong **MFA**.

### Governing privilege

- **PAM (Privileged Access Management)** — vault privileged credentials, broker
  **just-in-time (JIT)** elevation with approval, enforce session recording, and
  eliminate **standing** admin access. PAM is the answer for reducing the risk of
  always-on administrative rights.
- **IGA (Identity Governance and Administration)** — lifecycle, **access reviews/
  certification**, and **separation-of-duties** policy enforcement.
- **Access models** — **RBAC** (by role), **ABAC** (by attributes/context, the most
  granular), and policy-based access complement zero trust's dynamic decisions.

> To cut the risk of **standing** admin access: vault the credentials and grant
> **just-in-time**, approval-brokered elevation with session recording — that is
> **PAM**. Periodic **access reviews/certification** are **IGA**.

## Exam focus

- Protect data **at rest** (encryption + key mgmt), **in transit** (TLS 1.3/IPsec),
  and **in use** (**confidential computing / TEE**, or **homomorphic encryption** to
  compute on ciphertext).
- **Tokenization** replaces values with vault-backed tokens to **shrink PCI scope**;
  **masking** hides part of a value for display. **HSM** = tamper-resistant key
  storage/crypto so keys never leave in plaintext.
- **DLP** stops sensitive data from leaving (endpoint/network/cloud) and keys off
  **classification**.
- Protocols: **SAML** = XML browser SSO; **OIDC** = authentication on OAuth; **OAuth
  2.0** = delegated authorization; **SCIM** = provisioning.
- **Federation**: home **IdP** authenticates, **SP** trusts the assertion; the SP
  never holds partner passwords and IdP deprovisioning revokes access everywhere.
- **PAM** = vaulting + **just-in-time** elevation to kill standing admin access;
  **IGA** = access reviews/certification and SoD enforcement; **ABAC** is the most
  granular access model.
