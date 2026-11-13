# Incident Handling (NIST) & Attack Frameworks

When an incident hits, improvisation is the enemy. Mature security teams follow a
defined **incident-handling life cycle** and reason about the intrusion with
shared **analytic frameworks**. This lesson covers the NIST incident-response
life cycle that organizes the *response*, and the three frameworks — Cyber Kill
Chain, Diamond Model, and VERIS — that organize *understanding* of the attack.

## The NIST SP 800-61 incident response life cycle

The U.S. National Institute of Standards and Technology publishes the most widely
used incident-handling guide, **SP 800-61**. Its classic model has **four
phases**, and the order is tested directly.

> The NIST SP 800-61 incident response life cycle has four phases: **1.
> Preparation; 2. Detection and Analysis; 3. Containment, Eradication, and
> Recovery; 4. Post-Incident Activity.** Note that containment, eradication, and
> recovery are grouped into a single (third) phase.

Walk through what each phase actually involves:

1. **Preparation** — everything you do **before** an incident: building the
   **CSIRT**, acquiring tools, writing playbooks, and training staff. It also
   means identifying stakeholders (see below). This phase is where readiness is
   won or lost.
2. **Detection and Analysis** — **validating** incoming alerts, **confirming** a
   genuine incident has occurred, and **determining which systems are affected**.
   This is the analyst's core triage work.
3. **Containment, Eradication, and Recovery** — the combined action phase:
   - **Containment** — stop the spread (e.g., disconnect an infected endpoint
     from the network so malware can't reach other hosts).
   - **Eradication** — remove the threat: delete malware, **disable breached
     accounts**, and **close the exploited vulnerability** so it can't return.
   - **Recovery** — restore cleaned systems from **known-good backups**, validate
     them, and return them to production while **watching closely** for
     recurrence.
4. **Post-Incident Activity** — the **lessons-learned** review: document what
   happened, what worked, and how to improve detection and response next time.

A subtle but tested point about **Preparation**: stakeholders such as **Legal,
HR, and Public Relations** must be identified in the plan **before** an incident,
so the right parties can be engaged quickly for legal, personnel, and
communication decisions during a real response — not scrambled for mid-crisis.

> *Currency note:* In 2025 NIST released **SP 800-61 Revision 3**, which reframes
> incident response around the **NIST Cybersecurity Framework (CSF) 2.0**
> functions (**Govern, Identify, Protect, Detect, Respond, Recover**) rather than
> four sequential phases. CBROPS is built on the long-standing **four-phase**
> model above, so learn that order — but be aware the newer revision exists.

The life cycle is also a **cycle**: Post-Incident feeds back into Preparation, so
each incident makes the team readier for the next.

## Attack frameworks: three ways to structure an intrusion

Frameworks give analysts a shared language for *describing* an attack. Three
appear on the exam, and each answers a different question.

### The Cyber Kill Chain (Lockheed Martin)

The **Cyber Kill Chain** models an intrusion as **seven sequential stages**. The
idea: break the chain at any stage and you stop the attack.

> The seven Cyber Kill Chain stages are **Reconnaissance → Weaponization →
> Delivery → Exploitation → Installation → Command and Control (C2) → Actions on
> Objectives.**

| Stage | What happens |
|-------|--------------|
| **Reconnaissance** | Research and select targets (harvest emails, find exposed services) |
| **Weaponization** | Couple an exploit with a backdoor into a deliverable payload (e.g., a malicious PDF) — *before* contacting the victim |
| **Delivery** | Transmit the weapon to the target (email the PDF, host a drive-by) |
| **Exploitation** | The victim triggers it; the embedded code runs via a vulnerability |
| **Installation** | Malware installs itself for persistence |
| **Command and Control (C2)** | The malware opens a channel back to the attacker for instructions |
| **Actions on Objectives** | The attacker achieves the goal (steal data, encrypt, destroy) |

Watch the early-stage distinctions: **Weaponization** (building the payload)
happens **before** **Delivery** (sending it), and **Reconnaissance** is pure
research before anything is sent.

### The Diamond Model of Intrusion Analysis

Where the Kill Chain is a timeline, the **Diamond Model** describes a single
intrusion **event** by four interconnected **core features**.

> The Diamond Model's four core features are **Adversary, Capability,
> Infrastructure, and Victim.** The **Capability** is the malware/exploits/tools;
> the **Infrastructure** is the attacker's servers and domains.

The power of the Diamond is pivoting: knowing one vertex helps you discover
another (an adversary's known **infrastructure** leads to other **victims** using
the same **capability**). It complements the Kill Chain — stage *plus* structure.

### VERIS

**VERIS** (Vocabulary for Event Recording and Incident Sharing) — the framework
behind the **Verizon Data Breach Investigations Report (DBIR)** — structures each
incident around the **"4 A's."**

> VERIS's four A's are **Actor, Action, Asset, and Attribute.** They capture *who*
> did it, *what* they did, *what* was affected, and *how it was affected* (which
> security attribute).

VERIS exists to make incident data **consistent and shareable**, so that
aggregated reports like the DBIR can compare incidents across organizations.

## How it fits together

In a real response, the frameworks and the life cycle interlock. During
**Detection and Analysis** you might place the activity on the **Kill Chain** (are
they at Delivery or already at Actions on Objectives?) and populate a **Diamond**
to pivot on the adversary's infrastructure. During **Post-Incident Activity** you
record the event in a structured way (VERIS-style) so the lessons scale beyond
your own team. The life cycle tells you *what to do*; the frameworks tell you
*how to think about the adversary*.

## Exam focus

- NIST SP 800-61 four phases **in order**: **Preparation → Detection and Analysis
  → Containment, Eradication, and Recovery → Post-Incident Activity.** Containment,
  eradication, and recovery are **one** combined phase.
- Match actions to phases: build CSIRT/train = **Preparation**; validate/confirm
  = **Detection and Analysis**; isolate host = **Containment**; remove
  malware/close vuln = **Eradication**; restore from backup = **Recovery**;
  lessons learned = **Post-Incident**. Identify **Legal/HR/PR before** an incident.
- **Cyber Kill Chain** = 7 stages (Recon, Weaponization, Delivery, Exploitation,
  Installation, C2, Actions on Objectives). Weaponization precedes Delivery.
- **Diamond Model** = **Adversary, Capability, Infrastructure, Victim** (Capability
  = tools; Infrastructure = attacker servers/domains).
- **VERIS 4 A's** = **Actor, Action, Asset, Attribute** (behind the Verizon DBIR).
