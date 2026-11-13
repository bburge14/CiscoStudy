# Cryptographic Concepts: Symmetric, Asymmetric & Hashing

Cryptography is how we protect data with math instead of walls. It delivers three
of the security goals directly: **confidentiality** (encryption), **integrity**
(hashing), and **non-repudiation** (digital signatures). The trick is knowing
which tool does which job — a mistake the exam probes relentlessly. This lesson
builds the three pillars: symmetric encryption, asymmetric encryption, and
hashing, then shows how they combine into signatures.

## Symmetric encryption: one shared key

> **Symmetric** cryptography uses a **single shared secret key** for both
> encryption and decryption. The same key that locks the data unlocks it.

Symmetric ciphers are **fast**, which makes them the right choice for encrypting
**bulk data** — files at rest, disk volumes, the actual payload of a TLS session.
The modern standard:

- **AES (Advanced Encryption Standard)** — the go-to symmetric **block cipher**
  (standardized in FIPS 197), with key sizes of 128, 192, or 256 bits. When a
  question asks for a fast, modern cipher to encrypt large volumes of data at
  rest, **AES** is the answer.
- **3DES** is legacy and deprecated; **DES** is broken. **ChaCha20** is a modern
  stream cipher used where AES hardware isn't available.

Block vs stream: a **block cipher** (AES) encrypts fixed-size blocks and is the
norm; a **stream cipher** (ChaCha20, RC4—now broken) encrypts bit-by-bit for
continuous data. Block ciphers use **modes of operation** (e.g., **GCM**, which
also provides built-in authentication; avoid **ECB**, which leaks patterns).

The catch with symmetric crypto is **key distribution**: how do two parties agree
on the shared secret without an eavesdropper capturing it? That problem is exactly
what asymmetric cryptography solves.

## Asymmetric encryption: a key pair

> **Asymmetric** (public-key) cryptography uses a **mathematically related key
> pair**: a **public key** that can be shared freely and a **private key** kept
> secret. What one key does, only the *other* can undo.

This one property enables two different jobs depending on *which* key you use:

- **For confidentiality (encryption):** encrypt with the **recipient's public
  key**; only the recipient's matching **private key** can decrypt. So if **Alice
  wants only Bob to read a message, she encrypts it with Bob's public key.** This
  is the perennial exam question — encrypt *to* someone with *their public key*.
- **For authenticity (signing):** encrypt (sign) with your **own private key**;
  anyone can verify with your **public key** (covered below).

Common algorithms: **RSA** (based on factoring large numbers), **ECC (Elliptic
Curve Cryptography)** (same security with much smaller keys — ideal for mobile/
IoT), and **Diffie-Hellman** (for securely agreeing on a shared key). Asymmetric
crypto is **slow**, so in practice it's used to exchange a symmetric key, and then
the fast symmetric cipher does the bulk work — a **hybrid** approach (exactly what
TLS does).

> **Encrypt for secrecy -> recipient's PUBLIC key. Sign for proof -> your own
> PRIVATE key.** Reverse them and the whole scheme fails. This is the single most
> important crypto rule on the exam.

## Hashing: a one-way fingerprint

> A **cryptographic hash** is a **one-way** function that turns any input into a
> fixed-length digest. You cannot reverse it to recover the input, and any change
> to the input — even one bit — produces a completely different digest.

Hashing provides **integrity**, not confidentiality: it proves data hasn't
changed, it doesn't hide it. Good hash functions resist **collisions** (two
different inputs producing the same digest).

- **SHA-2** (SHA-256, SHA-512) and **SHA-3** (FIPS 202) are current and secure.
- **MD5** and **SHA-1** are **broken** (practical collisions found) — never use
  them for security.
- Add a unique random **salt** before hashing passwords so identical passwords
  don't share a digest and precomputed **rainbow tables** fail. Password-specific
  functions (**bcrypt, scrypt, PBKDF2, Argon2**) are deliberately slow to resist
  brute force.
- **HMAC** combines a hash with a secret key to provide integrity *and*
  authentication of a message.

## Putting it together: digital signatures

Signatures combine hashing and asymmetric crypto to deliver **integrity**,
**authenticity**, and **non-repudiation** at once:

> To **sign**: hash the document, then **encrypt the hash with the sender's
> private key.** To **verify**: the recipient decrypts the signature with the
> sender's **public key** to get the original hash, independently hashes the
> document, and checks that the two match.

If they match, the document is unaltered (integrity) and genuinely from the sender
(authenticity), and the sender can't deny signing it (non-repudiation). Note a
signature does **not** provide confidentiality — the document itself isn't
encrypted by signing it.

| Goal | Tool |
|------|------|
| **Confidentiality** | Encryption (symmetric for bulk; asymmetric to share the key) |
| **Integrity** | Hashing (and HMAC) |
| **Authenticity & non-repudiation** | Digital signature (hash + sign with private key) |

A forward-looking note: large quantum computers would threaten RSA and ECC, so
NIST finalized the first **post-quantum cryptography** standards in August 2024 —
**FIPS 203 (ML-KEM)** for key establishment, **FIPS 204 (ML-DSA)** and **FIPS 205
(SLH-DSA)** for signatures. Symmetric crypto and hashing are far less affected
(larger keys/digests suffice).

## Exam focus

- **Symmetric** = one shared key, **fast**, for **bulk data**; **AES** is the
  modern standard block cipher. Its weakness is **key distribution**.
- **Asymmetric** = public/private key pair, **slow**, solves key exchange. **Encrypt
  for confidentiality with the recipient's PUBLIC key** (Alice -> Bob uses Bob's
  public key).
- **Sign with your PRIVATE key**; verify with the sender's public key. Memorize:
  **public to encrypt to someone, private to sign.**
- **Hashing** is **one-way** and gives **integrity** only. **SHA-2/SHA-3** good;
  **MD5/SHA-1 broken.** **Salt** passwords; **HMAC** adds authentication.
- A **digital signature** = hash the data, encrypt the hash with the **sender's
  private key** -> integrity + authenticity + non-repudiation (but not
  confidentiality).
