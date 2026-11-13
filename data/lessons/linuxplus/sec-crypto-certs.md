# Certificates, Keys & GPG

Encryption protects data in transit and at rest, and proves who sent it. A Linux
administrator does not design cryptography, but must handle its artifacts
fluently: TLS **certificates** for services, **hashes** for integrity, and **GPG**
keys for encrypting and signing files. This lesson is the practical tooling.

## The building blocks

Three primitives underlie everything here:

- **Symmetric encryption** uses one shared secret key for both encryption and
  decryption — fast, used for bulk data (AES).
- **Asymmetric encryption** uses a **key pair**: a *public* key anyone may hold
  and a *private* key kept secret. Data encrypted to the public key can only be
  decrypted with the private key; data signed with the private key can be verified
  with the public key.
- **Hashing** produces a fixed-length fingerprint of data. It is one-way and used
  to check **integrity**, not to encrypt.

## TLS certificates (X.509)

A TLS certificate binds a public key to an identity (a hostname) and is vouched
for by a **Certificate Authority (CA)**. The trust chain runs: a browser/OS trusts
root CAs → a root signs an intermediate → the intermediate signs your server's
certificate.

The lifecycle you must know:

1. Generate a **private key**.
2. Create a **Certificate Signing Request (CSR)** containing your public key and
   identity details.
3. Send the CSR to a CA, which returns a **signed certificate**. (For internal
   use you can skip the CA and make a **self-signed** certificate.)

**OpenSSL** does all of this. Certificates are usually **PEM** files (Base64 text
beginning `-----BEGIN CERTIFICATE-----`):

```
$ openssl genpkey -algorithm RSA -out server.key           # private key
$ openssl req -new -key server.key -out server.csr          # CSR
$ openssl req -x509 -new -key server.key -days 365 \
      -out server.crt                                        # self-signed cert
$ openssl x509 -in server.crt -text -noout                   # inspect a cert
$ openssl s_client -connect example.com:443                  # check a live service
```

Trusted CA certificates are stored system-wide (`/etc/pki/tls/certs` on Red Hat,
`/etc/ssl/certs` on Debian). To trust a new internal CA, drop its certificate in
the right directory and run **`update-ca-trust`** (Red Hat) or
**`update-ca-certificates`** (Debian). For public-facing servers, **Let's
Encrypt** with the `certbot` client automates issuance and renewal for free.

> Watch certificate **expiry**. An expired certificate breaks TLS even though the
> key and configuration are otherwise fine — `openssl x509 ... -noout -dates`
> shows the validity window, and monitoring it prevents outages.

## Hashing for integrity

To confirm a download wasn't corrupted or tampered with, compare its hash against
a published value:

```
$ sha256sum ubuntu.iso
e3b0c442...  ubuntu.iso
$ sha256sum -c SHA256SUMS      # verify files against a checksum list
```

Use **SHA-256** (or stronger). **MD5** and **SHA-1** are considered broken for
security — you may still *see* `md5sum`, but don't rely on it to detect malicious
tampering.

## GPG (GnuPG)

**GPG** is the open implementation of OpenPGP, used to encrypt, decrypt, sign and
verify files and email. Like TLS it uses key pairs, but trust is established
through a **web of trust** (users signing each other's keys) rather than a
hierarchical CA.

Generate and share keys:

```
$ gpg --full-generate-key          # create your key pair
$ gpg --list-keys                  # show public keys in your keyring
$ gpg --export -a "Jordan" > jordan.asc    # export your public key (ASCII)
$ gpg --import alex.asc            # import someone else's public key
```

Encrypt *to a recipient's public key* so only their private key can open it:

```
$ gpg -e -r alex@example.com report.pdf    # produces report.pdf.gpg
$ gpg -d report.pdf.gpg > report.pdf       # recipient decrypts
```

Sign to prove authenticity and integrity:

```
$ gpg --sign release.tar.gz                # embedded signature
$ gpg --detach-sign release.tar.gz         # separate .sig file
$ gpg --verify release.tar.gz.sig release.tar.gz
```

> Remember the direction: you **encrypt with the recipient's public key** (only
> they can decrypt) and **sign with your own private key** (anyone can verify with
> your public key). Mixing these up is a favorite exam trap.

## Encryption at rest

Beyond individual files, whole block devices can be encrypted with **LUKS**,
managed by `cryptsetup`. `cryptsetup luksFormat /dev/sdb1` encrypts a partition
and `cryptsetup open` unlocks it into a mappable device — the standard way to
protect data on a disk that could be stolen.

## Exam focus

- **Asymmetric** crypto uses a public/private **key pair**; **symmetric** uses one
  shared key; **hashing** is one-way and checks *integrity*, not confidentiality.
- TLS certificate flow: **private key → CSR → CA-signed certificate** (or a
  **self-signed** cert for internal use). The trust chain is root CA →
  intermediate → server cert. Certificates are usually **PEM** text.
- `openssl` is the Swiss-army tool: `genpkey` (key), `req` (CSR / `-x509`
  self-signed), `x509 -text -noout` (inspect), `s_client` (test a live port).
  Trust a CA with `update-ca-trust` / `update-ca-certificates`; **certbot** =
  Let's Encrypt automation. Watch for **expiry**.
- Verify downloads with **`sha256sum`** (`-c` against a list); treat **MD5/SHA-1**
  as broken.
- GPG: encrypt with the **recipient's public key**, decrypt with their private
  key; **sign with your private key**, verify with the signer's public key.
  `gpg -e -r`, `gpg -d`, `gpg --detach-sign`, `gpg --verify`, `gpg --import`.
- **LUKS/`cryptsetup`** provides full-disk/partition encryption at rest.
