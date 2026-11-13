# The Incident Response Lifecycle & Attack Frameworks

When prevention fails, a disciplined process is what keeps a bad day from
becoming a catastrophe. This lesson covers the incident response (IR) lifecycle —
the phases every responder works through — the preparation that makes those
phases possible, and the attack frameworks analysts use to structure what the
adversary is doing. Later lessons drill into detection and into containment; here
we build the map.

## The NIST SP 800-61 lifecycle

> **NIST SP 800-61** defines a four-phase incident response lifecycle:
> **1) Preparation**, **2) Detection & Analysis**, **3) Containment, Eradication
> & Recovery**, and **4) Post-Incident Activity**.

The order is testable. The phase immediately **after Detection & Analysis** is
**Containment, Eradication & Recovery** — you've confirmed the incident, now you
stop the bleeding, remove the threat, and restore service. The lifecycle is a
*loop*: lessons from phase 4 feed back into phase 1.

Many SOCs use the **SANS** six-step handling process, which maps cleanly onto
NIST:

| SANS (PICERL) | NIST equivalent |
|---------------|-----------------|
| **P**reparation | Preparation |
| **I**dentification | Detection & Analysis |
| **C**ontainment / **E**radication / **R**ecovery | Containment, Eradication & Recovery |
| **L**essons Learned | Post-Incident Activity |

So when a scenario asks which SANS step corresponds to *first recognizing* an
incident, the answer is **Identification**.

## Preparation: the work you do before anything breaks

Preparation is the phase that decides how the others go.

- **Incident response plan** — the overarching, approved document that defines
  roles, authority, and severity thresholds.
- **Playbooks (runbooks)** — repeatable, step-by-step procedures for *specific*
  attack types, such as ransomware. When a SOC lead wants responders to follow
  consistent steps for a known scenario, a playbook is the artifact.
- **RACI matrix** — assigns duties as Responsible, **Accountable**, Consulted,
  Informed. The person marked **Accountable** is *ultimately answerable for the
  outcome and approves its completion* — there is exactly one per task.
- **Communication plan with an out-of-band channel.** If attackers have
  compromised corporate email, responders must coordinate on a *separate*,
  trusted channel (an encrypted phone bridge, say) so the adversary can't read
  the response — and because primary systems may be unavailable.
- **Training and exercises.** A **tabletop exercise** gathers stakeholders to
  *talk through* a simulated scenario (e.g., ransomware) and validate the plan
  **without disrupting production** — the low-risk way to find gaps before a real
  incident does.

Preparation also overlaps with continuity planning. When a ransomware outage
threatens to halt order processing, the **business continuity plan (BCP)** is the
plan that specifically addresses **keeping critical business functions operating
during the disruption**.

## Attack frameworks: structuring the adversary's story

Responders lean on three frameworks to describe *what* an attacker is doing and
*where* in the campaign they are.

### The Lockheed Martin Cyber Kill Chain

> The **Cyber Kill Chain** breaks an intrusion into seven sequential phases:
> **Reconnaissance → Weaponization → Delivery → Exploitation → Installation →
> Command & Control (C2) → Actions on Objectives.**

The earlier you disrupt the chain, the cheaper the defense — and the earliest
phase here is **Reconnaissance**. A couple of phases the exam probes:

- Emailing a weaponized PDF to employees — *transmitting* the payload to the
  target — is **Delivery**.
- Malware that repeatedly beacons to an external server to receive attacker
  instructions is in **Command & Control (C2)**.

### The Diamond Model of Intrusion Analysis

> The **Diamond Model** describes every intrusion event with four core features:
> **Adversary, Capability, Infrastructure, and Victim.**

Its power is **pivoting**: start from one known feature and discover the others.
Given a malicious C2 IP (Infrastructure), query passive DNS and registration data
to uncover the **Adversary** behind it — moving across the diamond from one vertex
to another.

### MITRE ATT&CK

**MITRE ATT&CK** catalogs real-world adversary behavior as **tactics** (the goal
— the *why*) and **techniques** (the method — the *how*). It's the go-to reference
for mapping observed activity to a standardized taxonomy. Remember the
tactic-vs-technique split: **Lateral Movement** and **Persistence** are *tactics*;
the specific tricks used to achieve them are techniques.

## Post-Incident Activity: closing the loop

After recovery, the team holds a **lessons-learned** meeting and updates its
playbooks based on what went wrong. Its purpose is forward-looking: **improve
future response and prevent recurrence**, not assign blame. A key output is
**root-cause analysis** — identifying the underlying reason (for instance, an
unpatched VPN appliance that was the initial entry point) so the same door can't
be used twice.

## A note on currency: NIST SP 800-61 Rev 3

In **April 2025**, NIST published **SP 800-61 Revision 3**, which reframes
incident response around the six **NIST Cybersecurity Framework (CSF) 2.0**
Functions — **Govern, Identify, Protect, Detect, Respond, Recover** — rather than
the classic four-phase lifecycle. CS0-003 was built on the **Rev 2** four-phase
model above, so answer exam questions with those four phases; recognize the Rev 3
/ CSF 2.0 framing as the current real-world direction.

## Exam focus

- **NIST SP 800-61** four phases: **Preparation → Detection & Analysis →
  Containment, Eradication & Recovery → Post-Incident Activity.** The phase after
  Detection & Analysis is **Containment, Eradication & Recovery**.
- **SANS PICERL** maps to NIST; **Identification** = Detection & Analysis.
- Preparation artifacts: **IR plan**, **playbook/runbook** (per-scenario steps),
  **RACI** (**Accountable** = ultimately answerable/approves), **out-of-band
  comms** (so the attacker can't read the response), **tabletop exercise**
  (talk-through, no production impact). **BCP** keeps critical functions running.
- **Cyber Kill Chain** (7 phases): earliest is **Reconnaissance**; sending the
  weaponized payload is **Delivery**; beaconing for instructions is **C2**.
- **Diamond Model** = Adversary, Capability, Infrastructure, Victim; moving
  between them is **pivoting**.
- **MITRE ATT&CK**: tactic = goal/why, technique = how; Lateral Movement and
  Persistence are **tactics**.
- **Lessons learned / root-cause analysis** exist to **prevent recurrence**.
- Currency: **Rev 3 (2025)** reorganizes IR around **CSF 2.0** functions; the exam
  uses the Rev 2 four phases.
