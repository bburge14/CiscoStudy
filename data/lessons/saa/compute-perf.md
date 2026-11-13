# High-Performing Compute

The Performance Efficiency pillar asks a simple question with many answers: given a
workload's shape, what runs it fastest and scales cleanest? The SAA exam hands you
a workload profile — bursty web traffic, event-driven code, tightly coupled HPC,
in-memory analytics — and asks for the compute choice and scaling behavior that fit.
This lesson moves from picking the right EC2 family, to scaling it, to the
serverless and container options that remove servers from the picture.

## Scaling out, not up

> **Scaling *out* (horizontal) means adding more instances to share the load;
> scaling *up* (vertical) means making one instance bigger. Resilient, high-
> performing designs prefer scaling out, because many small instances behind a load
> balancer tolerate failure and scale without limit.**

EC2 Auto Scaling drives horizontal scaling. The policy types:

- **Target tracking** — hold a metric at a target (keep average CPU near 50%); the
  group adjusts capacity automatically. This is the default dynamic choice.
- **Step scaling** — add a *different* number of instances depending on how far the
  metric exceeds its threshold (a small breach adds a few, a large breach adds
  many).
- **Warm pools** — when instances take minutes to boot and warm up, a warm pool
  keeps pre-initialized instances ready so scale-out is immediate.

## Picking the right EC2 instance family

Instance families are tuned for different resource ratios. The exam tests the big
ones:

| Family | Optimized for | Example use |
|--------|---------------|-------------|
| General purpose (M, T) | Balanced | Web/app servers |
| Compute optimized (C) | High CPU | Batch, gaming servers |
| **Memory optimized (R, X)** | High RAM-to-vCPU | **In-memory analytics databases** |
| Storage optimized (I, D) | High local IOPS | NoSQL, data warehouses |
| Accelerated (P, G) | GPUs | ML training, rendering |

A large in-memory analytics database that needs a high ratio of RAM to vCPU points
straight to **memory-optimized (R family)**.

## Serverless compute with AWS Lambda

> **AWS Lambda runs event-driven code with no servers to manage, scaling
> automatically from zero to thousands of concurrent executions and billing per
> invocation.** It is the answer for short, event-driven work and for re-
> architecting a lightly used service so you stop paying for idle instances.

Two concurrency controls are tested:

- **Provisioned concurrency** — keeps execution environments initialized and ready,
  eliminating **cold-start** latency for a latency-sensitive function.
- **Reserved concurrency** — *caps* a function's maximum concurrent executions,
  protecting a small downstream database that can only handle limited connections
  from being overwhelmed during spikes.

Remember the pair: **provisioned** = warm and fast; **reserved** = capped to protect
downstream.

## Containers: Fargate, ECS, and EKS

- **AWS Fargate** — serverless containers. You run containers without managing or
  patching the underlying EC2 hosts. Choose it when a team wants to stop managing
  container infrastructure.
- **Amazon ECS** — AWS's container orchestrator; can run on EC2 or on Fargate.
- **Amazon EKS** — managed **Kubernetes**: AWS runs the Kubernetes control plane
  while you deploy existing Kubernetes manifests. Choose it when a team has
  standardized on Kubernetes.

The split: **Kubernetes standardization → EKS**; **don't want to manage hosts →
Fargate** (works under ECS or EKS).

## High-performance computing (HPC) and fast networking

Tightly coupled HPC jobs need instances to talk to each other with the lowest
possible latency:

- **Cluster placement group** — packs instances close together in one AZ for the
  lowest network latency and highest throughput between them. The answer for
  tightly coupled HPC.
- **Elastic Fabric Adapter (EFA)** — a network interface with OS-bypass networking
  for MPI-based HPC, giving the lowest inter-node latency as a job scales across
  many instances.

(Enhanced networking with the ENA for high packets-per-second throughput is covered
in the performance networking lesson.)

## A worked example

A web app with daily CPU swings should run in an **Auto Scaling group with a target
tracking policy** on CPU, on **general-purpose** instances. An image-processing step
triggered by uploads fits **Lambda** — scale to zero when idle, thousands of
executions during a burst — with **reserved concurrency** so it never exhausts the
downstream database's connections. A nightly MPI simulation runs on instances in a
**cluster placement group** with **EFA** for the tightest inter-node latency.

## Exam focus

- **Scale out** (add instances) over scale up. **Target tracking** holds a metric;
  **step scaling** scales by breach size; **warm pools** pre-boot slow-starting
  instances.
- In-memory / high-RAM workload → **memory-optimized (R) instances**; match other
  families to their resource bias.
- **Lambda** = serverless, event-driven, scales 0→thousands, pay per invocation.
  **Provisioned concurrency** kills cold starts; **reserved concurrency** caps
  concurrency to protect downstream systems.
- **Fargate** = serverless containers (no hosts to patch); **EKS** = managed
  Kubernetes control plane; **ECS** = AWS-native orchestration.
- Tightly coupled HPC → **cluster placement group**; MPI with OS-bypass for lowest
  latency → **EFA**.
