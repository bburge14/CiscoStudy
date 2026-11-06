# Storage, Motherboards, CPUs & Power

These four parts are the heart of a PC: where data lives (**storage**), the board
that ties everything together (**motherboard**), the brain that does the work
(**CPU**), and the box that feeds them all electricity (**power supply**). Build
a mental picture of how they connect and the exam questions answer themselves.

## Storage: where your data lives

Unlike RAM, storage is **non-volatile** — it keeps your files when the power is
off. There are two main technologies.

### Hard drives vs solid-state

- A **hard disk drive (HDD)** stores data magnetically on spinning platters read
  by a moving head. Its speed is tied to **rotational speed**: **5400 RPM**
  (slower, cooler, laptops) or **7200 RPM** (faster, desktops). HDDs are cheap
  per terabyte but mechanical — slower and more fragile. Sizes: **3.5"**
  (desktop) and **2.5"** (laptop).
- A **solid-state drive (SSD)** uses flash memory with **no moving parts**. It is
  far faster, silent, cooler, and shock-resistant, at a higher cost per terabyte.

### The SSD connection matters: SATA vs NVMe

An SSD's speed depends on *how it connects*, and this is a top exam point:

- **SATA SSD** — a 2.5" SSD (or an M.2 SATA card) on the SATA bus, capped at
  about **600 MB/s**. Still far quicker than a hard drive.
- **NVMe SSD** — an **M.2** card that talks over **PCI Express** lanes using the
  **NVMe** protocol. It runs **several times faster** than SATA because PCIe is a
  much wider, more direct path to the CPU.

> **SATA vs NVMe in one line:** same job, but **NVMe uses PCIe and is many times
> faster** than a SATA SSD. If a question asks for the fastest storage, it is
> NVMe.

Other storage you should recognize: **flash media** (SD, microSD, USB thumb
drives) and **optical discs** (CD ~700 MB, DVD ~4.7 GB, Blu-ray ~25 GB+), now
mostly legacy.

### RAID: combining drives

**RAID** (Redundant Array of Independent Disks) joins several drives for speed,
redundancy, or both. Know these four cold:

| RAID | Needs | What you get | Trade-off |
|------|-------|--------------|-----------|
| **0** | 2+ drives | **Striping** — speed, full capacity | **No redundancy**; one drive dies = all data lost |
| **1** | 2 drives | **Mirroring** — exact copy, redundancy | Usable space = half |
| **5** | 3+ drives | **Striping + parity** — speed *and* survives **1** drive failure | Loses one drive's worth to parity |
| **10** | 4+ drives | **Mirror + stripe** — speed *and* redundancy | Expensive; half the space |

> **RAID 0 has no redundancy** — it is pure speed and is the trap answer when a
> question asks for fault tolerance. **RAID 1** mirrors, **RAID 5** survives one
> failure with parity, **RAID 10** combines mirroring and striping.

## The motherboard: the backbone

The **motherboard** is the printed circuit board every other part plugs into. Its
job is to connect the CPU, RAM, storage, expansion cards, and power.

### Form factors: ATX, microATX, ITX

The **form factor** is the board's size and layout, which must match the case:

- **ATX** — full size, the most slots and ports.
- **microATX (mATX)** — smaller, fewer expansion slots; fits smaller cases.
- **Mini-ITX (ITX)** — very small, usually one expansion slot; for compact PCs.

> A smaller form factor means **fewer RAM and expansion slots** — size and
> expandability trade directly against each other.

### CPU sockets: LGA vs PGA

The CPU drops into a **socket**, and the two styles are a guaranteed exam item:

- **LGA** (Land Grid Array) — the **pins are on the socket/motherboard**, and the
  CPU has flat contacts. This is **Intel's** style.
- **PGA** (Pin Grid Array) — the **pins are on the CPU**, dropping into holes in
  the socket. This is the classic **AMD** style.

> **LGA = pins on the board (Intel); PGA = pins on the chip (AMD).** Bent socket
> pins (LGA) or bent CPU pins (PGA) are a common, delicate failure — handle by
> the edges.

### Expansion: PCI Express

Add-in cards (graphics, NVMe, network, capture) use **PCI Express (PCIe)** slots.
PCIe comes in widths by *lane count*: **x1, x4, x8, x16**, where more lanes = more
bandwidth. A graphics card uses a long **x16** slot; a small Wi-Fi or sound card
uses a short **x1** slot.

> A card fits a slot of its size **or larger** — an x1 card works in an x16 slot.
> Each PCIe generation also doubles the per-lane speed of the one before it.

### Firmware, the chipset, and the CMOS battery

- The **BIOS/UEFI** firmware is the boot code stored on the board that
  initializes hardware and launches the OS. **UEFI** is the modern replacement
  for legacy BIOS — it adds a graphical setup, mouse support, drives larger than
  2 TB (GPT), and **Secure Boot**.
