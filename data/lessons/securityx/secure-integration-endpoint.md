# Secure Integration & Endpoint/System Security

Enterprises are built from systems talking to other systems, and from endpoints
that are the first thing an attacker touches. This lesson covers two engineering
problems: integrating applications, APIs, and protocols **securely**, and hardening
**endpoints and specialized systems** (including IoT/OT) with hardware roots of
trust. Both are about shrinking what an attacker can reach and verifying trust
at every hop.

## Secure integration: APIs, protocols, and gateways

Integration is where trust boundaries meet. The architect's job is to let systems
exchange data and function without exposing credentials, data, or control.

### Delegated authorization with OAuth

A recurring scenario: a web app must let users grant a **third-party service
limited, revocable access** to specific data in the app's API **without sharing the
users' passwords**. The answer is **OAuth 2.0** — the user authorizes a scoped,
revocable access token; the third party never sees the password, and the user can
revoke access at any time. (For the *authentication* layer on top, **OIDC**.)

> "Grant a third party limited, revocable API access without sharing the password"
> = **OAuth 2.0** (delegated authorization with scoped tokens).

### The API gateway

When an enterprise exposes many internal microservice APIs to partners, it needs
**one enforcement point** rather than per-service security. An **API gateway**
centralizes **authentication, authorization, TLS termination, rate limiting**,
schema validation, and logging — a single, consistent chokepoint that also
simplifies the back-end services. Pair it with an **mTLS**-secured service mesh for
service-to-service trust internally.

### Secure protocols and forward secrecy

Choose protocols that authenticate and encrypt:

- **TLS 1.3** for data in transit — it removed legacy ciphers and mandates
  **ephemeral key exchange (PFS)**.
- **SSH** (not Telnet), **SFTP/FTPS** (not FTP), **DNSSEC** for DNS integrity,
  **SNMPv3** (not v1/v2c), **LDAPS**, **HTTPS**.
- **Perfect Forward Secrecy (PFS)** is a protocol property worth calling out: if a
  compliance rule says a compromised long-term private key must **not** make
  previously recorded sessions decryptable, you require **PFS** via ephemeral
  Diffie-Hellman (**ECDHE**). Each session gets a unique ephemeral key, so there is
  no master key to unlock the archive.

> If "a stolen long-term key must not decrypt past recorded TLS sessions," the
> requirement is **Perfect Forward Secrecy (ephemeral key exchange)**.

Round out integration security with **input validation** at every boundary,
**message signing**, **webhook verification**, and secrets kept in a **vault**
rather than in code or config.

## Endpoint security: beyond antivirus

Signature antivirus catches known malware; modern threats are **fileless** and use
**living-off-the-land** techniques (abusing built-in tools like PowerShell). You
need behavior-based detection.

- **EDR (Endpoint Detection and Response)** — continuous behavioral monitoring,
  detection of fileless/LOLbin techniques, and the ability to investigate and
  remotely respond (isolate a host, kill a process). EDR is the answer when the
  requirement goes "beyond signature AV" to behavior and response.
- **XDR (Extended Detection and Response)** — correlates EDR with network, identity,
  email, and cloud telemetry for cross-domain detection.
- **Application allowlisting** — only explicitly approved executables run. On a
  hardened kiosk running a **fixed set of applications**, allowlisting is the
  **strongest preventive** control against unknown/unauthorized code (deny by
  default). Its opposite, blocklisting, only stops known-bad.

### Host hardening

Reduce the endpoint's attack surface: remove unneeded software and services,
disable default accounts, apply **CIS Benchmark/STIG** baselines, enforce **full-
disk encryption (FDE)**, host firewall, and patching. **Configuration management**
keeps the baseline from drifting.

## Hardware roots of trust

Software security rests on hardware you can trust to be honest about the system's
state.

- **TPM (Trusted Platform Module)** — a dedicated secure cryptoprocessor on the
  motherboard that stores keys and **platform-integrity measurements**. It anchors
  **full-disk encryption** (e.g., BitLocker) and **measured boot**.
- **Secure Boot** — the UEFI firmware verifies each boot component's signature so
  **unsigned/untrusted code cannot load** during startup, blocking bootkits.
- **Measured Boot / remote attestation** — each boot stage is hashed into the TPM;
  a remote verifier can then **attest** the device booted into a known-good state
  before granting access (a zero-trust device-posture input).
- **HSM** — the enterprise-grade, tamper-resistant key store (covered with PKI); the
  TPM is its per-device cousin.

> **TPM** = per-device secure cryptoprocessor storing keys and integrity
> measurements (anchors FDE and attestation). **Secure Boot** = firmware refuses to
> load unsigned boot code.

## Securing IoT, OT, and specialized systems

Not every system is a patchable server. SecurityX expects you to handle the awkward
ones:

- **OT/ICS/SCADA** — industrial systems prioritize **availability and safety** over
  confidentiality, often run fragile, un-patchable legacy controllers, and use
  protocols with no built-in security. Defend by **network segmentation** (isolate
  OT from IT), **unidirectional gateways/data diodes**, strict monitoring, and
  compensating controls — *not* by aggressive patching that could halt production.
- **IoT** — large fleets of weak, long-lived devices. Change defaults, segment onto
  their own network, and lean on lightweight crypto (**ECC**).
- **Embedded/RTOS, medical, and legacy** systems — wrap them in compensating
  controls (segmentation, monitoring, access restriction) when they cannot be
  secured directly.
- **Mobile** — manage with **MDM/UEM**, enforce encryption and containerization,
  and address **BYOD** with policy and isolation.

> For OT/ICS and unpatchable legacy systems, the default control is
> **segmentation + monitoring + compensating controls**, because availability/safety
> outrank patching and the devices often cannot be changed.

## Exam focus

- **OAuth 2.0** = delegated, revocable, scoped API access without sharing
  passwords; an **API gateway** is the single enforcement point for authn/authz,
  TLS termination, and rate limiting across many APIs.
- Prefer secure protocols (**TLS 1.3, SSH, SFTP, DNSSEC, SNMPv3**); require **PFS/
  ephemeral key exchange** so a stolen long-term key can't decrypt recorded
  sessions.
- **EDR** = behavior-based detection and response beyond signatures (catches
  fileless/LOLbin); **application allowlisting** is the strongest preventive control
  on fixed-purpose/kiosk hosts (deny by default).
- **TPM** stores keys and integrity measurements and anchors FDE/attestation;
  **Secure Boot** blocks unsigned boot code; **measured boot/attestation** feeds
  zero-trust device posture.
- For **OT/ICS/IoT/legacy**: availability and safety come first, many systems can't
  be patched — segment, monitor, and apply **compensating controls**.
