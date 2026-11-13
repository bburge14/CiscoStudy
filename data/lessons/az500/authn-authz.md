# Authentication, MFA & Conditional Access

Knowing *who* a user is — authentication — is where most real-world breaches are
won or lost. Stolen passwords are cheap; the controls in this lesson are what make
a stolen password useless. We cover the authentication methods Entra ID offers,
multifactor authentication, Conditional Access as the policy engine on top, and
the risk signals that make those policies adaptive.

## Authentication methods

Entra ID can verify an identity with several factors. The exam groups them by how
phishing-resistant they are:

- **Password** — the weakest factor; something you *know*.
- **Microsoft Authenticator** — push approval or a one-time code on a phone;
  something you *have*. Number matching (approving by typing a shown number)
  defeats "MFA fatigue" prompt-bombing.
- **FIDO2 security keys** and **Windows Hello for Business** — public-key,
  **passwordless**, and **phishing-resistant**: the private key never leaves the
  device and is bound to the real site, so a fake login page gets nothing.
- **OATH hardware/software tokens** — time-based one-time codes.
- **SMS / voice call** — convenient but weakest of the second factors (vulnerable
  to SIM-swap and interception); fine as a fallback, not as the goal.

> **Passwordless is the direction of travel.** FIDO2 keys, Windows Hello, and
> passkeys in Microsoft Authenticator remove the password entirely, which removes
> the thing attackers phish.

### Protecting the password itself

- **Self-service password reset (SSPR)** lets users reset their own password after
  proving identity with registered methods — cutting helpdesk load and the risk of
  social-engineered resets. With on-premises sync, **password writeback** pushes
  the new password back to AD.
- **Entra Password Protection** blocks weak and banned passwords (a Microsoft
  global list plus your custom banned list) and can extend to on-premises AD.
- **Smart lockout** locks out brute-force attempts while telling real users and
  attackers apart, so a legitimate user isn't locked out by someone guessing.

## Multifactor authentication (MFA)

**MFA requires two or more factors from different categories** — something you
know, have, or are. It is the single highest-impact control against credential
theft. You can turn it on in three escalating ways:

- **Security defaults** — a free, all-or-nothing baseline that forces MFA
  registration and challenges risky sign-ins. Good for small tenants; no
  granularity.
- **Conditional Access policies** — the granular, recommended approach (needs
  P1). You decide exactly *when* MFA is required.
- **Per-user MFA** — the legacy method; avoid it in favor of Conditional Access.

## Conditional Access: the policy engine

**Conditional Access (CA)** is the heart of Entra authentication security. A
policy is an **if–then** statement:

> **If** these signals are true for a sign-in, **then** block it or grant it only
> after these requirements are met.

### Assignments (the "if") — signals

CA evaluates **signals** about the sign-in:

- **Users and groups** — who is signing in (and who is excluded).
- **Target resources** — which cloud app or action, e.g. the Azure management
  portal or a specific app.
- **Network / location** — named locations defined by IP range or country; often
  used for "trusted" vs "untrusted" networks.
- **Device platform and state** — iOS/Android/Windows, and whether the device is
  **compliant** (via Intune) or **hybrid joined**.
- **Client app** — browser vs legacy authentication clients (legacy auth can't do
  MFA and should be blocked).
- **Sign-in risk and user risk** — real-time and offline risk scores from Entra ID
  Protection (see below).

### Access controls (the "then")

- **Block access** — the strongest control.
- **Grant with requirements** — require MFA, a compliant device, a hybrid-joined
  device, an approved client app, an app-protection policy, or a password change.
  Multiple requirements can be combined ("require MFA **and** compliant device").
- **Authentication strength** — require a *specific* strength, e.g. only
  phishing-resistant MFA for admins.
- **Session controls** — sign-in frequency, persistent browser session,
  app-enforced restrictions, and Conditional Access App Control (via Defender for
  Cloud Apps).

A classic exam pattern: "require MFA for all admins," "block legacy
authentication," "require a compliant device for the Azure portal," and "require
MFA when sign-in risk is medium or high."

## Entra ID Protection: making policy adaptive

**Microsoft Entra ID Protection** (a **P2** feature) uses Microsoft's threat
intelligence and machine learning to score risk, then feeds those scores into
Conditional Access.

- **Sign-in risk** — the probability *this particular sign-in* isn't the real
  user (impossible travel, anonymous IP/Tor, unfamiliar sign-in properties,
  malware-linked IP).
- **User risk** — the probability the *account itself* is compromised (for
  example, credentials found in a leak).
- **Risk-based policies** — e.g. require MFA at medium sign-in risk, require a
  secure password change at high user risk, or block entirely.

The division of labor is clean: **ID Protection detects and scores risk;
Conditional Access decides what to do about it.**

## Putting it together

Authentication starts with choosing strong factors — ideally **passwordless,
phishing-resistant** ones like FIDO2 and Windows Hello — and protecting passwords
with SSPR, banned-password lists, and smart lockout. **MFA** is the baseline
everyone should reach. **Conditional Access** then wraps every sign-in in an
if–then policy over users, apps, location, device state, and risk, and decides to
block or to grant with requirements. **Entra ID Protection** supplies the risk
signals that make those decisions adaptive instead of static.

## Exam focus

- **MFA = two or more factors from different categories.** It is the top control
  against stolen passwords. Prefer **Conditional Access** over security defaults
  (all-or-nothing) and legacy per-user MFA.
- **FIDO2 and Windows Hello for Business are passwordless and phishing-resistant**;
  **SMS/voice** are the weakest second factors. Use **number matching** to stop
  MFA-fatigue attacks.
- A Conditional Access policy is **if (signals) then (controls)**. Signals include
  user/group, app, **location**, **device compliance**, client app, and **risk**.
  Controls = **block**, or **grant** requiring MFA / compliant device / hybrid
  join / specific **authentication strength**, plus **session** controls.
- **Block legacy authentication** with Conditional Access — it bypasses MFA.
- **Entra ID Protection (P2)** produces **sign-in risk** and **user risk**;
  Conditional Access consumes them in **risk-based policies**. ID Protection
  detects; Conditional Access enforces.
- **SSPR + password writeback**, **banned-password protection**, and **smart
  lockout** harden the password itself.
