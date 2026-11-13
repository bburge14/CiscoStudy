# Microsoft Defender for Endpoint

Microsoft Defender for Endpoint (MDE) is the endpoint detection and response
(EDR) engine of Microsoft Defender XDR. It watches what happens on your
workstations, servers, and mobile devices, streams that telemetry to the cloud,
raises alerts, and gives the analyst the buttons to respond. For SC-200 you are
not configuring MDE as an administrator so much as *operating* it: onboarding
devices, reducing the attack surface, reading the device timeline, and letting
automation do the first pass of investigation and remediation.

## Getting devices into MDE: onboarding

A device produces no telemetry until it is **onboarded** — registered with your
tenant so its sensor reports in. How you onboard depends on the device and your
management tooling.

> **Onboarding connects a device's built-in sensor to your Defender for Endpoint
> tenant. Until a device is onboarded it is, at best, only *discovered* — seen on
> the network but not reporting its own events.**

Common onboarding paths you should recognize:

- **Local script** — a small package you run on a handful of machines. Fine for a
  lab or a pilot; it does not scale and is not meant for production fleets.
- **Microsoft Intune / Configuration Manager / Group Policy** — the scalable ways
  to push onboarding to managed Windows estates.
- **VDI onboarding package** — a dedicated package for **non-persistent virtual
  desktops** that are re-imaged frequently, so each rebuilt instance registers
  consistently instead of flooding the portal with duplicates.
- **Security settings management** — lets MDE itself enforce endpoint security
  policy on devices that are not enrolled in Intune.

Servers can be onboarded through the **Microsoft Defender for Cloud** integration
(the Defender for Servers plan deploys the MDE sensor) or directly. Know that the
two products are joined: Defender for Cloud uses MDE as its endpoint detection
component.

**Device discovery** rounds out the picture — onboarded devices passively
discover *unmanaged* devices on the same network so you can see shadow endpoints
and prioritize onboarding them.

## Reducing the attack surface

Detection is only half the job; the other half is shrinking what an attacker can
even attempt. **Attack surface reduction (ASR) rules** block the risky behaviors
malware relies on — Office apps spawning child processes, scripts launching
downloaded executables, credential theft from LSASS, and so on.

Each ASR rule runs in one of four modes:

| Mode | What it does |
|------|--------------|
| **Not configured / Off** | The rule is disabled. |
| **Audit** | Logs what *would* have been blocked, without blocking — your safe test mode. |
| **Block** | Enforces the rule and stops the behavior. |
| **Warn** | Blocks but lets the user override and continue. |

> The safe rollout pattern is **Audit first, then Block**. Turn a rule on in audit
> mode, review the `DeviceEvents` it generates for false positives, add exclusions
> where legitimate software trips it, and only then switch to Block.

Microsoft Defender Antivirus must be in **active mode** for ASR to function —
rules do nothing if the antivirus is passive or disabled. ASR is one pillar of a
broader family that also includes controlled folder access (anti-ransomware),
network protection, and web content filtering.

## Responding to a device: the analyst's buttons

When MDE flags something, the device page gives you **response actions** you can
take right from the portal:

- **Isolate device** — cut the machine off the network while still letting it talk
  to the Defender service, so you can investigate without the threat spreading.
- **Collect investigation package** — gather forensic artifacts (running
  processes, autoruns, network connections) into a downloadable bundle.
- **Run antivirus scan** — kick off a Defender AV scan remotely.
- **Restrict app execution** — allow only Microsoft-signed binaries to run.
- **Initiate Live Response** — open a remote command-line session on the device to
  pull files, run scripts, and remediate interactively.
- **Stop and quarantine a file** across every device where it appears.

Indicators let you tune verdicts: add a file hash, IP, URL, or certificate to an
**allow** or **block** list so MDE treats it the way you decide.

## Automated investigation and response (AIR)

A SOC cannot triage every alert by hand. **Automated investigation and response**
mimics the steps an analyst would take: when an alert fires, AIR examines the
files, processes, services, and registry keys involved, decides a verdict
(malicious, suspicious, or clean), and proposes remediation such as quarantining
a file or stopping a process.

> AIR's willingness to act on its own is set by the device group's **automation
> level**. At **Full** automation it remediates automatically; at **Semi**
> levels, remediation waits in the **Action center** for an analyst to approve.

The **Action center** is where pending and completed actions live — both the
automated ones awaiting approval and the manual ones you triggered. Approving or
rejecting there keeps a clean audit trail. Threat and vulnerability management
(exposure data, security recommendations, and the device's exposure/risk levels)
rounds out MDE by telling you *which* weaknesses to fix before they are exploited.

## Putting it together

MDE's value is the loop: onboard a device so its sensor reports, shrink its attack
surface with ASR rules, let EDR raise alerts on what slips through, let AIR triage
and remediate the routine cases, and reach for isolation, investigation packages,
and Live Response on the ones that need a human. Everything surfaces into the
Microsoft Defender portal and feeds the unified incident queue you will meet later
in this unit.

## Exam focus

- A device must be **onboarded** to report telemetry; **device discovery** only
  *finds* unmanaged devices. Use the **VDI package** for non-persistent virtual
  desktops, and Intune/Configuration Manager/GPO for scalable Windows onboarding.
- **ASR rule modes = Off, Audit, Block, Warn.** Roll out in **Audit first**, check
  false positives, then **Block**. Defender Antivirus must be in **active mode**.
- Know the response actions and what each is *for*: **isolate** (contain without
  losing contact), **collect investigation package** (forensics), **restrict app
  execution**, **Live Response** (interactive remote shell).
- **Automated investigation and response (AIR)** triages alerts; the **automation
  level** (Full vs Semi) decides whether remediation runs automatically or waits
  in the **Action center** for approval.
- Server onboarding commonly flows through **Defender for Cloud (Defender for
  Servers)**, which deploys the MDE sensor — the two products are integrated.
