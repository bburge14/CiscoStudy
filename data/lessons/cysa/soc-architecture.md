# System & Network Architecture, Logging & SOC Tooling

Before you can spot an attacker, you have to know what *normal* looks like and
where the evidence lives. This lesson is about the ground a SOC analyst stands
on: the architecture and log sources that record what happened, and the tools —
SIEM, SOAR, EDR, and the packet analyzers — that turn a flood of raw events into
a defensible answer.

## Know normal: baselining and asset visibility

You cannot detect an anomaly without a baseline. A **baseline** is a recorded
snapshot of normal behavior — which services run, which ports listen, how much
data a host usually sends, who logs in and when.

> **Baselining** captures normal activity so that deviations stand out. A
> workstation that averages 10 MB of uploads a day suddenly pushing 4 GB over
> HTTPS at 3 a.m. is only "obviously bad" because you know its baseline.

Two baselines matter constantly:

- **System baseline** — the known-good build, often a **gold image**. To find
  unauthorized persistence, *diff* a host's current autoruns, services, and
  scheduled tasks against that gold image; anything new is suspect.
- **Network baseline** — typical traffic volumes, protocols, and peers. Compare
  current flow against the host's established baseline to flag exfiltration.

None of this works without an **asset inventory**. If you do not know a host
exists, you will not baseline it, scan it, or notice when it misbehaves.

## Where the evidence lives: log and telemetry sources

Sort your data sources into two buckets, because the exam leans on the
distinction:

| Bucket | Examples | Answers the question |
|--------|----------|----------------------|
| **Endpoint (host) telemetry** | Windows Security event log, Sysmon, EDR | What happened *on the machine*? |
| **Network telemetry** | Firewall logs, IDS/IPS, NetFlow, full packet capture (PCAP) | What crossed *the wire*? |

- **NetFlow / flow records** log the *metadata* of conversations — who talked to
  whom, when, how much — without storing payloads. When full packet storage is
  unavailable, flow records are how you find which internal hosts contacted a
  malicious IP over the last 30 days.
- **Full packet capture (PCAP)** stores the actual bytes. It is the only source
  that shows the real payloads and destinations of exfiltrated data.
- **EDR telemetry** reconstructs process execution, file changes, and
  parent-child process relationships across the fleet.

### Windows event IDs worth memorizing

Windows writes security-relevant events to the **Security** log; **Sysmon** adds
richer detail. Know these cold:

- **4624** — a successful logon. The **Logon Type** tells you *how*: Type **3** =
  network (e.g., SMB), Type **10** = **RemoteInteractive (RDP / Terminal
  Services)**.
- **4625** — an account failed to log on. A burst of 4625s against one account is
  classic password guessing.
- **4688** — a new process was created; with command-line auditing on, it
  captures the full command line (gold for catching malicious macros).
- **4720** — a user account was created.
- **Sysmon Event ID 1** — process creation; **Event ID 3** — a network
  connection, tying a process to the outbound socket it opened.

### Ports as evidence

A service exposed where it should not be is itself a finding. Recognize
**TCP 445** (SMB — abused for lateral movement), **TCP 3389** (RDP — dangerous
when internet-facing), and **TCP 443** (HTTPS).

## Analysis techniques

Raw logs do not accuse anyone; analysis does.

- **Time synchronization.** Correlating firewall, IDS, and server events into one
  timeline only works if every source agrees on the clock. Enforce **NTP** so
  timestamps line up — out-of-order events usually mean a clock-sync problem,
  not time travel.
- **Parent-child process lineage.** `winword.exe` spawning `cmd.exe` spawning
  `powershell.exe` is an anomalous lineage that screams *malicious document*.
- **Deep packet inspection (DPI).** Traffic on TCP 443 that does not follow TLS
  and looks like an interactive shell is a liar. Application-layer DPI reveals
  the *true* protocol regardless of the port it rides on.
- **Baseline deviation.** Volume, timing, and peer anomalies all come back to
  "this is not what this host normally does."

## The SOC toolkit

> A **SIEM** (Security Information and Event Management) aggregates logs from
> across the environment and **correlates** them to detect multi-stage attacks.
> A **SOAR** (Security Orchestration, Automation and Response) then *acts* on
> findings through automated **playbooks**.

Think of the SIEM as the detective that notices the pattern and the SOAR as the
dispatcher that sends the response — enrich the indicator, open a ticket,
isolate the host — without a human clicking each step. Replacing manual,
repetitive triage with a playbook buys **faster, more consistent response with
fewer human errors**.

The rest of the kit:

- **EDR (Endpoint Detection and Response)** — detects on *behavior*, not just
  signatures, and lets you remotely isolate a host and kill a malicious process.
- **XDR (Extended Detection and Response)** — correlates and responds across
  endpoints, email, identity, and cloud from one platform, instead of analyzing
  each silo alone.
- **UEBA (User and Entity Behavior Analytics)** — builds behavioral baselines
  per user and device and alerts on sharp deviations, catching compromised
  accounts and insider misuse.

### Packet and log analysis tools

- **Wireshark** — a GUI packet analyzer. A **display filter** such as
  `http.request.method == "POST"` narrows a capture to what you care about, and
  **Follow TCP Stream** reassembles a conversation to confirm, say, credentials
  sent in cleartext.
- **tcpdump** — the headless capturer. `tcpdump 'host 10.0.0.5 and port 443' -w
  capture.pcap` grabs just the traffic you want and writes it for later analysis.
- **Sandbox detonation** — run a suspicious attachment in an isolated sandbox to
  watch its behavior safely; pair it with a hash reputation check.
- **Scripting.** To tally unique source IPs from a 5 GB firewall log, don't open
  it in a spreadsheet — write a script that streams the file line by line and
  aggregates counts, or apply a regular expression. Scripting is what makes
  analysis efficient and *repeatable*.

### Efficiency, integration, and tuning

Process improvement is a graded objective, not an afterthought. **Tool and
technology integration** (feeding EDR, intel, and ticketing into the SIEM) and
**standardized playbooks** cut response time. And tuning matters: when a
correlation rule floods analysts with alerts from a known-good vulnerability
scanner, **allow-list the scanner's source and refine the rule's thresholds** to
kill the noise and fight **alert fatigue** without going blind to real threats.

## Exam focus

- **Baseline first.** Deviation analysis — flow volume, logon patterns, autoruns
  diffed against the **gold image** — is how anomalies surface.
- **Endpoint vs network telemetry:** Windows Security log and Sysmon are
  endpoint sources; firewall, IDS, NetFlow, and PCAP are network sources.
- **Event IDs:** 4624 success (Type 3 = network, **Type 10 = RDP**), **4625**
  failed logon, **4688** process creation; **Sysmon 1** = process, **Sysmon 3**
  = network connection. Ports: **445** SMB, **3389** RDP, **443** HTTPS.
- **NetFlow** = who-talked-to-whom metadata (no payload); **full PCAP** = the
  actual bytes. Use flow records when packet storage is unavailable.
- Enforce **NTP** so multi-source timelines correlate; watch for anomalous
  **parent-child process** lineage; use **DPI** when the port lies about the
  protocol.
- **SIEM** correlates, **SOAR** automates the response, **EDR** isolates hosts on
  behavior, **XDR** spans domains, **UEBA** baselines users.
- **Wireshark** (display filters, Follow TCP Stream) and **tcpdump** (`-w` to a
  pcap) are the packet tools; **script** repetitive log parsing; **tune/allow-list**
  noisy rules to beat alert fatigue.
