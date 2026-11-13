# The Shared Responsibility Model

New AWS users often assume one of two wrong things: either "AWS handles all the
security" or "security is entirely my problem." The truth is a split, and knowing
*where* the line falls — and how it moves between services — is one of the most
heavily tested ideas on this exam. This lesson draws that line.

## Two halves: of the cloud vs. in the cloud

> Under the **Shared Responsibility Model**, **AWS is responsible for security
> *OF* the cloud**, and **the customer is responsible for security *IN* the
> cloud.**

Say those two prepositions out loud, because the whole model hangs on them:

- **Security *of* the cloud (AWS)** — the infrastructure that runs all the
  services: the data centers, the hardware, the networking, and the
  virtualization layer. AWS protects the thing you're building *on*.
- **Security *in* the cloud (you)** — everything you put on top: your data, how
  you configure services, who can access them, and your own applications. You
  protect the thing you *build*.

A useful analogy is renting an apartment. The landlord (AWS) secures the building:
the foundation, the exterior walls, the locks on the main entrance. You, the
tenant, are responsible for locking your own apartment door and deciding who you
hand a key to. If you leave your door wide open, that's on you — not the landlord.

## What AWS is responsible for

AWS owns and operates everything from the concrete up to the hypervisor:

- **Physical security** of data centers — guards, fences, badge access,
  environmental controls like power and cooling.
- **Hardware** — the servers, storage, and networking gear, and their disposal at
  end of life.
- **The virtualization layer / hypervisor** that isolates one customer's virtual
  machines from another's.
- **The global infrastructure** — Regions, Availability Zones, and edge locations.
- **The managed software of AWS's own services** — for a managed database, AWS
  patches and maintains the database engine and the host it runs on.

You will never patch an AWS data center's air conditioning or swap a failed disk.
That's AWS's job, by design.

## What the customer is responsible for

Your side is summed up by a phrase worth memorizing: you are responsible for
everything you put *in* the cloud and how you configure it.

- **Your data** — you own it, you classify it, and you decide how it's protected.
- **Identity and access management** — creating users and roles, applying least
  privilege, enabling MFA, managing keys.
- **Configuring the services you use** — for example, setting an S3 bucket's
  permissions so data isn't accidentally made public.
- **Operating-system, network, and firewall configuration** — *when the service
  exposes them to you* (more on that below).
- **Encryption settings** — choosing to encrypt data at rest and in transit, and
  managing the keys where that's your choice.
- **Your application code** and its security.

> The customer **always** owns and controls their **content (data)** and **who can
> access it**, no matter which service they use. If a question asks what stays the
> customer's job across every AWS service, the answer is **data and access
> management.**

## The line moves with the service type

Here's the subtlety the exam loves: the split is **not fixed** — it slides
depending on how managed the service is. The more AWS manages, the less is left to
you.

| Service type | Example | AWS handles | You handle |
|--------------|---------|-------------|------------|
| **IaaS** (infrastructure) | Amazon EC2 | Hardware, hypervisor, facilities | **Guest OS patching**, firewall rules, apps, data, access |
| **PaaS / managed** | Amazon RDS, AWS Lambda | All of the above **plus** OS and engine patching | Data, access, and service configuration |
| **SaaS** | Amazon WorkMail, QuickSight | Nearly everything in the stack | Mainly your data and user access |

With **Amazon EC2** (an IaaS service), you rent a virtual server, so **you** must
patch its operating system, configure its firewall, and secure the application.
Move to **Amazon RDS** or **Lambda**, and AWS now patches the OS and the engine
for you — your job shrinks to data, access, and configuration. The pattern:

> As you move from **EC2 (IaaS)** toward **fully managed services (PaaS/SaaS)**,
> **AWS takes on more operational responsibility** and you focus mainly on **data
> and access management.**

### Patching: a classic trap

- On **EC2**, patching the guest operating system is **your** responsibility.
- On **RDS**, patching the database and OS is **AWS's** responsibility.

Same word, "patching," opposite answers — the difference is the service.

## Shared and inherited controls

Some controls are genuinely shared. **Patch management** and **configuration
management**, for instance, are split: AWS patches the infrastructure, you patch
your guest OS and apps. **Awareness and training** is shared too — AWS trains its
people, you train yours. And you *inherit* controls like physical and
environmental security simply by running on AWS; you get the benefit without doing
the work.

## Why the model matters

The Shared Responsibility Model isn't bureaucratic fine print — it prevents the
most common cloud breaches. The majority of real-world "AWS breaches" aren't AWS
being hacked; they're customers leaving an S3 bucket public or handing out
over-broad permissions. That's the customer's side of the line. Knowing the model
tells you exactly which risks you still have to manage.

## The whole thing in one paragraph

AWS secures **of** the cloud — data centers, hardware, networking, and the
hypervisor — and you secure **in** the cloud — your data, identities and access,
service configuration, and anything the service leaves in your hands. The line
**slides with the service**: on **EC2 (IaaS)** you patch the guest OS and manage
firewalls; on managed services like **RDS and Lambda**, AWS takes those over and
you focus on data, access, and configuration. Through it all, **you always own
your data and who can access it.**

## Exam focus

- **AWS = security OF the cloud** (physical facilities, hardware, networking,
  hypervisor/virtualization, global infrastructure). **Customer = security IN the
  cloud** (data, IAM/access, configuration, apps).
- The customer is **always** responsible for **their data and access control**,
  on every service — the most common "what stays your job" answer.
- The split **shifts by service**: more managed = more on AWS. **EC2** → you patch
  the guest OS; **RDS/Lambda** → AWS patches it. Watch the patching trap.
- Classic customer tasks: **configuring S3 bucket permissions**, enabling MFA,
  setting least-privilege IAM, choosing encryption.
- Classic AWS tasks: **physical/environmental controls, maintaining the
  hypervisor and hardware**, decommissioning disks.
- Some controls are **shared** (patch and configuration management, awareness and
  training); physical controls are **inherited** by running on AWS.
