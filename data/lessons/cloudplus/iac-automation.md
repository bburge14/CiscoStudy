# Infrastructure as Code, Configuration Management & Automation

The second half of DevOps Fundamentals is about *defining and operating*
infrastructure through code rather than clicks. This lesson covers **infrastructure
as code (IaC)**, the closely related **configuration management**, and the
**scripting, APIs, and webhooks** that automate everything else a cloud platform
does.

## Infrastructure as Code

**IaC** means describing your infrastructure — networks, servers, permissions,
databases — in machine-readable files kept in version control, then having a tool
build exactly that. It replaces hand-clicking the console or running one-off
commands.

Why it matters:

- **Repeatable and consistent** — the same file builds identical dev, test, and
  prod environments, killing "it works in staging" drift.
- **Version-controlled** — infrastructure changes are reviewed, diffed, and
  rolled back like application code.
- **Auditable and fast** — you can stand up or tear down a whole environment in
  minutes, and the code *is* the documentation.

### Declarative vs. imperative

This distinction is heavily tested.

> **Declarative** IaC describes the *desired end state* ("there should be three web
> servers and this network") and the tool figures out how to get there.
> **Imperative** code specifies the *exact steps* in order ("create a server, then
> attach a disk, then..."). Most modern IaC is declarative.

A property that makes declarative tools safe is **idempotency**: applying the same
definition repeatedly produces the same result — if the three servers already
exist, running it again changes nothing rather than creating three more.

### IaC tools and concepts

- **Terraform** — the dominant multi-cloud provisioning tool, declarative, written
  in HCL. It keeps a **state file** recording what it created, runs a **plan**
  (preview of changes) before **apply**, and uses **modules** for reusable
  components.
- **CloudFormation / ARM / Bicep** — cloud-provider-native IaC for AWS and Azure.
- **Drift detection** — IaC tools can compare real infrastructure against the code
  and flag where someone made a manual change, reinforcing the **immutable
  infrastructure** idea: change the code and redeploy, never tweak live resources.

## Configuration management

IaC typically *provisions* the infrastructure; **configuration management** then
sets up *what runs on it* — installing packages, writing config files, managing
services — and keeps them in the intended state.

- **Ansible** — **agentless** (connects over SSH/WinRM), uses human-readable YAML
  **playbooks**; popular for its low setup cost.
- **Puppet** and **Chef** — traditionally **agent-based**, continuously enforcing a
  **desired state** on each managed node.

The common thread with IaC is again **declarative desired state** and
**idempotency**: you declare how a server should be configured, and the tool
converges it there and keeps it there, correcting drift automatically.

## Automation and scripting

Beyond provisioning, day-to-day cloud operations are automated with scripts and
API calls.

- **Scripting languages** — **Python** (rich cloud SDKs, the most common), **Bash**
  (Linux glue and quick tasks), and **PowerShell** (Windows and cross-platform
  administration).
- **CLIs and SDKs** — every provider ships a command-line interface and language
  SDKs so scripts can create and manage resources programmatically.
- **Scheduled automation** — cron jobs or scheduled functions run routine tasks
  (nightly cleanup, snapshots, reports) without a human.

### APIs and webhooks

Everything in the cloud is ultimately an **API** call.

- A **REST API** exposes resources over HTTP using verbs (GET/POST/PUT/DELETE) and
  usually **JSON** payloads. Scripts authenticate with an **API key** or a
  **token** (often OAuth), and must respect **rate limits** (providers throttle
  excessive calls).
- A **webhook** inverts the flow: instead of your code polling an API, the service
  **pushes** an HTTP callback to a URL you registered when an event happens (a
  commit, a build completion, an alert). Webhooks are the backbone of
  **event-driven automation** — a Git push fires a webhook that kicks off a
  pipeline.

> Polling asks "has anything changed?" over and over; a **webhook** is told
> "something changed" the moment it does. Webhooks are more efficient and timely
> for event-driven workflows.

### Data formats and GitOps

Automation lives on structured data: **JSON** (ubiquitous in APIs) and **YAML**
(favored for human-edited config — Kubernetes manifests, Ansible playbooks, CI
definitions). Indentation matters in YAML; a stray space breaks a deploy.

The culmination is **GitOps**: the Git repository is the single source of truth for
both infrastructure and configuration, and an automated agent continuously makes
the live environment match what's committed. A change is a pull request; a rollback
is a revert.

## Exam focus

- **IaC** = infrastructure defined in version-controlled code — repeatable,
  auditable, fast. **Declarative** describes the desired end state (the tool works
  out how); **imperative** lists exact steps. Declarative + **idempotent** is the
  modern norm.
- **Terraform** = multi-cloud, declarative (HCL), with **state file**, **plan**,
  **apply**, **modules**, and **drift detection**. **CloudFormation/ARM/Bicep** are
  provider-native. Pairs with **immutable infrastructure** (redeploy, don't tweak).
- **Configuration management** sets up software on provisioned hosts: **Ansible** =
  agentless/YAML playbooks; **Puppet/Chef** = agent-based desired-state. Same
  idempotent, declarative mindset.
- Scripting: **Python** (SDKs), **Bash** (Linux), **PowerShell** (Windows/cross-
  platform); providers offer **CLIs and SDKs**.
- **REST APIs** use HTTP verbs + **JSON**, authenticated by **key/token**, bounded
  by **rate limits**. A **webhook** is a service-pushed callback on an event — the
  basis of **event-driven automation** (vs. polling). **YAML** for human config,
  **JSON** for APIs; **GitOps** makes Git the source of truth.
