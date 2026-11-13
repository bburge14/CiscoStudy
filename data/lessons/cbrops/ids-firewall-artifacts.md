# IDS/IPS Events, Firewalls & Intrusion Artifacts

When a sensor fires, the analyst's job is to judge it correctly: was it real?
did it get through? which device even produced this log? This lesson covers the
language of **IDS/IPS alert classification**, the kinds of **firewall filtering**
that permit or deny traffic, and the **intrusion artifacts** you extract from an
event to turn one alert into a fleet-wide hunt.

## Classifying IDS/IPS events

An intrusion detection or prevention system makes a judgment, and that judgment
can be right or wrong, in two directions. The four combinations are fundamental.

> **True positive** — alerted, and it really was malicious. **True negative** —
> stayed silent, and traffic really was benign. **False positive** — alerted, but
> it was benign. **False negative** — stayed silent, but it really was malicious
> (the dangerous missed detection).

| Outcome | Alert fired? | Actually malicious? | Example |
|---------|--------------|---------------------|---------|
| **True positive** | Yes | Yes | IPS alerts on a real exploit attempt |
| **True negative** | No | No | No alert while only normal traffic flows |
| **False positive** | Yes | No | Alert on an authorized backup transfer |
| **False negative** | No | Yes | Malware slips past with no alert |

**False negatives** are the most dangerous — a real attack no one was told about.
**False positives** are the most *expensive day to day*, because they burn
analyst time and, left unchecked, cause alert fatigue. Tuning a sensor is largely
about pushing both error types down.

CBROPS also uses **impact** language for events that *did* fire:

- An alert on activity that turns out to be **unusual but authorized and
  harmless** (an admin's approved vulnerability scan) is classified **benign**.
- When an **IPS drops** an inbound exploit before it reaches the target, the
  outcome is **no impact** — the malicious attempt was correctly detected **and
  blocked**.

### Reading the source technology from a log

Part of triage is recognizing *what produced* a line, because the format tells
you. Learn these signatures:

- `signature ET MALWARE matched — inbound exploit pattern in payload` → an
  **IDS/IPS** (signature-based network sensor).
- `DENY tcp 203.0.113.5:443 -> 10.1.1.9:51000, rule 42` → a **firewall**
  (permit/deny by **rule** and **5-tuple**).
- A line with a **username, full URL, HTTP method, response code, and bytes
  served** → a **web proxy** log.

Mapping an event back to the **rule** that generated it is a core CBROPS skill —
the rule ID, signature name, and matched fields tell you *why* the sensor spoke.

## Firewall filtering

Firewalls decide permit or deny, but *how* they decide varies, and the
differences matter for what they can catch.

> **Stateless** filtering judges each packet in isolation by header fields.
> **Stateful** filtering tracks active connections in a **state table** and
> matches returning packets to them. **Deep packet inspection (DPI)** goes
> further and examines the **payload / application-layer content**.

- **Stateless packet filtering** — a simple router ACL permits/denies each packet
  solely on **source/destination IP, port, and protocol**, keeping **no memory**
  of prior packets. Fast, but a crafted packet can match a permissive rule, so it
  can be **tricked** into passing traffic a stateful firewall would block.
- **Stateful firewall** — maintains a **state table** of active connections. It
  automatically permits the **return traffic** of a connection an internal host
  originated, without a separate inbound rule, because it recognizes the packets
  as part of a tracked session.
- **Deep packet inspection (DPI)** — examines the **payload**, not just headers.
  DPI is **required** for tasks like detecting a known exploit **signature** or a
  **sensitive-data pattern inside the payload** — things 5-tuple filtering can
  never see.
- **Proxy (application-layer gateway) firewall** — **terminates the client's
  connection** and makes the request to the server **on the client's behalf**,
  fully inspecting application-layer content in between.

A firewall should run a **default-deny** posture (an implicit deny): permit only
what is explicitly allowed and block everything else. That posture is why a
stateful firewall needs no inbound rule for return traffic — the state table, not
a broad allow rule, is what lets the replies back in.

## Intrusion artifacts

An artifact is a concrete detail pulled from an event that you can act on — to
block, to hunt, or to understand. Good analysts mine every alert for them.

> An **intrusion artifact** is an observable element of an event — a URL, a file
> hash, an IP, a process name, a registry key — that can be used as an **indicator
> of compromise (IOC)** to detect, block, and hunt the threat elsewhere.

Common artifacts and how you use them:

- **URL/URI requested** — a proxy log showing a request to
  `http://malicious-update[.]example/installer.exe` just before infection gives
  you a **URL to block and hunt** across the fleet.
- **File hash (SHA-256)** — match it against threat intelligence to **confirm a
  file is known malware**.
- **Process name + registry Run key** — a process like `svch0st.exe` (note the
  zero) spawned from an odd path, plus a new Run-key value, identify the
  **malicious process and its persistence mechanism** — host IOCs to detect and
  remediate across every machine.
- **Ports** — in a captured session, **443** is a **well-known** service port
  (HTTPS) while **51972** is a **client ephemeral** port; reading the pair tells
  you which side is the server.
- **Source vs. destination IP** — for an inbound web attack, **source = attacker,
  destination = victim**.
- **Request contents** — a URI like `/admin/../../etc/passwd` is a textbook
  **directory/path-traversal** attempt to read files outside the web root.

The analytic move is always the same: find the artifact, decide whether it is an
**IOC**, then **pivot** — block it at the firewall/DNS/proxy and search every log
source for the same artifact to find other affected hosts.

## Exam focus

- The four outcomes: **true positive** (alerted, real), **true negative** (quiet,
  benign), **false positive** (alerted, benign), **false negative** (quiet,
  malicious — the dangerous miss). **Benign** = fired on authorized/harmless
  activity; a **blocked** exploit = **no impact**.
- Identify the source device by log shape: **IDS/IPS** (signature match in
  payload), **firewall** (DENY by rule + 5-tuple), **web proxy** (user + URL +
  method + response code). Map events back to the **rule** that fired.
- Firewalls: **stateless** = per-packet, no memory, can be tricked; **stateful**
  = **state table** tracks connections and permits return traffic; **DPI** reads
  the **payload** (needed for exploit signatures / sensitive-data patterns);
  **proxy** terminates and re-originates the connection. Use a **default-deny**
  posture.
- **Artifacts** (URL, **hash**, IP, process name, registry key, ports, request
  URI) are **IOCs** to block and hunt. **443 = well-known, high ports =
  ephemeral**; **source = attacker**; `../` in a URI = **path traversal**.
