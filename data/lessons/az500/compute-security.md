# Secure Compute & Disk Encryption

Virtual machines are still where a lot of sensitive workloads run, and their disks
hold the data an attacker ultimately wants. Securing compute means two things:
**hardening the VM** so it is a smaller target, and **encrypting its disks** so a
stolen copy is worthless. The disk-encryption options confuse people because Azure
offers several that overlap — so we separate them carefully.

## Hardening the virtual machine

Before encryption, reduce the attack surface:

- **Trusted launch** — enable **Secure Boot** and a **vTPM** so the VM boots only
  trusted, signed code and can attest its integrity, defending against rootkits and
  boot-level malware.
- **Patch and configure** — keep the OS current with **Azure Update Manager** and
  assess OS settings against the **Microsoft Cloud Security Benchmark** (surfaced
  by Defender for Cloud).
- **No secrets on disk** — give the VM a **managed identity** so it fetches
  secrets from Key Vault at runtime rather than storing credentials locally.
- **No exposed management ports** — reach VMs through **Azure Bastion** and,
  where available, **just-in-time VM access** (covered with Defender for Cloud),
  not internet-facing RDP/SSH.
- **Endpoint protection** — **Microsoft Defender for Servers** brings EDR (via
  Microsoft Defender for Endpoint) and vulnerability assessment to VMs; the plan
  details live in the Security Operations unit.

## Encryption at rest: it's already on

Every **managed disk** is encrypted at rest by default with **server-side
encryption (SSE)**, using **platform-managed keys (PMK)** that Microsoft handles
transparently. You never see a plaintext disk in storage. The question is how much
*control* and *coverage* you need beyond that default.

### Three ways to encrypt a VM's disks

| Option | Where encryption happens | Keys | What it covers |
|--------|--------------------------|------|----------------|
| **SSE with PMK** (default) | Azure storage service | Microsoft | OS & data **managed disks** at rest |
| **SSE with CMK** | Azure storage service | **Your key** in Key Vault, via a **disk encryption set** | OS & data managed disks at rest, with key control |
| **Azure Disk Encryption (ADE)** | **Inside the guest OS** | Your key in Key Vault | OS & data volumes via **BitLocker** (Windows) / **dm-crypt** (Linux) |
| **Encryption at host** | **On the VM host** | PMK or CMK | Disk data **plus temp disks and disk caches**, end to end from host to storage |

Reading that table is most of the battle, so here is the plain-English version:

- **Server-side encryption with customer-managed keys (CMK)** keeps the same
  platform encryption but lets *you* own the key. You create a **disk encryption
  set** that references a key in **Azure Key Vault**, so you can rotate it and
  revoke access. Revoking the key makes the disks unreadable — powerful, but handle
  with care.
- **Azure Disk Encryption (ADE)** does the encryption **inside the VM** using the
  OS's own tools — **BitLocker** on Windows, **dm-crypt** on Linux — with keys
  stored in Key Vault. Choose it when a requirement specifically calls for
  **BitLocker/dm-crypt** or guest-level volume encryption.
- **Encryption at host** encrypts data starting on the **physical host** before it
  is written anywhere, and uniquely covers the **temp disk and the OS/data disk
  caches** as well. It does not use BitLocker/dm-crypt and adds no guest overhead.
- **Double encryption at rest** layers two encryption passes (infrastructure +
  service) for regulatory requirements that demand two independent layers.

### Picking the right one

- "Encrypt disks with **BitLocker/dm-crypt**" ⇒ **Azure Disk Encryption**.
- "Encrypt the **temp disk and caches**, end-to-end from the host" ⇒ **encryption
  at host**.
- "We must **control and rotate the key** ourselves" ⇒ **CMK** with a disk
  encryption set (combine with ADE or encryption at host).
- "Two independent layers of encryption at rest" ⇒ **double encryption**.

## Confidential computing

For the highest assurance, **Azure confidential computing** protects data **in
use**: confidential VMs run inside hardware-based **trusted execution environments
(TEEs)** so memory is encrypted and shielded even from the host and Azure
operators. **Confidential disk encryption** binds the OS disk key to the VM's
virtual TPM. This is beyond everyday workloads but worth recognizing as the
"data-in-use" answer.

## Controlling access to the disks themselves

Encryption protects data at rest, but a managed disk can also be **exported** (a
temporary SAS URL that downloads the VHD) — a quiet exfiltration path if left
open. Harden the disk resource too:

- Set the disk's **network access policy** to **deny public export** or require a
  **disk access** resource reached over a **private endpoint**, so a VHD can't be
  pulled to the open internet.
- Govern who can generate export SAS with **RBAC**, and watch disk operations in
  the **Activity log**.

Also prefer **ephemeral OS disks** for stateless, immutable VMs where appropriate,
and remember that **snapshots and images** inherit the sensitivity of their source
disk — they need the same encryption and access controls, not less.

## Putting it together

Harden the VM first — **trusted launch** (Secure Boot + vTPM), prompt patching
with **Update Manager**, **managed identities** instead of stored secrets, Bastion
and JIT instead of open ports, and **Defender for Servers** for EDR. Then encrypt:
every managed disk is already encrypted with **platform-managed keys**, and you
escalate as requirements demand — **CMK** for key ownership (via a disk encryption
set and Key Vault), **Azure Disk Encryption** for BitLocker/dm-crypt inside the
guest, and **encryption at host** to also cover temp disks and caches end-to-end.
**Confidential computing** adds protection for data *in use*.

## Exam focus

- **Managed disks are encrypted at rest by default** with **platform-managed keys
  (SSE/PMK)** — no action needed for baseline at-rest encryption.
- **CMK** = your key in **Key Vault** referenced by a **disk encryption set**; use
  it when you must **own, rotate, or revoke** the key.
- **Azure Disk Encryption (ADE)** encrypts **inside the guest** with **BitLocker
  (Windows) / dm-crypt (Linux)**; the answer when BitLocker/dm-crypt is named.
- **Encryption at host** uniquely covers **temp disks and disk caches** end-to-end
  from the host and adds no guest-OS overhead.
- **Double encryption at rest** = two independent layers for strict compliance.
- Hardening staples: **trusted launch (Secure Boot + vTPM)**, **Update Manager**,
  **managed identity for secrets**, **Bastion/JIT** instead of exposed RDP/SSH.
- **Confidential computing / confidential VMs (TEEs)** protect data **in use**.
