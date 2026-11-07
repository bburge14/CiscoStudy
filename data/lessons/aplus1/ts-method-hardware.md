# The Troubleshooting Method, Hardware & Displays

Troubleshooting is the heart of the A+ — nearly a third of Core 1 is about
finding and fixing faults. But CompTIA does not just want the *answer*; it wants
you to follow a **method** so you fix the right thing without making new problems.
Learn the six steps first, then apply them to the two most common fault areas:
the hardware that will not run and the display that will not show.

## The CompTIA six-step troubleshooting method

Memorize these six steps **in order** — the exam asks "what do you do next?" and
the only way to answer is to know where you are in the sequence.

> **1. Identify the problem → 2. Establish a theory of probable cause → 3. Test
> the theory → 4. Establish a plan and implement the solution → 5. Verify full
> functionality (and prevent recurrence) → 6. Document.**

Walking through each:

1. **Identify the problem.** Gather information and **question the user**. Ask
   what changed, reproduce the symptom if you can, and check recent changes
   (updates, new hardware). Crucially, **back up data before you make changes** —
   so a fix never costs the user their files.
2. **Establish a theory of probable cause.** Form your best guess, and
   **question the obvious** first (is it plugged in? is the cable loose?). Start
   simple before exotic.
3. **Test the theory to determine the cause.** Try it. **If the theory is
   confirmed**, move on. **If it is not**, establish a *new* theory — or
   **escalate** if it is beyond you. Do not plow ahead on a disproven guess.
4. **Establish a plan of action and implement the solution.** Decide the steps
   (and their impact) to fix it, then do them, following any change procedures.
5. **Verify full system functionality**, and **if applicable, implement
   preventive measures** so the problem does not come back.
6. **Document** the findings, actions, and outcomes, so the next technician — or
   you, in six months — benefits.

> Two step-specific trap answers: **"back up the data"** belongs in **step 1**
> (before changes), and **"document"** is always **last**. If a theory test
> *fails*, the next move is a **new theory or escalation**, never jumping to a
> fix.

## Troubleshooting hardware that will not run

With the method in hand, turn to failing hardware. The first clue is often the
**POST** — the Power-On Self-Test the firmware runs at startup. If it finds a
fatal fault, you get **beep codes** or a blank screen instead of a boot.

### Power and POST symptoms

- **No power at all** (no lights, no fans) — check the wall outlet, the PSU
  switch, the **115/230 V** selector, and the power connections. A dead PSU is a
  prime suspect; swap to test.
- **Powers on but no POST / no display** — reseat RAM and the GPU, listen for
  **beep codes**, and clear CMOS. Bad or unseated **RAM** is a classic "fans spin
  but nothing on screen" cause.
- **Continuous reboots** or **unexpected/intermittent shutdowns** — very often
  **overheating** (clogged fans, failed cooler, dried thermal paste) or a failing
  PSU. The system protects itself by cutting power.
- **System lockups / app crashes / BSOD** — can be bad RAM, overheating, or
  driver faults. A **blue screen** (BSOD) that names memory, or random crashes,
  points at **RAM** — test with a memory diagnostic.

### Dangerous and physical symptoms

- **Burning smell or smoke** — cut power **immediately**; this is usually a
  failing PSU or a shorted component and is a safety hazard.
- **Loud whining or grinding noise** — a failing fan bearing or, from a hard
  drive, failing mechanics.
- **Swollen / bulging capacitors** on the motherboard (or a swollen battery) —
  visible physical failure; the part must be replaced.
- **Inaccurate system date/time** that resets every power-off — a dead **CMOS
  battery (CR2032)**. Simple and commonly tested.

### Storage-specific symptoms

Storage failures have their own tell-tales:

- **Clicking noise** from a hard drive ("click of death") = failing heads/
  mechanics — back up **now**.
- **Grinding** = mechanical HDD failure.
- **Slow read/write, long boots, frequent freezes** = a dying drive or a nearly
  full one.
