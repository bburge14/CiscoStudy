# Encryption, Hashing & Governance

This lesson pairs two things every security professional leans on daily. First,
the math that keeps secrets secret: **encryption** and **hashing**. Second, the
management discipline that keeps an organization honest: **governance, risk, and
compliance (GRC)**. One protects the bytes; the other protects the behavior.

## Encryption: scrambling data so only the right people can read it

> **Encryption** converts readable data (*plaintext*) into unreadable data
> (*ciphertext*) using an algorithm and a **key**. Only someone with the correct
> key can reverse the process and read the original.

There are two families of encryption, and the whole difference is about keys.

### Symmetric encryption

**Symmetric** encryption uses **one shared secret key** to both encrypt and
decrypt. It is fast and great for large amounts of data, but it has a catch: both
sides must already share the same key, and getting that key to the other party
safely is hard.

- Same key locks and unlocks — like a single house key you must copy and hand to
  anyone who needs in.
- Common example: **AES** (Advanced Encryption Standard).

### Asymmetric encryption

**Asymmetric** encryption uses a **key pair**: a **public key** and a
**private key** that are mathematically linked. What one key locks, only the
other can unlock.

- You can hand your **public key** to the world. Anyone encrypts a message to you
  with it, and only **your private key** can decrypt it — solving the key-sharing
  problem.
- It is slower than symmetric, so in practice the two are combined: asymmetric
  encryption safely exchanges a symmetric key, which then does the bulk work.
- This key-pair idea underpins **certificates**, **TLS/HTTPS**, and digital
  signatures.

| | Symmetric | Asymmetric |
|---|-----------|------------|
| Keys | One shared secret | Public + private pair |
| Speed | Fast | Slower |
| Main challenge | Sharing the key safely | Slower, more overhead |
| Typical use | Bulk data encryption | Key exchange, signatures, certificates |

### The three states of data

You encrypt data differently depending on what it is doing:

- **At rest** — stored on a disk, in a database, in a blob. (Protected by storage
  or disk encryption.)
- **In transit** — moving across a network, e.g. your browser to a web server.
  (Protected by **TLS**, which gives you HTTPS.)
- **In use** — loaded in memory and actively being processed. (The hardest to
  protect; technologies like confidential computing address it.)

## Hashing: a one-way fingerprint

Hashing looks similar to encryption but does a completely different job, and the
exam loves to test the difference.

> **Hashing** runs data through a one-way function to produce a fixed-length
> value (a **hash**). It **cannot be reversed** back to the original, and there
> is **no key**. The same input always produces the same hash.

Because it cannot be undone, hashing is not for data you need to read back. Its
jobs are:

- **Password storage** — systems store the *hash* of your password, not the
  password. At sign-in they hash what you typed and compare. A stolen hash file
  does not hand the attacker the actual passwords.
- **Integrity checking** — hash a file now and later; if the two hashes differ,
  the file changed. This is how integrity (the "I" in CIA) is verified.

The clean contrast: **encryption is two-way (with a key); hashing is one-way
(no key).** A salted hash adds a random value so two identical passwords do not
produce the same stored hash.

## Governance, Risk, and Compliance (GRC)

Technology alone does not make an organization secure — people and processes do.
**GRC** is the management framework that directs security from the top. The exam
tests the three distinct functions, so learn exactly what each one means.

> - **Governance** is the system of **rules, policies, standards, roles and
>   processes** by which leadership *directs and controls* the organization.
> - **Risk management** is the process of **identifying, assessing and treating**
>   threats to the organization.
> - **Compliance** is **adhering to the laws, regulations and standards** that
>   apply to the organization.

### Governance

Governance answers "who decides, and by what rules?" It is leadership setting
direction: writing the information-security policy, defining standards, assigning
responsibilities, and making sure security supports the business's goals. If a
scenario describes **setting policies and standards that direct how security is
run**, that is governance.

### Risk management

Risk management answers "what could go wrong, and what do we do about it?" You
**identify** potential threats, **assess** each one's likelihood and impact, then
choose how to **treat** it. The four classic responses:

- **Mitigate** — reduce the risk with a control (e.g. add MFA).
- **Transfer** — shift it to someone else (e.g. buy insurance).
- **Avoid** — stop the risky activity entirely.
- **Accept** — acknowledge it and live with it (for low risks).

### Compliance

Compliance answers "are we following the rules imposed on us?" Those rules come
from **outside** the organization and carry legal weight — for example **GDPR**
(EU personal data), **HIPAA** (US healthcare data), **ISO 27001**, or **PCI
DSS**. Confirming that your controls satisfy such a regulation is compliance.
Microsoft offers **Microsoft Purview** and the **Service Trust Portal** to help
organizations manage and demonstrate compliance — more on those in Unit 4.

A quick way to keep the three straight: **governance sets the rules, risk
management weighs the dangers, compliance proves you met external obligations.**

## The whole thing in one paragraph

**Symmetric** encryption uses one shared key (fast, but key-sharing is hard);
**asymmetric** uses a public/private key pair (solves key sharing, powers
certificates and TLS); and you protect data **at rest, in transit and in use**.
**Hashing** is a one-way, keyless fingerprint used for password storage and
integrity checks — it cannot be reversed. On the management side, **GRC** splits
into **governance** (leadership's rules and direction), **risk management**
(identify, assess and treat threats), and **compliance** (meeting external laws
and regulations such as GDPR and HIPAA).

## Exam focus

- **Symmetric = one shared key** (fast, bulk data). **Asymmetric = public +
  private key pair** (key exchange, certificates, signatures). What the public
  key encrypts, only the matching private key decrypts.
- **Hashing is one-way and keyless** — used for **password storage** and
  **integrity**. If the question says "cannot be reversed" or "store passwords
  safely," the answer is hashing, not encryption.
- Know the **three data states**: **at rest, in transit, in use**. TLS protects
  data **in transit** (HTTPS).
- **GRC = Governance, Risk, Compliance.** Governance **directs and controls**
  (policies/standards/roles); risk management **identifies, assesses and treats**
  threats; compliance **meets external laws/regulations** (GDPR, HIPAA, ISO).
- Risk responses to recognize: **mitigate, transfer, avoid, accept.**
