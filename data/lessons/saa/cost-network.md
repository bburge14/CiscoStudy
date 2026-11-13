# Cost-Optimized Networking & Data Transfer

Data transfer is the cost most teams forget to budget for, and the exam knows it.
Moving bytes between AZs, between Regions, out to the internet, or through a NAT
gateway all carry charges, and a few design choices cut them dramatically. The key
is to understand AWS's transfer pricing model, then apply the right lever: bypass
expensive paths, cache at the edge, or simply keep traffic close. The guiding fact:
**data *into* a Region is generally free; data *out* is what you pay for.**

## The data transfer cost model

> **Data transfer *into* a Region from the internet is generally free. Data
> transfer *out* to the internet is billed. Traffic between AZs and between Regions
> also costs money; traffic within a single AZ using private IPs is cheapest.**

That single model drives most of the answers below: reduce outbound internet
transfer, reduce cross-AZ and cross-Region chatter, and avoid metered middleboxes
like NAT gateways where you can.

## Bypass the NAT gateway for AWS services

NAT gateways charge both an hourly fee and a per-GB **data-processing** charge, so
sending large volumes of AWS-service traffic through one is expensive.

> **For private-subnet workloads pulling large volumes from S3 or DynamoDB, create
> a *gateway VPC endpoint* so that traffic bypasses the NAT gateway entirely. Gateway
> endpoints are free and eliminate the NAT data-processing charge.**

This is the single most common cost-network answer: private instances reading a lot
from S3 → gateway endpoint, not a bigger or second NAT gateway.

## Reduce data-transfer-out to the internet

- **CloudFront in front of an S3 origin** — serving popular static assets straight
  from S3 racks up data-transfer-out charges; putting CloudFront in front caches at
  the edge and lowers those costs (edge-to-user transfer is cheaper, and cache hits
  skip the origin).
- **CloudFront price classes** — if your users are concentrated in, say, North
  America and Europe, select a **price class** that limits delivery to the needed,
  less expensive edge locations instead of paying for the most expensive ones
  worldwide.
- **AWS Direct Connect** — for very large, *sustained* transfers from AWS back to an
  on-premises data center, Direct Connect offers lower data-transfer-out pricing
  than the public internet.
- **S3 Requester Pays** — when publishing large public datasets, enable Requester
  Pays so the *downloader* covers the data-transfer and request costs, not you.

## Keep traffic close

- **Same AWS Region as the workload** — a bucket repeatedly read by EC2 should live
  in the **same Region** as the instances to avoid inter-Region transfer charges.
- **Same Availability Zone** — chatty, high-volume traffic between two tiers in
  different AZs incurs cross-AZ charges; where resilience requirements allow, keep
  heavily communicating components in the **same AZ** using private IPs.

Note the tension with resilience: multi-AZ improves availability but adds cross-AZ
transfer cost. The exam expects you to balance them ("within HA limits").

## Connecting VPCs cost-effectively

When only **two** VPCs exchange a large volume of traffic, a **VPC peering**
connection avoids the per-attachment hourly charge and some per-GB processing of
**AWS Transit Gateway**. Transit Gateway earns its cost at scale (many VPCs,
transitive routing); for a simple two-VPC link, peering is cheaper.

## Trim replication traffic

Cross-Region replication copies cost inter-Region transfer. If only a subset of
objects actually needs to exist in the second Region, **scope the replication rule**
(by prefix or tag) to replicate just those objects rather than the whole bucket.

## A worked example

Private instances downloading terabytes from S3 through a NAT gateway are racking up
data-processing charges, so the team adds an **S3 gateway endpoint** — free, and the
NAT charges vanish. A popular download site puts **CloudFront** in front of its S3
origin and picks a **price class** matching its North-America/Europe audience. A
public research dataset switches on **S3 Requester Pays**. Two VPCs that only need to
talk to each other use **VPC peering** rather than Transit Gateway, and an
over-broad cross-Region replication rule is **scoped by prefix** to copy only what
the DR plan requires.

## The cost-versus-resilience tension

Cost-network questions often hide a trade-off against the resilience domain, and
the exam expects you to respect both. Spreading tiers across Availability Zones
improves fault tolerance but adds cross-AZ transfer charges; a single NAT gateway
is cheaper but is itself a single point of failure, while one NAT gateway *per AZ*
is resilient but costs more. The right instinct is: cut data-transfer cost *within
the resilience the requirement demands*, not below it. If a question stresses high
availability, do not "optimize" by collapsing everything into one AZ — instead
reach for the levers that save money *without* sacrificing it, like gateway
endpoints, CloudFront, and same-Region placement.

One more distractor to recognize: adding a **second NAT gateway** or giving
instances **public IPs** are tempting-looking wrong answers to "high NAT costs for
S3 traffic." Both increase cost or exposure; the correct move is a free **gateway
VPC endpoint** that removes the S3 traffic from the NAT path altogether.

## Exam focus

- Transfer **in** is generally free; transfer **out** is billed; **cross-AZ** and
  **cross-Region** cost money; **same-AZ private IP** is cheapest.
- Private workloads reading lots from S3/DynamoDB → **gateway VPC endpoint** (free,
  bypasses NAT data-processing charges) — not a second NAT gateway.
- Lower data-transfer-out → **CloudFront** in front of S3, a matching **price
  class**, **Direct Connect** for sustained on-prem transfer, and **S3 Requester
  Pays** for public datasets.
- Keep the bucket in the **same Region** as EC2; co-locate chatty components in the
  **same AZ** within HA limits.
- Two VPCs, high traffic → **VPC peering** (avoids Transit Gateway per-attachment and
  per-GB charges). Trim CRR cost by **scoping the replication rule** (prefix/tag).
