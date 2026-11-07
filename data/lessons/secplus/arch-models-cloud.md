# Architecture Models & Cloud Security

How you *build* a system shapes how you *secure* it. A sprawling cloud deployment,
a tiny embedded sensor, and a legacy factory controller each come with their own
security trade-offs. This lesson surveys the main architecture models and then
zooms in on securing the cloud and virtualization — the places most modern work
lives.

## Why architecture is a security question

> Every architecture choice trades some mix of **availability, resilience, cost,
> scalability, patchability, and attack surface**. There's no free lunch — the
> model you pick decides which risks you inherit.

When the exam describes a design, it's really asking: *what did this choice make
easier, and what did it make riskier?* Keep that lens on as we go.

## On-premises vs. cloud

- **On-premises** — you own and run everything in your own building. Maximum
  control, but you carry all the cost, patching, and physical security yourself.
- **Cloud** — you rent computing from a provider. Cheaper to start, instantly
  scalable, but you give up some control and must understand *who secures what*.

### The shared responsibility model

The most tested cloud idea is the **responsibility matrix** (shared
responsibility model). The provider secures *some* layers and you secure the rest,
and the line moves depending on the service type:

| Model | Provider secures | You secure |
|-------|------------------|------------|
| **IaaS** (infrastructure) | Physical, host, network | OS, apps, data |
| **PaaS** (platform) | + OS, runtime | Apps, data |
| **SaaS** (software) | Almost everything | Mostly just your data and access |

> No matter the model, **you are always responsible for your own data and who can
> access it.** The provider never takes that off your plate.

**Hybrid** deployments mix on-prem and cloud, and bring their own considerations
(consistent policy across both, secure links between them). Using **third-party
vendors** in the cloud extends your trust — and your risk — to them.

## Modern cloud-native building blocks

- **IaC (Infrastructure as Code)** — defining servers and networks in code
  (templates/scripts) rather than clicking buttons. Repeatable and reviewable, but
  a mistake in the template is instantly everywhere.
- **Serverless** — you run functions without managing servers; the provider
  handles the infrastructure. Shrinks what you patch, but adds dependence on the
  provider.
- **Microservices** — one big app split into many small, independent services.
  Flexible and scalable, but more network connections to secure between them.
- **Containerization** — packaging an app with its dependencies (e.g. Docker) so
  it runs consistently anywhere. Lighter than full VMs; containers share the host
  OS kernel, so isolation is thinner.
- **Virtualization** — running many **virtual machines** on one physical host via
  a **hypervisor**. Each VM has its own OS and strong isolation.

## Network architecture models

- **Physical isolation / air-gapped** — a system with *no* network connection to
  anything untrusted. The strongest isolation, used for the most sensitive
  systems; the trade-off is you can't manage it remotely.
- **Logical segmentation** — using VLANs and subnets to separate traffic on shared
  hardware. Cheaper and flexible, but a misconfiguration can collapse the
  separation.
- **SDN (Software-Defined Networking)** — separating the network's **control
  plane** (decisions) from the **data plane** (forwarding), managed centrally in
  software. Agile, but the central controller is a juicy target.

## Specialized and constrained systems

Some environments can't be secured like a normal server, and the exam wants you to
recognize them:

- **IoT (Internet of Things)** — everyday devices (cameras, thermostats) with
  network connectivity. Often weak defaults, rarely patched, huge in number.
- **ICS / SCADA** — Industrial Control Systems and Supervisory Control and Data
  Acquisition systems that run factories, power grids, and utilities. They
  prioritize uptime over security and often can't be patched or taken offline.
- **RTOS (Real-Time Operating System)** — runs where timing is critical (medical
  devices, car systems). Limited resources make traditional security hard.
- **Embedded systems** — purpose-built computers inside other products, often with
  no easy way to update.

> The common thread for IoT, ICS/SCADA, RTOS, and embedded systems: **hard or
> impossible to patch, and often can't be taken down.** So you protect them
> indirectly — **segmentation, isolation, and monitoring** rather than patching.

## Architecture considerations (the trade-off checklist)

When choosing or defending a design, weigh: **availability**, **resilience**,
**cost**, **responsiveness**, **scalability**, **ease of deployment**, **risk
transference** (e.g. shifting risk to a provider or insurer), **ease of
recovery**, **patch availability** vs. **inability to patch**, and the physical
realities of **power** and **compute**. The "right" answer on the exam is usually
the option that matches the *priority the scenario states* — if it stresses
uptime, favor availability and resilience; if it stresses budget, favor cost.

## Securing cloud and virtualization

A few threats are unique to shared, virtualized infrastructure:

- **VM escape** — breaking out of a guest VM to reach the hypervisor or sibling
  VMs. The worst-case failure of virtualization isolation.
- **VM sprawl** — so many forgotten VMs spin up that nobody tracks or patches them
  all, creating blind spots.
- **Resource reuse** — memory or storage handed to a new tenant without being
  wiped, leaking the previous tenant's data.
- **Misconfiguration** — the top cause of real cloud breaches: public storage
  buckets, over-broad identity permissions, open management ports.

Defenses that fit the cloud:

- **Security groups** — virtual firewalls around cloud resources, allowing only
  needed traffic.
- **Least-privilege IAM** — tightly scoped cloud identities and roles.
- **Encryption** of data at rest and in transit by default.
- **CASB (Cloud Access Security Broker)** — a control point that enforces policy
  between users and cloud services.
- **Monitoring and logging** turned on everywhere, since you can't physically
  inspect the hardware.

## The whole thing in one paragraph

Architecture is a security decision because every model trades availability,
resilience, cost, scalability, patchability and attack surface differently. The
big split is **on-premises** (full control, full burden) vs. **cloud** (scalable,
but governed by the **shared responsibility model**, where the provider secures
lower layers and you always own your data and access). Cloud-native pieces —
**IaC**, **serverless**, **microservices**, **containers**, and **virtualization**
— each shift what you must protect, while **air-gapping**, **logical
segmentation**, and **SDN** describe how networks are separated. Constrained
systems like **IoT**, **ICS/SCADA**, **RTOS**, and **embedded** devices usually
can't be patched or downed, so you protect them with **segmentation, isolation,
and monitoring**. In the cloud specifically, watch for **VM escape**, **sprawl**,
**resource reuse**, and above all **misconfiguration**, countered with security
groups, least-privilege IAM, encryption, CASBs, and heavy logging.

## On the exam

- The **shared responsibility model** is heavily tested. Remember the sliding
  scale IaaS → PaaS → SaaS (provider secures more as you go right) and that **you
  always own your data and access**.
- IoT, ICS/SCADA, RTOS, and embedded systems share one weakness: **can't easily
  patch or take offline** → the answer is usually **segmentation/isolation and
  monitoring**, not "install antivirus" or "patch it."
- **Air-gapped** = no network connection at all; the trade-off is no remote
  management.
- **VM escape** is breaking *out* of a VM; **resource reuse** is leftover data
  leaking between tenants.
- When a question lists design options, pick the one matching the **stated
  priority** (uptime → availability/resilience, budget → cost, speed of change →
  scalability/ease of deployment).
- The leading cause of real cloud incidents is **misconfiguration** — a very
  common correct answer.
