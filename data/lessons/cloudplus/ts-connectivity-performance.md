# Troubleshooting Connectivity & Performance

Two problem families dominate day-two cloud operations: things that **can't connect**
and things that **are too slow**. This lesson applies the troubleshooting
methodology to both — the network path that silently drops traffic, and the
resource bottleneck that drags response times down.

## Troubleshooting connectivity

When "it can't reach the service," work the path methodically from name resolution
to the final security check. In a software-defined network, the fault is almost
always a *configuration* rule, not a cut cable.

### Name resolution and routing

- **DNS resolution** — can the client even resolve the name to an address? Test
  with `nslookup` or `dig`. Wrong records, a stale cache, or the wrong resolver are
  classic causes; "the IP works but the name doesn't" points straight at DNS.
- **Routing** — is there a route to the destination? A **missing or wrong route
  table entry**, a private subnet with no path to its **NAT gateway**, or an
  absent **internet gateway** route will black-hole traffic. **Overlapping CIDR
  ranges** between peered networks or a VPN also break routing.
- **Public vs. private addressing** — an instance in a private subnet has no public
  IP; reaching it from outside requires a load balancer, bastion, or VPN. Confirm
  you're targeting the right address.

### Security rules and secure channels

- **Security groups and NACLs** — the most common cloud connectivity culprit. A
  **stateful security group** missing an inbound allow, or a **stateless NACL**
  that permits inbound but not the return traffic, silently drops packets. Check
  both layers, and both directions.
- **VPN / tunnel down** — a site-to-site tunnel can drop on a mismatched pre-shared
  key, phase/encryption-parameter mismatch, or a peer IP change.
- **TLS/certificate errors** — an expired, untrusted, or wrong-hostname certificate
  breaks HTTPS even when the network path is fine. Read the exact certificate error.
- **Load balancer health checks** — if backends are marked unhealthy, the balancer
  returns errors even though instances are "running." A failing health check (wrong
  path, wrong port, blocked by a security group) is a frequent hidden cause.

### Connectivity tools

Match the tool to the question: **`ping`** (reachability/latency, if ICMP is
allowed), **`traceroute`/`tracert`** (where along the path it stops), **`nslookup`/
`dig`** (DNS), **`telnet`/`curl`/`nc`** (is a specific *port* open and answering),
**`netstat`/`ss`** (local listeners and connections), and **`tcpdump`** (packet
capture when you must see the traffic itself). One subtle layer-3 issue to know:
an **MTU mismatch** (often with VPN/encapsulation) lets small packets through but
quietly breaks large transfers.

> Connectivity triage shortcut: **name → route → security rule.** Resolve the name
> (`dig`), confirm a route exists, then check security groups/NACLs **in both
> directions.** Most cloud "can't connect" tickets end at a security-group rule.

## Troubleshooting performance

Performance problems are about a **resource running out** or a **limit being hit**.
Start from the monitoring baseline and find the saturated resource.

### Find the bottleneck

- **CPU** — sustained high utilization means the instance is too small or the code
  is hot. Right-size up, scale out, or optimize.
- **Memory** — exhaustion causes swapping (which cripples performance) or
  out-of-memory kills. Memory-optimized instances or a leak fix are the levers.
- **Disk / storage I/O** — hitting a volume's **IOPS** or **throughput** cap
  throttles the app even when CPU is idle. Many "slow database" issues are really
  an under-provisioned disk; move to a higher-IOPS tier.
- **Network bandwidth** — a saturated link or an instance-size network cap limits
  transfer-heavy workloads.

### Limits, contention, and scaling

- **Throttling / rate limiting** — the platform is deliberately capping API calls
  or a service tier; the symptom is `429`/throttle errors, and the fix is backoff,
  a quota increase, or a higher tier — not more instances.
- **Connection limits** — a database or load balancer maxing out its connection
  pool rejects new work while CPU looks fine.
- **Noisy neighbor** — on shared (multitenant) hardware, another tenant's load
  steals resources; the fix may be a dedicated host or a different instance class.
- **Autoscaling not triggering** — the service is slow under load but never scaled
  out. Check the scaling policy's metric and threshold, the max-instance cap, and
  the cooldown — a too-high threshold or a maxed-out ceiling leaves you stuck at
  capacity.

### Fixing it

Right-size or scale the saturated resource, add **caching** or a **CDN** to offload
repeated work, tune slow database queries, and compare against the **performance
baseline** to confirm you actually improved things. Change one variable at a time —
raising CPU *and* IOPS *and* instance count at once tells you nothing about which
mattered, and often just raises the bill.

> Don't "throw instances at it" blindly. If the bottleneck is disk IOPS, a database
> connection cap, or API throttling, **adding instances won't help** and may make
> contention worse. Identify the saturated resource *first*.

## Exam focus

- Connectivity triage order: **DNS → routing → security rules.** "IP works, name
  doesn't" = **DNS**; black-holed traffic = **missing route / NAT / overlapping
  CIDR**; silently dropped packets = **security group / NACL** (check *both
  directions*; SGs are stateful, NACLs stateless).
- Also suspect **VPN tunnel down**, **certificate/TLS errors**, and **failing load
  balancer health checks** (backends look "running" but are marked unhealthy).
- Tools: **ping** (reachability), **traceroute** (where it stops), **dig/nslookup**
  (DNS), **telnet/curl/nc** (is a port open), **tcpdump** (packet capture); watch
  for **MTU** mismatch breaking large transfers.
- Performance = a **saturated resource or a hit limit**: **CPU, memory, disk
  IOPS/throughput, or network**. "Slow database" is often **under-provisioned
  disk IOPS**, not CPU.
- **Throttling/`429`** means a rate/quota limit (back off or raise the quota, not
  add instances); check **connection limits**, **noisy neighbors**, and
  **autoscaling that never triggered** (wrong metric/threshold, maxed ceiling).
- **Identify the saturated resource first** — blindly adding instances won't fix
  IOPS, connection, or throttling limits. Change **one variable at a time** against
  the **baseline**.
