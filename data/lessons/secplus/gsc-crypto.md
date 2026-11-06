# Cryptographic Solutions & PKI

Cryptography sounds like heavy math, but for Security+ it's really a toolbox of a
dozen ideas you can explain in plain words. Get the handful of core concepts
straight — what scrambles data, what proves it wasn't changed, and how we trust a
stranger's key — and the rest clicks into place.

## Two families of encryption

**Encryption** scrambles readable data (**plaintext**) into unreadable
**ciphertext** using a **key**. There are two families, and the whole exam hinges
on telling them apart.

> **Symmetric** encryption uses **one shared key** for both locking and
> unlocking. **Asymmetric** encryption uses a **key pair** — a public key and a
> private key that are mathematically linked.

- **Symmetric** — fast, great for bulk data, but how do you get the one key to the
  other side safely? That's the **key exchange** problem. Example algorithm:
  **AES** (with key lengths like 128 or 256 bits).
- **Asymmetric** — slower, but solves key exchange elegantly. Anyone can encrypt
  to you with your *public* key; only your *private* key can decrypt. Example:
  **RSA**, and **ECC** (elliptic curve, which gets strong security from shorter
  keys — handy for phones and IoT).

The usual real-world trick is to use both: asymmetric crypto to safely exchange a
symmetric key, then fast symmetric crypto for the actual data. That's exactly what
happens when your browser sets up a TLS connection.

A quick word on **key length**: longer keys are exponentially harder to brute
force. But you can't compare key lengths *across* families — a 256-bit AES
(symmetric) key and a 2048-bit RSA (asymmetric) key are both "strong"; the numbers
aren't meant to be compared directly.

## Where you can apply encryption

Encryption isn't one setting — you choose the **level**:

| Level | What it protects |
|-------|------------------|
| **Full-disk** | The entire drive (e.g. BitLocker) |
| **Partition / volume** | A specific section of a disk |
| **File** | Individual files |
| **Database** | A whole database |
| **Record** | A single row/field inside a database |

You also encrypt data **in transit** — **transport/communication** encryption
like TLS protecting traffic on the wire.

## Hashing: proving data hasn't changed

**Hashing** is *not* encryption. A hash function takes any input and produces a
fixed-length **fingerprint**. It's **one-way** — you can't reverse a hash back
into the original.

> If even one character of the input changes, the hash changes completely. That's
> what makes hashing the tool for **integrity**: compare the before and after
> hash, and if they match, nothing was altered.

Common algorithm: **SHA-256**. (MD5 and SHA-1 still appear but are considered
broken for security use because of collisions — more on that below.)

Two companions to hashing:

- **Salting** — adding a random value to a password *before* hashing it, so two
  users with the same password get different hashes and precomputed
  ("rainbow table") attacks fail.
- **Key stretching** — deliberately slow, repeated hashing (e.g. PBKDF2, bcrypt)
  so that guessing passwords is painfully slow for an attacker.

## Digital signatures: integrity + authenticity + non-repudiation

A **digital signature** combines hashing and asymmetric crypto to do three things
at once. The signer hashes the message, then encrypts that hash with their
**private key**. Anyone can verify it using the signer's **public key**.

Because only the signer has the private key, a valid signature proves:

1. **Integrity** — the hash matches, so nothing was changed.
2. **Authenticity** — it genuinely came from the signer.
3. **Non-repudiation** — the signer can't deny it.

