# Identity, Access Control & Data Classification

Protecting information starts with two questions: *who is allowed to touch this
data?* and *how sensitive is it in the first place?* Access control answers the
first; data classification answers the second, and the two work together — you
classify data so you know how strongly to control access to it. This lesson
covers the mechanics of identity and access, and the classification that tells
you how much protection each asset deserves.

## The four steps: identification to accountability

Every access decision follows the same sequence. CISA uses the shorthand **IAAA**.

> - **Identification** — the user **claims** an identity (a username).
> - **Authentication** — the user **proves** that claim (a password, token, or
>   fingerprint).
> - **Authorization** — the system **permits** the authenticated user to do only
>   what their rights allow.
> - **Accounting (accountability)** — the system **logs** what was done, tying
>   actions back to the identity.

Keep the order straight: you *claim*, then *prove*, then are *permitted*, then are
*held accountable*.

### Authentication factors and MFA

Authentication draws on three classic factor categories:

- **Something you know** — a password, PIN, or passphrase.
- **Something you have** — a hardware token, smart card, or one-time code.
- **Something you are** — a biometric (fingerprint, iris, face).

(Context factors like *somewhere you are* and *something you do* are sometimes
added.) The rule the exam hammers:

> **Multi-factor authentication (MFA)** requires two or more factors from
> **different categories**. A password plus a hardware-token code (know + have) is
> true MFA; a PIN plus a fingerprint (know + are) is true MFA. **Two passwords —
> or a password and a security question — are the same category, so that is still
> single-factor.**

## Access control principles and models

Two principles govern *how much* access to grant:

> **Least privilege** gives each user only the access **strictly necessary** to
> perform their job — no more. **Need-to-know** limits access to the specific
> information required for a task. Together they shrink what any one compromised
> account can reach.

The main access control **models** describe who sets permissions:

| Model | Who decides access | Characteristic |
|-------|--------------------|----------------|
| **DAC** (discretionary) | The resource **owner** grants access at their discretion | Flexible, common in business |
| **MAC** (mandatory) | The **system** enforces access by **labels/clearance** | Rigid, used in high-security/military |
| **RBAC** (role-based) | Access is tied to the user's **role/job function** | Scales well, eases administration |

### The access lifecycle and its biggest risk

Access must be managed over a user's whole lifecycle — **granted** when they join,
**changed** when they move roles, and **revoked** promptly when they leave. The
most-tested failure is neglecting ongoing review:

> If user access rights are **never reviewed** after being granted, the greatest
> risk is **privilege creep** — users accumulate excessive or inappropriate access
> over time, including lingering access for people who **changed roles or left the
> organization**. Regular **access recertification** (periodic reviews by data
> owners) is the control that catches it.

Timely **de-provisioning** of terminated users is especially critical: a departed
employee whose access still works is a serious, and very common, audit finding.

## Data classification

You can't protect everything equally, and you shouldn't try. **Classification**
sorts data by sensitivity so protection can be proportionate.

> The purpose of a **data classification scheme** is to ensure data receives a
> level of protection **appropriate to its sensitivity and value**. Public
> marketing copy and customer financial records should not get the same controls.

Who sets the label is testable and consistent with the roles from Domain 2:

> The **data owner** (a business role) **assigns the classification level**; the
> **custodian** (often IT) **protects the data according to that classification**.
> Owner decides, custodian safeguards.

Typical schemes use tiers like **public → internal → confidential → restricted**
(commercial) or **unclassified → confidential → secret → top secret**
(government). The auditor's key test is **alignment**:

> Controls must **track the classification**. Finding **highly sensitive data
> stored without encryption** while trivial public data is heavily protected is a
> red flag — **protection controls are not aligned with the classification**.

Classification also drives **retention and disposal**. How long data is kept is
not a matter of convenience:

> Record **retention periods** are determined **primarily by legal, regulatory,
> and business requirements** — not by available storage or habit. At end of life,
> data must be **securely disposed of** (wiped, degaussed, or destroyed) so it
> can't be recovered.

## Exam focus

- **IAAA**: **Identify** (claim) → **Authenticate** (prove) → **Authorize**
  (permit) → **Account** (log).
- **MFA** needs factors from **different categories** (know/have/are); two of the
  same category is still **single-factor**.
- **Least privilege** and **need-to-know** minimize access. Know **DAC** (owner
  grants), **MAC** (label/clearance enforced by system), **RBAC** (access by
  role).
- No periodic access review → **privilege creep** and lingering access for
  transferred/terminated users; fix it with **access recertification** and prompt
  **de-provisioning**.
- **Data owner classifies**; **custodian protects** per classification. Controls
  must **match sensitivity**; **retention** is set by **legal/regulatory/business**
  requirements, with secure disposal at end of life.
