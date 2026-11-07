# Security Concepts & Windows Security

This lesson has two halves that fit together. First the **concepts** every
technician shares — how we prove *who* someone is, how we keep intruders out
physically, and the golden rule of "only as much access as needed." Then the
**Windows-specific features** that put those concepts into practice: firewall,
encryption, UAC, and permissions.

## Authentication: the factor categories

Authentication asks "are you really who you claim to be?" and the answer comes from
one or more **factor categories**:

- **Something you know** — a password, PIN, or security question.
- **Something you have** — a phone running an authenticator app, a smart card, or a
  hardware **keyfob** that shows a rotating one-time code.
- **Something you are** — a biometric: fingerprint, face, iris.
- (Minor extras: **somewhere you are** — location; **something you do** — behavior.)

**Multi-factor authentication (MFA)** means combining **two or more *different*
categories** — not two passwords.

> A password **plus** a one-time code from an authenticator app = *something you
> know* **+** *something you have*. That mix of **two categories** is what makes it
> MFA.

A physical **keyfob that displays a rotating six-digit code** is a textbook
*something you have*. Two passwords would **not** be MFA, because they're both the
same category.

## Physical security

Keeping the wrong people away from the hardware is its own layer:

- **Access control vestibule (mantrap)** — a small two-door room where the **outer
  door must close and the person be verified before the inner door opens**. It
  stops tailgating by letting one verified person through at a time.
- **Badge readers / smart-card locks**, **biometric locks**, **PIN pads** on doors.
- **Bollards, fences, lighting, cameras, security guards** around the perimeter.

> The "two-door room, outer closes before inner opens" description is always the
> **access control vestibule** (mantrap).

## Least privilege and Active Directory housekeeping

The single most important access rule:

> **Principle of least privilege** — every user and service gets the **minimum
> rights required to do its job, and no more.** Fewer rights means a compromised
> account can do less damage.

In an Active Directory domain you'll also meet **folder redirection**: pointing a
user's **Documents** folder to a **network file server** so it lives centrally and
gets **backed up** with the server — the user still sees it as their Documents, but
it physically resides on the server. Related AD tools include **Group Policy**
(push settings), **login scripts**, and **organizational units** for grouping
accounts.

## Windows security features

Now the toolbox Windows gives you.

### Windows Defender (Antivirus + Firewall)

**Microsoft Defender Antivirus** is the built-in real-time anti-malware engine.
**Windows Defender Firewall** filters network traffic by rule. When you need to
**block inbound connections on a specific TCP port** using only built-in tools,
that's a **Windows Defender Firewall** inbound rule — no third-party product
required.

### Encryption: BitLocker, BitLocker To Go, and EFS

Windows encrypts **data at rest** two ways, and the exam pairs them:

| Feature | What it encrypts |
|---------|------------------|
| **BitLocker** | an **entire volume** (often with a TPM chip holding the key) |
| **BitLocker To Go** | **removable drives** — USB flash drives, external disks |
| **EFS** (Encrypting File System) | **individual files/folders** on NTFS |

> **The two built-in features that protect data at rest by encrypting it are
> BitLocker and EFS.** BitLocker is whole-volume; EFS is file-level.

So "encrypt data copied to **USB flash drives** so a lost drive can't be read" →
**BitLocker To Go**. "Encrypt **just a few files** so only my account opens them" →
**EFS**. "Encrypt the **whole system drive**" → **BitLocker**.

### UAC (User Account Control)

When a program tries to make a system change, Windows **dims the screen** (the
secure desktop) and prompts for **consent or an administrator password** before
proceeding. That's **UAC** — it keeps even admins running with standard rights
until elevation is genuinely needed.

### NTFS vs. share permissions (the recap that keeps mattering)

Shared folders carry two permission sets, and across the network the **effective
permission is the most restrictive of the two**:

> NTFS **Full Control** but Share **Read**, accessed over the network → the user
> effectively gets **Read**. The tighter permission always wins.

Locally (at the keyboard) only **NTFS** applies; share permissions are ignored
unless you're coming in over the network. When combining *multiple* NTFS entries
for a user, those accumulate — but an explicit **Deny** overrides any Allow.

### Account and policy hardening (preview)

Windows also exposes **Local Security Policy** / Group Policy for **account lockout**
(lock after N bad attempts), **password policy** (length, complexity, expiration),
and more. Those belong to workstation hardening, covered next unit-lesson, but know
they live here in the Windows security stack.

## The whole thing in one paragraph

Authentication draws on factor **categories** — know, have, are — and **MFA** means
mixing **two different categories** (a password plus an authenticator code, or a
rotating-code keyfob). Keep people out physically with an **access control
vestibule** (two doors, verify before the inner opens) and badge/biometric locks,
and keep access tight with **least privilege**. In Windows, the **Defender
Firewall** blocks ports with inbound rules, **BitLocker** encrypts whole volumes
(**BitLocker To Go** for USB), **EFS** encrypts individual files — BitLocker and
EFS being the two data-at-rest encryptors — **UAC** prompts before system changes,
and network access is capped by the **most restrictive** of NTFS vs. share
permissions.

## On the exam

- MFA requires **two different factor categories**. Password + authenticator app =
  **know + have**; a rotating-code **keyfob** = *something you have*. Two passwords
  is **not** MFA.
- The two-door "verify before inner door opens" room is the **access control
  vestibule (mantrap)**; **least privilege** = minimum rights needed.
- **Folder redirection** puts a user's Documents on a central server for backup.
- Windows features: **Defender Firewall** blocks a port, **BitLocker** = whole
  volume, **BitLocker To Go** = USB/removable, **EFS** = individual files; **the
  two encrypt-at-rest features are BitLocker and EFS**; **UAC** = the elevation
  prompt.
- Share vs. NTFS over the network → **most restrictive wins** (Full Control + Read
  = Read); only NTFS applies locally, and an explicit **Deny** beats any Allow.
