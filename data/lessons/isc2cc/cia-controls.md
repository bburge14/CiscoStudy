# The CIA Triad & Security Controls

Everything in cybersecurity is in service of a few simple goals, and everything
we *do* to protect information is some kind of control. This lesson covers both:
the **CIA triad** that defines what "secure" even means, and the **security
controls** we deploy to achieve it. Get these two ideas straight and most of the
rest of the certification becomes easier to reason about.

## The CIA triad: the three goals of security

> The **CIA triad** states the three core goals of information security:
> **Confidentiality**, **Integrity**, and **Availability**. Protecting
> information means protecting all three.

Think of it as a three-legged stool. Knock out any leg and the information is no
longer properly protected.

### Confidentiality

**Confidentiality** means only authorized people can view or access information.
It is about *keeping secrets secret*. When a hospital makes sure only a patient's
own doctors can read their medical record, that is confidentiality at work.

- Protected by: encryption, access controls, strong authentication.
- Broken by: a data leak, a stolen laptop, or shoulder-surfing a password.

### Integrity

**Integrity** means information stays accurate and complete, and is not changed
except by authorized people in authorized ways. If an attacker alters the dollar
amounts in an accounting database, integrity has been violated — the numbers are
no longer trustworthy even though they are still readable.

- Protected by: hashing, digital signatures, change control, input validation.
- Broken by: unauthorized edits, corruption, or a faulty process.

### Availability

**Availability** means the information and systems are usable when authorized
people need them. A perfectly confidential, perfectly accurate database is
useless if it is offline during business hours.

- Protected by: redundancy, backups, patching, and capacity planning.
- Broken by: a denial-of-service attack, hardware failure, or ransomware.

A quick analogy: your bank account must be seen only by you (confidentiality),
show the correct balance (integrity), and be reachable at the ATM when you need
cash (availability).

### A note on the "extra" terms

Two related ideas often appear alongside the triad:

- **Non-repudiation** — a user cannot credibly deny having performed an action
  (supported by logging and digital signatures).
- **Authenticity** — information or a message genuinely comes from the claimed
  source.

They aren't part of the three-letter triad, but they round out the picture.

## Security controls: how we actually protect CIA

> A **security control** is any safeguard or countermeasure put in place to
> reduce risk and protect confidentiality, integrity, and availability.

Controls are described in two different ways, and the exam expects you to keep
them separate: their **category** (what *kind* of thing the control is) and their
**type** (what *function* it performs).

### Control categories — what kind of control it is

| Category | Also called | Examples |
|----------|-------------|----------|
| **Administrative** | Managerial | Policies, procedures, security-awareness training, acceptable-use policy, hiring background checks |
| **Technical** | Logical | Firewalls, encryption, antivirus, passwords, full-disk encryption, access control lists |
| **Physical** | — | Security guards, fences, bollards, locks, cameras, badge readers |

The clue is the *nature* of the safeguard. A written rule is **administrative**.
Something enforced by hardware or software is **technical**. Something you could
physically touch or walk into is **physical**.

### Control types — what function the control performs

| Type | What it does | Example |
|------|--------------|---------|
| **Preventive** | Stops an incident before it happens | A firewall blocking malicious traffic |
| **Deterrent** | Discourages an attacker from trying | A "24-hour video surveillance" warning sign |
| **Detective** | Identifies and alerts on an incident | An intrusion detection system; CCTV that records |
| **Corrective** | Fixes or mitigates during/after an incident | Antivirus quarantining and removing malware |
| **Recovery** | Restores systems and data to normal | Restoring servers from clean backups |
| **Compensating** | An alternative safeguard when the primary one isn't feasible | Isolating a legacy system that can't support MFA onto a tightly monitored network |

The same technology can be more than one type depending on how it is used, and a
single incident often moves through several types: a **deterrent** sign tries to
scare the attacker off, a **preventive** firewall tries to block them, a
**detective** IDS catches what gets through, a **corrective** tool cleans the
infection, and a **recovery** restore brings service back.

### Categories and types are independent

Every control has *both* a category and a type. A security guard is **physical**
(category) and can be **deterrent**, **detective**, or **preventive** (type)
depending on their role. Encryption is **technical** (category) and
**preventive** (type). Don't mix the two axes up — that confusion is a classic
exam trap.

## Putting it together

The CIA triad tells you *what* you are protecting; security controls are *how*.
When you read a scenario, ask first which leg of the triad is at stake, then
classify the safeguard by both its category (administrative / technical /
physical) and its function (preventive, deterrent, detective, corrective,
recovery, compensating). That two-question habit answers a surprising share of
exam items.

## Exam focus

- **Confidentiality** = secrecy; **Integrity** = accuracy / no unauthorized
  change; **Availability** = usable when needed. Map each scenario to one leg.
- Altering data without permission attacks **integrity**; a denial-of-service
  attacks **availability**; a leak or theft attacks **confidentiality**.
- **Category** = the nature of the control: administrative (managerial),
  technical (logical), or physical. A policy or training is administrative;
  encryption/firewall/antivirus is technical; guards/fences/locks are physical.
- **Type** = the function: preventive, deterrent, detective, corrective,
  recovery, compensating. Know the one-line definition of each.
- A **compensating** control is the alternative you add when the ideal control
  can't be used (e.g., a legacy box that can't run MFA gets extra isolation).
- Every control has *both* a category and a type — keep the two axes separate.
