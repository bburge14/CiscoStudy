# Attack Surface & Detection Methods

To defend a system you first map where it can be attacked, then you choose *how*
you will notice an attack. This lesson pairs those two ideas: the **attack
surface** (and the **vectors** that reach it) and the **detection methods** a
sensor uses to raise an alert. Each detection method has a blind spot, and
knowing those blind spots is what separates an analyst who trusts their tools
blindly from one who knows when to look harder.

## Attack surface and attack vectors

A single vulnerability is one weakness. Step back and look at *everything* an
attacker could poke at, and you are looking at the attack surface.

> The **attack surface** is the sum of all the points — network services, open
> ports, applications, APIs, user accounts, devices, even people — where an
> attacker could try to enter a system or extract data. An **attack vector** is
> the specific path or method an attacker uses to reach it.

The distinction the exam cares about: an attack surface is the *whole set* of
exposure points, not any one flaw. Reducing the attack surface — closing unused
ports, uninstalling unneeded software, disabling dormant accounts, segmenting
the network — is one of the most effective defenses precisely because it removes
opportunities wholesale rather than patching them one at a time.

Common **attack vectors** you should recognize:

- **Email** — phishing messages with malicious links or attachments; the single
  most common initial vector.
- **Web / drive-by** — a compromised or malicious website delivering an exploit.
- **Removable media** — a USB drive carrying malware across an air gap.
- **Supply chain** — malicious code slipped into trusted software or hardware.
- **Direct network access** — exposed services on open ports, weak remote
  access, wireless.
- **Social engineering** — manipulating a person rather than a machine (phone,
  pretext, impersonation).

A memory hook: the **surface** is the castle wall's entire length; a **vector**
is the particular gate or tunnel the attacker chooses.

### Common attacks that reach the surface

Vectors deliver attacks, so it helps to recognize the attacks themselves:

- **Man-in-the-middle (on-path)** — the attacker secretly relays, and may alter,
  traffic between two parties who believe they talk directly.
- **ARP spoofing (ARP poisoning)** — forged ARP replies map the attacker's MAC
  to a victim IP (often the gateway), redirecting local traffic to the attacker;
  a common way to *become* the man in the middle on a LAN.
- **DoS vs. DDoS** — a denial-of-service floods a target to exhaust it; a
  **distributed** DoS sends that flood from thousands of botnet hosts at once,
  making it far harder to block by source. These attack **availability**.
- **Buffer overflow** — input written past the end of a fixed-size buffer
  overwrites adjacent memory and can hijack a program's execution flow.
- **Ransomware** — malware that encrypts a victim's files and demands payment;
  it most directly attacks **availability**.

## How sensors detect: the main methods

A detection engine — an IDS/IPS, antivirus, or SIEM rule — decides *this is
suspicious* using one of a few approaches. Each has a characteristic strength
and a characteristic weakness.

> **Signature / rule-based detection** matches traffic or files against a
> database of **known-bad** patterns. **Anomaly / behavioral detection** builds a
> baseline of **normal** and alerts on deviations from it.

### Signature-based (rule-based) detection

The engine holds a library of signatures — byte patterns, rule conditions,
known malicious hashes — and raises an alert when incoming data **matches** one.

- **Strength:** very accurate and low-noise for *known* threats. If a packet
  matches the signature for a specific exploit, you can be confident what it is.
- **Weakness:** it is blind to anything with no signature yet. A brand-new or
  modified attack — a **zero-day**, or malware whose bytes were tweaked — sails
  right past. Signatures must be constantly updated, and they always lag the
  newest threats.

This is the exam's favorite point: **signature detection cannot catch unknown
attacks that have no existing signature.**

### Anomaly / behavioral detection

The engine first learns a **baseline** of normal behavior — typical traffic
volumes, usual ports, normal login times — then flags activity that departs from
it.

- **Strength:** can catch *novel* attacks and insider misuse that no signature
  describes, because it keys on "this isn't normal" rather than "this matches a
  known bad thing."
- **Weakness:** more prone to **false positives** — legitimate-but-unusual
  activity (a big quarter-end data transfer) looks anomalous. The baseline must
  be built carefully and kept current, or the alerts become noise.

### Other approaches you may meet

- **Statistical** detection is a form of anomaly detection using thresholds and
  rates — for example, raising an alert when traffic volume runs several
  standard deviations above the computed mean for that hour.
- **Heuristic** detection flags a never-before-seen file because it *exhibits
  traits* common to malware (packing, self-modifying code, suspicious API calls)
  rather than matching a specific signature.
- **Reputation-based** detection blocks or flags based on the known reputation of
  an IP, domain, URL, or file hash drawn from threat intelligence.

## The trade-off, and why SOCs blend methods

No single method is enough, so real sensors **combine** them. Signatures give
precise, low-noise coverage of the known; anomaly detection provides a chance at
the unknown; reputation feeds add context. The analyst's job is to understand
*why* an alert fired so they can judge it: a signature hit says "this looks
exactly like known exploit X," while an anomaly alert says "this is unusual —
investigate whether it's benign." Treating those two the same way is a mistake;
the first is often high-confidence, the second often needs human validation.

That blend is also why **tuning** matters. A signature set that is too broad
floods analysts with false positives; an anomaly baseline that is stale does the
same. Good detection is not "turn everything on" — it is choosing methods whose
blind spots don't overlap and tuning them to the environment.

## Exam focus

- **Attack surface** = the *sum of all* points an attacker could use to get in or
  get data out — distinct from a single vulnerability. Shrinking it (closing
  ports, removing software, disabling accounts, segmentation) is a core defense.
- An **attack vector** is the specific path used (email/phishing, web, removable
  media, supply chain, social engineering). Email is the most common initial
  vector.
- **Signature/rule-based** detection matches **known-bad** patterns: accurate for
  known threats but **cannot detect new/unknown attacks (zero-days)** with no
  signature, and needs constant updates.
- **Anomaly/behavioral** detection baselines **normal** and alerts on deviation:
  can catch novel attacks but produces **more false positives**.
- Real sensors **blend** signature, anomaly, statistical, and reputation methods;
  know *why* an alert fired to judge how much to trust it.
