# Security Methodologies: Shared Responsibility, Defense in Depth & Zero Trust

Before you can name a single Microsoft product, you have to speak the language of
modern security. This lesson covers three ideas that show up again and again on
SC-900 and in the real world: the **shared responsibility model** (who secures
what in the cloud), **defense in depth** (layer your protection), and **Zero
Trust** (stop trusting things just because they are "inside"). Underneath all of
them sits the oldest idea in the field — the **CIA triad** — so we start there.

## The CIA triad: what we are protecting

Every security control exists to defend one of three properties of information.

> **Confidentiality** means only authorized people can read the data.
> **Integrity** means the data is accurate and has not been tampered with.
> **Availability** means the data and systems are there when authorized users
> need them.

- **Confidentiality** is protected by things like encryption and access control.
  A leaked customer list is a confidentiality failure.
- **Integrity** is protected by things like hashing and digital signatures. A
  bank balance silently changed by an attacker is an integrity failure.
- **Availability** is protected by backups, redundancy and DDoS protection. A
  ransomware attack that locks every file is an availability failure.

Think of the triad as a three-legged stool: weaken any one leg and the whole
thing tips over.

## The shared responsibility model

When you run everything in your own data center, security is entirely your job.
Move to the cloud and some of that work shifts to the provider — but **not all of
it**. The shared responsibility model draws the line between what Microsoft
secures and what you, the customer, still own.

The line moves depending on the service model:

| Responsibility | On-premises | IaaS | PaaS | SaaS |
|----------------|-------------|------|------|------|
| Physical datacenter, hosts, network | You | **Microsoft** | **Microsoft** | **Microsoft** |
| Operating system | You | You | Microsoft | Microsoft |
| Network / application controls | You | Shared | Shared | Microsoft |
| Identity & directory infrastructure | You | Shared | Shared | Shared |
| **Accounts, identities, data, devices** | **You** | **You** | **You** | **You** |

The pattern to memorize: the more the provider manages (SaaS being the most),
the less you manage. But look at the bottom row.

> No matter which cloud model you choose — IaaS, PaaS or SaaS — **you always
> remain responsible for your data, your accounts and identities, and the
> devices** that connect. The provider never owns those.

Why does this matter? Because the single most common cause of a cloud breach is a
customer misconfiguring something they owned all along — a public storage
container, a weak password, an over-permissioned account. The cloud provider
secures the building; you still have to lock your own apartment.

## Defense in depth

No single wall stops every attacker, so good security uses **many** layers. If
one fails, the next still protects the asset. This is **defense in depth**, and
the exam likes to picture it as a stack of rings around the data.

A common way to list the layers, from outside to inside:

- **Physical security** — locks, guards, badge readers on the datacenter.
- **Identity and access** — authentication, MFA, Conditional Access.
- **Perimeter** — DDoS protection and edge firewalls against volume attacks.
- **Network** — segmentation so a breach in one segment cannot spread.
- **Compute** — hardened, patched servers and endpoints.
- **Application** — secure code and protection against app-layer attacks.
- **Data** — encryption and access control on the information itself.

> Defense in depth assumes any one control **can and will fail**. By stacking
> independent layers, you make the attacker defeat all of them in sequence, not
> just one.

The analogy is a medieval castle: a moat, then walls, then a gate, then guards,
then a locked keep. An attacker who swims the moat still faces the walls.

## Zero Trust

The old network model trusted anything on the corporate LAN — once you were
"inside," you roamed freely. Remote work, cloud apps and mobile devices shattered
that assumption. **Zero Trust** replaces "trust the network" with "trust
nothing by default; verify everything."

Zero Trust rests on three guiding principles:

> - **Verify explicitly** — always authenticate and authorize using all
>   available signals (identity, device health, location, the resource).
> - **Use least privilege access** — give each identity only the access it needs,
>   just in time and just enough, so a compromise reaches less.
> - **Assume breach** — design as if an attacker is already inside. Segment
>   access, encrypt everything, and minimize the **blast radius** of any single
>   compromise.

Zero Trust is applied across six technology "pillars": **identities, devices,
applications, data, infrastructure, and networks**. Each pillar is a place to
verify explicitly and enforce least privilege. Notice how neatly this pairs with
defense in depth — Zero Trust tells you *how* to treat each layer, and "assume
breach" is why we still bother layering.

### How it connects to the rest of SC-900

- "Verify explicitly" is exactly what **Conditional Access** does in Microsoft
  Entra (covered later): check signals, then allow, block or challenge.
- "Least privilege" is why tools like **Privileged Identity Management** hand out
  admin rights only for a limited time.
- "Assume breach" is why **Microsoft Defender XDR** and **Microsoft Sentinel**
  watch for attackers who are already past the front door.

## The whole thing in one paragraph

Security protects the **confidentiality, integrity and availability** of
information. In the cloud, the **shared responsibility model** splits the work
with the provider — more is theirs as you move from IaaS toward SaaS, but your
**data, identities, accounts and devices are always yours to secure**. **Defense
in depth** layers independent controls (physical, identity, perimeter, network,
compute, application, data) so one failure is not fatal. And **Zero Trust**
throws out implicit network trust in favor of three rules — **verify explicitly,
use least privilege, assume breach** — applied across identities, devices, apps,
data, infrastructure and networks.

## Exam focus

- **CIA triad:** confidentiality (only authorized can read), integrity (data is
  accurate/untampered), availability (accessible when needed).
- **Shared responsibility:** the provider's share grows from IaaS → PaaS → SaaS,
  but **you always keep responsibility for data, identities/accounts, and
  devices.** If a question asks what is "always" the customer's job, that is it.
- **Defense in depth** = **multiple layers** of defense; if one fails the others
  still protect the asset. Know the layer stack: physical, identity, perimeter,
  network, compute, application, data.
- **Zero Trust = three principles:** **verify explicitly, use least privilege
  access, assume breach.** "Assume breach" is about limiting blast radius through
  segmentation and encryption.
- Zero Trust is not a product — it is a strategy applied across the six pillars:
  **identities, devices, applications, data, infrastructure, networks.**
