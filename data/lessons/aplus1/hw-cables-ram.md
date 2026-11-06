# Cables, Connectors & Memory

Hardware starts with the parts you can hold: the cables that carry signals and
the memory sticks that give the CPU a workspace. Cables are a game of matching a
plug to a port and knowing what each one is good for; memory is a game of
matching the right stick to the right slot. This lesson does both.

## Copper network cables: twisted pair

The workhorse of wired networking is **twisted-pair** cable ending in an **RJ45**
plug. The pairs are twisted to cancel interference, and the *category* tells you
how fast and how far it can go:

| Category | Max speed | Notes |
|----------|-----------|-------|
| Cat 5    | 100 Mbps  | obsolete |
| Cat 5e   | 1 Gbps    | the common minimum today |
| Cat 6    | 10 Gbps (up to 55 m) | tighter spec |
| Cat 6a   | 10 Gbps (full 100 m) | shielded, thicker |

Twisted pair runs about **100 meters (328 ft)** before the signal degrades — a
number worth memorizing. Cable comes **unshielded (UTP)** or **shielded (STP)**;
you choose STP in electrically noisy places (near motors, fluorescent ballasts).

> **Plenum** cable has a fire-resistant, low-smoke jacket. It is required in
> **plenum spaces** — the air-handling gaps above drop ceilings — so that a fire
> does not fill the building's air with toxic smoke through the ductwork.

### T568A/B and straight-through vs crossover

The eight wires terminate in a fixed color order defined by **T568A** and
**T568B**. Both ends the *same* standard = a **straight-through** cable (PC to
switch). Each end a *different* standard (one A, one B) = a **crossover** cable,
historically used to join two like devices (PC-to-PC, switch-to-switch). Modern
gear with **Auto-MDI-X** fixes this automatically, so crossovers are rarely
needed now — but the exam still tests the concept.

## Coaxial and fiber

- **Coaxial (coax)** — a single copper core in shielding, ending in an **F-type**
  screw-on connector. It carries cable TV and connects a **cable modem**.
  **RG-6** is the common grade (RG-59 is older/thinner).
- **Fiber-optic** — glass strands carrying **light**, not electricity. Fiber is
  immune to electrical interference, spans long distances, and reaches the
  highest speeds. Two flavors: **single-mode** (a thin core for very long runs)
  and **multimode** (a wider core for shorter runs). Connectors to recognize:
  **LC** (small, latching), **SC** (square, push-pull), and **ST** (round,
  bayonet twist-lock).

> Fiber beats copper when you need **distance** or **immunity to interference**,
> or the absolute **highest speed** — at a higher cost and with more fragile
> cable.

## Video cables

Monitors connect with one of four, newest first:

- **HDMI** — carries **video and audio** on one cable; universal on TVs and most
  monitors.
- **DisplayPort** — the PC-focused modern standard; also carries audio and can
  daisy-chain monitors. **DP** connectors often have a latch.
- **DVI** — older digital (some variants also analog). No audio.
- **VGA** — the oldest, **analog** 15-pin blue connector. Picture quality
  degrades over long runs; no audio.

> If a question wants one cable for **video + audio to a TV**, that is **HDMI**.
> VGA is the pure-analog legacy answer.

## Peripheral and storage cables

- **USB** — the universal peripheral bus. Speeds climbed over the years: **USB
  2.0** (480 Mbps), **USB 3.x** (5–20 Gbps, ports often blue), and **USB-C** (the
  reversible connector that can carry USB, video, and power).
- **Thunderbolt** — very high bandwidth over the USB-C shape (and older
  Mini-DisplayPort shape on TB1/2).
- **Lightning** — Apple's small reversible connector on older iPhones.
- **SATA** — the flat data cable to internal drives; **eSATA** is the external
  version.
- **Molex** and **SATA power** — the power leads from the PSU to drives.
- **Serial (RS-232 / DB9)** — legacy console/management connections on networking
  gear.

## Memory: giving the CPU a workspace

