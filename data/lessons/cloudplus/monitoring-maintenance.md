# Monitoring, Logging, Observability & Lifecycle Maintenance

Once a workload is live, operations takes over. Two daily disciplines keep it
healthy: **monitoring and logging** tell you what the system is doing right now and
what it did in the past, and **maintenance** keeps it patched, current, and tidy so
it stays secure and supportable. Both lean hard on automation at cloud scale.

## The three pillars of observability

**Monitoring** asks "is a known thing OK?"; **observability** is the broader goal
of being able to ask *new* questions about a system from the data it emits. It
rests on three kinds of telemetry:

> **Metrics** are numeric time-series (CPU %, request rate, queue depth) — cheap to
> store and ideal for dashboards and alerts. **Logs** are timestamped event
> records (an error, a login, an API call) — rich detail for investigation.
> **Traces** follow a single request as it hops across services — essential for
> finding *where* latency or failure occurs in a microservices call chain.

You need all three: metrics tell you *that* something is wrong, logs and traces
help you find *why* and *where*.

## Collecting and using the data

- **Agents / collectors** run on instances (or sidecars in containers) to ship
  metrics and logs to a central service. The cloud's managed monitoring service
  gathers platform metrics automatically.
- **Log aggregation / centralization** pulls logs from every source into one
  searchable place — commonly an **ELK/OpenSearch** stack or a managed log
  service — because logs scattered across dead instances are useless.
- **Dashboards** visualize metrics (tools like **Grafana**); **APM (application
  performance monitoring)** instruments code to surface slow transactions.
- **Synthetic monitoring** runs scripted probes against your service from outside
  to catch problems before users do; **real user monitoring (RUM)** measures
  actual user experience.

### Alerting done right

An **alert** fires when a metric crosses a **threshold** you set against a
**baseline** of normal behavior. The art is tuning:

- Alert on **symptoms users feel** (error rate, latency) more than raw resource
  numbers.
- Too-sensitive thresholds cause **alert fatigue** — so many false alarms that
  real ones get ignored. **Event correlation** groups related alerts so one
  incident doesn't page you fifty times.
- Route alerts somewhere actionable (on-call paging, chat, a ticket), and set
  **log/metric retention** to satisfy troubleshooting and compliance needs
  without paying to store noise forever.

A **SIEM** adds a security lens, correlating logs to detect threats (covered more
in the Security unit); here the point is that centralized logging feeds it.

## Lifecycle maintenance

Software and systems don't stay still. **Lifecycle management** tracks each
component from deployment through **end-of-life (EOL)** / end-of-support, when a
vendor stops shipping security fixes. Running past EOL is a serious risk because
new vulnerabilities will never be patched.

### Patch management

**Patching** applies vendor updates to close vulnerabilities and fix bugs. Know
the vocabulary:

- **Patch / security update** — a fix for a specific flaw.
- **Hotfix** — an urgent, narrowly scoped fix outside the normal cycle.
- **Version upgrade** — a larger move to a new release, with more testing risk.
- **Firmware update** — low-level updates to hardware/hypervisor components.

Good practice: **test patches in a non-production environment first**, schedule
them in a **maintenance window**, and keep a **rollback** path. Many teams run a
regular patch cadence (e.g., monthly) plus an out-of-band process for critical
emergencies.

### Update strategies that avoid downtime

Patching live fleets without an outage uses deployment patterns:

- **Rolling update** — update instances a few at a time so the service stays up;
  slower but needs little extra capacity.
- **Blue-green** — stand up a fully patched "green" environment alongside the live
  "blue," cut traffic over, and keep blue for instant rollback.
- **Canary** — update a small slice first, watch it, then proceed if healthy.

### Fighting configuration drift

Over time, manual tweaks make instances diverge from their intended state —
**configuration drift**. Drift is dangerous because "it works on that server"
hides untracked, unrepeatable changes. The cloud answer is to define state in code
and reconcile continuously:

- **Immutable infrastructure** — never patch a running instance; instead build a
  new image and replace it, so every instance is identical and disposable.
- **Configuration management** tools (Ansible, Puppet) and **runbooks** automate
  routine upkeep — rotating certificates before they expire, cleaning logs,
  restarting stuck services — so maintenance is consistent and auditable rather
  than ad hoc.

## Exam focus

- **Three pillars of observability: metrics** (numeric time-series — dashboards/
  alerts), **logs** (event records — investigation), **traces** (one request across
  services — find *where* latency/failure is).
- **Centralize logs** (ELK/OpenSearch or managed service); dashboards (Grafana);
  **APM** for slow code; **synthetic monitoring** probes from outside before users
  notice.
- Alerts fire on a **threshold** vs. a **baseline**; over-sensitive thresholds
  cause **alert fatigue**, and **event correlation** collapses related alerts. Set
  **retention** for troubleshooting + compliance.
- **EOL / end-of-support** means no more security patches — a major risk. Know
  **patch vs. hotfix vs. version upgrade vs. firmware**; always **test patches in
  non-prod first** and use a **maintenance window** + rollback.
- Zero-downtime updates: **rolling** (few at a time), **blue-green** (swap
  environments, instant rollback), **canary** (small slice first).
- **Configuration drift** = instances diverging from intended state; fix with
  **immutable infrastructure** (replace, don't patch) and **configuration
  management** (Ansible/Puppet) driven by runbooks.
