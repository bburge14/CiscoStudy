# Network Defense & Secure Infrastructure

Now that you know the threats, here are the tools and designs that stop them. This
lesson has two halves: the **defensive technologies** that protect network traffic
(firewalls, IDS/IPS, VPNs, segmentation, and more), and the **secure
infrastructure** choices that protect systems and facilities (cloud service
models, DMZs, and data-center controls). Together they form the defensive side of
network security.

## Network defense technologies

### Firewalls

> A **firewall** sits at the boundary between networks — typically between a
> company's internal network and the internet — and allows or blocks traffic
> according to a set of rules.

The firewall is the gatekeeper of the perimeter. It usually works on **implicit
deny**: permit only what the rules allow, drop everything else.

### IDS vs. IPS

Two intrusion technologies are often confused; the difference is whether they can
**act**.

> An **IDS (Intrusion Detection System)** passively monitors traffic and **raises
> an alert** on suspicious activity, but does **not** block it. An **IPS
> (Intrusion Prevention System)** sits **inline** and can **automatically block**
> malicious traffic in real time.

- **IDS** = detect and alert (a smoke detector — it warns you).
- **IPS** = detect and **stop** (a sprinkler — it acts). When a scenario wants a
  device that blocks malicious packets itself, the answer is **IPS**.

### VPNs

> A **VPN (Virtual Private Network)** creates an encrypted tunnel across an
> untrusted network like the public internet, so a remote user's traffic stays
> private.

A remote employee uses a VPN to connect to the corporate network with their
traffic protected inside the tunnel — defending against eavesdropping and
man-in-the-middle attacks.

### Segmentation and zero trust

> **Network segmentation** divides a network into smaller, isolated zones so that
> a compromise in one zone can't easily spread to the others.

Segmentation limits an attacker's lateral movement. A complementary modern model
is **zero trust**, which assumes **no user or device is trustworthy by default —
even inside the network — and verifies every access request explicitly.** "Never
trust, always verify" is its motto.

### Host and wireless defenses

- **Antivirus / anti-malware** — host-based software that detects, quarantines,
  and removes viruses, Trojans, and other malicious software.
- **Application allowlisting (whitelisting)** — configuring systems so that
  **only a pre-approved set of applications may run**, and everything else is
  blocked by default. It's far stronger than trying to block known-bad software.
- **Wireless encryption** — use **WPA2 or WPA3** to secure Wi-Fi. The older
  **WEP** is long broken and must not be used.

### Proxies, honeypots, and air gaps

- **Proxy server** — an intermediary that sits between internal users and the
  internet, forwarding their web requests, caching content, and able to filter or
  log which sites they visit.
- **Honeypot** — a deliberately vulnerable-looking **decoy** system that holds no
  real data, deployed purely to attract attackers, waste their time, and study
  their techniques. Any interaction with it is suspicious by definition.
- **Air gap** — the most extreme isolation: keeping a highly sensitive system
  **physically disconnected** from the internet and all untrusted networks.

## Secure infrastructure

Defending traffic is only half the job; you also have to make smart choices about
*where and how* systems run.

### Cloud service models

When you use the cloud, how much you manage versus how much the provider manages
depends on the service model. Learn the three and who's responsible for what.

| Model | Provider manages | Customer manages | Example |
|-------|------------------|------------------|---------|
| **IaaS** (Infrastructure as a Service) | The physical infrastructure: VMs, storage, networking | The operating systems and applications on top | Renting virtual machines |
| **PaaS** (Platform as a Service) | The platform: OS, runtime, and tools | Only their own application code | A managed app-hosting platform |
| **SaaS** (Software as a Service) | Everything — the whole application | Nothing but their data and usage | Web-based email |

The pattern is a spectrum: with **IaaS** the customer manages the most (OS and
up), with **SaaS** the customer manages the least (just uses the finished app),
and **PaaS** sits in the middle. A **private cloud** is infrastructure dedicated
exclusively to one organization (not shared with other tenants), giving more
control over security and compliance.

### Network placement: the DMZ

> A **DMZ (demilitarized zone), also called a screened subnet,** is a buffer
> network between the internet and the internal network where public-facing
> servers are placed.

If you must host a public web server reachable from the internet, you put it in
the **DMZ**, not on the internal network. That way, if the exposed server is
compromised, the attacker still isn't inside your trusted internal network.

### Data-center environmental and power controls

Availability depends on the physical environment, too:

- **HVAC (heating, ventilation, and air conditioning)** — keeps equipment within
  safe temperature and humidity ranges. Overheating kills hardware and threatens
  availability, so HVAC is a genuine security control.
- **UPS (Uninterruptible Power Supply)** — a battery that keeps critical servers
  running through a brief power outage until a generator starts or utility power
  returns, preventing sudden shutdowns.

### The IoT problem

**Internet of Things (IoT)** devices — smart cameras, thermostats, sensors — are
a common security concern because they **frequently ship with weak or default
credentials and are rarely patched**, which expands the attack surface. Changing
default passwords and segmenting IoT devices onto their own network are standard
precautions.

## Exam focus

- **Firewall** = allow/block traffic at the boundary by rules. **IDS** detects and
  alerts (passive); **IPS** sits inline and **blocks** in real time.
- **VPN** = encrypted tunnel over the internet. **Segmentation** isolates zones to
  limit spread. **Zero trust** = verify every request, trust nothing by default.
- **Application allowlisting** = only approved apps run. Secure Wi-Fi with **WPA2
  or WPA3**, never WEP. A **honeypot** is a decoy; an **air gap** is physical
  isolation; a **proxy** forwards and filters web requests.
- Cloud models: **IaaS** (you manage OS + apps), **PaaS** (you manage only your
  code), **SaaS** (provider manages the whole app). A **private cloud** is
  single-tenant.
- Put public-facing servers in a **DMZ (screened subnet)**, not the internal
  network.
- **HVAC** and a **UPS** protect **availability** in the data center. **IoT**
  devices are risky due to default credentials and missing patches.
