# Insider Risk, eDiscovery & Privacy

Not every threat comes from outside, and not every compliance task is about
hardening data. This final lesson covers the Microsoft Purview solutions for
**risks and investigations** — insider risk, communication compliance, eDiscovery
and audit — and then **Microsoft Priva**, the dedicated tool for managing
**privacy**. These answer the questions "what are our own people doing?" and "how
do we respect individuals' personal data?"

## Insider Risk Management

Most security tools watch for outside attackers. But a departing employee copying
customer lists, or a careless user mishandling sensitive files, is a threat from
*inside*.

> **Insider Risk Management** helps detect, investigate and act on **risky
> activities by internal users** — such as potential data theft by a departing
> employee or accidental oversharing — by analyzing signals across Microsoft 365.

A thoughtful detail the exam likes: because investigating your own employees is
sensitive, Insider Risk Management uses **pseudonymization** by default — it
replaces user names with anonymized identifiers during analysis to help protect
privacy, revealing identities only when an investigation justifies it.

## Communication Compliance

Related but different, this one watches **what people say**, not what they take.

> **Communication Compliance** detects **inappropriate or non-compliant
> messages** — such as harassment, offensive language, sharing of sensitive
> information, or regulatory violations — within corporate communications like
> email and Microsoft Teams chats.

It helps organizations meet conduct and regulatory obligations by flagging risky
communications for reviewers. (Don't confuse it with DLP: DLP stops sensitive
*data* from leaking; Communication Compliance flags inappropriate *conduct* in
messages.)

## eDiscovery

When there is a lawsuit or investigation, legal teams must find and preserve all
relevant electronic content. That process is **electronic discovery**, or
**eDiscovery**.

> **eDiscovery** lets you **identify, place holds on, collect, review and export**
> electronic content across Microsoft 365 that is relevant to a legal case.

Microsoft offers tiers:

- **eDiscovery (Standard)** — core search, legal hold and export.
- **eDiscovery (Premium)** — advanced workflows for complex litigation, including
  **custodian management**, **legal hold notifications**, and **review sets** for
  analyzing large volumes of content beyond basic search and export.

The giveaway: if a scenario mentions **custodians, legal hold notifications or
review sets**, it is **eDiscovery (Premium)**.

## Audit

Investigations also need a record of **who did what**. Purview's **Audit**
solution logs user and admin activities across Microsoft 365:

- **Audit (Standard)** — captures and lets you search audit logs of activities.
- **Audit (Premium)** — longer retention and higher-value events for deeper
  forensic investigations.

Audit provides the evidence trail that insider risk cases and eDiscovery rely on.

## Microsoft Priva: managing privacy

Everything above is about compliance and investigations. **Privacy** is a
distinct discipline — respecting individuals' rights over their personal data — and
Microsoft gives it a dedicated product.

> **Microsoft Priva** helps organizations manage **privacy risks** — such as data
> overexposure and oversharing of personal data — and **automate privacy
> operations**. It is distinct from Purview's broader compliance tooling, focusing
> specifically on **personal data and privacy**.

Priva's two capabilities for SC-900:

### Privacy Risk Management

> **Privacy Risk Management** gives visibility into the **personal data** your
> organization stores and detects privacy risks — such as data **transfers** and
> **overexposure** — then offers policies to help mitigate them.

### Subject Rights Requests

Privacy laws like **GDPR** give individuals the right to ask an organization for a
copy of, or the deletion of, the personal data held about them (a "data subject
request").

> **Subject Rights Requests** help organizations **manage and fulfill** these
> requests at scale — finding the relevant personal data, reviewing it, and
> producing or deleting it — with automation and workflows instead of a manual
> scramble.

### Priva vs. Purview

Keep the relationship clear: **Microsoft Priva focuses specifically on privacy
risk management and subject rights requests for personal data**, while **Microsoft
Purview** covers the broader set of data governance, protection, risk and
compliance solutions. Priva is the privacy specialist within the larger family.

## The whole thing in one paragraph

Purview's risk and investigation solutions include **Insider Risk Management**
(detect risky activity by **internal** users, with **pseudonymization** to protect
privacy), **Communication Compliance** (flag inappropriate messages like
harassment), **eDiscovery** (identify, hold, collect, review and export content
for legal cases — **Premium** adds custodians, hold notifications and review
sets), and **Audit** (log who did what). Separately, **Microsoft Priva** manages
**privacy**, with **Privacy Risk Management** (visibility into personal data and
risks like overexposure) and **Subject Rights Requests** (fulfilling GDPR-style
requests to access or delete personal data) — the privacy specialist alongside the
broader Purview compliance suite.

## Exam focus

- **Insider Risk Management** = risky activity by **internal** users (e.g.
  departing-employee data theft); uses **pseudonymization** to protect user
  privacy during investigation.
- **Communication Compliance** = detect **inappropriate/non-compliant messages**
  (harassment, sensitive-info sharing) in email/Teams — about **conduct**, not
  data leakage.
- **eDiscovery** = identify, **hold**, collect, review, export content for legal
  cases. **Premium** = **custodians, legal hold notifications, review sets**.
  **Audit** logs user/admin activity.
- **Microsoft Priva** = **privacy** specialist: **Privacy Risk Management**
  (overexposure/oversharing of personal data) + **Subject Rights Requests**
  (GDPR-style access/delete requests).
- **Priva = privacy-specific; Purview = broader compliance.** Keep the scopes
  straight.
