# Social Engineering

Most of this track attacks machines. Social engineering attacks *people* — and it
remains one of the most successful intrusion methods precisely because no patch
fixes human psychology. For the exam you need to name the technique from a
scenario and pair it with the defense. The theme throughout: the strongest
technical controls can be undone by one person who was convinced to help.

## What social engineering is

> **Social engineering is manipulating people into divulging information or
> performing actions that compromise security.** It targets human trust rather
> than technical flaws.

It works by pulling psychological levers: **authority** ("I'm from IT"),
**urgency** ("do this now or the account locks"), **fear**, **scarcity**,
**trust**, and **reciprocity**. A typical attack follows a shape — research the
target, build a plausible hook, exploit the person, then exit cleanly.

## The techniques, by name

### Message-based attacks

- **Phishing** — a fraudulent email (or message) that lures the victim to a
  lookalike site or malicious attachment. The classic example: an email "from IT"
  urging you to click a link and "verify" your password on a fake site.
- **Spear phishing** — phishing *tailored* to a specific person or group using
  researched detail.
- **Whaling** — spear phishing aimed at **executives** ("big fish").
- **Smishing** — phishing over **SMS** text messages.
- **Vishing** — phishing over **voice/phone**.
- **Business Email Compromise (BEC)** — impersonating an executive or vendor to
  trick staff into wiring money or sending data.

### Pretext and bait

- **Pretexting** — inventing a believable scenario to justify the request. Often
  combined with vishing: an attacker **phones the help desk posing as a senior
  executive** and invents an urgent story to pressure staff into resetting an
  account — that is **vishing with pretexting**.
- **Baiting** — leaving tempting bait (a malware-laden USB drive, a "free"
  download) for a curious victim to take.
- **Quid pro quo** — offering a service or benefit in exchange for information or
  access.

### Physical and in-person

- **Tailgating / piggybacking** — following an authorized person through a secure
  door.
- **Dumpster diving** — recovering sensitive material from the trash.
- **Shoulder surfing** — reading screens or keypads over someone's shoulder.
- **Impersonation** — pretending to be staff, a vendor, or a delivery person.

### Web-based lures

- **Watering hole** — compromising a legitimate site the target group is known to
  visit, so the victims come to the malware.
- **Pharming** — redirecting victims from a real site to a fake one via DNS
  tampering.

> The **insider threat** is social engineering's cousin: a person who already has
> legitimate access and misuses it, whether maliciously or by being manipulated.

## Why it is so effective

People are helpful, busy, and trusting by default. An attacker who sounds
authoritative and creates urgency can short-circuit careful thinking. Technology
can filter *some* of this, but the final decision — to click, to tell, to hold the
door — is human. That is why defense is a blend of training and technical backstops.

## Defending against social engineering

- **Security awareness training** — the primary control; teach people the patterns
  above and how to pause and verify.
- **Simulated phishing campaigns** — measure and reinforce that training.
- **Verification procedures** — call back on a known-good number before acting on
  unusual requests (especially money or password resets).
- **Multi-factor authentication** — so a phished password alone is not enough.
- **Email authentication — SPF, DKIM, DMARC** — reduces spoofed sender addresses.
- **Email and web filtering** — blocks many lures before they arrive.
- **Least privilege** — limits what a manipulated account can do.
- **A clear, blame-free reporting path** — so victims report fast instead of hiding
  mistakes.
- **Physical controls** — badges and **access control vestibules (mantraps)**
  specifically counter **tailgating**.

## Reading the red flags

Because the final decision is human, teaching people to pause on the tell-tale signs
is the highest-leverage defense. The common red flags in a phishing message:

- An **urgent or threatening tone** ("your account closes in 24 hours").
- A **mismatch between the display name and the real sender address**, or a
  lookalike domain (character swaps, extra words).
- **Generic greetings** and unexpected attachments or links.
- A request to **bypass normal process** — to pay, reset, or share a credential
  "just this once."
- **Hovered links** that point somewhere other than they claim.

The instinct to build is simple: when a message creates pressure to act fast and
break a rule, slow down and verify through a separate, known-good channel.

## Measuring and reducing human risk

Mature programs do not just lecture — they **run simulated phishing campaigns**,
track click rates over time, and give fast, blame-free feedback. The goal is a
culture where reporting a suspicious message is routine and a near-miss is treated
as useful data rather than a reason to hide.

## Exam focus

- Match the vector: **phishing** = fraudulent email to a lookalike site;
  **whaling** = executives; **smishing** = SMS; **vishing** = voice/phone.
- **Vishing with pretexting** = a phone call plus an invented urgent story (e.g.
  impersonating an executive to the help desk).
- **Tailgating/piggybacking** is countered by an **access control vestibule**;
  **shoulder surfing** by screen privacy and awareness.
- **Baiting** uses tempting bait (malicious USB); **quid pro quo** trades a favor
  for access; **watering hole** compromises a site the target visits.
- The **primary defense is security awareness training**, backed by **MFA**,
  **verification callbacks**, and **SPF/DKIM/DMARC**.
