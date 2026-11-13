# Compliance, Governance & Security Services

You've seen *who* is responsible (the Shared Responsibility Model) and *how* access
is controlled (IAM). This lesson covers the rest of the security picture:
**governance** (setting rules across many accounts), **compliance** (proving you
meet external standards), and the **security services** AWS gives you to detect,
protect, and audit. There are a lot of service names here — the trick is to learn
each one's *job*, because exam questions describe the job and ask for the name.

## Governance across many accounts

Large organizations don't run one AWS account; they run dozens. **AWS
Organizations** ties them together.

> **AWS Organizations** lets you centrally manage **multiple AWS accounts** —
> grouping them, applying policies across them, and combining their bills through
> **consolidated billing** (which can earn volume discounts).

The key governance control inside Organizations is the **Service Control Policy**:

- **Service Control Policies (SCPs)** are **guardrails** that set the *maximum*
  permissions member accounts can have. An SCP can block a whole account from
  using a disallowed service or Region — even an account administrator can't
  exceed what the SCP allows. SCPs **restrict**; they don't grant.

Setting all this up by hand is tedious, so AWS offers a wizard:

- **AWS Control Tower** automates setting up a secure, compliant **multi-account
  environment** (a "landing zone") with sensible guardrails pre-configured. Think
  of it as Organizations best-practices on autopilot.

## Proving compliance

Auditors want evidence. AWS provides services for the paperwork and the
configuration tracking.

| Service | Job |
|---------|-----|
| **AWS Artifact** | Self-service portal to **download AWS's compliance reports** (SOC, PCI DSS, ISO) and manage agreements. |
| **AWS Config** | Records and evaluates your **resource configurations** over time; flags resources that drift out of compliance with rules. |
| **AWS Audit Manager** | **Automates collecting evidence** for audits and mapping it to frameworks. |

AWS itself is certified against many **compliance programs** — PCI DSS, HIPAA, SOC
1/2/3, ISO 27001, FedRAMP, GDPR and more — and Artifact is where you get the proof
of those certifications to show your own auditors.

### Who owns the data

A compliance question customers always ask: who controls my content? The answer is
clear and tested:

> **You, the customer, retain ownership and control of your content.** You choose
> which **Region** your data is stored in (supporting **data residency**
> requirements) and which services process it. AWS does not move or access your
> content for its own purposes.

## Security services: detection

This group *finds* problems. They sound similar, so anchor each to its one-line
purpose.

| Service | Finds / does |
|---------|--------------|
| **Amazon GuardDuty** | Intelligent **threat detection** — continuously analyzes account and network activity logs for malicious behavior. |
| **Amazon Inspector** | Automated **vulnerability scanning** of EC2 instances and container images for software flaws and exposure. |
| **Amazon Macie** | Discovers and protects **sensitive data** (like PII) stored in **Amazon S3** using machine learning. |
| **Amazon Detective** | **Investigates** security findings — analyzes and visualizes relationships to find the **root cause**. |

The clean split: **GuardDuty** *detects* a threat, **Inspector** *scans for*
vulnerabilities, **Macie** *finds sensitive data*, and **Detective** *investigates*
after a finding is raised.

## Security services: protection

This group *blocks* attacks at the network and application edge.

- **AWS Shield** — **DDoS protection**. **Shield Standard** is **automatic and free
  for all customers**, covering common network-layer attacks. **Shield Advanced**
  is a **paid** tier adding protection against larger, more sophisticated attacks
  plus a response team and cost protection.
- **AWS WAF** (Web Application Firewall) — filters **HTTP/HTTPS** traffic to block
  web exploits like **SQL injection** and **cross-site scripting**, using rules you
  define.
- **AWS Firewall Manager** — **centrally** configures and enforces firewall rules
  (WAF rules, Shield Advanced protections) **across all your accounts** at once.

> **Shield Standard = free, automatic DDoS protection for everyone. Shield
> Advanced = paid, enhanced DDoS protection.** This Standard-vs-Advanced contrast
> is a frequent question.

## Data protection and secrets

- **AWS KMS (Key Management Service)** — creates and manages the **encryption keys**
  used to encrypt your data, with tight access control and auditing.
- **AWS Secrets Manager** — securely **stores, retrieves, and automatically
  rotates** secrets such as database passwords and API keys, so they're not
  hard-coded in applications.
- **AWS Certificate Manager (ACM)** — provisions and manages the **TLS/SSL
  certificates** that enable HTTPS, handling renewals for you.

A subtle distinction: **KMS** manages the *keys* that do encryption; **Secrets
Manager** manages *credentials* like passwords and rotates them.

## Visibility and audit

- **AWS Security Hub** — a **central dashboard** that aggregates and prioritizes
  security findings from GuardDuty, Inspector, Macie and others, and checks your
  posture against best-practice standards. One pane of glass for security.
- **AWS CloudTrail** — records **API activity**: *who did what, when, and from
  where* across your account. It's your audit trail for governance and
  investigations. (Don't confuse it with **Amazon CloudWatch**, which monitors
  *performance and operational metrics* — CloudTrail = **who did what**, CloudWatch
  = **how is it performing**.)

## The whole thing in one paragraph

**AWS Organizations** manages many accounts with **consolidated billing** and
**SCP** guardrails, and **Control Tower** sets that up as a governed landing zone.
You prove compliance with **Artifact** (download AWS's audit reports), **Config**
(track resource configuration), and **Audit Manager** (automate evidence) — while
**you keep ownership of your data and choose its Region.** For security, **detect**
with GuardDuty (threats), Inspector (vulnerabilities), Macie (sensitive data) and
Detective (investigation); **protect** with Shield (DDoS: free Standard vs. paid
Advanced), WAF (web exploits) and Firewall Manager (central rules); **secure data**
with KMS (keys), Secrets Manager (credentials) and ACM (certificates); and **audit**
with Security Hub (central findings) and CloudTrail (who did what).

## Exam focus

- **AWS Organizations** = manage multiple accounts + **consolidated billing**;
  **SCPs** = guardrails that cap what member accounts can do (restrict, never
  grant). **Control Tower** = automated multi-account landing zone.
- **AWS Artifact** = download AWS **compliance reports** (SOC, PCI, ISO). **Config**
  = track resource configuration/compliance. **Audit Manager** = automate audit
  evidence.
- The **customer owns their data** and **chooses the Region** (data residency).
- Detection four: **GuardDuty** (threat detection), **Inspector** (vulnerability
  scanning), **Macie** (sensitive data in S3), **Detective** (investigate root
  cause).
- **Shield** = DDoS: **Standard is free/automatic**, **Advanced is paid/enhanced**.
  **WAF** = block web exploits (SQLi, XSS). **Firewall Manager** = central firewall
  rules across accounts.
- **KMS** = manage encryption keys; **Secrets Manager** = store and rotate
  passwords/keys; **ACM** = TLS certificates.
- **Security Hub** = central security dashboard. **CloudTrail** = API activity /
  **who did what** (vs. **CloudWatch** = performance monitoring).
