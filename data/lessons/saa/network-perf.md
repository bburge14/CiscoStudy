# High-Performing Networking & Content Delivery

Latency is distance plus congestion. High-performing network design shortens the
distance (serve from the edge, route to the nearest Region) and removes congestion
(dedicated links, faster NICs). The exam gives you a latency or throughput problem —
global users, a chatty non-HTTP protocol, an unreliable internet path — and asks for
the service that fixes it. The two edge services, CloudFront and Global Accelerator,
cause the most confusion, so pin down the difference early.

## Content delivery at the edge: CloudFront

> **Amazon CloudFront is a content delivery network (CDN) that caches content at
> edge locations close to users, cutting latency for globally distributed
> audiences.** Point it at an origin (an S3 bucket or an application) and users are
> served from the nearest edge.

Related CloudFront features:

- **Origin group with origin failover** — configure a primary and secondary origin
  so CloudFront retries the secondary if the primary returns errors.
- **Lambda@Edge / CloudFront Functions** — run lightweight code at edge locations to
  customize requests and responses (header manipulation, simple redirects) without
  a round trip to the Region.

## CloudFront versus Global Accelerator

Both use the AWS global edge network, but they solve different problems.

| | CloudFront | AWS Global Accelerator |
|---|-----------|------------------------|
| Caches content? | **Yes** (CDN) | No |
| Protocols | HTTP/HTTPS | **TCP and UDP** |
| IP addresses | DNS-based, dynamic | **Two static anycast IPs** |
| Best for | Cacheable web/media | Non-HTTP apps, static IPs, fast regional failover |

> **Global Accelerator provisions two static anycast IP addresses and routes users
> over the AWS backbone to the nearest healthy Region, with fast regional failover
> — but it does not cache.** Choose it for latency-sensitive, non-HTTP (TCP/UDP)
> applications that need fixed IPs; choose CloudFront for cacheable HTTP content.

## Route 53 routing policies for performance

DNS can steer users to the best endpoint. The performance-oriented policies:

- **Latency-based routing** — send each user to the Region that gives them the
  **lowest network latency**. The default answer for "lowest latency across
  Regions."
- **Geolocation routing** — return different endpoints (and localized content) based
  on the user's **country**, for compliance or language.
- **Geoproximity routing (with bias)** — route by geographic distance and shift
  traffic between Regions by adjusting a **bias** value that grows or shrinks a
  Region's service area.

Don't confuse latency-based ("fastest for the user") with geolocation ("based on
where they are, regardless of speed").

## Connectivity: Direct Connect and VPC peering

- **AWS Direct Connect** — a dedicated, consistent, high-bandwidth **private**
  network link between an on-premises data center and AWS, avoiding the variability
  of the public internet. The answer when a requirement names consistent,
  dedicated bandwidth to AWS.
- **VPC peering** — a private, low-latency connection between **two** VPCs using
  private IPs; ideal when only two VPCs owned by the same company need to talk.

## Faster instance networking: enhanced networking

Within a Region, instances can push more packets with less overhead:

> **Enhanced networking with the Elastic Network Adapter (ENA) gives very high
> throughput and packets-per-second with consistently low latency between EC2
> instances.** It is the answer for raw instance-to-instance network performance
> (distinct from EFA, which targets tightly coupled HPC/MPI).

## A worked example

A global, read-heavy application in one Region is slow for distant users. Two
complementary moves: serve static content through **CloudFront** edge locations, and
add **cross-Region read replicas** (or a global database) so reads happen closer to
users. A separate real-time multiplayer service uses UDP and needs fixed IPs and
fast failover between Regions — that is **Global Accelerator**, not CloudFront. For
users spread worldwide hitting a multi-Region deployment, **latency-based routing**
sends each to the quickest Region.

## CloudFront or Global Accelerator? A decision path

Because these two services share the edge network, questions deliberately make them
look interchangeable. Walk this short path:

1. **Is the content cacheable HTTP/HTTPS** (images, video, static or semi-static
   web pages, APIs with cacheable responses)? → **CloudFront**.
2. **Is it a non-HTTP protocol (TCP/UDP), or does it need static IPs to
   allowlist**, or **fast failover between Regions with no caching**? → **Global
   Accelerator**.
3. **Do you need both** — cache web assets *and* accelerate a separate TCP/UDP
   service? Use each for its job; they are not mutually exclusive.

A parallel warning applies to Route 53: a routing policy only points DNS at an
endpoint — it does **not** cache or accelerate anything. If the requirement is
"serve content faster," that is CloudFront, not a clever routing policy. Route 53
policies answer "*which* endpoint," not "*how fast* the bytes travel."

## Exam focus

- Cache content near users globally → **CloudFront** (CDN). Retry a backup origin →
  **origin group / origin failover**. Run code at the edge → **Lambda@Edge /
  CloudFront Functions**.
- Non-HTTP (TCP/UDP), two **static anycast IPs**, fast regional failover, no caching
  → **Global Accelerator**. Cacheable HTTP → **CloudFront**.
- Route 53: **latency-based** = lowest latency Region; **geolocation** = by country;
  **geoproximity (bias)** = shift traffic between Regions.
- Dedicated, consistent private bandwidth to on-prem → **Direct Connect**. Two VPCs,
  private low-latency → **VPC peering**.
- High instance-to-instance throughput/PPS with low latency → **enhanced networking
  (ENA)**.
