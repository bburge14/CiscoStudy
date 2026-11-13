# Evasion, Encryption & Certificate Visibility

Encryption is a defender's best friend and, paradoxically, one of the analyst's
biggest headaches. The same cryptography that protects legitimate traffic also
hides malicious traffic from inspection, and attackers pile on a whole toolkit of
**evasion and obfuscation** tricks to stay invisible. This lesson covers those
tricks and then the **certificates and PKI** that make encryption trustworthy —
and that, read correctly, give the analyst clues even when the payload is opaque.

## Evasion and obfuscation: hiding from the sensor

An attacker who assumes they are being watched will try to defeat the sensors.
These techniques don't change *what* the attack does; they change whether your
tools can *see* it.

> **Evasion** techniques aim to slip malicious activity past detection;
> **obfuscation** makes the malicious content unreadable to a simple inspection.
> Both reduce sensor visibility without stopping the attack.

- **Encryption (e.g., TLS)** — when malware talks to its command-and-control
  server over TLS, the payload on the wire is **ciphertext**. A signature-based
  IDS that only sees the wire cannot match content signatures against data it
  cannot read. This is the single biggest visibility gap in modern monitoring.
- **Tunneling** — encapsulating one protocol's traffic inside another, such as
  smuggling C2 data inside **DNS** queries or **ICMP** packets, to ride a
  protocol that inspection tends to wave through.
- **Fragmentation** — splitting a malicious payload across many small IP
  fragments in the hope the IDS evaluates each fragment alone and never
  reassembles the complete signature.
- **Encoding / obfuscation** — hiding a command string by **Base64**-encoding (or
  otherwise transforming) it so a keyword search for the plaintext never matches.
- **Anonymization (Tor)** — routing traffic through many relays so the true
  source and destination are obscured, frustrating attribution.
- **Address translation (PAT/NAT)** — when many internal hosts share one public
  IP, perimeter and external logs show the **shared public address**, not the
  specific inside host, complicating attribution.
- **Resource exhaustion of the sensor** — flooding an IDS with crafted traffic so
  it drops packets or stops inspecting while the real attack slips through.

The analyst's takeaways: encryption and tunneling mean you must lean on
**metadata and flow data** (who/when/how much) when payload is hidden; and
translation/anonymization mean an external IP is rarely the end of the
attribution story.

## Certificates and PKI: the trust behind encryption

Encryption only helps if you are talking to the *right* party. That assurance
comes from **public key infrastructure (PKI)** and the **digital certificates**
it issues.

> A **certificate authority (CA)** is the trusted entity that validates
> identities and issues and **digitally signs** digital certificates. A
> certificate binds a public key to an identity, vouched for by the CA's
> signature.

### How a certificate comes to exist

1. A server generates a key pair and a **Certificate Signing Request (CSR)**
   containing its **public key** and identifying information.
2. It submits the CSR to a **CA**, which validates the identity.
3. The CA issues an **X.509 certificate**, signed with the CA's key.

Standard **X.509** fields an analyst should expect include the **subject**, the
**issuer's distinguished name**, the **public key**, and the **validity period**
(the *Not Before* / *Not After* dates). An expired or self-signed certificate on
a supposedly trusted service is worth a second look.

### The chain of trust

Browsers and operating systems ship with a **trust store** of **root CA**
certificates. A server's certificate is usually signed by an **intermediate CA**,
whose certificate chains up to a trusted **root** already in the store. The
client trusts the server because it can follow that chain to a root it already
trusts. Break the chain — an unknown issuer — and the client warns the user.

### Asymmetric keys, in one breath

> To send data only the recipient can read, encrypt with the **recipient's
> public** key; they decrypt with their **private** key. To prove *you* sent
> something, create a **digital signature** by encrypting the message's hash with
> **your private** key; anyone verifies it with **your public** key.

A valid digital signature therefore gives three things at once:
**authentication** of origin, **integrity** (the content wasn't altered), and
**non-repudiation** (the signer can't credibly deny it). Keep the two uses
straight — *public key to encrypt to someone; private key to sign as someone.*

### Revocation

Sometimes a certificate must be distrusted before it expires — say, after a key
compromise. Two mechanisms publish that a certificate is revoked:

- **Certificate Revocation List (CRL)** — a signed list of revoked certificate
  serial numbers the client can download.
- **Online Certificate Status Protocol (OCSP)** — the client asks the CA about a
  single certificate's status in real time.

## Where the two halves meet

Notice how evasion and PKI connect. An attacker uses TLS to blind your
signatures — but the **certificate** that TLS presents is itself metadata you can
inspect: a freshly issued cert, a self-signed cert, an odd issuer, or a domain
that doesn't match can all flag malicious C2 even when the payload is unreadable.
When content is encrypted, you shift your attention to everything *around* the
content — certificates, flow volumes, destinations, and timing.

## Exam focus

- **TLS/encryption** defeats signature IDS because the payload is **ciphertext** —
  content signatures can't match. Shift to metadata/flow analysis when payload is
  hidden.
- Know the evasion techniques: **tunneling** (protocol-in-protocol, e.g., DNS/ICMP
  C2), **fragmentation** (split to avoid signature reassembly), **encoding/
  obfuscation** (e.g., Base64), **Tor** (anonymizes source/destination), **PAT**
  (shared public IP hides the internal host), **sensor resource exhaustion**.
- A **CSR** carries a public key + identity to a **CA** for signing. A **CA**
  issues and signs **X.509** certs (fields: subject, **issuer DN**, public key,
  **validity Not Before/Not After**).
- Trust chains: server cert → **intermediate CA** → **root CA** in the trust
  store.
- Asymmetric: **encrypt with recipient's public key**; **sign with your private
  key**. A digital signature provides **authentication, integrity, and
  non-repudiation**.
- Revocation is published via **CRL** and **OCSP**.
