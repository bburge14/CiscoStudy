# Zero Trust, Physical Security & Change Management

Three very different ideas share this lesson, but they all answer the same
question in their own way: *how do you keep trust from being abused?* Zero Trust
rebuilds how networks decide who to trust, physical security protects the trust
boundary you can touch, and change management keeps well-meaning changes from
quietly breaking your defenses.

## Zero Trust: stop trusting the network

The old way of building networks assumed a hard outer wall and a soft, trusting
inside: once you were "on the network," you were mostly trusted. Attackers loved
that, because one foothold inside meant free movement everywhere.

> **Zero Trust flips the assumption: never trust, always verify. Every request is
> checked on its own merits, no matter where it comes from — inside or outside.**

Security+ describes Zero Trust as two cooperating planes. Picture a nightclub with
a strict door policy.

### The control plane — the brains that decide

The **control plane** is where access *decisions* are made. Its key pieces:

- **Policy Engine (PE)** — the component that actually evaluates each request
  against the rules and decides allow or deny.
- **Policy Administrator (PA)** — carries out the engine's decision by
  establishing or cutting the connection.
- Together these form the **Policy Decision Point (PDP)** — the decision-maker.
- **Adaptive identity** — identity isn't a one-time yes/no; it adjusts based on
  context (device health, location, behavior). A login from a new country gets
  more scrutiny.
- **Threat scope reduction** — shrink what any one identity can reach, so a
  compromise does less damage.
- **Policy-driven access control** — decisions come from written policy, applied
  consistently, not from where you happen to sit.

### The data plane — where traffic actually flows

The **data plane** is where the approved connection lives:

- **Policy Enforcement Point (PEP)** — the gatekeeper that lets the traffic
  through (or not) based on what the control plane decided. Think of it as the
  bouncer who checks with the manager, then opens the rope.
- **Subject/System** — the user or device making the request.
- **Implicit trust zones** — the limited area a request is allowed into *after*
  it's approved.

The clean way to remember it: the **control plane decides** (PDP = Policy Engine +
Policy Administrator), and the **data plane enforces** (PEP). Decision and
enforcement are deliberately separated.

## Physical security: protecting what you can touch

All the encryption in the world won't help if someone can walk up and carry off
your server. Physical controls protect people, equipment, and facilities.

Common deterrents and barriers:

- **Bollards** — short, sturdy posts that stop vehicles from ramming a building
  while still letting people walk through.
- **Fencing** — a visible perimeter; taller and with anti-climb features for more
  sensitive sites.
- **Lighting** — well-lit areas deter intruders and make cameras useful at night.
- **Access badges** — cards that gate entry and create a log of who went where.
- **Access control vestibule** (sometimes called a mantrap) — a small two-door
  airlock where the second door won't open until the first closes, defeating
  **tailgating** (an unauthorized person slipping in behind an authorized one).
- **Video surveillance** — cameras that deter and record.
- **Security guards** — human judgment that can respond to the unexpected.

Detection comes from **sensors**, and you should know the flavors:

| Sensor | How it detects |
|--------|----------------|
| **Infrared** | Senses body heat / changes in heat |
| **Pressure** | Triggers on weight, e.g. a floor mat |
| **Microwave** | Bounces microwaves to sense movement |
| **Ultrasonic** | Uses sound waves to detect motion |

### Deception and disruption technology

A clever branch of defense *invites* attackers into fake targets so you can watch
them and waste their time:

- **Honeypot** — a single decoy system that looks juicy but has no real value;
  any interaction with it is suspicious by definition.
- **Honeynet** — a whole fake network of honeypots.
- **Honeyfile** — a bait file (e.g. `passwords.xlsx`) that alerts you if opened.
- **Honeytoken** — a piece of fake data (a fake credential or record) planted so
  that if it ever shows up in use, you know it was stolen.

> Anything touching a honeypot is, by design, up to no good — there's no
> legitimate reason to be there. That makes decoys a very low-noise detective
> tool.

## Change management: don't let good intentions break security

Most outages and many security holes come not from attackers but from *changes* —
a well-meaning update that opens a port, breaks a dependency, or disables logging.
**Change management** is the disciplined process that keeps changes safe and
reversible.

The business process pieces you should recognize:

- **Approval process** — changes get reviewed and signed off, not made on a whim.
- **Ownership** — someone is clearly responsible for the change.
- **Stakeholders** — everyone affected is identified and consulted.
- **Impact analysis** — what could this break, and what's the security effect?
- **Test results** — prove it works in a test environment first.
- **Backout plan** — a documented way to undo the change if it goes wrong.
- **Maintenance window** — a scheduled, low-impact time to make the change.
- **Standard Operating Procedure (SOP)** — the repeatable, documented steps.

There are **technical implications** to weigh too: updating **allow lists / deny
lists**, **restricted activities**, planned **downtime**, needing a **service
restart** or **application restart**, dealing with fragile **legacy
applications**, and untangling **dependencies** (change A may require change B
first).

Finally, every change should leave a paper trail: **updating diagrams** and
**updating policies/procedures** so documentation stays truthful, and **version
control** so you can see exactly what changed, when, and by whom — and roll back
if needed.

## The whole thing in one paragraph

Zero Trust replaces "trust the inside of the network" with "verify every request,"
splitting the job into a **control plane** that decides (the Policy Decision Point
= Policy Engine + Policy Administrator, using adaptive identity and policy-driven
rules) and a **data plane** that enforces (the Policy Enforcement Point). Physical
security protects the tangible boundary with bollards, fencing, lighting, badges,
access control vestibules, cameras and guards, detects intrusions with infrared,
pressure, microwave and ultrasonic sensors, and can even bait attackers with
honeypots, honeynets, honeyfiles and honeytokens. And change management keeps
changes from becoming incidents through approvals, ownership, impact analysis,
test results, a backout plan, a maintenance window and SOPs — plus careful
handling of allow/deny lists, restarts, legacy apps and dependencies, all tracked
with updated documentation and version control.

## On the exam

- Memorize the Zero Trust mapping: **PDP = decision** (Policy Engine + Policy
  Administrator), **PEP = enforcement**. If the stem says "makes the decision,"
  it's the control plane; "allows the traffic through," it's the data plane.
- An **access control vestibule** (mantrap) is the go-to answer for stopping
  **tailgating/piggybacking**.
- Know the sensor types by their medium: **infrared = heat**, **pressure =
  weight**, **microwave** and **ultrasonic = motion** via waves.
- Anything describing a **decoy** that has no legitimate use points to a
  honeypot/honeynet/honeyfile/honeytoken — and a honeytoken is specifically *fake
  data* used to detect theft.
- For change management, the **backout plan** is the answer whenever the concern
  is "how do we undo this if it fails," and a **maintenance window** is "when do we
  do it with least impact."
- A common distractor: change management is a **managerial/operational** control,
  not a technical one — it governs *how* changes happen.
