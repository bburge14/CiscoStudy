# Public Key Infrastructure (PKI)

Asymmetric cryptography has a chicken-and-egg problem: a public key is only useful
if you're *sure* it really belongs to the party you think it does. If an attacker
can hand you *their* public key while claiming to be your bank, encryption buys you
nothing. **Public Key Infrastructure (PKI)** is the system of trusted authorities,
certificates, and processes that solves this — it's what makes public-key crypto
usable at internet scale. This lesson covers the players, the certificate, and how
trust is established and revoked.

## The problem PKI solves

> **PKI** binds a **public key** to a **verified identity** through a **digital
> certificate** issued by a trusted third party, so you can trust that a given
> public key really belongs to its claimed owner.

The "trusted third party" is the linchpin: instead of everyone personally
verifying everyone else, we all agree to trust a handful of authorities, and they
vouch for identities on our behalf.

## The players

PKI has a clear division of labor, and the exam tests the difference between two
roles that are easy to conflate:

| Component | Role |
|-----------|------|
| **Certificate Authority (CA)** | The trusted entity that **issues and digitally signs** certificates. Its signature is what makes a certificate trustworthy |
| **Registration Authority (RA)** | **Verifies the identity** of a certificate requester and forwards approved requests to the CA — but does **not** issue certificates itself |
| **Subscriber** | The entity (person, server) that obtains and holds a certificate |
| **Relying party** | Anyone who trusts and validates a certificate to communicate securely |
| **Certificate repository** | Where issued certificates and revocation info are published |

> The **CA issues** certificates; the **RA verifies identity and refers** the
> request. If a question says "verifies the requester but does not issue," that's
> the **RA**.

## The digital certificate (X.509)

The certificate itself follows the **X.509** standard. It is a signed data
structure that primarily does one thing:

> An **X.509 certificate binds a public key to the verified identity of its
> owner** (the "subject"), and the whole thing is **digitally signed by the issuing
> CA** so it can't be forged or altered.

Fields you should recognize: **subject** (the owner), **issuer** (the CA),
**public key**, **validity period** (not-before / not-after dates), **serial
number**, and **Subject Alternative Names (SANs)** for additional hostnames. A
**wildcard** certificate (`*.example.com`) covers all subdomains of a domain.

To get one, a subscriber generates a key pair and sends a **Certificate Signing
Request (CSR)** — containing the public key and identity details — to the CA. The
private key never leaves the subscriber. A **self-signed** certificate (issued by
itself, with no CA) provides encryption but no third-party trust, so browsers warn
on it.

## The chain of trust

CAs are organized in a hierarchy so that a compromise doesn't take down everything:

> A **root CA** sits at the top and is trusted implicitly (its certificate ships
> in your OS/browser **trust store**). The root signs **intermediate CAs**, which
> in turn sign end-entity certificates. Validating a certificate means following
> this **chain** up to a trusted root.

The root CA is kept **offline** for protection; day-to-day issuance is done by
intermediates. If an intermediate is compromised, it can be revoked without
reissuing the root. Your browser trusts a website's certificate because it can
build an unbroken signature chain from that certificate up to a root it already
trusts.

## Revocation: canceling trust early

Certificates have expiration dates, but sometimes you must invalidate one *before*
it expires — a stolen private key, an employee who left, a mis-issued cert. Two
mechanisms report revocation:

- **CRL (Certificate Revocation List)** — a signed list of revoked certificate
  serial numbers, published periodically by the CA. The downside: it can grow
  large and may be out of date between publications.
- **OCSP (Online Certificate Status Protocol)** — lets a relying party query the
  status of a **single** certificate in **real time**, without downloading a big
  list. **OCSP stapling** improves performance and privacy by having the web
  server attach a recent, CA-signed status response during the handshake.

> Need to check one certificate's revocation status in real time without parsing a
> huge list? That's **OCSP**. The bulk, periodically published list is the **CRL**.

A couple of related concepts: **key escrow** stores a copy of private keys with a
trusted party so encrypted data can be recovered if a key is lost (a deliberate
trade-off against confidentiality), and **certificate pinning** hard-codes an
expected certificate/key in an application to resist fraudulent certificates.

## Certificate types and validation levels

Not all certificates vouch for the same thing. By **validation level**, a CA
checks more before issuing a more trusted certificate:

- **DV (Domain Validation)** — proves only control of the domain; fast, automated,
  minimal assurance.
- **OV (Organization Validation)** — the CA also verifies the organization exists.
- **EV (Extended Validation)** — the most rigorous vetting of the legal entity.

By **purpose**, certificates differ in what they secure:

| Certificate | Use |
|-------------|-----|
| **Server (TLS/SSL)** | Authenticates a website/server to clients |
| **Client** | Authenticates a user or device to a server (mutual TLS) |
| **Code-signing** | Proves software came from a named publisher and wasn't altered |
| **Wildcard** (`*.example.com`) | Covers all subdomains of one domain |
| **SAN / multi-domain** | Covers several explicitly named hostnames |

The practitioner's job is matching the right certificate to the need — a wildcard
to protect many subdomains cheaply, a code-signing certificate to let users trust a
downloaded installer, client certificates where you want strong device
authentication rather than passwords.

## Exam focus

- **PKI binds a public key to a verified identity** via CA-signed **certificates**,
  solving "is this public key really theirs?"
- **CA issues and signs** certificates; the **RA verifies identity and forwards**
  requests but **does not issue**. Don't swap them.
- An **X.509 certificate binds a public key to the subject's verified identity**
  and is signed by the CA. You request one with a **CSR**; the private key stays
  with you. **Self-signed** = no third-party trust.
- Trust flows down a **chain**: trusted **root CA** (offline) -> **intermediate**
  -> end entity. Validation follows the chain to a root in the **trust store**.
- Revocation: **CRL** = big periodic list; **OCSP** = real-time single-certificate
  status check (**OCSP stapling** optimizes it). Know **key escrow** (key recovery)
  and **pinning**.
