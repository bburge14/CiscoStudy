# Global Infrastructure & Ways to Access AWS

AWS runs a physical network of data centers spanning the globe, and it gives you
several ways to reach into that network and build. This lesson covers both halves:
the **global infrastructure** (Regions, Availability Zones, and the edge) and the
**ways you access AWS** (the console, the CLI, SDKs, and infrastructure as code).

## The building blocks: Regions and Availability Zones

> An **AWS Region** is a separate **geographic area** of the world where AWS
> clusters data centers (for example, one in Northern Virginia, another in
> Frankfurt). Regions are **isolated** from one another.

You choose which Region(s) to run in, and — importantly — your data stays in the
Region you pick unless you move it. Inside each Region are Availability Zones:

> An **Availability Zone (AZ)** is one or more discrete **data centers** within a
> Region, each with independent power, cooling, and networking. AZs in a Region are
> physically separated but linked by **high-speed, low-latency** connections.

The relationship is a hierarchy: a **Region contains multiple AZs**, and an **AZ
contains one or more data centers**. The separation is deliberate — a fire or flood
in one AZ shouldn't take down another.

## Designing for high availability

The single most important reason AZs exist: **spread your workload across multiple
AZs** so that if one fails, your application keeps running in the others.

> Running across **two or more Availability Zones** is the foundation of **high
> availability** on AWS. One AZ is a single point of failure; multiple AZs survive
> the loss of a data center.

If a question describes wanting an application to survive a data-center outage, the
answer almost always involves **multiple Availability Zones.**

## Edge locations and content delivery

Regions and AZs are where your workloads *run*. **Edge locations** are a separate,
much larger set of sites that sit close to end users to *deliver* content fast.

- **Edge locations** (points of presence) cache content near users for the
  **Amazon CloudFront** content delivery network, and serve **Amazon Route 53**
  DNS. A user in Tokyo gets content from a nearby edge location instead of
  crossing an ocean, cutting latency.

## Bringing AWS closer: hybrid and edge options

Sometimes a Region isn't close enough, or data must stay in a specific building.
AWS extends its infrastructure outward with a few specialized options:

| Option | What it is | When you'd use it |
|--------|------------|-------------------|
| **AWS Local Zones** | AWS compute/storage placed in a **large metro area** near users | Single-digit-millisecond latency to a city far from a Region |
| **AWS Outposts** | Racks of **AWS hardware installed in your own data center** | Workloads that must stay **on-premises** for latency or data residency, run with AWS APIs |
| **AWS Wavelength** | AWS compute/storage embedded **inside telecom 5G networks** | **Ultra-low-latency** apps for mobile/5G users |

A quick way to remember: **Outposts** = AWS in *your* building; **Local Zones** =
AWS in a *nearby city*; **Wavelength** = AWS in the *5G network*.

## Choosing a Region

Picking where to run isn't arbitrary. Four factors drive the decision:

- **Compliance and data residency** — some data must legally stay in a certain
  country, forcing a Region choice.
- **Latency** — choose a Region close to your users for a faster experience.
- **Service availability** — not every service or feature launches in every Region
  at once.
- **Pricing** — costs vary by Region, so the same workload can cost more in one
  than another.

## Ways to access AWS

Now the second half: once you have an account, how do you actually *do* things?
There are three fundamental ways, plus automation on top.

| Method | What it is | Who uses it |
|--------|------------|-------------|
| **AWS Management Console** | A **web-based graphical interface** — point and click in the browser | Beginners, visual tasks, exploring |
| **AWS CLI** | The **command-line interface** — type commands in a terminal | Scripting, repeatable admin tasks |
| **AWS SDKs** | **Software development kits** — call AWS from your own code (Python, Java, etc.) | Developers building applications |

All three ultimately call the same underlying **AWS APIs**. The console is the
friendly front end; the CLI and SDKs are for automation and code.

## Infrastructure as Code

Clicking in the console is fine once. For repeatable, reliable environments you
define your infrastructure in files instead.

> **Infrastructure as Code (IaC)** means defining and provisioning resources from
> **machine-readable template or definition files**, so an environment is
> **repeatable, versioned, and automated** rather than hand-built.

AWS's tools for this:

- **AWS CloudFormation** — describe your resources in a **template** (JSON/YAML),
  and CloudFormation creates and manages them as a unit (a "stack"). Tear it all
  down just as cleanly.
- **AWS CDK (Cloud Development Kit)** — define infrastructure using a **real
  programming language** (TypeScript, Python, etc.), which generates
  CloudFormation under the hood.

## Managing fleets at scale

Once you're running many servers, you need to operate them centrally:

- **AWS Systems Manager** — manage a **fleet** of EC2 and on-premises servers from
  one place: apply OS patches, run commands at scale, and store configuration and
  parameters. The go-to answer for "operate and patch many servers centrally."

## Deployment models and connectivity

AWS recognizes that not everything moves to the cloud at once:

- **Cloud (all-in)** — everything runs on AWS.
- **Hybrid** — a mix of AWS and on-premises/private infrastructure, connected
  together (Outposts is one way to do this).
- **On-premises / private** — resources in your own data center.

To connect your network to AWS you have three choices: over the **public
internet**, through an encrypted **VPN** (Site-to-Site VPN) over the internet, or
through **AWS Direct Connect**, a **dedicated private physical connection** for
consistent, high-bandwidth, lower-latency links (covered more with networking).

## The whole thing in one paragraph

AWS's infrastructure is **Regions** (isolated geographic areas) made of multiple
**Availability Zones** (separated data centers), and you achieve **high
availability** by spreading across **multiple AZs**; **edge locations** deliver
content close to users via CloudFront, and **Outposts, Local Zones, and
Wavelength** push AWS into your building, nearby cities, and 5G networks. You access
it all through the **Console** (GUI), **CLI** (terminal), or **SDKs** (code);
automate it with **Infrastructure as Code** (**CloudFormation** templates or the
**CDK**); operate fleets with **Systems Manager**; and connect on-premises
networks over the internet, a **VPN**, or dedicated **Direct Connect**.

## Exam focus

- **Region** = isolated geographic area; **Availability Zone** = one or more
  separated data centers within a Region. A **Region contains multiple AZs.**
- **High availability = deploy across multiple Availability Zones** so one
  data-center failure doesn't take you down.
- **Edge locations** cache content near users for **CloudFront** (CDN) and Route
  53. **Outposts** = AWS hardware on-premises; **Local Zones** = near a metro;
  **Wavelength** = inside 5G networks for ultra-low latency.
- Choose a Region by **compliance/data residency, latency, service availability,
  and price.**
- Access methods: **Management Console** (web GUI), **CLI** (command line),
  **SDK** (your own code) — all hit the same APIs.
- **Infrastructure as Code** = provision from template/definition files
  (repeatable); **CloudFormation** (templates) and **CDK** (programming language).
- **Systems Manager** = centrally manage/patch a fleet of servers.
- Connectivity: public internet, **VPN** (encrypted over internet), or **Direct
  Connect** (dedicated private link).
