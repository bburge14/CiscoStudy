# Provisioning & Compute Deployment

Architecture decides *what* to build; deployment is where it actually gets stood
up. This lesson covers two deployment foundations: **provisioning** — the
repeatable mechanics of creating resources — and **compute deployment** — choosing
and launching the instances, containers, and functions that run your code.

## Provisioning: repeatable resource creation

**Provisioning** is the act of creating and configuring a resource so it's ready
to use. In the cloud you almost never click buttons one at a time; you provision
from **templates** so every environment comes out identical.

- **Templates** describe the desired resources declaratively (networks, VMs,
  permissions). The same template produces dev, test, and prod identically —
  this is the gateway to infrastructure as code, covered in the DevOps unit.
- **Images (golden images / machine images)** are pre-baked disk snapshots with
  the OS, patches, and agents already installed, so a new instance boots ready to
  work instead of configuring itself from scratch. A **golden image** is the
  hardened, approved baseline an organization standardizes on.
- **Bootstrapping / user data** runs a startup script the first time an instance
  boots (install packages, join a domain, pull config) — the lightweight
  alternative or complement to baking an image.

Two self-service concepts you'll meet:

- A **service catalog** is a curated menu of approved, pre-configured products
  users can deploy themselves, keeping choices governed.
- **Tagging** (key/value metadata like `env=prod`, `owner=team-a`,
  `cost-center=42`) is how you organize, find, automate against, and — crucially —
  **allocate cost** to resources. Untagged resources are the enemy of cost
  visibility and cleanup.

### Thin vs. thick provisioning

A classic allocation distinction, most relevant to storage but asked generally:

> **Thick provisioning** reserves the full allocated capacity up front, whether or
> not it's used. **Thin provisioning** allocates space on demand as data is
> written, letting you **overcommit** — promise more than physically exists on the
> assumption not everyone uses their max at once.

Thin provisioning improves utilization and cost but needs monitoring: if real
usage catches up to physical capacity, writes fail. Thick provisioning is
predictable and avoids that risk at the cost of stranded, idle capacity.

## Compute deployment: choosing the right engine

Cloud compute comes in three broad shapes, and matching workload to shape is the
core skill:

| Compute type | What it is | Best for |
|--------------|-----------|----------|
| **Virtual machine (instance)** | A full guest OS on a hypervisor | Traditional apps, full OS control, long-running services |
| **Container** | App + dependencies sharing the host kernel | Microservices, portable and dense packing, fast scaling |
| **Serverless / functions** | Code the provider runs on demand | Event-driven, spiky, "scale to zero" workloads |

VMs give the most control and isolation; containers give portability and density;
serverless removes server management entirely and bills per invocation.

### Sizing instances

Providers group VMs into **instance families** tuned to a profile:

- **General purpose** — balanced vCPU-to-memory ratio for typical web/app servers.
- **Compute optimized** — high CPU for batch processing, gaming, media encoding.
- **Memory optimized** — large RAM for databases and in-memory caches.
- **Storage optimized** — high local disk throughput/IOPS for big-data workloads.
- **Accelerated (GPU/FPGA)** — specialized hardware for ML training and rendering.

**Right-sizing** means picking the family and size that fits the workload's real
vCPU, memory, and I/O profile — not guessing high "to be safe," which wastes money.

### Placement and tenancy

Where instances physically land matters for both resilience and compliance:

- **Affinity** — keep related instances close together (same host/zone) for low
  latency.
- **Anti-affinity** — deliberately keep redundant instances *apart* (different
  hosts/zones) so one hardware failure can't take out your whole cluster. A
  highly available pair should always use anti-affinity.
- **Dedicated / single-tenant hosts** — your instances run on hardware not shared
  with other customers, often required by licensing or compliance. The default is
  **multitenant** (shared hardware, logically isolated).
- **Overcommitment / oversubscription** — the host allocates more virtual CPU or
  memory than it physically has, relying on the fact that guests rarely peak at
  once. It raises density and lowers cost but risks contention under heavy load.

### Scaling the deployment

Compute is usually deployed into an **autoscaling group** rather than as lone
instances: a group launches instances from a template, spreads them across zones,
and grows or shrinks against a policy (covered in the Architecture unit). Deploying
this way means a failed instance is automatically replaced — the instances are
treated as disposable **"cattle, not pets."**

## Exam focus

- **Provision from templates and images, not by hand.** A **golden image** is the
  hardened standard baseline; **bootstrapping/user data** configures an instance at
  first boot. A **service catalog** offers governed self-service.
- **Tagging** (key/value metadata) drives organization, automation, and especially
  **cost allocation** — untagged resources break chargeback and cleanup.
- **Thick provisioning** reserves capacity up front; **thin provisioning**
  allocates on demand and allows **overcommitment** (watch for running out of real
  capacity).
- Match compute to workload: **VM** = full OS/control, **container** = portable/
  dense microservices, **serverless** = event-driven, scale-to-zero, pay-per-call.
- Instance **families**: general / compute / memory / storage optimized /
  accelerated (GPU). **Right-size** to the real profile.
- **Anti-affinity** separates redundant instances across hosts/zones for HA;
  **affinity** keeps them together for latency. **Dedicated hosts** = single-tenant
  for licensing/compliance; **overcommitment** raises density but risks contention.