- Firmware settings (boot order, time, security) are saved in a tiny **CMOS**
  memory kept alive by a coin-cell **CMOS battery (CR2032)**. When that battery
  dies, the clock resets and settings are lost on every power-off — the classic
  "PC forgets the date and time" symptom.
- The **chipset** is the board's traffic controller between the CPU and the rest.

### CPU features and cooling

A modern CPU has multiple **cores** (independent processing units) and often
**threads** (logical cores via hyper-threading/SMT), is **64-bit**, may include an
**integrated GPU**, and supports **hardware virtualization** (Intel **VT-x** /
AMD **AMD-V**) — which must be enabled in UEFI to run hypervisors efficiently.

A CPU produces heat, so it needs a **heatsink and fan** (or liquid cooling), with
a thin layer of **thermal paste** between the CPU and heatsink to transfer heat.
Too much, too little, or old dried paste causes overheating.

## The power supply (PSU)

The **PSU** converts wall **AC** into the low-voltage **DC** rails (**+3.3 V, +5
V, +12 V**) the components use. Four things matter.

### Wattage

The PSU must supply enough **watts** for everything, especially a hungry graphics
card. Undersizing causes random shutdowns and reboots under load. Size with
headroom (a margin above the system's peak draw).

### Efficiency: 80 PLUS

The **80 PLUS** rating certifies the PSU is at least 80% efficient (less wasted as
heat), with tiers **80+ Bronze → Silver → Gold → Platinum → Titanium** climbing
in efficiency. Higher tiers run cooler and cheaper over time.

### Connectors

Know which plug feeds what — a favorite exam list:

| Connector | Feeds |
|-----------|-------|
| **24-pin** (20+4) | the **motherboard** main power |
| **4/8-pin EPS (CPU)** | the **CPU** power near the socket |
| **6/8-pin PCIe** | a **graphics card** |
| **SATA power** | SATA drives |
| **Molex (4-pin)** | older drives, fans, accessories |

### Modular and input voltage

- **Modular** PSUs let you attach only the cables you need (tidy airflow);
  **non-modular** have all cables permanently attached.
- Some PSUs have a **115 V / 230 V** input switch — set it wrong for your region
  and the PSU will not work or can be damaged. Many modern units auto-range.

> **Safety:** a PSU holds dangerous charge even unplugged. Technicians **do not
> open** a PSU — it is replaced as a unit, not repaired.

## The whole thing in one paragraph

Storage is non-volatile: mechanical **HDDs** (5400/7200 RPM, 3.5"/2.5") versus
fast **SSDs**, where connection decides speed — a **SATA SSD** (~600 MB/s) versus
an **NVMe** M.2 SSD on **PCIe** (many times faster) — and **RAID** combines
drives (**0** stripe/no redundancy, **1** mirror, **5** stripe+parity surviving
one failure, **10** mirror+stripe). The **motherboard** (form factors **ATX >
mATX > ITX**, fewer slots as it shrinks) seats the CPU in an **LGA** socket
(pins on board, Intel) or **PGA** (pins on chip, AMD), offers **PCIe** slots
(x1–x16), runs **UEFI/BIOS** firmware with settings kept by a **CMOS battery**,
and hosts a CPU with cores/threads, virtualization (**VT-x/AMD-V**), and a
heatsink using **thermal paste**. The **PSU** turns AC into DC rails, rated by
**wattage** and **80 PLUS** efficiency, feeding the board (**24-pin**), CPU
(**EPS 4/8-pin**), GPU (**PCIe 6/8-pin**), and drives (SATA/Molex) — never opened,
only replaced.

## On the exam

- **NVMe (PCIe M.2)** is the fastest storage; **SATA SSD** is next; **HDD**
  (7200 > 5400 RPM) is slowest but cheapest per TB.
- RAID: **0 = speed, no redundancy**; **1 = mirror**; **5 = stripe + parity,
  survives one drive**; **10 = mirror + stripe**. Fault tolerance? Never RAID 0.
- **LGA = Intel (pins on the board); PGA = AMD (pins on the chip).**
- **ATX > microATX > Mini-ITX** in size and number of slots. Graphics cards use a
  **PCIe x16** slot.
- **UEFI** adds Secure Boot, GPT (>2 TB), and a GUI over legacy BIOS. A **dead
  CMOS battery (CR2032)** = clock/settings reset each boot.
- Enable **VT-x/AMD-V** in UEFI for virtualization. Reapply **thermal paste** when
  reseating a cooler.
- PSU connectors: **24-pin board, 8-pin EPS CPU, 6/8-pin PCIe GPU, SATA/Molex
  drives.** Rate by **wattage** + **80 PLUS**. **Never open a PSU** — replace it.
