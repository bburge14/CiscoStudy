# Network Security, Compliance & Hardening

With identity and data covered, security's remaining job is to control traffic
between systems and to prove the whole environment meets its obligations. This
lesson covers **network security** — segmentation, firewalls, and the zero-trust
model — and **compliance and hardening** — the frameworks you answer to and the
posture work that keeps the environment defensible.

## Segmentation: limit the blast radius

The first principle of network security is **don't let everything talk to
everything.** Segmentation divides the network so a compromise in one place can't
spread freely.

- **Network segmentation** splits the VPC into subnets/tiers (web, app, data) with
  controlled paths between them, so a breached web server can't reach the database
  directly.
- **Microsegmentation** pushes this further, down to per-workload policy: each
  service only accepts the specific flows it needs, even from neighbors in the
  same subnet.
- **Security groups** (stateful, instance-level) and **NACLs** (stateless,
  subnet-level) are the cloud's enforcement tools; use default-deny and open only
  required ports from specific sources.

## Firewalls and traffic inspection

- A **next-generation firewall (NGFW)** filters beyond ports — it's
  application-aware and can do intrusion prevention and TLS inspection.
- A **WAF (web application firewall)** sits in front of web apps and blocks
  application-layer attacks (SQL injection, cross-site scripting) that a network
  firewall can't see.
- **IDS/IPS** detect (IDS) or detect-and-block (IPS) known malicious patterns.
- **DDoS protection** absorbs or filters volumetric floods before they reach your
  service — essential for anything internet-facing.
- A **bastion host / jump box** is the single hardened, monitored entry point for
  administrative access into private subnets, so instances never expose SSH/RDP to
  the internet.

### Reaching services privately

- **Private endpoints / service endpoints** let you reach a managed service (object
  storage, a database) over the provider's private network instead of the public
  internet, keeping traffic off the open net.
- **Egress filtering** controls *outbound* traffic — often overlooked, but it's how
  you stop a compromised instance from calling home to an attacker or exfiltrating
  data.

## Zero trust

The old model trusted anything "inside" the network perimeter. **Zero trust**
abandons that assumption.

> Zero trust means **never trust, always verify**: every request is authenticated,
> authorized, and encrypted *regardless of where it originates*, inside or outside
> the network. Trust is based on verified identity and device posture, not network
> location.

In practice this means strong identity (MFA), least-privilege authorization on
every call, microsegmentation, and continuous verification — assume the network is
already hostile and the perimeter is gone. It pairs naturally with cloud, where
"inside the LAN" no longer means anything.

## Compliance: proving you meet the rules

**Compliance** is demonstrating that your environment satisfies external
regulations and standards. You should recognize the major ones and what they
cover:

| Framework | Scope |
|-----------|-------|
| **PCI DSS** | Payment card data |
| **HIPAA** | U.S. healthcare / protected health information |
| **GDPR** | EU personal data and privacy |
| **SOC 2** | Service-organization controls (security, availability, confidentiality) |
| **ISO/IEC 27001** | International information-security management standard |
| **FedRAMP** | U.S. government cloud authorization |

Related obligations: **data sovereignty/residency** (keep data in a jurisdiction),
**audits** (independent checks you must evidence with logs and reports), and the
**shared responsibility model** — the provider certifies the infrastructure, but
your configuration and data handling are *your* compliance burden to prove.

## Hardening and posture management

**Hardening** reduces a system's attack surface by removing or locking down
anything not required.

- **Secure baselines / benchmarks** — configure systems to a known-good standard.
  The **CIS Benchmarks** are the widely used, vendor-neutral hardening guides.
- **Least functionality** — install and enable only what the role needs; disable
  default accounts, unused services, and open ports. Change default credentials
  always.
- **Vulnerability scanning** — regularly scan images and running systems for known
  flaws, and remediate by severity.
- **Patch management** — keep systems current (see the Operations unit); unpatched
  known vulnerabilities are a leading breach cause.
- **CSPM (cloud security posture management)** — continuously scans your cloud
  configuration for misconfigurations and drift from policy (a public bucket, an
  open security group, unencrypted storage) and flags or fixes them. Because most
  cloud breaches are *misconfigurations*, CSPM is the posture tool built for the
  cloud.
- **Penetration testing** — authorized simulated attacks validate that the
  hardening actually holds (coordinate with the provider per their rules).

## Exam focus

- **Segmentation** limits blast radius; **microsegmentation** enforces per-workload
  policy. Default-deny with **security groups** (stateful) and **NACLs**
  (stateless), opening only required ports from specific sources.
- **NGFW** = app-aware filtering/IPS; **WAF** = blocks web-app attacks (SQLi/XSS);
  **IDS detects, IPS blocks**; **DDoS protection** for internet-facing services; a
  **bastion/jump box** is the single hardened admin entry point.
- **Private/service endpoints** keep traffic off the public internet; **egress
  filtering** stops exfiltration and call-home.
- **Zero trust = never trust, always verify**, based on identity and device posture
  *regardless of network location* — assume the perimeter is gone.
- Match frameworks to scope: **PCI DSS** (cards), **HIPAA** (health), **GDPR** (EU
  privacy), **SOC 2**, **ISO 27001**, **FedRAMP** (US gov). Your **configuration and
  data** remain your compliance responsibility.
- Harden with **CIS Benchmarks**, **least functionality** (disable defaults/unused
  services), **vulnerability scanning**, and **patching**. **CSPM** catches cloud
  **misconfigurations** — the leading cause of cloud breaches.
