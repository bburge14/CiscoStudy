# Data Lifecycle, States & Protection Methods

Data is not static. It is created, stored, used, shared, archived, and eventually
destroyed — and at every stage it exists in one of three *states*, each needing a
different control. A CISSP must protect data appropriately throughout that journey
and, just as importantly, dispose of it so it cannot be recovered. This lesson
covers the data states, the lifecycle, the protection techniques, and the right
way to sanitize media.

## The three data states

Where data lives at a given moment determines how you protect it.

> **Data at rest** sits in storage (disks, databases, backups). **Data in transit**
> moves across a network. **Data in use** is loaded in memory and being actively
> processed.

| State | Primary control |
|-------|-----------------|
| **At rest** | Storage/disk/database encryption (AES), access controls |
| **In transit** | **TLS**, **IPsec/VPN** — encrypt the channel end to end |
| **In use** | Hardest to protect; secure enclaves / trusted execution, strict memory handling, tokenization |

The most common exam cue: sensitive records moving between a browser and an
application server across the internet are **in transit**, and the right control
is **TLS** (or a VPN/IPsec tunnel). Records on the server's disk are **at rest**
and want storage encryption. Don't reach for disk encryption when the scenario is
clearly about a network path.

## The data lifecycle and retention

Think of data as moving through stages: **create → store → use → share → archive →
destroy** (some models phrase it collect, retain, and dispose). Each stage has its
own risks — sharing invites leakage, archiving invites forgotten exposure.

**Retention** is a governance decision with legal teeth:

> Keep data **only as long as it is needed** for business or law, then dispose of
> it. Keeping data too long increases breach exposure and discovery cost; disposing
> of it too soon can violate regulations or destroy evidence.

A **legal hold** suspends normal destruction when litigation is anticipated —
deleting data under hold (even on a routine schedule) can constitute spoliation.
Retention schedules should be driven by the data's classification and the laws that
apply to it.

## Protection methods

Beyond encryption, several techniques reduce the sensitivity of data so that a
leak matters less. Know what each does and what it preserves.

- **Encryption** — reversible with a key; protects confidentiality in any state.
- **Tokenization** — replaces a sensitive value with a non-sensitive **token**,
  with the real value held in a separate secured vault. Common for payment card
  data; the token has no exploitable mathematical relationship to the original.
- **Masking** — hides part of a value for display (showing `****-****-****-1234`).
- **Anonymization** — irreversibly removes identifiers so data can no longer be
  tied to an individual (and, done properly, falls outside privacy law).
- **Pseudonymization** — replaces identifiers with a reversible alias; still
  personal data under GDPR because re-identification is possible.
- **Obfuscation** — broadly, making data harder to interpret.
- **DLP (Data Loss Prevention)** — inspects data in motion, at rest, and at
  endpoints to detect and block unauthorized exfiltration based on classification
  and patterns.
- **DRM (Digital Rights Management)** — enforces usage rules (view, print, expire)
  that follow the file after it leaves your environment.

> Exam distinction: **tokenization** swaps a value for a vaulted token;
> **anonymization** destroys the link to a person (irreversible);
> **pseudonymization** is reversible, so it is still regulated personal data.

## Data remanence and secure sanitization

When media reaches end of life, the data must not be recoverable. **Data
remanence** is the residual data that lingers after a naive delete — which only
removes pointers, leaving the bits readable. **NIST SP 800-88 Rev. 1** defines
three levels of sanitization:

| Level | What it means | When to use |
|-------|---------------|-------------|
| **Clear** | Overwrite via the normal interface | Media reused inside the organization, low risk |
| **Purge** | Stronger techniques (cryptographic erase, the drive's built-in secure-erase, or **degaussing for magnetic media**) that defeat lab recovery | Media leaving the org or changing security level |
| **Destroy** | Physically ruin the media (shred, pulverize, incinerate, disintegrate) | Highest assurance |

Two heavily tested traps:

- **Degaussing works only on magnetic media** (HDDs, tapes). It uses a strong
  magnetic field and does **nothing** reliable to flash-based **SSDs**. For SSDs,
  use **cryptographic erase** (destroy the encryption key so the ciphertext is
  useless) or **physical destruction**.
- Degaussing a hard drive also destroys the servo tracks, rendering the drive
  unusable — which is fine for disposal but not for reuse.

> For SSDs holding confidential data, the BEST sanitization answers are
> **cryptographic erase** or **physical destruction** — not degaussing, and not a
> single quick-format.

**Cryptographic erase** is elegant: if the whole drive was encrypted, you only
have to securely delete the key. Instantly, terabytes become unrecoverable noise.

## Data location and sovereignty

Where data physically lives is a control in its own right. **Data sovereignty**
means data is subject to the laws of the country where it is **stored** — a record
held in an EU data center falls under EU law regardless of where the company is
headquartered. **Data residency** requirements may force data to remain within a
specific jurisdiction. Together these shape cloud-region choices and the cross-
border transfer mechanisms that make international processing lawful (recall the
EU–US Data Privacy Framework from the compliance lesson). They are a frequent
reason the "store it in the cheapest region" answer is wrong.

## Exam focus

- Three states: **at rest** (storage encryption), **in transit** (**TLS / IPsec /
  VPN**), **in use** (enclaves, hardest to protect). Match the control to the
  state — "moving across the internet" = in transit = TLS.
- **Retention**: keep data only as long as needed; a **legal hold** overrides
  routine destruction.
- Protection methods: **tokenization** (vaulted substitute), **masking** (hide
  part for display), **anonymization** (irreversible), **pseudonymization**
  (reversible, still personal data), **DLP** (detect/block exfiltration), **DRM**
  (usage control that follows the file).
- **NIST SP 800-88**: **Clear → Purge → Destroy.** **Degaussing is magnetic-media
  only**; for **SSDs** use **cryptographic erase or physical destruction**.
- **Data remanence** is the residue a simple delete leaves behind — the reason
  real sanitization is required.
- **Data sovereignty/residency**: data obeys the laws of **where it is stored**,
  shaping cloud-region and cross-border transfer decisions.
