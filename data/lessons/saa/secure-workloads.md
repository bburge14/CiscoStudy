# Securing Workloads: Threat Detection, Protection & Governance

IAM locks the doors and VPC firewalls filter the halls; this lesson is about
*watching* the building and *responding* when something goes wrong. The SAA exam
presents a security need — "detect threats," "block an HTTP flood," "find PII,"
"patch a fleet" — and asks for the one service that fits. The trick is that many of
these services sound alike, so this lesson sorts them into three jobs: see,
protect, and operate.

## Seeing: audit, configuration, and detection

> **AWS CloudTrail records *who* made which API call, from which IP, and when. AWS
> Config records *what your resources look like* over time and evaluates them
> against rules.** CloudTrail answers "who did it"; Config answers "is it compliant
> and how did it change."

- **AWS CloudTrail** — the audit log of API activity across the account. Use it in
  an investigation to pin down a specific action to an identity.
- **AWS Config** — continuously records resource configurations, evaluates them
  against rules (for example, "no S3 bucket may be public"), shows a compliance
  timeline, and can auto-remediate drift.
- **Amazon GuardDuty** — managed threat detection that analyzes CloudTrail, VPC
  Flow Logs, and DNS logs for malicious behavior.
- **Amazon Inspector** — automated, continuous vulnerability scanning of EC2
  instances, container images in ECR, and Lambda functions for known CVEs and
  unintended network exposure.
- **Amazon Macie** — uses machine learning to discover and classify sensitive data
  such as **PII** stored in S3 buckets.

### Tying it together across accounts

As findings pile up from many services and accounts, two services help you make
sense of them:

- **AWS Security Hub** — a single place that **aggregates and prioritizes**
  findings from GuardDuty, Inspector, and Macie across many accounts, and runs
  automated best-practice and compliance checks (such as CIS benchmarks).
- **Amazon Detective** — after a finding, it helps you **investigate root cause**
  by analyzing relationships and behavior over time across VPC Flow Logs,
  CloudTrail, and GuardDuty findings.

The clean split: **Security Hub aggregates and scores** (the dashboard);
**Detective investigates** (the magnifying glass).

## Protecting: edge and application defenses

Public-facing applications attract floods and injection attacks. AWS layers
defenses at the edge:

> **AWS WAF (a web ACL) inspects HTTP(S) requests and blocks application-layer
> attacks such as SQL injection and cross-site scripting.** A **rate-based rule**
> blocks any IP that exceeds a request threshold — the answer for HTTP floods and
> credential-stuffing from individual IPs.

- **AWS Shield** — DDoS protection. **Shield Standard** is free and automatic;
  **Shield Advanced** adds enhanced protection against large, sophisticated DDoS
  attacks, 24/7 response support, and cost protection for scaling triggered by an
  attack.
- **CloudFront geographic (geo) restrictions** — allow or block viewers by country,
  for licensing or compliance that limits delivery to specific countries.
- **AWS Firewall Manager** — centrally defines and enforces WAF rules, Shield
  protections, and security group policies across **all accounts in AWS
  Organizations**, so a new account inherits the standard automatically.

A useful mental model: **WAF** filters bad *requests*, **Shield** absorbs *volume*
attacks, and **Firewall Manager** makes sure both are applied *everywhere* at once.

## Operating: patch, access, and metadata hygiene

Day-to-day operations are where many breaches actually start, so AWS Systems
Manager carries several exam-relevant tools:

- **Systems Manager Patch Manager** — patches operating systems across a large EC2
  fleet on a schedule and reports patch compliance, with minimal manual effort.
- **Systems Manager Session Manager** — gives shell access to instances in private
  subnets **without opening inbound SSH (port 22)** or bastion hosts. This is the
  secure answer whenever a policy forbids inbound SSH/RDP.
- **IMDSv2** — requiring token-backed, session-oriented requests to the EC2
  instance metadata service helps defend the instance's role credentials against
  theft through server-side request forgery (SSRF). Enforcing IMDSv2 is a standard
  hardening step.

## A worked example

A security team runs many accounts and wants one console that pulls together
GuardDuty, Inspector, and Macie findings and checks them against CIS — that is
**Security Hub**. When a specific GuardDuty finding needs a deep root-cause dig
across weeks of flow logs and API calls, they switch to **Detective**. If the same
application is getting hammered by an HTTP flood at its ALB, a **WAF rate-based
rule** sheds the abusive IPs, and if the attacks grow into large volumetric DDoS,
**Shield Advanced** provides the heavier protection and response support.

## Exam focus

- **CloudTrail** = who made which API call (audit). **Config** = resource
  configuration history and compliance rules (e.g., no public S3).
- **GuardDuty** = threat detection from logs. **Inspector** = vulnerability/CVE
  scanning of EC2, ECR images, and Lambda. **Macie** = find and classify PII in S3.
- **Security Hub** = aggregate and prioritize findings + compliance standards
  across accounts. **Detective** = investigate root cause across related data.
- **WAF web ACL** = block SQLi/XSS; **WAF rate-based rule** = block IPs over a
  request threshold (HTTP floods, credential stuffing).
- **Shield Standard** (free) vs **Shield Advanced** (large DDoS, 24/7 support, cost
  protection). **CloudFront geo restrictions** = allow/block by country.
- **Firewall Manager** = centrally enforce WAF/Shield/SG policies across
  Organizations.
- **Patch Manager** = scheduled OS patching + compliance. **Session Manager** =
  private shell access with no inbound SSH. **IMDSv2** = protect instance role
  credentials from SSRF.
