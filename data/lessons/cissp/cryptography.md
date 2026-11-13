# Cryptography & Public Key Infrastructure

Cryptography is the engineering that turns the goals of Domain 1 — confidentiality,
integrity, authenticity, non-repudiation — into math you can rely on. CISSP does
not ask you to do the algebra, but it asks you constantly to pick the *right tool*:
which algorithm, which key, which mode, which PKI component solves the stated
problem. This lesson builds that judgment from the ground up.

## What cryptography delivers

Match the service to the mechanism — this mapping drives most crypto questions.

| Goal | Delivered by |
|------|--------------|
| **Confidentiality** | Encryption (symmetric or asymmetric) |
| **Integrity** | Hashing, MACs |
| **Authentication** | MACs, digital signatures |
| **Non-repudiation** | **Digital signatures only** (asymmetric) |

> **Non-repudiation requires asymmetric digital signatures.** A shared-key MAC or a
> bare hash cannot provide it, because with a shared secret either party could have
> produced the value — there is no proof of a *single* originator.

## Symmetric cryptography

One shared secret key encrypts and decrypts. It is **fast**, so it carries the
bulk of real data.

- **AES** — the standard. Block size 128 bits; key sizes **128, 192, or 256 bits**
  (based on the Rijndael cipher). Secure and ubiquitous.
- **3DES** — legacy; NIST has disallowed it (deprecated through 2023). Avoid in new
  designs.
- **DES** — broken; its **56-bit** key is trivially brute-forced. Historical only.
- **Blowfish / Twofish, RC4, ChaCha20** — RC4 (stream) is insecure and retired;
  ChaCha20 is a modern, fast stream cipher used in TLS.

The weakness of symmetric crypto is **key distribution**: every pair of
communicators needs a shared key delivered securely. For *n* people wanting
pairwise secrecy you need **n(n−1)/2** keys — which explodes with scale and
motivates asymmetric crypto.

## Asymmetric (public-key) cryptography

Each party has a **key pair**: a public key anyone may hold and a private key kept
secret. What one key locks, only the other opens. It is **slower**, so it is used
for small jobs — key exchange and signatures — not bulk data.

Two uses, and the direction matters:

- **For confidentiality**: encrypt with the **recipient's public** key; only their
  private key decrypts.
- **For a signature**: sign with the **sender's private** key; anyone verifies with
  the sender's public key.

Key algorithms:

- **RSA** — based on the difficulty of factoring large numbers; widely used.
- **ECC (Elliptic Curve)** — equivalent security with **much smaller keys**, so it
  is ideal for **mobile, IoT, and constrained devices**.
- **Diffie-Hellman** — a **key-exchange** protocol: two parties derive a shared
  secret over an open channel without ever transmitting it. (It does not encrypt or
  sign by itself.)

## Hashing and digital signatures

A **hash** is a one-way function producing a fixed-length digest; change one bit of
input and the digest changes completely. Hashes provide **integrity**.

- **MD5** — broken (collisions); do not use.
- **SHA-1** — deprecated. NIST disallowed it for digital signatures back in 2013
  and has set **December 31, 2030** as the date to retire it entirely; the SHA-2
  and SHA-3 families are the recommended replacements.
- **SHA-2** — the current workhorse (SHA-256, SHA-384, SHA-512).
- **SHA-3** — the newest standard (Keccak), a different internal design as a hedge
  against future attacks on SHA-2.
- **HMAC** — a keyed hash that provides **integrity *and* authenticity** (it proves
  the message wasn't altered and came from someone holding the key).

> A **digital signature** = hash the message, then encrypt the hash with the
> **sender's private key**. It delivers **integrity, authentication, and
> non-repudiation** at once. This is why non-repudiation is inherently asymmetric.

## Hybrid cryptography and modes

Real protocols combine the two: use **asymmetric** crypto to exchange a random
**symmetric session key**, then use the fast symmetric cipher for the actual data.
This is exactly how **TLS** works, and it solves the key-distribution problem while
keeping bulk encryption fast.

**Block cipher modes of operation** turn a block cipher into something usable, and
the exam tests their security:

- **ECB (Electronic Codebook)** — encrypts each block independently; identical
  plaintext blocks produce identical ciphertext, leaking patterns. **Avoid.**
- **CBC (Cipher Block Chaining)** — chains blocks with an initialization vector
  (IV) so patterns disappear.
- **CTR (Counter)** — turns a block cipher into a stream cipher; parallelizable.
- **GCM (Galois/Counter Mode)** — **authenticated encryption (AEAD)**: provides
  confidentiality **and** integrity/authenticity in one pass. The modern default in
  TLS.

> If a stem shows repeating patterns surviving encryption, the culprit is **ECB**.
> If it asks for confidentiality *and* integrity together, the answer is an **AEAD
> mode like GCM**.

## Public Key Infrastructure (PKI)

PKI is the trust framework that answers "whose public key is this, really?" It
binds identities to public keys using **digital certificates**.

- **Certificate Authority (CA)** — a trusted third party that **issues and signs**
  certificates vouching for the subject's identity.
- **Registration Authority (RA)** — verifies identity before the CA issues.
- **Digital certificate (X.509)** — binds a public key to an identity, signed by
  the CA.
- **Chain of trust** — certificates validate up to a trusted **root CA**.
- **Revocation** — a **CRL (Certificate Revocation List)** is a published list of
  revoked certs; **OCSP (Online Certificate Status Protocol)** checks a single
  cert's status in real time, avoiding big list downloads.
- **Key escrow** — a copy of keys held by a third party for recovery (balances
  availability against the risk of a single point of compromise).

## Attacks and forward secrecy

Know the named attacks: **brute force** (try all keys — defeated by key length),
**birthday attack** (find hash collisions using probability), **rainbow tables**
(precomputed hash lookups — defeated by **salting**), **known/chosen plaintext**,
**side-channel** (timing, power analysis), and **meet-in-the-middle** (why 2DES is
weak). **Perfect Forward Secrecy (PFS)**, via ephemeral Diffie-Hellman, ensures
that compromising a long-term key does not expose past session traffic.

## Exam focus

- Match goal to tool: **encryption = confidentiality**, **hash = integrity**,
  **HMAC = integrity + authenticity**, **digital signature = integrity +
  authentication + non-repudiation (asymmetric)**.
- **Symmetric** (AES, fast, bulk) suffers **key distribution**; **asymmetric**
  (RSA, ECC, Diffie-Hellman) is slow but solves it. **Encrypt with recipient's
  public key; sign with sender's private key.** **ECC** fits constrained devices.
- Hash status: **MD5 and SHA-1 are out** (SHA-1 retires 2030); use **SHA-2 /
  SHA-3**.
- Modes: **ECB leaks patterns (avoid)**; **GCM** is authenticated encryption
  (confidentiality + integrity). **Hybrid** crypto (asymmetric to exchange a
  symmetric session key) is how TLS works.
- PKI: **CA issues/signs certs**, **RA verifies identity**, **X.509** binds key to
  identity, **CRL vs OCSP** for revocation. **PFS** protects past sessions if a
  long-term key is later compromised.
