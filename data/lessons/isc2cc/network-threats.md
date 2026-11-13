# Network Threats & Attacks

To defend a network, you first have to recognize what's coming at it. This lesson
catalogs the **malware** and **attacks** the CC exam expects you to identify by
description. The exam almost never asks you to *perform* an attack — it gives you a
scenario and asks you to **name** it. So focus on the defining characteristic of
each one.

## Malware: malicious software

**Malware** is any software written to harm or exploit a system. The main types
differ in *how they spread* and *what they do*.

### Virus

> A **virus** attaches itself to a legitimate program or file and runs only when
> the user opens that host file, then spreads to other files.

The key traits: it needs a **host file** and needs a **user to run it**. No user
action, no execution. Think of it like a biological virus that needs a cell to
infect.

### Worm

> A **worm** spreads by itself from computer to computer across a network, needing
> **no host file and no user action**.

The giveaway is **self-propagation**. A worm can race across an entire network on
its own, which is why worms cause such fast, widespread outbreaks. Virus vs. worm
is a favorite distinction: *virus needs a user to open a host file; worm spreads
on its own.*

### Trojan horse

> A **Trojan horse** disguises itself as something harmless or useful, but when
> the user installs and runs it, it secretly does something malicious — often
> opening a **backdoor** for an attacker.

A "free game" that quietly gives an attacker remote access is a Trojan. The trick
is **deception**: the user runs it willingly because it looks legitimate.

### Ransomware

> **Ransomware** encrypts the victim's files and demands payment (usually in
> cryptocurrency) in exchange for the decryption key.

When a hospital's files are suddenly locked and a message demands money to unlock
them, that's ransomware. It directly attacks **availability**.

### Spyware

> **Spyware** secretly gathers information — recording keystrokes, browsing
> habits, or credentials — and sends it to an attacker, often without obviously
> harming the system.

Spyware is about **stealth and surveillance**. A keylogger that quietly captures
what you type is spyware.

## Attacks against networks and systems

Beyond planting malware, attackers use a range of techniques.

### Denial-of-service and DDoS

> A **denial-of-service (DoS)** attack floods a system with traffic or requests
> until it can no longer serve legitimate users. A **distributed** denial-of-
> service (**DDoS**) does this from **many** compromised machines at once.

In a DDoS, an attacker directs thousands of compromised devices — a **botnet** —
to overwhelm a web server until real customers can't connect. The target of a DoS
is **availability**.

### Man-in-the-middle (on-path)

> A **man-in-the-middle (MITM)**, now often called an **on-path** attack, secretly
> positions the attacker *between* two parties, letting them read and relay (and
> possibly alter) the traffic without either side knowing.

Unsecured public Wi-Fi is a classic setting: the attacker sits between the user
and their bank, silently intercepting the conversation. Encryption (HTTPS/TLS,
VPNs) is the main defense.

### Password and brute-force attacks

> A **brute-force attack** rapidly tries huge numbers of password combinations
> against a login until it finds one that works.

Strong, long passwords; account lockouts after failed attempts; and MFA are the
standard defenses. (Related attacks include dictionary attacks, which try common
words, and credential stuffing, which reuses leaked passwords.)

### Social engineering and phishing

Many attacks target *people* rather than technology.

> **Social engineering** manipulates people into revealing information or taking
> an action, exploiting trust, authority, urgency, or fear.

- **Phishing** — a deceptive **email** that appears to come from a trusted source
  (like "IT") and urges the recipient to click a link or "verify" their
  credentials. Phishing is sent broadly to many people.
- **Spear phishing** — a **targeted** version aimed at a specific person, using
  personalized details (a real project name, a real manager's name) to seem
  convincing. The narrower and more tailored the lure, the more it leans toward
  spear phishing.

A phone call from someone pretending to be a trusted executive, using urgency and
authority to pressure an employee, is social engineering too. (The security-
awareness lesson covers more techniques like pretexting, baiting, and shoulder
surfing.)

### Insider threat

> An **insider threat** is a trusted person with **legitimate** access who misuses
> it — maliciously or accidentally — to harm the organization.

An employee who deliberately copies confidential customer data to sell to a
competitor is a malicious insider. Insiders are dangerous precisely because they
already have access, so least privilege, monitoring, and separation of duties are
key defenses.

## How to approach these on the exam

Read the scenario and latch onto the *defining* behavior:

- Spreads by itself, no user needed → **worm**.
- Needs the user to open an infected file → **virus**.
- Looks legitimate, hides a backdoor → **Trojan**.
- Encrypts files for ransom → **ransomware**.
- Floods a server from many machines → **DDoS**.
- Secretly sits between two parties → **man-in-the-middle / on-path**.
- Targets one specific person with a tailored message → **spear phishing**.
- Trusted employee abusing access → **insider threat**.

## Exam focus

- **Virus** needs a host file and a user to run it; a **worm** self-propagates
  with no user action. This distinction is tested constantly.
- **Trojan** = disguised malware that opens a backdoor; **ransomware** = encrypts
  files for payment; **spyware** = secretly records and exfiltrates activity.
- **DoS/DDoS** attacks **availability** by flooding; a DDoS uses many compromised
  machines (a **botnet**).
- **Man-in-the-middle / on-path** = attacker secretly intercepts traffic between
  two parties (common on open Wi-Fi).
- **Brute-force** = trying many passwords until one works.
- **Phishing** = broad deceptive email; **spear phishing** = targeted and
  personalized. Both are **social engineering**.
- An **insider threat** is a trusted user with legitimate access who misuses it.
