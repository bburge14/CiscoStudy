# Cloud Security Posture: Secure Score & Compliance

Microsoft Defender for Cloud does two complementary jobs. It **strengthens your
posture** — finding misconfigurations and weak settings before an attacker does —
and it **protects workloads** with threat detection (the next lesson). This lesson
is about the posture half: cloud security posture management (CSPM), the secure
score that measures it, and the regulatory compliance dashboard that maps it to
standards. Defender for Cloud covers Azure and, through connectors, **AWS and
GCP**, so "cloud" here means multicloud.

## CSPM: continuously assessing your configuration

**Cloud Security Posture Management** continuously inspects your resources against
security best practices and produces **recommendations** — concrete hardening
actions like "enable encryption on this storage account" or "restrict this NSG
rule."

> The **foundational CSPM** capabilities are **free** and on by default once
> Defender for Cloud is enabled: asset inventory, continuous assessment, secure
> score, and MCSB compliance. The paid **Defender CSPM** plan adds advanced
> features — **attack path analysis**, **agentless scanning**, the **cloud
> security explorer**, risk prioritization, and governance rules.

Recommendations come from a **security initiative**, and the default one is the
**Microsoft Cloud Security Benchmark (MCSB)** — Microsoft's own set of security
best practices, turned on automatically for every subscription.

## Secure score: one number for posture

All those recommendations roll up into a single **secure score**, expressed as a
percentage.

> **Secure score aggregates your security recommendations into a percentage that
> rises as you remediate them.** It groups related recommendations into **security
> controls**, and you earn a control's points only when **all** its recommendations
> are satisfied for a resource — which is why the score rewards finishing a control,
> not just chipping at it.

Secure score gives the SOC a prioritization tool: the portal shows how many points
each control is worth and how many resources are unhealthy, so you can spend effort
where it moves the needle most. Over time the trend line tells leadership whether
posture is improving.

### Managing recommendations

- **Remediate** — fix the finding; many recommendations offer a **"Fix" button**
  or a quick-fix remediation script.
- **Exempt** — mark a recommendation not applicable for a resource (with a
  justification), so it stops dragging the score without being silently ignored.
- **Enforce / Deny** — use governance to assign owners and due dates, or to block
  non-compliant resource creation outright.

Continuous assessment means these states update automatically as your environment
changes — spin up a new VM and it is evaluated against the initiative within the
assessment cycle.

## Regulatory compliance

Secure score answers "how hardened am I?" The **regulatory compliance dashboard**
answers "how do I measure up against a *named standard*?"

> By default the compliance dashboard shows your posture against the **Microsoft
> Cloud Security Benchmark**. You can **add other standards** — NIST SP 800-53,
> PCI DSS, ISO 27001, CIS, SOC 2, and more — assigned at the subscription or
> management-group scope, and the dashboard maps your existing assessments to each
> standard's controls.

Each standard is broken into controls, each control into the assessments that
satisfy it, so you can see exactly which failing checks are blocking compliance and
generate a report (PDF/CSV) for auditors. Note that assessing against the broad
catalog of regulatory standards is a capability associated with the paid **Defender
CSPM** plan.

## Seeing risk the way an attacker does

The paid **Defender CSPM** plan adds two tools that go beyond a flat list of
recommendations:

- **Attack path analysis** connects individual weaknesses into the *chain* an
  attacker could walk — for example, "internet-exposed VM → has a known
  vulnerability → holds a managed identity with rights to a sensitive storage
  account." Fixing one link breaks the whole path, so attack paths help you
  prioritize the few fixes that matter most.
- **Cloud security explorer** lets you query your cloud graph ("show all
  internet-exposed VMs with high-severity vulnerabilities") to proactively find
  risky combinations before they become incidents.

> A plain recommendation says *this resource is misconfigured*. An **attack path**
> says *here is how that misconfiguration gets chained to reach something
> valuable* — context that changes what you fix first.

## Multicloud and hybrid

Defender for Cloud is not Azure-only. You connect **AWS and GCP** accounts through
native cloud connectors, and on-premises or other-cloud servers through Azure Arc.
Once connected, the same recommendations, secure score, and compliance dashboard
span all of them — one posture view across the whole estate.

## Exam focus

- **Foundational CSPM is free and default** (asset inventory, continuous
  assessment, secure score, MCSB compliance). **Defender CSPM** is the paid plan
  that adds **attack path analysis, agentless scanning, cloud security explorer**,
  and advanced regulatory compliance.
- The default initiative/standard is the **Microsoft Cloud Security Benchmark
  (MCSB)**, enabled automatically.
- **Secure score** is a **percentage** that aggregates recommendations into
  **security controls**; you get a control's points only when **all** its
  recommendations pass for a resource. Rising score = better posture.
- The **regulatory compliance dashboard** maps your posture to named standards
  (**NIST, PCI DSS, ISO 27001, CIS**), which you add per subscription/management
  group; MCSB shows by default.
- Recommendations can be **remediated** (often a one-click **Fix**), **exempted**,
  or **enforced** via governance. Defender for Cloud is **multicloud** (Azure, AWS,
  GCP) and hybrid via **Azure Arc**.
