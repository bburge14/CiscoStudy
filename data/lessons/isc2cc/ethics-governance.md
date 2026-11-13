# The (ISC)² Code of Ethics & Security Governance

A security professional holds a position of trust — they often have the keys to
an organization's most sensitive information. Two things keep that trust in
check: a professional **code of ethics** that binds the individual, and
**governance** documents that set the rules for the whole organization. This
lesson covers both.

## The (ISC)² Code of Ethics

Everyone who earns an (ISC)² certification agrees to abide by its Code of Ethics.
It is short, but it is binding, and the exam expects you to know its structure and
the order of its canons.

> The (ISC)² Code of Ethics has a **preamble** plus **four canons**. The canons
> are listed in a deliberate order of precedence: when two seem to conflict, the
> earlier canon takes priority.

The four canons, in order:

1. **Protect society, the common good, necessary public trust and confidence, and
   the infrastructure.**
2. **Act honorably, honestly, justly, responsibly, and legally.**
3. **Provide diligent and competent service to principals.**
4. **Advance and protect the profession.**

A few points the exam tests:

- There are exactly **four** canons (plus the preamble). If an answer says three
  or five, it's wrong.
- They apply **in order**. The **first canon — protect society** — outranks the
  others. So if protecting the public conflicts with pleasing a client, the
  professional sides with the public.
- "**Principals**" in the third canon means the people you serve — your
  **employers and clients**. Diligent, competent work for them is canon three.
- The Code is **binding**. A member found, through (ISC)²'s peer-review process,
  to have seriously violated it can be **sanctioned, up to and including
  revocation of their certification**.

### Matching scenarios to canons

- A flaw in a water-treatment system that could endanger the public → **canon 1**
  (protect society and the infrastructure).
- Refusing to falsify or hide a finding in a report → **canon 2** (act honestly
  and with integrity).
- Doing careful, high-quality work for your employer or client → **canon 3**
  (diligent, competent service to principals).
- Mentoring newcomers and never misrepresenting your credentials → **canon 4**
  (advance and protect the profession).

A useful memory hook: **Society → Honesty → Principals → Profession.** The order
matters, so practice it until it's automatic.

## Security governance: turning intent into rules

**Governance** is how senior management directs and controls security. It works
through a hierarchy of documents, each with a different level of authority and
detail. People confuse these constantly, so learn the exact distinctions.

> **Policies** state management's intent, **standards** make requirements
> specific and mandatory, **procedures** give the step-by-step how-to, and
> **guidelines** offer optional, recommended advice.

| Document | Mandatory? | What it is | Example |
|----------|-----------|------------|---------|
| **Policy** | Yes | A high-level statement of management's intent and expectations | "We will protect company information." |
| **Standard** | Yes | A specific, required rule that supports a policy | "All laptops must use AES-256 full-disk encryption." |
| **Procedure** | Yes | The exact, ordered steps to accomplish a task | "Steps to reset a locked user account." |
| **Guideline** | No | Recommended, optional best-practice advice | "You should choose a passphrase of several words." |
| **Baseline** | Yes | A minimum set of security settings every system must meet | "Every laptop must have screen lock, disk encryption, and firewall on before issue." |

How to keep them straight:

- A **policy** is broad and says *what* and *why*, not *how*. It's the
  constitution, not the instruction manual.
- A **standard** is a mandatory, specific rule — a particular technology,
  setting, or configuration that *must* be used.
- A **procedure** is a detailed recipe: numbered, repeatable steps. If it reads
  like a checklist, it's a procedure.
- A **guideline** is advisory. The giveaway words are "should," "recommended,"
  or "optional." Guidelines are *not* mandatory.
- A **baseline** defines the minimum acceptable level of security for a class of
  systems — the floor everyone must clear.

> The single biggest tell: **guidelines are optional; policies, standards,
> procedures, and baselines are mandatory.** If the stem says "recommended but
> not required," the answer is a guideline.

### Who approves it

Governance only works if leadership stands behind it. **Senior (executive)
management** holds ultimate responsibility for formally approving and endorsing
the organization's information security policy. Security staff may write the
documents, but management's sign-off gives them authority.

## Laws, regulations, privacy, and PII

Some rules come from *outside* the organization and carry legal force:

- **Laws and regulations** — external, legally binding requirements such as
  **HIPAA** (healthcare data in the U.S.) and **GDPR** (personal data in the
  EU). Unlike an internal policy, breaking these can bring fines or legal
  penalties, so they often set the floor an organization must meet.
- **Personally Identifiable Information (PII)** — information that can identify a
  specific person, such as a full name combined with a Social Security number,
  address, or account number. PII is exactly the kind of data those laws protect.
- **Privacy** — the principle that individuals have the right to control how
  their personal information is collected, used, and shared. Security protects
  data; privacy governs how personal data may be *used* in the first place.

## Exam focus

- The (ISC)² Code of Ethics = **preamble + four canons**, applied **in order of
  precedence**; **canon 1 (protect society) always wins** a conflict.
- Canon order: **protect society → act honorably → serve principals → advance the
  profession.** "Principals" = your employers and clients.
- A serious violation can lead to **sanctions up to revocation** of the
  certification, decided through peer review.
- Governance hierarchy: **policy** (high-level intent) → **standard** (mandatory
  specific rule) → **procedure** (step-by-step) → **guideline** (optional advice).
  A **baseline** is the mandatory minimum configuration.
- **Guidelines are optional; everything else in the hierarchy is mandatory.**
- **Senior management** approves the security policy. **Laws/regulations** (HIPAA,
  GDPR) are external and legally binding. **PII** identifies a person; **privacy**
  is the right to control one's personal information.
