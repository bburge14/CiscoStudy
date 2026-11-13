# Architecture Vulnerabilities & Physical Security

Every architecture carries inherent weaknesses, and every system ultimately sits in
a physical place that must be protected. This lesson pairs the vulnerabilities of
modern computing architectures — from race conditions to cloud multitenancy — with
the physical controls that defend facilities, including the fire-suppression and
power questions the exam loves.

## Vulnerabilities in system architectures

Know these classic weaknesses by name and trigger.

> A **TOCTOU (time-of-check to time-of-use)** race condition occurs when a system
> checks a condition (authorization, a file's identity) and then acts on it, and an
> attacker changes the state in the gap between the two steps.

The tell is "a state change *between* the check and the use." Other named issues:

- **Covert channels** — unintended communication paths that bypass policy. A
  **storage** covert channel writes to a shared resource; a **timing** covert
  channel modulates how long something takes.
- **Buffer overflow** — writing past a buffer's bounds to corrupt memory or run
  code (the root of many exploits; see the secure-coding lesson).
- **Maintenance hooks / backdoors** — developer shortcuts left in production.
- **Aggregation and inference** — in databases, combining individually innocuous
  facts (**aggregation**) or deducing sensitive facts from available ones
  (**inference**) to learn more than you're cleared for; polyinstantiation and
  controlled views mitigate.
- **Emanations (TEMPEST)** — electromagnetic leakage that can be captured at a
  distance; shielding and Faraday cages defend against it.
- **Single point of failure** — any one component whose loss breaks the system;
  design for redundancy.

### Vulnerabilities of specific platforms

| Platform | Signature risk |
|----------|----------------|
| **Cloud** | Shared-responsibility confusion, **multitenancy** isolation failures, misconfiguration |
| **Virtualization** | **VM escape** (breaking out to the hypervisor), hypervisor as a high-value target |
| **Containers** | Weak isolation vs VMs; insecure images, shared kernel |
| **Serverless** | Opaque runtime, dependency and permission sprawl |
| **IoT** | Weak default credentials, no patch path, long lifespans |
| **ICS / SCADA** | Legacy protocols, **availability and safety first**, fragile to active scanning |
| **Embedded / mobile** | Limited resources, physical capture, insecure updates |

> The **cloud shared-responsibility model** is a recurring exam theme: the provider
> secures the infrastructure *of* the cloud; the customer secures what they put
> *in* it (data, access, configuration). The split shifts with IaaS vs PaaS vs
> SaaS, but the customer **always** owns their data and identities.

ICS/SCADA questions reward a risk-manager instinct: because these systems
prioritize availability and safety and often can't tolerate aggressive testing, you
isolate and monitor them rather than patch aggressively mid-shift.

## Physical security: designing the site

Physical security is the layer all the cryptography in the world can't replace — if
an attacker can carry off the server, you've lost. Good design starts before the
walls go up.

**Crime Prevention Through Environmental Design (CPTED)** shapes the environment to
discourage crime through three ideas: **natural surveillance** (open sightlines,
lighting), **natural access control** (guiding movement with landscaping and
entries), and **territorial reinforcement** (clear ownership through signage and
boundaries). Layer physical controls like an onion — **defense in depth**.

Perimeter and entry controls:

- **Bollards** stop vehicles while letting people pass; **fencing**, **gates**, and
  **lighting** form the outer layer; **security guards** add human judgment.
- An **access control vestibule (mantrap)** — a two-door airlock where the second
  door won't open until the first closes — is the go-to defense against
  **tailgating/piggybacking**.
- **Badges, biometric readers, and locks** gate interior access and create a log of
  who went where.

**Data center placement** is tested: put it in the **core** of the building, not
the top floor (roof leaks, lightning) or the basement (flooding). Control access
tightly and monitor it continuously.

## Fire: classes, detection, suppression

A classic exam cluster. First, the fire classes:

| Class | Fuel |
|-------|------|
| **A** | Ordinary combustibles (paper, wood) |
| **B** | Flammable liquids/gases |
| **C** | **Electrical equipment** |
| **D** | Combustible metals |
| **K** | Kitchen oils/fats |

Suppression systems:

- **Wet pipe** — water always in the pipe; simple but risky near electronics.
- **Dry pipe** — pipes hold pressurized air; water enters only when triggered
  (good for cold areas).
- **Preaction** — requires two triggers before water releases; favored in data
  centers to prevent accidental discharge.
- **Deluge** — dumps large volumes fast; for high-hazard areas.

> For a **data center electrical (Class C) fire**, the BEST answer is a
> **clean-agent gaseous system** (e.g., FM-200, inert gases, Novec 1230) that
> suppresses fire **without damaging energized electronics** the way water would.
> **CO₂** works but is dangerous to people (it displaces oxygen), and **Halon** is
> banned for ozone depletion — both are common distractors.

Pair suppression with **smoke and heat detectors** for early warning.

## Power and environment

Electronics need clean, continuous power and a stable climate.

- **UPS (uninterruptible power supply)** — battery bridge for short outages and
  clean shutdown; a **generator** handles longer outages. Together they protect
  availability.
- Guard against **surges, spikes, sags/brownouts, and blackouts**; use surge
  protection and redundant feeds.
- **HVAC** keeps temperature and **humidity** in range — too dry invites static
  discharge, too humid invites condensation and corrosion. Data centers use
  **positive air pressure** so contaminants are pushed out, not drawn in.

## Exam focus

- **TOCTOU** = a state change **between check and use** (a race condition).
  **Aggregation/inference** are the database disclosure risks; **covert channels**
  (storage/timing) bypass policy; **TEMPEST** addresses emanations.
- **Cloud shared responsibility**: provider secures the infrastructure, customer
  secures data/config/identity — and the customer **always owns the data**.
  **VM escape** is the hypervisor risk; **ICS/SCADA** prioritizes availability and
  resists aggressive scanning.
- **CPTED** = natural surveillance, natural access control, territorial
  reinforcement. An **access control vestibule (mantrap)** stops **tailgating**.
  Place the **data center in the building core**.
- Fire classes: **C = electrical.** For data centers use a **clean-agent gas
  (FM-200/inert/Novec)**, not water, **CO₂** (unsafe for people), or banned
  **Halon**. **Preaction** systems prevent accidental water discharge.
- **UPS** bridges short outages (then a **generator**); **HVAC** manages
  temperature and humidity with **positive pressure**.
