# Risk Identification, Assessment & Asset Classification

Risk management is the engine room of CISM — the largest conceptual idea the
whole certification is built on. Governance sets how much risk the organization
will tolerate; risk management is how you *find*, *measure*, and *describe* risk
so leadership can make that call with eyes open. This lesson covers the first
half of the discipline: identifying and valuing what you're protecting, then
assessing and analyzing the risk to it, both in words and in numbers.

## The vocabulary risk is built from

Get these four terms exactly right; distractors are built from confusing them.

> A **threat** is something that could cause harm (a hacker, a flood, a
> careless employee). A **vulnerability** is a weakness a threat could exploit (an
> unpatched server). **Risk** is the *potential for loss* when a threat exploits
> a vulnerability. An **asset** is what you're protecting.

Risk only exists where a threat meets a matching vulnerability on an asset of
value. No vulnerability, or no asset worth harming, and the risk collapses.

> **Risk is a function of two factors combined: the likelihood that an event
> occurs, and the impact (consequence) if it does.** Raise either one and the
> risk rises.

That likelihood-times-impact idea is the backbone of every assessment, whether
you express it as "high/medium/low" or as dollars.

## Start by knowing what you have

A risk assessment that doesn't begin with assets is building on sand.

> The **FIRST** step in a risk assessment is to **identify and value the
> organization's information assets.** You cannot judge risk to something you
> haven't catalogued or valued.

You find the assets, you understand what each is worth to the business, and only
then do you reason about the threats and vulnerabilities facing them. This is why
asset classification and risk assessment belong in the same lesson: classifying
assets is how the manager assigns that value systematically.

## Asset classification: protection proportional to value

Not all data deserves the same protection. Classifying lets you spend your
finite budget where it matters — the value-delivery idea from governance, applied
to data.

> The **PRIMARY purpose of classifying information assets** is to **determine the
> appropriate level of protection based on the asset's sensitivity and
> criticality.** Classification drives the strength of the controls.

A typical scheme runs from least to most sensitive — for example *Public →
Internal → Confidential → Restricted*. The labels matter less than the principle:
the higher the classification, the stronger the required controls (encryption,
access restriction, retention rules, handling procedures).

Who sets the label? Not IT, and not you.

> The **data (information) owner** — a business leader — **determines the
> classification level.** The owner knows the business value and legal
> sensitivity of the information; IT merely enforces the resulting controls.

Classification is also the input to many later decisions: which systems need the
tightest monitoring, what must be covered by the continuity plan, and where
regulatory obligations bite hardest.

## Qualitative vs. quantitative analysis

Once risk is identified, you analyze it — and you can do so two ways.

> **Qualitative analysis** rates risk in relative terms (high/medium/low,
> ratings on a scale or heat map) using judgment and experience.
> **Quantitative analysis** assigns *numeric, usually monetary* values to
> likelihood and impact.

| | Qualitative | Quantitative |
|---|---|---|
| Expresses risk as | High / Med / Low, scores | Dollars, probabilities |
| Strength | Fast, intuitive, no hard data needed | Objective, supports cost/benefit |
| Weakness | Subjective, hard to compare precisely | Needs reliable data; time-consuming |
| Typical tool | Risk matrix / heat map | SLE, ARO, ALE |

Neither is "better" in the abstract — the manager picks the one that fits the
data available and the decision at hand. Many programs blend them: qualitative to
triage quickly, quantitative to justify a specific investment to the CFO.

## The quantitative formulas you must know

The exam expects you to compute a loss expectancy. Learn these cold.

> **Single Loss Expectancy (SLE) = Asset Value (AV) × Exposure Factor (EF)**
>
> **Annualized Loss Expectancy (ALE) = SLE × Annualized Rate of Occurrence
> (ARO)**

Definitions of the pieces:

- **Asset Value (AV)** — what the asset is worth.
- **Exposure Factor (EF)** — the *proportion* of the asset's value lost in a
  single event, as a percentage (a flood that destroys a quarter of a server
  room has EF = 0.25).
- **SLE** — the money lost in **one** occurrence of the threat.
- **ARO** — how many times per **year** you expect the event (once a decade =
  0.1; twice a year = 2).
- **ALE** — the expected loss **per year**; this is the number you compare
  against the annual cost of a control.

### Worked example

A data-center asset is valued at **$200,000**. A flood would destroy an estimated
**25%** of its value, and floods are expected about **once every 10 years**.

1. **SLE** = AV × EF = $200,000 × 0.25 = **$50,000**.
2. **ARO** = once per 10 years = **0.1**.
3. **ALE** = SLE × ARO = $50,000 × 0.1 = **$5,000 per year**.

Now the manager's point: if a flood-mitigation control costs **$2,000 a year**,
spending it to avoid $5,000 of annual expected loss is a good deal. If it cost
$9,000 a year, it would not be — you'd be spending more than the risk is worth.
**ALE turns risk into a number you can put next to a price tag.** That cost/benefit
comparison is the real reason the exam makes you learn the math.

## Inherent vs. residual risk

Two states of risk you must separate:

> **Inherent risk** is the risk *before* any controls are applied — the raw
> exposure. **Residual risk** is what *remains after* controls are in place.

You can never drive residual risk to zero; controls reduce it to a level
leadership either accepts or treats further. Keeping the two straight matters
because the business accepts *residual* risk, and the goal of treatment (next
lesson) is to pull residual risk down inside the organization's appetite.

## Recording it all: the risk register

The output of assessment isn't a feeling, it's a documented list.

> A **risk register** is the living record of identified risks — each with its
> likelihood, impact, owner, current treatment, and status.

The register is what lets a manager track risk over time, report it to the
steering committee, and prove that nothing is being quietly forgotten.

## The manager's reflex

- A risk assessment **starts by identifying and valuing assets.**
- Classification exists to **match protection to sensitivity and criticality**,
  and the **data owner** sets the level.
- When a question gives you AV, EF, and ARO, reach for **SLE = AV × EF** then
  **ALE = SLE × ARO**, and use ALE to judge whether a control is worth its cost.
- Distinguish **inherent** (before controls) from **residual** (after).

## Exam focus

- **Risk combines likelihood and impact.** Raise either and risk rises.
- The **FIRST step in a risk assessment is to identify and value information
  assets.** Everything else depends on it.
- **Asset classification's PRIMARY purpose is to set the level of protection by
  sensitivity and criticality**, and the **data owner determines the
  classification.**
- **Qualitative** = ratings/judgment (high/med/low); **quantitative** = numbers
  and money (SLE/ARO/ALE). Pick the one that fits the data and the decision.
- **SLE = Asset Value × Exposure Factor; ALE = SLE × ARO.** EF is the percentage
  of value lost in one event; ARO is events per year. ALE is the annual expected
  loss — compare it to a control's annual cost.
- **Inherent risk = before controls; residual risk = after controls.** The
  business accepts residual risk, which can never reach zero.
- The **risk register** documents each risk's likelihood, impact, owner, and
  treatment status.
