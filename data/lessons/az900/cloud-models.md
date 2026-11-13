# Cloud Computing, Deployment Models & Shared Responsibility

Before you can talk about any Azure service, you need the mental model that sits
underneath all of them: what "the cloud" is, how you pay for it, who owns the
hardware, and exactly where Microsoft's job ends and yours begins. This lesson
builds that foundation. Get these ideas straight and a surprising share of the
exam answers itself.

## What cloud computing actually means

> **Cloud computing is renting IT resources — compute, storage, networking,
> databases, and more — over the internet from a provider, and paying only for
> what you use.**

Instead of buying servers, racking them in a room, cooling them, and replacing
them every few years, you reach into a provider's enormous shared pool of
hardware and take exactly the slice you need, right now. When you are done, you
give it back. The provider (Microsoft, in Azure's case) owns and operates the
physical datacenters; you consume the capacity as a service.

### The consumption-based model

The way you pay is as important as what you get. Traditional IT is a big purchase
up front: you buy a server whether or not you ever use its full power. The cloud
works differently.

> **The consumption-based model (also called pay-as-you-go) means you are billed
> only for the resources you actually consume — per second, per gigabyte, per
> request — with no up-front hardware purchase.**

Two consequences fall out of this, and both show up on the exam:

- **Spin up fast, with no capital outlay.** You can provision a resource in
  minutes and start paying only from that moment. There is no procurement cycle.
- **Scale down and your bill shrinks.** This is the key financial advantage when
  demand *drops*. If traffic falls overnight, you can release capacity and simply
  stop paying for it. You never pay for idle hardware you were forced to buy in
  advance.

Think of it like electricity. You don't build a power plant in your basement; you
draw what you need from the grid and the meter charges you for exactly that. Use
less, pay less.

## The three deployment models

"Where does the cloud physically live, and who shares it?" The answer is the
**deployment model**. There are three you must know cold.

> **Public cloud:** the provider owns all the hardware and offers services over
> the internet to many different organizations that share the same underlying
> infrastructure. Azure is a public cloud. You own none of the equipment.

> **Private cloud:** cloud-style resources dedicated to a single organization. It
> may sit in the company's own datacenter or be hosted for them, but it is not
> shared with outsiders. It offers the most control and can satisfy strict
> regulatory needs — at the cost of buying and maintaining the hardware yourself.

> **Hybrid cloud:** a combination of public and private that work together, so
> workloads and data can move between them. You keep sensitive systems private
> while bursting into the public cloud for extra capacity or new projects.

A quick comparison of what each buys you:

| Model | Who shares it | Main advantage | Main trade-off |
|-------|---------------|----------------|----------------|
| **Public** | Many organizations | No hardware to buy; near-unlimited scale; fast | Less direct control over the infrastructure |
| **Private** | One organization | Maximum control and isolation | You fund and maintain the hardware (high CapEx) |
| **Hybrid** | A blend of both | Flexibility; keep some workloads on-premises | More complex to design and manage |

The exam loves the public-vs-private trade-off. The key advantage of the **public
cloud** over running your own private cloud is that you **avoid buying,
maintaining, and over-provisioning hardware** — you trade a large up-front
investment for flexible, on-demand capacity you can grow or shrink at will.

## The shared responsibility model

Moving to the cloud does not make security someone else's problem. It *splits*
the work. The **shared responsibility model** draws the line between what the
cloud provider handles and what the customer must still handle.

> **The cloud provider is always responsible for the physical layer — the
> datacenters, the physical servers and hosts, and the physical network. The
> customer is always responsible for their own data, their identities and user
> accounts, and managing access.**

Picture it as a diagram with a line through the middle. Below the line sits
everything physical, and that is Microsoft's job: when a customer running Azure
virtual machines asks who secures the physical servers and the building they live
in, the answer is always **the cloud provider**. Above the line sit the things
only you can decide: your data, who your users are, and who is allowed to do what.

The clever part is that the line *moves* depending on the service type (which the
next lessons explore). The more of the stack the provider manages, the more of
the middle layers — operating system, networking controls, applications — shift
to them. But no matter which service you pick:

- **You always own your data.** Microsoft never decides what your data is, how it
  is classified, or who should see it.
- **You always own identity and accounts.** Creating users, enforcing strong
  sign-in, and granting the right permissions is your responsibility.
- **You always own access management and endpoints.** The devices your people use
  and the access they are granted stay on your side of the line.

> The single duty that **never** transfers to the provider is securing your own
> **data, identities, and access**. If an exam question asks what the customer is
> *always* responsible for regardless of model, that is the answer.

## Putting it together

Cloud computing is renting IT over the internet and paying only for what you use;
the consumption-based model is why your bill rises and falls with actual demand
and needs no up-front purchase. The public cloud (Azure) is shared infrastructure
the provider owns; a private cloud is dedicated to one organization; a hybrid
cloud bridges the two. And through all of it, the shared responsibility model
keeps the physical layer with the provider while your data, identities, and access
remain yours to protect.

## Exam focus

- **Consumption-based / pay-as-you-go** = billed only for what you use, no
  up-front cost. The financial win when demand **drops** is that you release
  capacity and **stop paying** for it.
- **Public cloud** = provider-owned hardware shared by many organizations over the
  internet (Azure). Its advantage over a **private cloud** is no hardware to buy
  or maintain and elastic, on-demand scale.
- **Private cloud** = dedicated to a single organization; most control, but you
  fund the hardware. **Hybrid** = public and private working together.
- **Shared responsibility model**: the provider always secures the **physical**
  datacenters, hosts, and network; the customer is **always** responsible for
  **data, identities/accounts, and access** — those never transfer to Microsoft.
- If the stem asks "who secures the physical servers and datacenter," the answer
  is the **cloud provider**; if it asks what the customer *always* keeps, the
  answer is **data and identity**.
