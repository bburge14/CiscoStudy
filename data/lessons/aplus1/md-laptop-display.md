# Laptop Hardware & Displays

A laptop is a whole desktop folded into something you can carry, so every part
has been shrunk, soldered, or made to lie flat. That is the one idea that makes
laptop repair make sense: the pieces do the same jobs as desktop parts, but they
come in smaller shapes and they are packed tightly, so you have to know the shape
before you can swap the part.

## The parts you can actually replace

Not everything inside a laptop is removable — more and more is soldered to the
board — but a technician is still expected to swap the field-replaceable pieces.
The common ones:

- **Battery** — almost always **lithium-ion (Li-ion)** or lithium-polymer.
  Older ones pop out behind a latch; many modern ones are internal and held by a
  few screws and a connector. A battery that has **swelled** (puffed up, bowing
  the case or trackpad) is a safety hazard — stop using it, do not puncture it,
  and replace it.
- **Keyboard** — a thin unit held by small screws and a delicate **ribbon
  cable** into a ZIF (zero-insertion-force) connector. Lift the little latch
  before pulling the ribbon or you will tear it.
- **Trackpad / touchpad** — similar ribbon connector underneath.
- **RAM** — see below; uses a special small stick.
- **Storage** — a 2.5" drive or an M.2 card (below).
- **Wireless card** — usually an **M.2 (A/E key)** card with two tiny antenna
  wires clipped on. Those antennas run *up into the display lid* (more on that
  later).

> **Rule of thumb:** if a part has its own cable or screw, treat it as
> replaceable; if it is soldered (CPU, often RAM, often storage on ultrabooks),
> it is not a field swap.

## Laptop memory is SO-DIMM

Desktop RAM sticks are too long for a laptop, so laptops use a shorter stick
called a **SO-DIMM** (Small Outline DIMM). It is the same memory technology as a
desktop — DDR4 or DDR5 — just a smaller physical module.

SO-DIMMs lie flat. You slide the stick into the slot at roughly a 30-degree
angle, then press it down until the two side clips snap over the notches. To
remove one, spread those clips apart and it pops back up to the angle.

> On many thin laptops the memory is **soldered to the board** and cannot be
> upgraded at all — you choose the amount at purchase. Always check before
> promising a customer a RAM upgrade.

## Laptop storage: 2.5" drives and M.2

Laptops use two storage shapes:

