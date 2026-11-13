# Logging, Monitoring & Change Management

Day-to-day security operations rest on two disciplines: *seeing* what is happening
across the environment (logging and monitoring), and *controlling* how the
environment changes over time (change and configuration management). Both are
process-heavy, and both are where the exam rewards the risk-manager answer over the
quick technical fix. This lesson covers the monitoring stack and the change
discipline that keeps well-meaning changes from becoming incidents.

## Monitoring the environment

You cannot respond to what you cannot see. Modern operations centers run a stack of
tools, and CISSP tests what each one is for.

> A **SIEM (Security Information and Event Management)** platform **aggregates and
> correlates** logs from across the environment, normalizes them, and raises alerts
> when correlated patterns suggest an incident. It is the single pane of glass for
> detection.

> A **SOAR (Security Orchestration, Automation, and Response)** platform adds the
> *response* layer: it **automatically enriches alerts, runs predefined playbooks,
> and orchestrates actions across tools** (firewall, EDR, ticketing) with minimal
> analyst effort. SOAR **complements** the SIEM — SIEM detects, SOAR acts.

The distinction is a reliable exam item: if the scenario is "aggregate and correlate
logs to detect," that's **SIEM**; if it's "automate playbook-driven response across
our tools to cut repetitive triage," that's **SOAR**.

Other monitoring concepts:

- **Continuous monitoring** — ongoing, often automated assessment of security
  posture rather than a once-a-year snapshot.
- **IDS/IPS** — detect (and for IPS, block) malicious traffic.
- **UEBA (User and Entity Behavior Analytics)** — baselines normal behavior and
  flags anomalies (a user suddenly downloading gigabytes at midnight).
- **Egress / ingress monitoring** — watch outbound traffic for data exfiltration
  and command-and-control, not just inbound threats. **DLP** often rides here.
- **Threat intelligence and IOCs (Indicators of Compromise)** — enrich detection
  with known-bad indicators and adversary behavior.

> A managerial note: alerts have no value unless someone triages them. The common
> failure isn't missing tools — it's **alert fatigue** drowning real signals, which
> is exactly the problem SOAR and tuned correlation are meant to solve.

## Change management

Most outages and many security holes come not from attackers but from **changes** —
a patch that breaks a dependency, an update that opens a port, a tweak that disables
logging. **Change management** is the disciplined process that keeps changes safe,
reviewed, and reversible.

The process you should recognize:

1. **Request (RFC)** — a change is formally proposed.
2. **Impact analysis** — what could it break, and what is the security effect?
3. **Approval** — a **Change Advisory Board (CAB)** reviews and signs off; changes
   aren't made on a whim.
4. **Testing** — prove it works in a non-production environment first.
5. **Implementation** — make the change in a scheduled **maintenance window**.
6. **Backout plan** — a documented way to undo the change if it fails.
7. **Review / documentation** — confirm success and update records (diagrams,
   configuration items).

An **emergency change** path exists for truly urgent fixes (a critical exploit in
the wild), but it still requires after-the-fact review — it is not a license to
skip discipline.

> Change management is an **administrative/operational** control, not a technical
> one. Its purpose is to prevent **unauthorized or untested changes** from
> destabilizing systems or quietly weakening security.

## Configuration management and patching

Where change management governs *the process of changing*, **configuration
management** governs *the known-good state*:

- **Baselines** define the approved secure configuration for a system class.
- A **CMDB (Configuration Management Database)** tracks configuration items and
  their relationships.
- **Versioning** preserves history so you can see exactly what changed and roll
  back.
- The enemy is **configuration drift** — systems gradually diverging from the
  baseline through undocumented tweaks until no one knows the true state.

**Patch management** is a special, high-stakes change:

> A critical security patch should be **tested in a non-production/staging
> environment and then deployed through change management with a rollback plan** —
> balancing the risk of exposure (patch now) against the risk of instability (test
> first). Only a genuinely urgent threat justifies the emergency path.

That balance — exposure vs stability — is the exam's favorite patching question. The
wrong answers are usually "push straight to production immediately" or "wait for the
next quarterly cycle"; the right answer is the measured, change-managed middle.

## Separation of duties in change control

Change management is also a fraud-and-error control. The person who *requests* or
*develops* a change should not be the one who *approves* and *deploys* it to
production — the same separation-of-duties logic from Domain 1, applied to
operations. This stops a single insider from pushing malicious or unreviewed code
live, and it guarantees a second set of eyes validates impact. In regulated
environments (think SOX, which scrutinizes changes to financial systems),
demonstrating that separation in the deployment pipeline is itself an audit
requirement — "the developer can't self-approve to prod" is a control, not
bureaucracy.

## Exam focus

- **SIEM** = aggregate and **correlate** logs to **detect**; **SOAR** = **automate
  and orchestrate** playbook-driven **response**. SOAR complements the SIEM.
- Know **UEBA** (behavioral anomalies), **egress monitoring** (exfiltration/C2),
  **continuous monitoring**, and **IOCs/threat intel**. The real-world failure is
  **alert fatigue**, not missing tools.
- Change management steps: **request → impact analysis → CAB approval → test →
  implement in a maintenance window → backout plan → document.** It is an
  **administrative** control that prevents **unauthorized/untested** changes; an
  **emergency change** still gets after-the-fact review.
- Configuration management maintains **baselines** (via a **CMDB** and versioning)
  and fights **configuration drift**.
- Patch a critical vulnerability by **testing in staging, then deploying via change
  management with rollback** — balance exposure against stability; don't push
  blindly to production or defer a critical fix for months.
- Apply **separation of duties** to change control: the requester/developer of a
  change should not also approve and deploy it (an audit expectation under SOX).
