# Security Controls, the CIA Triad & AAA

Before you can defend anything, you need a shared way to talk about *what* you're
protecting and *how* you protect it. This lesson gives you that vocabulary. It's
the foundation the rest of Security+ is built on, so go slowly — almost every
other topic is just a specific example of the ideas here.

## The three things every security program protects

Nearly everything in security traces back to protecting three qualities of
information. We call them the **CIA triad**, and they're worth knowing cold.

> **Confidentiality** keeps secrets secret. **Integrity** keeps data correct and
> unaltered. **Availability** keeps it reachable when you need it.

- **Confidentiality** — only the right people can see the data. Encryption and
  access controls are the usual tools. A leaked customer database is a
  confidentiality failure.
- **Integrity** — the data hasn't been changed, by accident or on purpose.
  Hashing and digital signatures prove this. A tampered bank balance is an
  integrity failure.
- **Availability** — the data and systems are up and usable. Backups, redundancy
  and DDoS defenses protect it. A ransomware outage is an availability failure.

Every control you'll ever deploy is really defending one or more of these three.
When a question asks "which principle does this protect?", map the scenario back
to the triad and the answer usually falls out.

## Two more ideas that ride alongside the triad

Two concepts come up so often they're worth adding right away.

**Non-repudiation** means someone can't credibly deny they did something. A
**digital signature** gives non-repudiation: because only the signer holds the
private key, they can't later claim "that wasn't me." Think of it as a tamper-proof
signature on a contract.

**Authenticity** is the companion idea — proof that a message or user really is
who it claims to be. If integrity says "this wasn't changed," authenticity says
"this genuinely came from the stated source."

## A control is described by two things: its category and its type

A **security control** is any safeguard you put in place to reduce risk. Security+
describes every control two ways at once, and the exam loves to test the
difference. The two questions are:

1. **What kind of thing is it?** → the **category**
2. **What is it trying to do in time?** → the **type**

Keep these on separate axes in your head. A single control has one category *and*
one type.

## Control categories: what kind of safeguard it is

| Category | What it is | Example |
|----------|-----------|---------|
| **Technical** | Enforced by technology | Firewall, encryption, antivirus |
| **Managerial** | Administrative, about how people manage risk | Risk assessments, security policies, onboarding reviews |
| **Operational** | Carried out by people day to day | Security guard rounds, user awareness training, backups |
| **Physical** | Tangible, real-world barriers | Locks, fences, bollards, badge readers |

A quick gut-check: **technical** = a machine does it, **managerial** = a decision
or policy, **operational** = a human process, **physical** = you could touch it.

## Control types: what the safeguard is trying to accomplish

| Type | Purpose | Example |
|------|---------|---------|
| **Preventive** | Stop an incident before it happens | Firewall rule, door lock |
| **Deterrent** | Discourage an attacker from trying | Warning sign, visible camera |
| **Detective** | Notice an incident in progress or after | IDS, log review, motion sensor |
| **Corrective** | Fix things and restore after an incident | Restoring from backup, patching |
| **Compensating** | A stand-in when the ideal control isn't possible | Extra monitoring because a legacy app can't be patched |
| **Directive** | Tell or require people to act a certain way | Acceptable use policy, a "no tailgating" procedure |

The two that trip people up are **deterrent** vs **preventive**, and
**compensating** vs **corrective**. A deterrent only discourages (a sign saying
"Guard dogs on duty"); a preventive actually blocks (the locked gate). A
compensating control substitutes for one you can't use right now; a corrective
control cleans up *after* the damage.

> A camera is a great example of how category and type stack: it is a
> **technical** (or physical, depending on framing) control that is **detective**
> when it records an intrusion and **deterrent** when a would-be intruder sees it
> and walks away.

## Gap analysis: knowing where you fall short

Before picking controls, organizations often run a **gap analysis** — comparing
where their security *is* against where it *should be* (often a standard or a
desired baseline). The "gap" is the distance between the two, and closing it
becomes the to-do list. It's a planning step, not a control itself, but it's how
teams decide which controls they actually need.

## AAA: three questions every system asks about you

When you access almost any secured system, it runs through **AAA** —
**Authentication, Authorization, and Accounting**:

- **Authentication** — *who are you?* You prove your identity (password,
  fingerprint, certificate).
- **Authorization** — *what are you allowed to do?* Once you're known, the system
  decides which resources and actions you're permitted.
- **Accounting** — *what did you actually do?* The system logs your activity for
  later review.

Authentication always comes before authorization — the system has to know who you
are before it can decide what you may do.

## Authenticating people vs. authenticating systems

AAA isn't just for humans. Devices and services authenticate too, and the methods
differ:

- **People** usually authenticate with factors you'll meet in detail later —
  something you know (a password), something you have (a token), something you are
  (a fingerprint).
- **Systems** often authenticate with **digital certificates** rather than
  passwords. A server proves its identity with a certificate signed by a trusted
  authority; one device trusts another because it trusts the certificate. This is
  how a web server proves it really is your bank before your browser trusts it.

## The whole thing in one paragraph

Security exists to protect three qualities of information — confidentiality,
integrity, and availability (the CIA triad) — often reinforced by non-repudiation
and authenticity. You defend those qualities with **controls**, and each control
is described on two axes at once: its **category** (technical, managerial,
operational, or physical) and its **type** (preventive, deterrent, detective,
corrective, compensating, or directive). A **gap analysis** tells you which
controls you're missing. And whenever someone or something uses a secured system,
**AAA** runs: authentication proves who they are, authorization decides what they
can do, and accounting records what they did — with people typically proving
identity through passwords or biometrics and systems proving it through
certificates.

## On the exam

- Expect questions that give a scenario and ask for **both** the category and the
  type of a control. Answer them independently — don't let one bias the other.
- "A sign that warns of a guard dog" is a **deterrent**; "the locked gate itself"
  is **preventive**. Watch the verb: *discourage* = deterrent, *block* =
  preventive, *detect/notice* = detective, *restore/repair* = corrective.
- A **compensating** control is chosen because the preferred control is
  unavailable (often a legacy system that can't be patched). The word "instead" or
  "because we can't" is a strong hint.
- Map any "which is violated?" scenario to one CIA letter: *data leaked* =
  confidentiality, *data altered* = integrity, *system down* = availability.
- **Non-repudiation** is almost always the answer when the stem mentions a
  **digital signature** and the inability to deny an action.
- Remember the AAA order: **authentication** (identity) always precedes
  **authorization** (permissions), and **accounting** is the logging that follows.
