# Analyzing Indicators of Malicious Activity

Most of a SOC analyst's day is spent answering one question: *is this normal, or
is this an attacker?* This lesson is a field guide to the tell-tale signs —
grouped into network, host, and application indicators — so that when an alert
fires you can name the behavior and act on it. None of this is about *running*
attacks; it is about recognizing their footprints in your telemetry.

## Network indicators

The wire rarely lies if you know what to listen for.

- **Command-and-control (C2) beaconing.** A host that connects to the same
  external IP every 60 seconds, each time sending a small, uniform payload,
  around the clock, is not browsing the web — it is *beaconing* to its handler
  for instructions. Regularity and uniformity are the giveaways.
- **Port / network scanning.** A single internal IP rapidly opening connections
  to hundreds of ports across many hosts within seconds is **reconnaissance** —
  usually an attacker mapping the network after a foothold.
- **Domain generation algorithm (DGA).** Malware that makes DNS lookups for
  dozens of long, algorithmically generated domains each day — most of which
  fail to resolve until one succeeds — is using a DGA to find its C2 while
  staying ahead of domain blocklists.
- **DNS tunneling.** A host issuing a high volume of DNS queries for long,
  random-looking *subdomains of a single registered domain* is smuggling data or
  C2 inside DNS, a protocol firewalls rarely block.

> Beaconing is about *rhythm* (same peer, same interval). A DGA is about *many
> changing domains*. DNS tunneling is about *one domain with endless weird
> subdomains*. Keep those three straight.

## Host indicators

On the endpoint, attackers must execute, hide, and survive a reboot — and each
leaves artifacts.

- **Credential dumping.** An unusual process opening a handle to `lsass.exe` and
  reading its memory is harvesting credentials from the Local Security Authority
  Subsystem. LSASS access by anything but the OS is a red flag.
- **Masquerading.** A process named `svchost.exe` running from
  `C:\Users\Public\` and *not* spawned by `services.exe` is malware wearing a
  trusted name. The right name in the wrong place (or with the wrong parent) is
  the tell.
- **Persistence.** After eradication you must ensure malware will not relaunch at
  logon. Inspect **Run / RunOnce registry keys** and **scheduled tasks** first —
  the two most common auto-start footholds.
- **Command obfuscation / defense evasion.** A process launched as
  `powershell.exe -nop -w hidden -enc <long Base64 string>` is hiding its intent:
  `-enc` runs a Base64-encoded command so the real instructions never appear in
  plain text.
- **Living-off-the-land binaries (LOLBins).** Attackers abuse signed,
  built-in Windows tools to download and run payloads while blending in. Learn
  the usual suspects — `certutil.exe` (can download and decode files) and
  `mshta.exe` (executes scripted HTA content) among them.

### Data staging

Just before exfiltration, attackers often **collect and stage** data. A large,
multi-part `.rar` archive of documents appearing in a server temp directory is
classic staging — the loot is being bundled for a quick, quiet exit. Spotting it
here, before the upload, is a rare chance to stop a breach mid-stride.

## Account and identity indicators

- **Impossible (atypical) travel.** An account that authenticates from New York
  and, eight minutes later, from Singapore cannot have physically moved. This
  geographic impossibility points to **credential compromise** — two parties
  using one identity.

These account-based signals are why **UEBA** and identity logs belong in every
hunt for compromised credentials.

## Application and email indicators

Email authentication is a favorite exam target because the mechanisms interlock.

> **SPF** checks the *envelope* (Return-Path) sender's IP. **DKIM** cryptographically
> signs the message. **DMARC** ties them to the visible **From** header through
> *alignment* and tells receivers what to do on failure.

- A spoofed message can **pass SPF yet fail DMARC**: SPF authenticated the
  envelope domain, but that domain did not *align* with the From-header domain,
  so DMARC — which cares about the From the user actually sees — still fails.
- When triaging a suspected phish, header mismatches are strong evidence: the
  **From** domain differs from the **Return-Path**, and **Reply-To** points to an
  unrelated address. Legitimate mail rarely scatters its addresses like that.

For web-application attack indicators (SQL injection, XSS, and friends) you will
go deeper in the Vulnerability Management unit; here, just recognize that
suspicious input patterns in web logs are host-and-application indicators too.

## Putting an alert together

A single indicator is a lead, not a verdict. The craft is correlation: an LSASS
read (host) *plus* new outbound beaconing (network) *plus* an impossible-travel
login (identity) is a story — credential theft, C2, and misuse — not three
unrelated blips. Analysts who map each indicator to a stage of the attack turn
noise into a timeline a responder can act on.

## Exam focus

- **C2 beaconing** = regular, uniform callbacks to the same peer; **DGA** = many
  generated domains, mostly failing to resolve; **DNS tunneling** = endless
  random subdomains of *one* domain. Don't swap them.
- **LSASS memory access** = credential dumping. **Right name, wrong path/parent**
  (e.g., `svchost.exe` from `C:\Users\Public\`) = masquerading.
- Persistence lives in **Run/RunOnce keys** and **scheduled tasks**.
- `powershell -enc <Base64>` = command obfuscation / defense evasion;
  **`certutil.exe` and `mshta.exe`** are abused **LOLBins**.
- A staged **multi-part `.rar` in a temp dir** = data **collection/staging**
  before exfiltration.
- **Impossible travel** = likely **credential compromise**.
- A spoof can **pass SPF but fail DMARC** because the envelope domain doesn't
  **align** with the From header; **From ≠ Return-Path** with an odd **Reply-To**
  signals spoofing.
