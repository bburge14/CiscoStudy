# Sniffing & Session Hijacking

These two topics belong together because one feeds the other: sniffing *captures*
traffic, and session hijacking uses captured or stolen material to *take over* a
connection. Both live at the network/perimeter layer, and both have the same
ultimate cure — encryption done properly. We will cover what each attack class is
and, crucially, the controls that stop it.

## Sniffing: reading traffic you should not see

> **Sniffing is capturing network traffic as it travels, often to read data that
> was sent in cleartext.** It is *passive* when the attacker just listens, and
> *active* when they must manipulate network devices to see traffic that would not
> normally reach them.

On old shared media (hubs), everyone saw everything, so **passive sniffing** was
enough. On a modern **switched** network a switch forwards frames only to the
right port, so an attacker must *make* the traffic come to them — that is **active
sniffing**.

### How active sniffing is achieved (and defended)

- **ARP poisoning (ARP spoofing)** — the attacker sends **forged ARP replies** so
  victims associate the attacker's MAC with the **default gateway's IP**, placing
  the attacker on the traffic path (an on-path/"man-in-the-middle" position).
  *Defense:* **Dynamic ARP Inspection (DAI)**, static ARP entries for critical
  hosts.
- **MAC flooding** — floods the switch's CAM table until it can no longer store
  mappings and "fails open," behaving like a hub. *Defense:* **port security**
  limiting MACs per port.
- **DHCP starvation + rogue DHCP** — exhausts the DHCP pool, then answers clients
  with attacker-controlled gateway/DNS. *Defense:* **DHCP snooping**.
- **DNS poisoning** — feeds victims false name-to-IP answers. *Defense:* DNSSEC,
  trusted resolvers.

### Tools and what is at risk

**Wireshark** and **tcpdump** capture and analyze packets; **Ettercap** and similar
tools automate on-path attacks. The data most exposed is anything sent in the clear
— **Telnet, FTP, HTTP, and SNMPv1/2**. The blanket defense is **encryption**:
HTTPS/TLS, SSH instead of Telnet, and encrypted management protocols, backed by
switch-layer controls (DAI, DHCP snooping, port security) and VLAN segmentation.

## Session hijacking: stealing the connection

Even with a correct login, the *session* that follows can be stolen.

> **Session hijacking is taking over an already-authenticated session — usually by
> stealing its session token — so the attacker acts as the user without ever
> knowing the password.**

It happens at two levels:

| Level | How it works |
|-------|-------------|
| **Network level** | Hijacking TCP/IP sessions via sequence-number prediction or an on-path position |
| **Application level** | Stealing or forging the **session token/cookie** that identifies the logged-in user |

Application-level techniques you should recognize by name:

- **Token theft by sniffing** — grabbing the session cookie off an unencrypted
  connection (sometimes called *sidejacking*).
- **Cross-Site Scripting (XSS)** — stealing cookies through injected script.
- **Session fixation** — forcing a victim to use a session ID the attacker already
  knows.
- **Predictable tokens** — guessing weak, non-random session IDs.

### Defending against session hijacking

The single most effective control is encryption of the session:

- **TLS/HTTPS everywhere** — the control that most directly stops *network-based*
  hijacking, because the attacker can no longer read tokens on the wire.
- **Long, random, unpredictable session IDs** — defeat guessing.
- **Regenerate the session ID after login** — defeats fixation.
- **Secure cookie flags** — `Secure` (HTTPS only), `HttpOnly` (not readable by
  script, blunting XSS theft), and `SameSite`.
- **Short idle timeouts and real logout** that invalidates the token server-side.
- **Re-authentication** for sensitive actions.

## Why the pairing matters

Sniffing is how an attacker *obtains* a token on an unencrypted network; session
hijacking is what they *do* with it. That is why "encrypt the session with
TLS/HTTPS" answers both problems: it stops the capture and makes a stolen token far
harder to obtain in the first place.

## The protocols that give you away

Sniffing only yields secrets when traffic is unencrypted. These legacy cleartext
protocols all have secure replacements you should recommend:

| Cleartext | Exposes | Secure replacement |
|-----------|---------|---------------------|
| Telnet | Login + whole session | SSH |
| FTP | Credentials + files | SFTP / FTPS |
| HTTP | Everything | HTTPS (TLS) |
| SNMPv1/v2c | Community strings + data | SNMPv3 |
| POP3/IMAP/SMTP (plain) | Mail + credentials | TLS-wrapped equivalents |

A useful mental model: an unencrypted network is a **postcard** — every relay that
handles it can read it — while TLS is a **sealed envelope**. Session tokens written
on a postcard are exactly what hijacking harvests, which is why "encrypt everything"
answers both halves of this lesson.

## Exam focus

- **Passive vs active sniffing**: switched networks require **active** sniffing
  because the switch isolates traffic.
- **ARP poisoning/spoofing** = forged ARP replies binding the attacker's MAC to the
  **gateway IP** → on-path position. Defense: **DAI** (plus DHCP snooping and port
  security for the related attacks).
- **MAC flooding** overflows the **CAM table**; **port security** is the fix.
- Cleartext protocols (**Telnet, FTP, HTTP**) are the prize; **encryption** is the
  blanket defense.
- **Session hijacking** = taking over an authenticated session by **stealing the
  session token**, no password needed.
- The control that most directly stops network-based hijacking is **TLS/HTTPS**;
  add **random session IDs, ID regeneration after login, and HttpOnly/Secure/
  SameSite cookies**.
