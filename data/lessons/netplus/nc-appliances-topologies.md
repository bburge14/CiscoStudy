# Appliances, Topologies & Cloud

This lesson is a tour of the *things* a network is built from — the boxes, the
shapes you wire them into, and the cloud model that increasingly replaces the boxes
with rented equivalents. None of it is math; it's vocabulary and knowing which tool
fits which job.

## Network appliances: the boxes and what each one does

Every appliance exists to solve one problem. The trick on the exam is matching the
device to the job and knowing which OSI layer it lives at.

| Appliance | Its job | Layer |
|-----------|---------|------:|
| Hub | Repeats signals to every port (obsolete, one collision domain) | 1 |
| Switch | Forwards frames by MAC address within a LAN | 2 |
| Router | Forwards packets between networks by IP | 3 |
| Firewall | Allows or blocks traffic by a rule set | 3–7 |
| Load balancer | Spreads client requests across many servers | 4–7 |
| IDS / IPS | Detects (IDS) or detects **and blocks** (IPS) attacks | 3–7 |
| Proxy | Makes requests on a client's behalf, can cache and filter | 7 |
| Wireless AP | Bridges Wi-Fi clients onto the wired LAN | 2 |
| WLC | Central controller that manages many APs | 2–3 |

A few distinctions the exam probes:

> **IDS vs IPS:** an IDS only *watches and alerts* — it sits out of band. An IPS sits
> *inline* and can *drop* the malicious traffic. If the question wants the attack
> stopped, not just logged, the answer is IPS.

> **Router vs Layer 3 switch:** both route between subnets. A router has fewer, slower
> ports and handles WAN links; a Layer 3 switch routes between VLANs at wire speed
> inside a building. Use the switch for lots of internal VLANs, the router for the
> edge.

Other appliances worth naming: a **load balancer** gives many servers one virtual
address and shares the load (and can do SSL offload and health checks); a **proxy**
sits in front of clients to cache and filter their outbound web traffic; a **content
delivery network (CDN)** caches content at the edge near users. On the modern exam
many of these appear as **virtual** appliances or cloud functions rather than
physical boxes — same job, software form.

## Topologies: the shapes you wire devices into

A topology is simply the map of how nodes connect. There's a *physical* topology
(the actual cabling) and a *logical* one (how data flows), and they can differ.

- **Star** — every device connects back to one central switch. The dominant LAN
  shape today. One cable fault isolates one device; a central switch failure takes
  down everything attached to it.
- **Mesh** — devices interconnect with many links. A **full mesh** connects every
  node to every other node (maximum redundancy, lots of cable); a **partial mesh**
  connects only the important ones. Common in WANs for resilience.
- **Bus** — all devices share one backbone cable (legacy; a single break splits the
  network).
- **Ring** — each device links to two neighbors forming a loop (legacy; used in some
  fiber backbones with dual rings for redundancy).
- **Point-to-point** — a single link between exactly two devices, like a WAN circuit.
- **Hybrid** — any mix of the above, which is what real networks actually are.

> Count the links in a full mesh with **n(n−1)/2**. Five sites fully meshed need
> 5×4/2 = **10** links. The exam likes this formula.

### Datacenter and campus designs

Two named architectures show up:

- **Three-tier (core / distribution / access)** — the classic campus hierarchy.
  Access layer connects end devices, distribution aggregates and applies policy,
  core moves traffic fast between distribution blocks. A **collapsed core** merges
  core and distribution into one layer for smaller sites.
- **Spine-and-leaf** — the modern datacenter design. Every **leaf** switch connects
  to every **spine** switch (but leaves don't connect to leaves, and spines don't
  connect to spines). Any server is a predictable two hops from any other, which
  suits the heavy east-west (server-to-server) traffic of virtualized datacenters.

## Cloud concepts: renting the network instead of owning it

The cloud replaces equipment you buy and rack with capacity you rent on demand.
There are two things the exam always tests: the **service models** (how much of the
stack the provider manages) and the **deployment models** (who the cloud is for).

**Service models — "as a Service":**

| Model | You manage | Provider manages | Example |
|-------|------------|------------------|---------|
| IaaS | OS, apps, data | The virtual hardware | Rent a VM and build it up |
| PaaS | Just your app and data | OS, runtime, hardware | A hosted app platform |
| SaaS | Nothing but your settings/data | Everything | Webmail, a CRM site |

> A one-line hook: **IaaS** you get bare infrastructure, **PaaS** you get a platform
> to deploy code onto, **SaaS** you just log in and use the finished software. The
> higher up you go, the less you manage.

**Deployment models — who it serves:**

- **Public** — shared provider infrastructure, open to any customer.
- **Private** — dedicated to one organization (on-prem or hosted).
- **Hybrid** — a mix of public and private, with connectivity between them.
- **Community** — shared by several organizations with common needs.

**Cloud building blocks you should recognize:**

- **VPC (Virtual Private Cloud)** — your own isolated, private network *inside* a
  public cloud, with its own subnets and routing.
- **NFV (Network Function Virtualization)** — running routers, firewalls and load
  balancers as software instances instead of dedicated hardware.
- **Elasticity / scalability** — capacity grows and shrinks automatically with
  demand, and you pay only for what you use.
- **Multitenancy** — many customers share the same physical infrastructure, kept
  logically separated.

**Getting to the cloud:** you reach cloud resources over the internet (often through
a **VPN**), or over a dedicated private circuit the providers call **Direct Connect**
or **ExpressRoute** for steady, private bandwidth that never touches the public
internet.

## On the exam

- Match the appliance to the job and layer: switch = L2/MAC, router = L3/IP,
  firewall filters by rules, load balancer spreads load, proxy fronts clients.
- **IDS detects, IPS detects and blocks (inline).** Pick IPS when traffic must be
  stopped.
- Recognize topologies by description: star (central switch), full vs partial mesh,
  point-to-point, and compute full-mesh links with **n(n−1)/2**.
- **Spine-and-leaf** is the datacenter answer (every leaf to every spine, two-hop,
  east-west traffic); three-tier core/distribution/access is the campus answer.
- Service models by who manages what: **IaaS → PaaS → SaaS**, less to manage as you
  rise. Deployment models: public, private, hybrid, community.
- Know **VPC** (isolated network in a public cloud), **NFV** (virtualized network
  functions), elasticity/scalability, and that Direct Connect is a private link to
  the cloud.
