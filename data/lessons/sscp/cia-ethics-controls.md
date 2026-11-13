# CIA, the Code of Ethics & Security Controls

Before we touch a firewall rule or a key length, we need the vocabulary the whole
profession is built on. This lesson covers three foundations an SSCP uses every
single day: the **goals** of security (the CIA triad and its friends), the
**ethics** that bind you as a certified practitioner, and the **controls** you
deploy to reach those goals. Get these straight and the rest of the exam becomes
a matter of applying them.

## The CIA triad — the three goals

Every security decision ultimately serves one or more of three goals. The exam
calls them the **CIA triad**, and you should be able to match a scenario to the
right letter instantly.

> **Confidentiality** keeps information from being disclosed to unauthorized
> people. **Integrity** keeps information from being altered without
> authorization. **Availability** keeps information and systems usable when
> authorized people need them.

- **Confidentiality** is defeated by *disclosure* — a leaked database, shoulder
  surfing, a misdirected email. Encryption and access controls defend it.
- **Integrity** is defeated by *alteration* — a tampered record, a corrupted
  file, a man-in-the-middle rewriting traffic. Hashing and digital signatures
  defend it.
- **Availability** is defeated by *destruction* or denial — ransomware, a DDoS
  flood, a failed disk. Redundancy, backups, and capacity planning defend it.

A handy mirror image is the **DAD triad** — **Disclosure, Alteration,
Destruction** — the three bad outcomes that security exists to prevent. If CIA is
what you want, DAD is what the attacker wants.

Two more terms ride alongside the triad:

- **Non-repudiation** — proof that a specific party took an action, so they
  cannot later credibly deny it. A **digital signature** provides it by binding a
  message to the signer's private key.
- **Authenticity** — assurance that data or a message genuinely came from its
  claimed source.

## The (ISC)² Code of Ethics

Earning an (ISC)² certification means agreeing to its **Code of Ethics**. It is
short, binding, and frequently tested. Memorize the four **canons** and, crucially,
their **order of precedence** — when two canons seem to conflict, the earlier one
wins.

1. **Protect society, the common good, necessary public trust and confidence, and
   the infrastructure.**
2. **Act honorably, honestly, justly, responsibly, and legally.**
3. **Provide diligent and competent service to principals.**
4. **Advance and protect the profession.**

The classic exam scenario: you discover your employer is quietly shipping a
product with a flaw that endangers the public. Pleasing your employer is canon 3
(service to principals), but protecting the public is canon 1 — and **canon 1
outranks canon 3**, so your duty is to the public. A memory hook:
**Society -> Honesty -> Principals -> Profession.** "Principals" means the people
you serve: your employers and clients. A serious, peer-reviewed violation can lead
to sanctions up to revocation of the certification.

## Security controls — the tools you deploy

A **control** (or safeguard/countermeasure) is any measure that reduces risk. The
exam slices controls two ways: by **category** (what kind of thing it is) and by
**function/type** (what it does). You must be fluent in both.

> By **category**: a **technical** (logical) control is implemented in hardware or
> software; an **administrative** (managerial) control is a policy, procedure, or
> process; a **physical** control is a tangible barrier in the real world.

- **Technical** — firewalls, encryption, access control lists, antivirus.
- **Administrative** — security policies, background checks, change management,
  awareness training.
- **Physical** — locks, fences, bollards, guards, cameras, mantraps.

The **functional types** describe the control's job relative to an incident:

| Type | What it does | Example |
|------|--------------|---------|
| **Preventive** | Stops an incident before it happens | Firewall, locked door, encryption |
| **Detective** | Discovers an incident in progress or after | Audit logs, IDS, CCTV review |
| **Deterrent** | Discourages an attacker from trying | Warning banner, visible guard |
| **Corrective** | Fixes/limits damage during an incident | Quarantine, patching the flaw |
| **Recovery** | Restores systems to normal afterward | Restoring from backup, failover |
| **Compensating** | A substitute when the primary control isn't feasible | Extra monitoring in place of MFA |
| **Directive** | Instructs or mandates behavior | A policy requiring badge use |

Watch the subtle distinctions the exam loves:

- A **warning banner** at logon is a **deterrent** (it discourages), even though
  it looks like a policy. Reviewing the logs it references is **detective**.
- **Restoring data from backup** after ransomware is **recovery**; isolating the
  infected host during the attack is **corrective**.
- A **compensating** control is specifically a stand-in for a control you can't
  implement — don't confuse it with "corrective."

### Defense in depth

No single control is trusted alone. **Defense in depth** layers controls of
different categories so that if one fails, another still protects the asset — a
locked server room (physical), full-disk encryption (technical), and a
clean-desk policy (administrative) all guarding the same data. Think of a castle:
moat, wall, and guards, not just a single gate.

## Exam focus

- **CIA = Confidentiality, Integrity, Availability.** Match the scenario: leak ->
  confidentiality, tampering -> integrity, outage -> availability. **DAD**
  (Disclosure, Alteration, Destruction) is the inverse.
- **Non-repudiation** = can't deny you did it, delivered by a **digital
  signature**.
- **(ISC)² Code of Ethics = four canons applied in order.** Canon 1, **protect
  society**, always wins a conflict. Order: society, honesty, principals,
  profession.
- Classify controls two ways: **category** (technical/administrative/physical)
  and **function** (preventive, detective, deterrent, corrective, recovery,
  compensating, directive).
- A **warning banner = deterrent**; **log/CCTV review = detective**; **restore
  from backup = recovery**; a **compensating control substitutes** for one you
  can't deploy.
- **Defense in depth** = layered controls, so one failure isn't fatal.
