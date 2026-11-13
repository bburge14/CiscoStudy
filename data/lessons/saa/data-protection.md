# Data Protection: Encryption, KMS & Secrets

Securing identities controls *who* can act; data protection controls what happens
to the bytes themselves. The exam expects you to pick the right encryption model
for data at rest and in transit, to know which service holds keys versus secrets,
and to handle awkward real-world cases like encrypting a database that was created
without encryption. The guiding idea is **defense in depth**: even if a bucket is
left open, encrypted data is still unreadable.

## Encryption in transit: force TLS

Protecting data *in transit* means nothing can read it as it crosses the network.

> **To require that every request to an S3 bucket use TLS, attach a bucket policy
> that denies requests when `aws:SecureTransport` is `false`.** Plaintext HTTP
> requests are then rejected outright.

For public-facing HTTPS, you need certificates:

- **AWS Certificate Manager (ACM)** issues and *auto-renews* public TLS
  certificates and integrates directly with load balancers and CloudFront, so you
  never manually renew a cert on an ALB again. ACM public certificates are free.
- **AWS Private CA** issues certificates for *internal* domains that never touch
  the internet — ideal for mutual TLS between microservices.

## Encryption at rest with AWS KMS

**AWS Key Management Service (KMS)** is the service that creates and controls the
cryptographic keys used to encrypt data across S3, EBS, RDS, and most other
services. You rarely encrypt large data with a KMS key directly; instead KMS uses
**envelope encryption**.

> **Envelope encryption: KMS generates a *data key*, which encrypts your data
> locally; that data key is then itself encrypted by the KMS key. You store the
> encrypted data key beside the ciphertext.** This lets you encrypt gigabytes
> efficiently while a single protected key anchors the chain.

### Choosing an S3 server-side encryption mode

| Mode | Who holds the key | When to choose |
|------|-------------------|----------------|
| **SSE-S3** | S3-managed keys (default) | Simple encryption, no key control needed |
| **SSE-KMS** | A KMS key you manage | You need an **audit trail** of key use and control over rotation/access |
| **SSE-C** | Keys the **customer supplies** on each request | AWS does the crypto but you keep and send the key |

Pick **SSE-KMS with a customer managed key** when a rule requires an auditable
record (every use is logged in CloudTrail) plus control over who can use the key
and how often it rotates. Pick **SSE-C** when the requirement is that the customer
provides the key material and AWS stores none of it.

### Key rotation and multi-Region keys

- **Automatic rotation** — enable it on a customer managed key and KMS rotates the
  key material on a schedule (365 days by default, configurable) with no
  application changes; this satisfies "rotate the key once a year with least
  effort." AWS managed keys rotate automatically and are not configurable.
- **KMS multi-Region keys** — a set of keys with the same key material in several
  Regions, so data encrypted in one Region can be decrypted in another after
  cross-Region replication, without re-encrypting.

### When you need your own hardware: CloudHSM

> **AWS CloudHSM is a dedicated, single-tenant hardware security module that *you*
> fully control, meeting FIPS 140-2 Level 3.** Choose it when a regulator demands
> single-tenant, customer-controlled key hardware; choose KMS for the managed,
> multi-tenant default.

## Storing secrets and parameters

Credentials and configuration values need their own homes:

- **AWS Secrets Manager** — stores secrets and can **automatically rotate** them on
  a schedule, with built-in rotation for Amazon RDS. Choose it whenever the
  requirement includes automatic credential rotation.
- **AWS Systems Manager Parameter Store** — stores configuration values and
  encrypted `SecureString` parameters. It is the low-cost choice when you need a
  few encrypted secrets *without* automatic rotation.

The deciding word is **rotation**: needs it → Secrets Manager; a handful of static
secrets and minimize cost → Parameter Store SecureString.

## Write-once protection and integrity

Some compliance rules demand that data cannot be changed or deleted at all:

> **S3 Object Lock in compliance mode enforces write-once-read-many (WORM): for a
> fixed retention period, no one — not even an administrator or the root user —
> can overwrite or delete the object.**

This is the answer for financial or legal records that must be provably immutable.
(A parallel feature, **AWS Backup Vault Lock in compliance mode**, does the same
for backups — covered in the disaster-recovery lesson.)

## A classic gotcha: encrypting an existing unencrypted resource

You cannot simply "turn on" encryption for an already-running unencrypted RDS
instance or EBS volume. The pattern is always snapshot-and-copy:

1. Take a snapshot of the unencrypted resource.
2. **Copy the snapshot with encryption enabled**, choosing a KMS key.
3. Restore a new, encrypted instance or volume from the encrypted copy.
4. Cut over to the new resource.

Memorize this sequence — the exam loves to test that encryption is set at
creation, so the fix is to create a fresh encrypted copy.

## Keeping the services straight

A short analogy: think of **KMS** as the locksmith who makes and guards keys,
**Secrets Manager** as a safe that automatically changes its combination on a
schedule, **Parameter Store** as a cheap labeled drawer, **ACM** as the notary that
issues and renews your public ID cards, and **CloudHSM** as your own private vault
that only you can open.

## Exam focus

- Force TLS to S3 → **bucket policy denying `aws:SecureTransport = false`**. Public
  HTTPS certs that auto-renew → **ACM**; internal certs → **AWS Private CA**.
- **KMS** makes and controls keys and uses **envelope encryption** (a data key
  encrypts the data; the KMS key encrypts the data key).
- **SSE-KMS** = auditable, controllable key use (logged in CloudTrail);
  **SSE-C** = customer supplies the key each request; **SSE-S3** = simple default.
- **Enable automatic key rotation** on a customer managed key for low-effort annual
  rotation. **Multi-Region keys** let you decrypt replicated data in another Region.
- **CloudHSM** = single-tenant, customer-controlled HSM, FIPS 140-2 Level 3.
- **Secrets Manager** rotates secrets automatically (RDS integration); **Parameter
  Store SecureString** is the cheaper option when rotation is not required.
- **S3 Object Lock (compliance mode)** = immutable WORM storage for a retention
  period.
- Encrypt an existing unencrypted RDS/EBS → **snapshot, copy with encryption,
  restore**.