- **S.M.A.R.T. errors** = the drive's self-monitoring is warning of impending
  failure — replace it before it dies.
- **Boot failures / "no boot device"** = check boot order in UEFI, cabling, or a
  failed drive.
- **LED status / activity lights** help: a drive light stuck on or off is a clue.

> With any sign of drive failure — **clicking, grinding, or S.M.A.R.T.
> warnings** — the first action is almost always **back up the data immediately**,
> because the drive may not survive long.

## Troubleshooting displays

Display problems split into "no picture" and "bad picture," and the fix depends on
which parts are involved: the panel, the backlight, the cable, or the GPU.

### No image or dim image

- **No image at all** — confirm power and the correct **input/source**, reseat or
  swap the **video cable**, and test a second monitor to isolate monitor vs PC.
  On a laptop, try the **external-display toggle** (Win+P) in case output was
  switched.
- **Dim image** — on a laptop, check **brightness** first, then suspect the
  **backlight or inverter** (shine a flashlight: if you can faintly see the
  desktop, the panel works and the backlight is the fault).

### Bad-picture symptoms

- **Flickering** — a loose cable, a wrong/low **refresh rate**, or a failing
  backlight.
- **Dead pixels** — pixels stuck black; a small number is often a panel defect.
- **Burn-in / image persistence** — a faint ghost of a static image, common on
  OLED/plasma; vary the content and use screen savers to avoid it.
- **Color patches / wrong colors** — often a loose cable (a bent pin on an analog
  cable), a color-calibration issue, or a failing panel.
- **Artifacts / distortion / strange patterns** — frequently a **GPU**
  overheating or failing, or a bad driver.
- **Geometry / oversized images and icons** — usually the **resolution** is set
  wrong or the **GPU driver** is missing (Windows falls back to a low generic
  resolution).

### Projector symptoms

- **Projector shuts off after a while / overheats** — a clogged filter or failing
  fan; the lamp runs hot and the unit self-protects.
- **Dim projector image** — an aging **lamp/bulb** nearing end of life.

## The whole thing in one paragraph

CompTIA's method is six ordered steps — **identify** the problem (question the
user, **back up first**), **theorize** the cause (question the obvious), **test**
the theory (confirm → proceed; fail → new theory or **escalate**), **plan and
implement** the fix, **verify** functionality and prevent recurrence, and
**document** last. Applied to hardware, a blank **no-POST** with spinning fans
points at **RAM/GPU reseating** and **beep codes**; reboots, intermittent
shutdowns, and lockups usually mean **overheating** or a failing **PSU**; a
burning smell means **cut power now**; a clock that resets means a **dead CMOS
battery**; and drive **clicking, grinding, or S.M.A.R.T.** warnings mean **back up
immediately**. For displays, isolate **no image** (source, cable, toggle) from a
**dim image** (brightness, then backlight/inverter), while flickering, dead
pixels, burn-in, wrong colors, and **artifacts** map to cables, panel defects,
refresh rate, or a failing **GPU/driver**, and projectors that cut out are
**overheating** (dim = aging lamp).

## On the exam

- Know the **six steps in order**. "Back up data" = step 1 (before changes);
  "document" = step 6 (last). A failed theory test → **new theory or escalate**,
  not a fix.
- **Fans spin, no display** → reseat **RAM/GPU**, listen for **beep codes**.
- **Random reboots / intermittent shutdowns** → **overheating** or a failing
  **PSU**. **Burning smell/smoke** → **power off immediately.**
- **Clock/date resets each boot** → dead **CMOS battery (CR2032)**.
- Drive **clicking/grinding/S.M.A.R.T.** warning → **back up the data now**;
  failing drive.
- **Dim laptop screen** (faint image visible) → **backlight/inverter**, not the
  panel. **No image** → check **source, cable, and the display toggle**.
- **Artifacts/distortion** → failing/overheating **GPU** or bad driver;
  **oversized icons / wrong geometry** → wrong **resolution/driver**.
