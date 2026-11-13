# Mobile, IoT & Big Data Security

The endpoints an SSCP protects are no longer just desktops. Smartphones carry
corporate data out the door, IoT devices sprinkle tiny unmanaged computers across
the environment, and big-data platforms concentrate enormous volumes of sensitive
information. Each breaks the assumptions of traditional endpoint security in its
own way. This lesson covers the controls for all three.

## Managing mobile devices

Phones and tablets mix personal and corporate life, often on hardware the company
doesn't own. The management approach depends on ownership:

| Model | Meaning |
|-------|---------|
| **BYOD** | Bring Your Own Device — employee-owned, personal and work data mixed |
| **COPE** | Corporate-Owned, Personally Enabled — company owns it, some personal use allowed |
| **CYOD** | Choose Your Own Device — pick from an approved, company-managed list |
| **COBO** | Corporate-Owned, Business-Only — locked to work use |

To enforce policy, organizations use management tooling — and the exam distinguishes
two scopes:

> **MDM (Mobile Device Management)** manages the **entire device** (enforce
> passcode, encryption, remote wipe) — natural for corporate-owned hardware.
> **MAM (Mobile Application Management)** manages **only the corporate apps and
> data** — deploying them, applying policy, and wiping them — without touching the
> user's personal content. **UEM (Unified Endpoint Management)** unifies both,
> across mobile and traditional endpoints.

> On employee-owned **BYOD** phones, where the company wants to control only its own
> apps and data and leave personal content alone, **MAM** (with
> **containerization** that walls corporate data into a managed container) is the
> right fit.

That container concept drives the right way to offboard a personal device:

> A **selective (enterprise) wipe** removes **only** the managed corporate
> container/apps and data, leaving the employee's personal photos and messages
> intact — the correct choice when a BYOD employee leaves. A **full wipe** erases
> the entire device (appropriate for corporate-owned or a lost/stolen device).

## Mobile threats and controls

- **Jailbreaking (iOS) / rooting (Android)** — removing the vendor's built-in
  restrictions. This is a serious risk because it **strips away the OS security
  controls and app sandboxing**, letting untrusted code run with elevated
  privileges and potentially bypassing MDM/MAM protections. MDM should detect and
  block jailbroken/rooted devices.
- **App sandboxing** — the OS isolates each app so it can't freely access others'
  data; jailbreaking defeats it.
- **Sideloading / untrusted apps** — installing apps from outside the official
  store bypasses vetting; enforce approved stores.
- **Device loss/theft** — mitigate with **full-disk encryption**, strong
  screen-lock, and **remote wipe**.
- **Insecure networks** — public Wi-Fi exposes traffic; require a **VPN**.

## Securing IoT and operational technology

The **Internet of Things (IoT)** — cameras, sensors, smart devices — and
**operational technology (OT)** like **ICS/SCADA** industrial controls bring
computers into places never designed for security.

> IoT devices are hard to secure because they often ship with **weak default
> credentials**, **rarely or never receive patches**, have **no user interface** to
> configure, and run stripped-down software — yet they sit on the same network as
> everything else.

The defenses are pragmatic:

- **Change default credentials** immediately — default passwords are the number-one
  IoT weakness (and how many IoT botnets are built).
- **Network segmentation** — isolate IoT/OT onto their own VLANs so a compromised
  camera can't reach servers, and so fragile OT systems are shielded.
- **Patch/update** where possible; inventory devices you can't.
- **Disable unneeded features/services** and restrict inbound/outbound traffic.
- For **OT/ICS/SCADA**, remember these prioritize **availability and safety** over
  confidentiality, often can't be patched or rebooted freely, and may run legacy
  protocols — so segmentation and monitoring matter more than aggressive patching.

## Securing big data

Big-data platforms (data lakes, analytics clusters) concentrate huge volumes of
data, which makes them both valuable and risky. The "three Vs" — **volume,
variety, velocity** — strain traditional controls. Key practices:

- **Access control at scale** — fine-grained authorization so analysts see only
  what they should; a single over-broad grant can expose everything.
- **Encryption** of data at rest and in transit across the cluster.
- **De-identification** — **anonymization** (irreversibly removing identifiers) or
  **pseudonymization/tokenization** (replacing identifiers reversibly) so analytics
  can run without exposing real PII. Beware that combining "anonymized" datasets can
  sometimes **re-identify** individuals.
- **Data governance and classification** — know what sensitive data lives in the
  lake, and apply retention and handling rules to it.
- **Secure the pipeline and APIs** feeding the platform, not just the storage.

Edge and embedded computing extend the same themes outward: constrained devices,
physical exposure, and the need to push security (encryption, authentication,
secure boot) down to the smallest nodes.

## Exam focus

- Ownership models: **BYOD, COPE, CYOD, COBO.** **MDM** manages the **whole
  device**; **MAM** manages **only corporate apps/data** (best for BYOD, via
  **containerization**); **UEM** unifies them.
- A **selective/enterprise wipe** removes only the corporate container (right for a
  departing BYOD employee); a **full wipe** erases everything (lost/stolen or
  corporate-owned).
- **Jailbreaking/rooting** removes vendor security controls and **app sandboxing**,
  enabling elevated untrusted code and bypassing MDM — block such devices.
- **IoT** risks: **weak default credentials, no/late patches, no UI.** Defend with
  **changing defaults** and **network segmentation**. **OT/ICS/SCADA** prioritize
  **availability/safety** and resist patching — segment and monitor them.
- **Big data**: enforce **access control at scale**, **encryption**, and
  **anonymization/pseudonymization** (watching for **re-identification**), under
  solid **data governance**.
