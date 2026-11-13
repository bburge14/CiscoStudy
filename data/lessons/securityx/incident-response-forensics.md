# Incident Response & Digital Forensics

When prevention and detection have done their jobs, the question becomes: how well
does the enterprise *respond*? Incident response is the disciplined process of
handling an attack from first alert to final lesson; digital forensics is the
rigorous collection and analysis of evidence that must hold up to scrutiny. This
lesson covers both, at the scale and legal exposure of an enterprise.

## The incident response lifecycle

The authoritative reference is **NIST SP 800-61**. The long-standing **Revision 2**
model defines a four-phase lifecycle you must know in order:

1. **Preparation** — build the capability before anything happens: an IR plan,
   trained team, tools, communications, and detection coverage.
2. **Detection & Analysis** — identify that an incident is occurring, scope it, and
   triage severity.
3. **Containment, Eradication & Recovery** — stop the spread, remove the threat, and
   restore systems to normal operation.
4. **Post-Incident Activity** — the "lessons learned" review that feeds back into
   preparation.

> NIST SP 800-61 (Rev 2) lifecycle, in order: **Preparation → Detection & Analysis →
> Containment, Eradication & Recovery → Post-Incident Activity.** The cycle loops:
> lessons learned feed preparation.

A currency note: **NIST SP 800-61 Revision 3 (April 2025)** reframes incident
response around the six **CSF 2.0 Functions** — **Govern, Identify, Protect, Detect,
Respond, Recover** — integrating IR into broader risk management rather than a
standalone lifecycle. Know the classic four phases (Rev 2) for most questions, and
recognize the CSF-2.0 alignment as the current direction.

### Containment decisions under pressure

Containment is where judgment shows. During an active **ransomware outbreak
spreading via SMB**, the priority is to **stop the spread immediately while
preserving evidence** — isolate/segment affected hosts from the network (pull them
off the LAN, block SMB) rather than powering them off, which destroys volatile
memory evidence. Choices the exam tests:

- **Isolation/segmentation** contains while preserving state — usually preferred.
- **Short-term vs long-term containment** — a quick stop-gap vs a durable fix.
- Don't tip off the adversary prematurely, and don't destroy evidence you'll need.

**Eradication** removes the foothold (malware, persistence, compromised accounts);
**recovery** restores from known-good backups and validates before returning to
production. **Post-incident activity** is a **blameless** review that documents root
cause, what worked, and improvements to controls and playbooks.

> A blameless, post-incident "lessons learned" review that captures root cause and
> improvements is **Post-Incident Activity** (the lessons-learned phase). "Blameless"
> is deliberate — it surfaces truth instead of hiding mistakes.

### Teams, plans, and exercises

- **CSIRT/CIRT** — the incident response team; roles span IR lead, analysts, legal,
  comms/PR, and management.
- **IR plan + playbooks** — documented, repeatable procedures per incident type.
- **Communication plan** — who is notified, including **regulatory breach-
  notification** timelines and law enforcement.
- **Exercises** — **tabletop** (discussion-based walk-throughs) and **simulations**
  validate readiness before a real event. Preparation is the phase these live in.

## Digital forensics: evidence that holds up

Forensics must be **defensible** — collected and handled so the evidence is
admissible and the analysis is trustworthy.

### Order of volatility

Collect the **most volatile data first**, because it disappears fastest:

1. **CPU registers and cache**
2. **RAM (memory) and running state** (network connections, processes)
3. **Disk / storage**
4. **Remote logs / archival media**

> The principle of collecting the most fragile data (CPU registers, RAM) before the
> durable data (disk, archives) is the **order of volatility**. For **fileless /
> in-memory malware**, this is critical: capture a **memory image of the running
> system first**, then image the disk — power-off loses the only copy of the
> threat.

### Chain of custody and integrity

- **Chain of custody** — a documented record of **every person who handled the
  evidence, plus when and why**, from collection to court. A gap can make evidence
  inadmissible.
- **Integrity via hashing** — hash evidence (e.g., SHA-256) at acquisition and
  verify the hash matches later, proving it was not altered.
- **Write blockers** — hardware/software that lets you read a drive without writing
  to it, so acquisition does not change the original.
- **Forensic imaging** — work from a **bit-for-bit copy**, never the original.

### Legal process and cloud complications

- **Legal hold / preservation** — once litigation or investigation is anticipated,
  preserve relevant data and suspend routine deletion.
- **e-Discovery** — identifying and producing electronically stored information for
  legal proceedings.
- **Cloud and virtualization** complicate forensics: you may not control the
  hardware, data is multi-tenant, and you rely on provider logs and snapshots.
  Build forensic access into cloud contracts and architecture in advance.

> Evidence admissibility rests on **chain of custody** (who/when/why handled it) and
> **integrity** (hash at collection, verify later, image via write blocker). Gaps in
> custody or unverified integrity can sink a case.

## Exam focus

- **NIST SP 800-61 (Rev 2)** IR lifecycle in order: **Preparation → Detection &
  Analysis → Containment, Eradication & Recovery → Post-Incident Activity**; Rev 3
  (2025) aligns IR to **CSF 2.0 Functions** (Govern/Identify/Protect/Detect/Respond/
  Recover).
- For ransomware spreading via SMB, **isolate/segment** affected hosts to stop
  spread **while preserving evidence** — don't power off (destroys RAM evidence).
- The **lessons-learned / Post-Incident Activity** phase is **blameless** and
  improves controls and playbooks.
- **Order of volatility**: CPU registers → RAM → disk → archives; for **fileless
  malware**, capture **memory first**, then disk.
- **Chain of custody** = who/when/why handled evidence (needed for admissibility);
  prove **integrity** with hashing and acquire via **write blocker** on a **bit-for-
  bit image**.
- **Legal hold** preserves data and suspends deletion; cloud forensics depends on
  provider logs/snapshots arranged in advance.