- **2.5-inch drive** — the small hard-drive/SSD size (desktops use 3.5"). It
  connects with a **SATA** data+power edge and sits in a caddy.
- **M.2** — a bare stick that lies flat in a slot and is held down by one screw.
  M.2 comes in two flavors that look almost identical, and telling them apart is
  a classic exam point:
  - **M.2 SATA** — runs over the SATA bus, so it is no faster than a 2.5" SSD.
  - **M.2 NVMe** — runs over **PCI Express** lanes, which is dramatically
    faster. **NVMe** (Non-Volatile Memory Express) is the protocol that lets an
    SSD talk straight to the CPU over PCIe instead of the slower SATA path.

> **NVMe vs SATA in one line:** same slot shape is possible, but NVMe uses PCIe
> and is several times faster than anything on SATA.

M.2 cards are described by a size code like **2280** — that is 22 mm wide and
80 mm long. The screw post has to match the length.

## Function keys and special toggles

Laptops fold extra controls onto the keyboard because there is no room for a full
set. The **Fn** key, held with a function key (F1–F12), triggers the icon printed
on that key: screen brightness up/down, volume, keyboard backlight, and so on.
Two toggles show up constantly on the exam:

- **Dual-display / screen-output toggle** — switches between the built-in panel,
  an external monitor, or both (extend/duplicate). On Windows the shortcut is
  **Win+P**.
- **Wireless / airplane toggle** — turns the Wi-Fi and Bluetooth radios off, for
  flights or to save power.
- **Cellular, Bluetooth, and touchpad** on/off keys appear too, plus a physical
  or Fn **webcam privacy** switch on many machines.

## Docking stations and port replicators

A laptop lives two lives — mobile and at a desk. A **docking station** lets you
drop the laptop onto one connector and instantly gain full-size ports: monitors,
wired network, keyboard, mouse, power. A **port replicator** is the simpler
cousin — it just multiplies ports, usually over USB-C, without the proprietary
dock connector. Both save you from plugging in six cables every morning.

## The display: how a laptop screen makes a picture

Now the lid. A laptop display is a thin sandwich, and the exam cares about the
*type of panel* and what lights it up.

Most laptop screens are **LCD** (liquid crystal display). Liquid crystals cannot
make their own light, so an LCD needs a **backlight** behind it. There are three
common LCD panel technologies, and you should know their trade-offs:

| Panel | Strength | Weakness |
|-------|----------|----------|
| **TN** (twisted nematic) | fast, cheap, high refresh | poor color, narrow viewing angles |
| **IPS** (in-plane switching) | best color, wide viewing angles | a bit pricier, slightly slower |
| **VA** (vertical alignment) | deep contrast / blacks | slower response than TN |

> **If a question wants accurate color and wide viewing angles, the answer is
> IPS.** If it wants the cheapest/fastest gaming panel, that is TN.

**OLED** is the other family. An **OLED** (organic LED) panel has *no backlight
at all* — each pixel makes its own light, so black pixels are truly off. That
gives perfect blacks and thin panels, at the cost of possible burn-in over time.

## Backlights and the inverter

Older LCD laptops lit the panel with a **CCFL** (cold-cathode fluorescent lamp)
backlight. A fluorescent tube needs high-voltage AC, but the laptop runs on low-
voltage DC, so those models include an **inverter** — a small board that steps
the DC up to the AC the lamp needs.

> **The inverter is a favorite exam trap.** On a CCFL laptop, a screen that is
> *very dim but still faintly showing an image* often means a failed inverter or
> backlight, not a dead panel — shine a flashlight at the screen and if you can
> just make out the desktop, the pixels work; the light is the problem.

Modern laptops use **LED backlights** instead, which run on DC directly and need
**no inverter**. So if a machine is recent and has no inverter, a dim screen
points at the LED backlight circuit or a brightness setting.

## What else lives in the lid

Because the lid is the highest, most open part of the laptop, several components
ride up there:

- **Wi-Fi / Bluetooth antennas** — the wires from the M.2 wireless card thread up
  through the hinge and run around the screen bezel for the best signal. This is
  why reseating a wireless card can involve working in the display assembly.
- **Webcam and microphone** — mounted in the top bezel, cabled down to the board.
- **Digitizer** — on a touchscreen, the digitizer is the layer that senses your
  finger or stylus and turns touches into coordinates. The LCD shows the picture;
  the digitizer feels the touch. They are two separate layers bonded together.

## The whole thing in one paragraph

A laptop is a desktop shrunk flat: RAM is a short **SO-DIMM** (DDR4/DDR5, often
soldered), storage is a 2.5" SATA drive or an **M.2** card — and M.2 **NVMe**
rides PCIe so it is far faster than **M.2 SATA**. The **Fn** key folds in extra
controls like the Win+P dual-display toggle and the wireless/airplane switch, and
a docking station restores full-size ports at a desk. The screen is usually an
LCD panel — **TN** (fast/cheap), **IPS** (best color and angles), or **VA** (deep
contrast) — needing a backlight, while **OLED** lights each pixel itself for true
blacks. Old CCFL backlights need an **inverter** to make high-voltage AC (a dim-
but-visible screen suggests the backlight/inverter, not the panel); LED
backlights skip the inverter. The lid also carries the Wi-Fi antennas, webcam,
mic, and — on a touchscreen — the digitizer that senses touch.

## On the exam

- **SO-DIMM** = laptop RAM. If asked what memory a laptop takes, it is a SO-DIMM
  (in DDR4 or DDR5), not a full-size DIMM.
- Know **M.2 NVMe (PCIe, fast)** versus **M.2 SATA / 2.5" SATA (slower)**. "Which
  is fastest?" → NVMe.
- **IPS** = best color + viewing angles; **TN** = cheap/fast; **VA** = contrast;
  **OLED** = per-pixel light, perfect blacks, no backlight.
- A **dim screen you can still faintly read** on an older laptop → **backlight or
  inverter**, not the whole display. Shine a flashlight to confirm.
- **LED backlights need no inverter**; only CCFL backlights do.
- The **digitizer** senses touch; the **LCD/OLED** shows the image — separate
  layers.
- Wi-Fi **antennas run up into the display lid**, so lid work can be needed to
  reseat a wireless card.
- A **swollen (puffed) Li-ion battery** is a safety issue — replace it, never
  puncture it.
