# Compute & Networking Services

Compute is where your code actually runs; networking is how everything connects
and stays isolated. These two families are the heart of domain 3, and the exam
tests whether you can match a short scenario to the right service. There are many
names here, so lean on the tables and learn each service by its *job* and its
*when-to-use*.

## Amazon EC2: virtual servers

> **Amazon EC2 (Elastic Compute Cloud)** provides resizable **virtual servers**
> (instances) in the cloud. You pick the operating system, size, and count, and
> you manage the instance — making EC2 the classic **IaaS** compute service.

Two EC2 terms you must know:

- **AMI (Amazon Machine Image)** — a **template** containing the operating system
  and configuration used to launch an instance. Launch ten instances from one AMI
  and they start identical.
- **Instance types / families** — EC2 comes in families tuned for different
  workloads. You pick the family that fits, which is right-sizing in action:

| Family | Optimized for | Example use |
|--------|---------------|-------------|
| **General purpose** | Balanced CPU/memory | Web servers, small databases |
| **Compute optimized** | High CPU | Batch processing, gaming servers |
| **Memory optimized** | Large RAM | In-memory databases, analytics |
| **Storage optimized** | High local disk throughput | Data warehouses, big data |
| **Accelerated computing** | GPUs/specialized hardware | Machine learning, graphics |

## Scaling and load balancing

Running one instance is fragile and inflexible. Two services make EC2 elastic and
resilient:

- **Amazon EC2 Auto Scaling** — **automatically adds and removes instances** to
  match demand, and replaces unhealthy ones. This is how you "stop guessing
  capacity."
- **Elastic Load Balancing (ELB)** — **distributes incoming traffic** across
  multiple instances (across AZs), so no single server is overwhelmed and a failed
  one is bypassed.

Together they're the standard high-availability pattern: a load balancer in front
of an Auto Scaling group spread across multiple Availability Zones.

## Containers

Containers package an app with its dependencies so it runs consistently anywhere.
AWS offers orchestration for them:

| Service | What it is |
|---------|------------|
| **Amazon ECS** | AWS's **native** container orchestration — run and scale Docker containers; no Kubernetes needed. |
| **Amazon EKS** | **Managed Kubernetes** — use the open-source Kubernetes ecosystem on AWS. |
| **AWS Fargate** | **Serverless compute for containers** — runs ECS/EKS containers **without you managing the underlying servers**. |

The distinction the exam tests: **ECS** = AWS-native orchestration, **EKS** =
Kubernetes, **Fargate** = you don't manage the servers at all.

## Serverless compute: Lambda

> **AWS Lambda** runs your code **without provisioning or managing any servers**.
> It's **event-driven** — a function runs in response to a trigger (a file upload,
> an API call) — and you **pay only for the compute time it uses**, down to the
> millisecond, nothing when idle.

Lambda is the purest "serverless" answer: no instances to size, patch, or scale.
If a scenario says "run code in response to events with no servers to manage,"
it's Lambda.

## Simpler and specialized compute

- **Amazon Lightsail** — the **easy button**: pre-configured bundles (like a
  WordPress site) with **simple, predictable monthly pricing**. Great for small
  projects and users who don't want to assemble EC2, networking, and storage
  themselves.
- **AWS Elastic Beanstalk** — a **PaaS** that takes your application code and
  **automatically handles the provisioning, load balancing, and scaling** of the
  EC2 resources underneath. You focus on the app, not the infrastructure.
- **AWS Batch** — runs large numbers of **batch computing jobs**, provisioning the
  right compute automatically.

## Networking: the VPC

Now connectivity. Everything starts with the VPC.

> **Amazon VPC (Virtual Private Cloud)** is a **logically isolated section of the
> AWS cloud** where you control your own IP address ranges, **subnets**, and
> routing. It's your private network inside AWS.

Within a VPC you create **subnets** — subdivisions of your IP range, usually split
into **public** subnets (reachable from the internet) and **private** subnets
(not directly reachable, for databases and back ends).

