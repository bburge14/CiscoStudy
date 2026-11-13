# Support, SLAs & Service Lifecycle

The final pieces of the exam are the least glamorous but very testable: when
something breaks, **how do you get help and what has Microsoft promised?** And as
Microsoft 365 constantly evolves, **how are new features previewed, released, and
announced?** This lesson covers support options and the service level agreement,
then the service lifecycle.

## The Service Level Agreement (SLA)

Customers handing their email and files to the cloud want a guarantee of
uptime. That guarantee is the SLA.

> A **Service Level Agreement (SLA)** is a **financially backed** commitment that
> Microsoft's online services will be **available a certain percentage of the
> time** — for Microsoft 365, a **99.9% monthly uptime** target. "Financially
> backed" means that if Microsoft misses it, you may be eligible for **service
> credits**.

Two nuances worth knowing:

- **99.9%** sounds nearly perfect but still allows a small amount of downtime each
  month — the SLA defines exactly how availability is measured.
- A credit generally applies only when Microsoft **declares** a qualifying service
  incident, not for every hiccup on your end (your own internet outage isn't
  covered).

## Checking service health

When users report that Outlook or Teams is slow, your first question should be: *is
this us, or is it Microsoft?* There's a dedicated place to find out.

> The **Service health** page in the **Microsoft 365 admin center** tells you
> whether **Microsoft is experiencing a service incident** affecting your services
> — so you can tell waiting users "Microsoft is on it" instead of chasing a
> non-existent local problem.

## Getting support

Microsoft 365 offers several layers of help:

- **Self-help** — documentation, how-to guides, and community forums for routine
  questions.
- **Assisted support** — open a **support request** (also called a service request)
  from the **Microsoft 365 admin center**. You **assign a severity** to indicate how
  urgent it is, which influences response time; critical issues get faster, around-
  the-clock attention.
- **FastTrack for Microsoft 365** — for customers onboarding at scale, FastTrack
  provides **Microsoft-led guidance and remote assistance** to help **deploy and
  adopt** Microsoft 365 and migrate data, at no extra cost for qualifying
  subscriptions.
- **Premium paid support** (such as Unified Support) — advanced, proactive support
  that larger organizations can purchase.

> Two quick tells: "**check if Microsoft is down**" = the **Service health** page;
> "**get Microsoft's help to deploy and adopt** M365 at scale" = **FastTrack**.

## The service lifecycle

Microsoft 365 is a living service — features arrive continuously rather than in big
boxed releases every few years. That's governed by a **Modern Lifecycle Policy** of
continuous servicing: as long as you stay current and licensed, the service keeps
being supported and updated. But features don't appear all at once; they move
through stages.

### From preview to general availability

> New capabilities progress through a lifecycle: **private preview** (a limited,
> invite-only early look), then **public preview** (open to customers who opt in,
> but **not yet fully supported or SLA-backed**), and finally **general
> availability (GA)** — fully released, supported, and covered by the SLA.

The lesson here: **preview features are for evaluation**, may change, and shouldn't
be relied on for production until they reach GA.

### Finding out what's coming

Microsoft gives you two different windows into change — don't mix them up:

| Resource | What it shows | Audience |
|----------|---------------|----------|
| **Microsoft 365 roadmap** | A **public** view of features **in development, rolling out, or recently launched** across the whole service | Anyone |
| **Message center** (in the admin center) | **Advance notices** about changes and new features that will affect **your specific tenant** | Your admins |

So the **roadmap** is the big public picture of where Microsoft 365 is going, while
the **Message center** is the targeted, tenant-specific heads-up your admins act on.

### Controlling how fast your tenant gets features

Organizations can also choose how early their users receive new features:

- **Standard release** — the **default**. Users get new features on the normal,
  **broadly available** schedule.
- **Targeted release** — opt a **group of pilot users** (or the whole organization)
  into features **earlier**, to evaluate and prepare before the broad rollout.

> Remember: **Standard = the normal schedule; Targeted = early access** for pilots.
> If a scenario wants some users to try features *ahead of everyone else*, that's
> **Targeted release**.

## The whole thing in one paragraph

Microsoft 365's **SLA** is a **financially backed 99.9% uptime** commitment with
**service credits** if missed, and the **Service health** page in the **Microsoft
365 admin center** shows whether Microsoft is having an incident. Support ranges
from self-help to **severity-rated support requests** opened in the admin center,
with **FastTrack** providing free deployment and adoption guidance at scale. Under a
**continuous (Modern Lifecycle) servicing** model, features move from **private
preview** to **public preview** (not yet SLA-backed) to **general availability**;
the **Microsoft 365 roadmap** is the public view of what's coming, the **Message
center** gives tenant-specific advance notice, and **Standard** vs **Targeted
release** controls whether users get features on the normal schedule or early.

## Exam focus

- An **SLA** is a **financially backed** uptime commitment (**99.9%** for Microsoft
  365); missing it can earn **service credits**.
- "Is Microsoft having an outage?" → the **Service health** page in the **Microsoft
  365 admin center**. Open a **support request** there and **assign a severity**.
- **FastTrack for Microsoft 365** = Microsoft-provided **deployment and adoption**
  guidance/remote assistance for qualifying customers.
- Lifecycle stages: **private preview → public preview (not SLA-backed) → general
  availability (GA)**.
- **Microsoft 365 roadmap** = public view of upcoming/rolling-out/launched features;
  **Message center** = advance notices for **your tenant**.
- **Standard release** = normal/default schedule; **Targeted release** = **early**
  access for pilot users.
