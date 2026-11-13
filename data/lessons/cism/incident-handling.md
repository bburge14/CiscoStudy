# Containment, Eradication & Post-Incident Review

An incident has been confirmed and classified. Now the team has to stop the
bleeding, clean out the infection, get back to normal, and — the step everyone is
tempted to skip — learn from it. This lesson walks the heart of the incident
lifecycle: containment, eradication, and recovery, in that order, followed by the
post-incident review that turns a bad day into a stronger program. As always,
think like the manager coordinating the response, not the analyst at the keyboard.

## The order matters: contain, then eradicate, then recover

These three phases come in a fixed sequence, and the exam tests whether you know
which is which and why order matters. The analogy is a house fire: first you stop
it spreading (containment), then you put it out and remove what's smoldering
(eradication), then you rebuild and move back in (recovery).

> - **Containment** — limit the spread and impact of the incident, e.g. by
>   **isolating affected systems or network segments**, so the damage stops
>   growing while you work.
> - **Eradication** — **remove the threat**: delete the malware, close the
>   exploited vulnerability, and eliminate the attacker's footholds and
>   persistence.
> - **Recovery** — **restore affected systems to normal operation** and confirm
>   they're clean and functioning before returning them to service.

Match the exam's cues:

| Action | Phase |
|--------|-------|
| Isolating infected network segments during an outbreak | **Containment** |
| Removing malware and closing the exploited hole | **Eradication** |
| Rebuilding systems and returning them to production | **Recovery** |

Why this order? **Contain first** so the problem stops growing while you
investigate — if you start cleaning one machine while the worm keeps spreading,
you lose. Then **eradicate**, because restoring a system while the attacker still
has a foothold just hands it back to them. Then **recover**, verifying before you
reconnect. Skipping or reordering these is a reliable wrong answer.

### Short-term vs. long-term containment

Containment often has two gears: a quick move to stop immediate harm (pull the
cable, disable the account) and a more considered one (rebuild in a clean
segment) that buys time to eradicate properly. The manager balances *stopping the
damage* against *preserving the business* — and against preserving evidence.

## Preserve the evidence: chain of custody

Especially when an incident may lead to legal action, discipline, or regulatory
scrutiny, how you handle evidence matters as much as the technical cleanup.

> **Chain of custody** is the documented, unbroken record of who collected,
> handled, and stored each piece of evidence, and when. It preserves the
> evidence's integrity so it can be trusted — in court or an investigation.

Here's the tension the exam likes: aggressive containment (wiping a machine
immediately) can **destroy forensic evidence.** The manager weighs the need to
stop damage against the need to preserve evidence, guided by the incident's
severity and legal implications. If evidence could be needed later, you capture
it (forensic images, logs) *before* you eradicate. Accountability and
documentation — the manager's themes — apply even in the middle of a crisis.

## Measuring the response

You manage what you measure, and incident response has its own key metrics:

- **MTTD (Mean Time to Detect)** — how long before you notice an incident.
- **MTTR (Mean Time to Respond/Recover)** — how long to contain and restore.

Falling detection and response times are signs of a maturing capability; rising
ones are a warning. These feed the reporting you deliver to leadership and the
improvements you drive through the review that follows.

## Post-incident review: the step that pays forward

When the fire is out, the amateur moves on; the professional asks *why it happened
and how we respond better next time.* This is the **post-incident review**, also
called the **lessons-learned** session or post-mortem.

> The **PRIMARY purpose of a post-incident review is to identify root causes and
> improvements that prevent recurrence and strengthen the response capability.**
> It is about learning and improving — not assigning blame.

A review conducted to punish people teaches everyone to hide problems; a review
conducted to learn makes the whole program better. The exam consistently frames
it as improvement-oriented, so beware "blame"-flavored distractors. A good review:

- Reconstructs the timeline and establishes the **root cause** (root-cause
  analysis asks *why* until it reaches the underlying failure, not just the
  surface symptom).
- Evaluates what worked and what didn't in the response itself.
- Produces concrete, assigned **improvements** with owners and deadlines.

### Close the loop — act on what you learn

A review that generates insight but changes nothing is wasted. The exam makes
this point directly:

> When a post-incident review finds a weakness — say, **unclear escalation paths
> delayed the response** — the manager should **update the incident response plan
> and related processes to correct it.** Findings feed back into readiness.

This is the lifecycle closing on itself: post-incident learning flows back into
**preparation**, so the next incident is handled better. Updating the plan,
retraining the team, adding a control, or fixing the root-cause vulnerability —
these are how an organization actually gets more resilient. Improvement that
isn't implemented is just a nicely written report.

## The manager's reflex

- Phases run **containment → eradication → recovery**, in that order and for a
  reason. Stop the spread, then remove the threat, then restore and verify.
- Weigh fast containment against **evidence preservation** (chain of custody)
  when legal consequences are possible.
- The post-incident review exists to **find root causes and improve**, never to
  blame — and its findings must **update the plan and processes.**

## Exam focus

- **Containment = limit spread / isolate**; **eradication = remove the threat
  (malware, vulnerability, footholds)**; **recovery = restore to normal and
  verify.** Know the order and never recover before eradicating.
- Preserve evidence with a documented **chain of custody**; aggressive
  containment can **destroy forensic evidence**, so capture it first when legal
  action is possible.
- Track **MTTD/MTTR**; improving times signal a maturing response capability.
- The **post-incident review's PRIMARY purpose is to find root causes and drive
  improvements to prevent recurrence** — it is learning-focused, not blame.
- **Act on review findings**: update the **IR plan and processes** so lessons
  feed back into preparation and the next incident goes better.
