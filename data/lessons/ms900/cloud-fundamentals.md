# Cloud Benefits, Service Models & Adoption

Before we talk about any Microsoft 365 app, we need to answer a bigger question:
*why run software in the cloud at all?* Microsoft 365 is a cloud service, so the
exam starts by making sure you understand what "the cloud" buys an organization,
the different shapes cloud services come in, and the practical things to weigh
before moving.

## What the cloud actually is

"The cloud" just means computing delivered as a service over the internet, run in
someone else's data centers, and paid for by subscription instead of bought
outright. You rent capacity and capability; the provider owns and operates the
hardware.

> **Cloud computing turns IT from something you *build and own* into something you
> *consume and pay for as you go*.** You stop managing servers and start
> consuming services.

That single shift is what produces nearly every benefit below.

## The benefits of the cloud

The exam loves to give you a scenario and ask which benefit it describes. Learn
these by their trigger words.

- **Scalability** — grow or shrink your resources to match demand. A firm that
  jumps from 50 to 500 employees simply buys more licenses; no new servers.
- **Elasticity** — scalability that happens quickly and, often, automatically as
  load rises and falls (think seasonal spikes).
- **Cost model: CapEx → OpEx** — instead of a big up-front *capital expenditure*
  (buying servers you own and depreciate), you pay a predictable, per-user
  *operational expenditure*. No hardware to purchase or refresh.
- **Reliability and high availability** — the service is engineered to stay up,
  with redundancy across data centers so a single failure doesn't take you down.
- **Business continuity** — because your data and services live in Microsoft's
  resilient infrastructure, work can continue even if your own office is
  unavailable (a storm, a power cut, a lost laptop).
- **Agility and speed** — you can turn on a new service in minutes rather than
  waiting weeks to procure and rack hardware.
- **Access from anywhere** — email, files, and meetings are reachable from home,
  the office, or the road, on nearly any device with an internet connection.
- **Security and up-to-date software** — the provider continuously patches and
  updates the platform, so you're always on a current, maintained version.

> A clean way to remember the money angle: **CapEx is "buy it," OpEx is "rent
> it."** The cloud moves you from buy to rent.

## The three cloud service models

Cloud services are sold at three levels of abstraction. The difference is *how
much the provider manages for you*.

| Model | What the provider runs | What you manage | Everyday analogy |
|-------|------------------------|-----------------|------------------|
| **IaaS** (Infrastructure as a Service) | The physical hardware, networking, virtualization | The operating system, apps, and data on the VMs you rent | Leasing an empty apartment — you furnish it |
| **PaaS** (Platform as a Service) | Hardware *plus* the OS and runtime platform | Just your application and its data | A furnished apartment — you bring your things |
| **SaaS** (Software as a Service) | Everything — hardware, platform, and the application itself | Only your data, users, and settings | A hotel room — you just show up |

> **Microsoft 365 is a SaaS offering.** Microsoft fully manages the servers, the
> underlying infrastructure, and the software updates; you simply use the apps and
> manage your own users and data. If a scenario says "Microsoft handles the
> servers and patching," the answer is SaaS.

### The shared responsibility model

With any cloud service, security and operational duties are *split* between the
provider and the customer — this is the **shared responsibility model**. The
higher up the stack you buy (toward SaaS), the more the provider handles. But some
duties *always* stay with you: your **data**, your **user accounts and
identities**, and your **access management** are your responsibility in every
model. Microsoft can run the service flawlessly, but it can't stop you from
sharing a file with the wrong person.

## Deployment models: public, private, hybrid

Separate from *what* you buy is *where* it runs:

- **Public cloud** — resources are owned by a provider (like Microsoft) and shared
  among many customers over the internet. Microsoft 365 lives here. It's the most
  cost-effective and scalable.
- **Private cloud** — cloud-style infrastructure dedicated to a single
  organization, for control or regulatory reasons. More control, more cost.
- **Hybrid cloud** — a mix that connects on-premises systems with the public
  cloud, so you can keep some workloads local while using cloud services for
  others. Common during a migration.
- **On-premises** — the traditional model: you own and run everything in your own
  building. Maximum control, maximum cost and effort.

## Considerations before adopting the cloud

Moving to Microsoft 365 isn't free of trade-offs, and the exam expects you to name
the honest considerations:

- **Internet dependency** — because the services are delivered over the internet,
  you need **reliable connectivity and enough bandwidth**. If the link is down,
  access to cloud services suffers.
- **Ongoing subscription cost** — you trade a one-time purchase for a recurring
  per-user fee that continues as long as you use the service.
- **Less direct control** — Microsoft decides when the platform is updated, so you
  give up some of the control you'd have running your own servers.
- **Data residency and compliance** — regulated organizations must confirm where
  data is stored and that the service meets their legal obligations.

For most organizations, these are outweighed by not having to buy, patch, and
refresh servers — a lean IT team can hand the plumbing to Microsoft and focus on
the business. That value proposition, especially for **hybrid work** where people
need secure access from anywhere, is why cloud adoption has become the default.

## The whole thing in one paragraph

The cloud delivers IT as a subscription service over the internet, trading the
capital cost of owning servers (CapEx) for a predictable per-user operating cost
(OpEx) and adding scalability, reliability, business continuity, agility, and
access from anywhere. Services come as **IaaS**, **PaaS**, or **SaaS** — Microsoft
365 is **SaaS**, where Microsoft manages the whole stack and you manage only your
data and users under a **shared responsibility model**. Deployment can be
**public** (Microsoft 365), **private**, or **hybrid**, and before adopting you
weigh internet dependency, recurring cost, reduced control, and compliance.

## Exam focus

- Match benefits to trigger words: **scalability** = grow/shrink with demand,
  **CapEx→OpEx** = stop buying servers and pay per user, **high availability /
  business continuity** = stays up and keeps working if your office is down,
  **access from anywhere** = internet-connected devices.
- **Microsoft 365 = SaaS.** The provider (Microsoft) runs the servers,
  infrastructure, and updates. IaaS = you still manage the OS; PaaS = you manage
  only your app; SaaS = you manage only data and users.
- Under the **shared responsibility model**, **your data, identities, and access**
  are always your job, no matter the model.
- Deployment models: **public** (shared, most scalable — Microsoft 365),
  **private** (dedicated), **hybrid** (on-premises + cloud linked together).
- The classic *consideration* for cloud adoption is dependence on **reliable
  internet connectivity and bandwidth**, plus recurring subscription cost.
