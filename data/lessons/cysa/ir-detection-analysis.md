# Detection, Analysis & Digital Forensics

This is the phase where a stray alert becomes a confirmed incident with a scope,
a timeline, and evidence that would survive a courtroom. Detection and analysis
demand two disciplines at once: the *analytical* skill to tell a real attack from
noise, and the *forensic* rigor to collect evidence without destroying it. Get
the forensics wrong and even a correct conclusion may be unusable.

## Precursors vs. indicators

NIST SP 800-61 gives us two words for "signs," and they are not interchangeable:

> A **precursor** is a sign that an incident *may occur in the future*; an
> **indicator** is a sign that an incident *may have occurred or is occurring
> now*.

Reconnaissance scanning against a web app in a server log is a **precursor** — it
suggests an attack *might* be coming. The exploit attempt that follows would be an
indicator. Spotting precursors is your chance to get ahead of the attacker.

## From alert to confirmed incident

An alert is a hypothesis; analysis tests it.

- **Validate before you escalate.** When a SIEM fires a "malware detected" alert,
  first confirm the file is truly malicious and present on the host. If it isn't,
  you were **acting on a false positive** — and escalating it wastes the team.
- **Scope the incident.** Once one workstation is confirmed infected, query
  **EDR across the fleet** to find every host showing the same indicators.
  *Scoping* answers "how far did this spread?" before you plan containment.
- **Correlate the right logs.** To learn whether a compromised account logged in
  to multiple servers, correlate **authentication/security event logs from the
  servers and domain controllers** first — that is where logon events live.

Those artifacts — a malicious **file hash**, a **C2 IP**, a suspicious **domain** —
are collectively **Indicators of Compromise (IoCs)**. Which data source you reach
for depends on the question: **EDR telemetry** for a timeline of process
execution and parent-child relationships, **full packet capture (PCAP)** when you
need the actual payloads and destinations of exfiltrated traffic.

## Digital forensics: collect it right

Analysis that may lead to legal action has to follow forensic procedure, or the
evidence is worthless.

### Order of volatility

> The **order of volatility** says: collect the *most ephemeral* evidence first,
> because it disappears soonest. **CPU cache/registers and RAM** go first, before you ever
> power the machine down.

From a running, compromised server, the memory and cache must be captured before
anything that would disturb them — disk images and archived logs can wait because
they persist. Powering off to "preserve" a system actually destroys the most
volatile and often most valuable evidence.

### Preserving integrity

- **Capture volatile memory before powering down**, then image the disk.
- **Hash everything.** Compute a cryptographic hash (e.g., **SHA-256**) of both
  the original and the copy, before and after imaging, to prove the image is a
  **bit-for-bit, unaltered copy**. Record the hash with the evidence.
- **Use a write blocker.** Before analyzing a suspect drive, connect it through a
  **write blocker** — a device that permits reading but prevents any writes to the
  original media, so the act of examining it can't alter it.
- **Chain of custody.** Record **who handled the evidence, when, and why at every
  transfer**. This documentation establishes an unbroken chain that proves the
  evidence wasn't tampered with — essential if it ever reaches court.

> For a live acquisition that may become a legal case, the two must-do actions are:
> **generate and record a hash of each acquired image**, and **capture volatile
> memory before powering down**. Integrity plus volatility, together.

### Forensic artifacts worth knowing

- **Windows Prefetch** files prove that a now-deleted executable actually *ran* on
  a host — invaluable when the malware is gone but you need to show it executed.
- **Memory-forensics frameworks** such as **Volatility** parse a RAM image to list
  the processes that were running, their network connections, and any injected
  code at the moment of capture — turning a raw memory dump into an investigation.

## Live vs. static acquisition — and legal hold

*How* you acquire evidence depends on the state of the system:

- **Live (volatile) acquisition** captures a running system's memory, active
  network connections, and running processes — evidence that vanishes on
  shutdown. Required when the machine can't be taken down or holds RAM-only
  artifacts.
- **Static (dead) acquisition** images powered-off media through a write blocker.
  It's the most defensible for disk evidence because the source never changes
  during collection.

When litigation is possible, a **legal hold** is issued to preserve all
potentially relevant data and suspend routine deletion — destroying evidence
under a hold, even by automated retention policy, can be **spoliation**. Beyond
Prefetch, analysts lean on other Windows artifacts to reconstruct activity:
**Amcache/Shimcache** for program-execution history, **Shellbags** for which
folders a user browsed, and the event logs covered in the first lesson. Each adds
a corroborating data point to the story.

## Building the timeline

Everything above feeds one deliverable: a defensible timeline of what happened,
when, and on which systems. Correlated logs, EDR process trees, memory artifacts,
and packet captures — all time-aligned — let you state with confidence how the
attacker got in, what they touched, and whether data left. That timeline drives
the containment and recovery decisions in the next lesson, and the reporting in
the final unit.

## Exam focus

- **Precursor** = sign an incident *may happen later* (e.g., recon scanning);
  **indicator** = sign one is happening/has happened.
- **Validate** a SIEM alert before escalating (avoid acting on a **false
  positive**); **scope** with fleet-wide **EDR** queries; correlate
  **authentication logs from servers and domain controllers** for account misuse.
- A hash + C2 IP + domain together are **IoCs**. Use **EDR** for process
  timelines, **full PCAP** for exfiltration payloads.
- **Order of volatility:** collect **CPU cache/registers and RAM first**; **capture memory
  before powering down**.
- Prove integrity with a **SHA-256 hash** (bit-for-bit copy), a **write blocker**
  (read-only access to original media), and a documented **chain of custody**
  (who/when/why at each transfer).
- **Prefetch** proves a deleted executable **ran**; **Volatility** analyzes a
  **RAM image** for processes, connections, and injected code.
