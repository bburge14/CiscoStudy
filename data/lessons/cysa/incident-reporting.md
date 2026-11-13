# Incident Reporting, Declaration & Regulatory Timelines

During an incident, *who you tell and when* can matter as much as the technical
response — a missed legal deadline turns a contained breach into a regulatory
penalty. This lesson covers declaring an incident, communicating about it safely,
and the hard-number notification timelines that regulators impose. These day-counts
are among the most frequently tested facts in the whole domain, so learn them
exactly.

## Declaring and escalating

An incident doesn't manage itself; someone has to *call it one*.

> When analysis confirms activity past the plan's severity threshold — say, active
> exfiltration of regulated data — the correct step is to **formally declare an
> incident and escalate per the incident-response plan**. Declaration triggers the
> authority, budget, and communication paths the plan defines.

Who you pull in first depends on the incident. For a confirmed breach of customer
**personal data**, engage **legal / privacy counsel first** to determine the
organization's **mandatory notification obligations** — the clock on those is
often already running.

## Identifying the stakeholders

Before you can notify anyone, you have to know *who* — and a breach touches far
more people than the SOC. Build the stakeholder list during preparation so you're
not improvising mid-crisis.

- **Internal stakeholders** — executive leadership (who own the business risk),
  **legal/privacy counsel** (notification duties and liability), **public
  relations/communications** (external messaging), **HR** (if an insider or an
  employee is involved), IT/engineering (the responders), and the **business/system
  owners** of the affected services.
- **External stakeholders** — regulators and supervisory authorities, **law
  enforcement** where a crime is involved, affected **customers and data
  subjects**, **partners** bound by contract, the **cyber-insurance** carrier, and
  peer **ISACs** for sector-wide awareness.

> Match the detail to the stakeholder. Executives need business impact and
> decisions; regulators need the facts the law specifies; customers need plain
> guidance on what happened and what to do. One incident, many tailored messages.

### Severity drives the response

How loudly you escalate depends on **severity classification** — most plans rank
incidents on a scale (for example, low/medium/high/critical) weighing data
sensitivity, scope, and business impact. The severity level determines who gets
woken up, how fast, and whether the event crosses the threshold that triggers
*formal declaration* and the external clocks below. Misclassifying a major breach
as routine is how notification deadlines get blown.

## Communicating safely during an incident

- **Out-of-band channels.** When corporate email and Active Directory may be
  compromised, move coordination to a separate, trusted channel (an encrypted
  phone bridge). The reasons are twofold: the **primary systems may be untrusted
  or unavailable**, and the **attacker may be reading internal communications**.
- **Control external messaging.** An engineer wanting to post technical breach
  details to personal social media "for transparency" must not. **Route all
  external and media communications through PR and legal; staff must not disclose
  independently.** Uncoordinated disclosure creates legal exposure and tips off
  the adversary.

## Regulatory notification timelines

Different laws impose different deadlines, each triggered by a different event.
Memorize these:

| Regulation / rule | Who / what | Deadline |
|-------------------|-----------|----------|
| **EU GDPR** | Notify the supervisory authority of a personal-data breach | Without undue delay, **no later than 72 hours** after becoming aware |
| **SEC cybersecurity disclosure** | U.S. public company files Form 8-K (Item 1.05) for a **material** incident | **4 business days** after determining the incident is material |
| **HIPAA Breach Notification Rule** | U.S. healthcare provider notifies affected individuals of a PHI breach | **No later than 60 calendar days** after discovery |

The *trigger* is as important as the number:

- **GDPR**'s 72 hours starts when you **become aware** of the breach — and it's
  *hours*, not days.
- The **SEC**'s four business days starts at the **materiality determination**,
  not at discovery; the two dates can differ, and the clock is in *business* days.
- **HIPAA**'s 60 days runs from **discovery** of the breach, in *calendar* days.

> A memory hook: **GDPR = 72 hours, SEC = 4 business days, HIPAA = 60 calendar
> days.** Mixing up the units (hours vs. business days vs. calendar days) is the
> trap.

## Insurance and third parties

If the organization holds a **cyber-insurance** policy, notify the carrier
**promptly** after an incident like ransomware — for two valid reasons:

- **Timely notice is often a condition of coverage** under the policy; miss it and
  the claim may be denied.
- The insurer may **require the use of approved vendors** (incident-response firms,
  forensics, legal) — using your own without approval can jeopardize the claim.

## The incident report itself

Once the dust settles, the written incident report communicates the whole event
to its stakeholders. A complete report covers the essentials — *who, what, when,
where, and why* — along with the **impact and scope**, a **timeline**, the
**evidence**, and **recommendations**. Executives get a concise **executive
summary**; technical teams get the detail.

Finally, after a resolved incident the team produces a **lessons-learned report**.
Its primary purpose is to **identify what worked and what didn't so processes and
controls can be improved to prevent recurrence** — the same forward-looking goal
that closes the response lifecycle.

## Exam focus

- Confirmed activity past the severity threshold → **formally declare and escalate
  per the IR plan**. For a personal-data breach, engage **legal/privacy counsel
  first** to determine notification duties.
- Use **out-of-band comms** because primary systems may be compromised/unavailable
  **and** the attacker may be reading them. **Route all external/media comms
  through PR and legal**; staff never disclose on their own.
- **Timelines:** **GDPR = 72 hours** after becoming aware; **SEC = 4 business
  days** after determining materiality (Form 8-K Item 1.05); **HIPAA = 60 calendar
  days** after discovery. Watch the *units* and the *trigger event*.
- Notify **cyber-insurance** promptly — timely notice is often a **coverage
  condition**, and insurers may mandate **approved vendors**.
- An incident report covers **who/what/when/where/why, impact, scope, timeline,
  evidence, recommendations**; the **lessons-learned report** exists to **prevent
  recurrence**.
