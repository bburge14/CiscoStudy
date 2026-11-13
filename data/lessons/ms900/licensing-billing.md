# Licensing & Billing

Microsoft 365 is sold by subscription, and this lesson is about the commercial
mechanics: the **plans** an organization can buy, how **licenses** are assigned to
people, and how the whole thing is **paid for and managed**. The exam expects you
to match an organization's profile to the right plan and to know where billing
tasks happen.

## Licensing basics: the user subscription license

Microsoft 365 is licensed **per user**, not per device (for the mainstream plans).

> A **user subscription license** is assigned to an individual and grants that
> person access to the services in their plan. Buying a subscription gives you a
> pool of licenses; a user doesn't actually get email or Teams until a license is
> **assigned** to their account.

This is a point the exam tests directly: a new employee's account can exist in
**Microsoft Entra ID** yet still be unable to use Exchange Online or Teams — because
no license has been **assigned** to them yet.

## The plan families

Microsoft groups plans into families aimed at different organizations. You don't
need to memorize prices, but you must recognize who each is for.

### Microsoft 365 Business (small and medium businesses, up to 300 users)

| Plan | What it adds |
|------|--------------|
| **Business Basic** | Cloud services (Exchange, Teams, OneDrive, SharePoint) + **web and mobile** Office apps — **no installed desktop apps** |
| **Business Standard** | Everything in Basic **plus the installed desktop** Office apps |
| **Business Premium** | Everything in Standard **plus advanced security and device management** (Microsoft Entra ID P1, Intune, Defender for Business) |

### Microsoft 365 Enterprise (large organizations, no user cap)

- **E3** — the full desktop apps and core services at enterprise scale.
- **E5** — the **most comprehensive** plan: everything in E3 **plus advanced
  security** (Microsoft Defender), **advanced compliance** (Microsoft Purview),
  **Teams Phone**, **Power BI Pro**, and audio conferencing.

### Microsoft 365 Frontline (F-series)

- **F1 / F3** — built for **frontline, shift-based workers** who often **share
  devices**, don't sit at a desk, and mainly need **web and mobile** apps at a lower
  cost per user.

There are also **Microsoft 365 Apps** plans (just the apps, no broader services) and
sector-specific families — **Education** (A1/A3/A5), **Government** (G-series), and
**Nonprofit**.

### Matching a scenario to a plan

- "Full **installed desktop** apps + cloud services, about 120 people" →
  **Business Standard**.
- "Cloud email, Teams, OneDrive, and **web/mobile** apps only — **no installed**
  Office" → **Business Basic**.
- "Shift-based **frontline** workers sharing devices, mostly web/mobile" →
  **Microsoft 365 F3**.
- "The **most comprehensive** plan with **advanced security and compliance**" →
  **Microsoft 365 E5**.

## Add-ons

On top of a base plan you can buy **add-ons** — extra capabilities licensed
separately and assigned per user. The headline one is the **Microsoft 365 Copilot**
add-on (requires a qualifying base plan), but add-ons also include **Teams Phone**,
**Visio**, **Project**, and extra storage. The pattern: a base plan plus optional
add-ons tailored to who needs what.

## Billing and cost management

Once you've chosen plans, you manage the commercial side centrally.

> The **Microsoft 365 admin center** is the one place to **buy and assign
> licenses, add users, manage subscriptions, and view invoices**. It's the hub for
> both administration and billing.

### Who can manage billing

You don't have to be an all-powerful admin to handle money:

- The **Billing Administrator** role lets a finance staffer **manage purchases,
  subscriptions, and invoices** **without** granting the broad power of a **Global
  Administrator**. This follows least privilege — give finance exactly the access
  they need.

### How you pay: monthly vs. annual

Microsoft offers different commitment terms, and the trade-off is a classic exam
point:

- **Annual commitment** — commit for a year; typically a **lower per-user rate**.
- **Month-to-month** — maximum flexibility to add or drop licenses and cancel, at a
  **higher per-user rate**.

> The rule: **annual = cheaper per user but a year's commitment; monthly = more
> expensive per user but fully flexible.**

### Where you buy

- **Direct from Microsoft** (web-direct, self-service) — pay by credit card or
  invoice.
- **A Cloud Solution Provider (CSP) partner** — a Microsoft partner who sells,
  bills, and supports you, often bundling services.
- **An Enterprise Agreement** — a volume-licensing contract for large organizations.

Because it's a predictable **per-user subscription**, Microsoft 365 makes budgeting
straightforward: multiply users by plan price, with no surprise hardware costs.

## The whole thing in one paragraph

Microsoft 365 is licensed with **per-user subscription licenses** that must be
**assigned** before a user can access services, across plan families aimed at
different organizations: **Business** (Basic = web/mobile only, Standard = adds
desktop apps, Premium = adds advanced security, up to 300 users), **Enterprise**
(E3, and the most comprehensive **E5** with advanced security and compliance), and
**Frontline** (**F3** for shift workers), with optional **add-ons** like Copilot and
Teams Phone. Billing is run from the **Microsoft 365 admin center**, where a
**Billing Administrator** can manage purchases without full admin rights, and
customers choose **annual** (cheaper per user) or **monthly** (flexible) terms,
buying **direct**, through a **CSP partner**, or via an **Enterprise Agreement**.

## Exam focus

- A user's account can exist in **Microsoft Entra ID** but still lack access until a
  **license is assigned** — assignment is what grants the services.
- Plan matching: **Business Basic** = web/mobile apps only (no desktop install);
  **Business Standard** = adds installed desktop apps; **E5** = most comprehensive
  (advanced security + compliance + Teams Phone + Power BI Pro); **F3** = frontline/
  shift workers sharing devices.
- The **Microsoft 365 admin center** is where you buy/assign licenses and view
  invoices; the **Billing Administrator** role manages billing **without** Global
  Admin rights.
- **Annual commitment = lower per-user cost but a year's commitment; monthly =
  higher per-user cost but flexible.**
- **Microsoft 365 Copilot** and **Teams Phone** are examples of **add-ons** bought
  on top of a base plan.
