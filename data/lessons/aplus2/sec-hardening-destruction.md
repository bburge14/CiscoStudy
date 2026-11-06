# Workstation Hardening & Data Destruction

Two jobs bookend a workstation's life. **Hardening** is what you do while it's in
service — shrinking the ways an attacker can get in. **Data destruction** is what
you do at the end — making sure the data on a drive can never be read once the
drive leaves your hands. Both are checklists, and the exam tests whether you pick
the *right* item for the stated goal.

## Hardening a workstation

Hardening means closing doors. No single setting does it; you stack several.

### The core measures

- **Keep everything patched.** Regular **OS and application updates / patch
  management** is the ongoing defense against **newly discovered vulnerabilities**.
  When a stem asks the *best ongoing* protection against fresh exploits, it's
  **patching**, not a one-time tweak.
- **Run anti-malware** with **current definitions**, and **enable the host
  firewall**.
- **Disable AutoRun / AutoPlay** so malware can't auto-execute the moment a USB
  stick or disc is inserted.
- **Remove unneeded software and services** (least *functionality*) — fewer
  programs means fewer things to exploit.
- **Encrypt** the drive (BitLocker) and set a **screen lock / inactivity timeout**.

> On shared lab machines, two high-value actions are **disabling AutoRun/AutoPlay**
> and **enabling the firewall / running updated anti-malware** — they cut off the
> easiest infection paths.

### Account management

- Apply **least privilege**: everyday users get **standard** accounts, not admin.
- **Rename or disable the default Administrator** account and **disable the Guest
  account** — both are well-known targets.
- **Change default credentials** on anything that ships with them.
- Require a login; don't leave accounts without passwords.

> Best-practice account hardening: **disable/rename the built-in admin, disable
> Guest, and give users standard (least-privilege) accounts.**

### Strong password policy

A good password policy sets several knobs at once:

| Setting | Best practice |
|---------|---------------|
| **Length** | a sensible minimum (longer is stronger) |
| **Complexity** | mix of character types |
| **Expiration** | change periodically (where policy requires) |
| **History / reuse** | block reusing recent passwords |
| **Account lockout** | lock after a number of failed attempts |

So "two settings that reflect password best practice" are things like a **minimum
length with complexity** and **account lockout after failed attempts** — not
"write it on a sticky note" or "never change it."

### Lock down the firmware and boot path

If a user can change the **boot order** and boot from a **USB stick or live CD**,
they can sidestep Windows security entirely. Stop that with a **BIOS/UEFI
(supervisor) password** plus **disabling boot from external media**.

> To stop users from **changing the boot order or booting external media** to
> bypass Windows, set a **BIOS/UEFI password**.

## Data destruction and disposal

At end of life, the deciding question is simple:

> **Will the drive be reused?** If **no**, you *destroy* it. If **yes**, you
> *sanitize/wipe* it so it still works but the old data is gone.

### Destroying a drive you will NOT reuse

When the drive is done for good, make the data physically unrecoverable:

- **Physical destruction** — **shredding**, **drilling**, **hammering/pulverizing**,
  **incinerating**, or **melting**. Two valid "physical destruction methods" on the
  exam are, for example, **shredding** and **incineration**.
- **Degaussing** — exposing the drive to a **powerful magnetic field** that wipes
  the magnetic domains. It works on **magnetic HDDs and tapes** and leaves the drive
  **unusable** afterward.

> **Degaussing = destroy data with a strong magnetic field.** It only works on
> **magnetic** media — it does **nothing** to an SSD or flash drive, which store
> data electronically, not magnetically.

So a hospital that must make **failed magnetic hard drives** unrecoverable before
they leave the building, with **no plan to reuse** them, uses a destructive method
— **degaussing or physical destruction** (shred/incinerate). Both guarantee the
data is gone; neither leaves a reusable drive.

### Sanitizing a drive you WILL reuse

If the drive stays in service — handed to another department, redeployed — you
can't smash it; you **overwrite** it:

- **Drive wipe / overwrite** (one or more passes of zeros/random data), a
  **low-level format**, or **ATA Secure Erase** make the old data unrecoverable
  while keeping the drive usable.
- A plain **standard/quick format is NOT secure** — it just clears the index, and
  the data is easily recovered. Never treat "I formatted it" as sanitized.

> **Reuse the drive internally but erase the old data → wipe / secure erase**, not
> physical destruction.

### Proving it was done

When a **third-party vendor** destroys drives for you, auditors and compliance want
evidence. The vendor supplies a **certificate of destruction** (or recycling) —
documented proof that **each drive** was destroyed, with serial numbers and dates.

## The whole thing in one paragraph

Harden a workstation by stacking defenses: **patch regularly** (the ongoing fix for
new vulnerabilities), run an updated firewall/anti-malware, **disable
AutoRun/AutoPlay**, enforce a **strong password policy** (length, complexity,
lockout), practice **least privilege** and **disable/rename default accounts**, and
lock the boot path with a **BIOS/UEFI password**. At disposal, decide by reuse:
**not reusing → destroy** (shred/incinerate, or **degauss** magnetic media with a
strong magnetic field), **reusing → wipe / secure erase** (a quick format is *not*
secure), and when a vendor does it, keep the **certificate of destruction** as
proof.

## On the exam

- The **best ongoing** defense against newly discovered vulnerabilities is
  **patch management / regular updates**.
- Account hardening = **least privilege**, **disable/rename the default admin**,
  **disable Guest**, change defaults; password policy = **length + complexity +
  lockout** (and no reuse).
- Stop boot-order bypass with a **BIOS/UEFI password** and by disabling external
  boot media; stop USB auto-infection by **disabling AutoRun/AutoPlay**.
- Disposal decision tree: **reuse → wipe/secure erase** (format alone is not
  secure); **destroy → shred/incinerate or degauss**. **Degaussing** only affects
  **magnetic** media, not SSD/flash.
- A **certificate of destruction** is the documented proof auditors want when a
  third party destroys the drives.
