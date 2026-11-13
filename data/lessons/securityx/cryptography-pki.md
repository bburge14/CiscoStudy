# Applied Cryptography, PKI & Post-Quantum Migration

Cryptography is the load-bearing wall of security engineering, and SecurityX tests
it at the level of someone who *chooses and migrates* cryptosystems for an
enterprise — including the generational shift to **post-quantum** algorithms now
underway. This lesson covers applied cryptography, the public-key infrastructure
that operationalizes it, and the PQC migration you must be able to plan.

## Choosing the right primitive

Start from what the data needs: **confidentiality**, **integrity**,
**authentication**, or **non-repudiation** — and pick accordingly.

- **Symmetric** encryption (**AES**) is fast and used for bulk data; both sides
  share one key, so key *distribution* is the hard part.
- **Asymmetric** (public-key) encryption (**RSA**, **ECC**) solves distribution
  with a key pair, but is far slower — so in practice it is used to exchange a
  symmetric key, giving a **hybrid** system.
- **ECC (Elliptic Curve Cryptography)** delivers equivalent strength to RSA with
  **much smaller keys and lower compute** — making it the right choice for
  **constrained, battery-powered devices** (IoT sensors) that still need strong
  public-key crypto.

### Modes matter: use authenticated encryption

A cipher's **mode of operation** determines its security properties:

- **ECB** is broken for structured data — identical plaintext blocks produce
  identical ciphertext, leaking patterns. Avoid it.
- **CBC** chains blocks but provides no built-in integrity.
- **GCM (Galois/Counter Mode)** is **AEAD — Authenticated Encryption with Associated
  Data** — it provides confidentiality *and* integrity/authenticity in one
  operation. **AES-GCM** (and ChaCha20-Poly1305) is the modern default and what TLS
  1.3 uses.

> Prefer **authenticated encryption (AES-GCM)**: encryption without integrity lets
> an attacker tamper with ciphertext undetected. **ECB** is the classic wrong
> answer because it leaks plaintext structure.

### Hashing and password storage

**Hashing** is one-way and proves **integrity**. For passwords, a plain hash is not
enough — attackers use precomputed tables. The correct design:

- **Salt** — a unique random value per password, so two users with the same
  password store different hashes and rainbow tables are defeated.
- **Key-stretching / slow hashes** — **bcrypt, scrypt, Argon2, PBKDF2** are
  deliberately slow and memory-hard to resist brute force.

> To store passwords so a breach reveals nothing and identical passwords differ:
> **salt each password and use a slow hash (bcrypt/Argon2/scrypt/PBKDF2)** — never a
> fast raw hash like SHA-256 alone.

### Keys, signatures, and secrecy

**Digital signatures** provide integrity, authentication, and **non-repudiation**:
you sign with your **private** key, and anyone verifies with your **public** key.
**Perfect Forward Secrecy (PFS)**, via ephemeral key exchange (**ECDHE**), ensures
that compromising a server's long-term private key does **not** decrypt previously
recorded sessions — each session uses a fresh ephemeral key. This is why TLS 1.3
mandates ephemeral key exchange.

## Public Key Infrastructure (PKI)

PKI is the system of CAs, certificates, and processes that binds public keys to
identities and makes public-key crypto usable at scale.

### The CA hierarchy

A well-designed PKI protects its most valuable asset — the **root** signing key:

- The **root CA** is kept **offline** and only ever signs **intermediate
  (subordinate) CA** certificates.
- **Intermediate CAs** issue the day-to-day end-entity certificates.
- If an intermediate's signing key is compromised, you revoke that intermediate and
  the offline root remains trustworthy — a far smaller blast radius than losing the
  root.

> Keep the **root CA offline** and issue from **intermediates**. This minimizes
> impact: a compromised issuing CA is revoked without destroying the trust anchor.

### Revocation: CRL vs OCSP vs stapling

Certificates sometimes must be revoked before expiry. Clients check status via:

- **CRL (Certificate Revocation List)** — a signed list of revoked serials;
  simple but large and periodically fetched.
