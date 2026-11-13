# Support Plans & Technical Resources

When something goes wrong at 2 a.m., or you just want best-practice advice, AWS has
a tier of **support plans** and a shelf of **technical resources** to lean on. The
exam expects you to match a need — a 24/7 phone line, a dedicated advisor,
automated best-practice checks — to the right plan or tool. This lesson maps them
out.

## The AWS Support plans

AWS offers several support plans at increasing price and service levels. The
Cloud Practitioner exam tests the long-standing five-tier lineup, so learn these:

| Plan | Who it's for | Key features |
|------|--------------|--------------|
| **Basic** | **Every** AWS account, **free** | Documentation, whitepapers, support forums, core **Trusted Advisor** checks, AWS Health Dashboard. **No technical support cases.** |
| **Developer** | Experimenting / early development | **Business-hours email** access to support; the cheapest plan with technical support |
| **Business** | Production workloads | **24/7** phone, chat, and email with Cloud Support Engineers; **full Trusted Advisor** |
| **Enterprise On-Ramp** | Production/business-critical | Everything in Business, plus a **pool of Technical Account Managers** and faster response |
| **Enterprise** | Business- and mission-critical | A **designated Technical Account Manager (TAM)**, concierge support, **Well-Architected reviews**, and the **fastest** response times |

A few facts that turn into exam answers:

> **Basic** is **free and included with every account**, but you **cannot open
> technical support cases** with it. **Business** is the lowest-cost plan offering
> **24/7 phone, chat, and email** support. **Enterprise** is the plan with a
> **designated Technical Account Manager (TAM)**.

### What separates the tiers

- **Technical support channels** widen as you climb: none (Basic) → email
  (Developer) → 24/7 phone/chat/email (Business and up).
- **Response times** get faster: Business targets a 1-hour response for a
  production system down, while Enterprise targets about **15 minutes** for a
  business-critical system down.
- **The Technical Account Manager (TAM)** is the headline of the top tiers: a
  *pool* of TAMs at Enterprise On-Ramp, and a **designated TAM** at Enterprise, who
  gives proactive guidance and runs Well-Architected reviews.

> Whenever a question mentions a **designated Technical Account Manager** or
> **proactive, personalized guidance**, the answer is **Enterprise Support.**

### Choosing the right plan

The exam often hands you a one-line requirement and asks for the cheapest plan
that meets it. Work from the need:

- "Free, included with every account" → **Basic.**
- "Just experimenting, email support is fine" → **Developer.**
- "Running in production, need **24/7 phone** support" → **Business** (the
  lowest-cost plan that offers 24/7 phone/chat/email).
- "Business-critical, want a **designated TAM** and Well-Architected reviews" →
  **Enterprise.**

The trick is "the **lowest-cost** plan that does X." Don't jump to Enterprise just
because it has every feature — pick the first tier up the ladder that satisfies the
stated requirement.

### A note on recent changes

AWS **restructured its support plans in late 2025**, introducing newer tiers such
as **Business Support+** and **Unified Operations** and beginning to retire the
Developer, Business, and Enterprise On-Ramp plans (with those legacy plans
scheduled to end in early 2027). The CLF-C02 exam and most study material still
describe the classic five tiers above, so that's what you should answer with — but
be aware the real-world lineup is changing, and the **Technical Account Manager**,
**24/7 support**, and **free Basic** concepts carry over regardless of the names.

## Technical resources

Beyond paid support, AWS provides a wealth of tools and resources — many free — to
help you build well. These are heavily tested, so learn each one's purpose.

| Resource | What it gives you |
|----------|-------------------|
| **AWS Trusted Advisor** | **Automated best-practice checks** across six categories: **cost optimization, security, fault tolerance, performance, operational excellence, and service limits (quotas)** |
| **AWS Health Dashboard** | Alerts about AWS service events — including a **personalized view of events affecting your own account's resources**, with remediation guidance |
| **AWS re:Post** | A **free, community-driven question-and-answer** service where AWS experts and users respond (the successor to the AWS forums) |
| **AWS Documentation** | Official technical docs and user guides for every service |
| **AWS Whitepapers** | In-depth technical and business guidance authored by AWS |
| **AWS Knowledge Center** | Answers to the most frequently asked support questions |
| **AWS Marketplace** | A digital catalog to **find, buy, and deploy third-party software** that runs on AWS |
| **AWS Partner Network (APN)** | The global community of **partners** (consulting and technology) who help you build and migrate |
| **AWS Professional Services / AWS IQ** | AWS experts (ProServe) and a marketplace to hire certified **third-party experts** (IQ) for help |

Two that are easy to confuse:

> **Trusted Advisor** inspects *your resources* and recommends best-practice
> improvements across cost, security, fault tolerance, performance, and service
> limits. The **AWS Health Dashboard** tells you about *AWS service events and your
> account's health* — outages and issues that affect you. One advises on your
> setup; the other reports on operational events.

And for getting help from the community versus from AWS directly: **re:Post** is
the **free community Q&A**, while opening a **support case** requires a paid support
plan (Developer and above).

## The whole thing in one paragraph

AWS Support climbs from **Basic** (free, no support cases) through **Developer**
(business-hours email), **Business** (24/7 phone/chat/email), **Enterprise
On-Ramp** (a TAM pool), to **Enterprise** (a **designated TAM**, Well-Architected
reviews, fastest response) — with the designated **TAM** and 24/7 access being the
most-tested distinctions, even as AWS reshuffles the plan names in 2025–2027. On
top of support, free and paid **resources** help you build well: **Trusted
Advisor** (best-practice checks across cost, security, fault tolerance,
performance, operational excellence, and service limits), the **Health Dashboard** (personalized service-
event alerts), **re:Post** (community Q&A), plus documentation, whitepapers, the
**Marketplace**, and the **Partner Network**.

## Exam focus

- **Basic** = **free**, included with every account, **no technical support
  cases**. **Business** = lowest-cost plan with **24/7 phone/chat/email**.
  **Enterprise** = **designated Technical Account Manager (TAM)** + Well-Architected
  reviews + fastest response.
- A **designated TAM / proactive personalized guidance** → **Enterprise Support.**
- **Trusted Advisor** = automated best-practice checks across **cost, security,
  fault tolerance, performance, operational excellence, and service limits (quotas).**
- **AWS Health Dashboard** = alerts about AWS events, including a **personalized
  view of your own account's** affected resources.
- **AWS re:Post** = **free community Q&A**; opening a support case needs a paid
  plan.
- **AWS Marketplace** = buy third-party software; **AWS Partner Network** =
  partners who help you build/migrate.
- Current-events note: AWS is **restructuring support plans** (Business Support+,
  Unified Operations, retiring Developer/Business/Enterprise On-Ramp by 2027), but
  answer the exam with the **classic five tiers** above.
