# Cloud Service Models, Deployment Models & Requirements

Every cloud project starts with two questions: *what does the business actually
need?* and *how should we shape the solution to meet it?* This lesson covers both
halves of that conversation — reading requirements correctly, and then choosing
the service model, deployment model, and design patterns that satisfy them. Get
this layer right and the rest of the build has a sound foundation; get it wrong
and no amount of clever engineering later will save the project.

## Requirements: functional vs. non-functional

A **requirement** is a statement of something the solution must do or must be.
The single most important distinction on the exam is between two kinds.

> **Functional requirements** describe *what the system does* — a specific
> feature or behavior ("a user can reset their password," "export a report to
> CSV"). **Non-functional requirements** describe *how well* it must do it — the
> quality attributes and constraints, often called the "-ilities": performance,
> scalability, availability, security, recoverability.

So "respond in under 500 ms," "sustain 10,000 concurrent users," "stay available
99.95% of the time," and "recover from a zone failure within 5 minutes" are all
**non-functional** — they constrain quality, not features. If the statement names
a discrete action a user performs, it is functional.

A few requirement artifacts you must recognize:

- **SLA (service-level agreement)** — the *contract* between a provider and a
  customer. It states a measurable commitment (e.g., 99.9% monthly uptime) and
  the remedy, usually **service credits**, if the target is missed.
- **SLO (service-level objective)** — the internal *target* that supports an SLA.
  SLOs roll up into the customer-facing SLA but are not the contract themselves.
- **SLI (service-level indicator)** — the actual measured value (e.g., the uptime
  you observed last month) compared against the objective.
- **Data sovereignty / residency** — a legal requirement that data be stored and
  processed only within a defined jurisdiction (an EU bank's records must stay in
  the EU). This drives region selection more than any technical factor.

## Cloud service models: who manages what

Cloud services are sold at different levels of abstraction. The classic three,
from most customer-managed to least:

| Model | Provider manages | You manage | Example |
|-------|------------------|-----------|---------|
| **IaaS** (Infrastructure) | Physical hardware, virtualization, network | OS, runtime, apps, data | Virtual machines, block storage |
| **PaaS** (Platform) | Everything up to the runtime/OS | Your code and data only | Managed app platforms, managed databases |
| **SaaS** (Software) | The entire stack | Only your data and user settings | Email, CRM, collaboration suites |

The pattern: as you move **IaaS → PaaS → SaaS**, you trade *control* for
*convenience*. IaaS gives you the most flexibility and the most work; SaaS gives
you the least of both. You'll also meet **XaaS** ("anything as a service") umbrella
terms — DBaaS, FaaS (function as a service / serverless), DRaaS — but they all sit
somewhere on this control-vs-convenience spectrum.

### The shared responsibility model

This spectrum is exactly why the **shared responsibility model** matters. Security
and operational duties are *split* between provider and customer, and the line
moves with the service model.

> A reliable rule of thumb: the provider is responsible for the security **of**
> the cloud (the hardware, hypervisor, and facilities); the customer is
> responsible for security **in** the cloud (their data, access controls, and
> configuration). The lower the service model (IaaS), the more falls on you.

One constant across every model: **the customer always owns their data and their
identity/access configuration.** A misconfigured storage bucket is the customer's
fault, never the provider's.

## Cloud deployment models

Where the cloud lives, and who shares it:

- **Public cloud** — resources owned and operated by a provider, shared across
  many tenants (multitenancy). Lowest cost, highest elasticity, least control.
- **Private cloud** — cloud infrastructure dedicated to one organization, whether
  on-premises or hosted. More control and isolation, higher cost.
- **Hybrid cloud** — a deliberate mix of public and private that work together
  (e.g., sensitive data on-prem, burst capacity in public cloud).
- **Community cloud** — infrastructure *shared by several organizations with
  common requirements* (regulatory, mission, security) and restricted to that
  group. Regional hospitals under the same privacy rules jointly funding one
  environment is the textbook example.
- **Multicloud** — using *more than one public provider* on purpose, to avoid
  lock-in, meet data-residency rules, or use each provider's best services.

Do not confuse hybrid with multicloud: hybrid mixes *private + public*, while
multicloud means *multiple public providers*.

## Cloud-native design patterns

Modern cloud solutions favor **cloud-native** design — building for the cloud's
strengths (elasticity, managed services, automation) rather than lifting a legacy
monolith unchanged.

- **Microservices** — decompose an application into small, independently
  deployable services that each own one capability and talk over APIs. This gives
  **loose coupling**: a change or failure in one service doesn't cascade into the
  others, and each can scale on its own.
- **Containers** — package an app with its dependencies into a lightweight,
  portable unit that shares the host OS kernel (unlike a VM, which carries a full
  guest OS). Containers start in seconds and pack densely. Docker is the common
  runtime; orchestration (Kubernetes) manages them at scale.
- **Serverless / FaaS** — you deploy functions and the provider runs them on
  demand, scaling to zero when idle. You pay per invocation and never manage
  servers. Great for event-driven, spiky workloads.

### Designing for resilience

The headline resilience principle is **eliminate single points of failure**.
Spread redundant, identical instances across independent **availability zones**
(isolated data-center groups) behind a **load balancer**, so losing one zone
doesn't take the service down. Pair this with loose coupling and stateless
components and the architecture can lose pieces without losing the service.

## Exam focus

- **Non-functional = the "-ilities" and constraints** (performance, uptime,
  recovery, security); **functional = a specific user action or feature.** Latency,
  throughput, scalability, and availability targets are always non-functional.
- **SLA = the contract and its penalties; SLO = the target that supports it; SLI =
  the measured value.** "Service credits for missed uptime" points to an SLA.
- "**Data must stay in country/region**" is a **data sovereignty / residency**
  requirement and drives region choice.
- Service-model control spectrum: **IaaS (most control/work) → PaaS → SaaS (least).**
  Remember the shared responsibility split moves with it; the customer **always**
  owns data and access configuration.
- **Hybrid = private + public together; multicloud = multiple public providers;
  community = shared by organizations with common requirements.**
- A **container** shares the host kernel (lightweight, portable); a **VM** carries
  a full guest OS. **Microservices** give loose coupling; **serverless** scales to
  zero and bills per invocation.
- Spreading redundant instances across **availability zones** behind a load
  balancer is the canonical way to **remove single points of failure** (HA).
