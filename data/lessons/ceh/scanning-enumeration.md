# Scanning Networks & Enumeration

Footprinting told you a target *exists*. Scanning and enumeration tell you how to
*reach* it: which hosts are alive, which ports are open, which services sit behind
them, and which accounts and shares those services expose. On the exam this is the
most tool-and-port-heavy material in the whole track, so this lesson leans into the
recognition facts — Nmap scan types, port numbers, and the protocols that give up
too much.

## Scanning: finding hosts, ports and services

> **Scanning is the active discovery of live hosts, open ports, running services
> and operating systems on a target network.**

Scanning builds on the TCP three-way handshake (**SYN → SYN/ACK → ACK**). By
sending crafted packets and watching the response flags, a scanner infers the
state of each port: **open**, **closed**, or **filtered** (no clear answer,
usually a firewall).

### Nmap scan types to recognize

**Nmap** is the dominant scanner, and CEH expects you to match the flag to the
behavior:

| Option | Scan | Behavior |
|--------|------|----------|
| `-sn` | Host discovery ("ping sweep") | Finds live hosts, **scans no ports** |
| `-sS` | TCP SYN ("half-open") | Sends SYN, gets SYN/ACK, replies RST — never finishes the handshake; the default stealthy scan |
| `-sT` | TCP connect | Completes the full handshake (used without raw-packet privileges) |
| `-sU` | UDP scan | Probes UDP services (slower, no handshake) |
| `-sV` | Version detection | Identifies the service and version on a port |
| `-O` | OS detection | Fingerprints the operating system |
| `-A` | Aggressive | Combines version, OS, scripts and traceroute |
| `-Pn` | No ping | Skip host discovery; treat hosts as up |
| `-p` | Port spec | Choose ports, e.g. a range or a list |

You will also see **NULL, FIN and Xmas** scans — probes that send unusual TCP flag
combinations to tease a response out of a target and infer filtering. The key idea
to remember: a **SYN scan is "half-open"** because it never completes the
handshake, which historically made it quieter than a full connect scan.

### Defending against scanning

- **Firewalls and ACLs** to drop or filter probes and expose only needed ports.
- **IDS/IPS** to detect the tell-tale pattern of a sweep.
- **Rate limiting** and connection throttling to slow mass probing.
- **Close or disable unused ports and services** — the smallest surface wins.

## Enumeration: extracting the details

Once you know a service is open, **enumeration** actively connects to it to pull
back specifics — user accounts, machine names, shares, groups and configuration.

> **Enumeration is the active extraction of detailed information (usernames,
> shares, services, config) by directly querying a service after it has been
> found. It is noisier and more intrusive than scanning.**

### Services that leak the most

- **NetBIOS / SMB** — Windows file sharing. Modern SMB rides on **TCP 445** (older
  NetBIOS used 137–139). Tools such as **enum4linux** list shares, users and
  groups over SMB. **Null sessions** (unauthenticated connections) historically
  gave this away for free.
- **SNMP** — network management on **UDP 161/162**. Devices ship with default
  **community strings** (`public` for read, `private` for read-write). An attacker
  who guesses `public` can read a device's entire configuration and interface list.
- **LDAP** — directory service on **389** (636 for LDAPS); can reveal users,
  groups and organizational structure.
- **SMTP** — mail on **25**; the `VRFY` and `EXPN` verbs can confirm whether a
  user account exists.
- **DNS** — a permitted **zone transfer (AXFR)** on **53** dumps internal records.
- **NTP** — time service on **123** can reveal hosts it talks to.

### Common ports worth memorizing

| Port | Service | Port | Service |
|------|---------|------|---------|
| 21 | FTP | 161/162 | SNMP (UDP) |
| 22 | SSH | 389 | LDAP |
| 23 | Telnet | 443 | HTTPS |
| 25 | SMTP | 445 | SMB |
| 53 | DNS | 1433 | MS SQL |
| 80 | HTTP | 3306 | MySQL |
| 123 | NTP | 3389 | RDP |

### Defending against enumeration

- **Change default SNMP community strings** and move to **SNMPv3** with
  authentication and encryption; disable SNMP where it is not needed.
- **Disable null sessions** and restrict anonymous SMB/LDAP access.
- **Turn off unneeded verbs** (SMTP `VRFY`/`EXPN`) and services.
- **Disable DNS zone transfers** to untrusted hosts.
- Apply the principle of least function: if a service does not need to answer, it
  should not be reachable.

## How the pieces fit

Footprinting is passive map-making. Scanning is knocking on doors to see which are
open. Enumeration is reaching through an open door to ask "who lives here, and what
do you have?" Each phase narrows the target and raises the noise level — and each
has a matching defense in reducing exposed services and locking down defaults.

## From noise to knowledge

Scanning and enumeration together answer one question: "what can I reach, and what
will it tell me?" The trade-off is always stealth versus completeness — aggressive
options (`-A`, fast timing) gather more but light up every IDS, while slow, targeted
probes stay quiet but take longer. For a defender, that same noise is the
opportunity: a sweep across many ports and hosts is one of the easiest patterns to
detect and alert on.

## Exam focus

- **`-sn`** = host discovery only (no ports); **`-sS`** = stealthy **half-open**
  SYN scan and the privileged default; **`-sT`** = full connect; **`-sU`** = UDP.
- `-sV` finds service versions, `-O` fingerprints the OS, `-Pn` skips host
  discovery. Match the flag to the behavior — this is tested directly.
- Port states are **open / closed / filtered**; "filtered" implies a firewall.
- **SMB enumeration → TCP 445**; **enum4linux** lists Windows shares, users and
  groups.
- **SNMP** defaults to community string **`public`** (read); guessing it exposes a
  device's full config. Fix: change it and use **SNMPv3**.
- Enumeration is **more intrusive than scanning** — it directly queries services
  for accounts, shares and configuration.
- Defenses across both phases reduce to: **close unused services, change defaults,
  restrict anonymous access, and filter/monitor at the perimeter.**
