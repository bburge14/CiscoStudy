# Peripherals & Printers

Peripherals are everything you plug into a computer to get data in or out, and
printers are the one peripheral complex enough to earn their own objective — the
A+ even expects you to recite the laser printing process step by step. We will
start with the simple peripherals, then slow down and really learn the printers.

## Peripherals: input and output

A quick way to sort peripherals is by direction. **Input** devices send data
*in*; **output** devices push results *out*; some do both.

- **Input:** keyboard, mouse, touchpad, **webcam**, microphone, **scanner**
  (flatbed or with an ADF — Automatic Document Feeder), signature pad, game
  controller, **barcode / QR scanner**, and a card reader.
- **Output:** **monitor**, speakers, **projector**, headset.
- **Both / storage:** external drives, flash drives, **touchscreens** (display +
  input), and a **KVM switch** (one Keyboard, Video, Mouse driving several PCs).

### Expansion cards

When a motherboard lacks a feature, you add a **PCIe expansion card**: a
**graphics card (GPU)** for video, a **sound card** for better audio, a **capture
card** to record video, or a **NIC** for extra/faster networking. Each drops into
a PCIe slot sized to its lane count.

> Match the card to the slot: a GPU needs a **PCIe x16** slot and often its own
> **PCIe power** connector from the PSU; small cards use short x1 slots.

## Printer families

Four printing technologies dominate the exam, plus 3D printing:

| Type | How it marks paper | Typical use |
|------|-------------------|-------------|
| **Laser** | toner fused by heat | office, high volume |
| **Inkjet** | liquid ink sprayed from a head | home, photos |
| **Thermal** | heat on special paper | receipts, labels |
| **Impact** | pins strike a ribbon | multipart carbon forms |

### Inkjet printers

An inkjet sprays tiny droplets of liquid **ink** from a moving **print head** on
a **carriage** that slides across the page on a belt, while **rollers / a feeder**
pull paper through. Key terms: **ink cartridges**, **duplexing assembly**
(two-sided printing), and **calibration** (aligning the heads so colors and lines
line up). Clogged heads cause missing colors or streaks — run the cleaning cycle.

### Thermal printers

A **thermal** printer has a **heating element** that darkens **special
heat-sensitive paper** as a **feed assembly** rolls it past. No ink, no toner —
which is why **receipts** fade over time and why the main maintenance is keeping
the head clean and loading the right thermal paper.

### Impact printers

An **impact** (dot-matrix) printer has a **print head** of pins that strike an
**inked ribbon** against the paper, so it physically dents the page. That impact
is why it is still used for **multipart carbon forms** (invoices, shipping
copies) — the blow prints through all the layers at once. It uses **tractor feed**
(the paper with sprocket holes on the edges). Consumable: the **ribbon**.

### 3D printers

A **3D printer** builds an object in layers, either melting plastic **filament**
(FDM) or curing liquid **resin** with light. The object forms on a **print bed**.

## The laser printer — and its seven steps

Laser printers are the exam's deepest printer topic because the **imaging
process** has a fixed order you must know. First, the parts: the **imaging drum**
(photosensitive), the **charge roller (primary corona)**, the **laser/scanner
assembly**, the **toner** (fine powder), the **transfer roller/belt**, the
**fuser** (hot rollers), and the **pickup/separation rollers** that feed paper.

Here is the sequence — memorize the order:

> **The 7 steps: Processing → Charging → Exposing → Developing → Transferring →
> Fusing → Cleaning.**

1. **Processing** — the printer receives the page and builds the full raster
   image in memory.
2. **Charging** — the charge roller applies a uniform **negative charge** across
   the drum, wiping it to a blank slate.
3. **Exposing** — the **laser** writes the image by discharging the spots that
   will hold toner, leaving an invisible electrostatic image on the drum.
4. **Developing** — negatively charged **toner** is attracted to the discharged
   (exposed) areas, so the image on the drum is now made of toner.
5. **Transferring** — the charged **transfer roller** pulls the toner off the drum
   onto the paper. At this point the toner is only sitting loosely on the page.
6. **Fusing** — the hot **fuser** rollers melt the toner and press it permanently
   into the paper. (This is why a freshly printed sheet is warm.)
7. **Cleaning** — any leftover toner is scraped off the drum and the drum is
   electrically reset, ready for the next page.

> A memory hook: **"Please Charge Every Dog's Tail For Cleaning."** Mixing up the
> order — especially putting **fusing** anywhere but near the end — is the classic
> way to lose this question.

A few fault cues that follow directly from the steps: faint/light print often
means **low toner**; toner that **smears or rubs off** points at a failed
**fuser**; a repeating mark down the page is usually a scratch or defect on the
**drum**.

## Connecting and sharing printers

Printers attach by **USB** (one PC), **wired Ethernet**, or **Wi-Fi** (any device
on the network). To share one printer with many users you either enable Windows
**printer sharing** on a host PC or use a dedicated **print server** (a box or a
server role) that queues and dispatches jobs. Cloud/mobile printing adds options
like network discovery and vendor apps.

Before a printer works you install the correct **driver** and often set the right
**page description language** (**PCL** or **PostScript**) so the computer and
printer speak the same language.

## Printer maintenance and consumables

Each type has its own consumables and upkeep: laser = **toner cartridge** and
periodic **maintenance kit** (fuser and rollers); inkjet = **ink cartridges**,
head **cleaning/calibration**; thermal = **thermal paper** and head cleaning;
impact = **ribbon** and replacing the **print head**. Always follow the
manufacturer's maintenance cycle to avoid jams and quality problems.

## The whole thing in one paragraph

Peripherals split into **input** (keyboard, mouse, scanner/ADF, webcam, barcode
reader), **output** (monitor, projector, speakers), and both/storage (touchscreen,
external drives, **KVM**), with **PCIe expansion cards** (GPU, sound, capture,
NIC) adding missing features. Printers come as **laser** (toner fused by heat),
**inkjet** (liquid ink from a moving head), **thermal** (heat on special paper,
for receipts), **impact** (pins + ribbon for multipart forms), and **3D**
(filament/resin on a bed). The laser **imaging process** runs in a fixed order —
**Processing, Charging, Exposing, Developing, Transferring, Fusing, Cleaning** —
and its symptoms map to parts (light = toner, smearing = fuser, repeating marks =
drum). Printers connect by **USB, Ethernet, or Wi-Fi**, are shared via Windows
sharing or a **print server**, need the right **driver/PCL/PostScript**, and each
type has its own consumables.

## On the exam

- Recite the **laser steps in order**: **Processing → Charging → Exposing →
  Developing → Transferring → Fusing → Cleaning.** Order questions are guaranteed.
- Laser symptoms: **light print = low toner**, **smears/rubs off = fuser**,
  **repeating defect = drum.**
- **Impact** printers (pins + ribbon) are the answer for **multipart/carbon
  forms**; **thermal** (heat + special paper) is the answer for **receipts**.
- **Inkjet** uses liquid ink and needs **head cleaning/calibration**; missing
  colors = clogged head.
- A **KVM switch** runs multiple PCs from one keyboard/video/mouse set.
- Share a printer with Windows **printer sharing** or a **print server**; install
  the correct **driver** (PCL or PostScript).
- A **GPU** needs a **PCIe x16** slot and usually its own PCIe power lead.