- **OCSP (Online Certificate Status Protocol)** — a real-time query to a responder;
  lower latency than CRLs but puts load on the responder and can leak which sites a
  client visits.
- **OCSP stapling** — the **server** fetches and attaches ("staples") a recent,
  signed OCSP response to its handshake, so clients verify revocation **with minimal
  latency and without each client querying the responder**. This is the answer for
  low-latency, high-traffic revocation checking.

### Certificate types and trust

- **Mutual TLS (mTLS)** authenticates **both** ends with certificates — essential
  in zero-trust microservices where each service must prove identity, not just the
  server. If a stem says "both ends authenticate with certificates," it is mTLS.
- **Wildcard** certs cover `*.example.com`; **SAN** certs cover multiple named
  hosts.
- **Key escrow** stores a copy of keys for lawful recovery; **certificate pinning**
  ties a client to a specific expected certificate.

## Post-Quantum Cryptography (PQC) and the migration

A large-scale quantum computer would break RSA and ECC (via Shor's algorithm). The
threat is already here in one form: **"harvest now, decrypt later"** — adversaries
record today's encrypted traffic to decrypt once quantum capability arrives. That
makes PQC migration urgent for long-lived secrets.

In **August 2024, NIST finalized the first post-quantum standards**:

| Standard | Algorithm (origin) | Purpose |
|----------|--------------------|---------|
| **FIPS 203** | **ML-KEM** (from CRYSTALS-Kyber) | Key encapsulation / key establishment |
| **FIPS 204** | **ML-DSA** (from CRYSTALS-Dilithium) | Primary digital signatures |
| **FIPS 205** | **SLH-DSA** (from SPHINCS+) | Hash-based signatures (a math-diverse backup) |

ML-KEM and ML-DSA are **lattice-based**; SLH-DSA rests on **hash** security, giving
diversity if a lattice weakness is found. NIST later selected **HQC** as a backup
KEM and continues to standardize additional signatures (e.g., FN-DSA/FIPS 206 in
draft).

### Planning the migration

The migration is multi-year, and the exam rewards the *architectural* mindset:

- **Crypto-agility** — design systems so algorithms can be swapped without
  re-architecting. This is the single most important enabler.
- **Inventory first** — you cannot migrate what you cannot find; build a complete
  cryptographic inventory (a cryptographic bill of materials).
- **Hybrid deployment** — run a classical and a PQC algorithm together during the
  transition so you are protected even if one is later found weak.
- **Prioritize long-lived data** — anything that must stay secret for a decade is
  most exposed to harvest-now-decrypt-later and migrates first.

> The threat driving PQC today is **harvest now, decrypt later**. NIST's finalized
> standards are **FIPS 203 (ML-KEM)**, **FIPS 204 (ML-DSA)**, **FIPS 205
> (SLH-DSA)**. The migration strategy is **crypto-agility + inventory + hybrid**,
> prioritizing long-lived secrets.

## Exam focus

- **Symmetric (AES)** = fast/bulk; **asymmetric (RSA/ECC)** = key exchange;
  **ECC** = strong with small keys for **IoT/constrained devices**. Real systems
  are **hybrid**.
- Use **authenticated encryption (AES-GCM / AEAD)**; **ECB** leaks structure and is
  the wrong answer for structured data.
- Password storage = **salt + slow hash (bcrypt/Argon2/scrypt/PBKDF2)**. Salting
  makes identical passwords store differently.
- **PFS (ECDHE)** means a stolen long-term key cannot decrypt past recorded
  sessions — TLS 1.3 requires ephemeral key exchange.
- PKI: keep the **root CA offline**, issue from **intermediates**; **OCSP stapling**
  gives low-latency revocation without per-client responder load; **mTLS**
  authenticates both ends (zero-trust microservices).
- PQC: threat = **harvest-now, decrypt-later**; standards **FIPS 203 ML-KEM / 204
  ML-DSA / 205 SLH-DSA** (Aug 2024); migrate via **crypto-agility, inventory, and
  hybrid**, long-lived data first.
