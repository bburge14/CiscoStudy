# The Incident Response Lifecycle

Sooner or later, something gets through. When it does, the difference between a
contained scare and a catastrophic breach is whether the organization has a
practiced, disciplined **incident response (IR)** process. This lesson walks the
IR lifecycle phase by phase — the order matters enormously, and the exam tests it
directly — and clears up where NIST's guidance sits today.

## What counts as an incident

> An **event** is any observable occurrence; a **security incident** is an event
> that actually violates (or imminently threatens) security policy, or the
> confidentiality, integrity, or availability of information.

Not every alert is an incident, and not every incident is a breach. A **breach**
specifically involves confirmed unauthorized access to or disclosure of protected
data. Part of IR is **triage** — quickly deciding whether an alert is a real
incident and how severe it is, so the response matches the threat.

## The lifecycle, phase by phase

The SSCP uses a six-phase model. Learn the phases *and their order*, because a
very common question simply asks you to sequence them:

> **Preparation -> Detection & Analysis (Identification) -> Containment ->
> Eradication -> Recovery -> Lessons Learned (Post-Incident Activity).**

### 1. Preparation

Everything you do *before* an incident: writing the IR plan, standing up the
**CSIRT** (Computer Security Incident Response Team), defining roles and
escalation paths, deploying monitoring, keeping contact lists and **runbooks**
current, and training through tabletop exercises. The best responders win the
incident here, long before it happens. Preparation is the one phase that's always
ongoing.

### 2. Detection & Analysis (Identification)

Recognizing that an incident is occurring — from SIEM alerts, IDS/IPS, user
reports, or threat intel — and then *analyzing* it to confirm it's real, determine
scope, and assess severity. You can't respond to what you haven't detected.

### 3. Containment

Limiting the damage and stopping the spread *before* you clean up. This is often
the most time-critical phase. The exam distinguishes:

- **Short-term containment** — immediate, often crude action to stop the bleeding
  (isolate or disconnect the infected host from the network).
- **Long-term containment** — temporary fixes that let the business keep running
  while you prepare eradication (e.g., rebuilding clean systems in parallel).

> During an active malware outbreak, **isolating infected hosts to stop the spread
> is containment** — and it comes *before* eradication. Don't start cleaning until
> you've stopped the fire from spreading. A key judgment call: preserve evidence
> during containment if the incident may lead to prosecution.

### 4. Eradication

Removing the cause: delete the malware, remove attacker artifacts and backdoors,
disable breached accounts, and **patch the exploited vulnerability** so the same
attack can't simply recur. Eradication addresses the root cause, not just the
symptom.

### 5. Recovery

Restoring affected systems to normal, validated operation — rebuilding or
restoring from known-clean backups, carefully returning systems to production, and
**monitoring closely** to confirm the threat is truly gone and doesn't come back.
Business decides when systems are trusted enough to go live.

### 6. Lessons Learned (Post-Incident Activity)

After the dust settles (ideally within a week or two), the team holds a **post-
incident review**: What happened? How did we do? What do we change? The output
feeds directly back into **Preparation**, improving the plan, the controls, and
the training. Skipping this phase guarantees you'll relive the same incident.

## A quick cross-walk to NIST

You'll see NIST referenced two ways, and both are "correct" depending on the
edition:

| Framing | Phases |
|---------|--------|
| **NIST SP 800-61 Rev. 2** (classic) | Preparation; Detection & Analysis; Containment, Eradication & Recovery; Post-Incident Activity |
| **SSCP six-phase** | Preparation; Identification; Containment; Eradication; Recovery; Lessons Learned |

The two are the same journey sliced differently — Rev. 2 bundles containment,
eradication, and recovery into one phase. Note that **NIST SP 800-61 Revision 3
(April 2025)** re-casts incident response around the **NIST Cybersecurity
Framework 2.0 functions** (Govern, Identify, Protect, Detect, Respond, Recover)
rather than a linear lifecycle. For the SSCP, the six-phase lifecycle above is
what you'll be tested on, but it's worth knowing the guidance has modernized.

## Roles, communication, and discipline

A good response is a *coordinated* one. Know your **CSIRT roles** (incident
handler, analysts, legal, communications/PR, management). Follow the
**communication plan** — including **out-of-band** channels, because if the
attacker is in your email, you don't discuss the response over that same email.
Understand escalation and legal/regulatory **notification** duties; many breach
laws impose tight reporting deadlines. And resist the urge to jump straight to
"fix it" — responding out of order (eradicating before containing, recovering
before eradicating) is how incidents get worse.

## Exam focus

- Memorize the order: **Preparation -> Detection & Analysis -> Containment ->
  Eradication -> Recovery -> Lessons Learned.** Sequencing questions are common.
- **Containment comes before eradication.** Isolating infected hosts to stop the
  spread is **containment**; removing the malware and **patching the exploited
  flaw** is **eradication**; restoring from clean backups is **recovery**.
- **Preparation** (plan, CSIRT, runbooks, training) and **Lessons Learned** (feeds
  back into preparation) bookend the process.
- **Short-term vs long-term containment**: stop the bleeding now vs. keep running
  while preparing a full fix.
- NIST **SP 800-61 Rev. 2** bundles containment/eradication/recovery; **Rev. 3
  (2025)** reframes IR around the **CSF 2.0 functions**. Preserve evidence and use
  **out-of-band** communications when the attacker may be watching.
