# Remote Access & Physical Security

This lesson covers the two ways people and problems reach your gear: across the
network from far away, and in person at the rack. Remote access is mostly about VPNs
and secure management; physical security is about keeping the wrong bodies away from
the hardware.

## VPNs: a private tunnel across a public network

A **VPN (Virtual Private Network)** builds an encrypted tunnel across the internet so
traffic travels as if it were on a private link. The two deployment shapes:

- **Site-to-site VPN** — connects two *networks* permanently, e.g. a branch office to
  headquarters. The routers at each end build the tunnel; users don't notice it.
- **Client-to-site (remote access) VPN** — connects one *user's device* back to the
  corporate network, e.g. a laptop at home. The user runs a VPN client.

Two technologies implement them, and the exam contrasts them:

| | IPsec VPN | SSL/TLS VPN |
|--|-----------|-------------|
| Layer | Network (L3) | Application-ish (L4–7) |
| Client | Usually needs a client | Can be **clientless** (browser) |
| Typical use | Site-to-site, full access | Remote user access to web apps |

> **IPsec** secures at Layer 3 and is the usual choice for site-to-site tunnels.
> **SSL/TLS VPNs** can run clientless in a browser, which makes them convenient for
> remote users. Know both names and when each fits.

**Inside IPsec**, two protocols and two modes come up:

- **AH (Authentication Header)** — integrity and authentication, **no encryption**.
- **ESP (Encapsulating Security Payload)** — integrity **and encryption** (the one
  you actually want).
- **IKE** negotiates the keys and builds the security association.
- **Tunnel mode** encrypts the whole original packet (site-to-site); **transport
  mode** encrypts only the payload (host-to-host).

**Split vs full tunnel** is a design choice for remote-access VPNs:

> **Full tunnel** sends *all* the client's traffic through the VPN (more secure, more
> load). **Split tunnel** sends only corporate-bound traffic through the tunnel and
> lets the rest go straight to the internet (faster, but less control).

## Secure remote management

Beyond VPNs, admins reach devices to manage them, and the protocol choice is a
security decision:

- **SSH (port 22)** — encrypted remote CLI. The standard. Always prefer it.
- **Telnet (port 23)** — remote CLI in **clear text**. Obsolete and unsafe; never use
  it on production gear.
- **RDP (port 3389)** — Microsoft Remote Desktop for a Windows GUI.
- **VNC** — cross-platform remote GUI/screen sharing.

**Out-of-band (OOB) management** reaches a device through a path *separate* from the
production network — a **console** cable, a dedicated management port, or a modem —
so you can still log in when the main network is down. A **jump box / bastion host**
is a hardened server that is the single controlled entry point into a sensitive
segment: admins log into it first, then reach the internal devices, so there's one
audited door instead of many.

### Centralized authentication: RADIUS vs TACACS+

Rather than local passwords on every device, remote access and admin logins
authenticate against a central server:

> **RADIUS** — open standard, combines authentication and authorization, encrypts
> only the **password**, uses UDP. Common for network access / 802.1X and VPNs.
> **TACACS+** — Cisco, separates **A**, **A** and **A**, encrypts the **entire**
> payload, uses TCP. Preferred for device administration.

## Physical security: keeping bodies away from the hardware

All the encryption in the world doesn't help if someone can walk up and unplug — or
walk off with — your server. Physical controls are layered from the perimeter inward.

**Perimeter and grounds:**

- **Fencing** and **bollards** (posts that stop vehicles) keep people and cars out.
- **Security guards** and **cameras/CCTV** provide deterrence and a record.
- **Lighting** removes the cover darkness gives an intruder.

**Entry control:**

- **Badge readers / key cards** and **PIN pads** restrict doors to authorized people.
- **Biometrics** (fingerprint, retina) authenticate the person themselves.
- An **access control vestibule (mantrap)** is a two-door airlock where the second
  door won't open until the first closes — it stops **tailgating**, where someone
  slips in behind an authorized person.
- **Visitor logs** and escorts track anyone without permanent access.

**At the rack and device:**

- **Locking racks and cabinets** keep hands off the equipment.
- **Asset tags** and **tamper-evident seals** reveal theft or meddling.
- **Cable locks** secure portable gear.

> **The mantrap/access control vestibule is the classic answer to tailgating.** And
> remember: a locked server room is a *physical* control, so it belongs in the same
> conversation as firewalls and encryption, not separate from it.

Environmental protections from the facilities topic belong here too: **fire
suppression** (clean-agent, not water, around electronics) protects the hardware, and
proper **HVAC** and **UPS/generator** power keep it alive. Physical and logical
security are two halves of defense in depth — you need both.

### Detective, preventive, deterrent

The exam sometimes asks you to *classify* a physical control rather than just name
it. Three categories cover most of them:

- **Deterrent** — discourages an attacker before they try: signs, lighting, visible
  cameras, a guard at the door.
- **Preventive** — physically stops the action: locks, badge readers, bollards, the
  access control vestibule.
- **Detective** — records or reveals that something happened: camera footage, motion
  sensors, tamper seals, visitor logs.

A single device can wear more than one hat — a visible camera *deters*, while its
recording *detects* — so read the question for which role it's testing.

## On the exam

- **Site-to-site** VPN joins networks; **client-to-site / remote-access** VPN joins a
  user's device. **IPsec** (L3, site-to-site) vs **SSL/TLS** (can be clientless).
- Inside IPsec: **ESP encrypts, AH doesn't**, IKE negotiates keys, tunnel vs
  transport mode. **Full tunnel** = all traffic; **split tunnel** = only corporate.
- Manage securely: **SSH (22) over Telnet (23)**, RDP (3389), VNC. Know **out-of-band
  management** and a **jump box/bastion host** as the single controlled entry point.
- **RADIUS** (open, UDP, encrypts only password, network access) vs **TACACS+**
  (Cisco, TCP, encrypts all, device admin).
- Physical layers: fencing/bollards, cameras, badge readers, **biometrics**, and the
  **access control vestibule (mantrap)** against **tailgating**; locking racks, asset
  tags, tamper seals. Physical security is part of defense in depth.
