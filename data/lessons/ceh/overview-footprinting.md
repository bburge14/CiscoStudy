# Ethical Hacking Overview & Footprinting

Before you touch a single tool, you have to understand *why* an ethical hacker
exists and *what makes the work legal*. An ethical hacker uses the same knowledge
as an attacker, but under a signed agreement, inside an agreed scope, and with the
goal of getting flaws fixed. That one difference — authorization — is what
separates a professional engagement from a crime. This lesson sets that framing,
then starts the first real phase of an assessment: footprinting.

## What ethical hacking actually is

> **Ethical hacking is the authorized practice of probing systems for weaknesses
> the way an attacker would, so the owner can fix them before a real attacker finds
> them. The defining word is *authorized*.**

Everything in the CEH world ultimately protects the **CIA triad** —
**Confidentiality, Integrity, Availability**. An attack is any action that breaks
one of those three. "Hack value" is simply how interesting a target is to an
attacker; your job is to think about value the way they do so you can defend it.

### Who the players are

The exam expects you to label attackers by intent and authorization:

- **White hat** — an authorized professional (an ethical hacker) working under
  contract to improve security.
- **Black hat** — a malicious attacker acting illegally for personal gain or harm.
- **Gray hat** — someone who acts without authorization but usually without clear
  malicious intent; still illegal.
- **Script kiddie** — an unskilled person running others' tools.
- **Hacktivist** — attacks to promote a political or social cause.
- **State-sponsored / APT** — well-funded groups working for a nation-state.
- **Suicide hacker** — aims to cause damage without caring about getting caught.
- **Insider** — a threat from someone who already has legitimate access.

## The five phases of an attack

CEH frames an engagement as a repeatable methodology. Memorize the order.

| Phase | What happens |
|-------|--------------|
| **1. Reconnaissance** | Gather information about the target — *this comes first* |
| **2. Scanning** | Probe live hosts, ports and services |
| **3. Gaining Access** | Exploit a weakness to get a foothold |
| **4. Maintaining Access** | Keep the foothold (backdoors, persistence) |
| **5. Clearing Tracks** | Hide evidence of the activity |

Reconnaissance is always phase one — you cannot attack what you have not found.
You will also meet industry models that describe the same idea: the **Cyber Kill
Chain** (Lockheed Martin's seven stages) and **MITRE ATT&CK** (a knowledge base of
real-world tactics and techniques). Know them by name and purpose.

### What keeps it legal

An engagement is defined by paperwork, not good intentions:

- **Scope** — exactly which systems, addresses and times are in bounds.
- **Rules of Engagement (RoE)** — what techniques are permitted.
- **Written authorization** — signed permission from someone who owns the asset;
  without it the same actions are criminal.
- **Non-disclosure agreement (NDA)** — protects what you learn.

> If a question describes someone testing systems they were *hired under a signed
> contract* to assess and *reporting findings to be fixed*, the answer is a **white
> hat / ethical hacker** — authorization is the tell.

## Footprinting: reconnaissance in detail

**Footprinting** (also called reconnaissance) is collecting information about a
target. It splits into two modes, and the distinction is heavily tested.

> **Passive footprinting** gathers information *without* sending traffic to the
> target's own systems (using third-party and public sources). **Active
> footprinting** interacts directly with the target, which can be logged.

### Passive techniques and tools

- **WHOIS** — queries registrar records for a domain: registrant, creation and
  expiry dates, and authoritative name servers. It queries the registry, not the
  target's hosts, so it is passive.
- **DNS interrogation** — `nslookup` and `dig` reveal name-to-IP mappings, mail
  servers (MX) and more. A misconfigured server may allow a **DNS zone transfer
  (AXFR)** that dumps every record at once.
- **theHarvester** — collects email addresses, employee names and subdomains for a
  domain by querying public search engines and data sources.
- **Maltego** — a link-analysis / OSINT tool that maps relationships between
  people, domains, infrastructure and more on a visual graph.
- **Shodan** — a search engine for Internet-connected devices; it indexes exposed
  services, banners and cameras without you touching the target.
- **Google dorking** — using advanced search operators to find exposed files and
  pages that were never meant to be public.
- **Recon-ng** — a framework that organizes OSINT gathering into modules.
- **Social media and job postings** — reveal names, roles and the exact
  technologies a company runs.

Active footprinting edges toward scanning: things like website mirroring, email
header tracking and banner grabbing that actually contact the target.

### Defending against footprinting

You cannot stop OSINT entirely, but you can shrink your exposure:

- Register domains with **WHOIS privacy / redaction**.
- **Disable DNS zone transfers** to untrusted hosts and segment internal DNS.
- Publish only what is necessary; review websites and metadata for leaked detail.
- Train staff on what *not* to post about internal systems.
- Monitor for your assets appearing in services like Shodan.

## Exam focus

- **Authorization** is what makes hacking ethical; a signed contract plus a report
  of fixable findings points to a **white hat / ethical hacker**.
- Know the attacker labels, especially **gray hat** (unauthorized but not clearly
  malicious — still illegal) and **hacktivist** (cause-driven).
- The five phases in order: **Reconnaissance → Scanning → Gaining Access →
  Maintaining Access → Clearing Tracks.** Reconnaissance is first.
- **Passive vs active** footprinting hinges on whether you *touch the target*.
  WHOIS, Shodan, theHarvester, Maltego and Google dorking are passive/OSINT.
- **WHOIS** = registrar/domain data; **theHarvester** = emails, names, subdomains;
  **Shodan** = exposed Internet devices; **Maltego** = relationship mapping.
- A **DNS zone transfer (AXFR)** that succeeds against a public server is a classic
  footprinting win — disable it as the defense.
