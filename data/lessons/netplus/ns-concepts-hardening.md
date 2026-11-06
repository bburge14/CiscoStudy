# Security Concepts & Network Hardening

Security on this exam is practical: know the core principles, recognize the common
attacks by their symptoms, and know the concrete steps that lock a network down.
This lesson does the concepts and the attacks first, then the hardening measures that
counter them.

## The core principles

Everything in security serves a small set of ideas. The first is the **CIA triad**,
the three goals of every control:

> **C**onfidentiality — only authorized people can read the data (encryption).
> **I**ntegrity — the data hasn't been altered (hashing, signatures).
> **A**vailability — the data and systems are there when needed (redundancy, backups).

Alongside it sits **AAA**, which governs access:

- **Authentication** — proving who you are.
- **Authorization** — what you're allowed to do once authenticated.
- **Accounting** — logging what you did.

Authentication uses **factors**, and combining different *types* gives
**multi-factor authentication (MFA)**:

- **Something you know** — password, PIN.
- **Something you have** — token, phone, smart card.
- **Something you are** — fingerprint, face (biometrics).

> Two passwords is **not** MFA — both are "something you know." True MFA mixes
> *different* factor types, e.g. a password **plus** a phone code.

Three design philosophies shape modern networks:

- **Least privilege** — give each user and device exactly the access it needs, no
  more.
- **Defense in depth** — layer multiple controls so no single failure is fatal.
- **Zero trust** — never trust by location; verify every user and device on every
  request, as if there is no "safe inside."

## Attacks to recognize

The exam describes an attack and asks you to name it, or asks for the defense. Know
these by their fingerprints:

| Attack | What happens |
|--------|--------------|
| **DoS / DDoS** | Flood a target with traffic so it can't serve real users (DDoS = from many sources) |
| **On-path (MITM)** | Attacker secretly relays/alters traffic between two parties |
| **ARP spoofing/poisoning** | Fake ARP replies redirect a victim's traffic to the attacker |
| **MAC flooding** | Overflow a switch's MAC table so it floods frames the attacker can sniff |
| **VLAN hopping** | Reach a VLAN you shouldn't, via double-tagging or switch spoofing |
| **DNS poisoning** | Corrupt DNS answers to send users to a malicious site |
| **Rogue AP / evil twin** | An unauthorized or look-alike access point lures clients |
| **Deauthentication** | Forged frames kick Wi-Fi clients off to force reconnection |
| **Phishing / social engineering** | Trick a *person* into giving up access |

> Social engineering targets **people**, not technology — phishing, pretexting,
> tailgating. The best defense is **user training**, because no firewall stops a user
> who hands over a password.

## Network hardening: closing the doors

Hardening is the set of concrete steps that shrink the attack surface. Group them by
what they protect.

### Harden the devices

- **Change default credentials** — the first thing an attacker tries is the factory
  admin/admin. Change every default password.
- **Disable unused services and ports** — every open service is a door; close the
  ones you don't use. Shut down unused *switch ports* too.
- **Use secure protocols** — **SSH not Telnet**, **HTTPS not HTTP**, **SNMPv3 not
  v1/v2c**, SFTP not FTP. Management in plaintext is a gift to a sniffer.
- **Patch and update firmware** — known vulnerabilities get patched; unpatched gear
  is low-hanging fruit.
- **Role-based access control (RBAC)** — grant admin rights by job role, applying
  least privilege to who can configure what.

### Harden the switch ports (Layer 2)

- **Port security** — limit which/how many MAC addresses a port accepts, and
  shut the port if an unknown one appears. Stops MAC flooding and random devices.
- **DHCP snooping** — the switch only trusts DHCP offers from legitimate ports,
  blocking a rogue DHCP server.
- **Dynamic ARP Inspection (DAI)** — validates ARP against the DHCP snooping table,
  defeating ARP poisoning.
- **BPDU Guard** — shuts a port that unexpectedly sends spanning-tree BPDUs, stopping
  a rogue switch.

### Control who gets on the network

> **802.1X** is port-based network access control: a device plugging in (the
> **supplicant**) must authenticate through the switch (the **authenticator**) to a
> **RADIUS** server before the port opens. No valid credentials, no network. This is
> the backbone of enterprise **NAC (Network Access Control)**, which can also check a
> device's health (patches, antivirus) before admitting it, and quarantine those that
> fail.

### Segment the network

> **Segmentation** is dividing the network into zones so a breach in one can't reach
> the others. **VLANs** separate groups at Layer 2; **ACLs** and **firewalls** control
> what crosses between them. A **DMZ (screened subnet)** isolates public-facing
> servers from the internal LAN, so a compromised web server doesn't expose
> everything else.

Segmentation applies least privilege to *traffic*: a user VLAN has no business
reaching the server management VLAN, so you don't let it. Guest Wi-Fi goes on its own
segment with no path to internal systems. Combined with 802.1X deciding *who* gets on
and port security locking *how* they connect, these controls layer into the
defense-in-depth the concepts section described.

## On the exam

- **CIA** = Confidentiality, Integrity, Availability. **AAA** = Authentication,
  Authorization, Accounting. MFA mixes *different* factor types (know/have/are).
- Know **least privilege, defense in depth, zero trust** by definition.
- Identify attacks from symptoms: **DDoS** (flood), **on-path/MITM**, **ARP
  poisoning**, **MAC flooding**, **VLAN hopping**, **DNS poisoning**, **evil
  twin/rogue AP**, **deauth**, **phishing** (targets people → train users).
- Device hardening: change defaults, disable unused ports/services, **secure
  protocols (SSH/HTTPS/SNMPv3)**, patching, RBAC.
- Layer 2 defenses map to attacks: **port security** → MAC flooding, **DHCP
  snooping** → rogue DHCP, **DAI** → ARP poisoning, **BPDU guard** → rogue switch.
- **802.1X** (supplicant/authenticator/RADIUS) controls who gets on the port; **NAC**
  checks device posture. **Segmentation** with VLANs, ACLs, firewalls and a **DMZ**
  contains breaches.
