# Capacity Planning, Scaling, Integration & Migration

A design has to hold up under real load, and most workloads don't *start* in the
cloud — they arrive there. This lesson covers how architects size a system and let
it grow (capacity planning and scaling), and how existing applications and data get
*into* the cloud and connected to everything else (migration and integration).

## Capacity planning

**Capacity planning** is forecasting how much compute, storage, memory, and
bandwidth a workload will need, so you provision enough to meet demand without
paying for a pile of idle resources. It rests on a few inputs:

- A **performance baseline** — a measurement of normal behavior (CPU, memory,
  requests per second) you compare everything against. Without a baseline you
  can't tell "busy" from "broken."
- **Trend analysis** — looking at historical usage to project future demand
  (seasonal peaks, steady growth) so you plan ahead of the curve.
- **Quotas and limits** — cloud providers cap how many resources an account can
  create. Capacity planning has to account for these, and you request increases
  before a launch, not during one.

The cloud's advantage over a fixed data center is **elasticity**: capacity can
grow and shrink automatically with demand, so you don't have to size for peak and
eat the cost year-round.

## Scaling: vertical vs. horizontal

There are two fundamentally different ways to add capacity, and the exam leans on
the distinction.

> **Vertical scaling (scale up)** makes a single instance *bigger* — more vCPU,
> more RAM. **Horizontal scaling (scale out)** adds *more instances* and spreads
> load across them.

| | Vertical (up) | Horizontal (out) |
|--|--------------|------------------|
| How | Resize one node | Add more nodes |
| Ceiling | Limited by the largest instance | Near-unlimited |
| Downtime | Often requires a reboot | None if load-balanced |
| Resilience | Still a single point of failure | Survives losing a node |
| Best for | Monoliths, databases that can't shard | Stateless web/app tiers |

Horizontal scaling is the cloud-native default because it is elastic and
resilient, but it requires the workload to be **stateless** (any instance can
serve any request) and sitting behind a **load balancer**.

### Autoscaling

**Autoscaling** adds or removes instances automatically against a policy. Two
trigger styles:

- **Reactive / dynamic scaling** fires on a live metric crossing a threshold
  ("CPU > 70% for 5 minutes → add two instances"). Simple and demand-driven, but
  it reacts *after* load arrives.
- **Scheduled scaling** changes capacity on a clock ("scale to 20 instances at
  8 a.m. weekdays") when you know the pattern in advance.
- **Predictive scaling** uses historical trends/ML to provision *ahead* of an
  expected spike.

A good policy also defines **minimum, maximum, and desired** instance counts, and
a **cooldown** so the group doesn't thrash (scaling up and down repeatedly).
**Right-sizing** — matching instance type to actual need — is the companion
discipline that keeps autoscaling from scaling out oversized nodes.

## Migration: moving workloads to the cloud

When an existing application moves to the cloud, you choose a **migration
strategy**. The common framework is the "**R**s":

- **Rehost ("lift and shift")** — move the workload as-is onto cloud VMs. Fastest,
  lowest risk, but you gain few cloud-native benefits.
- **Replatform ("lift and reshape")** — make a few optimizations during the move
  (e.g., swap a self-managed database for a managed one) without rewriting.
- **Refactor / re-architect** — redesign the app for the cloud (microservices,
  serverless). Most effort and cost, most long-term benefit.
- **Repurchase** — drop the old app and move to a SaaS equivalent.
- **Retain** — leave it where it is (not ready, or not worth moving).
- **Retire** — decommission it; it's no longer needed.

Two technical migration moves to know:

- **P2V (physical-to-virtual)** — convert a physical server into a VM image.
- **V2V (virtual-to-virtual)** — move a VM between hypervisors or platforms.

And two *cutover* styles:

- **Big-bang** — migrate everything and switch over at once. Simpler timeline,
  higher risk, harder rollback.
- **Phased** — move in stages (by module, region, or user group), reducing blast
  radius at the cost of running both environments during transition.

> Migration always needs a **rollback plan** and a maintenance window. Data
> migration in particular should be validated with a checksum or record count
> before you decommission the source — never delete the origin until the target
> is verified.

Migrations can run **online** (source stays live, changes sync continuously, then
a brief final cutover — minimal downtime) or **offline** (source is quiesced,
copied, then brought up elsewhere — simpler but with an outage window).

## Integration: making systems talk

Once in the cloud, workloads rarely stand alone. **Integration** connects them to
each other and to systems left on-premises.

- **APIs** — the primary integration surface; services expose REST (or gRPC/
  GraphQL) endpoints that other systems call.
- **Middleware / message queues / event buses** — decouple producers from
  consumers so systems integrate asynchronously and tolerate bursts.
- **Hybrid connectivity** — VPN or a dedicated private circuit (e.g., a direct
  interconnect) links a cloud VPC to the corporate network so integrated apps
  behave as one network.
- **Data integration / ETL** — moving and transforming data between systems so a
  cloud analytics platform can read on-prem records, for example.

The guiding idea mirrors good architecture: integrate through **loose coupling**
(well-defined APIs and queues) rather than brittle point-to-point links, so one
system's change or outage doesn't break the others.

## Exam focus

- **Vertical = bigger instance (scale up), horizontal = more instances (scale
  out).** Horizontal is elastic and resilient but needs **stateless** apps behind
  a **load balancer**; vertical is still a single point of failure.
- **Autoscaling** types: **reactive/dynamic** (metric threshold), **scheduled**
  (clock), **predictive** (forecast). Policies set min/max/desired and a
  **cooldown**; **right-sizing** prevents scaling out oversized nodes.
- A **performance baseline** is the reference for "normal"; **trend analysis**
  forecasts growth; watch provider **quotas/limits** before a launch.
- Migration **R**s: **rehost** = lift-and-shift (fastest, fewest benefits);
  **replatform** = minor optimization; **refactor** = full redesign (most
  effort/benefit); plus **repurchase, retain, retire.**
- **P2V** = physical→VM, **V2V** = VM→VM. **Online** migration minimizes downtime
  via continuous sync; **offline** takes an outage. **Phased** cutover lowers risk
  vs. **big-bang**. Always validate data before retiring the source.
- Integrate through **APIs, message queues/middleware,** and **hybrid VPN/direct
  connect** — favor **loose coupling** over point-to-point links.
