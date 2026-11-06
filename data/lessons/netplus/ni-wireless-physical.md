# Wireless Standards & Physical Installations

Two very physical topics live here: the radio standards behind Wi-Fi, and the cables,
connectors and gear that make up the wired plant. Both are heavy on specifics —
speeds, distances, names — so this lesson is built around the tables you'll want to
know on sight.

## 802.11: the Wi-Fi standards

All Wi-Fi is the IEEE **802.11** family. Over the years each new letter brought more
speed, and the marketing names (Wi-Fi 4, 5, 6) were added later to make them easier
to talk about. The key fact is which **frequency band** each uses, because that
drives range and interference.

| Standard | Wi-Fi name | Band(s) | Max rate (approx) |
|----------|------------|---------|-------------------|
| 802.11b | — | 2.4 GHz | 11 Mbps |
| 802.11a | — | 5 GHz | 54 Mbps |
| 802.11g | — | 2.4 GHz | 54 Mbps |
| 802.11n | Wi-Fi 4 | 2.4 and 5 GHz | 600 Mbps |
| 802.11ac | Wi-Fi 5 | 5 GHz | ~3.5 Gbps |
| 802.11ax | **Wi-Fi 6 / 6E** | 2.4, 5 (and 6 GHz for 6E) | ~9.6 Gbps |
| 802.11be | Wi-Fi 7 | 2.4, 5, 6 GHz | ~46 Gbps |

> **Wi-Fi 6 is 802.11ax.** That single mapping is almost guaranteed to appear. Wi-Fi
> 6**E** is the same standard extended into the new **6 GHz** band.

### The two classic bands

- **2.4 GHz** — travels farther and through walls better, but is slow and crowded
  (microwaves, Bluetooth, neighbors). It has only **three non-overlapping channels:
  1, 6, and 11.** Design around those three to avoid interference.
- **5 GHz** — much faster and far more channels, but shorter range and weaker through
  walls.
- **6 GHz** (Wi-Fi 6E/7) — even more clean spectrum, shortest range.

**Channel width** trades reach for speed: 20 MHz is narrow and reliable, and you can
bond channels up to 40/80/160 MHz for more throughput — mostly on 5/6 GHz, since
2.4 GHz is too cramped to bond.

### Technologies inside modern Wi-Fi

- **MIMO / MU-MIMO** — multiple antennas sending multiple streams at once; MU-MIMO
  serves several clients simultaneously instead of one at a time.
- **OFDMA** (new in Wi-Fi 6) — splits a channel so several clients share it
  efficiently, great for many small devices.
- **Beamforming** — focuses the signal toward a client rather than radiating evenly.
- **Band steering** — nudges capable clients onto the faster 5 GHz band.

### Wireless design terms

An **SSID** is the network name you pick from a list; a **BSSID** is the AP radio's
MAC address behind it. Several APs can share one SSID so clients **roam** seamlessly
between them. Antennas shape coverage: an **omnidirectional** antenna radiates in all
directions (good in the middle of an office), while **directional** antennas (Yagi,
parabolic dish) focus the signal one way for long point-to-point links.

**Wireless security** (covered more in the security unit): use **WPA3** where you
can, **WPA2** otherwise, and never WEP or WPA. **Personal/PSK** mode uses one shared
password; **Enterprise** mode authenticates each user through a **RADIUS** server
with **802.1X**.

## Copper cabling: the twisted-pair categories

Wired LANs still run mostly on twisted-pair copper, graded by **category**. Higher
categories support more speed, usually over the same 100 m run.

| Category | Max speed | Distance | Notes |
|----------|-----------|----------|-------|
| Cat 5e | 1 Gbps | 100 m | The old baseline |
| Cat 6 | 1 Gbps (10 G to ~55 m) | 100 m / 55 m | Common today |
| Cat 6a | 10 Gbps | 100 m | 10 G over a full run |
| Cat 7 | 10 Gbps | 100 m | Shielded, special connectors |
| Cat 8 | 25–40 Gbps | ~30 m | Datacenter short runs |

