# OSI Model, Ports & Protocols

Almost every other topic on this exam gets explained in terms of the OSI model and
the port numbers that go with it. Learn these two things well now and the rest of
the course keeps paying you back. We'll take the layers first, then the ports, then
the three ways traffic can be addressed.

## The OSI model: a stack of seven jobs

When two computers talk, a lot has to happen: the data has to be formatted, given
addresses, broken into pieces, pushed onto a wire, and put back together at the far
end. The OSI model is just a way of splitting that work into **seven layers**, each
with one job, stacked on top of each other. Data travels *down* the stack on the
sender and back *up* on the receiver.

Here they are from top to bottom, with the number everyone refers to them by:

| # | Layer        | Its one job                                   | Example |
|--:|--------------|-----------------------------------------------|---------|
| 7 | Application  | The program the user actually touches         | HTTP, DNS |
| 6 | Presentation | Formatting, encryption, compression           | TLS, JPEG |
| 5 | Session      | Starting, keeping and ending conversations    | RPC |
| 4 | Transport    | End-to-end delivery, ports, TCP vs UDP        | TCP, UDP |
| 3 | Network      | Logical addressing and routing between networks | IP, ICMP |
| 2 | Data Link    | Local delivery on one link, MAC addresses, frames | Ethernet, switches |
| 1 | Physical     | The actual signal: copper, fiber, radio       | cables, 1s and 0s |

The time-honored way to remember them top to bottom is "**A**ll **P**eople **S**eem
**T**o **N**eed **D**ata **P**rocessing." Bottom to top, flip it: "**P**lease **D**o
**N**ot **T**hrow **S**ausage **P**izza **A**way."

> **Burn these three into memory, because the exam leans on them constantly:**
> Layer 2 uses **MAC** addresses and switches; Layer 3 uses **IP** addresses and
> routers; Layer 4 uses **port numbers** and is where TCP and UDP live.

A quick way to place a device or problem: if it deals with a MAC address it's
Layer 2, an IP address Layer 3, a port number Layer 4. A switch is a Layer 2 device,
a router is Layer 3, and a plain cable or a signal problem is Layer 1.

### The unit of data changes names per layer

As data moves down the stack, each layer wraps it in its own header, and the result
gets a different name. This naming shows up in questions:

- Layer 4 (transport) — a **segment** (TCP) or **datagram** (UDP)
- Layer 3 (network) — a **packet**
- Layer 2 (data link) — a **frame**
- Layer 1 (physical) — **bits**

That wrapping is called **encapsulation** on the way down and **de-encapsulation**
on the way back up.

## Ports: the "door number" at Layer 4

An IP address gets traffic to the right *computer*. But that computer is running a
browser, an email client, a remote-desktop session — all at once. A **port number**
is the extra piece that says *which program* on that machine the traffic is for.
Think of the IP address as the street address of an apartment building and the port
as the specific apartment number.

Ports run 0–65535. The low ones (0–1023) are the **well-known** ports tied to
standard services, and those are the ones worth memorizing. Here is the core set the
exam expects on sight:

| Port | Protocol | What it does | TCP/UDP |
|-----:|----------|--------------|---------|
| 20/21 | FTP | File transfer (20 data, 21 control) | TCP |
| 22 | SSH / SFTP / SCP | Encrypted remote CLI and file copy | TCP |
| 23 | Telnet | Remote CLI, **unencrypted** (avoid) | TCP |
| 25 | SMTP | Sending mail between servers | TCP |
| 53 | DNS | Name-to-IP lookups | UDP (and TCP) |
| 67/68 | DHCP | Automatic IP addressing | UDP |
| 69 | TFTP | Trivial file transfer, no login | UDP |
| 80 | HTTP | Web, unencrypted | TCP |
| 110 | POP3 | Downloading mail | TCP |
| 123 | NTP | Clock synchronization | UDP |
| 143 | IMAP | Reading mail, kept on server | TCP |
| 161/162 | SNMP | Device monitoring (162 = traps) | UDP |
| 389 | LDAP | Directory lookups | TCP |
| 443 | HTTPS | Web, encrypted with TLS | TCP |
| 445 | SMB | Windows file sharing | TCP |
| 3389 | RDP | Remote Desktop to a Windows GUI | TCP |

