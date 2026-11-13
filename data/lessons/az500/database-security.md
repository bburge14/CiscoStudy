# Securing Azure SQL Databases

Databases concentrate risk: one query can return millions of records. Azure SQL
(the PaaS database service) gives you a deep stack of controls across
**authentication, networking, auditing, threat detection, and encryption**. The
exam leans hard on the encryption options because three of them — **TDE, Always
Encrypted, and dynamic data masking** — sound similar but protect very different
things.

## Authentication and authorization

- **Microsoft Entra authentication (recommended)** lets users, groups, and
  **managed identities** sign in with Entra identities, so you get MFA,
  Conditional Access, and central account lifecycle. You designate an **Entra
  admin** for the server. Prefer this over SQL logins.
- **SQL authentication** uses database-local usernames and passwords — fine for
  legacy apps, but the credentials live outside Entra, so harden and rotate them.
- Inside the database, apply **least privilege** with database roles; don't hand
  applications `db_owner` when a reader or writer role suffices.

## Network isolation

Azure SQL has a public endpoint by default, so restrict it:

- **Firewall rules** — server-level and database-level rules that allow only
  specific client IP ranges. The "Allow Azure services" option is broad; prefer
  explicit rules.
- **VNet service endpoints** to trust specific subnets, or — stronger — a
  **private endpoint** so the server is reachable only at a private IP, with public
  access **disabled**.

> Beware the **"Allow Azure services and resources to access this server"** toggle:
> it opens the server to **all** Azure IPs (effectively `0.0.0.0`), including other
> tenants' resources. Leave it **off** and use explicit rules or a private
> endpoint. For full network isolation, **Azure SQL Managed Instance** deploys
> directly into your VNet subnet.

Connection policy can also force clients through a **private path** and enforce a
**minimum TLS version** on the server, so legacy, unencrypted connections are
refused.

## Auditing

**SQL auditing** records database events — logins, queries, permission changes —
to a **storage account, Log Analytics workspace, or Event Hubs**. Sending audit
logs to **Log Analytics** lets you query them with KQL and wire them into Sentinel.
Auditing is your forensic record and a common compliance requirement.

## Microsoft Defender for SQL

**Microsoft Defender for SQL** (a Defender for Cloud plan) adds two things:

- **Advanced Threat Protection** — alerts on anomalous activity like potential
  **SQL injection**, access from unusual locations, or brute-force attempts.
- **Vulnerability Assessment** — scans the database against best-practice baselines
  and reports misconfigurations and excessive permissions to remediate.

## Encryption — three controls, three jobs

This is the heart of the lesson. Keep the three straight by asking *what state of
data* each protects.

| Control | Protects data... | How | Key location |
|---------|------------------|-----|--------------|
| **Transparent Data Encryption (TDE)** | **at rest** | Encrypts the database files, backups, and logs on disk | Service-managed by default; **CMK/BYOK** in Key Vault optional |
| **Always Encrypted** | **in use** (and in transit/at rest) | Encrypts **specific columns**; data is decrypted **only on the client** | Keys held **client-side**; the engine/DBA never sees plaintext |
| **Dynamic Data Masking** | **on display** | **Obfuscates** results for unprivileged users (e.g. shows `XXXX1234`) | None — it's not encryption |

In plain terms:

- **TDE** is on by default and handles **at-rest** encryption of the whole
  database transparently — neither apps nor queries change. Bring your own key with
  **CMK** when you need to own and revoke it.
- **Always Encrypted** protects the most sensitive **columns** (SSNs, card
  numbers) so that even a **database administrator cannot read them** — decryption
  happens in the client driver with keys the server never holds. It's the answer
  when the requirement is "DBAs/Microsoft must not see the plaintext." A variant,
  **Always Encrypted with secure enclaves**, allows some in-place operations on
  encrypted data.
- **Dynamic data masking** is **not encryption** at all — the stored data is
  unchanged; it just **hides** parts of the result for users without the unmask
  permission. A determined user with query access can sometimes infer masked
  values, so treat it as a convenience, not a security boundary.
- **TLS** protects data **in transit** to and from the database.

## Finding and limiting exposure

- **Data discovery & classification** scans columns and applies **sensitivity
  labels** (e.g. Confidential, PII), so you know where sensitive data lives and can
  feed classification into auditing.
- **Row-level security (RLS)** filters which **rows** a user can see based on their
  identity — useful for multitenant data in a shared table.
- **Ledger** provides **tamper-evidence**: cryptographically chained records prove
  data hasn't been altered, for high-integrity scenarios.

## Putting it together

Authenticate with **Entra ID** (and managed identities) over SQL logins, isolate
the server with **firewall rules or a private endpoint**, and turn on **SQL
auditing** to Log Analytics. Add **Microsoft Defender for SQL** for threat alerts
and vulnerability scans. For encryption, remember the three jobs: **TDE** encrypts
**at rest** (on by default, CMK optional), **Always Encrypted** protects
**columns in use** with **client-side keys the DBA can't read**, and **dynamic
data masking** merely **hides** values on display. Layer on **classification**,
**row-level security**, and **ledger** as the data sensitivity demands.

## Exam focus

- Prefer **Microsoft Entra authentication** (with an **Entra admin** and managed
  identities) over SQL logins; apply least-privilege database roles.
- Restrict the network with **firewall rules** or a **private endpoint** (disable
  public access); send **SQL auditing** to **Log Analytics** for KQL/Sentinel.
- **Microsoft Defender for SQL** = **Advanced Threat Protection** (SQLi, anomalous
  access alerts) + **Vulnerability Assessment**.
- **TDE** = encryption **at rest** (default; **CMK** for key ownership).
- **Always Encrypted** = **column-level**, decrypted **only on the client**, so
  **DBAs/Microsoft never see plaintext** — the answer when privileged users must be
  excluded.
- **Dynamic data masking** is **not encryption** — it only **obfuscates query
  results** for unprivileged users.
- **TLS** = data in transit; **classification/labels**, **row-level security**, and
  **ledger** (tamper-evidence) round out data protection.
