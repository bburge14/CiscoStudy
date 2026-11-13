# Vulnerability Scanning & Assessment Tools

Vulnerability management starts with *finding* the weaknesses, and finding them
well is harder than clicking "scan." This lesson covers how to choose the right
scan for the target, why the same host can look clean or vulnerable depending on
*how* you look, and the tools that turn a scan into actionable findings.

## You can't scan what you can't see

> Before the first enterprise scan, you need **asset discovery and host/service
> enumeration** — a reliable inventory of live hosts and the services they run.
> A scan is only as complete as the asset list behind it.

From there, matching the scan method to the target is the whole game.

## Choosing the right scan

Each pairing below is a classic "which method?" question.

- **Credentialed vs. non-credentialed.** An **authenticated (credentialed)** scan
  logs in and reads actual patch levels, giving the most accurate picture — the
  right choice to find exactly which OS patches are missing on hardened servers. A
  **non-credentialed** scan sees only the outside and tends to report many
  "potential" findings — a common source of **false positives** the admin insists
  were patched months ago.
- **Agent-based vs. network.** Sales laptops that are frequently off-network and
  rarely online for scheduled scans are best covered by **agent-based scanning** —
  the agent assesses locally and reports back when it reconnects.
- **Passive vs. active.** Active scanners *probe*, which can crash fragile legacy
  **SCADA/OT** controllers. When management still wants visibility, use **passive
  network monitoring** of the OT segment — it watches traffic without touching the
  devices.
- **Internal vs. external.** An **external** scan launched from outside the
  perimeter shows exactly what an unauthenticated internet attacker could
  enumerate against a new DMZ app — a different, and often scarier, view than an
  internal scan.
- **Continuous vs. scheduled.** A cloud environment that spins ephemeral
  instances up and down many times a day defeats a monthly scan. Use
  **continuous/automated scanning triggered as assets are provisioned**.
- **Container images.** For apps shipped as containers, scan the **images in the
  registry / CI pipeline** *before* deployment, catching vulnerable packages
  early rather than in production.

### False positives vs. false negatives

Know the difference, and which is worse:

- A **false positive** is a reported vulnerability that isn't really there — noise
  that wastes remediation effort (often from non-credentialed scans).
- A **false negative** is a real vulnerability the scan *missed* — the more
  dangerous result, because it goes unaddressed. A firewall dropping a scanner's
  probes makes a segment under-report: the "clean" result is really false
  negatives, so scan from *inside* the protected segment.

## Standards and compliance drivers

- **SCAP (Security Content Automation Protocol)** lets different tools run
  automated configuration-compliance checks consistently against a standardized
  benchmark — the answer whenever an agency needs interoperable, repeatable
  compliance scanning.
- **PCI DSS** requires merchants handling payment-card data to run **external
  vulnerability scans at least quarterly by an Approved Scanning Vendor (ASV)**,
  and again **after significant changes**.
- **Scan timing.** An intensive authenticated scan that degrades a busy ERP
  system at peak hours should be moved to an approved **maintenance window** —
  visibility shouldn't cost an outage.

## Assessment tools

Once you have results — or want to probe directly — these are the tools the exam
expects you to recognize.

| Tool | What it's for |
|------|---------------|
| **Nmap** | Host/port/service discovery; `-sV` does **service/version detection** |
| **Nessus** | Widely used network and host vulnerability scanner |
| **Nikto** | Flags outdated web-server software, dangerous default files, misconfigurations |
| **Burp Suite / OWASP ZAP** | **Intercepting proxies** to manipulate HTTP requests against a running web app |

**Nmap's `-sV`** is the option purpose-built to identify the exact service and
software version behind each open port — essential for mapping what's actually
exposed.

### Testing application code and components

> **SAST** reads source code *without running it*; **DAST** tests the *running*
> application from the outside; **IAST** instruments the app with an agent that
> watches it during QA; **SCA** inventories the third-party/open-source
> components bundled inside it.

- **SAST (Static)** finds vulnerable code **early** and pinpoints the exact line,
  but tends to produce **more false positives**.
- **DAST (Dynamic)** tests from the outside with no source access, catching
  runtime and configuration flaws a static view misses.
- **IAST (Interactive)** correlates runtime behavior with specific code by
  observing execution during functional tests — a hybrid of the two.
- **SCA (Software Composition Analysis)** is how you keep finding vulnerable
  open-source libraries after an incident like **Log4Shell** — ongoing
  identification of what's buried in your dependencies.
- **Fuzzing** feeds a program large volumes of malformed, unexpected, and random
  input to trigger crashes or memory errors that reveal vulnerabilities.

A **software bill of materials (SBOM)** is the formal, machine-readable inventory
of every component and dependency — so the *next* time a library is disclosed as
vulnerable, you can answer "are we affected?" in minutes, not weeks.

### Naming things: CWE vs. CVE

A finding may cite both, and they are not the same:

- **CWE (Common Weakness Enumeration)** names the *weakness type* — e.g.,
  **CWE-89** is "SQL injection" as a class.
- **CVE (Common Vulnerabilities and Exposures)** identifies a *specific
  vulnerability instance* in a particular product — e.g., **CVE-2023-XXXX**.

CWE is the category; CVE is the individual case.

## Exam focus

- **Asset discovery** comes first — you can't scan an unknown host.
- **Credentialed** scans are most accurate for patch levels; **non-credentialed**
  breed false positives. **Agent-based** suits roaming laptops; **passive
  monitoring** suits fragile **OT/SCADA**; **external** scans show the attacker's
  outside view; **continuous** scanning suits ephemeral cloud assets; scan
  **container images in the pipeline**.
- **False negative** (missed real vuln) is worse than a false positive; a firewall
  dropping probes causes false negatives — scan from inside the segment.
- **SCAP** = standardized, interoperable compliance checks; **PCI DSS** = quarterly
  **ASV** external scans + after significant changes; move heavy scans to a
  **maintenance window**.
- **Nmap `-sV`** = service/version; **Nessus** = host/network scanner; **Nikto** =
  web-server issues; **Burp/ZAP** = intercepting proxies.
- **SAST** (source, early, more false positives) vs **DAST** (running app,
  black-box) vs **IAST** (agent during QA) vs **SCA** (open-source components);
  **fuzzing** = malformed input; **SBOM** = component inventory.
- **CWE** = weakness *type*; **CVE** = a specific vulnerability *instance*.
