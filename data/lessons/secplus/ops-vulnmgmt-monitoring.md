# Vulnerability Management, Monitoring & Automation

Keeping an enterprise safe is a continuous loop: **find** weaknesses, **watch**
for trouble, and **respond faster than humans alone can**. This lesson covers the
three engines that drive that loop — vulnerability management, security monitoring,
and the automation and orchestration that ties it all together.

## Vulnerability management: find and fix weaknesses

**Vulnerability management** is the ongoing process of identifying, prioritizing,
fixing, and verifying the fix of weaknesses. It never ends — new flaws appear
daily.

### Identifying vulnerabilities

You find weaknesses many ways, and the exam lists them:

- **Vulnerability scan** — automated tools (e.g. Nessus) probe systems for known
  flaws. The workhorse.
- **Application security testing** — **static** analysis (SAST, scans source
  code), **dynamic** analysis (DAST, tests the running app), and **package
  monitoring** (watching third-party libraries for known vulnerabilities).
- **Penetration testing** — ethical hackers actively try to exploit weaknesses to
  show real impact.
- **Threat feeds** — **OSINT** (open-source intelligence), **proprietary/
  third-party** feeds, **information-sharing organizations** (like ISACs), and
  **dark web** monitoring.
- **Responsible disclosure / bug bounty** — paying outside researchers to report
  flaws rather than exploit them.
- **System/process audit** — reviewing configurations and procedures for gaps.

### Analyzing what you find

Not every finding is real or urgent. Analysis separates signal from noise:

- **Confirmation** — rule out a **false positive** (a flagged issue that isn't
  real) and watch for a **false negative** (a real issue the scan missed — the
  more dangerous one).
- **Prioritization** — you can't fix everything at once, so rank by severity and
  context.
- **CVE (Common Vulnerabilities and Exposures)** — the public catalog that gives
  each known vulnerability a unique ID.
- **CVSS (Common Vulnerability Scoring System)** — a 0–10 severity score; higher =
  more severe.
- **Context** — **exposure factor**, **environmental variables**, **industry/
  organizational impact**, and your **risk tolerance** all adjust the real
  priority. A "critical" CVE on an isolated test box may matter less than a
  "medium" on an internet-facing server.

> A scan result is a *starting point*, not a verdict. **Confirm** it's real, then
> **prioritize** by combining the CVSS score with how exposed and important the
> asset actually is.

### Responding and validating

Once confirmed and prioritized, you **respond and remediate**:

- **Patching** — the usual fix.
- **Insurance** — transfer the financial risk (cyber-insurance).
- **Segmentation** — wall off what you can't immediately fix.
- **Compensating controls** — add other protections when you can't patch.
- **Exceptions / exemptions** — formally accept a risk you won't fix right now,
  with documentation and sign-off.

Then you **validate**: **rescanning** to confirm the fix worked, plus **audit**
and **verification**, and finally **reporting** the results to stakeholders.

## Security monitoring and alerting

You can't prevent everything, so you watch continuously to catch what slips
through. Monitoring covers **systems**, **applications**, and **infrastructure**.

### Monitoring activities

- **Log aggregation** — pull logs from everywhere into one place.
- **Alerting** — raise a flag when something suspicious happens.
- **Scanning** — continuously check for vulnerabilities and misconfigurations.
- **Reporting** and **archiving** — summarize findings and retain logs for the
  required period.
- **Alert response and remediation** — including **quarantine** (isolate a
  suspect host) and **alert tuning** (reduce false alarms so real ones aren't
  lost in the noise).

> **Alert tuning** is the unsung hero of monitoring: too many false alerts and
> analysts suffer *alert fatigue* and start ignoring everything — including the
> real attack.

### Monitoring tools

| Tool | What it does |
|------|--------------|
| **SIEM** | Aggregates and correlates logs; the nerve center of a SOC |
| **SCAP** | A standard that lets tools share security configuration data |
| **Benchmarks** | Known-good configs to measure against (e.g. CIS) |
| **Antivirus** | Detects and removes known malware |
| **DLP** | Stops sensitive data from leaving |
| **SNMP traps** | Devices push alerts about their status |
| **NetFlow** | Records network traffic flows for analysis |
| **Vulnerability scanners** | Find weaknesses |

Monitoring can be **agent-based** (software installed on each host, richer data)
or **agentless** (no install, lighter but less detail). The **SIEM** is the one to
know best — it's where logs are correlated and alerts are born.

## Automation and orchestration

Humans don't scale, and attackers move fast. **Automation** handles individual
repetitive tasks; **orchestration** strings many automated tasks into a
coordinated workflow. Together (often via **SOAR** — Security Orchestration,
Automation, and Response) they let a small team cover a big environment.

### Where automation shines (use cases)

- **User and resource provisioning** — create accounts and spin up systems to a
  standard automatically.
- **Guard rails** — automated limits that stop unsafe actions.
- **Security groups** — apply firewall policy automatically.
- **Ticket creation** and **escalation** — route incidents without manual
  shuffling.
- **Enabling/disabling services and access** — e.g. auto-disable an account on
  offboarding.
- **Continuous integration and testing (CI/CD)** — bake security checks into the
  build pipeline.
- **Integrations and APIs** — glue tools together.

### Benefits and cautions

Benefits: **efficiency / time saving**, **enforcing baselines**, **standard
configurations**, **scaling securely**, faster **reaction time**, acting as a
**workforce multiplier**, and even **employee retention** (less tedious work).

But automation isn't free. Watch the trade-offs: **complexity**, **cost**, a
**single point of failure** (if the automation breaks, everything it ran breaks),
**technical debt**, and **ongoing supportability** (someone has to maintain the
scripts).

> Automation is a **force multiplier**: it makes a small team act like a big one
> and enforces consistency — but a bug in an automated workflow is also multiplied
> across everything it touches.

## The whole thing in one paragraph

**Vulnerability management** is a never-ending loop: **identify** weaknesses
(scans, SAST/DAST, pen tests, threat feeds, bug bounties, audits), **analyze**
them (confirm false positives/negatives, prioritize using **CVE** IDs and **CVSS**
scores adjusted by exposure and business impact), **respond** (patch, segment,
compensating controls, insurance, or a documented **exception**), and **validate**
by **rescanning** and reporting. **Security monitoring** watches systems, apps,
and infrastructure through log aggregation, alerting, **quarantine**, and **alert
tuning**, powered by tools like the **SIEM** (the hub), SCAP, antivirus, DLP,
NetFlow, and SNMP traps, agent-based or agentless. And **automation and
orchestration** (often **SOAR**) scale all of this — provisioning, guard rails,
ticketing, CI/CD — acting as a **workforce multiplier** while introducing risks of
complexity, cost, and a single point of failure.

## On the exam

- Know the loop: **identify → analyze → respond → validate (rescan) → report**.
- **CVE** is the unique *identifier* of a vulnerability; **CVSS** is its 0–10
  *severity score*. Don't swap them.
- **False positive** = flagged but not real (wastes time); **false negative** =
  real but missed (dangerous). Analysts most fear false negatives.
- A high CVSS doesn't automatically mean "fix first" — context like **exposure**
  and **asset importance** reprioritizes it.
- A documented decision *not* to fix a vulnerability right now is an **exception/
  exemption** (accepting the risk).
- **SIEM** is the correlation/log hub; **SOAR** adds automated response. If the
  stem says "automatically respond to alerts," think SOAR/automation.
- **Alert tuning** fixes **alert fatigue** from too many false alarms.
- Automation's classic downside is becoming a **single point of failure**.
