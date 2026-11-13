# Identity, Access Management & Data Security

Security in the cloud starts with two questions: *who are you and what may you do?*
(identity and access management) and *how do we protect the data itself?* (data
security). Because the customer always owns identity configuration and data under
the shared responsibility model, these are the two areas where cloud breaches most
often originate — and where the exam spends the most time.

## Authentication vs. authorization

Keep these straight; the whole domain hangs on the distinction.

> **Authentication** proves *who you are* (a login, a token, a certificate).
> **Authorization** decides *what you're allowed to do* once authenticated.
> **Accounting / auditing** records what you did. Together: AAA.

Authentication strength comes from **factors**: something you *know* (password),
something you *have* (a phone, a hardware token), something you *are* (biometrics).
Combining two different factors is **multi-factor authentication (MFA)** — the
single highest-value control for cloud accounts, because a stolen password alone
is then useless.

## Managing access

Cloud IAM models access with a few building blocks:

- **Users** are individual identities; **groups** collect users so you assign
  permissions once.
- **Roles** are sets of permissions that can be *assumed* temporarily — the
  preferred way to grant access to workloads and to humans, because the
  credentials are short-lived rather than long-standing keys.
- **Policies** are the documents that state which actions are allowed on which
  resources.
- **Service accounts / machine identities** let applications and instances
  authenticate without a human, ideally via an assumed role, not an embedded key.

### Access control models

- **RBAC (role-based)** — permissions follow a job role (a "billing-admin" role).
  Simple and the cloud default.
- **ABAC (attribute-based)** — decisions use attributes (department, resource tag,
  time, location), allowing fine-grained, dynamic rules.
- Older models to recognize: **DAC** (owner sets permissions) and **MAC**
  (system-enforced labels, used in high-security environments).

### Principles that keep access safe

- **Least privilege** — grant only the permissions needed for the task, nothing
  more. The default should be *deny*.
- **Separation of duties** — split sensitive actions so no single person can
  complete a risky process alone (one requests, another approves).
- **Just-in-time (JIT) access** and **PAM (privileged access management)** — grant
  elevated rights only for the moment they're needed and record their use, instead
  of standing admin access.

### Federation and SSO

- **SSO (single sign-on)** lets a user authenticate once and reach many apps.
- **Federation** trusts identities from another identity provider (IdP) so users
  sign in with their existing corporate account. The protocols: **SAML** (classic
  enterprise web SSO), **OIDC** (OpenID Connect, modern identity on top of OAuth),
  and **OAuth 2.0** (delegated *authorization* — granting an app limited access
  without sharing a password). Note OAuth handles authorization/delegation; OIDC
  adds the authentication layer.

## Protecting the data

Data must be protected in each of its **states**, and you encrypt accordingly.

> **At rest** — stored on disk, in a database, or in object storage. Protect with
> **encryption at rest**. **In transit** — moving across a network. Protect with
> **TLS** (encryption in transit). **In use** — loaded in memory/CPU; protected
> with emerging **confidential computing** (secure enclaves).

### Encryption building blocks

- **Symmetric** encryption uses one shared key (AES) — fast, used to encrypt the
  bulk data. **Asymmetric** uses a public/private key pair (RSA, ECC) — used for
  key exchange and digital signatures.
- **TLS** secures data in transit and relies on **certificates** issued by a
  trusted CA; certificate **expiry and renewal** must be automated or outages
  follow.
- **KMS (key management service)** creates, stores, rotates, and controls access to
  encryption keys. A hardware-backed **HSM (hardware security module)** offers the
  highest assurance. **BYOK (bring your own key)** lets the customer supply/control
  the key material rather than trusting a provider-generated key.
- **Key rotation** regularly replaces keys to limit exposure if one is
  compromised.

### Other data protections

- **Data classification** labels data by sensitivity (public, internal,
  confidential, restricted) so controls match risk — the starting point for
  everything else.
- **DLP (data loss prevention)** inspects and blocks sensitive data from leaving
  (a credit-card number in an outbound email or upload).
- **Tokenization** swaps sensitive values for meaningless tokens (common for PCI
  card data); **masking** hides part of a value (`****-1234`) for display. Both
  reduce how much real sensitive data is exposed.

## Exam focus

- **Authentication = who you are; authorization = what you may do; accounting =
  what you did.** **MFA** (two different factors) is the top control for cloud
  accounts.
- Prefer **roles with temporary credentials** over long-lived keys; use **groups**
  to assign permissions once. **RBAC** = permissions by job role (cloud default);
  **ABAC** = decisions by attributes/tags.
- **Least privilege** (default deny) and **separation of duties** are core
  principles; **JIT/PAM** replaces standing admin access.
- **SAML** = enterprise web SSO, **OIDC** = modern authentication (on OAuth),
  **OAuth 2.0** = delegated authorization. **SSO** = sign in once; **federation** =
  trust an external IdP.
- Data states: **at rest** (encrypt at rest), **in transit** (TLS), **in use**
  (confidential computing). **Symmetric/AES** for bulk data, **asymmetric/RSA** for
  key exchange and signatures.
- **KMS** manages keys (HSM = highest assurance; **BYOK** = customer-controlled
  key); **rotate** keys regularly. **Classification** drives controls; **DLP**
  blocks exfiltration; **tokenization/masking** reduce exposure of real values.
