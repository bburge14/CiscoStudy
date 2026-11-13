# Azure's Core Architecture: Regions, Zones & the Resource Hierarchy

Azure is a global network of datacenters, but you never deal with "a datacenter"
directly. Instead you work with a set of neat abstractions — regions, availability
zones, resources, resource groups, subscriptions, and management groups — that let
you place, organize, and govern what you build. This lesson is the map of that
structure. It splits into two halves: the *physical* geography of Azure, and the
*logical* hierarchy you use to organize resources.

## The physical side: regions, zones, and geographies

### Regions

> **An Azure region is a geographic area containing one or more datacenters that
> are near one another and connected by a low-latency network.** When you deploy a
> resource, you choose the region it lives in.

Picking the right region is a real design decision, and the exam tests the factors
that matter. The relevant considerations are:

- **Service availability** — not every service or VM size exists in every region.
- **Price** — costs for the same resource can differ between regions.
- **Compliance and data residency** — legal rules about where data may be stored.
- **Proximity to users** — a closer region means lower latency for your customers.

If a question asks what to weigh when choosing a region, the right *set* is this
group — services offered, cost, compliance, and latency to users — not things like
the color of the building or the time of day.

### Availability zones

Inside many regions, Azure offers **availability zones** for extra resilience.

> **Availability zones are physically separate locations within a single region,
> each with its own independent power, cooling, and networking.** Spreading a
> workload across zones means the failure of one zone does not take your
> application down.

Zones protect against a datacenter-level failure *within* a region. The number of
zones can vary by region, so don't memorize a fixed count — focus on the idea:
independent facilities, far enough apart to fail independently, close enough for
fast synchronous replication.

### Region pairs and geographies

For protection against a whole-region disaster, Azure uses the idea of paired
regions and groups everything into geographies.

- **A geography** is a discrete market, often a country or area, that serves as a
  **data residency boundary**. If a regulator requires that customer data stay
  within a specific country, you choose regions inside that country's geography.
- **A region pair** is two regions within the same geography, set a safe distance
  apart, used as targets for disaster recovery and data replication. Pairs help
  preserve data residency because both halves usually sit in the same geography.
  (Note that many newer regions are not paired and instead rely on availability
  zones for resilience.)

> When the requirement is "keep data within a country's borders for compliance,"
> think **geography / region pair** — those concepts exist specifically to
> preserve **data residency**.

## The logical side: the resource hierarchy

Now for how you *organize* what you deploy. Azure arranges everything into four
levels of scope, from the single thing you create up to the top of your whole
organization.

> **A resource is a single manageable item you create in Azure** — a virtual
> machine, a storage account, a database, a virtual network. It is the basic unit
> of everything you deploy.

Those resources are organized into containers, and the containers nest. From the
**narrowest** scope to the **broadest**:

| Level | What it is |
|-------|------------|
| **Resource** | A single deployed item (VM, storage account, database) |
| **Resource group** | A logical container that holds related resources, usually for one application or project; managed and deleted together |
| **Subscription** | A unit of billing and access that holds resource groups; also sets spending and usage limits |
| **Management group** | A container for **multiple subscriptions**, used to apply governance (policies and access) across all of them at once |

Read from the top down, the hierarchy is: **management groups → subscriptions →
resource groups → resources.** From broadest scope to narrowest, that is the
order you want when a question asks you to rank them.

### Resource groups

A **resource group** is a logical folder. Every resource must belong to exactly
one resource group. Grouping an application's resources together lets you deploy,
manage, apply permissions to, and delete them as a unit — delete the group and
everything in it goes with it.

### Subscriptions

A **subscription** is both a **billing boundary** (it generates its own invoice)
and an **access/management boundary** (it can carry its own limits and policies).
Organizations often create **more than one subscription** for reasons beyond
splitting the bill:

- To **separate environments** — for example, production from development and test.
- To create **access boundaries** between departments or teams.
- To work within **subscription limits/quotas**, or to isolate different cost
  centers and governance requirements.

So if a question asks "besides separating invoices, why create multiple
subscriptions," the answer is about **isolation and governance** — separate
environments, access control, and staying within service limits.

### Management groups

When you have many subscriptions, you do not want to configure each one by hand.
A **management group** sits *above* subscriptions and lets you apply policy and
role assignments once, to every subscription beneath it. Management groups can even
be nested to mirror your org chart.

### Azure Resource Manager (ARM)

Underneath all of this is **Azure Resource Manager**, the deployment and management
service that every request flows through — whether it comes from the portal, CLI,
PowerShell, or an API. ARM is what consistently creates, updates, and deletes the
resources in your hierarchy.

## The shape of it all

Physically, Azure is organized into **regions** (areas of nearby datacenters),
hardened by **availability zones** (independent facilities within a region) and
**region pairs/geographies** (for disaster recovery and data residency).
Logically, you place each **resource** into a **resource group**, group those
under a **subscription** (billing + access), and govern many subscriptions through
a **management group** — all orchestrated by **Azure Resource Manager**.

## Exam focus

- **Region** = geographic area of nearby datacenters on a low-latency network.
  Choose one based on **service availability, price, compliance/data residency,
  and proximity to users**.
- **Availability zones** = physically separate, independently powered locations
  *within* a region; protect against a single datacenter failure.
- **Geography / region pair** = the concepts for **data residency** and
  region-level disaster recovery (keep data in a country's borders).
- Hierarchy, broadest → narrowest: **management group → subscription → resource
  group → resource**. A **resource** is a single manageable item.
- **Resource group** = logical container managed/deleted together. **Subscription**
  = billing *and* access boundary; create multiple to **separate environments**,
  set access boundaries, and work within limits — not just to split invoices.
- **Management group** = governs **many subscriptions** at once. **Azure Resource
  Manager** is the service all deployments go through.