A few deserve special attention because they travel in pairs or get confused:

> **DNS is 53. DHCP is 67 and 68** — the server listens on 67, the client on 68.
> A quick hook: a host can't find itself, so it asks for an address on 67/68, then
> looks names up on 53.

> **SSH (22) is the encrypted replacement for Telnet (23).** Any time a question
> offers both, SSH is the secure answer. Likewise **HTTPS (443)** replaces
> **HTTP (80)**, and **RDP (3389)** is the Windows remote-desktop protocol.

### Secure vs insecure pairs

Several protocols come as a plaintext version and an encrypted upgrade. The exam
loves to ask you to pick the secure one:

- Telnet 23 → **SSH 22**
- HTTP 80 → **HTTPS 443**
- FTP 20/21 → **SFTP (over SSH, 22)** or FTPS
- SNMPv1/v2c → **SNMPv3** (adds authentication and encryption)
- LDAP 389 → **LDAPS 636**

## Protocols below the ports: ICMP, TCP and UDP

Not everything uses a port. **ICMP** is the Layer 3 helper protocol that `ping` and
`traceroute` ride on — it carries error and diagnostic messages, not application
data, so it has no port number at all.

At Layer 4 the two choices are **TCP** and **UDP**:

- **TCP** sets up a connection first (the three-way handshake: SYN, SYN-ACK, ACK),
  numbers every byte, and resends anything lost. Reliable but slower. Used for the
  web, email, file transfer — anything where every byte must arrive.
- **UDP** just fires packets off with no handshake and no retransmission. Fast and
  lightweight, with no guarantee. Used for DNS, DHCP, VoIP and video, where speed
  matters more than perfection and a lost packet isn't worth waiting for.

> **TCP = reliable and ordered, UDP = fast and best-effort.** If a question stresses
> accuracy, think TCP; if it stresses speed or real-time media, think UDP.

## Traffic types: who is the packet for?

The last concept in this lesson is *how many* recipients a packet is aimed at. The
destination address decides this, and there are four named patterns:

- **Unicast** — one sender to **one** specific receiver. The everyday case: your PC
  loading one web server. One-to-one.
- **Broadcast** — one sender to **everyone** on the local network at once, using the
  special address `255.255.255.255` (or the subnet's broadcast). One-to-all. ARP and
  the first step of DHCP use it. Broadcasts stay inside their own broadcast domain —
  routers don't forward them. **IPv4 only.**
- **Multicast** — one sender to a **group** of interested receivers, and only those
  who opted in. One-to-many. Used for streaming video and routing protocols. IPv4
  multicast lives in the `224.0.0.0/4` range.
- **Anycast** — one address shared by **several** servers; the network delivers to
  the **nearest** one. One-to-nearest. This is how large DNS services answer you
  from a server close by.

> A memory hook: uni = **one**, broad = **all**, multi = **many (who joined)**,
> any = **the closest one**.

A related idea is the **broadcast domain** versus the **collision domain**. Every
port on a hub shares one collision domain; a switch gives each port its own
collision domain but all its ports share one broadcast domain; a **router** breaks
up broadcast domains. That's why segmenting with routers (or VLANs) keeps broadcast
chatter from flooding the whole network.

## On the exam

- Know the seven layers **in order and by number**, and that L2 = MAC/switch,
  L3 = IP/router, L4 = ports/TCP-UDP. Expect "at which layer does X operate?"
- Match the data unit to the layer: segment (4), packet (3), frame (2), bits (1).
- Memorize the well-known ports cold — especially **SSH 22, Telnet 23, DNS 53,
  DHCP 67/68, HTTP 80, HTTPS 443, RDP 3389, SNMP 161/162**. Expect "which port
  must be open?" and "pick the secure protocol" questions.
- When asked to replace an insecure protocol, choose its encrypted partner
  (Telnet→SSH, HTTP→HTTPS, FTP→SFTP, SNMPv2c→SNMPv3).
- TCP is reliable/connection-oriented (handshake, retransmit); UDP is fast and
  connectionless. DNS, DHCP, VoIP and video favor UDP.
- Classify traffic correctly: unicast one-to-one, broadcast one-to-all (IPv4 only,
  stopped by routers), multicast one-to-group, anycast one-to-nearest.
