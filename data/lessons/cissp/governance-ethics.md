# Security Governance, the CIA Triad & Professional Ethics

CISSP is not an exam about configuring firewalls. It is an exam about *thinking
like a risk manager who happens to understand technology*. Before any control is
chosen, a well-run program establishes why security exists, who is accountable
for it, and what rules bind the professionals who run it. This lesson covers that
foundation: the goals security protects, the controls that protect them, the
governance that directs the whole effort, and the ethics and personnel practices
that keep trusted people honest.

## The CIA triad — and its evil twin

Every safeguard in the CBK serves one of three goals.

> **Confidentiality** keeps information from unauthorized disclosure.
> **Integrity** keeps it accurate and unaltered. **Availability** keeps it
> accessible to authorized users when they need it.

The mirror image is the **DAD triad** — *Disclosure, Alteration, Destruction* —
the three ways an attacker defeats CIA. Two more properties round out the set and
appear constantly in exam stems:

- **Authenticity** — the data genuinely comes from its claimed source.
- **Non-repudiation** — the originator cannot credibly deny the action later
  (delivered by digital signatures, covered in the cryptography lesson).

A classic exam move is to hand you a scenario and ask which element is *primarily*
at stake. Ransomware encrypting files that you can no longer read is an
**availability** problem first; a leaked customer list is **confidentiality**; a
tampered bank balance is **integrity**. Read for the harm, not the attack name.

## Control types and functions

CISSP classifies every control two ways at once, and the exam loves to test the
distinction.

**By type (how it is implemented):**

- **Administrative / managerial** — policies, procedures, training, risk
  assessments. People and process.
- **Technical / logical** — firewalls, encryption, access control lists, MFA.
- **Physical** — fences, locks, guards, bollards, cameras.

**By function (what it does in the timeline of an event):**

| Function | Role | Example |
|----------|------|---------|
| **Preventive** | Stop an incident before it happens | Locked door, MFA |
| **Detective** | Discover an incident in progress or after | IDS, log review, CCTV |
| **Corrective** | Fix damage and restore after an event | Restoring from backup |
| **Deterrent** | Discourage the attacker from trying | Warning banner, visible guard |
| **Recovery** | Return to normal operations | DR site, rebuild procedures |
| **Directive** | Instruct or mandate behavior | Policy requiring badge use |
| **Compensating** | An alternative when the primary control isn't feasible | Jump host + extra logging when a legacy app can't do MFA |

> A **compensating control** is the answer whenever a required safeguard cannot be
> implemented and the organization substitutes something that provides *comparable*
> protection. It is about feasibility, not laziness — and it should still be
> documented and risk-accepted.

## Governance: who is actually accountable

**Security governance** is how senior leadership directs and oversees the program
so that security supports business objectives rather than fighting them. The
single most tested governance fact is about accountability:

> **Senior (executive) management — and ultimately the board of directors — holds
> final accountability for security and for formally accepting residual risk. This
> cannot be delegated.** Execution is delegated to a CISO and staff;
> *accountability* stays at the top. This is "tone at the top."

Two legal standards flow from that responsibility:

- **Due care** — doing what a reasonable, prudent organization would do to protect
  assets (taking responsible action). Think "doing the right thing."
- **Due diligence** — the ongoing homework behind due care: investigating,
  monitoring, and maintaining that effort over time. Think "continuously verifying
  you are still doing the right thing."

When an exam question asks what demonstrates due care vs due diligence, remember:
diligence is the research and continuous practice; care is the action taken.

## The (ISC)² Code of Ethics

Every CISSP agrees to be bound by the (ISC)² Code of Ethics. You must know its
shape and the *order* of its canons, because that order is how conflicts are
resolved.

> The Code has a **preamble** plus **four canons**, listed in deliberate order of
> precedence. When two canons appear to conflict, the earlier one wins.

1. **Protect society, the common good, necessary public trust and confidence, and
   the infrastructure.**
2. **Act honorably, honestly, justly, responsibly, and legally.**
3. **Provide diligent and competent service to principals** (your employers and
   clients).
4. **Advance and protect the profession.**

The highest-yield scenario: a client asks you to stay silent about a flaw that
endangers the public. Canon I (protect society) outranks Canon III (serve
principals), so you side with public safety. Memory hook: **Society → Honor →
Principals → Profession.** A serious, peer-reviewed violation can lead to
sanctions up to revocation of the certification.

## Personnel security: controlling trusted insiders

People are hired into positions of trust, so the program must limit how much
damage any one person can do — accidentally or deliberately.

- **Separation of duties (SoD)** — split a sensitive task so no single person can
  complete it alone (the person who requests a payment can't also approve it).
  This prevents fraud by requiring collusion.
- **Least privilege** — grant only the access a role genuinely needs, nothing more.
- **Need to know** — a tighter cousin: even with clearance, you only see the
  specific data your task requires.
- **Job rotation** — move people through roles periodically. It deters and exposes
  fraud (a hidden scheme surfaces when someone else sits in the chair) *and*
  cross-trains staff so the organization isn't dependent on one person.
- **Mandatory vacation** — force time away so irregularities surface while the
  employee is absent.
- **Dual control (two-person rule)** — two people must act together to perform a
  single critical operation (two keys to launch).

Surrounding these are the lifecycle practices: **background checks** before hire,
**non-disclosure agreements (NDAs)** to bind confidentiality, structured
**onboarding**, and disciplined **offboarding** that revokes access the moment
employment ends. Separation of duties, job rotation, and mandatory vacation are a
classic complementary trio — expect a question asking which *combination* best
detects and deters insider fraud.

## Exam focus

- **CIA**: confidentiality = no disclosure, integrity = no unauthorized change,
  availability = accessible when needed. The attacker's version is **DAD**. Add
  **authenticity** and **non-repudiation** to the vocabulary.
- Classify controls **both** ways: type (**administrative / technical /
  physical**) and function (**preventive, detective, corrective, deterrent,
  recovery, directive, compensating**). A **compensating control** is the
  alternative used when the required control isn't feasible.
- **Senior management / the board is ultimately accountable** and must formally
  accept residual risk; this responsibility cannot be delegated, only executed by
  the CISO. Know **due care** (prudent action) vs **due diligence** (ongoing
  investigation and maintenance).
- The (ISC)² Code of Ethics = **preamble + four canons in order of precedence**;
  **Canon I (protect society) always wins** a conflict. Violations can cost you the
  cert.
- **Separation of duties** forces collusion; **least privilege** and **need to
  know** minimize access; **job rotation** and **mandatory vacation** surface
  hidden fraud; **dual control** needs two people for one action. These are
  administrative controls, and the "best detect-and-deter insider fraud" answer is
  usually a *combination* of them.
