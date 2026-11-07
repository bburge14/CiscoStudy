# Secure Baselines, Hardening & Asset Management

Security operations is the daily work of keeping systems safe after they're built.
It starts with two unglamorous but vital habits: configuring systems to a known-
good standard and hardening them (**secure baselines**), and knowing exactly what
you own across its whole life (**asset management**). You can't protect what you
can't configure consistently or don't even know you have.

## Secure baselines: a known-good starting point

> A **secure baseline** is a documented, approved configuration that every system
> of a given type must match. It turns "secure" from an opinion into a checklist.

Baselines have a three-step lifecycle the exam expects you to know:

1. **Establish** — define the baseline: which settings, which services off, which
   passwords required. Often based on an industry **benchmark** (e.g. CIS
   Benchmarks).
2. **Deploy** — apply the baseline to systems, ideally automatically (imaging,
   group policy, configuration-management tools).
3. **Maintain** — keep systems *on* the baseline over time, re-checking and
   correcting drift as patches and changes accumulate.

A baseline that's set once and never maintained slowly rots as systems drift away
from it — maintenance is where most of the value lives.

## Hardening: shrinking a system's attack surface

**Hardening** is the act of locking down an individual system so there's less for
an attacker to grab. The core moves:

- **Change default passwords** — the very first step on anything new.
- **Remove unnecessary software** and disable **unused ports and protocols** —
  every service you don't run is a door that can't be forced.
- Install **endpoint protection** (antivirus/EDR) and enable a **host-based
  firewall** and **HIPS**.
- Apply **encryption** (e.g. full-disk).
- Keep up with **patching**.

### Hardening targets

The same philosophy applies everywhere, but the details differ by device:

- **Workstations and servers** — patch, AV/EDR, host firewall, least privilege.
- **Mobile devices** — managed with **MDM** (Mobile Device Management); enforce
  encryption, screen locks, and remote wipe.
- **Switches and routers** — disable unused services, secure management access,
  use strong admin credentials.
- **Cloud infrastructure** — tighten IAM, security groups, and storage
  permissions.
- **ICS/SCADA, embedded, RTOS, IoT** — these often *can't* be patched or hardened
  the normal way, so you protect them with **segmentation, isolation, and
  monitoring** instead.

### Wireless and mobile specifics

- **Wireless install** uses **site surveys** and **heat maps** to place access
  points for coverage without over-broadcasting signal where attackers could grab
  it.
- **Wireless security** today means **WPA3**, paired with **AAA/RADIUS** for
  enterprise authentication (802.1X) rather than a single shared password.
- **Mobile deployment models** trade control for convenience: **BYOD** (personal
  devices — least control), **COPE** (Corporate-Owned, Personally Enabled — most
  control), and **CYOD** (Choose Your Own Device — a middle ground).
- **Connection methods** to manage include **cellular**, **Wi-Fi**, and
  **Bluetooth**.

### Application hardening and sandboxing

Software gets hardened too: **input validation** (never trust user input),
**secure cookies**, **static code analysis** (scanning source for flaws), and
**code signing** (proving an app hasn't been tampered with). **Sandboxing** runs
untrusted code in an isolated space so it can't harm the real system — great for
testing suspicious files.

## Asset management: you can't protect what you can't see

**Asset management** tracks hardware, software, and data from cradle to grave.
Weak asset management is how forgotten servers go unpatched and old laptops leak
data.

### The asset lifecycle

- **Acquisition / procurement** — bring assets in through an approved process, so
  security is considered *before* purchase, not after.
- **Assignment / accounting** — record **ownership** (who's responsible) and
  **classification** (how sensitive). Every asset should have an owner.
- **Monitoring / tracking** — maintain an **inventory** and **enumeration** of
  what you have and where it is. You can't patch or defend an asset you forgot
  about.
- **Disposal / decommissioning** — retire assets safely at end of life.

### Safe disposal

Retiring hardware is a data-leak risk if done carelessly:

| Method | What it means |
|--------|---------------|
| **Sanitization** | Wipe data so it can't be recovered (while keeping the device usable) |
| **Destruction** | Physically destroy the media (shred, degauss, incinerate) |
| **Certification** | Get documented proof the data was destroyed |
| **Data retention** | Keep required data for the mandated period *before* disposal |

> Before any device leaves your control, its data must be **sanitized or
> destroyed**, and for sensitive assets you want a **certificate of destruction**
> as evidence. Simply deleting files is *not* enough — the data is still
> recoverable.

## The whole thing in one paragraph

Security operations starts with **secure baselines** — approved configurations you
**establish**, **deploy**, and **maintain** (often from benchmarks like CIS) — and
**hardening**, which shrinks a system's attack surface by changing default
passwords, removing unneeded software, disabling unused ports/protocols, adding
endpoint protection and host firewalls, and encrypting. Hardening targets range
from workstations and servers to mobile devices (via **MDM** and **BYOD/COPE/
CYOD** models), network gear, cloud, and hard-to-patch **ICS/SCADA/IoT/embedded**
systems (protected by segmentation and monitoring), plus wireless done right
(**WPA3**, **RADIUS**, site surveys/heat maps) and application hardening (input
validation, code signing, sandboxing). Underpinning it all is **asset
management** — tracking assets through **acquisition**, **assignment** (ownership
and classification), **monitoring/inventory**, and safe **disposal**
(**sanitization**, **destruction**, **certification**, honoring **data
retention**).

## On the exam

- The secure-baseline lifecycle is **establish → deploy → maintain**. Questions
  about systems "drifting out of compliance over time" point to the **maintain**
  phase.
- The first hardening step on any new device is **change the default password**;
  the general principle is **remove/disable everything you don't need**.
- **MDM** manages mobile devices; know the control spectrum: **BYOD** (least
  corporate control) vs. **COPE** (most) with **CYOD** between them.
- **WPA3** is the current wireless standard; enterprise Wi-Fi authenticates via
  **RADIUS/802.1X**, not a shared key.
- For disposal: **sanitize** = wipe but keep the device; **destroy** = physically
  demolish the media; always get a **certificate of destruction** for sensitive
  data. Deleting/formatting is not secure erasure.
- Every asset needs an **owner** and a **classification** — that's the
  "assignment/accounting" step.
- **Sandboxing** is the answer for safely running or testing untrusted code.
