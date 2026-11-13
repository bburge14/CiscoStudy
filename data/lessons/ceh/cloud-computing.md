# Cloud Computing Security

Almost every organization now runs part of its estate in someone else's data
center. That shift changes *who* is responsible for *what*, and most cloud breaches
trace back to a misunderstanding of exactly that. This lesson covers the service
and deployment models, the all-important shared responsibility model, and the cloud
attack classes — misconfiguration above all — with their defenses.

## Service and deployment models

> **IaaS** gives you virtual infrastructure (you manage the OS up). **PaaS** gives
> you a platform to deploy code (you manage the app and data). **SaaS** gives you
> finished software (you manage mostly your data and access).

The more the provider manages, the less you do — but **your data and who can access
it are always yours to protect**. Deployment models describe *where* the cloud
lives: **public** (shared, multi-tenant), **private** (dedicated), **hybrid** (a
mix), and **community** (shared by related organizations).

## The shared responsibility model

This is the most tested cloud concept, so be precise:

> **In the shared responsibility model, the provider secures the cloud itself
> ("security *of* the cloud") and the customer secures what they put in it
> ("security *in* the cloud").** The split shifts with the service model — but the
> **customer's data and its classification are always the customer's
> responsibility, in IaaS, PaaS, and SaaS alike.**

Think of it as renting versus owning: the landlord maintains the building; you
still lock your own door and decide who gets a key.

## Cloud attack classes

### Misconfiguration (the big one)

> The dominant cause of cloud data exposure is **misconfiguration** — most famously
> an **object-storage bucket left publicly readable**, exposing sensitive files to
> anyone on the Internet.

Because the control plane is just an API, a single wrong setting can expose
enormous amounts of data instantly. This is why "cloud storage misconfiguration
(excessive public access)" is the archetypal cloud finding.

### The rest of the surface

- **Weak identity and access management** — over-permissive roles, missing MFA,
  and **account hijacking** of privileged users.
- **Leaked credentials and keys** — long-lived access keys hard-coded in code
  repositories or config.
- **Insecure APIs** — the management interface is Internet-facing by nature, so weak
  API auth is critical.
- **Container and Kubernetes risks** — vulnerable images, exposed dashboards, and
  weak orchestration settings.
- **Serverless risks** — over-privileged functions and event-injection.
- **Cloud metadata abuse** — an **SSRF** flaw used to reach the instance **metadata
  endpoint (169.254.169.254)** and steal temporary credentials (ties back to the
  web-app lesson).
- **Multi-tenancy side-channels** and **shadow IT** (unsanctioned cloud use).

## Defending cloud environments

- **Block public access** on storage by default and audit it continuously.
- **CSPM (Cloud Security Posture Management)** — tools that automatically detect
  misconfigurations and drift across accounts.
- **Least-privilege IAM** — grant minimal rights, prefer short-lived **roles** over
  static keys, and enforce **MFA** on all privileged identities.
- **Secrets management** — never hard-code keys; use a managed vault and rotate.
- **Encryption** at rest and in transit, with proper **key management (KMS)**.
- **Logging and monitoring** — enable the provider's audit log (e.g. CloudTrail)
  and alert on anomalies.
- **CASB (Cloud Access Security Broker)** — visibility and policy across cloud
  services, including shadow IT.

> The defining theme: in the cloud, the fastest path to a breach is a wrong setting,
> so the fastest path to safety is **continuous configuration and identity
> hygiene** — least privilege, no public buckets, no hard-coded keys, and logging on.

## Cloud-native attack surface

As workloads move from virtual machines to **containers** and **serverless
functions**, the surface shifts with them:

- **Containers** package an app with its dependencies. Risks include running
  **vulnerable or unverified images**, over-privileged containers, and **exposed
  orchestration dashboards** (such as an unauthenticated Kubernetes API).
- **Serverless functions** remove the server you patch, but an **over-privileged
  function role** still lets a single flaw reach far more than it should.
- **Cryptojacking** — attackers who gain access often spin up compute to mine
  cryptocurrency, turning a misconfiguration into a surprise cloud bill before it is
  ever used to steal data.

### Telling the tools apart

Three acronyms are easy to confuse, so fix the role of each:

- **CSPM** watches **configuration** (the misconfigured-bucket problem).
- **CWPP** protects **workloads** (the VMs, containers, and functions themselves).
- **CASB** sits between users and cloud services to enforce **access policy** and
  surface **shadow IT**.

## How a typical cloud breach unfolds

The pattern repeats across real incidents: a resource is left public or a key is
committed to a code repository, an automated scanner finds it within hours, and the
attacker uses that access to read data or pivot through over-broad IAM. None of it
required breaking encryption — it required a setting nobody reviewed. That is why
cloud defense is less about exotic exploits and more about **continuous visibility
and least privilege**.

## Exam focus

- **IaaS/PaaS/SaaS** differ by how much the provider manages, but **data is always
  the customer's responsibility** in every model — a classic exam answer.
- **Shared responsibility** = provider secures *of* the cloud, customer secures *in*
  the cloud.
- **Cloud storage misconfiguration (public buckets)** is the leading cause of cloud
  data exposure; fix by **blocking public access** and using **CSPM**.
- Watch for **leaked/hard-coded keys**, **weak IAM** (fix: least privilege + MFA +
  roles), **insecure APIs**, and **SSRF to the metadata endpoint
  (169.254.169.254)**.
- Core defenses: **least-privilege IAM, MFA, CSPM, encryption + KMS, secrets
  management, audit logging, and a CASB**.
