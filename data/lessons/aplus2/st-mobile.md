# Mobile OS Troubleshooting

Phones and tablets fail in their own ways, and the fixes follow the same
least-invasive-first rule you use everywhere else: **restart the app before the
device, update before you reinstall, reinstall before you factory-reset.** The exam
gives you a symptom and wants the *correct first move* — and sometimes the correct
move is a safety call, not a software step.

> **Climb the ladder:** force-stop the app → restart the device → update/reinstall
> the app → check settings/certificates → factory reset as a last resort.

## Suspect malware when the battery, heat, and data all spike together

A single symptom rarely means malware, but a **cluster** does:

- Sudden **poor battery life**,
- the device **runs hot even when idle**, and
- a **spike in cellular data usage**.

Together, those point to **malware or a misbehaving app** running in the background
— using the CPU (heat + battery) and phoning home (data). This is especially likely
right after the user **sideloaded an app from an APK** obtained **outside the
official store**, which bypasses the store's vetting.

> **Battery drain + overheating + data spike = suspect mobile malware**, most often
> from a **sideloaded / untrusted app**.

The fix: identify and **uninstall the suspect app**, run a reputable mobile
anti-malware scan, review app **permissions**, install OS updates, and **factory
reset** only if it can't be cleaned. Prevention is simpler — install apps **only
from the official store** and keep sideloading off.

## A swollen battery is a safety stop, not a software bug

If a phone has a **bulging back cover** and a **swollen battery pushing the screen
up**, that is a physical **hazard**, not something you troubleshoot in software.

> **Stop using it immediately. Power it down, do not charge it, and never puncture
> or bend it.** A swollen lithium battery can rupture or catch fire. Replace the
> battery (or device) and dispose of the old one through **proper battery
> recycling** / regulated e-waste.

This is the one mobile question where the "fix" is to put the device down and handle
it safely.

## One app misbehaves while everything else is fine

When **one app** repeatedly **crashes or won't load** but every other app works,
the problem is that app, not the OS. Work up the ladder:

1. **Force-stop** the app and reopen it.
2. **Clear the app's cache/data**.
3. **Update** the app (a bug may already be fixed).
4. **Uninstall and reinstall** it.

The best *first* step is usually to **update or reinstall the problem app** — you
don't reset the whole phone for one broken app.

## A totally frozen device

If the device is **completely frozen** — touchscreen unresponsive, no button brings
up a menu — the first thing to try is a **soft reset (force restart)**: the
manufacturer's **button combination** that forces a reboot (for example, holding
power, or a specific volume+power sequence). It's the mobile equivalent of
power-cycling, and it loses no data.

> Frozen and unresponsive → **force restart (soft reset)** first, before anything
> drastic.

## Connectivity: Bluetooth won't pair

A phone that **won't connect to a new Bluetooth headset** — both charged and nearby
— usually isn't broken; the accessory just isn't **discoverable**. Put the headset
into **pairing mode** so the phone can find it, then pair. If it still fails,
**remove/"forget" the device** and pair again from scratch.

## Email: encrypted messages won't open

A subtle one: the user can **send and receive normal email** fine, but **encrypted
(S/MIME) messages** fail with a **decryption / certificate error**. Normal mail
working rules out a broken account or connection — the issue is the **S/MIME
certificate**. The fix is to **install/reinstall the user's valid S/MIME
certificate (and private key)** on the device so it can decrypt the messages.

> Plain mail works but **encrypted (S/MIME)** mail throws a cert error → it's a
> **certificate problem**, so **reinstall the S/MIME certificate/key**.

## A few more everyday symptoms

The same climb-the-ladder logic covers the rest of the common calls:

- **No wireless connectivity / can't reach Wi-Fi** — first toggle **Airplane mode**
  off/on (or Wi-Fi off/on) to reset the radios; then forget and rejoin the network,
  and check the router.
- **Weak or dropped cellular signal** — move to better coverage, toggle Airplane
  mode, and confirm the account/SIM; a case or location can block reception.
- **Slow performance / laggy device** — close background apps, free up **storage**
  (a nearly full device slows down), reboot, and install pending updates.
- **Won't charge** — check the **cable, charger, and port** (lint in the port is
  common) before blaming the battery.
- **GPS/location is wrong** — enable high-accuracy location and toggle it off/on.

> Reach for the **least disruptive** fix first — toggling a radio, closing apps, or a
> reboot — and keep a **factory reset for last**, after backing up the user's data.

## The whole thing in one paragraph

Troubleshoot mobile devices least-invasively: a cluster of **battery drain +
overheating + data spike** (often after a **sideloaded APK**) means **malware** —
uninstall the app, scan, update, reset only as a last resort. A **swollen/bulging
battery** is a **safety stop**: power down, don't puncture, replace and recycle. One
**crashing app** → **update/reinstall that app**, not the phone. A **frozen device**
→ **force restart (soft reset)**. A new **Bluetooth** accessory that won't connect →
put it in **pairing mode** (or forget and re-pair). And normal email working while
**encrypted S/MIME** fails is a **certificate** issue — reinstall the S/MIME cert.

## On the exam

- **Battery drain + heat + data spike**, especially after a **sideloaded app**, =
  **mobile malware** → remove the app, scan, (factory reset last).
- A **swollen battery** is a safety hazard: **stop, power off, don't puncture,
  recycle** — it is not a software fix.
- One app crashing while others work → **update/reinstall that app**; a **frozen,
  unresponsive** device → **force restart (soft reset)** first.
- **Bluetooth won't pair** → enable **pairing mode / discoverable**, or forget and
  re-pair.
- Normal mail fine but **encrypted (S/MIME)** mail errors → a **certificate
  problem**; reinstall the S/MIME certificate.
