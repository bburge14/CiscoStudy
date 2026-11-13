# Network Security: VPC Firewalls & Private Connectivity

A Virtual Private Cloud (VPC) is your own logically isolated network in AWS. The
exam tests whether you can filter traffic with the right firewall, keep workloads
off the public internet, and connect VPCs and data centers securely. Two
distinctions do most of the heavy lifting here: **security groups versus network
ACLs**, and **gateway versus interface endpoints**. Get those cold and most
questions answer themselves.

## Two firewalls: security groups and network ACLs

Every VPC gives you two layers of packet filtering. They look similar but behave
very differently, and the exam leans hard on the contrast.

> **Security groups are *stateful* and operate at the instance/ENI level: if you
> allow inbound traffic, the return traffic is automatically permitted. They
> support *allow* rules only.**
>
> **Network ACLs are *stateless* and operate at the subnet level: they evaluate
> numbered rules in order and support both *allow* and *deny* rules, but they have
> no memory, so return traffic needs its own explicit rule.**

| | Security group | Network ACL |
|---|----------------|-------------|
| Scope | Instance / ENI | Subnet |
| State | Stateful (return traffic auto-allowed) | Stateless (both directions explicit) |
| Rules | Allow only | Allow **and** deny |
| Evaluation | All rules together | Numbered, lowest first, stops at match |

Two consequences the exam tests directly:

- **Stateless means ephemeral ports.** If a NACL allows inbound HTTP on port 80 but
  responses are dropped, you must add an **outbound** rule for the **ephemeral port
  range** (typically 1024–65535) so return traffic can leave.
- **Only a NACL can deny.** To explicitly block a single malicious IP from an
  entire subnet, use a **NACL deny rule** — security groups cannot express a deny.

A powerful pattern: in a security group rule you can reference *another security
group* as the source. So an app tier can allow traffic only from the web tier's
security group, and it keeps working even as the web tier's instances scale in and
out and their IPs change — no IP lists to maintain.

## Seeing and detecting traffic

- **VPC Flow Logs** capture *metadata* about IP traffic on network interfaces —
  source, destination, ports, and accept/reject — for troubleshooting and intrusion
  analysis. They do **not** capture packet payloads.
- **Amazon GuardDuty** is the managed threat-detection service that continuously
  analyzes CloudTrail events, VPC Flow Logs, and DNS logs to flag malicious or
  unauthorized behavior. You turn it on; there is nothing to deploy inline.
- **AWS Network Firewall** is a managed, *stateful* firewall at the VPC perimeter
  with intrusion-prevention signatures and outbound domain filtering that can apply
  across many VPCs. Reach for it when a question asks for deep, managed perimeter
  inspection beyond what security groups and NACLs provide.

## Keeping workloads private

Most secure designs keep instances off the public internet entirely.

> **A NAT gateway lets instances in a *private* subnet make *outbound* connections
> (to download patches, say) while remaining unreachable from the internet.** Place
> the NAT gateway in a public subnet and point the private subnet's default route
> at it.

### VPC endpoints: reach AWS services without the internet

A workload in a private subnet can still call AWS service APIs privately using
**VPC endpoints**, which come in two flavors:

- **Gateway endpoints** — for **S3 and DynamoDB only**. They add a route in your
  route table and cost nothing. Attach a **VPC endpoint policy** to restrict which
  buckets the endpoint may reach, helping prevent data exfiltration.
- **Interface endpoints (AWS PrivateLink)** — an elastic network interface with a
  private IP in your subnet, used for most *other* services (SQS, Systems Manager,
  and so on). This is how a private-subnet workload calls the SQS API without any
  NAT gateway or internet path.

### PrivateLink for your own services

**AWS PrivateLink** also lets a provider publish an **endpoint service** (behind a
Network Load Balancer) that consumers reach through interface endpoints in their
own VPCs — private SaaS consumption with no VPC peering and no internet exposure.

## Connecting many VPCs and on-premises

- **VPC peering** — a one-to-one private connection between two VPCs. Simple, but
  it does **not** route transitively, so a full mesh of many VPCs becomes
  unmanageable.
- **AWS Transit Gateway** — a central hub that connects hundreds of VPCs and your
  on-premises network with *transitive* routing, replacing the messy mesh. This is
  the answer whenever the scale is "hundreds of VPCs through a central hub."

## A worked example

An application tier must accept traffic only from a web tier whose instances scale
constantly. The cleanest design is to reference the web tier's **security group**
as the source in the app tier's inbound rule — not a list of IPs. If the same
design also needs to call SQS privately, add an **interface VPC endpoint** for SQS
so no traffic leaves for the public internet.

## Exam focus

- **Security group = stateful, instance level, allow-only.** **NACL = stateless,
  subnet level, allow + deny.** Stateless NACLs need an explicit **ephemeral-port**
  outbound rule for return traffic.
- Block a single IP for a whole subnet → **NACL deny rule** (security groups cannot
  deny). Allow only the web tier → **reference its security group** as the source.
- **VPC Flow Logs** = IP flow metadata, no payloads. **GuardDuty** = managed threat
  detection from CloudTrail, VPC Flow Logs, and DNS logs.
- **NAT gateway** = outbound-only internet for private subnets. **Gateway
  endpoint** (free) = private S3/DynamoDB access; restrict it with a **VPC endpoint
  policy**. **Interface endpoint / PrivateLink** = private access to most other
  services (e.g., SQS).
- **PrivateLink endpoint service** (behind an NLB) = expose your own service
  privately to consumers. **Transit Gateway** = hub-and-spoke for hundreds of VPCs
  plus on-prem; **VPC peering** = two VPCs, non-transitive.
- **AWS Network Firewall** = managed stateful VPC-perimeter firewall with IPS and
  domain filtering.
