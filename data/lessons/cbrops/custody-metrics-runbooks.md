# Chain of Custody, SOC Metrics & Runbooks

The final lesson covers how a response is kept **defensible**, how a SOC is
**measured**, and how it stays **consistent and fast**. Chain of custody protects
evidence so it holds up legally; metrics tell management (and the team) whether
the SOC is improving; and runbooks with automation make response repeatable
instead of heroic. Together they are the operational discipline behind everything
you have learned.

## Chain of custody and evidence handling

Evidence is only useful if a court — or an internal disciplinary board — will
accept it. That acceptance depends on being able to account for the evidence at
every moment.

> The **chain of custody** is the chronological documentation that records every
> person who collected, handled, or transferred a piece of evidence, preserving
> its **integrity** and **legal admissibility**.

Each time evidence changes hands, the record must capture **who** had it,
**when**, **what** was done with it, and **each transfer — with signatures**. A
gap in that chain — a period no one can account for — can render the evidence
inadmissible, because no one can prove it wasn't altered.

### Preserving integrity

Two techniques keep the evidence itself trustworthy:

- **Cryptographic hashing** — compute a hash at **acquisition** and again at
  **analysis**, then compare. Matching hashes prove **data integrity** (the image
  wasn't altered); differing hashes mean it was tampered with and its
  admissibility is in doubt. (Same principle as the forensic-image check in Unit
  3, now in a legal frame.)
- **Hardware write blocker** — when imaging a suspect drive, connect it through a
  write blocker so the acquisition process **cannot modify the source**,
  preserving the original exactly.

### Order of volatility

Live systems lose evidence fast, so **NIST SP 800-86** defines an **order of
volatility**: collect the most fleeting data first.

> Capture the **most volatile** data first — the contents of **RAM** and active
> network connections — because it vanishes when the system is powered off.
> Collect the **least volatile** data — **archival/backup media** — last.

So a responder who arrives at a running, compromised workstation with active
malware in memory should **capture a RAM (memory) image and other volatile data
first**, before powering it down or imaging the disk. Pull the plug first and you
lose the memory-resident malware and live connections forever. Roughly, the order
runs: CPU registers/cache → RAM and network state → disk → logs → archival media.

## CSIRT and SOC metrics

The team that runs incident response is the **CSIRT**.

> A **Computer Security Incident Response Team (CSIRT)** exists to **receive,
> triage, and respond to** reported security incidents — the organized human
> capability behind the life cycle from the previous lesson.

A SOC is judged by **time-based metrics**, because in incident response, time is
damage. Learn these precisely:

| Metric | What it measures |
|--------|------------------|
| **Mean Time to Detect (MTTD)** | Average time from when an intrusion **begins** to when the SOC **first detects** it |
| **Mean Time to Respond (MTTR)** | Time from **detection** to the start of **effective response** |
| **Time to Contain** | Time from detection to **stopping the spread** to more systems |
| **Dwell time** | Total time an attacker stays **undetected**, from initial compromise until detection |

The reason these matter is cause and effect: **lowering MTTD and time to contain
shrinks attacker dwell time**, and less dwell time means **fewer systems
compromised and less data lost** before the threat is stopped. A SOC that detects
in minutes and contains in an hour prevents far more damage than one that takes
weeks — which is exactly why these numbers are tracked and driven down.

## Runbooks, playbooks, and automation

Consistency under pressure comes from writing the response down in advance.

> A **playbook** (also called a **runbook**) is a documented, repeatable set of
> steps for responding to a **specific type** of incident.

Playbooks turn tribal knowledge into a procedure anyone on the team can follow
the same way at 3 a.m. They also define **escalation** — for example, a Tier-1
analyst escalates to Tier-2 when set criteria are met — so incidents reach the
right expertise **without delay or omission**.

### Run book automation (RBA) and SOAR

**Run book automation (RBA)**, delivered by **SOAR** platforms, executes playbook
steps automatically.

- **Benefit** — it **automates repetitive response tasks**, cutting response time
  and human error, and letting analysts focus on confirmed threats rather than
  routine toil.
- **Best candidates for automation** — **high-volume, well-defined, repetitive
  tasks with clear decision logic**, such as enriching an alert with reputation
  data. (Judgment-heavy, ambiguous decisions are poor automation candidates —
  keep a human in the loop there.)
- **Example** — a phishing-report playbook that automatically extracts URLs and
  attachments, detonates them in a sandbox, enriches indicators with threat
  intelligence, and opens a ticket. It handles routine triage **consistently and
  quickly**, so analysts spend their time on the alerts that are actually real.

## The operational picture

Step back and the unit comes together. The **CSIRT** runs the **NIST life cycle**;
**playbooks and automation** make each phase repeatable and fast; **metrics** like
MTTD and dwell time prove whether it's working and push the team to improve; and
**chain of custody** ensures the evidence gathered along the way survives legal
scrutiny. That is a security operations program — not just tools and alerts, but
the discipline that turns them into reliable defense.

## Exam focus

- **Chain of custody** = chronological record of **who** handled evidence,
  **when**, **what** was done, and **each transfer (signed)** — it preserves
  **integrity and admissibility**; gaps can make evidence inadmissible.
- Preserve integrity with **hashing** at acquisition vs. analysis (match =
  intact) and a **hardware write blocker** (prevents modifying the source).
- **Order of volatility (NIST SP 800-86)**: collect **RAM/volatile data first**,
  **archival/backup media last**. Image memory before powering a live host down.
- A **CSIRT** receives, triages, and responds to incidents. Metrics: **MTTD**
  (begin→detect), **time to respond** (detect→response), **time to contain**
  (detect→stop spread), **dwell time** (total undetected). Lower MTTD/containment
  ⇒ less dwell ⇒ less damage.
- A **playbook/runbook** = documented steps for a specific incident type; it
  standardizes response and **escalation**. **RBA/SOAR** automates **high-volume,
  well-defined, repetitive** tasks (e.g., alert enrichment), reducing time and
  error.
