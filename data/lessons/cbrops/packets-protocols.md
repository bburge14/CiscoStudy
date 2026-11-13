# Packet & Session Analysis and Protocol Headers

Network intrusion analysis is the craft of reading traffic. That means two
skills: slicing captured traffic into the **conversations** that matter and
pivoting on them, and knowing the **protocol headers** well enough that the
fields themselves tell you a story. This lesson covers both — the analyst's
toolkit for the wire and the header fields that attacks leave fingerprints in.

## Sessions and the 5-tuple

A capture is a blur of packets until you group them into conversations. The key
that defines a conversation is the **5-tuple**.

> The **5-tuple** is the combination of **source IP, destination IP, source
> port, destination port, and transport protocol** that uniquely identifies a
> single network conversation.

The 5-tuple is the analyst's pivot. When one malicious conversation shows up, you
**filter every log source — firewall, proxy, NetFlow — on that shared 5-tuple**
to pull together every record of it and isolate the compromised host. Reading the
tuple also tells you roles at a glance: the **source** of an inbound attack is the
likely **attacker**, the **destination** the **victim**; a server on **port 443**
with a client on **port 51972** means HTTPS to a **client ephemeral port**. And
the destination port hints at the service and its risk before you read any
payload — **port 23 is Telnet**, a cleartext remote-access protocol whose
credentials are visible on the wire.

### Working a capture in Wireshark

- **Display filters** narrow a capture to what you care about. For example,
  `ip.addr == 10.0.0.5 && tcp.port == 443` shows only traffic to or from that
  host on HTTPS.
- **Follow TCP Stream / Export Objects** reassembles a TCP conversation and lets
  you **carve a transferred file back out** of the packets for inspection — the
  payoff of having full capture for a suspect flow.

### Where capture comes from: TAP and SPAN

To watch traffic you need a copy of it. A **network TAP** or a switch **SPAN
port** sends a **copy** of traffic to a monitoring tool without sitting in the
forwarding path. Because it is **passive**, it can observe but **cannot block** —
unlike an inline device. That is the trade-off: passive monitoring never drops
legitimate traffic but also can't stop an attack by itself.

A reminder from Unit 2 that recurs here: analysts keep **NetFlow** for broad,
long-term visibility of *all* flows and targeted **full packet captures** for
payload depth on *specific* suspect flows — breadth and depth, not one or the
other.

## Protocol headers, field by field

Attacks live in header fields. You don't need to memorize every bit, but you must
know what the important fields do and how they're abused.

### Ethernet (Layer 2)

The **Ethernet frame header** operates at **Layer 2**, delivering a frame between
devices on the same local segment using **source and destination MAC addresses**.
MACs are local; they change at every hop, unlike IP addresses.

### IPv4 (Layer 3)

| Field | Purpose | Analyst angle |
|-------|---------|---------------|
| **TTL (Time To Live)** | Each router **decrements** it; packet is discarded at 0 | Limits a packet's lifetime so it can't loop forever; `traceroute` exploits it |
| **Protocol** | Names the encapsulated transport | **6 = TCP**, 17 = UDP, 1 = ICMP |
| **Identification, Flags (More Fragments), Fragment Offset** | Let a receiver reassemble fragments | Abused in **fragmentation-based IDS evasion** |

### TCP (Layer 4, connection-oriented)

TCP is reliable and stateful, and its **control flags** drive everything:

> TCP's **control flags** field (**SYN, ACK, FIN, RST**, plus PSH/URG) governs
> connection setup and teardown. The normal **three-way handshake** is **SYN →
> SYN-ACK → ACK**.

- A flood of **SYN** packets that never complete the handshake is the signature
  of a **SYN flood** (an availability attack).
- A **RST** flag most commonly signals an **abrupt reset/refusal** — a closed
  port or a forced teardown. Many RSTs in reply to connection attempts suggest
  scanning against closed ports.

### UDP (Layer 4, connectionless)

> **UDP is connectionless** — there is **no handshake, no sequence numbers, no
> ACKs**. Its header is minimal: just source/destination **ports, length, and
> checksum.**

That simplicity matters to an analyst: UDP has no connection state to reason
about, which is part of why it's used for spoofing and amplification attacks.

### ICMP (control messages)

ICMP carries diagnostics, and two utilities you must map to their messages:

- **`ping`** sends an **ICMP Echo Request (Type 8)** and expects an **Echo Reply
  (Type 0)** — confirming basic reachability.
- **`traceroute`** sends packets with **increasing TTL**; each router whose TTL
  reaches zero returns an **ICMP Time Exceeded (Type 11)**, revealing the path
  hop by hop.

Because ICMP is often permitted through, it's also a favorite **tunneling**
channel for covert C2 — a connection back to the evasion techniques of Unit 2.

## Putting the wire together

A capable analyst reads a capture top-down: identify the **conversation**
(5-tuple), judge roles and risk from the **addresses and ports**, then drop into
the **headers** to confirm what's happening — SYNs with no handshake, abnormal
TTLs, fragmentation, odd ICMP. When payload depth is needed and available,
**Follow TCP Stream** reconstructs the exchange. The headers are not trivia; they
are the evidence.

## Exam focus

- The **5-tuple** = src IP, dst IP, src port, dst port, protocol — it uniquely
  identifies a conversation and is the **pivot** to correlate records across
  firewall/proxy/NetFlow logs. **Source = attacker, destination = victim** for an
  inbound attack.
- **Wireshark**: display filter example `ip.addr == x && tcp.port == 443`;
  **Follow TCP Stream / Export Objects** carves out transferred files. **TAP/SPAN**
  = passive copy, **cannot block**.
- **Ethernet** = Layer 2 via **MAC** addresses. **IPv4 TTL** is decremented per
  router (loop protection; used by traceroute); **Protocol 6 = TCP**;
  **Identification/Flags/Fragment Offset** enable reassembly and enable
  fragmentation evasion.
- **TCP** flags SYN/ACK/FIN/RST; handshake **SYN → SYN-ACK → ACK**; many SYNs =
  **SYN flood**; **RST** = reset/refusal. **UDP** is connectionless (no
  handshake/seq/ACK).
- **ping** = ICMP Echo Request (8)/Reply (0); **traceroute** relies on **ICMP
  Time Exceeded (11)**. **Telnet = port 23** (cleartext).
