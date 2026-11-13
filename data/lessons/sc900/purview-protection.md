# Information Protection & Data Lifecycle

Once Microsoft Purview knows *what* data you have (the previous lesson), it can
**protect** that data and manage it through its whole life. This lesson covers two
related areas: **information protection** — **sensitivity labels** that classify
and protect content, and **data loss prevention (DLP)** that stops it leaking —
and **data lifecycle management** — **retention** and **records management** that
control how long content is kept.

## Sensitivity labels

The cornerstone of Purview information protection is the **sensitivity label**.

> A **sensitivity label** classifies and protects documents and emails by tagging
> them with a label such as **Public**, **General**, **Confidential** or **Highly
> Confidential**. The label can enforce protection — **encryption** and usage
> restrictions — and add **visual markings** like headers, footers and
> **watermarks**.

The powerful part is that the label **travels with the content**. Apply
"Confidential" with encryption to a file, and even if it is emailed outside the
company or copied to a USB stick, the protection and markings go with it.

Key points about labels:

- Labels are **customizable** — you define the names and what each one does.
- They can be applied **manually** by users, **automatically** based on
  classification (the SITs and trainable classifiers from the last lesson), or
  **recommended** to the user.
- One label can do several jobs at once: mark the document visually, encrypt it,
  and restrict who can open or forward it.

Think of a sensitivity label as a sticker that is also a lock: it says how
sensitive something is **and** enforces the handling rules.

## Data loss prevention (DLP)

Labels protect individual items; **DLP** stops sensitive data from leaving by
accident.

> **Data loss prevention (DLP)** detects and prevents the risky or accidental
> **sharing, transfer or use** of sensitive information. A DLP policy can block or
> warn when someone tries to send protected data outside the organization.

A classic example: a user tries to email a spreadsheet full of credit card numbers
to an external address, or paste it into a Microsoft Teams chat. A DLP policy
recognizes the sensitive content (again, via sensitive information types or
labels) and **blocks it, warns the user, or allows it with justification** —
across email, Teams, SharePoint, OneDrive and endpoints.

DLP is the enforcement that acts on classification: classification *finds* the
credit card numbers; DLP *stops them walking out the door.*

## Data lifecycle management: retention

Data should not live forever, nor should it be deleted too soon. Regulations often
require keeping certain records for a fixed number of years, then disposing of
them. **Data lifecycle management** handles this with retention.

> **Retention labels and retention policies** enforce **how long content is kept
> and when it is deleted**. A retention policy applies retention settings broadly
> (e.g. to an entire SharePoint site or mailbox); a retention label applies them
> to **individual items**.

Retention does two jobs that sound opposite but work together:

- **Retain** content for a required period — so it cannot be deleted prematurely
  (useful for legal and regulatory obligations).
- **Delete** content after its retention period ends — so you are not hoarding
  data you no longer need (which is itself a risk).

Example: *keep financial records for seven years, then automatically delete them.*

## Records management

Some content needs a stronger guarantee than ordinary retention — it must be
formally declared a **record** to satisfy legal and regulatory requirements.

> **Records management** lets an organization formally declare items as
> **records**, applying stricter controls such as **immutability** (records can't
> be edited or deleted during their retention) and **disposition review** (a human
> review before a record is finally deleted at the end of its lifecycle).

Records management is retention with teeth: the highest-stakes documents are
locked down, tracked, and reviewed before disposal, which is exactly what
compliance regimes for financial, legal and healthcare records demand.

## Putting the protection story together

| Capability | Job |
|------------|-----|
| **Sensitivity labels** | Classify + protect items (encryption, markings); travels with the content |
| **Data loss prevention (DLP)** | Prevent accidental/risky sharing of sensitive data |
| **Retention labels & policies** | Control how long content is kept, then delete it |
| **Records management** | Formally declare records; immutability + disposition review |

Notice how each builds on classification from the previous lesson: you **find**
sensitive data (classification), **label and protect** it (sensitivity labels),
**stop it leaking** (DLP), and **govern its lifespan** (retention and records).

## The whole thing in one paragraph

Microsoft Purview **information protection** centers on **sensitivity labels**,
which classify and protect documents and emails with **encryption** and **visual
markings** and travel with the content, and on **data loss prevention (DLP)**,
which **blocks or warns** when sensitive data is shared inappropriately across
email, Teams and more. **Data lifecycle management** uses **retention labels and
policies** to control **how long content is kept and when it is deleted**, while
**records management** formally declares items as **records** with **immutability**
and **disposition review** for the strictest legal and regulatory obligations.

## Exam focus

- **Sensitivity labels** classify **and protect** documents/emails — they can
  **encrypt**, restrict usage, and add **headers/footers/watermarks**, and the
  protection **travels with the file.**
- **Data loss prevention (DLP)** = prevent **accidental or risky sharing** of
  sensitive data (e.g. block emailing credit card numbers externally or in Teams).
- **Retention labels and policies** control **how long content is retained and
  when it's deleted** (policy = broad scope; label = individual items).
- **Records management** = formally declare **records** with **immutability** and
  **disposition review** to meet legal/regulatory requirements.
- Everything builds on classification: **find → label/protect → prevent leaks →
  govern lifecycle.**