**RAM** (Random Access Memory) is the fast, temporary workspace the CPU uses for
whatever is running right now. It is **volatile** — empty the moment power is
lost — which is why unsaved work disappears in a crash. More RAM lets more run at
once without the system falling back on slow disk.

### DDR generations

Modern RAM is **DDR** (Double Data Rate) SDRAM, and each generation is faster and
more efficient — and **physically keyed so it only fits its own slot**:

| Generation | Typical era | Note |
|------------|-------------|------|
| DDR3 | older | legacy systems |
| **DDR4** | current mainstream | wide support |
| **DDR5** | newest | higher speed, higher capacity |

> **You cannot mix generations.** DDR4 will not fit a DDR5 slot — the notch is in
> a different place on purpose. Match the motherboard's supported generation
> exactly.

Desktops use full-length **DIMM** sticks; laptops and small PCs use the shorter
**SO-DIMM**. A stick's speed is written as **DDR4-3200** (mega-transfers/sec) or
as a **PC4-25600** bandwidth number.

### Channels: installing in pairs

Memory controllers can talk to more than one stick at a time, which widens the
pipe to the CPU:

- **Single channel** — one stick, narrowest path.
- **Dual channel** — a matched **pair** of sticks, roughly doubling memory
  bandwidth. This is the common target.
- **Triple / quad channel** — high-end platforms with 3 or 4 sticks.

> To get **dual channel**, install **matched sticks in the correctly colored
> (paired) slots** — usually slots 2 and 4, as the motherboard manual shows.
> Two sticks in the wrong slots run as single channel.

### ECC and the server variants

- **ECC** (Error-Correcting Code) RAM detects and fixes single-bit errors on the
  fly. It is used in **servers** where silent memory corruption is unacceptable.
  Most desktops use **non-ECC**.
- **Registered / buffered** memory adds a register to support very large server
  capacities. Desktop RAM is **unbuffered**. These are not interchangeable with
  consumer boards.

### Virtual memory

When RAM fills up, the OS spills the least-used data to a **page file / swap** on
the drive — **virtual memory**. It prevents out-of-memory crashes but is far
slower than real RAM, so heavy swapping ("thrashing") is a sign you need more
physical RAM.

## The whole thing in one paragraph

Wired networks run on **twisted-pair** (Cat 5e/6/6a, RJ45, ~100 m, UTP or
shielded STP, **plenum** jacket above ceilings) terminated to **T568A/B** —
same-both-ends is straight-through, mixed is crossover — alongside **coax**
(F-type, cable modems) and **fiber** (glass, light, LC/SC/ST, best distance and
interference immunity). Video uses **HDMI** (video+audio), **DisplayPort**,
**DVI**, or legacy analog **VGA**, while peripherals use **USB** (2.0→3.x→USB-C),
**Thunderbolt**, **SATA/eSATA**, and legacy **serial**. Memory is **DDR** RAM
(DDR3/DDR4/DDR5, **keyed so generations never mix**), full-size **DIMM** or laptop
**SO-DIMM**, installed as matched pairs for **dual-channel** bandwidth, with
**ECC** for servers and **virtual memory** as the slow disk-based overflow when
RAM fills.

## On the exam

- Twisted pair: **Cat 5e = 1 Gbps, Cat 6/6a = 10 Gbps, ~100 m max**, **RJ45**
  plug. **Plenum** cable goes in air-handling ceiling spaces.
- **T568A both ends / T568B both ends = straight-through**; **mixed = crossover.**
- **Fiber** for distance / interference immunity / top speed; connectors **LC,
  SC, ST**. **Coax** uses **F-type** (RG-6) for cable.
- **HDMI** carries video + audio; **VGA** is analog legacy; **DisplayPort** is the
  modern PC standard.
- RAM is **keyed per DDR generation — never mixable.** Desktop = **DIMM**, laptop
  = **SO-DIMM**.
- **Dual channel** needs **matched sticks in the paired slots**; wrong slots drop
  to single channel.
- **ECC** = servers (corrects errors); desktops are non-ECC. **Virtual memory /
  page file** is slow disk overflow — heavy use means buy more RAM.
