# Threat Intelligence & Threat Hunting

Detection waits for an alert; **intelligence** and **hunting** go looking. This
lesson covers the two halves of proactive defense: consuming threat intelligence
well — knowing what it is, where it comes from, and how far you may share it —
and running hypothesis-driven hunts that find adversaries your tools missed.

## Intelligence vs. the indicators it carries

> An **Indicator of Compromise (IOC)** is forensic *evidence a breach happened* —
> a malicious file hash, a C2 IP, a suspicious domain. An **Indicator of Attack
> (IOA)** describes *behavior in progress* — credential dumping followed by
> lateral movement — regardless of whether any known-bad file is seen.

IOCs are atomic and after-the-fact; IOAs catch intent as it unfolds. A detection
that fires on the *behavioral sequence* before any known-bad file appears is an
IOA.

### The four altitudes of intelligence

Match the intel to the audience:

| Type | Horizon | Audience | Example |
|------|---------|----------|---------|
| **Strategic** | Long-term trends, motivations | Executives, CISO | Multi-year investment guidance |
| **Operational** | A specific, often imminent campaign | SOC leadership | "This ransomware crew targets our sector this month" |
| **Tactical** | Adversary **TTPs** | Hunters, detection engineers | Techniques an actor favors |
| **Technical** | Atomic IOCs | Sensors, SIEM | Hashes, IPs, domains to block |

A CISO asking for long-horizon analysis of adversary trends wants **strategic**
intelligence; a warning about an active campaign against your industry this month
is **operational**.

### Sources and sharing

- **OSINT (Open-Source Intelligence)** enriches an indicator from public sources
  — WHOIS records, certificate transparency logs, public malware repositories.
- **ISACs (Information Sharing and Analysis Centers)** are purpose-built bodies
  for exchanging vetted intel among peers *in the same industry sector*.
- **STIX** and **TAXII** are the standards for machine-readable intel: **STIX**
  *expresses* threat data in a structured format; **TAXII** *transports* it. Pair
  them to automate ingestion of a partner's feed.

> **Traffic Light Protocol (TLP) 2.0** governs how far you may share. From most
> to least restrictive: **TLP:RED** (named recipients only — no further
> disclosure), **TLP:AMBER+STRICT** (your organization only), **TLP:AMBER** (org
> *and its clients*), **TLP:GREEN** (the community), **TLP:CLEAR** (no
> restriction). TLP 2.0 renamed the old **WHITE** to **CLEAR**.

### Judging intelligence quality

Intel is not gospel. Two habits keep you honest:

- **Confidence.** A single, unverified forum post claiming a nation-state hit
  your industry gets **low confidence** — corroborate before you attribute or
  alert leadership. Attribution is a claim you must be able to defend.
- **Timeliness.** An open feed that keeps flagging IP addresses sinkholed months
  ago generates false positives. **Aging** indicators are a quality problem; good
  intel is current.

A **nation-state / advanced persistent threat (APT)** profile shows itself
through months of stealthy **dwell time**, custom malware, and patient espionage
against intellectual property — not smash-and-grab noise.

## Attack frameworks that organize intelligence

**MITRE ATT&CK** is a standardized, real-world catalog of adversary behavior,
organized into **tactics** and **techniques**.

> In ATT&CK, a **tactic** is the adversary's *goal* — the **why** (e.g., the
> fourteen Enterprise tactics such as Reconnaissance, Initial Access,
> Persistence, Privilege Escalation, Credential Access, Lateral Movement,
> Collection, Exfiltration, and Impact). A **technique** is the *method* used to
> achieve that goal — the **how**.

So **Lateral Movement**, **Persistence**, **Exfiltration**, and **Credential
Access** are *tactics*; the specific ways to accomplish them are techniques.

The **Pyramid of Pain** ranks indicator types by how much it *hurts the adversary*
when you detect them. From trivial to replace to very costly: hash values → IP
addresses → domain names → network/host artifacts → tools → **TTPs**. Detecting
**TTPs** is the costliest for an attacker to evade, which is why mature programs
hunt behaviors, not just atomic indicators.

## Threat hunting: assume they're already in

> **Threat hunting** proactively searches for adversaries that have evaded
> existing controls, driven by a specific, testable **hypothesis** rather than by
> waiting for an alert. Its founding premise is **assume-breach** — act as if an
> intruder is already inside.

### Running a good hunt

- **Start with the crown jewels.** With limited time, hunt first on the systems
  holding the organization's most critical data.
- **Build a strong hypothesis.** The best inputs are *recent threat intel on an
  actor's TTPs targeting your sector* and *an unexplained deviation from your
  environment's baseline*. A fresh APT report on techniques used against your
  industry becomes "assume those TTPs are present — hunt for them."
- **Hunt TTPs, not just atoms.** Behaviors are costlier for adversaries to change
  than hashes and IPs, so detections built on TTPs last longer.
- **Correlate weak signals.** A rare parent-child process, a first-seen signed
  binary, and an unusual outbound port each drown you in false positives alone —
  but fire an alert only when they *co-occur on the same host* and the noise
  collapses into signal.
- **Frequency analysis (stacking).** Aggregate one data field across thousands of
  endpoints and investigate its *rarest* values — least-frequency-of-occurrence
  analysis surfaces the odd one out.
- **Proactive timing.** When a critical, actively exploited vulnerability in your
  VPN appliance is disclosed, don't just wait for the patch — hypothesize it may
  already have been exploited and hunt your telemetry for signs of compromise.

### Why hunts pay off even when they find nothing

- **Visibility gaps close.** A hunt that finds no active compromise but reveals a
  lateral-movement technique your tooling could not see produces a new
  **detection/analytic** — a permanent win.
- **Attack surface shrinks.** Discovering forgotten internet-facing servers
  running unused services lets you harden or remove them.
- **Hunts become repeatable.** Documenting the hypothesis, data sources, queries,
  and outcome makes a hunt *measurable* and lets a successful one be **automated
  into a standing detection**. A good trick to visualize coverage is a **MITRE
  ATT&CK Navigator heatmap** of which techniques you can currently detect — and
  where the blind spots are.

## Exam focus

- **IOC** = evidence a breach happened (hash/IP/domain); **IOA** = adversary
  behavior/intent in progress. A behavioral-sequence detection is an IOA.
- Intel altitudes: **strategic** (trends/motivations, executives), **operational**
  (a specific campaign), **tactical** (TTPs), **technical** (atomic IOCs).
- **OSINT** = public sources; **ISAC** = sector-based sharing; **STIX** expresses
  and **TAXII** transports machine-readable intel.
- **TLP 2.0:** RED (named recipients only) → AMBER+STRICT (own org) → AMBER (org +
  clients) → GREEN (community) → **CLEAR** (no limit; formerly WHITE).
- Weight unverified intel at **low confidence** and corroborate; **aging/sinkholed**
  indicators cause false positives. **APT** = long dwell time, custom malware,
  espionage.
- **ATT&CK:** tactic = goal/**why**; technique = method/**how**. Lateral Movement,
  Persistence, Exfiltration, Credential Access are **tactics**.
- **Pyramid of Pain:** detecting **TTPs** hurts the adversary most; hashes least.
- Hunting is **hypothesis-driven** and **assume-breach**; start at the **crown
  jewels**, hunt **TTPs**, **correlate** co-occurring weak signals, use
  **frequency analysis**, and **document hunts** so they automate into detections.
