# Risk Management

Security is never about eliminating all danger — that's impossible and would cost
infinitely. It's about understanding **risk** and making sensible decisions about
it. This lesson teaches the vocabulary of risk and the four ways an organization
can respond to it. These terms are precise, and the exam loves to test whether you
can tell them apart.

## The building blocks: asset, threat, vulnerability

Three terms sit underneath everything else. Learn them cold.

> An **asset** is anything of value worth protecting. A **threat** is anything
> that could cause harm. A **vulnerability** is a weakness a threat could exploit.

- **Asset** — anything of value to the organization: data, hardware, software,
  facilities, and even people. If losing it would hurt, it's an asset.
- **Threat** — any circumstance or event with the potential to cause harm. A
  hacker, a piece of malware, a disgruntled employee, a flood, or a power outage
  are all threats. The person or thing behind a threat is the **threat actor**
  (or threat agent).
- **Vulnerability** — a weakness or gap in a system, process, or control that a
  threat could take advantage of. A missing security patch, a weak password, or
  an unlocked door are classic vulnerabilities.

A helpful sentence to hold them together: *a threat exploits a vulnerability to
harm an asset.* The burglar (threat) uses the unlocked window (vulnerability) to
steal the jewelry (asset).

## What "risk" actually means

> **Risk** is the potential for loss or harm when a threat exploits a
> vulnerability. It is judged by two things: how **likely** the event is, and how
> big the **impact** would be if it happened.

So risk is not the same as a threat or a vulnerability — it's the *combination*,
weighed by probability and consequence:

- **Likelihood** — the probability that a given threat will actually exploit a
  vulnerability in some period of time.
- **Impact** — the magnitude of the harm if it does happen, measured in money,
  downtime, reputation, safety, or legal consequence.

A threat with no matching vulnerability poses little risk; a serious
vulnerability that no threat is interested in poses little risk. You need both,
and then you weigh likelihood against impact. A flood is high-impact but may be
low-likelihood in a desert; a phishing email is lower-impact per message but very
high-likelihood.

### Inherent vs. residual risk

- **Inherent risk** is the risk that exists *before* you apply any controls — the
  raw exposure.
- **Residual risk** is the risk that *remains after* controls have been applied.
  No control is perfect, so some residual risk almost always survives.

Management's job is to decide whether the **residual risk** is low enough to live
with. That decision connects directly to the four responses below.

## The four ways to treat a risk

Once a risk is identified and assessed, the organization chooses how to respond.
There are four standard options — memorize all four and a one-line example of
each.

| Response | What it means | Example |
|----------|---------------|---------|
| **Avoidance** | Eliminate the risk by not doing the risky activity at all | Cancelling a new online feature because it's too risky |
| **Mitigation** (reduction) | Apply controls to lower the likelihood and/or impact | Patching flaws and adding a web application firewall |
| **Transference** | Shift the impact to a third party | Buying cyber-insurance to cover losses from an attack |
| **Acceptance** | Make an informed decision to take no further action and bear the risk | Deciding a small risk isn't worth an expensive control |

Watch the distinctions carefully, because the exam leans on them:

- **Avoidance** removes the activity entirely — you don't launch the feature,
  period. It's the only option that drops the risk to zero, but it may cost you
  the business opportunity.
- **Mitigation** keeps the activity but adds safeguards to shrink the risk. This
  is the most common response and is where most security spending goes.
- **Transference** does not make the bad thing less likely — insurance doesn't
  stop the ransomware — it just moves the *financial* consequence onto someone
  else. Outsourcing to a provider can also transfer some risk.
- **Acceptance** is a deliberate, documented choice to absorb the risk, usually
  because the cost of any control is greater than the expected loss. Quietly
  ignoring a risk is *not* acceptance; acceptance is an informed management
  decision.

> Insurance is the signature example of **transference**; cancelling the project
> is the signature example of **avoidance**. If a scenario adds a firewall or
> patches a flaw, that's **mitigation**. If management knowingly does nothing,
> that's **acceptance**.

## Risk appetite and tolerance

Organizations differ in how much risk they're willing to take on. **Risk
appetite** is the amount of risk an organization is willing to pursue in order to
meet its goals; **risk tolerance** is how much variation from that it will accept
in practice. A startup chasing growth may have a larger appetite than a hospital
guarding patient safety. These terms explain *why* two organizations facing the
same risk might reasonably choose different responses.

## The basic flow

Risk management is an ongoing cycle, not a one-time task:

1. **Identify** assets, threats, and vulnerabilities.
2. **Assess** each risk by estimating likelihood and impact.
3. **Treat** the risk by choosing avoidance, mitigation, transference, or
   acceptance.
4. **Monitor** continuously, because assets, threats, and vulnerabilities all
   change over time.

## Exam focus

- **Asset** = anything of value; **threat** = anything that could cause harm;
  **vulnerability** = a weakness a threat can exploit. Don't confuse them.
- **Risk** = potential for loss when a threat meets a vulnerability, judged by
  **likelihood** (probability) and **impact** (severity).
- Memorize the four risk responses: **avoidance** (stop the activity),
  **mitigation** (add controls), **transference** (insurance / shift to a third
  party), **acceptance** (knowingly bear it).
- **Transference ≠ reducing the risk** — it moves the financial impact, it
  doesn't make the event less likely.
- **Residual risk** is what remains *after* controls are applied; management
  decides whether it's acceptable.
- Acceptance must be an *informed, deliberate* decision — not neglect.
