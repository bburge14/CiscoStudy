# Network Models, Protocols & Ports

You can't secure a network you don't understand. Firewalls filter by port and
address, IDS signatures reference protocols, and attacks target specific layers —
so the models and the port map in this lesson are the reference you'll lean on
through the entire network domain. We'll build the OSI and TCP/IP models, contrast
TCP with UDP, and then drill the well-known ports and their secure replacements.

## The OSI model: seven layers

The **OSI (Open Systems Interconnection)** model is a conceptual seven-layer stack.
Data is **encapsulated** on the way down (each layer adds its header) and
**de-encapsulated** on the way up. Know each layer, what it does, and a sample
device or protocol — the exam asks "at which layer does X operate?"

| # | Layer | Job | Examples |
|---|-------|-----|----------|
| 7 | **Application** | Interface to apps | HTTP, DNS, SMTP |
| 6 | **Presentation** | Format, encrypt, compress | TLS, JPEG, ASCII |
| 5 | **Session** | Set up/maintain sessions | RPC, NetBIOS |
| 4 | **Transport** | End-to-end delivery | **TCP, UDP** |
| 3 | **Network** | Logical addressing & routing | **IP**, ICMP, routers |
| 2 | **Data Link** | Local delivery via MAC | Ethernet, switches, MAC |
| 1 | **Physical** | Bits on the wire | Cables, hubs, signals |

Two anchors the exam leans on:

> **Layer 3 (Network)** handles **logical IP addressing and routing** of packets
> *between* networks — this is where routers live. **Layer 2 (Data Link)** handles
> local delivery by **MAC address** — this is where a traditional Ethernet switch
> forwards frames.

A common mnemonic from layer 1 up: "**P**lease **D**o **N**ot **T**hrow **S**ausage
**P**izza **A**way." The **PDU** (unit of data) is named per layer: bits (L1),
**frames** (L2), **packets** (L3), **segments** (L4).

## The TCP/IP model

The practical **TCP/IP** model collapses OSI into four layers: **Application**
(OSI 5-7), **Transport** (OSI 4), **Internet** (OSI 3), and **Link/Network Access**
(OSI 1-2). It's the model the internet actually runs on; OSI is the teaching and
troubleshooting reference.

## TCP vs UDP

Both live at the Transport layer, but they behave oppositely, and the choice has
security relevance:

> **TCP (Transmission Control Protocol)** is **connection-oriented and reliable**:
> it uses a three-way handshake (SYN, SYN-ACK, ACK), sequences data, acknowledges
> receipt, and retransmits losses. **UDP (User Datagram Protocol)** is
> **connectionless** and fast, with no handshake, ordering, or guaranteed
> delivery.

Pick **TCP** when you need reliability (web, email, file transfer); pick **UDP**
when speed matters more than perfection (DNS queries, streaming, VoIP). The TCP
handshake is also what attackers abuse in a **SYN flood**, and the connectionless
nature of UDP makes it easy to **spoof** in amplification attacks.

## Addressing in brief

- **IPv4** uses 32-bit addresses; **private ranges** (10.0.0.0/8, 172.16.0.0/12,
  192.168.0.0/16) are not routable on the internet and rely on **NAT (Network
  Address Translation)** to reach it. NAT also provides a modest side benefit of
  hiding internal addresses.
- **IPv6** uses 128-bit addresses, solving exhaustion and building in features
  that were bolted onto IPv4.
- **MAC addresses** are 48-bit hardware addresses used at Layer 2 within a local
  segment.

## Well-known ports and their secure versions

Ports identify services at the Transport layer. Memorize the common ones — and
especially the **insecure/secure pairs**, because "replace the cleartext protocol
with its encrypted equivalent" is a staple recommendation.

| Port | Protocol | Notes |
|------|----------|-------|
| 20/21 | **FTP** | File transfer, **cleartext** |
| 22 | **SSH / SFTP / SCP** | Secure remote admin & transfer |
| 23 | **Telnet** | Remote admin, **cleartext — avoid** |
| 25 | **SMTP** | Sending email |
| 53 | **DNS** | Name resolution (UDP, TCP for zone transfers) |
| 69 | **TFTP** | Trivial FTP, no auth |
| 80 | **HTTP** | Web, **cleartext** |
| 88 | **Kerberos** | Authentication |
| 110 / 143 | **POP3 / IMAP** | Receiving email |
| 123 | **NTP** | Time sync (log correlation!) |
| 161/162 | **SNMP** | Network management (use **SNMPv3**) |
| 389 / 636 | **LDAP / LDAPS** | Directory (636 = over TLS) |
| 443 | **HTTPS** | **HTTP over TLS** — the default for secure web |
| 445 | **SMB** | Windows file sharing |
| 3389 | **RDP** | Remote Desktop |

> **HTTPS uses TCP port 443.** Cleartext-to-secure swaps to know: **Telnet(23) ->
> SSH(22)**, **HTTP(80) -> HTTPS(443)**, **FTP(21) -> SFTP(22) or FTPS**,
> **SNMPv1/2 -> SNMPv3**, **LDAP(389) -> LDAPS(636)**.

Security takeaway: any protocol that sends **credentials or data in cleartext**
(Telnet, FTP, HTTP, SNMPv1/2) can be sniffed off the wire and should be replaced
with its encrypted counterpart wherever possible.

## Exam focus

- OSI layers 1-7: Physical, Data Link, Network, Transport, Session, Presentation,
  Application. **L3 = IP addressing/routing (routers)**; **L2 = MAC/switching
  (switches)**. PDUs: frame (L2), packet (L3), segment (L4).
- **TCP = connection-oriented, reliable** (handshake, sequencing, retransmission);
  **UDP = connectionless, fast, best-effort.** Choose TCP for reliability, UDP for
  speed.
- **TCP/IP model** = Application, Transport, Internet, Link (OSI condensed).
- Know the port map, especially **HTTPS = 443**, and the cleartext->secure pairs:
  **Telnet->SSH**, **HTTP->HTTPS**, **FTP->SFTP/FTPS**, **SNMP->SNMPv3**,
  **LDAP->LDAPS**.
- Replace **cleartext** protocols (Telnet, FTP, HTTP, SNMPv1/2) with encrypted
  equivalents; **NTP** keeps clocks synced for log correlation.
