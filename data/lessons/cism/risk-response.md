# Risk Response & Ongoing Risk Monitoring

You've found the risk and measured it. Now comes the decision the whole exercise
was for: *what do we do about it?* This lesson covers the four ways an
organization can respond to risk, who gets to make the call, and why the job is
never finished — risk has to be watched continuously because the world keeps
changing. Throughout, keep the manager's lens: your role is to present options
and residual risk to the business, not to unilaterally decide for it.

## The four risk response options

Once a risk is understood, leadership chooses a **treatment** (also called a risk
response). There are exactly four, and the exam expects you to match a scenario
to the right one instantly.

> - **Mitigate (reduce)** — apply controls to lower the likelihood or impact.
> - **Transfer (share)** — shift the financial consequence to a third party,
>   e.g. buy insurance or outsource.
> - **Avoid** — eliminate the risk by not doing the risky activity at all.
> - **Accept** — knowingly take the risk, usually when it's already within
>   appetite or treatment would cost more than the risk is worth.

Match the clues:

| Scenario | Response |
|----------|----------|
| Deploy MFA to cut account-takeover risk | **Mitigate** |
| Buy cyber-insurance to offset breach losses | **Transfer (share)** |
| Cancel a new online service whose risk can't be cost-effectively reduced | **Avoid** |
| Decide a small, well-understood risk isn't worth spending on | **Accept** |

Two of these trip people up most:

- **Transfer** does **not** make the risk disappear — it moves the *financial*
  burden. Cyber-insurance pays out after a breach, but you still suffered the
  breach, and reputational harm often stays with you. Outsourcing is similar: you
  transfer operation, but accountability remains yours.
- **Avoidance** is the drastic one: you **don't do the activity.** When a project
  carries unacceptable risk that cannot be reduced cost-effectively and the
  organization cancels it, that is avoidance — not acceptance, not mitigation.

A gut check the exam rewards: a control that *lowers* risk is mitigation; a
decision to *not act at all* is avoidance; paying someone else to carry the loss
is transfer; and living with it on purpose is acceptance.

## Appetite and tolerance: the guardrails for the decision

How do you know whether a residual risk is acceptable? Leadership tells you, in
advance, through two related concepts.

> **Risk appetite** is the broad amount of risk an organization is *willing to
> pursue* in service of its objectives. **Risk tolerance** is the acceptable
> *variation* around that — how far a specific risk may stray before it demands
> action.

Appetite is the strategic setting; tolerance is the operational band around it.
A bank might have a low appetite for fraud risk overall, with a narrow tolerance
on any single high-value account. These guardrails are set by the **board/senior
management** (governance) and give the manager an objective test: if residual
risk sits inside appetite, acceptance is reasonable; if it exceeds appetite, the
risk must be treated further.

## Who accepts risk — and how

This is a favorite CISM trap. The security manager analyzes and recommends, but
does **not** own or accept the risk.

> Risk is accepted by the **risk owner — the business owner / senior manager**
> whose function bears the consequence. Acceptance must be a **formal, documented,
> informed decision**, and it should only cover risk **within the organization's
> appetite.**

Several nuances the exam probes:

- Acceptance is **not** "ignoring" a risk. Ignoring is negligence; acceptance is
  a conscious, recorded choice by an accountable owner.
- The **security manager's job** is to make sure the owner understands the
  residual risk before signing — then document it. The decision belongs to the
  business.
- Risk that **exceeds appetite should not simply be accepted.** It is escalated
  for treatment or for an explicit, exceptional decision at a higher level.

Tie this back to roles: the data/business owner who classified the asset is the
same party who accepts its residual risk. Ownership of the asset and ownership of
its risk travel together.

## Cost-benefit: don't spend more than the risk is worth

A control should cost **less** than the loss it prevents. This is where last
lesson's ALE pays off.

> A proposed control is worth implementing when its **annual cost is lower than
> the reduction in Annualized Loss Expectancy (ALE)** it delivers. Spending
> $20,000 a year to avoid $5,000 of annual expected loss is poor management — you
> would be over-protecting.

Over-control wastes money and can smother the business; under-control leaves
unacceptable exposure. The manager finds the balance, and *value delivery* — the
governance outcome — is exactly this discipline applied to controls.

## Risk monitoring: the job is never done

Here's the mistake that sinks programs: treating risk assessment as a one-time
project. A risk register written last year describes a world that no longer
exists.

> Risk must be **monitored on an ongoing basis** because the **threat landscape
> and the business environment change over time**, which changes risk levels. New
> threats emerge, systems change, the business enters new markets — yesterday's
> acceptable risk can become today's crisis.

Continuous monitoring keeps the risk register truthful, confirms that controls
still work, and catches risks drifting toward or past the appetite line.

### Key risk indicators (KRIs)

How do you get an *early warning* that risk is rising before it turns into an
incident? You track **KRIs**.

> A **Key Risk Indicator (KRI)** is a metric that gives an **early-warning
> signal that risk exposure is increasing** toward or beyond acceptable levels —
> a leading indicator, not a lagging report of damage already done.

Examples: a climbing number of overdue critical patches, a rising count of failed
logins, or growing use of unsanctioned "shadow IT." A good KRI is tied to a
threshold that, when crossed, triggers management review. Don't confuse a KRI
(forward-looking, about *risk*) with a KPI (about process *performance*) — we'll
sharpen that distinction in the program-metrics lesson. Here, remember: **KRI =
early warning of rising risk.**

## The manager's reflex

- Match the scenario to one of four responses: **mitigate, transfer, avoid,
  accept** — and remember transfer keeps the risk, avoidance means don't do it.
- The **business/risk owner accepts** risk, **formally and only within
  appetite**; the manager informs and documents.
- Justify controls with **cost < benefit (ALE reduction).**
- Risk work is **continuous**; use **KRIs** to see trouble coming.

## Exam focus

- The four risk responses: **mitigate (reduce), transfer/share (insurance,
  outsourcing), avoid (don't do the activity), accept (knowingly live with it).**
- **Cyber-insurance = transfer.** **Cancelling a too-risky project = avoidance.**
  Transfer and avoidance are the most-confused pair — transfer still leaves you
  with the risk's non-financial fallout.
- **Risk appetite** = willingness to take risk overall; **risk tolerance** =
  acceptable variation around it. Both are set by **senior management/board.**
- The **risk owner (business/senior manager) accepts residual risk** through a
  **formal, documented, informed** decision, and **only within appetite.** The
  security manager recommends; it does not accept risk.
- A control is justified when its **cost is less than the ALE reduction** it
  provides — avoid over-control and under-control alike.
- **Monitor risk continuously** because the threat and business environment
  change. A **KRI is an early-warning, leading indicator of rising risk.**
