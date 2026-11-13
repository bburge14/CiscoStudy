# Data Classification, Handling & Security Awareness

Data is the asset most organizations actually care about, and people are the
control most often overlooked. This lesson pairs two subjects that together close
a lot of the gap between policy and practice: how to **classify and handle data**
safely through its whole lifecycle, and how to build the **security awareness**
that makes the humans around that data a line of defense rather than the weakest
link.

## Classifying data: not all data is equal

The first step in protecting data is deciding how sensitive it is. **Data
classification** assigns a label that drives the handling rules.

> **Classification** is the process of categorizing data by sensitivity (and
> sometimes by criticality) so that appropriate controls can be applied. The more
> sensitive the class, the stronger the required protection.

Typical commercial labels, from least to most sensitive: **Public ->
Sensitive -> Confidential -> Restricted**. Government/military labels run
**Unclassified -> Confidential -> Secret -> Top Secret.** The exact words matter
less than the principle: the label determines who may access the data and how it
must be stored, transmitted, and destroyed.

### Who does what: data roles

The exam is strict about separating accountability from implementation:

- **Data owner** — a senior/business role **accountable** for the data. The owner
  *classifies* it and approves who may access it. Accountability can't be
  delegated.
- **Data custodian** — the IT staff who **implement and maintain** the controls
  the owner specifies (backups, encryption, access settings).
- **Data steward** — responsible for data **quality** and proper business use.
- **Data processor** — a party that processes data on behalf of the owner
  (relevant under privacy law).

A reliable tell: *deciding* the classification and *who gets access* is the
**owner**; *doing* the day-to-day protection is the **custodian**.

## The three states of data

Data must be protected in all three of its states, and each needs different
controls:

| State | Meaning | Primary protection |
|-------|---------|--------------------|
| **At rest** | Stored on disk, in a database, on a backup | Encryption (e.g., full-disk, database encryption) |
| **In transit (in motion)** | Moving across a network | Transport encryption (TLS, IPsec, VPN) |
| **In use** | Loaded in memory, being processed | Access controls, memory protection, secure enclaves |

A **Data Loss Prevention (DLP)** system enforces handling rules by inspecting
content and blocking unauthorized movement of sensitive data — for example,
stopping a file tagged "Confidential" from leaving over email or a USB drive. DLP
is most associated with protecting **data in transit** at the boundary, though
modern DLP also covers endpoints (in use) and storage (at rest).

## Handling data across its lifecycle

Classification labels drive concrete handling rules: marking, storage,
transmission, **retention**, and ultimately **destruction**. Two points the exam
hits hard:

- **Retention** — keep data only as long as policy or law requires, then dispose
  of it. Keeping data forever is a liability, not an asset.
- **Media sanitization** — when media is retired or reassigned, the data on it
  must be rendered unrecoverable. The standard reference is **NIST SP 800-88**,
  which defines three escalating levels:

> **Clear** overwrites data using standard read/write commands (resists
> keyboard-level recovery). **Purge** applies stronger techniques — such as
> cryptographic erase or degaussing — that resist even advanced laboratory
> recovery while the media may still be reusable. **Destroy** physically
> annihilates the media (shred, incinerate, pulverize) so it can never be reused.

Choose the level by the data's sensitivity and whether the media will be reused.
Note that **degaussing** works on magnetic media (hard drives, tapes) but **not**
on solid-state drives — SSDs rely on **cryptographic erase** or physical
destruction.

## Security awareness: turning people into a control

Technology can't stop a user who hands over their password to a convincing
phisher. **Security awareness** programs change behavior. The exam uses a specific
three-level model — know the distinctions:

> **Awareness** changes what people *notice* (broad, short, for everyone — posters,
> reminders, the phishing banner). **Training** teaches *specific skills* for a
> job ("how to securely configure this server"). **Education** is the broadest,
> long-term, concept-level learning (a degree or deep professional study).

- **Awareness** is the "what" — brief and universal; it keeps security top of
  mind.
- **Training** is the "how" — job-related and skill-building. Giving developers
  dedicated secure-coding instruction is **role-based training** targeted to a
  function.
- **Education** is the "why" at depth — understanding principles, not just
  procedures.

Effective programs are **role-based** (a developer, an executive, and a help-desk
agent need different content), **continuous** (not a once-a-year checkbox), and
**measured**. A common, powerful technique is the **simulated phishing campaign**:
send benign fake phishes and coach whoever clicks. Social-engineering defense —
recognizing phishing, pretexting, tailgating, and vishing — is one of the highest
return topics any awareness program can cover, because people are the attacker's
favorite entry point.

## Exam focus

- **Classification** drives handling: the label sets who may access data and how
  it's stored, moved, and destroyed.
- **Data owner = accountable**, classifies the data and approves access (senior/
  business role). **Data custodian = IT** that implements and maintains the
  controls. Don't swap them.
- Protect data in **three states**: **at rest** (storage encryption), **in transit**
  (TLS/IPsec/VPN), **in use** (access control / memory protection). **DLP** blocks
  unauthorized movement of sensitive data.
- **NIST SP 800-88** sanitization: **Clear** (overwrite) < **Purge** (crypto
  erase/degauss, resists lab recovery) < **Destroy** (physical). **Degaussing**
  doesn't work on **SSDs** — use crypto erase or destruction.
- Awareness model: **Awareness** (broad, everyone) -> **Training** (job-specific
  skills) -> **Education** (deep, conceptual). Secure-coding class for devs =
  **role-based training**. **Simulated phishing** is a key awareness tool.
