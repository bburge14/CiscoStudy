# High Availability & Fault Tolerance

Resilient design begins with a blunt assumption: **everything fails eventually**, so
build so that no single failure takes down the application. The Well-Architected
Reliability pillar calls this removing single points of failure. On the exam you
will be handed a component that can die — an instance, an Availability Zone, a
database — and asked which AWS feature keeps serving users anyway. The toolkit is
Multi-AZ redundancy, elastic load balancing, and Auto Scaling.

## Spread across Availability Zones

An **Availability Zone (AZ)** is an isolated set of data centers within a Region.
Putting redundant copies in multiple AZs survives the loss of any one.

> **The reference pattern for a resilient web tier: an EC2 Auto Scaling group
> spanning multiple AZs behind an Application Load Balancer.** The load balancer
> spreads traffic; Auto Scaling replaces failed instances automatically; multiple
> AZs survive a zone outage.

### Elastic Load Balancing: pick the right type

| Load balancer | Layer | Best for |
|---------------|-------|----------|
| **Application Load Balancer (ALB)** | 7 (HTTP/S) | Path- and host-based routing to microservices |
| **Network Load Balancer (NLB)** | 4 (TCP/UDP) | Millions of req/s, ultra-low latency, a static IP |

- An **ALB** with listener rules routes to different target groups by URL path
  (`/api`, `/images`) and by Host header — the answer for a single endpoint
  fronting several microservices over HTTP.
- An **NLB** handles extreme request rates at the lowest latency for non-HTTP
  protocols and can expose a **static IP** — the answer when those are the stated
  needs.

Two settings the exam tests on load balancers:

- **Health check type = ELB** on an Auto Scaling group: if instances pass EC2
  status checks but the *application* hangs and returns errors, switch the group to
  use the load balancer's health checks so it replaces truly-unhealthy instances.
- **Deregistration delay (connection draining)**: when Auto Scaling removes an
  instance, this lets in-flight requests finish instead of being cut off.

## Auto Scaling beyond "replace failed instances"

Auto Scaling also matches capacity to demand. Know the policy types:

- **Target tracking** — hold a metric at a target (keep average CPU near 50%); the
  group adds or removes capacity automatically. The default dynamic choice.
- **Step scaling** — add a *different* amount depending on how far a metric breaches
  its threshold.
- **Scheduled scaling** — scale on a *known time pattern* (load rises every weekday
  at 08:00), putting capacity in place *before* the ramp.

## Resilient databases

Relational databases are stateful, so redundancy works differently from a
stateless web tier.

> **RDS Multi-AZ keeps a *synchronous* standby in another AZ and fails over to it
> automatically if the primary fails — this is for *high availability*, not read
> scaling.** **Read replicas** are *asynchronous* copies you point read traffic at
> to *offload reads* — this is for *scaling*, not automatic failover.

Do not confuse the two: "automatic failover, no manual intervention" → **Multi-AZ**;
"reporting queries are overwhelming the primary" → **read replicas**.

**Amazon Aurora** takes resilience further:

- Aurora replicates its storage **six ways across three Availability Zones** and can
  **automatically fail over** to an Aurora Replica. It supports up to 15 replicas
  that share the same storage.

**Amazon DynamoDB global tables** give a multi-Region, **multi-active** database —
local low-latency reads *and* writes in several Regions, surviving a full Region
failure. That is the answer when the requirement names multi-Region active-active
for a key-value workload.

**Amazon ElastiCache for Redis** supports **Multi-AZ with automatic failover**: if a
cache node or its AZ fails, a replica is promoted with minimal disruption.

## Surviving a Region failure with Route 53

DNS is part of resilience too. **Amazon Route 53 failover routing** with health
checks directs users to a standby site in another Region when health checks show
the primary is down — the DNS-level piece of a multi-Region recovery design.

## A worked example

A three-tier app needs to survive an AZ loss. Put the web/app tier in an **Auto
Scaling group across multiple AZs behind an ALB**, enable **RDS Multi-AZ** for the
database, and keep session state off the instances (in DynamoDB or ElastiCache) so
any instance can be replaced. If reporting later strains the database, add **read
replicas** rather than enlarging the primary.

## Exam focus

- Resilient stateless tier = **Auto Scaling group across AZs behind a load
  balancer**; it auto-replaces failed instances and spreads traffic.
- **ALB** = HTTP/S path- and host-based routing to microservices; **NLB** =
  TCP/UDP, millions of req/s, ultra-low latency, static IP.
- ASG **health check type ELB** catches hung apps that still pass EC2 checks;
  **deregistration delay** lets in-flight requests drain.
- Scaling policies: **target tracking** (hold a metric), **step** (scale by breach
  size), **scheduled** (known time pattern).
- **RDS Multi-AZ** = automatic synchronous failover (HA). **Read replicas** =
  asynchronous read scaling. Don't swap them.
- **Aurora** = 6 copies across 3 AZs with auto failover, up to 15 replicas.
  **DynamoDB global tables** = multi-Region multi-active. **ElastiCache for Redis
  Multi-AZ** = automatic replica promotion.
- **Route 53 failover routing + health checks** = send users to a standby Region
  when the primary is down.
