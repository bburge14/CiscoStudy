# Cloud & Virtualization Security

Almost every organization now runs on virtualized and cloud infrastructure, and
both change the security picture in ways the exam probes carefully. Virtualization
packs many systems onto shared hardware; cloud rents that capacity from a provider
and splits security duties between you and them. This lesson covers the models, the
shared-responsibility line, and the isolation risks unique to these environments.

## Cloud service models

> **IaaS (Infrastructure as a Service)** rents raw compute, storage, and network
> (you manage the OS and up). **PaaS (Platform as a Service)** provides a managed
> platform to deploy your code (you manage the app and data). **SaaS (Software as
> a Service)** delivers finished applications (you manage mostly just your data and
> access).

As you move IaaS -> PaaS -> SaaS, the provider manages more and you manage less.
That ladder directly determines the shared-responsibility split below.

## Cloud deployment models

> **Public** cloud is shared, multi-tenant infrastructure open to many customers.
> **Private** cloud is dedicated to one organization. **Community** cloud is shared
> by several organizations with **common requirements** (e.g., a group of hospitals
> or agencies with the same regulatory needs). **Hybrid** combines two or more,
> connected together.

The community-cloud scenario is a frequent exam item: *several hospitals jointly
build and share a cloud tailored to their common regulatory and security
requirements* — that's a **community cloud**, not public or private.

## The shared responsibility model

This is the single most important cloud-security concept:

> Under the **shared responsibility model**, the **provider** secures the cloud
> *infrastructure* ("security **of** the cloud") and the **customer** secures what
> they put in it — their data, configurations, identities, and access ("security
> **in** the cloud").

The exact line shifts by service model, but the customer **always** owns their data
and access management. This explains the most common cloud breach:

> A storage bucket left **publicly accessible** with sensitive data is the
> **customer's misconfiguration**, not a provider failure. The fix is the
> customer's: correct the access policy, block public access, and enforce least
> privilege.

Tools that help: a **CASB (Cloud Access Security Broker)** enforces policy between
users and cloud services; **CSPM (Cloud Security Posture Management)** continuously
finds misconfigurations; and **IAM** discipline (least privilege, MFA) governs who
can do what.

## Multi-tenancy risks

Public cloud means your workloads share physical hardware with strangers:

> **Multi-tenancy** means multiple customers' workloads run on the same underlying
> hardware. The core concern is **isolation failure** — weak logical separation
> that could let one tenant access or affect another's data (**data commingling**),
> or a **"noisy neighbor"** consuming shared resources.

Strong **logical isolation**, encryption of your own data (ideally with keys you
control), and knowing your **data residency/sovereignty** (which country your data
physically sits in, for legal reasons) are the mitigations.

## Virtualization: the hypervisor and its risks

Underneath much of the cloud sits **virtualization**. A **hypervisor** creates and
runs virtual machines, each believing it has its own hardware.

- **Type 1 (bare-metal)** hypervisors run directly on hardware (ESXi, Hyper-V) —
  the enterprise standard.
- **Type 2 (hosted)** hypervisors run on top of a host OS (VirtualBox) — for
  desktops and labs.

The hypervisor is the crown jewel:

> Because the hypervisor controls **every** guest VM, its compromise can expose or
> control all of them at once — collapsing the isolation every VM depends on. That
> makes patching and protecting the hypervisor critically important.

Other virtualization risks:

- **VM escape** — a dangerous attack where code **breaks out of a guest VM** to
  reach the hypervisor or other VMs, defeating isolation.
- **VM sprawl** — uncontrolled proliferation of VMs that go unpatched and
  unmonitored (ties to asset management).
- **Snapshot rollback risk** — reverting a VM to an older snapshot can
  **reintroduce previously patched vulnerabilities** and undo security changes; and
  snapshots may **store sensitive data** (like keys) that must be protected.

## Containers vs VMs

Containers (Docker, Kubernetes-orchestrated) are lighter than VMs but isolate
differently — an important security distinction:

> A **container shares the host operating system's kernel** (OS-level
> virtualization), making it lightweight and fast but giving it a **weaker
> isolation boundary** than a full VM, which includes its own guest OS. A
> kernel-level compromise can therefore affect all containers on that host.

Container security means using **trusted/minimal base images**, scanning images for
vulnerabilities, not running as **root**, securing the **orchestrator** (Kubernetes
RBAC, secrets management), and protecting the shared host kernel. Serverless and
microservices push this further, trading infrastructure management for a larger
reliance on provider security and good configuration.

## Exam focus

- Service models: **IaaS -> PaaS -> SaaS**, provider manages more as you go up.
  Deployment: **public, private, community** (shared by orgs with common needs),
  **hybrid**.
- **Shared responsibility**: provider secures *of* the cloud; customer secures *in*
  the cloud (**always** your data + access). A **public S3-style bucket leak is the
  customer's misconfiguration** — fix access policy / block public access.
- **Multi-tenancy** risk = **isolation failure / data commingling / noisy
  neighbor**; mitigate with logical isolation, encryption, and data-residency
  awareness. A **CASB/CSPM** helps enforce and monitor.
- **Hypervisor compromise exposes all guest VMs** — patch it; **VM escape** breaks
  out of a guest; reverting a **snapshot can reintroduce patched vulnerabilities**.
- A **container shares the host kernel** -> lighter but **weaker isolation** than a
  VM. Secure images, avoid root, harden the orchestrator and host.
