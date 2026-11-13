# Storage & Network Deployment

Compute does the work, but it needs somewhere to keep data and a network to reach
the world. This lesson covers deploying the two supporting pillars: **storage** —
the right type, tier, and protection for the data — and the **virtual network**
that connects everything and controls what can talk to what.

## Storage types

Cloud storage comes in three fundamentally different shapes. Choosing the wrong
one is a common design mistake.

| Type | Access unit | Interface | Use it for |
|------|-------------|-----------|------------|
| **Block** | Fixed-size blocks (looks like a raw disk) | Attached as a volume (iSCSI) | Boot disks, databases, any app that wants a filesystem |
| **File** | Files in a shared hierarchy | Network shares (NFS, SMB/CIFS) | Shared drives, lift-and-shift apps needing a POSIX/Windows share |
| **Object** | Whole objects + metadata, flat namespace | HTTP(S) API | Backups, media, logs, static web content, data lakes |

> The quick test: if an app expects a **disk**, use **block**; if several hosts
> need a **shared folder**, use **file**; if you're storing huge numbers of
> **unstructured blobs** reached by API, use **object**.

Object storage scales almost without limit and is cheap, but you can't mount it as
a filesystem or run a database on it directly.

## Storage tiers and performance

Not all data deserves the same (expensive) fast storage. Providers offer **tiers**
priced by how quickly and often you access data:

- **Hot** — frequently accessed, lowest latency, highest storage cost.
- **Cool / infrequent access** — cheaper to store, small retrieval fee, for data
  touched occasionally.
- **Cold / archive** — cheapest storage, but retrieval can take minutes to hours
  and costs more. For long-term retention and compliance.

**Lifecycle policies** move objects automatically between tiers as they age (hot →
cool → archive → delete), which is a major cost lever.

Performance is measured in **IOPS** (operations per second — matters for
databases and random I/O) and **throughput** (MB/s — matters for large sequential
transfers). You provision volumes to hit a target; SSD-backed volumes serve high
IOPS, HDD-backed volumes serve cheap bulk throughput.

## Protecting stored data

- **RAID** combines disks for performance and/or redundancy. Know the common
  levels: **RAID 0** stripes for speed with *no* redundancy; **RAID 1** mirrors
  for redundancy; **RAID 5** stripes with one parity disk (survives one failure);
  **RAID 6** uses two parity disks (survives two); **RAID 10** mirrors *and*
  stripes for both speed and redundancy.
- **Replication** keeps copies in other zones or regions. **Synchronous**
  replication writes to both locations before acknowledging (zero data loss, added
  latency); **asynchronous** acknowledges locally and copies after (lower latency,
  small risk of loss).
- **Snapshots** are point-in-time copies of a volume, the basis for backups and
  fast rollback.
- **Ephemeral vs. persistent** — ephemeral (instance) storage vanishes when the
  instance stops; persistent volumes survive independently. Never put data you
  care about on ephemeral storage.

A **CDN (content delivery network)** caches content at edge locations near users —
strictly speaking a delivery optimization, but it's how static and media content
is "stored" close to the consumer to cut latency and origin load.

## Deploying the virtual network

Cloud networking is **software-defined**: you build a private virtual network and
define its behavior with configuration, not cables.

- A **VPC / virtual network (VNet)** is your isolated private network in the
  cloud, defined by a **CIDR** address range (e.g., `10.0.0.0/16`).
- **Subnets** carve the VPC into segments. A **public subnet** has a route to an
  **internet gateway**; a **private subnet** does not, and reaches out only
  through a **NAT gateway** (outbound only, nothing inbound).
- **Route tables** decide where traffic goes; **peering** or a **transit gateway**
  connects VPCs to each other.

### Controlling traffic

Two filtering layers, frequently confused:

> **Security groups** are *stateful* firewalls attached to an instance/interface:
> allow a flow in and the return traffic is automatically allowed. **Network ACLs
> (NACLs)** are *stateless* filters at the subnet boundary: you must permit both
> directions explicitly.

Security groups typically allow-list by port and source; they're the primary
instance-level control. NACLs add a coarse subnet-level guard.

### Connecting and distributing

- **Load balancers** spread traffic across backends. A **Layer 4** balancer routes
  by IP/port (fast, protocol-agnostic); a **Layer 7** balancer understands HTTP and
  can route by URL path, host, or header, and terminate TLS.
- **DNS** maps names to addresses; cloud DNS adds health-checked and
  latency/geo-based routing.
- **Hybrid links** — a **site-to-site VPN** tunnels over the internet (encrypted,
  cheaper, variable performance); a **direct connect / private interconnect** is a
  dedicated circuit (consistent latency, higher cost) for heavy or sensitive
  traffic.

## Exam focus

- **Block = a disk (boot, databases); file = a shared folder over NFS/SMB; object
  = API-accessed blobs (backups, media, static content).** Object scales huge but
  can't be mounted as a filesystem.
- Storage **tiers**: hot (frequent, pricey) → cool → cold/archive (cheap store,
  slow/costly retrieval). **Lifecycle policies** age data down tiers to save money.
  **IOPS** for random/database I/O, **throughput** for big sequential transfers.
- **RAID 0** = stripe/no redundancy, **1** = mirror, **5** = single parity, **6** =
  double parity, **10** = mirror + stripe. **Synchronous** replication = no data
  loss + latency; **asynchronous** = faster + small loss risk.
- **Security groups are stateful** (return traffic auto-allowed, instance level);
  **NACLs are stateless** (both directions explicit, subnet level).
- **Public subnet → internet gateway; private subnet → NAT gateway (outbound
  only).** **L4** load balancer routes by IP/port; **L7** routes by HTTP content and
  can terminate TLS. **VPN** = encrypted over internet; **direct connect** =
  dedicated private circuit.
