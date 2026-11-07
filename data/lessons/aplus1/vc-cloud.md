# Cloud Computing Models

"The cloud" is just **someone else's computers, rented over the internet**
instead of bought and racked in your own building. Once you accept that one idea,
the whole topic is about two questions: *how much of the stack do you rent* (the
service models) and *who gets to use it* (the deployment models). Add a short
list of defining traits and you have the objective.

## Why rent instead of own?

Running your own servers means buying hardware, powering and cooling it, and
paying staff — and you must buy for your busiest day, leaving the machines idle
the rest of the time. Cloud flips this: a provider owns a giant pool of hardware,
and you rent exactly what you need, when you need it, and pay only for that.

## The service models: IaaS, PaaS, SaaS

The three service models differ by **how much of the computing stack the provider
manages versus how much you do**. Picture the stack from bottom (hardware) to top
(the finished app):

> networking → storage → servers → virtualization → OS → runtime → app → data

- **IaaS** (Infrastructure as a Service) — you rent the raw building blocks:
  virtual machines, storage, and networks. The provider runs the physical
  hardware; **you** install and manage the OS, patches, and everything above.
  Most flexible, most work. *Example: a bare cloud VM you configure yourself.*
- **PaaS** (Platform as a Service) — you rent a ready **platform** to run your own
  code. The provider manages the OS, runtime, and scaling; **you** just deploy
  your application and data. *Example: a managed app/database platform for
  developers.*
- **SaaS** (Software as a Service) — you rent **finished software**, used through
  a browser. The provider manages *everything*; you just log in and use it.
  *Example: web email, online office suites, CRM.*

A classic way to remember who manages what is the **"pizza as a service"**
analogy:

> Making pizza **at home** = on-premises (you buy and do everything). **IaaS** =
> you take home a kit (they provide the kitchen/ingredients, you cook). **PaaS**
> = delivery (they cook, you provide the table and drinks). **SaaS** = dining out
> (they do it all; you just eat).

> **The rule:** the higher you go — IaaS → PaaS → SaaS — the **more the provider
> manages and the less you do.** Match the model to how much control versus
> convenience the scenario wants.

## The deployment models: who can use it

The second question is *who shares the cloud*:

- **Public cloud** — the provider's shared infrastructure, open to any paying
  customer (AWS, Azure, Google). Cheapest and most scalable; you share the
  underlying hardware with strangers (safely isolated).
- **Private cloud** — cloud technology dedicated to **one organization**, run in
  its own data center or a carved-out section of a provider. More control and
  privacy, higher cost — favored where regulations demand it.
- **Hybrid cloud** — a **mix** of public and private that work together, so an
  organization can keep sensitive data private while using the public cloud for
  the rest or for overflow.
- **Community cloud** — shared by **several organizations with a common need**
  (for example, agencies under the same compliance rules) who pool a cloud.

> **Hybrid = public + private combined.** Keep the sensitive workload private and
> burst to public capacity when demand spikes.

## The traits that define "cloud"

NIST lists a handful of characteristics that make something genuinely "cloud."
The A+ expects you to recognize them:

- **On-demand self-service** — you provision resources yourself, instantly,
  through a portal, with no human on the provider's side.
- **Rapid elasticity** — capacity scales **up and down automatically** with
  demand, so you are never stuck over- or under-provisioned.
- **Resource pooling** — the provider pools hardware and serves many customers
  from it (multi-tenancy), assigning slices as needed.
- **Measured service / metered utilization** — usage is tracked and you are
  billed **pay-as-you-go**, like electricity.
- **Broad network access** — reachable over the network from anywhere, on any
  device.
- **High availability** — resources are spread across redundant systems so a
  single failure does not take you down.

### Two terms worth separating

Students mix these up, so pin them down:

- **Scalability** = *planned* growth — you can add capacity as your needs grow
  over time.
- **Elasticity** = *automatic, moment-to-moment* flexing up and down with the
  current load.

> Think of **scalability** as buying a bigger house as the family grows, and
> **elasticity** as the house adding and removing rooms by the hour as guests
> come and go.

### Cloud-based applications and storage

Two everyday uses round out the objective:

- **Cloud file storage / file synchronization** — services like cloud drives keep
  your files **synced** across all your devices and backed up off-site. Edit on
  your laptop, and the change appears on your phone.
- **Cloud-based virtual desktops (VDI)** — your whole Windows desktop runs in the
  cloud and streams to a thin client or browser, so any device becomes your work
  PC. (We cover desktop/VM basics in the next lesson.)

A couple of advanced terms you may see: **cloud bursting** (spilling over from a
private cloud into public capacity during a spike) and **metered** billing that
makes that burst cost-effective.

## The whole thing in one paragraph

Cloud is renting someone else's computers over the internet, described by two
questions. **Service model** = how much the provider manages: **IaaS** (raw VMs/
storage, you run the OS up), **PaaS** (a ready platform, you deploy just your app
and data), **SaaS** (finished software you only log in to) — climbing IaaS→PaaS→
SaaS hands more management to the provider. **Deployment model** = who uses it:
**public** (shared, cheapest), **private** (one organization, most control),
**hybrid** (public + private together, burst and keep sensitive data private), and
**community** (several organizations with a shared need). It counts as cloud when
it has **on-demand self-service, rapid elasticity, resource pooling, measured/
metered billing, broad network access,** and **high availability** — where
**scalability** is planned growth and **elasticity** is automatic moment-to-moment
flexing — and everyday cloud uses include **file synchronization** across devices
and **cloud-based virtual desktops (VDI)**.

## On the exam

- **IaaS → PaaS → SaaS**: the higher you go, the **more the provider manages**.
  IaaS = you manage the OS; PaaS = you manage only the app/data; SaaS = you manage
  nothing but your use.
- Pick the model by control vs convenience. "Rent VMs and run our own OS" = IaaS;
  "developers just deploy code" = PaaS; "browser-based email/office" = SaaS.
- **Public** = shared/cheap; **private** = one org/most control; **hybrid** =
  both, for bursting and keeping sensitive data in-house; **community** = shared
  by orgs with a common requirement.
- **Rapid elasticity** = automatic up/down scaling; **metered/measured service** =
  pay-as-you-go billing; **resource pooling** = multi-tenant shared hardware.
- Distinguish **scalability** (planned growth) from **elasticity** (automatic,
  real-time flexing).
- **File synchronization** keeps files consistent across devices; **VDI** streams
  a full desktop from the cloud.
