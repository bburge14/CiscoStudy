# Threat Actors, Vectors & Social Engineering

Defense makes more sense when you know who's coming, why, and how they get in the
door. This lesson covers the *attackers* (threat actors), the *routes* they use
(threat vectors and attack surfaces), and the oldest trick of all — fooling a
human (social engineering).

## Threat actors: who is attacking you

A **threat actor** is anyone or any group that may cause harm. They differ wildly
in skill, resources, and motive, and the exam wants you to match an actor to a
scenario.

| Actor | Who they are | Typical motivation |
|-------|-------------|--------------------|
| **Nation-state** | Government-backed, highly skilled, well funded | Espionage, war, disruption |
| **Organized crime** | Professional criminal groups | Financial gain |
| **Hacktivist** | Ideologically driven | Philosophical/political beliefs |
| **Insider threat** | An employee or contractor | Revenge, financial gain, or accident |
| **Unskilled attacker** | "Script kiddie" using others' tools | Chaos, thrill, reputation |
| **Shadow IT** | Staff using unsanctioned tech | Convenience (not malice, but risky) |

### Attributes that tell actors apart

When a question describes an attacker, look for these **attributes**:

- **Internal vs. external** — inside the organization or outside it.
- **Resources / funding** — a lone amateur vs. a government budget.
- **Level of sophistication / capability** — off-the-shelf tools vs. custom
  zero-days.

> **Nation-state** actors sit at the top for resources and sophistication and
> often run slow, stealthy **Advanced Persistent Threats (APTs)**. **Unskilled
> attackers** sit at the bottom, borrowing tools they don't fully understand.

### Why they do it (motivations)

Motivations the exam lists include **data exfiltration**, **espionage**,
**service disruption**, **blackmail**, **financial gain**, **philosophical or
political beliefs**, **ethical** (e.g. a researcher), **revenge**, **disruption/
chaos**, and **war**. Tie the motive to the actor: hacktivist → beliefs, organized
crime → money, nation-state → espionage or war, disgruntled insider → revenge.

A special note on **shadow IT**: that's employees standing up their own
cloud apps or devices without approval. There's usually no malice, but it creates
unmanaged, unmonitored attack surface — a risk precisely *because* security can't
see it.

## Threat vectors and attack surfaces: how they get in

A **threat vector** (or attack vector) is the *path* an attacker uses. The
**attack surface** is the sum of all those possible paths. Shrinking the attack
surface — closing doors you don't need — is a core defensive goal.

Common vectors:

- **Message-based** — **email**, **SMS** (text), and **IM** (instant messaging).
  Email is the single most common vector, usually via phishing.
- **Image-based** and **file-based** — malware hidden in images or document/
  executable files.
- **Voice call** — phone-based scams (vishing).
- **Removable device** — a dropped USB stick someone plugs in.
- **Vulnerable software** — think **client-based** (an installed agent with a
  flaw) vs **agentless** (nothing installed, but still exposed).
- **Unsupported systems and applications** — end-of-life software that no longer
  gets patches is a standing invitation.
- **Unsecure networks** — **wireless**, **wired**, and **Bluetooth** connections
  without proper protection.
- **Open service ports** — every listening port is a potential door.
- **Default credentials** — the factory `admin/admin` nobody changed.
- **Supply chain** — attackers compromise a trusted **MSP**, **vendor**, or
  **supplier** to reach *you* through a door you already trust.

## Social engineering: hacking the human

The easiest system to break is often the person using it. **Social engineering**
manipulates people into giving up information or access. Know these by name:

- **Phishing** — fraudulent email trying to trick you into clicking, logging in,
  or paying. The umbrella term for the whole family.
- **Vishing** — *voice* phishing, over the phone.
- **Smishing** — phishing over *SMS* text messages.
- **Spear phishing** — phishing aimed at a *specific* person or group (not on the
  official objectives word-for-word, but the targeting idea matters).
- **Business Email Compromise (BEC)** — an attacker uses (or spoofs) a real
  executive's email to order a fraudulent wire transfer or data release.
- **Pretexting** — inventing a believable backstory ("I'm from IT, there's a
  problem with your account...") to justify the request.
- **Impersonation** — pretending to be someone else, like a vendor or help-desk
  agent.
- **Watering hole** — compromising a legitimate site the target group is known to
  visit, so the victims infect themselves.
- **Brand impersonation** — faking a trusted company's look and feel.
- **Typosquatting** — registering `micros0ft.com` or `gooogle.com` to catch
  mistyped URLs.
- **Misinformation / disinformation** — spreading false content to mislead, cause
  chaos, or manipulate opinion.

> Almost every social-engineering trick leans on a human lever: **urgency**
> ("do it now!"), **authority** ("this is the CEO"), **trust** ("it's your bank"),
> **fear**, or **scarcity**. Spot the lever and you'll spot the scam.

### A quick worked example

> An employee gets a call: "Hi, this is Dana from the service desk. We're seeing
> failed logins on your account and need to reset it — can you confirm your
> current password so we can verify it's really you?"
>
> - It's over the phone → **vishing**.
> - "Dana from the service desk" is a fabricated role → **pretexting** and
>   **impersonation**.
> - The lever is **authority + urgency**.
> - The right response: never give a password; hang up and call IT back on a
>   known-good number.

## The whole thing in one paragraph

**Threat actors** range from well-funded, sophisticated **nation-states** and
profit-driven **organized crime** down to **unskilled attackers**, plus
belief-driven **hacktivists**, risky **insiders**, and unmanaged **shadow IT** —
and you tell them apart by **internal/external**, **resources**, and
**sophistication**, matched to motives like espionage, financial gain, revenge or
chaos. They reach you through **threat vectors** (email/SMS/IM messages, images
and files, voice calls, removable devices, vulnerable or unsupported software,
unsecure wireless/wired/Bluetooth networks, open ports, default credentials, and
the supply chain) — the full set being your **attack surface**. And the most
reliable vector is **social engineering**: phishing and its cousins (vishing,
smishing), BEC, pretexting, impersonation, watering-hole, brand impersonation,
typosquatting, and misinformation — all pulling on human levers of urgency,
authority, trust and fear.

## On the exam

- Match actor to motive fast: **hacktivist → political beliefs**, **organized
  crime → money**, **nation-state → espionage/war** (and APTs), **insider →
  revenge or mistakes**, **unskilled → chaos/thrill**.
- **Shadow IT** is risky because it's *unsanctioned and unmonitored*, not because
  it's malicious — watch for that nuance.
- Channel decides the "-ishing" term: **email = phishing**, **phone/voice =
  vishing**, **SMS = smishing**.
- **BEC** specifically involves a (spoofed or hijacked) executive/business email
  driving a fraudulent transaction. **Pretexting** is the invented story;
  **impersonation** is pretending to be someone.
- **Watering hole** = compromise a site the victims *already* trust and visit.
  **Typosquatting** = lookalike/misspelled domains.
- "Reducing the attack surface" means closing unused ports, retiring unsupported
  software, and changing default credentials — don't overthink it.
