# Network Attacks

To defend a network you have to know how it gets attacked. This lesson is a field
guide to the attacks an SSCP must recognize by their description — the exam rarely
names the attack for you; it describes the behavior and asks you to identify it.
We'll group them by what the attacker is trying to do: intercept traffic, deny
service, impersonate, or steal credentials.

## Interception and on-path attacks

Many attacks aim to get *between* two communicating parties. On a local network,
the classic enabler is **ARP poisoning**:

> **ARP poisoning (ARP spoofing)** sends forged ARP replies on the LAN that map the
> **attacker's MAC address to another host's IP** — typically the default
> gateway's. Victims then send their traffic to the attacker instead of the real
> gateway.

Once traffic is flowing through the attacker, they can mount a **man-in-the-middle
(on-path) attack**:

> A **man-in-the-middle / on-path** attacker secretly relays and can read or alter
> traffic between two hosts that still believe they're talking directly to each
> other. ARP poisoning is one common way to achieve the position.

Related interception attacks:

- **DNS poisoning / spoofing** — corrupting DNS responses or cache so a name
  resolves to the attacker's IP, silently redirecting victims.
- **Eavesdropping / sniffing** — passively capturing traffic, especially
  devastating against **cleartext** protocols (Telnet, HTTP, FTP).
- **Session hijacking** — stealing a valid session token/cookie to take over an
  authenticated session.
- **Replay attack** — capturing valid traffic (e.g., an authentication exchange)
  and re-sending it later to impersonate; **timestamps/nonces** defeat it.

## Denial-of-service attacks

Instead of stealing data, these attacks destroy **availability**:

> A **Denial-of-Service (DoS)** attack overwhelms a system so legitimate users
> can't reach it. A **Distributed Denial-of-Service (DDoS)** does the same from
> **many compromised computers at once** — a **botnet** of thousands of hosts
> directed by the attacker — making it far harder to block.

Know the common flavors:

| Attack | Mechanism |
|--------|-----------|
| **SYN flood** | Floods half-open TCP connections, exhausting the connection table |
| **Amplification/reflection** (e.g., DNS, NTP) | Spoofs the victim's IP so small requests trigger huge replies aimed at the victim |
| **Smurf** | Spoofed ICMP broadcast so replies flood the victim (classic amplification) |
| **Botnet** | Network of compromised "zombie" hosts controlled via **command-and-control (C2)** |

The signature of a DDoS on the exam: a service becomes unreachable under a flood of
traffic **originating simultaneously from thousands of different sources**.

## Spoofing and rogue devices

- **IP/MAC spoofing** — forging a source address to impersonate a trusted host or
  evade filters.
- **MAC flooding** — overwhelming a switch's MAC table so it "fails open" and
  floods frames to all ports, enabling sniffing.
- **VLAN hopping** — tricking a switch into forwarding frames across VLANs the
  attacker shouldn't reach (via double-tagging or forged trunk negotiation).
- **Rogue access point / evil twin** — an unauthorized or impostor Wi-Fi AP that
  lures clients to connect so the attacker can intercept their traffic.

## Credential attacks

Passwords remain a prime target:

| Attack | How it works |
|--------|--------------|
| **Brute force** | Tries every possible combination until one works |
| **Dictionary** | Tries lists of likely passwords/common words |
| **Password spraying** | Tries a few common passwords across *many* accounts to dodge lockout |
| **Credential stuffing** | Reuses username/password pairs leaked from other breaches |
| **Rainbow table** | Uses precomputed hash tables to reverse unsalted password hashes |
| **Pass-the-hash** | Reuses a captured password hash to authenticate without cracking it |

The defenses tie back to earlier lessons: **salting** defeats rainbow tables,
**account lockout** slows brute force, **MFA** blunts stolen passwords, and
**unique passwords** limit credential stuffing.

## Application-adjacent attacks to recognize

The network often carries attacks aimed at applications — you should at least
recognize **SQL injection** (malicious input that manipulates a database query),
**cross-site scripting (XSS)** (injecting scripts into pages viewed by others),
and **cross-site request forgery (CSRF)** (tricking a browser into sending
unwanted authenticated requests). The common root cause is **failing to validate
and sanitize input**.

## A few more to recognize

The exam reaches for these variants, so match them by description:

| Attack | Description |
|--------|-------------|
| **Downgrade attack** | Forces a connection to a weaker, breakable protocol version (e.g., SSL stripping to drop HTTPS down to HTTP) |
| **Typosquatting** | Registers look-alike domains (`exampel.com`) to catch mistyped traffic |
| **Wardriving** | Driving around to map and find vulnerable wireless networks |
| **DNS tunneling** | Smuggles data or C2 traffic inside DNS queries to evade filtering |
| **Zero-day** | Exploits a vulnerability with no patch yet available |

The defensive lesson running through all of them: enforce **encryption
everywhere** (so downgrade and sniffing fail), **validate and sanitize input** (so
injection fails), **authenticate endpoints** (so spoofing and evil twins fail), and
**monitor** for the anomalies these attacks produce. Most network attacks exploit
either cleartext, trust, or unvalidated input — remove those and the attack surface
shrinks dramatically.

## Exam focus

- **ARP poisoning** = forged ARP replies mapping the **attacker's MAC to another
  host's IP** (often the gateway); it's a common way to set up a **man-in-the-
  middle / on-path** attack (silently relaying/altering traffic).
- **DoS** overwhelms a service; **DDoS** does it from **thousands of compromised
  hosts (a botnet)** via **C2** — the tell is a flood "from many sources at once."
  Know **SYN flood** and **amplification/reflection**.
- Recognize **DNS spoofing**, **session hijacking**, **replay** (beaten by
  nonces/timestamps), **MAC flooding**, **VLAN hopping**, and **evil twin/rogue
  AP** by their descriptions.
- Credential attacks: **brute force, dictionary, password spraying, credential
  stuffing, rainbow tables, pass-the-hash.** Defenses: **salting, lockout, MFA,
  unique passwords.**
- Application attacks (**SQLi, XSS, CSRF**) stem from **poor input validation**.
