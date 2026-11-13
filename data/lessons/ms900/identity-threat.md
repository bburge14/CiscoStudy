# Identity with Microsoft Entra ID & Threat Protection

Security in Microsoft 365 starts with a simple truth: in a cloud world, **identity
is the new security perimeter**. There's no office wall to hide behind, so the
question "is this really you, and should you be allowed in?" becomes the front
line. This lesson covers the service that answers that question — **Microsoft Entra
ID** — and the **Microsoft Defender XDR** suite that hunts threats once attackers
get past it.

## Microsoft Entra ID: the identity backbone

> **Microsoft Entra ID** (formerly **Azure Active Directory / Azure AD**) is
> Microsoft 365's cloud **identity and access management** service. It stores user
> accounts, **authenticates** sign-ins, and enables **single sign-on** to
> Microsoft 365 and thousands of other apps.

Two words you must not confuse:

- **Authentication** = proving **who you are** (sign-in).
- **Authorization** = deciding **what you're allowed to do** once you're in.

### Making sign-in stronger

Passwords alone are weak, so Entra ID layers on better methods:

- **Multi-factor authentication (MFA)** — require **two or more** kinds of proof:
  something you **know** (password), something you **have** (phone, security key),
  or something you **are** (fingerprint, face). Even a stolen password isn't enough.
- **Microsoft Authenticator** — the phone app that **approves sign-in requests**,
  supplies **one-time passcodes**, and enables **passwordless** sign-in.
- **Passwordless authentication** — remove the password entirely, using
  **Windows Hello**, **FIDO2 security keys**, or the Authenticator app. Nothing to
  phish or reuse.
- **Single sign-on (SSO)** — sign in once and reach many apps without re-entering
  credentials.
- **Self-service password reset (SSPR)** — let users **securely reset or unlock
  their own accounts** after verifying their identity, cutting help-desk calls.

### Deciding access with signals

Authentication is only step one. Entra ID then decides *whether to grant access*
based on context:

> **Conditional Access** evaluates signals — the user, the device's health and
> compliance, the location, the app, and the sign-in risk — and then **grants,
> blocks, or requires extra proof** (like MFA) for each access attempt.

Conditional Access is where identity meets Zero Trust: access isn't automatic; it's
earned per request. Working alongside it, **Microsoft Entra ID Protection**
automatically **detects risky sign-ins** — logins from anonymous IP addresses,
impossible/atypical travel, leaked credentials — and can trigger automatic
responses such as blocking or forcing a password change.

### Kinds of identity

Entra ID handles more than employees:

- **Member users** — your own organization's accounts.
- **Guest users (B2B)** — people from **outside** your organization invited to
  collaborate, using their own credentials.
- **Hybrid identity** — on-premises Active Directory accounts **synchronized** to
  Entra ID (via Microsoft Entra Connect), so users have one identity across both.

## Microsoft Defender XDR: threat protection

Even strong identity won't stop every threat, so Microsoft 365 includes an
integrated detection-and-response suite.

> **Microsoft Defender XDR** (formerly **Microsoft 365 Defender**) is a unified
> **extended detection and response (XDR)** suite. It collects and **correlates
> signals** across identities, endpoints, email, and cloud apps into prioritized
> **incidents**, managed from the **Microsoft Defender portal**
> (security.microsoft.com).

Its four core workloads each defend a different surface — learn them by what they
protect:

| Defender service | Protects | Classic scenario |
|------------------|----------|------------------|
| **Defender for Endpoint** | Laptops and servers (EDR) | Detect/investigate/respond to threats *on devices* |
| **Defender for Office 365** | Email and collaboration | Malicious links and attachments in email |
| **Defender for Identity** | On-premises Active Directory | Compromised accounts, lateral movement on-prem |
| **Defender for Cloud Apps** | Cloud/SaaS apps (CASB) | Discover **shadow IT** — unsanctioned cloud apps |

Two Defender for Office 365 features worth naming:

- **Safe Links** — **re-checks URLs at the moment you click**, so a link that was
  safe at delivery but turned malicious later is still caught.
- **Safe Attachments** — opens email attachments in an isolated sandbox
  ("detonates" them) to catch malware before it reaches the user.

### Measuring your posture

How do you know if you're well-configured? **Microsoft Secure Score** measures your
**security posture**, assigns a **score**, and recommends concrete improvements
(enable MFA, close risky settings). A higher score means a stronger posture, and it
gives security teams a clear, prioritized to-do list.

## The whole thing in one paragraph

**Microsoft Entra ID** (formerly Azure AD) is the cloud identity service that
**authenticates** users and enables **SSO**, strengthened by **MFA** (often via
**Microsoft Authenticator**), **passwordless** sign-in, **SSPR**, **Conditional
Access** (grant/block/require-MFA based on signals), and **Entra ID Protection**
(detecting risky sign-ins) — handling members, B2B **guests**, and **hybrid**
identities. **Microsoft Defender XDR** (formerly Microsoft 365 Defender) then
correlates signals into incidents across its workloads — **Defender for Endpoint**
(devices), **Defender for Office 365** (email, with **Safe Links** and **Safe
Attachments**), **Defender for Identity** (on-prem AD), and **Defender for Cloud
Apps** (shadow IT) — while **Microsoft Secure Score** measures and improves your
posture.

## Exam focus

- **Microsoft Entra ID = formerly Azure AD**, the cloud identity/access service.
  **Authentication** = who you are; **authorization** = what you can do.
- Know the identity features: **MFA** (two+ factors), **Microsoft Authenticator**
  (approve sign-ins/OTP/passwordless), **SSO**, **SSPR** (self-service reset),
  **Conditional Access** (signal-based grant/block), **Entra ID Protection** (risky
  sign-in detection).
- **Microsoft Defender XDR = formerly Microsoft 365 Defender**, managed in the
  **Microsoft Defender portal**. Match the workloads: **Endpoint** = devices,
  **Office 365** = email, **Identity** = on-prem AD, **Cloud Apps** = shadow
  IT/SaaS discovery (CASB).
- **Safe Links** = re-check URLs *at click time*; **Safe Attachments** = sandbox
  email attachments.
- **Microsoft Secure Score** measures your **security posture** and recommends
  improvements.
