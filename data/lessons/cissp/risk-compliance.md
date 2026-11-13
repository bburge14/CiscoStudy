# Risk Management, Legal & Compliance

Risk management is the spine of CISSP. Almost every "what should the organization
do FIRST / BEST" question is really asking you to behave like a risk manager:
identify what matters, decide how much risk is tolerable, and spend finite money
where it reduces the most risk. This lesson gives you the vocabulary, the two ways
to measure risk, the four ways to treat it, and the external legal landscape that
sets the floor you must clear.

## The vocabulary of risk

Get these terms exact — exam distractors swap them deliberately.

> A **threat** is a potential cause of harm (a hurricane, a hacker). A
> **vulnerability** is a weakness that the threat could exploit (an unpatched
> server). **Risk** is the *likelihood* that a threat exploits a vulnerability and
> the *impact* if it does. An **exposure** is an instance of being susceptible.

A threat with no matching vulnerability carries little risk, and a vulnerability
with no threat is largely academic. Risk lives at the intersection, so
**Risk ≈ Likelihood × Impact.** A **threat agent** or **threat actor** is the
entity that carries out the threat.

## Quantitative risk analysis

When data allows, express risk in money. Memorize this chain:

| Term | Meaning | Formula |
|------|---------|---------|
| **AV** | Asset Value | (given) |
| **EF** | Exposure Factor — % of asset lost in one event | (given, 0–100%) |
| **SLE** | Single Loss Expectancy | **AV × EF** |
| **ARO** | Annualized Rate of Occurrence — events per year | (given) |
| **ALE** | Annualized Loss Expectancy | **SLE × ARO** |

The decision rule for whether a safeguard is worth buying:

> **Safeguard value = (ALE _before_ − ALE _after_) − annual cost of the safeguard.**
> A positive result means the control is cost-justified; a negative one means you
> are spending more than you save.

Example: ALE is \$90,000. A control drops it to \$20,000 and costs \$40,000/year.
Benefit = (90,000 − 20,000) − 40,000 = **\$30,000 net**, so it is justified. If
that same control cost \$80,000/year, its value would be −\$10,000 and you would
*not* buy it on pure cost grounds. The exam expects you to run this arithmetic.

## Qualitative risk analysis

Many risks resist dollar figures (reputation, morale, safety). **Qualitative**
analysis rates likelihood and impact on scales — high/medium/low or 1–5 — and
plots them on a **risk matrix**. It is faster and more subjective. The **Delphi
technique** is the method to know: anonymous expert input gathered over rounds so
that loud voices and politics don't dominate the estimate. Most real programs use
a **hybrid**: qualitative triage first, quantitative depth where the stakes and
data justify it.

## Treating risk: the four responses

Once risk is understood, management chooses a response.

- **Mitigate (reduce)** — apply controls to lower likelihood or impact (deploy MFA,
  harden baselines, add IPS). The most common response.
- **Transfer (share)** — shift the financial impact to a third party, chiefly
  through **insurance** or by outsourcing the risky activity. Transfer moves the
  cost of harm, not the accountability.
- **Avoid** — stop doing the risky activity entirely (don't launch the feature).
- **Accept** — knowingly absorb the risk because treating it costs more than the
  risk itself.

> After controls are applied, what's left is **residual risk**. **Inherent risk**
> is the risk before any controls. The gap between residual risk and what the
> organization will tolerate is governed by its **risk appetite / tolerance** — and
> remember, **senior management must formally accept residual risk.**

Frameworks give this discipline structure: the **NIST Risk Management Framework
(SP 800-37)**, **ISO/IEC 27005**, and **FAIR** (a quantitative model) are the
names to recognize. You don't configure them; you know what they're for.

## The external landscape: laws and regulations

Some rules come from outside and carry legal force, often setting the minimum an
organization must meet. Match the data type to the law — that's the exam pattern.

| Driver | Governs | Nature |
|--------|---------|--------|
| **HIPAA** | U.S. protected health information (PHI/ePHI) — the Security Rule mandates administrative, physical, technical safeguards | Federal law |
| **GDPR** | Personal data of people in the EU | Regulation |
| **PCI DSS** | Payment card data | **Contractual** (not a law) |
| **SOX** | Accuracy of U.S. public-company financial reporting | Federal law |
| **GLBA** | U.S. financial institutions' customer data | Federal law |

**GDPR** is heavily tested and worth exact numbers. It has applied since **25 May
2018**. A controller must notify the supervisory authority of a qualifying
personal-data breach **without undue delay and, where feasible, within 72 hours**
of becoming aware (Article 33), and must tell affected individuals when the risk
to them is high (Article 34). Fines run in two tiers — up to **€10 million or 2%**
of global annual turnover for the lower tier and up to **€20 million or 4%** for
the most serious violations, whichever is greater. For transatlantic transfers,
the **EU–US Data Privacy Framework** (adequacy decision of July 2023) replaced the
invalidated Privacy Shield and, as of a September 2025 EU court ruling, remains in
force.

**PCI DSS** is a frequent trap: it is a **contractual** obligation enforced by the
card brands, not a government law. The current version is **v4.0.1** (published
June 2024); v3.2.1 was retired in 2024.

## Legal categories, intellectual property, and privacy

- **Law types:** **criminal** (offenses against society, punishable by fines or
  prison), **civil/tort** (disputes between parties, damages), **regulatory /
  administrative** (agency rules).
- **Intellectual property:** **patents** protect inventions (time-limited),
  **trademarks** protect brands and logos, **copyrights** protect expression
  (code, writing), and **trade secrets** protect confidential business value (the
  recipe) only for as long as they stay secret.
- **Privacy:** the right of individuals to control collection and use of their
  personal information. **PII** identifies a person; **PHI** is health
  information. Privacy law often constrains cross-border data transfer, which is
  why mechanisms like the Data Privacy Framework and standard contractual clauses
  matter.

## Exam focus

- **Threat × vulnerability = risk**, scaled by **likelihood and impact**. A threat
  with no matching vulnerability is low risk.
- Quantitative chain: **SLE = AV × EF**, **ALE = SLE × ARO**, and
  **safeguard value = (ALE_before − ALE_after) − annual cost**. Positive value =
  cost-justified. Be ready to compute it.
- **Qualitative** = subjective ratings and matrices; the **Delphi technique** =
  anonymous expert consensus.
- Four risk responses: **mitigate, transfer (insurance/outsourcing), avoid,
  accept**. What remains is **residual risk**, which **senior management must
  formally accept**.
- Match the law to the data: **HIPAA** = U.S. health, **GDPR** = EU personal data,
  **PCI DSS** = payment cards (**contractual, v4.0.1**), **SOX** = financial
  reporting, **GLBA** = financial customer data.
- **GDPR**: notify the supervisory authority **within 72 hours** (Art. 33); max
  fine **€20M or 4%** of global turnover. EU–US transfers run under the **Data
  Privacy Framework**.
- Know the IP four: **patent** (invention), **trademark** (brand), **copyright**
  (expression), **trade secret** (confidential, protected only while secret).
