# Azure Key Vault

Secrets sprinkled through code and config files are how breaches spread. **Azure
Key Vault** is the central, access-controlled, audited home for the three things
applications must never hardcode: **keys, secrets, and certificates**. It is also
the backing store for the customer-managed keys that encrypt storage, disks, and
SQL — so it quietly sits under much of the rest of this unit.

## What a vault holds

- **Keys** — cryptographic keys (RSA, EC) used for encryption, signing, and
  **wrapping** other keys. Keys can be generated in the vault and never exported.
- **Secrets** — arbitrary sensitive strings: passwords, connection strings, API
  keys.
- **Certificates** — X.509 certs, with lifecycle management and optional
  integration with certificate authorities for issuance and renewal.

## Standard, Premium, and Managed HSM

Protection level is a choice:

- **Standard** — keys protected in **software**.
- **Premium** — keys protected by **hardware security modules (HSMs)**, validated
  to **FIPS 140-2 Level 2**.
- **Azure Managed HSM** — a **single-tenant**, fully managed HSM pool validated to
  **FIPS 140-3 Level 3**, for strict regulatory or high-assurance needs.

Pick Premium or Managed HSM when compliance requires hardware-backed keys.

## The two permission models — know this cold

Historically Key Vault had its own access control. Today there are **two models**,
and choosing correctly is a frequent exam item.

> - **Azure RBAC (recommended)** uses the same role-based system as the rest of
>   Azure, works across the **control plane *and* data plane**, and supports
>   **granular, scoped** roles.
> - **Vault access policies (legacy)** are a Key-Vault-specific list that grants
>   **data-plane** permissions **for the whole vault** — you can't scope to a
>   single secret.

| | **Azure RBAC** | **Access policies (legacy)** |
|---|---|---|
| Scope | Management group → … → **individual secret/key** | Whole vault only |
| Planes | Control **and** data plane | Data plane only |
| Granularity | Fine (specific roles, specific objects) | Coarse (permission lists) |
| Status | **Recommended**; now the default model for new vaults | Legacy, still supported |

Common RBAC data-plane roles:

- **Key Vault Secrets User** — read secret *values* (what an app's managed identity
  usually needs).
- **Key Vault Secrets Officer** — manage secrets (create/delete), without managing
  access.
- **Key Vault Crypto User / Officer** — use / manage keys.
- **Key Vault Administrator** — full data-plane control.

A clean pattern: give an application a **managed identity**, assign it **Key Vault
Secrets User** on the vault (or a single secret), and let it fetch secrets at
runtime — **no credential stored anywhere**, least privilege, fully audited.

## Protecting the vault from deletion

Two safety features defend against accidental or malicious deletion:

- **Soft delete** retains deleted vaults and objects for a **retention period**
  (default 90 days) so they can be recovered. It is **on by default and can no
  longer be disabled**.
- **Purge protection** goes further: while enabled, a soft-deleted vault or object
  **cannot be permanently purged** until its retention period elapses — even an
  administrator can't force it. Enable this for vaults holding CMKs so an attacker
  (or mistake) can't destroy the keys your encrypted data depends on.

## Network and monitoring

- **Networking** — restrict the vault firewall to selected networks, add a
  **private endpoint** for private-only access, and allow **trusted Azure
  services** where a platform service needs the vault (e.g. a disk encryption set).
- **Logging** — send **diagnostic logs** to **Log Analytics** to record every
  access and operation (who read which secret, when). This is essential for audit
  and for Sentinel detections.
- **Microsoft Defender for Key Vault** — a Defender for Cloud plan that alerts on
  unusual or suspicious vault access.

## Key lifecycle

- **Rotation** — rotate keys and secrets regularly; Key Vault supports **automated
  key rotation** policies and notifications before expiry.
- **Versioning** — every update creates a new **version**; apps can pin a version
  or always take the latest.
- **Expiration and activation dates** — set validity windows so stale material is
  rejected.

## Putting it together

Key Vault centralizes **keys, secrets, and certificates** behind strong access
control and auditing, with **Standard**, **Premium (HSM)**, or **Managed HSM**
protection by assurance level. Prefer the **Azure RBAC** permission model — it
spans control and data planes and scopes down to a single object — over **legacy
access policies**; grant apps a **managed identity** with a narrow role like **Key
Vault Secrets User**. Defend the vault with **soft delete** (always on) and **purge
protection**, lock down the network with a **private endpoint**, log every access
to **Log Analytics**, watch it with **Defender for Key Vault**, and manage the
**rotation and expiry** of everything it holds.

## Exam focus

- Key Vault stores **keys, secrets, and certificates**. **Premium = HSM-backed
  (FIPS 140-2 Level 2)**; **Managed HSM = single-tenant, FIPS 140-3 Level 3**.
- **Two permission models: Azure RBAC (recommended)** vs **access policies
  (legacy)**. RBAC spans **control + data plane** and is **granular/scoped**;
  access policies are **data-plane, whole-vault** only. RBAC is now the default for
  new vaults.
- Key RBAC role: **Key Vault Secrets User** lets an identity **read secret
  values** — the usual grant for an app's **managed identity** (least privilege, no
  stored credential).
- **Soft delete** is **on by default and can't be disabled**; **purge protection**
  prevents permanent deletion during retention — enable it for vaults holding CMKs.
- Lock down access with a **private endpoint**, allow **trusted services**, and
  send **diagnostic logs to Log Analytics**; add **Defender for Key Vault** for
  alerts.
- Support **rotation, versioning, and expiry**; Key Vault is the store for **CMK**
  used by storage, disks, and SQL.
