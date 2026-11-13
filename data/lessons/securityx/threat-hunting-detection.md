# Threat Hunting, Intelligence & Detection Engineering

Security operations at the expert level is proactive. Instead of waiting for an
alert, mature teams **hunt** for adversaries that have evaded existing detections,
feed what they find back into **engineered detections**, and drive the whole cycle
with **threat intelligence**. This lesson covers hunting, the intelligence that
guides it, and the monitoring/detection platforms that make it possible.

## Threat hunting: assume breach, go looking

**Threat hunting** is the proactive, hypothesis-driven search for adversaries
already inside the environment who have slipped past automated alerting. It starts
not from an alert but from an **idea**:

> A hunt begins with a **hypothesis** — "if an attacker is using
> living-off-the-land techniques, I should see unusual PowerShell spawning from
> Office processes." The analyst then queries telemetry to prove or disprove it.

Hunts are informed by intelligence and frameworks, scoped by hypothesis, and their
findings become new detections. A hunt that finds nothing still produces value: it
validates coverage and refines the hypothesis.

### IOCs vs behaviors, and the Pyramid of Pain

Two analysts can hunt the same threat very differently:

- Searching for a **specific known-malicious file hash or C2 IP address** is
  hunting on **Indicators of Compromise (IOCs)** — precise but brittle, because
  attackers trivially change a hash or rotate an IP.
- Searching for **behavior** — "a process spawning a command shell that then makes
  an outbound connection" — hunts on **TTPs (Tactics, Techniques, and Procedures)**.
  Behavior is far harder for an attacker to change, so behavioral detection is more
  durable.

This is the **Pyramid of Pain**: hashes and IPs are cheap for attackers to change
(low pain); TTPs are expensive (high pain). Mature detection climbs the pyramid
toward behavior.

> IOC-based hunting (hash/IP) is precise but easily evaded; **TTP/behavior-based**
> hunting is durable because changing *how* they operate costs the adversary far
> more. Prefer behavior.

## Threat intelligence: knowing the adversary

**Cyber Threat Intelligence (CTI)** is evidence-based knowledge about threats that
informs decisions. It comes in tiers:

- **Strategic** — high-level trends and risk for leadership (who targets our
  sector, why).
- **Operational** — campaigns and adversary intent/capability.
- **Tactical** — the TTPs and IOCs analysts use day to day.

Sources include **OSINT**, commercial feeds, **ISACs** (industry sharing), and
internal telemetry. Intelligence is shared in standardized formats — **STIX**
(the data model) over **TAXII** (the transport) — so it can be machine-ingested.

### MITRE ATT&CK: the common language

**MITRE ATT&CK** is a structured, community knowledge base of real-world adversary
**tactics (the "why"/goal)** and **techniques (the "how")**. Teams map their
detections and hunts to ATT&CK to measure coverage, find gaps, and speak a common
language. If a stem describes "a structured knowledge base of adversary tactics and
techniques to map detections," the answer is **MITRE ATT&CK**. (The **Cyber Kill
Chain** and the **Diamond Model** are related adversary frameworks — kill chain for
attack phases, Diamond for relating adversary/capability/infrastructure/victim.)

## Monitoring and detection engineering

Detection engineering turns hunt findings and intelligence into reliable, tuned,
automated detections — treating detections as code (version-controlled, tested).

### The SIEM

A **SIEM (Security Information and Event Management)** aggregates logs from
firewalls, servers, endpoints, and cloud, then **correlates events across sources**
to detect multi-stage attacks and raise alerts. It is the backbone when the
requirement is "collect everything and correlate to spot an attack that spans
systems." A SIEM is only as good as its **log sources, parsing, and tuning** — too
many false positives and analysts tune out (alert fatigue).

### UEBA

**UEBA (User and Entity Behavior Analytics)** builds a baseline of normal behavior
per user and device and flags **deviations** — impossible travel, a service account
suddenly browsing file shares, off-hours bulk downloads. UEBA is the control for
catching a **compromised-but-valid account** or a **malicious insider**, where no
signature or bad IP is involved — the credentials are legitimate; only the behavior
is wrong.

> **SIEM** = aggregate + correlate logs across sources for multi-stage detection.
> **UEBA** = baseline normal and flag anomalies — the way to catch a valid account
> being misused or an insider.

### The time-sync prerequisite

Correlation across systems is impossible if clocks disagree. If timestamps from
firewalls, servers, and endpoints are off by minutes, you cannot reconstruct the
true event sequence. The fix is **synchronized time** via **NTP** to a common
source. Accurate, synchronized timestamps are a foundational requirement for both
monitoring and forensics.

> If logs can't be correlated because timestamps disagree, the problem is **clock
> synchronization** — deploy **NTP** so every source shares one time base.

### Telemetry sources and tuning

Feed detection from endpoints (**EDR**), network (**NDR**, flow/packet), identity,
and cloud logs — the broader the telemetry, the more an **XDR**-style correlation can
see. Reduce noise with **tuning**, enrichment (adding context/intel to alerts), and
**SOAR** to automate triage and response on what remains.

## Exam focus

- **Threat hunting** is **hypothesis-driven** and proactive — it starts from an idea
  ("if an attacker is doing X, I should see Y"), not an alert.
- **IOC** hunting (hash/IP) is brittle; **TTP/behavior** hunting is durable
  (**Pyramid of Pain**) — prefer behavior.
- **MITRE ATT&CK** = structured knowledge base of adversary **tactics (why)** and
  **techniques (how)** for mapping detections/coverage. Intel is shared via
  **STIX/TAXII**; CTI tiers = **strategic/operational/tactical**.
- **SIEM** aggregates and **correlates** logs across sources for multi-stage
  detection; **UEBA** baselines behavior to catch **compromised valid accounts and
  insiders**.
- Correlation and forensics both require **synchronized clocks** — use **NTP**; if
  timestamps disagree, that's the fix.
