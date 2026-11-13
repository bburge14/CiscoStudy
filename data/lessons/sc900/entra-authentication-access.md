# Authentication & Access Management

Having identities is only half the job. Entra ID also has to **prove** those
identities at sign-in and then **decide** what each one can reach. This lesson
covers the two capabilities that do that work: **authentication** (how Entra ID
verifies users, including MFA and passwordless) and **access management**
(Conditional Access, roles/RBAC, and Global Secure Access).

## Authentication factors and multifactor authentication

A password alone is weak — it can be phished, guessed or reused. The fix is to
require more than one kind of proof. Authentication factors fall into three
categories:

> - **Something you know** — a password or PIN.
> - **Something you have** — a phone, a security key, a token.
> - **Something you are** — a biometric such as a fingerprint or face.

> **Multifactor authentication (MFA)** requires two or more verification factors
> from **different** categories. A password *plus* an approval tapped on your
> phone is MFA; two passwords is **not**, because both are "something you know."

MFA is one of the single most effective controls there is, because stealing your
password no longer gets an attacker in — they would also need your phone or your
fingerprint.

## Passwordless authentication

The logical next step is to drop the password entirely. **Passwordless**
authentication replaces "something you know" with a stronger combination,
typically "something you have" plus "something you are/know." Microsoft Entra
supports three main passwordless methods:

- **Windows Hello for Business** — sign in with a biometric or PIN tied to the
  specific device; the credential never leaves the hardware.
- **FIDO2 security keys** — a physical key (often USB/NFC) that uses public-key
  cryptography and is highly phishing-resistant.
- **Microsoft Authenticator app** — approve a sign-in on your phone with a number
  match and biometric, no password required.

These are both more secure *and* more convenient — there is no password to phish,
reuse or forget.

## Self-service password reset and password protection

Even with MFA, passwords still exist, so Entra ID helps manage them.

> **Self-service password reset (SSPR)** lets users reset their own forgotten
> passwords after verifying their identity with registered methods — no help-desk
> call required.

SSPR cuts support costs and gets users back to work faster, while still requiring
them to re-prove their identity. **Password protection** hardens passwords
organization-wide:

- **Banned password lists** (global and custom) block weak or easily guessed
  passwords like `Password1` or your company name.
- **Smart lockout** detects and locks out brute-force sign-in attempts while
  still letting the real user in.

## Access management: Conditional Access

Authentication proves identity; **Conditional Access** decides what to do about
it. It is the Zero Trust "verify explicitly" principle turned into a product.

> **Conditional Access** evaluates **signals** about each sign-in and then makes
> an access decision: **allow, block, or require additional controls** such as
> MFA, before granting access to an app.

Think of a Conditional Access policy as an **if-then** statement: *if* these
conditions are true, *then* enforce these controls.

Signals (the conditions) include:

- **User or group** making the request.
- **Location** (IP address / country) — is it familiar or risky?
- **Device** platform and state — is it managed and compliant?
- **Application** being accessed.
- **Real-time sign-in risk** (from Entra ID Protection).

Based on those signals, the policy can **grant** access, **block** it, or grant
it only **with conditions** — most commonly "require MFA." For example: *allow
access to the finance app, but require MFA when the user signs in from an
unfamiliar location or an unmanaged device.* That single policy is Zero Trust in
action.

## Access management: roles and RBAC

Once a user is in, what can they administer? That is controlled by **role-based
access control**.

> **Role-based access control (RBAC)** grants permissions by assigning identities
> to **roles**, where each role bundles the permissions a particular job needs.
> You manage access by role, not by hand-crafting permissions per person.

RBAC is how you implement **least privilege**: give each administrator only the
role their job requires. Entra ID ships many **built-in roles** (for example,
**Global Administrator**, **User Administrator**, **Security Reader**). A Global
Administrator has sweeping control, so it should be tightly limited — a theme the
next lesson picks up with Privileged Identity Management.

## Access management: Global Secure Access

Modern access is not only about apps — it is also about the network path to them.
**Global Secure Access** is Microsoft's identity-centric network-access offering
(a Security Service Edge, or SSE). It has two parts:

- **Microsoft Entra Internet Access** — a secure web gateway that protects access
  to internet, SaaS and Microsoft 365 apps.
- **Microsoft Entra Private Access** — Zero Trust access to private, internal
  apps **without a traditional VPN**, so users reach only the specific resources
  they are entitled to.

Together they extend Conditional Access and Zero Trust to the network itself.

## The whole thing in one paragraph

Entra ID verifies identities with **authentication factors** — something you
**know, have, or are** — and **MFA** demands two or more from *different*
categories. **Passwordless** methods (**Windows Hello for Business**, **FIDO2
security keys**, **Microsoft Authenticator**) are stronger and simpler, while
**SSPR** lets users reset forgotten passwords and **password protection** (banned
lists, smart lockout) blocks weak ones. For access, **Conditional Access**
evaluates **signals** and then allows, blocks, or requires controls like MFA;
**RBAC** grants permissions through roles for least privilege; and **Global
Secure Access** (Entra Internet Access + Private Access) secures the network path.

## Exam focus

- **MFA = two or more factors from different categories** (know / have / are).
  Two passwords is not MFA. Categories: **something you know, have, are.**
- **Passwordless methods in Entra:** **Windows Hello for Business, FIDO2 security
  keys, Microsoft Authenticator.** FIDO2 is the most phishing-resistant.
- **SSPR** = users reset their **own** forgotten passwords after verifying
  identity. **Password protection** = banned password lists + smart lockout.
- **Conditional Access** evaluates **signals** (user, location, device, app,
  risk) and decides **allow / block / require MFA**. It is "verify explicitly."
- **RBAC** assigns permissions via **roles** to achieve **least privilege**.
  **Global Secure Access** = Entra **Internet Access** + **Private Access**
  (VPN-less Zero Trust network access).
