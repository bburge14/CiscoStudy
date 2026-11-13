# Secure Channels & Network Attacks

A network is only as safe as the channels that cross it and the attacks it can
withstand. This lesson covers the protocols that turn an open wire into a protected
conversation — TLS, SSH, and especially IPsec — and then the catalog of network
attacks CISSP expects you to recognize on sight and counter.

## Secure protocols: swap insecure for secure

A recurring exam move is to hand you a plaintext protocol and ask for its secure
replacement. Learn the pairs.

| Insecure | Secure replacement | Protects |
|----------|-------------------|----------|
| Telnet | **SSH** | Remote admin |
| FTP | **SFTP** (over SSH) / **FTPS** (over TLS) | File transfer |
| HTTP | **HTTPS** (HTTP over TLS) | Web traffic |
| SNMPv1/v2 | **SNMPv3** | Device management |
| LDAP | **LDAPS** | Directory queries |
| Plain email | **S/MIME** or **PGP** | Email content |

> **TLS** (Transport Layer Security) superseded **SSL**. SSL and **TLS 1.0/1.1 are
> deprecated**; **TLS 1.2 and 1.3** are current, with 1.3 dropping legacy ciphers
> and speeding the handshake. "Use HTTPS/TLS" is the answer whenever web data
> crosses an untrusted network.

Two special cases worth knowing: **DNSSEC** adds **integrity and authentication**
to DNS responses (it stops forged records) but does **not** encrypt them — a common
trap. And **S/MIME** vs **PGP** both secure email, differing mainly in their trust
model (S/MIME uses CA-issued certificates; PGP uses a web of trust).

## IPsec in depth

IPsec secures IP traffic itself (Layer 3) and is the backbone of site-to-site VPNs.
Its two protocols are a guaranteed exam item.

> **AH (Authentication Header)** provides **integrity and authentication only — no
> encryption.** **ESP (Encapsulating Security Payload)** provides
> **confidentiality (encryption)** plus optional integrity and authentication.

So when a VPN must provide **confidentiality**, the component is **ESP** — AH alone
cannot encrypt. Two modes:

- **Transport mode** — encrypts only the payload; the original IP header stays
  visible. Used host-to-host.
- **Tunnel mode** — encrypts the entire original packet and wraps it in a new
  header. Used **gateway-to-gateway** (site-to-site VPNs).

Supporting pieces: **IKE (Internet Key Exchange)** negotiates keys over **UDP 500**
(and 4500 for NAT traversal) and establishes **Security Associations (SAs)** — the
agreed parameters for each direction of the connection.

VPN flavors to recognize: **site-to-site** (connects whole networks, tunnel-mode
IPsec), **remote-access** (a user to the corporate network), and **SSL/TLS VPNs**
(clientless, browser-based access).

## Network attacks

CISSP expects pattern recognition: read the behavior, name the attack, know the
fix.

- **DoS / DDoS** — overwhelm a target so legitimate users can't connect; DDoS uses
  many sources (often a botnet).
- **SYN flood** — sends TCP connection requests but never completes the three-way
  handshake, exhausting the server's table of **half-open** connections. Mitigate
  with **SYN cookies**. (The "half-open connections exhausting the backlog" cue is
  unmistakable.)
- **Smurf / amplification / reflection** — spoof the victim's address and bounce
  traffic off third parties (or DNS/NTP servers) to multiply volume.
- **Man-in-the-middle (on-path)** — intercept and possibly alter traffic between two
  parties; defeated by mutual authentication and encryption.
- **ARP poisoning (spoofing)** — forge ARP replies to associate the attacker's MAC
  with another host's IP, enabling on-path attacks on a LAN.
- **DNS poisoning / cache poisoning** — inject forged DNS records so victims resolve
  a name to an attacker's server; DNSSEC defends against it.
- **Session hijacking** — steal or predict a session token to take over an
  authenticated session.
- **Replay** — capture and resend valid traffic (e.g., an authentication exchange);
  defeated by timestamps, sequence numbers, and nonces.
- **Spoofing** — forging a source identity (IP, MAC, email).
- **VLAN hopping** — escaping an assigned VLAN to reach another; mitigate by
  disabling unused trunking and auto-negotiation.
- **Eavesdropping / sniffing** — passive capture of unencrypted traffic; encryption
  makes captured data useless.

> The managerial throughline: most of these attacks are defeated not by a clever
> point tool but by **encryption, authentication, and segmentation** applied
> consistently. When several answers look plausible, favor the control that closes
> the *class* of attack (encrypt the channel) over one narrow signature.

## AAA protocols: RADIUS vs TACACS+

Centralized **AAA** (authentication, authorization, accounting) servers control who
may reach the network and what administrators may do on devices. The exam contrasts
the two protocols head to head.

> **RADIUS** runs over **UDP** (ports **1812/1813**), **encrypts only the password**
> (the rest of the packet is cleartext), and **combines authentication and
> authorization**. It is an open standard, ideal for network access (802.1X, VPN,
> Wi-Fi). **TACACS+** runs over **TCP** (port **49**), **encrypts the entire
> payload**, and **separates** authentication, authorization, and accounting — it is
> Cisco-originated and favored for granular device administration.

The hook: **TACACS+ = TCP, Total payload encryption, and separated AAA**; **RADIUS
= UDP, password-only encryption, combined authN/authZ**. Diameter is the modern
successor to RADIUS.

## Exam focus

- Swap insecure for secure: **Telnet→SSH, FTP→SFTP/FTPS, HTTP→HTTPS,
  SNMP→SNMPv3, LDAP→LDAPS.** **TLS replaced SSL**; **TLS 1.2/1.3** current, SSL and
  TLS 1.0/1.1 deprecated. **DNSSEC = integrity/authentication for DNS, not
  encryption.**
- **IPsec: AH = integrity/authentication, NO encryption; ESP = confidentiality**
  (+ optional integrity). **Tunnel mode** for site-to-site, **transport mode**
  host-to-host; **IKE** on UDP 500 sets up **SAs**.
- Attack recognition: **SYN flood** = half-open TCP exhaustion (fix: SYN cookies);
  **ARP poisoning** = forged MAC/IP on a LAN; **DNS poisoning** = forged records
  (fix: DNSSEC); **replay** (fix: nonces/timestamps); **on-path/MITM** (fix: mutual
  auth + encryption).
- Prefer defenses that neutralize a whole attack class — **encrypt, authenticate,
  segment** — over narrow fixes.
- **AAA protocols**: **TACACS+** (TCP 49, encrypts the whole payload, separates
  AAA) vs **RADIUS** (UDP 1812/1813, encrypts only the password, combines
  authN/authZ).
