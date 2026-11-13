# Cryptography

Cryptography is the math that makes confidentiality, integrity, authentication and
non-repudiation possible. You do not need to *do* the math for the exam, but you do
need to know which tool solves which problem, which key does what, and how the
classic attacks work in concept. This lesson builds from the three primitives —
symmetric, asymmetric, hashing — up through PKI and the attack classes, with the
defenses that keep crypto strong.

## What cryptography provides

> Cryptography delivers four services: **confidentiality** (secrecy),
> **integrity** (no undetected change), **authentication** (proof of origin), and
> **non-repudiation** (the sender cannot deny sending). Different primitives
> provide different services.

## Symmetric encryption

> **Symmetric encryption uses the *same* secret key to encrypt and to decrypt.**
> It is fast and ideal for bulk data, but both parties must already share the key —
> the "key distribution" problem.

Algorithms to recognize: **AES** (the modern standard), the obsolete **DES** and
stronger-but-legacy **3DES**, the broken stream cipher **RC4**, and
**Blowfish/Twofish**. If a question says "the same key encrypts and decrypts," it
is symmetric, and **AES** is the safe modern answer.

## Asymmetric encryption

> **Asymmetric (public-key) encryption uses a *key pair*: a public key and a
> private key that are mathematically linked.** What one key locks, only the other
> can unlock. This solves key distribution — you can share a public key freely.

The direction of the keys is the single most tested crypto fact:

| Goal | Encrypt / sign with | Decrypt / verify with |
|------|---------------------|------------------------|
| **Confidentiality** | Recipient's **public** key | Recipient's **private** key |
| **Authentication (signature)** | Sender's **private** key | Sender's **public** key |

> To send a confidential message only the recipient can read, encrypt it with the
> **recipient's public key** — because only the recipient holds the matching
> private key.

Algorithms: **RSA**, **ECC** (elliptic-curve — strong security with smaller keys),
**Diffie-Hellman** (key exchange), and **ElGamal**. Asymmetric crypto is slower, so
in practice it is used to **exchange a symmetric key** and to **sign**, then
symmetric crypto does the bulk work — this hybrid is how TLS works.

## Hashing

> **A hash function produces a fixed-length, one-way digest of its input.** It is
> for **integrity**, not secrecy — you cannot reverse a hash to recover the input.

The same input always yields the same hash; any change flips the output. Legacy
**MD5** and **SHA-1** are broken by collision attacks; use **SHA-2 (SHA-256)** or
**SHA-3**. For *passwords*, use deliberately slow, salted functions — **bcrypt,
scrypt, Argon2, PBKDF2** — not a plain fast hash. **HMAC** combines a hash with a
secret key to prove both integrity and authenticity.

## Digital signatures and PKI

A **digital signature** hashes a message and encrypts the hash with the signer's
**private key**; anyone can verify it with the signer's public key. That gives
integrity, authentication, and **non-repudiation** at once.

For this to scale, you need to trust that a public key really belongs to who it
claims. That is the job of **Public Key Infrastructure (PKI)**:

- **Certificate Authority (CA)** — a trusted party that issues and signs digital
  certificates.
- **Registration Authority (RA)** — verifies identity before a certificate is
  issued.
- **Digital certificate (X.509)** — binds a public key to an identity.
- **CRL / OCSP** — the Certificate Revocation List and Online Certificate Status
  Protocol, which say whether a certificate is still valid.
- **Chain of trust** — certificates chain from a trusted **root** through
  **intermediate** CAs to the end entity.

## Cryptographic attacks (in concept)

Know the *class* and its defense — never a procedure:

- **Brute force** — trying every key. *Defense:* large key sizes (e.g. AES-256).
- **Birthday attack** — exploits the math of **hash collisions**. *Defense:* strong,
  long hash outputs (SHA-256+).
- **Rainbow tables** — precomputed hash lookups for passwords. *Defense:* **salting**.
- **Known/chosen-plaintext** — analyzing plaintext/ciphertext pairs. *Defense:*
  modern ciphers resistant by design.
- **Side-channel** — leaking the key through timing, power, or emissions rather than
  the math.
- **Padding oracle** — abusing error responses about padding to decrypt.
- **Downgrade** — forcing a weak protocol/cipher (e.g. POODLE). *Defense:* disable
  legacy protocols.
- **Meet-in-the-middle** — why plain double-encryption (2DES) adds little strength.

## Keeping crypto strong

- Use **current, vetted algorithms** (AES, SHA-2/3, RSA-2048+/ECC) and retire
  **MD5, SHA-1, DES, RC4, and SSL/early TLS**.
- Prefer **authenticated encryption** (e.g. AES-GCM) so tampering is detected.
- **Salt** password hashes and use slow KDFs.
- Enforce **strong key management** — generation, storage, rotation, and
  destruction — ideally in an HSM or KMS.
- Configure protocols to **refuse downgrades** and weak cipher suites.

> The recurring idea: cryptography rarely fails because the math was broken — it
> fails because of **weak algorithms, weak keys, unsalted hashes, or
> misconfiguration**. Fix those and most attacks fall away.

## Exam focus

- **Symmetric** = **same key** both ways (AES); fast, but key distribution is the
  problem. **Asymmetric** = **key pair** (RSA, ECC, Diffie-Hellman).
- Key direction: **confidentiality → encrypt with the recipient's *public* key**;
  **signature → sign with the sender's *private* key**. This is tested directly.
- **Hashing** is one-way, for **integrity**; MD5/SHA-1 are **broken**, use
  SHA-2/SHA-3; hash **passwords** with salted **bcrypt/scrypt/Argon2/PBKDF2**.
- **Digital signature** = hash encrypted with the sender's private key → integrity,
  authentication, **non-repudiation**.
- **PKI** = **CA** issues, **RA** verifies, **X.509** certs bind key to identity,
  **CRL/OCSP** handle revocation, trust flows through a **chain of trust**.
- Attack classes: **brute force** (→ big keys), **birthday/collision** (→ strong
  hashes), **rainbow tables** (→ **salting**), **downgrade** (→ disable legacy),
  **side-channel**, **padding oracle**.