> The single most-tested cabling fact: the standard copper Ethernet run is **100
> meters**. And for **10 Gbps over a full 100 m, you need Cat 6a** (plain Cat 6 only
> reaches 10 G for about 55 m).

Twisted pair comes as **UTP** (unshielded, the norm) or **STP/shielded** (used around
heavy electrical interference). Cable run through air ducts must be **plenum-rated**
so it doesn't give off toxic smoke in a fire.

### Copper connectors and pinouts

The connector is the **RJ45** (8 pins). Wiring follows one of two pin orders,
**T568A** or **T568B** — pick one and use it everywhere.

- A **straight-through** cable uses the *same* standard on both ends (PC to switch).
- A **crossover** uses T568A on one end and T568B on the other (switch to switch,
  historically) — though **Auto-MDIX** now fixes mismatches automatically on modern
  gear.

Punch-down termination lands cables on a **110 block** or a **patch panel**;
individual wall jacks use **keystone** modules.

## Fiber: light instead of electricity

Fiber carries data as light, immune to electrical interference and able to run far
farther than copper. There are two kinds, and telling them apart is a classic
question:

| Type | Core | Light source | Reach | Use |
|------|------|--------------|-------|-----|
| **Multimode (MMF)** | Larger (~50/62.5 µm) | LED / VCSEL | Hundreds of meters | Inside buildings / campus |
| **Single-mode (SMF)** | Tiny (~9 µm) | Laser | Many kilometers | Long haul / between sites |

> **Single-mode = long distance (laser, tiny core); multimode = shorter distance
> (LED, bigger core).** A handy hook: **S**ingle-mode for **S**treet-to-city
> distances.

Fiber **connectors** to recognize by name: **LC** (small, the common one today),
**SC** (square, "stick and click"), **ST** (round bayonet, "stick and twist"), and
**MPO/MTP** (multi-fiber ribbon for high-density 40/100 G).

**Transceivers** are the swappable modules that let a switch port use the right
media: **SFP** (1 G), **SFP+** (10 G), **QSFP/QSFP+** (40 G and up). You match the
transceiver to the fiber type and distance.

## The physical environment

Cabling terminates in a **rack** (measured in **U**, 1.75 in each) holding switches,
patch panels and servers. The room needs supporting infrastructure:

- **UPS** — battery backup that rides through short outages and allows a clean
  shutdown; a **generator** covers longer ones.
- **PDU** — the rack's power strip, distributing and sometimes metering power.
- **HVAC / cooling** — electronics make heat; without cooling they throttle or fail.
- **Grounding** — protects equipment and people from stray voltage and static.
- **Fire suppression** — clean-agent systems that won't ruin electronics like water
  would.

Keeping all of this labeled and documented is what makes the operations topics in the
next unit possible.

## On the exam

- **Wi-Fi 6 = 802.11ax**; Wi-Fi 5 = ac; Wi-Fi 4 = n. 6E adds the **6 GHz** band.
- 2.4 GHz = longer range, only **channels 1/6/11** don't overlap; 5/6 GHz = faster,
  shorter, more channels. Know MIMO/MU-MIMO, OFDMA, beamforming, band steering.
- SSID is the name, BSSID is the AP's MAC; omni vs directional (Yagi/parabolic).
- Copper runs **100 m**; **Cat 6a** gives 10 G over the full run; know the category
  table and UTP/STP and plenum.
- RJ45 with **T568A/T568B**; straight-through (same both ends) vs crossover
  (A/B); Auto-MDIX fixes it automatically.
- **Single-mode = long/laser, multimode = short/LED.** Connectors LC/SC/ST/MPO;
  transceivers SFP (1 G), SFP+ (10 G), QSFP (40 G+).
- Datacenter environment: UPS vs generator, PDU, HVAC/cooling, grounding, rack units.
