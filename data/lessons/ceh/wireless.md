# Wireless Network Hacking

Wi-Fi removes the physical boundary that protects a wired LAN: an attacker no
longer needs to plug in, only to be within radio range. That makes the *encryption
standard* you choose the single most important wireless security decision. This
lesson walks the WEP-to-WPA3 evolution, names the attack classes against each, and
ends where it always does — with the defenses.

## Wireless building blocks

A quick vocabulary set: the **SSID** is the network name, the **BSSID** is the
access point's MAC, and an **AP** (access point) bridges wireless clients to the
wired network over **802.11** radio channels. Because the signal travels through
the air, anyone nearby can *receive* it — so confidentiality depends entirely on
encryption.

## The encryption standards (know the order)

> The progression is **WEP → WPA → WPA2 → WPA3**, each fixing the weaknesses of the
> last. On the exam, **WEP is "broken," WPA2 is the long-time strong standard, and
> WPA3 is current best practice.**

| Standard | Crypto | Status |
|----------|--------|--------|
| **WEP** | RC4 with weak IVs | **Broken** — crackable in minutes |
| **WPA** | TKIP | Interim fix, deprecated |
| **WPA2** | AES-CCMP, 4-way handshake | Strong; weak pre-shared keys crackable offline |
| **WPA3** | SAE (Dragonfly) handshake | Current; resists offline dictionary attacks |

**WPA3** replaces the pre-shared-key handshake with **SAE (Simultaneous
Authentication of Equals)**, which adds forward secrecy and defeats offline
password guessing even if the handshake is captured. (Researchers did disclose
"Dragonblood" weaknesses in early implementations — know the name as a concept.)

## Attack classes against wireless

- **Wardriving** — driving around an area with a Wi-Fi adapter and GPS to
  **discover, locate and map** wireless networks and their security settings.
  (Variants: warwalking, warflying.)
- **Rogue AP / Evil Twin** — an attacker stands up a fake access point advertising
  a **legitimate-looking SSID** to lure clients into connecting, then captures
  traffic or credentials through a captive-portal-style page. This is the wireless
  on-path attack. *Defense:* **802.1X/EAP** enterprise authentication (clients
  verify the network, not just vice versa), wireless IPS to detect rogues, and user
  awareness.
- **Deauthentication attack** — forging 802.11 **deauth** management frames to
  knock clients off the network, either as a denial-of-service or to force a
  reconnection whose handshake can be captured. *Defense:* **802.11w management
  frame protection (PMF)**.
- **KRACK (Key Reinstallation Attack)** — manipulates the **WPA2 4-way handshake**
  to force a client to **reinstall an already-in-use key** (an all-zero key),
  allowing decryption of traffic **without knowing the password**. *Defense:*
  patched clients/APs; WPA3 is not susceptible.
- **WPS attacks** — brute-forcing the Wi-Fi Protected Setup **PIN** (including the
  "Pixie Dust" offline method). *Defense:* **disable WPS**.
- **Handshake / PMKID capture** — capturing the authentication handshake and
  cracking a **weak passphrase offline**. *Defense:* long, random passphrases or
  enterprise auth.
- **Jamming** — flooding the RF band to deny service.

### Tools for recognition

The **aircrack-ng** suite is the best-known toolkit for capturing and analyzing
Wi-Fi handshakes in authorized testing; **Kismet** is a wireless detector/sniffer;
public databases like **WiGLE** map discovered networks. Recognize them by role.

## Defending wireless networks

- **Use WPA3** where supported; otherwise **WPA2 with AES** and a long, random
  passphrase. Never WEP.
- **802.1X / EAP (WPA-Enterprise)** for per-user authentication against a RADIUS
  server — the strongest answer for business networks and the best Evil-Twin
  defense.
- **Disable WPS** entirely.
- **Enable 802.11w (PMF)** to blunt deauthentication attacks.
- **Deploy a Wireless IPS (WIPS)** to detect rogue and evil-twin APs.
- **Segment** guest and IoT traffic, and use **client isolation** so wireless
  clients cannot reach each other.
- Treat **SSID hiding and MAC filtering** as minor speed bumps, not real security.

> The throughline: wireless security is a crypto-standard decision first
> (WPA3/WPA2-AES), an authentication decision second (802.1X), and a monitoring
> decision third (WIPS for rogues).

## Open networks and the risks of "free Wi-Fi"

Not every risk needs an encryption flaw. An **open network** (no encryption at all,
like much public Wi-Fi) sends traffic in the clear, which is why connecting to "free
airport Wi-Fi" is a textbook exposure — and an Evil Twin advertising the same name
is trivial to stand up. The user-side defense is a **VPN**, which tunnels traffic so
a hostile network (or twin) sees only ciphertext. The rule of thumb: on any network
you do not control, assume someone is listening and rely on end-to-end encryption
(HTTPS, VPN) rather than trusting the link.

### WPA3 transition and client hygiene

Many networks run **WPA3 transition mode**, accepting both WPA2 and WPA3 clients for
compatibility — convenient, but it can let an attacker force a WPA2 downgrade, so
**WPA3-only is stronger** where the device fleet allows it. On the client side,
modern devices use **MAC address randomization** to make tracking a device across
networks harder.

On the enterprise side, prefer **certificate-based EAP** methods over
password-based ones where possible, and keep **PMF (802.11w)** enabled, so the
convenience of transition mode does not quietly reopen the deauth and downgrade
doors it was meant to avoid.

## Exam focus

- Standard order and status: **WEP (broken) → WPA (TKIP) → WPA2 (AES) → WPA3 (SAE)**.
  WPA3 resists offline dictionary attacks.
- **KRACK** attacks the **WPA2 4-way handshake** by forcing **key reinstallation**
  (all-zero key) to decrypt traffic **without the password**.
- **Wardriving** = driving around to discover and map Wi-Fi networks (needs adapter
  + GPS).
- **Evil Twin / rogue AP** = a fake AP mimicking a real SSID; counter with
  **802.1X/EAP** and **WIPS**.
- **Deauth** attacks are countered by **802.11w (PMF)**; **disable WPS** to stop PIN
  brute forcing.
- Best defenses: **WPA3 or WPA2-AES with a strong passphrase, 802.1X enterprise
  auth, disable WPS, enable PMF, and monitor for rogue APs**.
