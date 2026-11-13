# Investigations, Forensics & Incident Management

Security operations is where plans meet reality. When something goes wrong, you
must investigate it correctly — preserving evidence that could end up in court — and
run a disciplined incident response that limits damage and restores trust. This
lesson covers digital investigations and forensics, then the incident management
lifecycle, both of which CISSP tests as process, not heroics.

## Types of investigation

The *kind* of investigation sets the evidentiary bar you must meet.

| Investigation | Standard of proof | Example |
|---------------|-------------------|---------|
| **Criminal** | **Beyond a reasonable doubt** (highest) | Prosecuting an intruder |
| **Civil** | **Preponderance of the evidence** (more likely than not) | A contract dispute |
| **Administrative / internal** | Lowest; internal policy | HR misconduct review |
| **Regulatory** | Set by the regulator | A compliance inquiry |

Because you rarely know at the outset whether an incident will become a criminal
case, **handle all evidence to the highest standard from the start** — you can
relax later, but you cannot retroactively fix mishandled evidence.

## Digital forensics

Forensics is the disciplined collection and analysis of evidence so it remains
**admissible**. Three ideas dominate the exam.

> **Admissible evidence must be relevant, reliable (competent), and — critically —
> obtained lawfully.** Evidence gathered through an unauthorized search can be
> **excluded no matter how incriminating it is.**

That last point is a classic trap: a manager who rifles through an employee's
personal, password-protected account without authorization may find damning files,
but a court is likely to **exclude** them because they weren't legally obtained.

- **Chain of custody** — a documented, unbroken record of who handled the evidence,
  when, and why, from collection to court. A gap lets the other side argue the
  evidence was altered.
- **Order of volatility** — collect the most ephemeral data first: CPU registers and
  cache, then RAM and running processes, then disk, then archives/backups. Pull
  volatile memory before you power down, or it's gone.
- **Forensic imaging** — make a **bit-for-bit copy** and work from the copy; use a
  **write blocker** so the original isn't modified, and compute a **hash** of both
  original and image to prove they match.

Evidence types to recognize: **real** (physical objects), **documentary** (records —
subject to the **best evidence rule**, which prefers originals), **testimonial**
(witness statements), and the caution around **hearsay** (secondhand statements,
often inadmissible, though business logs have exceptions). **eDiscovery** is the
legal process of identifying and producing relevant electronically stored
information.

## The incident management lifecycle

An **incident** must first be distinguished from the noise.

> An **event** is any observable occurrence. An **incident** is an event (or series)
> that **actually or potentially harms, or threatens, the CIA of assets or violates
> policy**. A **breach** is a confirmed unauthorized disclosure or loss of protected
> data.

Thousands of events a day are normal; the skill is finding the few that are
incidents. Incident response then follows a repeatable lifecycle. (ISC)² frames the
phases roughly as **Detect → Respond → Mitigate → Report → Recover → Remediate →
Lessons Learned**; NIST SP 800-61 Rev. 2 groups them as **Preparation; Detection &
Analysis; Containment, Eradication & Recovery; Post-Incident Activity**. Either way,
the logic is the same:

- **Preparation** — build the plan, the CSIRT, tooling, and runbooks *before* an
  incident. The most valuable phase, because you can't improvise trust at 3 a.m.
- **Detection & analysis** — identify that an incident is occurring and assess scope
  and severity.
- **Containment** — stop the bleeding. Short-term containment isolates fast;
  long-term containment stabilizes while you prepare to eradicate. **Contain before
  you eradicate.**
- **Eradication** — remove the cause (malware, the attacker's access, the
  vulnerability).
- **Recovery** — restore systems to normal, validated operation and monitor for
  recurrence.
- **Lessons learned (post-incident)** — a blameless review that feeds improvements
  back into preparation. Skipping this guarantees you repeat the incident.

> The ordering is tested: **detect, then contain, then eradicate, then recover,
> then learn.** Don't wipe and rebuild (eradicate) before you've contained and
> preserved evidence, or you destroy both the investigation and the chance to
> understand root cause.

A dedicated **CSIRT (Computer Security Incident Response Team)** with clear roles,
authority, and communication paths (including when and how to notify legal, PR,
and regulators) turns chaos into process.

## Communication, reporting, and notification

An incident is never only a technical event — it triggers obligations. Mature plans
decide *who must be told, by when, and by whom* before an incident ever strikes.

- **Internal escalation** — predefined paths to management, legal, HR, and PR, so
  decisions aren't improvised under pressure.
- **Regulatory notification** — many laws impose hard deadlines (recall GDPR's
  72-hour rule to the supervisory authority); missing one is a separate violation.
- **Law enforcement** — engage them for criminal matters, accepting that doing so
  may mean ceding some control over the investigation and the evidence.
- **Single spokesperson** — route all external communication through one trained
  voice to avoid leaking details or contradicting the organization's position.

> The exam rewards the measured, process-driven answer: notify the right parties
> within required timelines and preserve evidence — not a knee-jerk "pull the
> plug" or "tell no one."

## Exam focus

- Standards of proof: **criminal = beyond a reasonable doubt**, **civil =
  preponderance of the evidence**, **administrative = lowest**. Handle evidence to
  the **highest standard from the start**.
- Admissible evidence is **relevant, reliable, and lawfully obtained**;
  **unlawfully obtained evidence is excluded** regardless of its content. Maintain
  an unbroken **chain of custody**.
- Collect by **order of volatility** (RAM before disk); make a **bit-for-bit image**
  with a **write blocker** and verify with **hashes**. Know **best evidence rule**
  and **hearsay**.
- **Event** (observable) vs **incident** (harms/threatens CIA or breaks policy) vs
  **breach** (confirmed data loss).
- IR order: **Detect → Contain → Eradicate → Recover → Lessons Learned.**
  **Preparation** is foundational; **contain before eradicating**; never skip the
  **lessons-learned** review.
- IR includes **communication and notification**: predefined escalation,
  regulatory deadlines, and a **single trained spokesperson** for external
  messaging.
