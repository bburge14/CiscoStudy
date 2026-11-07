# Documentation, Monitoring & Logging

A network you can't see is a network you can't run. This lesson covers the three
things that make a network observable and accountable: the **documents** that
describe it, the **monitoring** that watches it live, and the **SNMP and logging**
that record what happened. There's little math here — it's about knowing which
artifact or tool answers which question.

## Network documentation

Good documentation turns "nobody knows how this works" into something a new engineer
can pick up. The exam expects you to match each document to what it captures.

**Diagrams:**

- **Physical diagram** — the actual cabling and hardware: which device plugs into
  which port, where cables run.
- **Logical diagram** — the flow of data: subnets, VLANs, IP addresses, routing.
  It ignores physical cabling.
- **Rack diagram** — a front view of a rack showing what occupies each **U**.
- **Floor plan / wiring diagram** — where drops, jacks and equipment sit in the
  building.

**Facilities and inventory:**

- **MDF (Main Distribution Frame)** — the building's main wiring room where the
  circuit enters and the core gear lives.
- **IDF (Intermediate Distribution Frame)** — a wiring closet on each floor that
  connects back to the MDF.
- **Asset inventory** — a record of every device: model, serial, owner, location,
  warranty. Needed for audits and life-cycle planning.
- **IPAM (IP Address Management)** — tracks which IP addresses and subnets are in
  use, so you don't hand out duplicates.

**Policies and agreements (know these acronyms):**

| Term | Meaning |
|------|---------|
| **SLA** | Service-Level Agreement — the uptime/response a provider promises |
| **MOU** | Memorandum of Understanding — a non-binding "we intend to" |
| **NDA** | Non-Disclosure Agreement — keep information secret |
| **AUP** | Acceptable Use Policy — how users may use the network |
| **SOP** | Standard Operating Procedure — step-by-step for a routine task |
| **BYOD** | Bring Your Own Device — policy for personal devices on the network |

> **A baseline is a documented record of "normal."** You capture typical CPU, link
> utilization and latency when things are healthy, so later you can tell whether
> today's numbers are a problem. Without a baseline, "the network is slow" has
> nothing to be measured against.

**Change management** ties into documentation: changes are requested, reviewed,
approved, scheduled in a maintenance window, and recorded — with a rollback plan if
they go wrong. Every change should update the diagrams it affects.

## Network monitoring: watching it live

Monitoring is how you learn about trouble *before* users call. There are a few
distinct **methods**, and the exam likes to ask which fits a need:

- **SNMP polling** — the monitor asks each device for counters (covered below).
- **Flow data (NetFlow / sFlow / IPFIX)** — the device reports *conversations*: who
  talked to whom, how much, on what ports. Great for "where is the bandwidth going?"
- **Packet capture (sniffing)** — grab the actual packets (with a tool like
  `tcpdump` or Wireshark) to inspect contents. The deepest view, but heavy.
- **Port mirroring / SPAN** — copies traffic from one switch port to another so a
  capture tool can see it.
- **Agent-based vs agentless** — an agent is software installed on the host that
  reports in; agentless monitoring reaches in over a protocol like SNMP or an API
  with nothing installed.
- **API polling** — modern gear exposes data through REST APIs that a dashboard
  pulls.

> **Flow data tells you *who and how much*; packet capture tells you *exactly what*.**
> Reach for flow to find the top talker, capture to read the actual payload.

**What to measure** — the performance metrics that come up repeatedly:

- **Bandwidth / throughput** — how much data the link can and does carry.
- **Latency** — delay, the time for a packet to get there (ms).
- **Jitter** — *variation* in latency; the killer for voice and video.
- **Packet loss** — packets that never arrived.
- **Uptime / availability** — often stated in "nines"; **99.999% ("five nines") is
  about 5 minutes of downtime per year.**

Environmental sensors (temperature, humidity, power) belong here too — a monitoring
system should alert on a hot closet or a failing UPS, not just on network counters.

## SNMP: polling devices for health

**SNMP (Simple Network Management Protocol)** is the workhorse for device monitoring.
A central **manager** polls many **agents** (the devices). Each agent exposes its
data as a tree of values called the **MIB**, and each specific value has an address
called an **OID**.

- The manager polls agents on **UDP 161**.
- Agents can also send unsolicited alerts on **UDP 162**.

Two kinds of unsolicited alert, and the difference is reliability:

> A **trap** is fire-and-forget — the agent sends it and never checks it arrived, so
> it can be lost. An **inform** is acknowledged and retransmitted until confirmed —
> reliable but heavier. Both ride **UDP 162**.

**Versions** matter for security:

- **v1 / v2c** protect access with a **community string** — a password sent in
  **clear text**. Anyone sniffing the wire can read it.
- **v3** adds real security with levels: `noAuthNoPriv`, `authNoPriv` (authentication
  only), and `authPriv` (authentication **and** encryption). Use **v3 authPriv** for
  anything real.

## Syslog and logging

Devices generate a constant stream of log messages. **Syslog** is the standard for
collecting them centrally, and it tags each message with a **severity 0–7**:

| # | Level | # | Level |
|--:|-------|--:|-------|
| 0 | Emergency | 4 | Warning |
| 1 | Alert | 5 | Notice |
| 2 | Critical | 6 | Informational |
| 3 | Error | 7 | Debugging |

> **Lower number = more severe.** 0 is a disaster, 7 is harmless debug chatter. When
> you set a logging level, the device sends that level **and everything more severe**
> (lower-numbered). The mnemonic "Every Awesome Cisco Engineer Will Need Ice-cream
> Daily" walks 0→7.

Logs are most useful **aggregated** into one place. A **SIEM (Security Information
and Event Management)** system collects logs from everywhere, correlates them, and
raises alerts — turning millions of lines into "these three events together mean an
attack." **Audit logs** specifically record who did what and when, which is what
compliance and incident investigations depend on. For any of this to be trustworthy,
every device's clock must agree — which is why **NTP** underpins the whole thing.

## On the exam

- Match documents to purpose: **physical** = cabling, **logical** = IP/VLAN flow,
  rack diagram = U layout, **IPAM** = address tracking, MDF/IDF = wiring rooms.
- Know the policy acronyms: **SLA, MOU, NDA, AUP, SOP, BYOD**.
- A **baseline** is recorded "normal" used to spot deviations. Change management =
  request, approve, window, document, rollback.
- Pick the monitoring method: **flow data** for who/how-much, **packet capture** for
  exact contents, SPAN to feed a sniffer, agent vs agentless.
- Metrics: bandwidth, latency, **jitter** (variation, hurts voice), packet loss,
  availability ("five nines" ≈ 5 min/yr).
- **SNMP**: manager polls agents on **161**, traps/informs on **162**; **trap =
  unreliable, inform = acknowledged**; use **v3 (authPriv)**, not v1/v2c community
  strings.
- **Syslog 0–7, lower = more severe**; a level sends itself and all worse. SIEM
  aggregates and correlates; audit logs record who-did-what; NTP keeps timestamps
  aligned.
