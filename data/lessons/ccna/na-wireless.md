# Wireless Architecture & Discovery Protocols

## Wireless fundamentals
Wi-Fi is **half-duplex** shared media using **CSMA/CA**. Two main bands:
- **2.4 GHz** — longer range, more interference; only **3 non-overlapping**
  channels (1, 6, 11) in the US.
- **5 GHz** — more channels, less congestion, shorter range.

An **SSID** names a WLAN; a **BSS** is one AP's cell (identified by the AP radio
MAC = BSSID); an **ESS** is multiple APs sharing an SSID for roaming.

## Autonomous vs controller-based (split-MAC)
- **Autonomous AP** — self-contained; each AP configured individually.
- **Lightweight AP + WLC (split-MAC)** — the AP handles real-time 802.11
  (beaconing, ACKs, encryption), the **WLC** handles management, roaming,
  security and RF. This scales to large deployments.

### CAPWAP
Lightweight APs join the WLC over **CAPWAP**, which builds two tunnels:
- **Control**: UDP **5246**, encrypted with DTLS.
- **Data**: UDP **5247** (data encryption optional).

CAPWAP tunnels traffic over the wired network so an AP's VLANs/SSIDs are defined
centrally on the WLC. (CAPWAP replaced the older LWAPP.)

## AP modes (lightweight)
- **Local** — default; client traffic tunneled back to the WLC (central switching).
- **FlexConnect** — branch mode; can switch client traffic **locally** and keep
  serving already-authenticated clients in **standalone** mode if the WLC link fails.
- **Monitor / Sniffer / Rogue detector / Bridge (mesh)** — specialized roles.

## WLC port & interface types (concept)
- **Management interface** — in-band WLC management and AP-join.
- **Dynamic (WLAN) interface** — maps an SSID/WLAN to a VLAN.
- **Virtual interface** — used for client web-auth/DHCP relay (e.g., 192.0.2.1).

## Discovery protocols: CDP vs LLDP
| | CDP | LLDP |
|--|-----|------|
| Standard | Cisco-proprietary | IEEE **802.1AB** (open) |
| Default | **On** | **Off** (`lldp run`) |
| Layer | 2 | 2 |
| Timers | 60 s hello, 180 s hold | 30 s hello, 120 s hold |

Both discover directly connected neighbors (device ID, port, platform, VLAN,
power). Use **LLDP** in multivendor environments.
```
show cdp neighbors [detail]
show lldp neighbors [detail]
```

## Exam cues
- CAPWAP = 5246 (control, DTLS) / 5247 (data).
- FlexConnect = branch local switching + survivability.
- CDP: Cisco, on by default. LLDP: 802.1AB, off by default.
