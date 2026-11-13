# Network Concepts: OSI, TCP/IP, Addressing & Ports

You can't secure a network you don't understand. This lesson covers the networking
fundamentals the CC exam expects: the **OSI model**, the **TCP/IP** protocols,
how devices are **addressed**, and the **well-known ports** that services listen
on. None of it is deep engineering — it's the shared vocabulary that the rest of
network security is built on.

## The OSI model: seven layers

> The **OSI (Open Systems Interconnection) model** is a seven-layer reference
> model that describes how data moves across a network, one layer at a time.

From top to bottom:

| # | Layer | Job (in brief) |
|---|-------|----------------|
| 7 | **Application** | Interfaces with user applications (HTTP, email) |
| 6 | **Presentation** | Formatting, encryption, compression |
| 5 | **Session** | Sets up and manages sessions/conversations |
| 4 | **Transport** | End-to-end delivery (TCP, UDP), ports |
| 3 | **Network** | Logical addressing and routing (IP addresses) |
| 2 | **Data Link** | Local delivery using MAC (hardware) addresses |
| 1 | **Physical** | The cables, signals, and bits on the wire |

A classic mnemonic (top to bottom) is **"All People Seem To Need Data
Processing."** The two layers you must nail for the exam are:

- **Layer 3 – Network:** a **router** operates here, forwarding packets between
  networks using **IP addresses** to choose the path.
- **Layer 2 – Data Link:** a traditional **switch** operates here, forwarding
  frames using **MAC (hardware) addresses**.

So: router = Layer 3 = IP addresses; switch = Layer 2 = MAC addresses. The TCP/IP
model is a simpler four-layer cousin (Application, Transport, Internet, Network
Access), but the seven-layer OSI model is the one most often tested.

## TCP vs. UDP: the two transport protocols

At Layer 4, two protocols carry your data, and choosing between them is a
reliability-versus-speed trade-off.

> **TCP** is **connection-oriented and reliable**: it sets up a connection,
> acknowledges received data, and retransmits what's lost. **UDP** is
> **connectionless and fast**: it just sends, with no setup and no guarantees.

- **TCP (Transmission Control Protocol)** — use it when delivery must be reliable
  and ordered (web pages, email, file transfers). Before any data flows, TCP
  establishes a connection with a **three-way handshake**: **SYN → SYN-ACK →
  ACK**.
- **UDP (User Datagram Protocol)** — use it when speed and low latency matter more
  than perfect delivery, and a few lost packets are tolerable, such as a live
  **voice-over-IP** call or video stream. UDP skips connection setup and
  retransmission.

Memory hook: TCP is a phone call (you connect, confirm, and acknowledge); UDP is
a postcard (you send it and hope it arrives).

## Ports: the doors services listen on

A single server can run many services at once; **ports** are the numbered doors
that keep their traffic separate. You should recognize a handful of **well-known
ports**:

| Port | Service | Notes |
|------|---------|-------|
| 21 | FTP | File transfer (control) |
| 22 | SSH | Secure remote administration |
| 23 | Telnet | Remote login — insecure, cleartext |
| 25 | SMTP | Sending email |
| **53** | **DNS** | Resolves domain names to IP addresses |
| 80 | HTTP | Web — unencrypted |
| **443** | **HTTPS** | Web — encrypted (TLS) |
| 3389 | RDP | Remote Desktop |

The two the exam emphasizes most: **HTTPS is port 443** (encrypted web traffic a
firewall must permit for secure sites) and **DNS is port 53**. Knowing the secure
versus insecure pairs also helps — HTTP (80) is cleartext while HTTPS (443) is
encrypted; Telnet (23) is cleartext while SSH (22) is encrypted.

## IP addressing

Every device on a network needs a logical address.

- **IPv4** addresses are **32 bits** long, written as four numbers like
  `192.168.10.10`. Thirty-two bits allows about 4.3 billion addresses — not
  enough for today's internet.
- **IPv6** addresses are **128 bits** long, written in hexadecimal groups, giving
  an effectively limitless supply of addresses.

### Private vs. public addresses

Some IPv4 ranges are reserved for **private** internal networks and are **not
routable on the public internet**:

- `10.0.0.0 – 10.255.255.255`
- `172.16.0.0 – 172.31.255.255`
- `192.168.0.0 – 192.168.255.255`

So an address like `192.168.10.10` is **private** — the kind your home or office
router hands out internally. Private addresses let many internal devices share
one public address and add a layer of separation from the internet.

## Helpful protocols: DHCP and DNS

Two protocols quietly make networks usable:

- **DHCP (Dynamic Host Configuration Protocol)** — automatically assigns IP
  addresses and other settings (gateway, DNS server) to devices when they join a
  network, so you don't configure each one by hand.
- **DNS (Domain Name System)** — resolves human-friendly domain names (like
  `example.com`) into the IP addresses machines actually use, running on port 53.
  Think of DNS as the internet's phone book.

## Exam focus

- The **OSI model has 7 layers**. A **router** works at **Layer 3 (Network, IP
  addresses)**; a **switch** works at **Layer 2 (Data Link, MAC addresses)**.
- **TCP** = reliable, connection-oriented, uses the **three-way handshake (SYN,
  SYN-ACK, ACK)**. **UDP** = fast, connectionless, tolerates loss (good for VoIP).
- **HTTPS = port 443**, **DNS = port 53**, HTTP = 80, SSH = 22. Know the common
  ones.
- **IPv4 = 32 bits**; **IPv6 = 128 bits**. `192.168.x.x` (and `10.x`,
  `172.16–31.x`) are **private**, non-internet-routable addresses.
- **DHCP** auto-assigns IP settings; **DNS** resolves names to IP addresses.
