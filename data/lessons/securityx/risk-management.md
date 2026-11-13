# Enterprise Risk Management

At the architect level, security exists to let the business take risk on purpose,
not to eliminate it. SecurityX expects you to think like someone who advises a
board: translate technical exposure into money and likelihood, recommend a
treatment, and know when the right answer is to *accept* a risk and move on. This
lesson builds the vocabulary and the math behind that conversation.

## Risk, in precise terms

A **risk** is the possibility that a **threat** exploits a **vulnerability** and
causes **impact**. Keep the three separate: a threat is the actor or event, a
vulnerability is the weakness, and impact is what it costs you. Risk only exists
where a threat and an exploitable vulnerability overlap on an asset that matters.

> **Inherent risk** is the exposure *before* any controls. **Residual risk** is
> what remains *after* controls are applied. **Control risk** is the chance a
> control fails to work as intended. You manage residual risk down to — not below
> — your risk appetite.

### Appetite, tolerance, and capacity

These three are tested constantly and are easy to confuse:

- **Risk appetite** — the *amount and type* of risk an organization is willing to
  pursue in pursuit of its goals. It is a strategic, board-level statement (e.g.,
  "we accept moderate risk to move to a cloud-first model quickly").
- **Risk tolerance** — the *acceptable variation* around a specific objective; how
  far from appetite you will drift before acting. Tolerance is narrower and more
  operational than appetite.
- **Risk capacity** — the *maximum* risk the organization could absorb and still
  survive. Appetite should never exceed capacity.

Appetite itself comes in flavors the exam names: **expansionary/aggressive**
(willing to take on more risk for growth), **neutral**, and **conservative/averse**.

## Quantitative risk: putting a number on it

Quantitative analysis assigns dollar values so controls can be justified against
their cost. Learn these formulas cold — they are near-guaranteed items.

| Term | Meaning | Formula |
|------|---------|---------|
| **AV** | Asset Value | the asset's worth |
| **EF** | Exposure Factor | % of the asset lost in one event |
| **SLE** | Single Loss Expectancy | `AV x EF` |
| **ARO** | Annualized Rate of Occurrence | expected events per year |
| **ALE** | Annualized Loss Expectancy | `SLE x ARO` |

Worked example: a data center worth **$2,000,000**; a flood destroys **25%** of
value (EF = 0.25) and is expected **once every 20 years** (ARO = 0.05).
`SLE = 2,000,000 x 0.25 = $500,000`. `ALE = 500,000 x 0.05 = $25,000` per year.

> The business case for a control is **ALE before control − ALE after control −
> annual cost of the control**. If a $10,000/yr control cuts ALE from $25,000 to
> $5,000, it saves `25,000 − 5,000 − 10,000 = $10,000` a year and is justified.

Quantitative analysis is objective and great for cost-justifying spend, but it is
data-hungry and the numbers are only as good as the estimates feeding them.

## Qualitative risk: ranking without dollars

**Qualitative** analysis rates risks on ordinal scales — *likelihood* against
*impact*, often plotted on a **risk heat map / matrix** (Low/Medium/High or 1–5).
It is fast, works when hard loss data is unavailable, and captures reputational and
safety harms that resist pricing. The trade-off is subjectivity. Mature programs
run both: qualitative to triage the whole register, quantitative to drill into the
items that rise to the top. A **semi-quantitative** approach puts numeric bands on
qualitative ratings as a bridge.

## Treating risk: the four strategies

Once a risk is understood, leadership chooses a treatment. Expect scenario items
that hand you a situation and ask which strategy it describes.

- **Mitigate (reduce)** — apply controls to lower likelihood or impact. The
  default for most risks (patching, segmentation, MFA).
- **Transfer (share)** — shift financial impact to a third party. **Cyber
  insurance** is the classic transfer; so is outsourcing a risky function. Note:
  you transfer *financial* loss, not accountability — reputational and legal
  responsibility usually stay with you.
- **Avoid** — stop the activity that creates the risk entirely (e.g., decline to
  launch a feature, exit a market).
- **Accept** — knowingly take the risk, with a documented, signed **risk
  acceptance**. Appropriate when residual risk is already within appetite or the
  cost of control exceeds the benefit. **Risk exception** and a time-boxed
  **exemption** are formal, approved deviations recorded the same way.

> Accepting risk is a legitimate, common decision — but only when it is *explicit*,
> *documented*, and *approved by the risk owner*. An undocumented acceptance is
> negligence, not a strategy.

## The register and the people

The **risk register** is the living inventory: each entry has a description,
category, inherent and residual scoring, a treatment, a **risk owner**, and a
status. Supporting metrics include **KRIs** (Key Risk Indicators — leading signals
that exposure is rising) versus **KPIs** (which measure performance). Two clocks
matter for surfacing risk: the **SLE/ALE** economics above and, operationally,
how quickly new exposure enters the register.

Accountability is specific. The **risk owner** accepts and manages a given risk;
**senior leadership and the board** own the enterprise risk posture and set
appetite. A **control owner** runs a particular safeguard. Confusing "who runs the
firewall" with "who accepts the risk" is a classic distractor.

## Risk during change: assessments and M&A

Risk is not a once-a-year exercise. A **continuous** program re-scores as the
environment shifts; an **ad hoc** assessment fires on a trigger. Specific triggers
you should recognize:

- **Mergers and acquisitions (M&A)** — acquiring a company means inheriting its
  breaches, technical debt, and liabilities. **Due diligence** before the deal and
  deep **integration** risk assessment after it are both essential; a target's
  unknown compromise becomes *your* incident on day one.
- **Divestiture** — splitting off a unit raises data-separation and residual-access
  risk.
- **New regulation, new technology, or a major incident** — each warrants a fresh
  assessment.

## Exam focus

- Know the formulas cold: **SLE = AV x EF**, **ALE = SLE x ARO**. Be ready to
  compute ALE and to justify a control by comparing ALE reduction to control cost.
- **Residual risk** = exposure remaining after controls; you drive it down to your
  **risk appetite**, not to zero.
- Distinguish **appetite** (strategic willingness), **tolerance** (acceptable
  variance around an objective), and **capacity** (the max you could survive).
- The four treatments: **mitigate, transfer, avoid, accept**. **Cyber insurance =
  transfer**; declining the activity = **avoid**; a signed sign-off = **accept**.
  Transfer moves financial loss, not accountability.
- **Qualitative** = likelihood x impact on an ordinal matrix (fast, subjective);
  **quantitative** = dollar values (objective, data-hungry). Mature programs use
  both.
- A **risk acceptance/exception** must be documented and approved by the **risk
  owner**; the **board/senior leadership** sets appetite and owns enterprise risk.
- **M&A** inherits the target's risk — do **due-diligence** assessment before and
  **integration** assessment after.
