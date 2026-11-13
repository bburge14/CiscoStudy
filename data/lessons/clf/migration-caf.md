# Cloud Adoption Framework & Migration Strategies

Deciding to use the cloud is the easy part. Actually moving a company's people,
processes, and hundreds of existing applications onto AWS is a large program of
work, and doing it blindly is how migrations stall. AWS offers two pieces of
structure for this: the **Cloud Adoption Framework** for organizing the whole
journey, and a set of **migration strategies** (the "R"s) for deciding what to do
with each individual application.

## The AWS Cloud Adoption Framework (CAF)

> The **AWS Cloud Adoption Framework (AWS CAF)** is guidance that helps an
> organization build a plan for its cloud journey, organized into **six
> perspectives**. Each perspective groups the capabilities a particular set of
> stakeholders is responsible for.

Think of CAF as a readiness checklist for the *whole business*, not just the tech.
A migration fails as often for people and governance reasons as for technical
ones, so CAF deliberately covers both. The six perspectives split neatly into
three that are business-focused and three that are technical:

| Perspective | Focus | Who cares |
|-------------|-------|-----------|
| **Business** | Tie cloud investment to business outcomes | CEO, CFO, CIO, CTO |
| **People** | Culture, org structure, roles, and skills/training | HR, team leads, cloud director |
| **Governance** | Manage and measure the initiative; control risk | program/portfolio managers, CFO |
| **Platform** | Build the cloud platform and modernize workloads | architects, engineers |
| **Security** | Confidentiality, integrity, availability of data and systems | CISO, security architects |
| **Operations** | Run and support services at the level the business needs | ops and SRE leaders |

The first three (**Business, People, Governance**) are about the organization;
the last three (**Platform, Security, Operations**) are about the technology. If a
question describes a *capability gap* — say, "staff need new skills" (People) or
"we need to control risk and compliance across the program" (Governance) — map it
to the matching perspective.

## The migration strategies: the 7 R's

Once you've planned the journey, you tackle applications one at a time. For each
one you pick a **migration strategy**. AWS describes seven, commonly called the
**7 R's** (they grew out of an earlier "6 R's" list; the seventh, *Relocate*, was
added later). The exam leans hardest on the first few.

> For each application, you choose **Rehost, Replatform, Repurchase, Refactor,
> Retire, Retain, or Relocate** — ranging from "move it as-is" to "rebuild it" to
> "don't move it at all."

| Strategy | Nickname | What you do |
|----------|----------|-------------|
| **Rehost** | "lift and shift" | Move the app to AWS **as-is**, no code changes. Fastest; good for a deadline. |
| **Replatform** | "lift, tinker, and shift" | Move it but make a **few optimizations** — e.g. put the database on Amazon RDS — without changing the core architecture. |
| **Repurchase** | "drop and shop" | **Replace** it with a different product, usually a SaaS subscription (drop a self-hosted CRM for a SaaS CRM). |
| **Refactor / Re-architect** | — | **Redesign** the app to be cloud-native (e.g. break a monolith into microservices or serverless). Most effort, most long-term benefit. |
| **Retire** | — | **Decommission** it — you discover it's no longer needed and simply turn it off. |
| **Retain** | "revisit" | **Keep it where it is** for now (on premises), perhaps because it's not ready to move or a recent investment. |
| **Relocate** | — | Move infrastructure **without buying new hardware or changing operations** — e.g. shift a VMware environment to AWS as a unit. |

How to tell the close ones apart on the exam:

- **Rehost vs. Replatform** — both *move* the app. Rehost changes **nothing**;
  Replatform makes **small optimizations** (the word "tinker" is the clue).
- **Repurchase vs. Refactor** — Repurchase **buys a replacement** (often SaaS);
  Refactor **rebuilds your own** app to be cloud-native.
- **Retire vs. Retain** — Retire means **turn it off** (not needed); Retain means
  **leave it running** where it is (not ready, or deliberately kept).

A quick analogy with a house move: Rehost is packing everything into the same
boxes and moving as-is. Replatform is upgrading a few appliances during the move.
Repurchase is selling your furniture and buying new. Refactor is building a new
house to a better design. Retire is throwing out what you don't need, and Retain
is leaving some things in the old place for now.

## Tools that help you migrate

You don't do all this by hand. A few services come up at Cloud Practitioner level:

- **AWS Migration Hub** — a single place to **discover** your existing servers and
  applications and **track** the progress of a migration across tools.
- **AWS Application Migration Service (MGN)** — the primary service for
  **rehosting** servers by replicating them to AWS with minimal downtime.
- **AWS Database Migration Service (DMS)** — migrates databases to AWS, and can
  migrate between different database engines, while the source stays online.
- **AWS DataSync** — moves large amounts of data **online** between on-premises
  storage and AWS over the network.

### A note on the Snow family

You may still see the **AWS Snow Family** (Snowball Edge, Snowcone) mentioned as
rugged physical devices AWS ships to you so you can copy data onto them and mail
them back — useful when there isn't enough bandwidth to transfer petabytes online.
Be aware that **AWS is winding the Snow Family down**: Snowball Edge devices went
*end of sale* in late 2025, with support ending at the end of 2026. For new needs,
AWS now points customers to online transfer with **DataSync**, secure in-person
transfer at an **AWS Data Transfer Terminal**, or partner solutions. Know Snow as
the historical "offline bulk data transfer" answer, but don't treat it as the
go-to for a brand-new project.

## The whole thing in one paragraph

The **Cloud Adoption Framework** plans the *whole journey* across **six
perspectives** — **Business, People, Governance** (organizational) and
**Platform, Security, Operations** (technical) — so a migration doesn't trip over
skills, governance, or operations. For each application you then pick one of the
**7 R's**: **Rehost** (as-is), **Replatform** (small tweaks), **Repurchase**
(buy a replacement), **Refactor** (rebuild cloud-native), **Retire** (turn off),
**Retain** (leave for now), or **Relocate** (move infrastructure wholesale). Tools
like **Migration Hub**, **Application Migration Service**, **DMS**, and
**DataSync** carry out the work, with the **Snow Family** as the legacy offline
transfer option that AWS is now retiring.

## Exam focus

- **CAF has six perspectives**: **Business, People, Governance** (business-side)
  and **Platform, Security, Operations** (technical-side). Match a described gap
  (skills → People, risk/compliance → Governance) to its perspective.
- Know the **R's** cold, especially: **Rehost** = lift-and-shift, no changes;
  **Replatform** = lift, tinker, and shift (small optimizations like moving to
  RDS); **Repurchase** = drop-and-shop (replace with SaaS); **Refactor** =
  re-architect to cloud-native; **Retire** = decommission; **Retain** = keep as-is
  for now.
- **Rehost vs. Replatform**: "no code changes" = Rehost; "a few optimizations" =
  Replatform. **Retire vs. Retain**: turn off vs. leave running.
- **DMS** migrates databases (even across engines) with the source online;
  **Application Migration Service (MGN)** rehosts servers; **Migration Hub**
  tracks the overall effort; **DataSync** moves bulk data online.
- The **Snow Family** is the historical offline bulk-transfer device set and is
  **being retired** — prefer DataSync or other current options for new transfers.
