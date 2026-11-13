# Network Security & Cryptography/PKI

Data in motion is data at risk. Networks carry it past firewalls, across the
public internet, and between buildings — and cryptography is what keeps it
confidential and trustworthy along the way. This lesson pairs the network
defenses the auditor expects to see with the encryption and public-key
infrastructure that protect data in transit (and at rest).

## Network defenses

The first job of network security is controlling what traffic is allowed where.
The workhorse is the **firewall**, and CISA expects you to distinguish its types.

> A **stateful inspection firewall** makes decisions based on the **state and
> context of a connection** — tracking whether a packet belongs to an established,
> legitimate session — rather than judging each packet in isolation (as a simple
> **packet-filter** does). This context makes it far harder to slip malicious
> traffic past.

Other firewall and gateway types include **application-layer (proxy) firewalls**
that inspect specific protocols, and **next-generation firewalls** that add
application awareness and intrusion prevention.

Where you place servers matters as much as how you filter:

> Internet-facing servers (public web, email) belong in a **DMZ (screened
> subnet)** — a buffer network sitting **between an external and an internal
> firewall**. If a public server is compromised, the attacker is still isolated
> from the internal corporate network.

For *detecting* and *blocking* attacks, know the IDS/IPS distinction cold:

> An **intrusion detection system (IDS)** is **passive** — it monitors traffic and
> **alerts** (detective). An **intrusion prevention system (IPS)** sits **inline**
> in the traffic path and can **block malicious traffic in real time**
> (preventive).

To protect traffic crossing untrusted networks:

> To protect the confidentiality and integrity of data sent between two offices
> over the public internet, use a **VPN**, typically built on **IPsec**, which
> creates an **encrypted tunnel** so eavesdroppers see only ciphertext.

Rounding out the defenses: **network segmentation** limits how far an intruder can
move; **network access control (NAC)** checks a device's identity and health
before admitting it; and **wireless security** relies on strong protocols (WPA2/
WPA3) rather than outdated, breakable ones.

## Cryptography fundamentals

Encryption transforms readable **plaintext** into unreadable **ciphertext** using
an algorithm and a **key**. There are two families, and their differences drive
every crypto question.

> **Symmetric** cryptography uses **one shared secret key** to both encrypt and
> decrypt. It is **fast**, but its challenge is **key distribution** — safely
> getting the same secret key to both parties. (AES is the common example.)

> **Asymmetric** (public-key) cryptography uses a **mathematically linked key
> pair**: a **public** key anyone can hold and a **private** key kept secret. What
> one key locks, only the other can unlock. It solves key distribution but is
> slower. (RSA, ECC are examples.)

In practice the two are combined: asymmetric crypto securely exchanges a symmetric
**session key**, then fast symmetric crypto protects the bulk data.

### Which key does what

This is the single most-tested crypto idea, and the direction is everything.

> - **For confidentiality to a recipient**, encrypt with the **recipient's
>   PUBLIC key** — only the recipient's private key can decrypt it, so only they
>   can read it.
> - **For a digital signature**, the sender encrypts the message's **hash
>   (digest)** with the **sender's PRIVATE key**. Anyone can verify it with the
>   sender's public key.

| Goal | Encrypt with… | Decrypt/verify with… |
|------|---------------|----------------------|
| **Confidentiality** to a recipient | Recipient's **public** key | Recipient's **private** key |
| **Digital signature** (sender proves origin) | Sender's **private** key | Sender's **public** key |

A memory hook: **you encrypt FOR someone with THEIR public key; you sign AS
yourself with YOUR private key.**

### Hashing, integrity, and signatures

A **hash function** produces a fixed-length, one-way **digest** of data; change
one bit and the digest changes, which is how you detect tampering (**integrity**).
A **digital signature** combines hashing with the sender's private key to deliver
three assurances at once:

- **Integrity** — the message wasn't altered (the hash matches).
- **Authentication** — it really came from the sender (only their private key
  could sign).
- **Non-repudiation** — the sender can't later deny signing it.

## Public key infrastructure (PKI)

Public keys are only useful if you can trust *whose* key you hold. PKI provides
that trust through certificates.

> A **certificate authority (CA)** is the trusted entity in a PKI that **issues,
> signs, and revokes digital certificates** binding a public key to a verified
> identity. Your trust in a certificate comes from your trust in the CA that
> signed it.

The surrounding pieces: a **registration authority (RA)** verifies identities
before certificates are issued; a **digital certificate** (X.509) carries the
subject's public key and the CA's signature; and revoked certificates are
published through a **certificate revocation list (CRL)** or checked in real time
via **OCSP**. The auditor checks that certificates are valid, current, and issued
by trusted CAs, and that private keys are protected — a leaked private key
collapses the whole chain of trust.

## Exam focus

- **Stateful inspection** firewalls track **connection state/context**; place
  public servers in a **DMZ/screened subnet** between two firewalls.
- **IDS = passive, alerts (detective); IPS = inline, blocks (preventive).** Use an
  **IPsec VPN** to protect traffic over the public internet.
- **Symmetric** = one shared key (fast; key-distribution problem); **asymmetric** =
  public/private key pair (solves distribution; slower).
- **Confidentiality → encrypt with the recipient's PUBLIC key.** **Digital
  signature → sign (encrypt the hash) with the sender's PRIVATE key**, giving
  integrity, authentication, and non-repudiation.
- A **CA** issues, signs, and revokes certificates binding a public key to an
  identity; protect **private keys** above all.
