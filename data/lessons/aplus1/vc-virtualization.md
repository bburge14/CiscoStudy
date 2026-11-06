# Client-Side Virtualization

Virtualization lets **one physical computer pretend to be several**. Each
pretend computer — a **virtual machine (VM)** — has its own virtual CPU, memory,
disk, and network card, runs its own operating system, and has no idea it is not
real hardware. "Client-side" just means doing this on a regular PC or workstation,
not in a data center. The piece of software that pulls off the illusion is the
**hypervisor**, and that is where we start.

## The hypervisor: two types

A **hypervisor** creates and runs VMs, slicing the real hardware into virtual
slices and keeping the VMs isolated from each other. There are two kinds, and the
difference is the single most tested idea in this objective.

- **Type 1 (bare-metal)** — the hypervisor is installed **directly on the
  hardware**, with no host OS beneath it. It *is* the operating system of that
  machine. This is what runs servers and data centers because it is fast and
  efficient. *Examples: VMware ESXi, Microsoft Hyper-V (as a role), Citrix
  XenServer, Proxmox.*
- **Type 2 (hosted)** — the hypervisor runs **as an application on top of a
  normal OS** (Windows, macOS, Linux). You double-click it like any program and
  create VMs inside it. This is the usual **client-side** choice on a technician's
  laptop. *Examples: VMware Workstation/Player, Oracle VirtualBox, Parallels.*

> **Type 1 sits on the bare metal (no host OS); Type 2 sits on top of a host OS.**
> On a desktop you almost always use **Type 2**; in the server room it is **Type
> 1**.

## Why run virtual machines?

VMs are not just a party trick — they solve real problems, and the exam lists the
purposes:

- **Sandboxing** — run risky or unknown software (even suspected malware) in an
  isolated VM. If it breaks or infects anything, it is trapped inside the VM and
  cannot touch the real machine. Delete the VM and the mess is gone.
- **Test / development** — try new software, patches, or OS builds safely before
  rolling them out, and spin up clean environments on demand.
- **Legacy software / OS support** — keep an old application alive by running the
  old OS it needs (say, Windows 7) in a VM on a modern PC.
- **Cross-platform** — run a different OS from your main one (Linux on a Windows
  laptop, Windows on a Mac) without rebooting.
- **Application virtualization** — stream or run a single app in an isolated
  bubble rather than installing it fully.
- **Training and labs** — give each learner a disposable environment (exactly how
  practice labs for this exam are built).

> If a question describes **safely running untrusted software or testing in
> isolation**, the answer is a **VM / sandbox** — the host is protected because
> the VM is walled off.

## What a VM needs: resource requirements

Every VM draws from the host's real resources, so the host must have enough to go
around. This is a reliable exam theme — the host needs **more** than the sum of
its guests:

- **CPU with virtualization support** — the processor must support **Intel VT-x**
  or **AMD-V**, and that feature must be **enabled in UEFI/BIOS**. A common
  real-world failure is a VM that will not start until virtualization is turned on
  in firmware.
- **Enough RAM** — each VM reserves memory from the host. Run three VMs that each
  want 4 GB and the host needs 12 GB *plus* enough for itself. Too little RAM and
  everything crawls.
- **Disk space** — each VM stores its virtual disk as a large file; several VMs
  eat storage fast. SSDs greatly improve VM responsiveness.
- **Networking** — a VM gets a **virtual NIC**; the hypervisor can bridge it onto
  the real network, share the host's connection (NAT), or keep it host-only.

> **No virtualization support, no VMs.** If a Type-2 hypervisor errors out at
> start, check **VT-x/AMD-V is enabled in UEFI** before anything else.

## Security and network requirements

Virtualization adds its own safety concerns:

- **Isolation is a feature, but not a guarantee.** Keep hypervisors patched; a
  flaw that lets code "escape" a VM onto the host is called a **VM escape** and is
  the worst-case risk.
- **Network segmentation** — a sandbox VM analyzing malware should usually be kept
  **off the production network** (host-only or an isolated segment) so nothing
  leaks out.
- Treat each guest OS like a real PC: it needs its own updates, antivirus, and
  secure configuration.

## Pieces of a VM you should recognize

- **Virtual disk** — a file on the host that acts as the VM's hard drive.
- **Virtual NIC** — the VM's network card, attached to a virtual switch.
- **Snapshot** — a saved point-in-time state of a VM. Take one before a risky
  change, and if it goes wrong, **revert** to the snapshot in seconds. This is
  what makes VMs ideal for testing.

### A word on containers and emulators

Two neighbors of virtualization sometimes appear:

- A **container** packages just an application and its dependencies and shares the
  host's OS kernel — lighter than a full VM, but not a separate OS. (Covered more
  on Network+; on A+ just know it is lighter-weight than a VM.)
- **Emulation** imitates *different* hardware (running a phone OS or an old game
  console on your PC), which is slower than virtualization because it translates
  instructions rather than slicing the same CPU.

## The whole thing in one paragraph

Client-side virtualization runs several **virtual machines** on one PC via a
**hypervisor**, which is either **Type 1 (bare-metal, no host OS — servers/data
centers)** or **Type 2 (hosted, runs as an app on a normal OS — the usual desktop
choice)**. VMs are used for **sandboxing** risky software safely, **test/dev**,
keeping **legacy** apps alive, running a **cross-platform** OS, app
virtualization, and **training labs**. The host must have the resources the guests
borrow: a CPU with **VT-x/AMD-V enabled in UEFI** (no support, no VMs), enough
**RAM** and **disk**, and **networking** through a **virtual NIC**. Security means
patching the hypervisor (to prevent **VM escape**) and segmenting sandbox VMs off
production, while **snapshots** let you revert a VM instantly after a risky change.

## On the exam

- **Type 1 = bare-metal, no host OS** (data centers); **Type 2 = hosted on a
  normal OS** (desktop/laptop). This distinction is the most tested point.
- A **VM / sandbox** is the answer for **safely running untrusted software** or
  testing in isolation — the host is protected.
- VMs need a CPU with **Intel VT-x / AMD-V enabled in UEFI/BIOS**; a hypervisor
  that will not start usually means virtualization is **disabled in firmware**.
- The host must have **enough RAM and disk for all guests plus itself** — more
  than any single VM.
- A **snapshot** saves a VM's state so you can **revert** after a bad change.
- **VM escape** (guest breaking out to the host) is the key virtualization
  security risk — keep hypervisors patched and sandboxes off production networks.
