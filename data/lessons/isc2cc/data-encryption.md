# Data Security & Encryption Basics

Data is the asset most organizations care about most, and encryption is the tool
we lean on hardest to protect it. This lesson covers how to protect data through
its **states** and its **disposal**, and then the **encryption basics** — symmetric
versus asymmetric, digital signatures, and hashing — that make confidentiality and
integrity possible. You don't need the math, just the concepts and the distinctions.

## The three states of data

To protect data, you first have to know *where* it is, because each state needs a
different protection.

> Data exists in three states: **at rest** (stored), **in transit** (moving over
> a network), and **in use** (loaded in memory and actively being processed).

- **Data at rest** — sitting in storage: on a hard drive, in a database, or on a
  backup tape, not currently moving or being processed. Protected mainly by
  **encryption** (e.g., full-disk encryption) and access controls.
- **Data in transit (in motion)** — moving across a network, such as a file being
  uploaded from a laptop to a cloud server. Protected by **encrypting the
  connection** (TLS/HTTPS, VPNs).
- **Data in use** — loaded into a computer's memory (RAM) and actively read or
  processed by an application. This is the hardest to protect, since the data must
  be decrypted to be worked on.

A single file passes through all three: encrypted on disk (at rest), encrypted as
it travels (in transit), and briefly exposed in memory while an app uses it (in
use).

## Data classification

> **Data classification** is the practice of labeling information by sensitivity —
> for example **Public**, **Internal**, and **Confidential** — so each category
> gets the appropriate level of protection.

Classification tells everyone how carefully to handle a given piece of data. You
don't spend the same effort guarding a public brochure as you do a file of
customer Social Security numbers. Classification drives the controls applied to
the data.

## Data Loss Prevention (DLP)

> **Data Loss Prevention (DLP)** is technology that inspects data leaving the
> organization — outbound email, file uploads, USB transfers — and **blocks
> sensitive data** (like credit-card or Social Security numbers) from getting out.

DLP enforces classification in real time: if someone tries to email a spreadsheet
full of card numbers, DLP can stop it. It's a key control against both accidental
leaks and malicious exfiltration.

## Securely disposing of data

When storage media reach end of life, deleting files is **not** enough — the data
is still recoverable. Sensitive media must be sanitized or destroyed:

- **Physical destruction** — shredding, pulverizing, or incinerating the drive.
  This most reliably ensures the data can never be recovered.
- **Degaussing** — exposing a **magnetic** hard drive to a powerful magnetic field
  that scrambles the stored data. (Degaussing works on magnetic media; it does
  nothing to solid-state drives.)

> Simply deleting or formatting leaves data recoverable. For sensitive media,
> **destroy or degauss** it, and for high-value assets get a certificate of
> destruction as proof.

## Encryption basics

> **Encryption** transforms readable **plaintext** (also called cleartext) into
> unreadable **ciphertext** using an algorithm and a key, so that only someone
> with the right key can read it. Its primary goal is **confidentiality**.

There are two families of encryption, and the difference is all about the keys.

### Symmetric encryption

> **Symmetric** encryption uses a **single shared secret key** to both encrypt and
> decrypt. It is fast, making it ideal for large volumes of data.

The classic algorithm is **AES (Advanced Encryption Standard)**. The catch:
everyone who needs to read the data must share the same secret key, and getting
that key to them securely (key distribution) is the hard part.

### Asymmetric (public-key) encryption

> **Asymmetric** encryption uses a **matched pair of keys** — a **public key** and
> a **private key**. What one key encrypts, only the other can decrypt.

The classic algorithm is **RSA**. The public key can be shared freely; the private
key is kept secret. This solves the key-distribution problem but is slower than
symmetric, so in practice the two are combined (asymmetric to exchange a key,
symmetric for the bulk data).

**For confidentiality:** you publish your **public key**; others use it to encrypt
a message that **only you can decrypt with your matching private key**. Encrypt to
the recipient's *public* key; they decrypt with their *private* key.

### Digital signatures

Asymmetric keys also work in reverse to *prove* who sent something:

> A **digital signature** is created with the sender's **private key** and verified
> by anyone with the sender's **public key**. A valid signature proves
> **integrity** (the message wasn't altered) and **origin/authenticity**, and
> provides **non-repudiation** — the sender can't credibly deny signing it.

Note the key usage flips depending on the goal: encrypt *to* someone with their
**public** key (confidentiality); sign *as* yourself with your **private** key
(integrity and non-repudiation).

### Hashing

> **Hashing** produces a fixed-length, **irreversible** "fingerprint" of data. It
> uses **no key** and cannot be reversed to recover the original.

A hash (e.g., SHA-256) lets you detect change: if even one bit of a file changes,
its hash changes, so hashing protects **integrity**, not confidentiality. Hashing
is *not* encryption — there's no key and no way to get the data back from the hash.

### Encryption vs. hashing in one line

- **Encryption** (reversible, uses a key) protects **confidentiality**.
- **Hashing** (irreversible, no key) protects **integrity**.

## Exam focus

- Three data states: **at rest** (stored), **in transit** (moving on a network),
  **in use** (in memory being processed). Encrypt at rest and in transit.
- **Data classification** labels data by sensitivity (Public/Internal/
  Confidential). **DLP** inspects outbound data and blocks sensitive info from
  leaving.
- Secure disposal: **physical destruction** (shred/pulverize) or **degaussing**
  (magnetic media). Deleting/formatting is *not* secure erasure.
- **Symmetric** = one shared key, fast, **AES**. **Asymmetric** = public/private
  key pair, **RSA**. Encrypt for confidentiality with the recipient's **public**
  key.
- **Digital signature**: sign with your **private** key, verify with your
  **public** key → integrity, authenticity, **non-repudiation**.
- **Hashing** = keyless, irreversible fingerprint for **integrity**. Encryption
  protects **confidentiality**; hashing protects **integrity**.
