# Compliance Management & Data Classification

The final domain is about **Microsoft Purview**, Microsoft's suite for data
security, governance, risk and compliance. Before you can protect data, you have
to (1) manage your compliance obligations and (2) know what data you actually
have. This lesson covers both foundations: the **compliance management** tools
(Compliance Manager, the Service Trust Portal) and **data classification** (how
Purview discovers and categorizes sensitive information).

## Microsoft Purview, at a glance

> **Microsoft Purview** is Microsoft's integrated suite of solutions for **data
> governance, data protection, risk and compliance**. It was formerly known as
> the **Microsoft 365 compliance center**. Admins work from the **Microsoft
> Purview portal**, a single entry point for all of these capabilities.

Think of Purview as the "compliance half" of the SC-900 world, the way Entra is
the identity half and Defender is the security half.

## Compliance Manager

Meeting regulations like GDPR, HIPAA or ISO 27001 is daunting — each has hundreds
of requirements. **Compliance Manager** turns that into a managed, measurable
process.

> **Compliance Manager** helps you manage compliance requirements by providing
> **prebuilt assessments** for common standards and regulations, **recommended
> improvement actions**, and an overall **compliance score**.

How it fits together:

- **Assessments** are templates for a specific regulation (e.g. "GDPR" or "ISO
  27001") that list the controls you need.
- **Improvement actions** are the concrete things to do to satisfy those controls.
  Some are **your** responsibility; some are **Microsoft-managed** (Microsoft does
  them for its cloud).
- Each action is weighted by risk and type (preventative vs. detective, mandatory
  vs. discretionary).

### The compliance score

> The **compliance score** is a **measurement of your progress in completing
> recommended improvement actions** that reduce compliance risk. It is **not** a
> guarantee of legal compliance — it tracks how far along you are.

A new tenant even starts with an initial score based on the Microsoft data
protection baseline, so you have a baseline to improve from day one.

## The Service Trust Portal

Compliance Manager helps you manage *your* obligations. But auditors often ask for
proof about **Microsoft's** own controls. That lives in a different place.

> The **Service Trust Portal (STP)** is where customers obtain **Microsoft's
> independent audit reports, certifications and compliance documentation** — for
> example **SOC** and **ISO** reports — for its cloud services.

Remember the split: **Service Trust Portal = Microsoft's audit reports and
certifications** (proof about Microsoft's cloud). **Compliance Manager = managing
and scoring your own organization's compliance.**

## Data classification: knowing what you have

You cannot protect what you cannot find. **Data classification** is how Purview
discovers and categorizes sensitive content across your Microsoft 365 data.

> **Data classification** identifies and categorizes data that contains sensitive
> content — such as credit card, passport or social security numbers — so the
> organization knows what sensitive data it holds and where.

Purview classifies data using three mechanisms:

### Sensitive information types (SITs)

> **Sensitive information types** are built-in and custom, **pattern-based**
> definitions that detect specific kinds of sensitive data — for example a social
> security number, a bank account number or a passport number — using patterns,
> keywords and checksums.

SITs are perfect for data with a recognizable *format*. Microsoft ships hundreds,
and you can build custom ones.

### Trainable classifiers

Some content has no neat pattern — a résumé, a legal contract or source code looks
different every time.

> **Trainable classifiers** identify categories of content that are hard to define
> with simple patterns by being **trained with example documents**, using machine
> learning to recognize similar content.

Rule of thumb: **recognizable pattern → sensitive information type; "I know it
when I see it" content → trainable classifier.**

### Seeing the results: content explorer and activity explorer

Once data is classified, two tools let admins see what exists and how it is used:

- **Content explorer** shows **what** sensitive content exists and **where** it
  lives.
- **Activity explorer** shows **what is happening** to that content — the actions
  and activity around labeled or sensitive items over time.

## How classification connects to protection

Classification is the foundation for the *next* lesson. Once Purview knows a
document contains credit card numbers (via a SIT) or is a résumé (via a trainable
classifier), you can automatically apply a **sensitivity label**, enforce **data
loss prevention**, or set **retention** — all of which depend on first knowing
*what the data is*.

## The whole thing in one paragraph

**Microsoft Purview** (formerly the Microsoft 365 compliance center) is
Microsoft's data governance, protection, risk and compliance suite, run from the
**Purview portal**. **Compliance Manager** gives **prebuilt assessments**,
**improvement actions** and a **compliance score** (your progress completing
recommended actions), while the **Service Trust Portal** provides **Microsoft's**
audit reports and certifications (SOC, ISO). **Data classification** discovers and
categorizes sensitive data using **sensitive information types** (pattern-based,
like SSNs), **trainable classifiers** (ML trained on examples, like résumés), with
**content explorer** and **activity explorer** showing what exists and what is
happening to it.

## Exam focus

- **Microsoft Purview** = integrated **data governance, protection, risk &
  compliance** suite; **formerly the Microsoft 365 compliance center**.
- **Compliance Manager** = **prebuilt assessments + improvement actions +
  compliance score**. The **compliance score** measures **progress completing
  recommended actions**, not guaranteed compliance.
- **Service Trust Portal** = **Microsoft's** audit reports/certifications (SOC,
  ISO). Don't confuse it with Compliance Manager (your own compliance).
- **Data classification:** **sensitive information types** = **pattern-based**
  (SSN, credit card); **trainable classifiers** = **ML trained on examples**
  (résumés, source code).
- **Content explorer** = what/where sensitive content is; **activity explorer** =
  what is happening to it.
