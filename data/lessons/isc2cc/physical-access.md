# Physical Access Controls

It's easy to obsess over firewalls and forget that an attacker who can simply walk
up to a server, unplug it, and carry it away has beaten all of it. **Physical
access controls** protect the tangible world — buildings, rooms, equipment, and
people. This lesson covers the common physical safeguards and, just as important,
the distinctions the exam likes to test between them.

## Why physical security comes first

All the encryption in the world won't help if someone steals the drive and has
unlimited time to attack it, or watches an administrator type a password over
their shoulder. Physical controls are the outer layer of defense in depth, and
many of them double as **deterrent**, **detective**, or **preventive** controls
depending on how they're used.

## Perimeter and barrier controls

The first job is to keep unauthorized people away from the building and grounds.

- **Fencing** — a visible perimeter barrier whose main purpose is to **deter and
  delay** unauthorized people from entering the grounds. A fence rarely stops a
  determined intruder outright, but it slows them and signals that entry is not
  welcome.
- **Bollards** — short, sturdy posts that block vehicles from ramming a building
  while still letting people walk past.
- **Lighting** — bright exterior lighting at night deters intruders and helps
  security cameras capture clear, usable images. (If you see a one-word answer
  about night-time deterrence that also helps cameras, it's *lighting*.)

## Controlling who comes through the door

Once at the entrance, you need to admit the right people and keep the wrong ones
out.

- **Access badge** — an ID card the employee carries ("something you have") that
  is read by a **card reader** at the door. The badge system both gates entry and
  logs who went where.
- **Biometric reader** — a device that grants entry by scanning a physical trait
  ("something you are"), such as a fingerprint or face, to authenticate the
  person.
- **Turnstile** — a barrier that admits exactly one person per valid badge scan,
  making it hard for a second person to slip through behind the first.

### Locks and keys

Locks are the oldest access control there is, and they come in several flavors you
should recognize:

- **Conventional (key) locks** — simple and cheap, but keys can be copied or lost,
  and there's no record of who used them.
- **Combination / cipher locks** — a keypad requiring a code; easy to re-key by
  changing the code, but vulnerable to shoulder surfing and shared codes.
- **Electronic / smart locks** — controlled by badge, PIN, or biometric and tied
  into the access system, so they can log every entry and be disabled instantly
  when someone leaves. These pair naturally with badge readers and vestibules.

A general principle: the more a lock can **log and be centrally managed**, the
better it supports accountability and quick deprovisioning.

### Access control vestibules and the tailgating problem

A specific, exam-favorite pairing:

> **Tailgating** (also called **piggybacking**) is when an unauthorized person
> closely follows an authorized employee through a controlled door before it
> closes, without ever presenting their own credential.

The go-to defense:

> An **access control vestibule** (historically called a **mantrap**) is a small
> booth with two interlocking doors; the second door won't open until the first
> has closed, admitting one person at a time. It defeats tailgating by design.

Whenever a scenario describes someone slipping in behind an authorized person,
the problem is **tailgating** and the classic answer is an **access control
vestibule** (or a turnstile, which has the same one-person-at-a-time effect).

## Monitoring and response

Barriers and doors keep people out; you also need to *watch* and *respond*.

- **Video surveillance (CCTV)** — cameras that record everyone entering an area.
  Note the type: because CCTV records but does **not physically stop** anyone, it
  is primarily a **detective** control (and a deterrent when visible). It helps
  you investigate *after* the fact.
- **Security guards** — the one control that brings human judgment. A guard can
  verify identities, notice something unusual, exercise judgment about an odd
  situation, and **actively respond** to an intruder. When a question asks for a
  control that can *adapt and respond*, the answer is usually a security guard.

## Protecting the equipment itself

Even inside a secured building, individual devices need protection:

- **Cable lock** — a lock that anchors a laptop to a desk, reducing the chance it
  is physically grabbed from an open desk in a shared or public workspace.
- **Locking racks and server cages** keep data-center hardware from being touched
  by unauthorized staff.
- **Device-level protections** like full-disk encryption (covered elsewhere) mean
  that even if hardware *is* stolen, the data on it stays confidential.

## Thinking in layers

Notice how these controls stack: a **fence** and **lighting** deter at the
perimeter, a **badge reader** and **vestibule** control the door, a **turnstile**
enforces one-at-a-time entry, **CCTV** records what happens, a **guard** responds
to anything unusual, and a **cable lock** protects the laptop at the desk. No
single control is enough; together they form defense in depth for the physical
world.

## Exam focus

- **Tailgating / piggybacking** = following an authorized person through a door
  without a credential. The signature defense is an **access control vestibule
  (mantrap)**; a **turnstile** also enforces one person per scan.
- **Fencing** primarily **deters and delays**; **lighting** deters at night and
  aids cameras; **bollards** stop vehicles.
- **CCTV** is primarily a **detective** control — it records but doesn't stop
  anyone.
- A **security guard** is the control that can verify identity, use judgment, and
  **actively respond**.
- **Badges** = "something you have" read by a card reader; **biometrics** =
  "something you are."
- A **cable lock** anchors a laptop to a desk to deter physical theft.
