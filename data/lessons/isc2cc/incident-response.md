# Incident Response

No matter how good your defenses are, something will eventually go wrong. What
separates a minor hiccup from a catastrophe is how well the organization *responds*.
Incident response is the disciplined, planned process for detecting, handling, and
learning from security incidents. This lesson covers the key vocabulary and the
phases of the incident-response lifecycle.

## Event, incident, and breach

These three words sound similar but mean very different things, and the exam
routinely tests the difference.

> An **event** is any observable occurrence in a system or network. An
> **incident** is an event (or series of events) that actually or potentially
> harms security. A **breach** is a confirmed incident in which protected data
> was actually accessed or disclosed.

- **Event** — something you can observe. Most events are routine and harmless: a
  user logging in, a file being saved, a packet arriving. The vast majority of
  events are nothing to worry about.
- **Incident** — an event that violates (or threatens to violate) security
  policy or the CIA of information: malware spreading, an unauthorized login, a
  system knocked offline. Incidents require a response.
- **Data breach** — a specific, confirmed incident in which sensitive or
  protected data (like customer records) is actually accessed, copied, or
  disclosed to unauthorized parties. A breach is a serious subtype of incident.

The relationship is a funnel: countless **events**, a small number of which turn
out to be **incidents**, a few of which are confirmed **breaches**.

## The incident-response team

Organizations don't improvise their response — they charter a dedicated team.

> A **CSIRT** (Computer Security Incident Response Team), also called a CIRT or
> IRT, is the group of trained staff responsible for detecting, responding to,
> and recovering from security incidents.

The CSIRT typically includes security analysts plus representatives from IT,
legal, management, and communications, so the organization can respond on every
front at once — technical, legal, and reputational.

## The incident-response lifecycle

Incident response follows a repeatable lifecycle. The widely taught model comes
from NIST's *Computer Security Incident Handling Guide* (SP 800-61) and has four
phases. (NIST refreshed the guide in 2025 to align with its Cybersecurity
Framework, but the four-phase lifecycle below is still the standard way these
concepts are taught and tested.)

### 1. Preparation

Everything you do *before* an incident: writing the incident-response plan,
assembling tools, defining roles, and training the team. Preparation is the first
phase and the foundation for all the others — you can't respond well to something
you never planned for.

### 2. Detection and Analysis

Here the team notices a possible incident and investigates it. An alert fires,
and responders examine logs and evidence to **confirm** whether a real incident
is occurring and to determine its **scope and severity**. This phase answers "is
this real, and how bad is it?"

### 3. Containment, Eradication, and Recovery

Once an incident is confirmed, the team works through three closely linked steps:

- **Containment** — limit the spread and scope so the damage stops growing. The
  classic move is isolating an infected server from the network before the
  malware reaches other systems.
- **Eradication** — remove the cause of the incident: delete the malware and fix
  (patch) the vulnerability that let it in, so it can't recur from the same
  source.
- **Recovery** — restore the affected systems to normal production and carefully
  monitor them to confirm they are clean and working properly.

The order matters: you **contain** first to stop the bleeding, **eradicate** to
remove the threat, then **recover** to return to normal. Rushing to recovery
before eradication just lets the attacker back in.

### 4. Post-Incident Activity (Lessons Learned)

After the dust settles, the team meets to review what happened: what worked, what
didn't, and what to change. The output feeds improvements back into
**preparation**, closing the loop so the next response is better. This is where a
painful incident becomes an investment.

A quick way to remember the flow: **Prepare → Detect & Analyze → Contain,
Eradicate, Recover → Learn.**

## What a regular user should do

Most employees aren't on the CSIRT, but they're often the first to notice
trouble. The single most important thing a user can do is **report promptly**.

> If an employee suspects an incident — their computer is behaving strangely, or
> they think they clicked a phishing link — they should **report it immediately**
> to the help desk or security team through the proper channel, and *not* try to
> investigate or fix it themselves.

Fast reporting lets trained responders begin containment before the damage
spreads. A user who stays quiet, or who starts poking around on their own, can
destroy evidence or make things worse.

## Exam focus

- **Event** = any observable occurrence (usually harmless). **Incident** = an
  event that harms or threatens security. **Breach** = a *confirmed* incident
  where protected data was actually exposed.
- The **CSIRT** (a.k.a. CIRT/IRT) is the team chartered to handle incidents.
- Know the four lifecycle phases in order: **Preparation → Detection & Analysis →
  Containment, Eradication & Recovery → Post-Incident Activity (lessons
  learned)**.
- **Containment** = stop the spread (isolate the host). **Eradication** = remove
  the cause (delete malware, patch the hole). **Recovery** = restore to normal
  and monitor. Do them in that order.
- **Preparation** happens *before* any incident; **lessons learned** feeds back
  into preparation.
- A user who suspects an incident should **report it promptly** through the
  proper channel — not investigate or fix it alone.