Note the direction: you **sign with the private key** and **verify with the
public key**. (To keep something *secret* you do the opposite — encrypt with the
recipient's public key.) Mixing up which key does what is the single most common
crypto mistake on the exam.

## Hiding data in other ways: obfuscation

Sometimes you don't encrypt, you **obfuscate** — make data less useful if seen:

- **Steganography** — hiding data *inside* something else, like a message tucked
  into an image file.
- **Tokenization** — replacing sensitive data with a meaningless **token**; the
  real value lives in a separate secure vault. Common for credit card numbers.
- **Data masking** — showing only part of a value, like `****-****-****-1234`.

## Where keys and secrets live: crypto tools

- **TPM (Trusted Platform Module)** — a chip *on the motherboard* of a single
  device that stores keys and supports full-disk encryption.
- **HSM (Hardware Security Module)** — a dedicated, often removable/networked
  appliance for generating and storing keys at scale for an organization.
- **Key Management System (KMS)** — software that handles the lifecycle of keys
  (creation, rotation, retirement).
- **Secure enclave** — an isolated processor region that guards secrets even from
  the main OS.

A handy distinction: **TPM = one device's chip**, **HSM = the organization's
key appliance**.

## Blockchain: an open, tamper-evident ledger

**Blockchain** is a distributed **open public ledger** where each block of records
is chained to the previous one by a hash. Because changing any block would break
every hash after it, the record becomes practically tamper-evident. It's the tech
behind cryptocurrencies, but the exam cares about the *properties*: distributed,
hash-linked, and resistant to quiet alteration.

## PKI: trusting a stranger's key

Asymmetric crypto only works if you can trust that a public key really belongs to
who it claims. **Public Key Infrastructure (PKI)** is the whole system of
authorities, certificates, and rules that makes that trust possible.

The core pieces:

- **Public key / private key** — the pair at the heart of it all. The public key
  is shared freely; the private key is guarded.
- **Key escrow** — a trusted third party holds a copy of keys so data isn't lost
  if a key is — a convenience that's also a risk if the escrow is compromised.

### Certificates and the authorities behind them

A **digital certificate** binds a public key to an identity, vouched for by a
**Certificate Authority (CA)**:

- **CA (Certificate Authority)** — the trusted issuer that signs certificates.
- **Root of trust** — the top CA everyone implicitly trusts; its root certificate
  anchors the whole chain.
- **Self-signed certificate** — signed by its own creator, not a trusted CA. Fine
  for internal/testing use; browsers warn on it for public sites.
- **Third-party certificate** — issued by a recognized public CA that browsers
  already trust.
- **Wildcard certificate** — covers a domain and all its subdomains at once
  (`*.example.com`).

### Getting and checking certificates

- **CSR (Certificate Signing Request)** — you generate a key pair and send the CA
  a CSR containing your public key and details; the CA returns a signed
  certificate. Your private key never leaves your hands.
- **CRL (Certificate Revocation List)** — a published list of certificates that
  have been revoked (compromised or no longer valid).
- **OCSP (Online Certificate Status Protocol)** — a faster, real-time way to ask
  "is this one certificate still valid?" instead of downloading the whole CRL.

> When a certificate is compromised, it must be **revoked**. Clients then learn
> it's dead either by checking the **CRL** (the full list) or by querying **OCSP**
> (one certificate, right now).

## The whole thing in one paragraph

Encryption comes in two families — **symmetric** (one shared key, fast, e.g. AES)
and **asymmetric** (a public/private key pair, solves key exchange, e.g. RSA/ECC)
— and you can apply it at many **levels** (full-disk, partition, volume, file,
database, record) and in transit. **Hashing** is one-way and proves **integrity**,
strengthened by **salting** and **key stretching**; a **digital signature**
(sign with the private key, verify with the public key) adds integrity,
authenticity and non-repudiation. You can also **obfuscate** with steganography,
tokenization or masking, and store keys in a **TPM** (one device), an **HSM**
(the org's key appliance), a **KMS** or a **secure enclave**. **Blockchain** is a
hash-linked public ledger. And **PKI** makes public keys trustworthy through
**CAs** issuing **certificates** (requested via a **CSR**, revoked via **CRL** or
checked via **OCSP**), all anchored to a **root of trust**.

## On the exam

- The #1 trap: **sign with the private key, verify with the public key**; to keep
  something *confidential*, encrypt with the recipient's **public key** and they
  decrypt with their **private key**. Slow down and name the goal first.
- **Hashing ≠ encryption.** Hashing is one-way and about **integrity**;
  encryption is reversible and about **confidentiality**.
- **Salting** defeats rainbow tables; **key stretching** slows down brute-force
  guessing. Don't confuse the two.
- **TPM** is a chip on one device's motherboard; an **HSM** is a separate
  appliance for the organization. "Each laptop's drive encryption key" → TPM;
  "central key storage for thousands of keys" → HSM.
- Revoked certificates are checked via **CRL** (whole list, can be stale) or
  **OCSP** (single cert, real time).
- A **wildcard** cert = one domain plus all subdomains. A **self-signed** cert =
  no external CA, hence the browser warning.
- **Tokenization** replaces data with a token stored in a vault; **masking** just
  hides part of it; **steganography** hides data inside other files.
