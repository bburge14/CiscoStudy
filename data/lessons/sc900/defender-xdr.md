# Microsoft Defender XDR

A sophisticated attack rarely stays in one place. It might arrive as a phishing
email, trick a user into running malware on their laptop, steal their identity,
then reach into cloud apps. If each of those signals sits in a separate tool, no
one sees the whole story. **Microsoft Defender XDR** stitches them together. This
lesson explains what XDR is, the Defender services that feed it, and the portal
where it all comes together.

## What XDR means, and what Defender XDR does

**XDR** stands for **Extended Detection and Response**. Where a single tool
detects threats in one domain, XDR **correlates signals across many domains** into
one picture.

> **Microsoft Defender XDR** (formerly Microsoft 365 Defender) is a unified
> pre- and post-breach enterprise defense suite. It **correlates signals across
> endpoints, email and collaboration, identities, and cloud apps** to detect,
> investigate and automatically respond to attacks across the kill chain.

The payoff of correlation:

> Because Defender XDR links related alerts from different domains into a **single
> incident**, an analyst sees the **end-to-end story of an attack** — the email,
> the device, the identity, the cloud app — instead of four disconnected alerts
> they must piece together by hand.

Defender XDR can also respond automatically — for example, **automated
investigation and response (AIR)** can isolate a compromised device or contain an
attack without waiting for a human.

## The core Defender services

Defender XDR is fed by a family of specialized services, each guarding one domain.
Match each to **what it protects**:

| Service | Protects |
|---------|----------|
| **Microsoft Defender for Office 365** | Email and collaboration (Teams, SharePoint, OneDrive) |
| **Microsoft Defender for Endpoint** | Devices / endpoints (laptops, servers, mobile) |
| **Microsoft Defender for Identity** | On-premises Active Directory identities |
| **Microsoft Defender for Cloud Apps** | SaaS / cloud applications |

### Microsoft Defender for Office 365

Protects against threats that arrive by **email and collaboration tools** —
phishing, malicious links and attachments. Two signature features:

> **Safe Attachments** opens email attachments in a protected **sandbox** to
> detonate and detect malware before they reach the user. **Safe Links** rewrites
> and **checks URLs at the moment the user clicks**, blocking malicious links even
> if they were safe when the mail was sent.

### Microsoft Defender for Endpoint

An **endpoint detection and response (EDR)** platform for devices. It provides
threat and vulnerability management, attack-surface reduction, next-gen antivirus,
EDR, and automated investigation — protecting laptops, servers and mobile devices.

### Microsoft Defender for Identity

Uses signals from your **on-premises Active Directory** to detect identity-based
attacks — compromised accounts, lateral movement, and techniques like
pass-the-hash. It focuses on the on-prem identity layer (complementing Entra ID
Protection, which watches cloud identities).

### Microsoft Defender for Cloud Apps

A **cloud access security broker (CASB)**. It gives visibility into which **SaaS
apps** your organization uses (including unsanctioned "shadow IT"), and controls
how data moves through them.

(You may also see **Microsoft Defender Vulnerability Management**, which discovers
and prioritizes vulnerabilities across assets, and **Microsoft Defender for
Cloud**, from the previous lesson, surfaced alongside these in the suite.)

## The Microsoft Defender portal

All of this needs one place to work from.

> The **Microsoft Defender portal** is the single, unified console where Defender
> XDR **incidents, alerts, and investigations** are accessed and managed across
> all the Defender services (and increasingly Microsoft Sentinel too).

Instead of hopping between tools, an analyst triages one correlated incident
queue, pivots across domains, and runs response actions from one portal.

## Microsoft Secure Score (and a name clash to avoid)

Defender XDR includes its own posture measurement.

> **Microsoft Secure Score** measures an organization's security posture across
> its **Microsoft 365** identities, devices and apps, and recommends actions to
> improve it. A higher score reflects a stronger posture.

Watch the exam trap: this **Microsoft Secure Score** (for Microsoft 365, in the
Defender portal) is **distinct from the secure score in Microsoft Defender for
Cloud**, which measures your **Azure / multicloud resource** posture. Same idea,
two different scores for two different scopes — know which one a question is asking
about.

## The whole thing in one paragraph

**Microsoft Defender XDR** (formerly Microsoft 365 Defender) correlates signals
across **endpoints, email/collaboration, identities and cloud apps** into a single
**incident** so analysts see the whole attack. It is fed by **Defender for Office
365** (email — **Safe Attachments** and **Safe Links**), **Defender for Endpoint**
(devices/EDR), **Defender for Identity** (on-prem AD identity attacks) and
**Defender for Cloud Apps** (SaaS/CASB). Everything is managed in the **Microsoft
Defender portal**, and **Microsoft Secure Score** rates your Microsoft 365 posture
— not to be confused with Defender for Cloud's Azure secure score.

## Exam focus

- **Microsoft Defender XDR** = **formerly Microsoft 365 Defender**; it
  **correlates signals across domains into one incident** telling the end-to-end
  attack story.
- Map the services: **Office 365 → email/collaboration**, **Endpoint → devices**,
  **Identity → on-premises AD identities**, **Cloud Apps → SaaS (CASB)**.
- **Safe Attachments** (sandbox/detonate attachments) and **Safe Links**
  (check URLs at click time) belong to **Defender for Office 365**.
- Everything is accessed in the **Microsoft Defender portal** (also the emerging
  home of Sentinel).
- **Microsoft Secure Score** = **Microsoft 365** posture; it is **different from**
  the **Defender for Cloud secure score** (Azure/multicloud). Don't mix them up.
