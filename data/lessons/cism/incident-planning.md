# Incident Response Planning & Readiness

Sooner or later, something gets through. Incident management is the discipline of
being *ready* for that moment and handling it so the business suffers as little as
possible. This is the second-largest domain on the exam, and it rewards the same
managerial instinct as the rest: prepare in advance, decide by severity, and
communicate to the right people. In this lesson we build the foundation —
readiness and the incident response plan — and introduce the lifecycle the next
lesson completes.

## What incident management is for

> **Incident management** is the capability to prepare for, detect, respond to,
> and recover from security incidents. Its **PRIMARY goal is to minimize the
> impact of incidents on the business and restore normal operations** as quickly
> as possible.

Keep that goal in mind, because the exam's best answers flow from it. The point of
incident response is **not** to catch the hacker, punish someone, or achieve
perfect forensics — it's to **protect the business and get back to normal.** When
options compete, the one that limits business impact usually wins.

A quick distinction worth holding:

> An **event** is any observable occurrence; an **incident** is an event (or
> series) that actually harms, or threatens to harm, the confidentiality,
> integrity, or availability of information. Most events are harmless noise; the
> job is to find the incidents inside the flood of events.

## Readiness: the work you do before anything happens

The single biggest factor in how well an organization handles an incident is how
well it prepared. You cannot improvise a good response at 3 a.m. during a
ransomware outbreak.

> What **MOST improves** an organization's readiness is a **documented *and
> regularly tested* incident response plan.** Documentation alone is not enough —
> an untested plan fails under real pressure.

The emphasis on **tested** is deliberate and heavily examined. A plan in a binder
nobody has rehearsed is a false comfort. Testing — through **tabletop exercises**
(talk-through scenarios) and more involved **simulations** — surfaces the gaps:
unclear roles, missing contact info, broken assumptions. The manager's job is to
build readiness, which includes:

- A **written IR plan** that everyone can find and follow.
- A trained **incident response team (IRT / CSIRT)** with defined roles.
- **Tools, access, and resources** staged in advance (logging, forensics
  capability, out-of-band communications).
- **Regular testing** and updates as the environment changes.

Preparation is the first phase of every incident-response lifecycle for exactly
this reason: readiness is a choice you make long before the alert fires.

## The incident response plan

> An **incident response plan** is the documented, approved set of procedures,
> roles, and decision criteria that governs how the organization detects,
> classifies, responds to, and recovers from incidents.

A strong plan answers, in advance: *How do we know it's an incident? How bad is
it? Who does what? Who do we tell, and when? How do we get back to normal?* Two
elements of the plan deserve special attention because the exam loves them:
**classification** and **communication/escalation.**

### Classify by severity — it drives everything

The moment an incident is confirmed, you must size it up.

> **Classifying an incident's severity is important because it determines the
> appropriate response, escalation, and allocation of resources.** You respond to
> a minor, contained event very differently from a company-wide breach.

Severity is the dial that controls how much of the organization you mobilize.
Over-respond to a trivial event and you waste resources and credibility;
under-respond to a major one and you let it metastasize. A good classification
scheme (e.g., low / moderate / high / critical) ties each level to defined
response times, escalation paths, and who gets pulled in.

### Communication and escalation — plan it in advance

Who gets told about a serious incident, and when? Not whoever the responder
happens to think of in the moment.

> During a major incident, the people informed are the **predefined stakeholders
> named in the communication/escalation plan** — which can include **senior
> management, legal, HR, public relations, and, where required, regulators and
> affected customers** — scaled to the incident's severity.

Baking this into the plan beforehand prevents two failures: silence (leadership
blindsided, legal obligations missed) and chaos (everyone emailing everyone). The
manager ensures the plan predefines *who* communicates *what* to *whom* at each
severity level, and respects legal **breach-notification** timelines. Notice this
is a management and communication function, not a technical one — classic CISM
territory.

## The lifecycle, and the first move: validate before you act

Incident response follows a lifecycle. A common formulation (NIST SP 800-61) is:
**Preparation → Detection & Analysis → Containment, Eradication & Recovery →
Post-Incident Activity.** ISACA frames the same flow around readiness, detection
and triage, response, and recovery/review. We've covered preparation; the next
lesson handles containment, eradication, and the lessons-learned review. One move
belongs here, because it sits at the very start of handling any alert:

> When a monitoring alert suggests a possible intrusion, the response team should
> **FIRST validate and analyze the alert** to confirm whether a real incident has
> occurred. Declaration, escalation, and action all follow from that triage.

Jumping to containment or notification before confirming the alert is real wastes
effort and can cause its own harm (disrupting systems over a false alarm). You
**detect, then triage/validate, then classify, then respond.** That ordering —
understand before you act — is the same reflex you saw with gap analysis in
governance. The exam rewards it every time.

## The manager's reflex

- The goal is always **minimize business impact and restore operations** — not
  catch the attacker.
- Readiness means a **documented *and tested* plan** plus a trained team.
- On any alert: **validate/triage FIRST**, then **classify by severity**, which
  **drives response, escalation, and resources.**
- Communicate to **predefined stakeholders** per the plan, scaled to severity.

## Exam focus

- The **PRIMARY goal of incident management is to minimize business impact and
  restore normal operations** — not forensics or attribution for its own sake.
- Know **event vs. incident**: an incident actually harms or threatens CIA.
- What **MOST improves readiness** is a **documented *and regularly tested*** IR
  plan; untested plans fail. Test with **tabletop exercises and simulations.**
- **Classifying severity determines the response, escalation, and resource
  allocation** — it's the dial for how much of the organization you mobilize.
- Inform **predefined stakeholders in the communication/escalation plan** (senior
  management, legal, PR, regulators/customers as required), scaled to severity.
- On a new alert, **validate and analyze it FIRST**; detection → triage →
  classification → response, never act before confirming.
