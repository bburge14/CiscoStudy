# Awareness, Training, Metrics & Reporting

Two of a manager's highest-leverage activities close out the program domain:
shaping how *people* behave, and proving to leadership that the program *works*.
People are both the biggest vulnerability and the largest sensor network you
have; metrics are how you turn a year of effort into a story an executive will
fund. Neither is technical — both are pure management — and both show up often on
the exam.

## Security awareness: changing behavior, not just informing

Most breaches have a human somewhere in the chain — someone clicked, someone
reused a password, someone emailed a spreadsheet to the wrong address. An
awareness program exists to move that human behavior.

> The **PRIMARY goal of a security awareness program is to influence employee
> behavior** so that staff recognize security risks and respond appropriately.
> The target is *behavior*, not mere knowledge.

That emphasis matters on the exam. The point of awareness is **not** "to inform
employees of the policy" or "to satisfy a compliance checkbox" — those are
distractors. Information that doesn't change what people *do* has failed. A
program that measurably reduces click-through on phishing tests is working; a
glossy memo nobody acts on is not.

### Awareness vs. training vs. education

These three are a ladder of depth, and the exam likes to separate them.

| Level | Goal | Example |
|-------|------|---------|
| **Awareness** | Change behavior; keep security top-of-mind | Phishing reminders, posters, simulations |
| **Training** | Build specific skills for a role | Teaching developers secure-coding practices |
| **Education** | Deep, lasting understanding | A degree or professional certification |

Awareness is broad and ongoing; training is role-specific and skill-building;
education is deep and formal. Mixing these up is a common trap.

### How to deliver it well

Delivery is where programs succeed or fail. The exam's preferred answer:

> Awareness is BEST delivered **tailored to the roles and responsibilities of
> different audiences, and on an ongoing (continuous) basis** — not as a single
> annual slide deck everyone clicks through.

Why tailored and ongoing? A finance clerk faces invoice fraud; a developer faces
code vulnerabilities; an executive faces whaling. One-size content wastes
everyone's time. And a once-a-year session is forgotten by February — behavior
change needs reinforcement. Leadership support matters too: when executives
visibly take part, the rest of the organization takes it seriously. Measure the
program's effect (phishing-test results, incident reports from staff) and adapt
it — awareness is itself a managed, improving process.

## Metrics: proving the program works

A program you can't measure is a program you can't defend at budget time. But a
*number* is not automatically a *metric*. Good metrics are **meaningful,
measurable, actionable, and aligned** to objectives — they answer a decision, not
just fill a slide.

> A **metric** is a measurement that supports a decision. "We blocked 4 million
> packets" is trivia; "95% of critical patches were applied within SLA, up from
> 80%" tells leadership whether a risk is under control.

### KPI vs. KRI vs. KGI — know the three

The exam lives on these three-letter terms. Keep them straight by what they
measure.

> - **KPI (Key Performance Indicator)** — how well a *process is performing*.
>   *Example:* the percentage of critical patches applied within the target
>   window.
> - **KRI (Key Risk Indicator)** — an *early-warning* signal that *risk exposure*
>   is rising toward or past acceptable levels. *Example:* a climbing count of
>   overdue critical patches.
> - **KGI (Key Goal Indicator)** — whether a *goal/objective has been achieved*.
>   *Example:* "the organization achieved ISO/IEC 27001 certification."

A memory hook: **KPI = performance (how well are we doing the work?)**, **KRI =
risk (is danger rising?)**, **KGI = goal (did we reach the outcome?)**. Note how
the *same underlying data* — patch timeliness — becomes a KPI when framed as
process performance and a KRI when framed as rising risk. The framing, not the
number, decides the label. That's a classic exam discrimination.

## Reporting: speak the audience's language

Collecting metrics is half the job; the other half is **reporting** them to the
right audience in terms that audience cares about. The single biggest reporting
mistake a manager can make is burying executives in technical detail.

> When reporting to the **board or senior management**, focus on
> **business-relevant information — risk posture, trends, and alignment with
> business objectives** — not firewall logs, patch counts, or packet statistics.

Think about what a board can actually *do* with the information. They can't tune
a SIEM, but they can decide to fund a program, accept a risk, or change
priorities — so give them the view that supports those decisions:

- **Technical teams** need operational detail: vulnerabilities, patch status,
  alert volumes.
- **Middle management** needs process performance: are controls operating,
  SLAs met?
- **The board/executives** need the big picture: how much risk are we carrying,
  is it trending up or down, and are we aligned with the business and compliant?

Reporting at the right **altitude** is a hallmark of a mature manager — and a
reliable right answer when the exam asks what to present to leadership. Tie it
back to governance: value delivery and performance measurement only land if
leadership can *understand* what you report.

## The manager's reflex

- Awareness exists to **change behavior**; deliver it **tailored and ongoing.**
- **KPI = process performance, KRI = rising risk (early warning), KGI = goal
  achieved.** Watch for the same data reframed.
- When reporting up, **translate to business risk and trends** — never technical
  minutiae for a board.

## Exam focus

- The **PRIMARY goal of security awareness is to influence/change employee
  behavior**, not merely to inform or to tick a compliance box.
- **Awareness → training → education**: top-of-mind behavior, then role-specific
  skills, then deep formal understanding.
- Awareness is **BEST delivered role-tailored and on an ongoing basis**, with
  leadership support, and measured so it can improve.
- **KPI** measures **process performance** (e.g., % critical patches applied in
  time); **KRI** is an **early warning of rising risk**; **KGI** shows a **goal
  was achieved.** The same data can be a KPI or a KRI depending on framing.
- **Report to the board in business terms** — **risk posture, trends, alignment
  with objectives** — not technical detail. Match the metric's altitude to the
  audience.
