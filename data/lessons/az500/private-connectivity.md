# Private Link, Private Endpoints, Service Endpoints & Bastion

Most Azure PaaS services — storage accounts, SQL databases, Key Vaults — are born
with a **public endpoint**. Even when access is locked down by keys and firewalls,
having a public front door is a liability. This lesson is about taking those
services *off* the public internet and administering VMs without exposing RDP or
SSH. Two features sound similar but work very differently: **service endpoints**
and **private endpoints**.

## Service endpoints: extend your VNet's identity

> A **virtual network service endpoint** extends your subnet's identity to an
> Azure PaaS service so the service's firewall can allow traffic *from that
> subnet*, and the traffic travels over the **Azure backbone** instead of the
> public internet.

What to understand about them:

- The PaaS resource **keeps its public IP / public endpoint**; you are not giving
  it a private address. You are telling the service "trust traffic coming from
  subnet X."
- You enable the endpoint on the **subnet** (e.g. `Microsoft.Storage`), then add a
  **VNet rule** on the resource's firewall to allow that subnet.
- They are **free**, simple, and good for keeping traffic on the backbone — but
  access is still scoped per-service and the resource remains publicly resolvable.

## Private endpoints and Private Link: a private IP for the service

> A **private endpoint** places a **network interface with a private IP from your
> VNet** in front of a specific PaaS resource. Clients reach the service at that
> private address, and traffic never touches the public internet. **Azure Private
> Link** is the underlying technology.

This is the stronger model, and the differences from service endpoints are exam
gold:

| | **Service endpoint** | **Private endpoint (Private Link)** |
|---|---|---|
| Gives the service | Nothing new — keeps public IP | A **private IP** in your VNet |
| Traffic path | Azure backbone, but to the public endpoint | Fully private to a private IP |
| Reachable from | The enabled subnet only | On-prem and peered VNets too (via the private IP) |
| Granularity | Whole service | A **specific resource** (this storage account) |
| DNS | Normal public DNS | Needs **private DNS** to resolve to the private IP |
| Cost | Free | Billed per endpoint + data |

### The DNS piece you can't skip

A private endpoint is useless if the name still resolves to the public IP.
Clients keep using the normal hostname (e.g.
`mystorage.blob.core.windows.net`), so you integrate an **Azure Private DNS zone**
(like `privatelink.blob.core.windows.net`) that overrides resolution to the
private IP. Misconfigured private DNS is the number-one reason private endpoints
"don't work," and the exam loves to test it.

### Private Link Service

Private Link also runs the other direction: **Private Link Service** lets you
publish *your own* service (sitting behind a Standard Load Balancer) so that other
tenants or VNets can reach it privately through their own private endpoints —
without any VNet peering or public exposure.

## Choosing between them

- Need the resource **completely off the public internet**, reachable from
  **on-premises** over ExpressRoute/VPN, or locked to a **single** resource? →
  **Private endpoint**.
- Just want VNet-scoped access over the backbone at no cost, and a public endpoint
  is acceptable? → **Service endpoint**.

A common hardening combo: create a **private endpoint** *and* set the resource's
firewall to **deny public network access**, so the only path in is the private IP.

## Azure Bastion: admin access without exposed ports

Opening **RDP (3389)** or **SSH (22)** to the internet — or even assigning VMs
public IPs for jump access — is a classic attack surface. **Azure Bastion**
removes it.

> **Azure Bastion** is a managed PaaS host you deploy into a dedicated
> `AzureBastionSubnet`. From the Azure portal (over **TLS/443**), it brokers **RDP
> and SSH** to your VMs **using their private IPs** — so the VMs need **no public
> IP and no open 3389/22** to the internet.

Why it matters for security:

- Eliminates internet-exposed management ports and the brute-force/port-scan risk
  that comes with them.
- Keeps VMs free of public IPs, shrinking the attack surface.
- Sessions run in the browser; higher SKUs add features like native client
  support, IP-based connection, and session recording.

## Putting it together

To pull PaaS services off the public internet you have two tools. **Service
endpoints** are the lightweight option: the resource keeps its public endpoint but
trusts a specific subnet over the Azure backbone, for free. **Private endpoints
(Private Link)** are the strong option: they give the resource a **private IP** in
your VNet, reachable even from on-premises, scoped to a single resource, and
require **private DNS** to work — pair them with "deny public access" for true
isolation. For administering VMs, **Azure Bastion** brokers RDP/SSH over TLS using
private IPs, so you never expose 3389 or 22 to the internet.

## Exam focus

- **Service endpoint**: resource **keeps its public IP**; you allow a **subnet** on
  the service firewall; traffic stays on the Azure backbone; **free**; scoped to
  the whole service.
- **Private endpoint / Private Link**: puts a **private IP from your VNet** in
  front of a **specific** resource; traffic is fully private and reachable from
  **on-prem/peered** networks. "Take the service off the public internet" ⇒
  private endpoint.
- Private endpoints **require private DNS** (e.g. `privatelink.*` zone) to resolve
  the hostname to the private IP — the most common misconfiguration.
- **Private Link Service** publishes *your own* service for private consumption by
  others.
- **Azure Bastion** gives browser-based **RDP/SSH over 443/TLS** using VMs'
  **private IPs**, so VMs need **no public IP and no open 3389/22**. It deploys
  into a dedicated **`AzureBastionSubnet`**.
