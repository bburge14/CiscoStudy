# Securing Azure Storage

A storage account can hold an organization's most sensitive data — backups,
documents, telemetry — behind a single public endpoint and a pair of all-powerful
keys. Securing it means controlling **how clients authorize**, **how you encrypt**,
and **which networks can even reach it**. SAS tokens and the storage firewall are
the two areas AZ-500 tests hardest.

## Authorizing access: three models

A request to blob or queue data can be authorized three ways, from strongest to
weakest:

- **Microsoft Entra ID (recommended)** — the caller (user or **managed identity**)
  presents an Entra token and is authorized by **Azure RBAC data roles** such as
  **Storage Blob Data Reader** or **Storage Blob Data Contributor**. No shared
  secret to leak, full audit trail, and you can disable the alternatives.
- **Shared Key** — the account's two **access keys** grant **full control** of the
  entire account. They are the "root password" of storage: rotate them (keep two
  so you can roll one while the other serves), store them only in Key Vault, and
  ideally **disable shared-key access** so everything must use Entra.
- **Shared access signatures (SAS)** — delegated, scoped, time-limited URLs,
  covered next.

## Shared access signatures (SAS)

> A **SAS** is a signed URL that grants **limited, time-bound** access to storage
> without revealing an account key. You choose exactly which services, resource
> types, permissions, time window, and (optionally) source IPs and protocol it
> allows.

There are three kinds, and the exam cares about the distinction:

| SAS type | Signed by | Notes |
|----------|-----------|-------|
| **User delegation SAS** | An **Entra ID** credential (not the account key) | **Recommended** for blobs; revoke by revoking the delegation key; auditable |
| **Service SAS** | Account key | Grants access to one service (e.g. Blob) |
| **Account SAS** | Account key | Broadest — can span services and account-level operations |

Because a SAS is hard to recall once issued, follow the rules:

- **Short expiry** and the **least permission** needed.
- **HTTPS only**, and restrict to specific **source IPs** where possible.
- Prefer the **user delegation SAS** (Entra-backed) so it isn't tied to a key.
- For service SAS, attach a **stored access policy** to the container — it lets you
  **revoke or change** the SAS after the fact by editing the policy, something a
  standalone SAS can't offer.

> **To revoke a leaked SAS:** rotate the signing key (for key-based SAS) or revoke
> the user delegation key, or edit/delete the **stored access policy** it's tied
> to. This is a favorite exam scenario.

## Encryption at rest

All Azure Storage is **encrypted at rest by default** with **256-bit SSE** and
**platform-managed keys** — there is no "unencrypted" option. You can escalate:

- **Customer-managed keys (CMK)** in **Key Vault** for key ownership, rotation,
  and revocation.
- **Infrastructure encryption** — an optional second layer (double encryption at
  rest) for strict compliance, enabled at account creation.

## The storage firewall and secure networking

By default a storage account accepts traffic from any network. Lock it down:

- Switch **public network access** to **Disabled** or to **Selected networks**,
  which **denies by default** and then allows only what you add.
- Allow specific **VNets/subnets** (via **service endpoints**) or — the strongest
  option — add a **private endpoint** so the account is reachable only at a private
  IP in your VNet (see the networking unit).
- Allow trusted **Azure services** (the "trusted Microsoft services" exception) and
  specific **resource instances** when a platform service needs in.

Two more transport and access toggles matter:

- **Secure transfer required** forces **HTTPS** (rejects plaintext HTTP), and you
  can set a **minimum TLS version**.
- **Disable anonymous blob public access** at the account level so no container can
  be made world-readable by accident — a frequent cause of data leaks.

## Protecting against deletion and tampering

- **Soft delete** (for blobs, containers, and file shares) retains deleted data for
  a retention period so you can recover from accidental or malicious deletion.
- **Immutable storage (WORM)** enforces write-once-read-many with **time-based
  retention** or a **legal hold**, so data can't be modified or deleted until the
  policy allows — important for compliance and ransomware resilience.
- **Versioning** keeps previous versions of blobs.

## Putting it together

Authorize with **Entra ID and RBAC data roles** wherever you can, treat the
**account keys** as root secrets (rotate, or disable entirely), and when you must
delegate, issue **scoped, short-lived SAS** — ideally **user delegation SAS**, with
**stored access policies** so you can revoke them. Storage is always **encrypted at
rest**; add **CMK** or **infrastructure encryption** for more control or layers.
Put the account behind the **storage firewall** (deny public access, allow
specific VNets or a **private endpoint**), force **HTTPS**, block **anonymous
public access**, and guard the data itself with **soft delete** and **immutable
(WORM)** policies.

## Exam focus

- Authorization models: **Entra ID + RBAC data roles (best)** > **SAS** (scoped,
  temporary) > **Shared Key** (full account control — rotate or disable).
- **User delegation SAS** is signed by **Entra ID** (not an account key) and is the
  recommended SAS; **service/account SAS** are key-signed. SAS best practices:
  **short expiry, least permission, HTTPS only, IP limits**.
- **Revoke a SAS** by rotating/revoking the signing key or editing the **stored
  access policy** it's bound to.
- Storage is **always encrypted at rest (SSE, 256-bit)**; add **CMK** (Key Vault)
  for key control and **infrastructure encryption** for a second layer.
- **Storage firewall**: set public access to **Disabled/Selected networks** (deny
  by default), allow **VNets (service endpoints)** or a **private endpoint**, plus
  trusted services.
- Enforce **secure transfer (HTTPS)** and **minimum TLS**, and **disable anonymous
  public blob access**. Use **soft delete** and **immutable WORM** (time-based
  retention / legal hold) to resist deletion and tampering.
