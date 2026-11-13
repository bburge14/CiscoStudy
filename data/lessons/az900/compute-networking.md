# Azure Compute & Networking

Compute is where your code and workloads actually run; networking is how
everything connects and reaches the outside world. These are the two biggest
families of "core services" on the exam. You are not expected to configure them —
only to know what each service is *for* and to pick the right one from a short
description. This lesson walks the main compute options, then the main networking
options, keeping the focus on "when would I use this?"

## Compute: where workloads run

Azure gives you several ways to run code, trading control for convenience much as
the IaaS/PaaS/SaaS spectrum did.

### Virtual machines (VMs)

> **An Azure virtual machine is a software emulation of a physical computer — an
> IaaS offering where you control the operating system and everything installed on
> it.**

VMs are the most flexible and the most hands-on compute option. You choose the OS,
install what you like, and you are responsible for patching and maintenance. Reach
for a VM when you need **full control**, are running a **legacy or specialized
application**, or are doing a **lift-and-shift** migration of existing servers.

To scale VMs, Azure offers:

- **Virtual Machine Scale Sets** — a group of identical VMs that can automatically
  grow or shrink in number behind a load balancer (horizontal scaling made easy).
- **Availability sets** — a way to spread VMs across fault and update domains so
  maintenance or a hardware fault doesn't take them all down at once.

### Containers

> **Containers package an application with just its dependencies so it runs
> quickly and consistently anywhere, sharing the host operating system instead of
> each carrying a full OS.** They are lighter and faster to start than VMs.

Azure's container options include **Azure Container Instances (ACI)** for running a
single container quickly without managing servers, **Azure Container Apps** for
serverless container-based apps, and **Azure Kubernetes Service (AKS)** for
orchestrating large fleets of containers.

### Azure App Service

> **Azure App Service is a PaaS offering for hosting web applications, REST APIs,
> and mobile back ends without managing the underlying servers or operating
> system.** The platform handles the OS, patching, and scaling for you.

When a scenario says "host a **scalable web app and REST API** without managing
the OS or servers," App Service is the answer. You deploy your code; Azure runs it.

### Azure Functions (serverless)

> **Azure Functions is serverless compute: you write a small piece of code that
> runs only in response to an event or trigger, and you pay only while it runs.**

"Serverless" doesn't mean there are no servers — it means you never think about
them. Functions shine for short, event-driven tasks: respond to a file upload,
process a message on a queue, run on a schedule.

A quick way to choose:

| Need | Service |
|------|---------|
| Full OS control, legacy apps, lift-and-shift | **Virtual machines** |
| Host a web app / REST API without server management | **App Service** |
| Lightweight, portable, consistent app packaging | **Containers (ACI/AKS/Container Apps)** |
| Run small code on an event, pay per execution | **Azure Functions** |

## Networking: how everything connects

### Virtual networks (VNets)

> **An Azure Virtual Network (VNet) is your own private, isolated network in Azure
> — the foundation that lets Azure resources communicate securely with each other,
> the internet, and your on-premises network.** VNets are divided into subnets.

Think of a VNet as your private slice of Azure's network fabric, where you control
addressing and segmentation just as you would on-premises.

### Connecting VNets to each other: peering

> **Virtual network peering connects two VNets so their resources communicate
> privately over Microsoft's backbone network, without traffic ever crossing the
> public internet.**

When two Azure VNets must talk to each other **privately, over the Microsoft
backbone and not the public internet**, the answer is **VNet peering**.

### Connecting to on-premises: VPN Gateway and ExpressRoute

Two services bridge Azure to your own datacenter or users, and the exam loves to
contrast them.

> **A VPN Gateway creates an encrypted tunnel over the public internet.** It comes
> in two flavors:
> - **Site-to-site VPN** connects an entire on-premises network to Azure over the
>   internet, with no dedicated circuit needed.
> - **Point-to-site VPN** connects a *single device* — one remote laptop — securely
>   into an Azure VNet from home.

> **Azure ExpressRoute is a private, dedicated connection to Azure that does not
> travel over the public internet at all, offering more predictable, low-latency,
> higher-bandwidth connectivity.**

The contrast in one line: a **VPN Gateway sends encrypted traffic across the
public internet**, while **ExpressRoute provides a private circuit that bypasses
the internet entirely**. Match the scenario:

- "Branch office needs an encrypted **site-to-site** tunnel over its existing
  internet connection, no dedicated circuit" → **VPN Gateway (site-to-site)**.
- "A **single remote employee's laptop** needs a secure connection from home" →
  **Point-to-site VPN**.
- "A **private, dedicated** connection with **predictable low latency** that does
  **not** cross the public internet" → **ExpressRoute**.

### Other networking pieces to recognize

- **Load balancer** — distributes incoming traffic evenly across multiple backend
  instances, supporting horizontal scale and availability.
- **Azure DNS** — hosting for your domain names, resolving names to IP addresses.
- **Application Gateway** — a web-traffic (layer 7) load balancer with routing and
  a built-in web application firewall option.

## Bringing it together

For compute, move along the control-vs-convenience spectrum: **VMs** for full
control, **containers** for portable packaging, **App Service** for hosting apps
without server chores, and **Functions** for tiny event-driven code. For
networking, the **VNet** is the private foundation; **peering** links VNets over
the backbone; a **VPN Gateway** tunnels over the internet (site-to-site for
networks, point-to-site for a single device); and **ExpressRoute** gives a private
circuit that skips the internet.

## Exam focus

- **Virtual machines** = IaaS, full OS control, best for legacy/lift-and-shift.
  **Scale sets** add identical VMs automatically.
- **App Service** = PaaS hosting for **web apps and REST APIs** with no OS/server
  management. **Azure Functions** = serverless, event-triggered, pay-per-run.
  **Containers** = lightweight, portable app packaging (AKS orchestrates many).
- **VNet** = your private network in Azure. **VNet peering** = private VNet-to-VNet
  traffic over the **Microsoft backbone**, not the internet.
- **VPN Gateway** = encrypted tunnel **over the internet**: **site-to-site** for a
  whole network, **point-to-site** for a single device.
- **ExpressRoute** = **private, dedicated** connection that **bypasses the public
  internet**, with predictable low latency. That "private, not over the internet"
  wording is the ExpressRoute tell.
