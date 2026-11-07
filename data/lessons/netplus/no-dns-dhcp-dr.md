# DNS, DHCP & Disaster Recovery

Two of these topics are the quiet services that make a network usable day to day —
name resolution and automatic addressing. The third is what you lean on when things
go badly wrong. We'll do the two services first, then recovery planning.

## DNS: turning names into addresses

People remember `www.example.com`; computers need `93.184.216.34`. **DNS (Domain
Name System)** is the phone book that translates between them, running on **port 53**
(UDP for ordinary lookups, TCP for large transfers). It's a **hierarchy**: a resolver
asks a root server, which points to the top-level domain (`.com`), which points to the
domain's **authoritative** server, which gives the final answer.

Two roles to keep straight:

> A **recursive resolver** does the legwork — it chases the answer down the hierarchy
> on your behalf and caches it. An **authoritative server** holds the real records for
> a zone and gives the definitive answer. Your PC asks a resolver; the resolver asks
> the authoritative servers.

**Record types** are heavily tested. Learn what each maps:

| Record | Maps | Example use |
|--------|------|-------------|
| **A** | Name → IPv4 | `www` → 93.184.216.34 |
| **AAAA** | Name → IPv6 | `www` → 2001:db8::1 |
| **CNAME** | Name → another name (alias) | `ftp` → `www` |
| **MX** | Domain → mail server | routes email |
| **NS** | Domain → its name servers | delegation |
| **PTR** | IP → name (reverse lookup) | reverse DNS |
| **SOA** | Zone's authority info | serial, refresh timers |
| **TXT** | Arbitrary text | SPF/DKIM, domain verification |
| **SRV** | Service → host/port | locates services |

> **A = IPv4, AAAA = IPv6, CNAME = alias, MX = mail, PTR = reverse.** These five are
> near-certain to appear. A **forward** lookup goes name→IP (A/AAAA); a **reverse**
> lookup goes IP→name (PTR).

**Internal vs external DNS:** an internal server resolves private names for employees;
external (public) servers resolve your domain for the world. **DNSSEC** adds digital
signatures so a resolver can trust that a record wasn't forged.

## DHCP: handing out addresses automatically

**DHCP (Dynamic Host Configuration Protocol)** gives a device its IP address, mask,
default gateway and DNS server automatically, so nobody configures each host by hand.
It runs on **UDP ports 67 (server) and 68 (client).**

The handshake is four steps, remembered as **DORA**:

> **D**iscover → **O**ffer → **R**equest → **A**cknowledge. The client broadcasts a
> **Discover**; a server replies with an **Offer**; the client **Requests** that
> offer; the server sends an **Acknowledgment** and the lease is active.

Terms you must know:

- **Scope / pool** — the range of addresses a server can hand out for a subnet.
- **Lease** — how long a client keeps its address before it must renew.
- **Reservation** — a specific IP tied to a device's MAC, so it always gets the same
  address (common for printers and servers).
- **Exclusion** — addresses inside the scope the server must *not* give out (because
  they're assigned statically).
- **Options** — extras delivered with the address: option 3 = default gateway,
  option 6 = DNS servers, and so on.

> **DHCP relay (IP helper):** DHCP Discover is a broadcast, and routers don't forward
> broadcasts. So when the DHCP server is on a *different* subnet, you configure a
> **DHCP relay / `ip helper-address`** on the router to forward the request across.
> Without it, clients on remote subnets get no address.

Remember from the addressing lesson: a host that gets **no** DHCP answer falls back
to an **APIPA** address (`169.254.x.x`), which is your signal that DHCP failed.

## Disaster recovery: planning for the bad day

Disaster recovery (DR) is how a business keeps running — or gets back up fast — after
a failure, from a dead server to a flooded datacenter. Two metrics define the goals,
and they're constantly confused, so pin them down:

> **RTO (Recovery Time Objective)** = how *fast* you must be back up — the maximum
> tolerable **downtime**.
> **RPO (Recovery Point Objective)** = how much *data* you can afford to lose — the
> maximum age of the last good backup.
>
> Hook: RT**O** = **O**utage time you can tolerate; RP**O** = how far back your
> recovery **P**oint can be.

A one-hour RPO means you back up at least hourly; a one-hour RTO means you must
restore service within an hour. Related reliability numbers:

- **MTTR (Mean Time To Repair)** — average time to fix a failed component.
- **MTBF (Mean Time Between Failures)** — average time a repairable device runs
  between failures (higher is better).
- **MTTF (Mean Time To Failure)** — expected life of a non-repairable part.

### Backups

| Type | Backs up | Restore | Notes |
|------|----------|---------|-------|
| **Full** | Everything | Fast (one set) | Slow to take, big |
| **Incremental** | Changes since the **last backup** | Slow (needs the chain) | Small, fast backups |
| **Differential** | Changes since the **last full** | Medium | Grows until next full |
| **Snapshot** | Point-in-time image | Very fast | Common for VMs/storage |

A widely-cited guideline is the **3-2-1 rule**: keep **3** copies of data, on **2**
different media, with **1** copy **off-site**.

### Recovery sites and high availability

If a whole site goes down, you fail over to another. The three site types trade cost
against readiness:

- **Hot site** — a full running duplicate, ready in minutes. Most expensive.
- **Warm site** — hardware and connectivity in place, but data must be loaded; ready
  in hours.
- **Cold site** — just space and power; you bring and build everything. Cheapest,
  slowest.

**High availability (HA)** aims to avoid the outage in the first place through
redundancy and automatic **failover**:

- **Active-active** — all nodes serve traffic and share load; if one fails the others
  absorb it.
- **Active-passive** — one node serves while a standby waits to take over on failure.
- **Clustering** and **load balancing** spread work across nodes; **FHRP** protocols
  like **VRRP/HSRP** give hosts a redundant default gateway.

Finally, a DR plan is only real if it's **tested** — a **tabletop exercise** walks
the team through the plan on paper, and a full failover test proves it actually
works before the real disaster does.

## On the exam

- DNS is **port 53**; know records cold: **A (IPv4), AAAA (IPv6), CNAME (alias),
  MX (mail), PTR (reverse), NS, SOA, TXT, SRV.** Forward = name→IP, reverse = IP→name.
- Recursive resolver chases the answer; authoritative server holds the records.
  DNSSEC signs records.
- DHCP uses **UDP 67/68** and the **DORA** sequence. Know scope, lease, reservation,
  exclusion, options, and that a **relay/`ip helper-address`** forwards requests
  across subnets.
- **RTO = downtime you can tolerate; RPO = data loss you can tolerate.** Don't mix
  them up. Know MTTR, MTBF, MTTF.
- Backup types: full vs **incremental** (since last backup) vs **differential**
  (since last full) vs snapshot; the **3-2-1 rule**.
- Recovery sites: **hot (ready now) > warm > cold (cheapest, slowest)**. HA:
  active-active vs active-passive, failover, clustering; test with tabletop exercises.
