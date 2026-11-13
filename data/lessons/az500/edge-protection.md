# Edge Protection: Web Application Firewall & DDoS Protection

Internet-facing applications face two very different kinds of attack. One is a
flood of traffic meant to knock you offline; the other is a crafted request meant
to exploit your application's logic. Azure answers them with two distinct edge
services: **DDoS Protection** for volumetric floods and the **Web Application
Firewall (WAF)** for application-layer exploits. They operate at different layers,
and the exam wants you to know which defends against what.

## The Web Application Firewall (WAF)

> A **WAF** inspects **HTTP/HTTPS (Layer 7)** requests and blocks application-layer
> attacks — **SQL injection, cross-site scripting (XSS)**, and the rest of the
> **OWASP Top 10** — before they reach your web app.

Where you run a WAF depends on whether your app is regional or global:

- **WAF on Azure Application Gateway** — a **regional**, Layer-7 load balancer.
  Use it to protect apps hosted in a specific region.
- **WAF on Azure Front Door** — a **global**, edge-delivered reverse proxy and
  CDN. Use it to protect globally distributed apps and block malicious traffic
  near its source, at the edge.

> **Regional vs global is the deciding question.** Application Gateway WAF =
> regional; Front Door WAF = global. Match the WAF to where the app lives.

### WAF rules and modes

A WAF policy combines managed and custom rules:

- **Managed rule sets** do the heavy lifting: the **OWASP Core Rule Set (CRS)** on
  Application Gateway and the **Microsoft Default Rule Set (DRS)** on Front Door,
  maintained by Microsoft against common exploits.
- **Custom rules** let you add your own logic — allow/deny by IP or geography,
  match on headers or query strings, and apply **rate limiting** to throttle
  clients sending too many requests.
- **Bot protection** rules classify traffic as good, bad, or unknown bots.

The WAF runs in one of two modes:

- **Detection mode** — logs what it *would* block but takes no action; use it to
  tune rules and find false positives before enforcing.
- **Prevention mode** — actively blocks matching requests. Move to prevention once
  you've validated the rules.

### A little more on the two front ends

Beyond "regional vs global," each front end adds security value worth knowing:

- **Application Gateway** terminates TLS and can re-encrypt to backends
  (**end-to-end TLS**), supports mutual TLS, and keeps traffic inside your VNet —
  useful when the app and its data must stay regional.
- **Front Door** is delivered from Microsoft's global edge, can reach backends
  privately via **Private Link origins**, offers **geo-filtering** and caching, and
  blocks bad traffic far from your origin. The **WAF policy** is an independent
  resource you **associate** with the Gateway listener or the Front Door profile,
  so one policy can be reused.

## Azure DDoS Protection

A **distributed denial-of-service (DDoS)** attack overwhelms a target with traffic
from many sources. These are **network-layer (L3/L4) volumetric** attacks, and a
WAF is the wrong tool for them.

> **Azure DDoS Protection** defends public IP endpoints against volumetric and
> protocol floods with **always-on traffic monitoring** and **automatic
> mitigation** that scales with Azure's global network capacity.

Important baseline: **DDoS infrastructure (basic) protection is always on for
free** at the platform level for all Azure traffic. The paid tiers add tuned,
per-resource protection, telemetry, alerting, and cost protection:

- **DDoS Network Protection** — protects **all** public IPs in the virtual
  networks it's enabled on; priced per protected VNet/plan. Good for larger estates
  with many public endpoints.
- **DDoS IP Protection** — protects **individual** public IP addresses; pay per
  protected IP. Good when you have only a few endpoints to cover.

The paid tiers add **adaptive tuning** (it learns your normal traffic to set
mitigation thresholds), rich attack **telemetry and metrics**, alerting, rapid
response support, and **cost-protection credits** for scale-out caused by an
attack.

## WAF vs DDoS — the clean split

| | **WAF** | **DDoS Protection** |
|---|---|---|
| Layer | L7 (HTTP/S application) | L3/L4 (network/transport) |
| Stops | SQLi, XSS, OWASP Top 10, bad bots | Volumetric/protocol floods |
| Attached to | App Gateway (regional) / Front Door (global) | Public IPs / VNets |
| Question cue | "malicious request / injection / OWASP" | "flood / overwhelm / availability" |

They are layered, not either/or: a hardened front end runs **DDoS Protection on
its public IP and a WAF on the application traffic**, so it survives both a flood
and a crafted exploit.

## Putting it together

At the internet edge, defend availability and application integrity separately.
**DDoS Protection** watches your public IPs and absorbs **volumetric L3/L4 floods**
automatically — basic protection is always on, and the **Network** or **IP**
tiers add tuning, telemetry, and cost protection. The **WAF** inspects **L7**
traffic and blocks **OWASP-class attacks** using managed rule sets plus custom and
rate-limiting rules; run it on **Application Gateway** for regional apps or
**Front Door** for global ones, and start in **detection** mode before switching to
**prevention**.

## Exam focus

- **WAF = Layer 7.** It blocks **SQL injection, XSS, and the OWASP Top 10**.
  "Crafted/malicious request" or "injection" ⇒ WAF.
- **Application Gateway WAF = regional; Front Door WAF = global.** Pick by where
  the app runs; Front Door blocks at the edge for globally distributed apps.
- WAF uses **managed rule sets** (OWASP CRS / Microsoft DRS) plus **custom rules**
  (geo/IP filtering, **rate limiting**, bot rules). **Detection mode** logs only;
  **prevention mode** blocks.
- **DDoS Protection = Layer 3/4 volumetric floods**; "flood/overwhelm/availability"
  ⇒ DDoS. Basic/infrastructure protection is **always on and free**.
- Paid tiers: **DDoS Network Protection** (all public IPs in a VNet) vs **DDoS IP
  Protection** (per individual public IP). Paid tiers add **adaptive tuning**,
  telemetry, and **cost protection**.
- WAF and DDoS are **complementary layers**, not alternatives.
