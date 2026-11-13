# Key Management

A cryptographic algorithm can be flawless and still fail completely if its keys
are mishandled. The hard part of real-world cryptography is almost never the
math — it's **key management**: generating keys securely, getting them to the
right parties without interception, storing them safely, rotating them on
schedule, and destroying them when done. This lesson covers that whole lifecycle
and the tools that protect it.

## The key management lifecycle

> **Key management** is the end-to-end process of handling cryptographic keys
> across their lifecycle: **generation -> distribution/exchange -> storage/use ->
> rotation -> revocation -> destruction.** A weakness at any stage undermines the
> cryptography that depends on it.

Walk the stages:

- **Generation** — keys must come from a strong, truly random source. Weak
  randomness (low **entropy**) produces guessable keys, so systems use a
  cryptographically secure random number generator.
- **Distribution/exchange** — getting the key to the other party without an
  eavesdropper capturing it (the central challenge, below).
- **Storage** — protecting keys at rest so they can't be stolen; never hard-code a
  key in source code or leave it in a config file in plaintext.
- **Rotation** — periodically replacing keys (see crypto-periods).
- **Revocation** — invalidating a key that's compromised or no longer needed.
- **Destruction** — securely erasing retired keys, often called **zeroization**
  (overwriting the key material in memory/hardware so it can't be recovered).

## The key distribution problem

Symmetric encryption is fast and strong, but it has one Achilles' heel:

> The principal challenge of symmetric cryptography is **securely distributing the
> shared secret key** to both parties without it being intercepted. If an attacker
> captures the key in transit, the encryption is worthless.

This is precisely the problem asymmetric cryptography was invented to help solve.
The elegant answer for agreeing on a shared secret over an untrusted network is a
**key exchange algorithm**:

> **Diffie-Hellman** lets two parties **derive a shared secret key over an
> insecure channel without ever transmitting the secret itself.** Each side mixes
> public values with its own private value; both arrive at the same secret, while
> an eavesdropper who sees only the public exchange cannot compute it.

Diffie-Hellman is used constantly (it's part of every TLS handshake). A critical
enhancement is **Perfect Forward Secrecy (PFS)**: using **ephemeral** (one-time)
Diffie-Hellman keys per session means that even if a long-term private key is later
stolen, past recorded sessions **cannot** be decrypted — each session's key is
independent and already destroyed.

## Crypto-periods: why keys expire

Keys shouldn't live forever. A **crypto-period** is the defined lifespan of a key,
after which it is rotated (replaced).

> Keys are rotated periodically to **limit the amount of data exposed if a key is
> compromised** and to **reduce the window available for cryptanalysis.** The more
> data encrypted under one key, and the longer it lives, the more valuable it is to
> an attacker and the more there is to lose.

Rotation is a containment strategy: a compromised key only exposes the data from
its own crypto-period, not everything you've ever encrypted. High-value or
high-volume keys get shorter crypto-periods.

## Protecting keys: HSMs and hardware roots of trust

Where you store keys matters as much as how you generate them. The gold standard
is dedicated hardware:

> A **Hardware Security Module (HSM)** is a dedicated, **tamper-resistant**
> hardware device that securely **generates, stores, and manages cryptographic
> keys** and performs crypto operations — keeping the private keys inside the
> device so they're never exposed in software or memory.

If someone tries to physically attack an HSM, it is designed to **zeroize** its
keys rather than surrender them. Related hardware and services:

| Component | Role |
|-----------|------|
| **HSM** | Tamper-resistant device for key generation/storage/operations |
| **TPM (Trusted Platform Module)** | A chip on a device's motherboard that stores keys for that host (e.g., disk-encryption keys) |
| **KMS (Key Management Service)** | A centralized (often cloud) service that manages keys and policies at scale |
| **Secure enclave** | An isolated processor region that protects keys/secrets in use |

## Governance controls for keys

Because keys are so powerful, access to them is split and controlled:

- **Dual control** — two people are required to perform a sensitive key operation,
  so no single person can act alone.
- **Split knowledge** — the key (or the knowledge to reconstruct it) is divided so
  no one person holds the whole thing (e.g., **M-of-N** schemes where any M of N
  key custodians must combine their parts).
- **Key escrow** — a trusted copy is held so encrypted data can be recovered if a
  key is lost, balanced carefully against the risk of that escrow being abused.
- **Separation of duties** — the person who manages keys shouldn't also be the one
  auditing their use.

These prevent a single rogue administrator from compromising the entire
cryptographic system.

## Exam focus

- Key management spans the whole lifecycle: **generate (strong entropy) ->
  distribute -> store -> rotate -> revoke -> destroy (zeroize).** The weakest stage
  defines the system's strength.
- The core symmetric weakness is **secure key distribution**; **Diffie-Hellman**
  solves it by letting two parties derive a shared secret over an untrusted
  channel **without transmitting it**. Ephemeral DH gives **Perfect Forward
  Secrecy**.
- A **crypto-period** bounds a key's life; **rotation** limits exposure if a key is
  compromised and shrinks the cryptanalysis window.
- An **HSM** is a **tamper-resistant** device that generates, stores, and uses keys
  without exposing them; a **TPM** anchors keys on a single host; a **KMS** manages
  keys at scale.
- **Dual control** and **split knowledge (M-of-N)** stop any one person from
  controlling a key; **key escrow** enables recovery.
