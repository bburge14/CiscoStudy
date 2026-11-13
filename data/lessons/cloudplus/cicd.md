# CI/CD Pipelines, Containers & Orchestration

CV0-004 added **DevOps Fundamentals** as a full domain, reflecting that modern
cloud teams ship software continuously and run it in containers. This lesson covers
the delivery engine — **CI/CD pipelines** — and the thing those pipelines most
often build and deploy: **containers**, managed at scale by **orchestration**.

## What CI/CD means

The terms blur together, so pin them down:

> **Continuous Integration (CI)** — developers merge code frequently into a shared
> repository, and every merge automatically triggers a **build** and **automated
> tests**. The goal is to catch integration problems within minutes, not at a
> painful merge weeks later.
>
> **Continuous Delivery (CD)** — every change that passes CI is automatically
> prepared and kept *ready* to release, but a human approves the final push to
> production.
>
> **Continuous Deployment** — goes one step further: every change that passes all
> tests is released to production **automatically**, with no manual gate.

The difference between the two CDs is exactly that final gate: **delivery = ready,
deploy = automatic**.

## The pipeline

A **pipeline** is the automated sequence a change flows through, usually:

1. **Source** — a commit/merge to version control (Git) triggers the pipeline.
2. **Build** — compile the code and package it into a deployable **artifact**
   (often a container image). "If it doesn't build, stop here."
3. **Test** — run automated **unit**, **integration**, and security tests. Failing
   tests fail the pipeline; this is a **quality gate**.
4. **Store** — push the versioned artifact to an **artifact/registry** (a package
   repository or container registry).
5. **Deploy** — release the artifact to an environment (staging, then production).

Common pipeline tools include **Jenkins**, **GitLab CI/CD**, and **GitHub
Actions**. Two cultural ideas you should recognize: **shift-left** (move testing
and security earlier in the pipeline, where fixes are cheap) and **fail fast**
(stop the pipeline at the first failure so bad code never advances).

### Safe deployment strategies

Pipelines deploy using the same low-risk patterns used for updates:

- **Rolling** — replace instances a few at a time.
- **Blue-green** — deploy to an idle duplicate environment, switch traffic over,
  keep the old one for instant **rollback**.
- **Canary** — release to a small percentage of users first, watch metrics, then
  continue or roll back.

Automated **rollback** on failed health checks is what makes continuous deployment
safe enough to trust.

## Containers

A **container** packages an application with its libraries and dependencies into
one portable unit that runs the same everywhere. Unlike a VM, it **shares the host
OS kernel** rather than carrying a full guest OS, so it's small and starts in
seconds.

- A **Dockerfile** is the recipe that defines an image.
- An **image** is the immutable, versioned build artifact; a **container** is a
  running instance of an image.
- A **registry** (Docker Hub, or a cloud container registry) stores and
  distributes images — the pipeline pushes here, and orchestrators pull from here.

Containers are ideal for **microservices**: each service is its own small image,
deployed and scaled independently. "**Build once, run anywhere**" is the core
promise — the same image moves from a developer's laptop through CI to production
unchanged, which kills a whole class of "works on my machine" problems.

## Orchestration with Kubernetes

Running a handful of containers by hand is fine; running hundreds across a fleet is
not. **Orchestration** automates deploying, scaling, networking, and healing
containers. **Kubernetes (K8s)** is the de facto standard; know its vocabulary:

- A **pod** is the smallest deployable unit — one or more tightly coupled
  containers sharing storage and a network address.
- **Nodes** are the worker machines that run pods; the **control plane** schedules
  pods onto nodes and maintains desired state.
- A **Deployment** declares *how many* replicas of a pod should exist; Kubernetes
  continuously reconciles reality to that declaration.
- A **Service** gives a stable network endpoint to a set of pods (whose individual
  IPs come and go); **Ingress** exposes services to outside traffic with
  host/path routing.
- **ConfigMaps** hold configuration and **Secrets** hold sensitive values, injected
  into pods instead of baked into images.
- **Health checks** (liveness/readiness probes) let Kubernetes restart unhealthy
  pods and keep traffic away from ones not ready — **self-healing**.

The unifying theme is **declarative desired state**: you describe what you want
(ten replicas, this image, this config), and the orchestrator makes it so and keeps
it that way even as nodes fail — the same mindset as infrastructure as code.

## Exam focus

- **CI** = auto build + test on every merge; **continuous delivery** = always
  *ready* to release (human approves); **continuous deployment** = auto-release to
  production (no manual gate). The final gate is the only difference.
- Pipeline stages: **source → build → artifact → test (quality gate) → deploy.**
  Tools: **Jenkins, GitLab CI, GitHub Actions.** Remember **shift-left** (test/
  secure early) and **fail fast**.
- Deploy safely with **rolling, blue-green** (instant rollback), and **canary**
  (small slice first); automate **rollback** on failed health checks.
- A **container shares the host kernel** (lightweight, portable) vs. a VM's full
  guest OS. **Dockerfile → image (artifact in a registry) → running container.**
  "Build once, run anywhere."
- **Kubernetes** orchestrates containers: **pod** (smallest unit), **node**
  (worker), **control plane** (scheduler/state), **Deployment** (replica count),
  **Service/Ingress** (networking), **ConfigMap/Secret** (config), **health
  checks** (self-healing). All driven by **declarative desired state.**
