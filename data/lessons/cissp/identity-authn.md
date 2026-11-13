# Identity Lifecycle & Authentication

Identity and access management answers a deceptively simple question: *is this
subject who it claims to be, and may it do what it's asking?* This lesson covers
how identities are created, maintained, and retired (the lifecycle), and how a
subject proves itself (authentication) — including the factor rules, biometric
error rates, and Kerberos, all heavily tested.

## AAA: the backbone

Access control rests on four steps. Keep them in order.

> **Identification** — the subject claims an identity (a username). **Authentication**
> — the subject proves it (a password or token). **Authorization** — the system
> decides what the proven subject may do. **Accountability (auditing)** — actions
> are logged to the identity so they can be traced.

Identification without authentication is just a claim; authorization without
authentication is a hole. Accountability is why you never use **shared accounts**
for sensitive actions — you lose the ability to attribute what was done.

## The identity lifecycle

Identities follow a **joiner-mover-leaver (JML)** arc, and each transition is a
control point.

- **Provisioning (joiner)** — create the account and grant access that matches the
  role, under **least privilege**.
- **Mover** — when someone changes roles, grant the new access **and revoke the
  old**. Failure to revoke causes **privilege creep / aggregation**, where
  long-tenured staff accumulate excessive rights.
- **Access review / recertification** — periodically re-verify that each person's
  access is still justified. This is the control that catches privilege creep.
- **Deprovisioning (leaver)** — remove access when employment ends.

> On termination — **especially involuntary** — **disable access immediately**, in
> coordination with the notification, before the person is told where possible.
> **Disable rather than delete** the account, so data, encryption keys, and audit
> trails are preserved.

**Privileged access management (PAM)** gets special treatment: admin accounts are
vaulted, their use is monitored and recorded, and **just-in-time (JIT)** access
grants elevated rights only for a short window and then revokes them — shrinking the
standing attack surface. Distinguish account types: **user**, **privileged**,
**service** (non-human, for applications), and **shared** (avoid for anything
requiring accountability).

## Authentication factors

A subject proves identity with one or more **factors**, and the *categories*
matter more than the count.

| Factor type | Examples |
|-------------|----------|
| **Something you know** | Password, PIN, security question |
| **Something you have** | Hardware token, smart card, phone/authenticator |
| **Something you are** | Fingerprint, face, iris (biometrics) |
| *(Supplementary)* somewhere you are | Geolocation |
| *(Supplementary)* something you do | Behavior, keystroke dynamics |

> **Multifactor authentication (MFA)** requires factors from **two or more
> different categories.** A password **plus a security question is NOT MFA** —
> both are "something you know." A password plus a hardware token **is** MFA (know
> + have).

This "two of the same type isn't MFA" distinction is one of the most common IAM
questions on the exam. Password managers and **passkeys/FIDO2** (see below) are
pushing toward **passwordless, phishing-resistant** authentication. When passwords
are used, they must be stored **hashed and salted**, never in plaintext, and long
**passphrases** beat short complex passwords.

## Biometric accuracy

Biometrics are judged by two error rates whose trade-off is a guaranteed item.

- **FAR (False Acceptance Rate), a.k.a. Type II error** — an **impostor is wrongly
  accepted.** This is the **security** risk.
- **FRR (False Rejection Rate), a.k.a. Type I error** — a **legitimate user is
  wrongly rejected.** This is the **usability** problem.
- **CER / EER (Crossover / Equal Error Rate)** — the point where FAR equals FRR.
  **A lower CER means a more accurate system** and is the standard way to compare
  biometric devices.

Tuning sensitivity trades one error for the other: tighten it and FAR drops but FRR
rises (frustrated users); loosen it and the reverse. For a high-security door you
accept a higher FRR to keep FAR near zero.

## Kerberos

**Kerberos** is the classic single-sign-on authentication protocol (the heart of
Active Directory) and shows up often. Know its moving parts.

> Kerberos uses a trusted **Key Distribution Center (KDC)** with two services: the
> **Authentication Service (AS)** and the **Ticket Granting Service (TGS)**. After
> login the user gets a **Ticket Granting Ticket (TGT)**; to reach a resource the
> client presents the TGT to the TGS and receives a **service ticket**. It uses
> **symmetric** cryptography and provides **mutual authentication**.

Two tested properties: Kerberos is **time-sensitive** — all clocks must be
synchronized (typically within ~5 minutes) because timestamps defend against
**replay** attacks; and the **KDC is a single point of failure/attack**, so it must
be hardened and redundant. Kerberos runs on **port 88**.

## Single sign-on trade-offs

**SSO** lets a user authenticate once and reach many systems — great for usability
and for centralizing control, but it concentrates risk: compromise the single
credential and the attacker reaches everything. That's precisely why SSO must be
paired with **strong MFA**.

## Exam focus

- **AAA order**: identify → authenticate → authorize → account. Accountability
  dies with **shared accounts**.
- Lifecycle: provision under **least privilege**; on role change, **revoke old
  access** (prevent **privilege creep**); run periodic **access recertification**;
  on termination (especially involuntary) **disable immediately, don't delete**.
  **PAM + just-in-time** access shrink privileged exposure.
- **MFA = factors from different categories** (know/have/are). **Password + security
  question is NOT MFA.** Store passwords **hashed and salted**.
- Biometrics: **FAR (Type II) = impostor accepted = security risk**; **FRR (Type I)
  = legit user rejected = usability**; **lower CER/EER = better**.
- **Kerberos**: **KDC (AS + TGS)**, **TGT** then **service tickets**, **symmetric**,
  **mutual auth**, **time-synchronized** to stop replay; the **KDC is a single
  point of failure**. Pair **SSO with MFA**.