## Securing the VPC: security groups vs. NACLs

Two firewall layers protect a VPC, and telling them apart is a favorite question.

| | **Security Group** | **Network ACL (NACL)** |
|-|--------------------|------------------------|
| Operates at | the **instance** level | the **subnet** level |
| State | **Stateful** (return traffic auto-allowed) | **Stateless** (must allow return traffic explicitly) |
| Rules | **Allow** rules only | **Allow and Deny** rules |

> A **security group** is a virtual firewall for an **instance** and is
> **stateful**; a **network ACL** is a firewall for a **subnet** and is
> **stateless**. Security groups can only *allow*; NACLs can also *deny*.

## Connecting in, out, and across

| Service | Job |
|---------|-----|
| **Internet Gateway** | Lets resources in a **public** subnet reach the internet |
| **NAT Gateway** | Lets **private** subnet resources reach *out* to the internet without being reachable *inbound* |
| **VPC endpoint** | Private connection to an AWS service (e.g. S3) **over the AWS network**, keeping traffic off the public internet |
| **AWS Direct Connect** | A **dedicated private physical link** from your data center to AWS (consistent, high bandwidth) |
| **AWS Site-to-Site VPN** | An **encrypted tunnel** from your network to AWS over the public internet |
| **AWS Transit Gateway** | A **central hub** that connects many VPCs and on-premises networks, instead of a tangle of point-to-point links |

If a scenario describes **many VPCs plus on-premises** needing a single connection
point, the answer is **Transit Gateway**. If it's reaching S3 **privately**, it's a
**VPC endpoint**.

## Edge and DNS

- **Amazon Route 53** — a scalable **DNS** service (translating names to
  addresses), which also **registers domains** and offers traffic-routing policies.
- **Amazon CloudFront** — the **content delivery network (CDN)**: caches content at
  **edge locations** worldwide so users get it from a nearby point with low
  latency.

## The whole thing in one paragraph

**EC2** gives you virtual servers (launched from an **AMI**, sized by instance
family), made resilient with **Auto Scaling** and **ELB** across multiple AZs; run
containers with **ECS** (native), **EKS** (Kubernetes), or **Fargate** (no servers
to manage); go fully serverless with **Lambda** (event-driven, pay-per-use); and
simplify with **Lightsail** or **Elastic Beanstalk**. Networking centers on the
**VPC** (your isolated network of **subnets**), protected by **security groups**
(instance, stateful) and **NACLs** (subnet, stateless), connected by **gateways**,
**VPC endpoints**, **Direct Connect**, **VPN**, and **Transit Gateway**, with
**Route 53** for DNS and **CloudFront** for content delivery.

## Exam focus

- **EC2** = virtual servers; an **AMI** is the **OS + configuration template** you
  launch from. Instance families (general/compute/memory/storage/accelerated) let
  you right-size.
- **Auto Scaling** adds/removes instances to match demand; **ELB** distributes
  traffic across instances and AZs — together, the HA pattern.
- Containers: **ECS** (AWS-native), **EKS** (Kubernetes), **Fargate** (serverless —
  no servers to manage). **Lambda** = run code with **no servers**, event-driven,
  pay per use.
- **Lightsail** = simplest way to launch a small site (e.g. WordPress) with
  predictable pricing; **Elastic Beanstalk** = PaaS that auto-provisions and scales
  your app's infrastructure.
- **VPC** = your isolated virtual network. **Security group** = instance-level,
  **stateful**, allow-only; **NACL** = subnet-level, **stateless**, allow *and*
  deny.
- **Transit Gateway** = central hub for many VPCs/on-prem; **VPC endpoint** =
  private access to AWS services; **Direct Connect** = dedicated private link; **VPN**
  = encrypted over internet.
- **Route 53** = DNS/domain registration; **CloudFront** = CDN caching at edge
  locations.
