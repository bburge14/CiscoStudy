# Mobile, IoT & OT Hacking

The devices that are hardest to secure are often the ones that do not look like
computers: the phone in a pocket, the camera on a wall, the controller running a
factory line. This lesson covers three such domains — **mobile platforms**, the
**Internet of Things (IoT)**, and **Operational Technology (OT)**. The common
thread is weak defaults and long lifecycles; the common cure is strong
authentication, segmentation, and updates.

## Mobile platform security

### The two models

> **Android** is the more open platform — it permits **sideloading** apps from
> outside the official store — while **iOS** is more closed, relying on strict App
> Store vetting. Both enforce **app sandboxing**, **code signing**, and
> **permission models** to isolate apps from each other and the system.

### Mobile threats

- **Malicious and trojanized apps** — apps that request excessive permissions or
  hide malware.
- **App repackaging** — taking a legitimate app, **inserting malicious code**, and
  redistributing the modified package through **third-party stores**.
- **Sideloading from untrusted sources** — bypassing the vetted store entirely.
- **Jailbreaking (iOS) / rooting (Android)** — removing vendor restrictions, which
  also removes security protections.
- **Insecure data storage** and **insecure communication** — sensitive data saved
  in the clear or sent without proper TLS.
- **Smishing and malicious configuration profiles** — mobile-flavored social
  engineering.

The **OWASP Mobile Top 10** catalogues these risks the way the web list does.

### Mobile defenses

- **Certificate pinning** — the app **hard-codes the expected server certificate or
  public key**, so a man-in-the-middle presenting a *different* (even validly
  signed) certificate is rejected. This is the key defense against mobile
  interception.
- **MDM / MAM / UEM** — mobile device, application, and unified endpoint management
  enforce policy, enable **remote wipe**, and separate corporate from personal data
  via **containerization / work profiles**.
- **Install from official stores only**, and vet apps before deployment.
- **Device encryption, screen lock, and biometrics**; keep the OS **updated**.
- **Block jailbroken/rooted devices** from accessing corporate resources.

## IoT and OT security

### What they are

> **IoT (Internet of Things)** devices are networked embedded systems — cameras,
> sensors, smart-home gear. **OT (Operational Technology)** is the hardware and
> software that monitors and controls **physical industrial processes** (ICS,
> SCADA, PLCs).

### The IoT attack surface

IoT devices are notorious for **default or weak credentials, unpatched firmware,
no update mechanism, and exposed management services**. The canonical example:

> The **Mirai** botnet spread by scanning the Internet for devices with open
> **Telnet** and trying a built-in list of **factory-default logins**, then used the
> compromised devices to launch massive DDoS attacks.

Know the common IoT protocols:

- **MQTT** — a lightweight publish/subscribe messaging protocol over TCP.
- **CoAP (Constrained Application Protocol)** — a lightweight **RESTful** protocol
  that runs over **UDP** for constrained devices and, lacking built-in
  authentication, relies on **DTLS** for security when exposed.
- **Zigbee, Z-Wave, BLE** — short-range wireless protocols for home/building
  automation.

### The OT difference

OT prioritizes **availability and safety** over confidentiality, and its equipment
has **decades-long lifecycles**, so patching is hard and systems are often legacy.
Its protocols — **Modbus** and **DNP3** — were designed for isolated networks and
frequently include **no authentication or encryption**. The **Purdue model**
describes the layered zones used to segment OT from IT. **Stuxnet** is the historic
example of malware purpose-built to attack industrial controllers; **IT/OT
convergence** has since widened the exposure.

### IoT/OT defenses

- **Change default credentials** immediately and disable unused services
  (especially **Telnet**).
- **Segment and zone** IoT/OT away from IT networks (per the Purdue model);
  air-gap the most critical systems where feasible.
- **Apply firmware/vendor updates** on a managed schedule.
- **Maintain an asset inventory** — you cannot protect what you do not know you
  have.
- **Monitor with OT-aware tooling** that understands industrial protocols.
- **Require authentication and encryption** wherever the equipment supports it.

> The unifying lesson: these devices ship insecure by default and live a long time,
> so defense leans on **changing defaults, segmenting networks, and sustaining
> updates** rather than on the device securing itself.

## The common thread

Mobile, IoT, and OT look different, but they fail in the same way: devices that ship
with weak defaults, live far longer than the vendor supports them, and sit outside
the patching and monitoring that cover traditional IT. The defensive answer is
therefore consistent across all three — **know what you have (inventory), change the
defaults, segment it off, and sustain updates** — because the device will not secure
itself.

## Exam focus

- **Android** allows **sideloading**; **iOS** is more closed. Both use
  **sandboxing, code signing, and permissions**.
- **Certificate pinning** defeats a man-in-the-middle by rejecting any server
  certificate but the expected one — the key mobile interception defense.
- **App repackaging** = inserting malicious code into a legitimate app and
  redistributing it. **Jailbreaking/rooting** removes protections.
- **MDM/MAM/UEM** enforce policy, enable remote wipe, and containerize corporate
  data.
- **Mirai** compromised IoT via **open Telnet + default credentials** to build a
  DDoS botnet — so **change defaults and disable Telnet**.
- **CoAP** = lightweight RESTful IoT protocol over **UDP**, secured with **DTLS**;
  **MQTT** = pub/sub over TCP.
- **OT** (ICS/SCADA, PLCs) uses **Modbus/DNP3** (often no auth/encryption),
  prioritizes availability/safety, and is defended mainly by **segmentation
  (Purdue model)** and inventory.
