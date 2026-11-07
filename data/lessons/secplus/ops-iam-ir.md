# Identity & Access, Incident Response & Forensics

This lesson covers three pillars of day-to-day security operations: deciding
**who gets in and what they can do** (identity and access management), reacting
when something goes wrong (**incident response**), and gathering evidence the
right way afterward (**digital forensics**). Access controls prevent incidents;
IR and forensics handle them when prevention fails.

## Identity and Access Management (IAM)

**IAM** is how an organization manages digital identities and what each one is
allowed to do. It spans the whole life of an account.

### The account lifecycle

- **Provisioning / de-provisioning** — create accounts when people join, and
  *promptly* disable them when people leave. A lingering account after offboarding
  is a classic breach path.
- **Permission assignments** — grant access according to the person's role,
  always aiming for **least privilege**.
- **Identity proofing** — verifying someone really is who they claim before
  issuing credentials.
- **Attestation** — periodically re-reviewing who has access to confirm it's still
  appropriate (access recertification).

### Single sign-on and federation

- **SSO (Single Sign-On)** — log in once, reach many systems. Convenient and
  reduces password fatigue, but the single login must be well protected.
- **Federation** — trusting identities from *another* organization's identity
  provider, so partners can access resources without separate accounts.
- Protocols to know: **SAML** (XML-based, common for enterprise web SSO and
  federation), **OAuth** (authorization/delegated access, "log in with..."), and
  **LDAP** (the directory protocol that stores and looks up identities).

### Access control models

How the system decides what you may access:

| Model | How access is decided |
|-------|-----------------------|
| **MAC** (Mandatory) | System-enforced by labels/clearance; users can't change it. Highest security (government) |
| **DAC** (Discretionary) | The data owner decides who gets access. Flexible, common on file shares |
| **RBAC** (Role-Based) | Access based on your job role. Scales well in business |
| **Rule-Based** | Access by rules/conditions (e.g. a firewall ACL) |
| **ABAC** (Attribute-Based) | Access by attributes (department, time, device, location). Most granular |

Add **time-of-day restrictions** (only during work hours) and always layer in
**least privilege** on top of whichever model you use.

### Multifactor authentication (MFA)

> Strong authentication combines **factors** from different categories: something
> you **know** (password/PIN), something you **have** (token/phone/security key),
> something you **are** (biometric), and somewhere you **are** (location).

The key rule: true MFA uses factors from **different categories**. A password plus
a PIN is *not* MFA — both are "something you know." Implementations include
**biometrics**, **hard and soft tokens**, and **security keys**.

### Passwords and privileged access

- **Password best practices** — reasonable **length** and **complexity**, no
  **reuse**, sensible **age/expiration** (modern guidance favors length over
  frequent forced changes).
- **Password managers** generate and store strong unique passwords.
- **Passwordless** methods (biometrics, security keys) remove the password
  weakness entirely.
- **PAM (Privileged Access Management)** protects powerful admin accounts with
  **just-in-time permissions** (elevated only when needed), **password vaulting**
  (checked out from a vault), and **ephemeral credentials** (that expire quickly).

## Incident response

When prevention fails, **incident response (IR)** is the disciplined plan for
reacting. Memorize the phases **in order** — the exam tests sequence constantly:

1. **Preparation** — build the plan, tools, and training *before* anything
   happens.
2. **Detection** — recognize that an incident is occurring (often via the SIEM).
3. **Analysis** — confirm it's real and assess scope and severity.
4. **Containment** — stop the bleeding; limit the spread (isolate hosts).
5. **Eradication** — remove the cause (delete malware, close the hole).
6. **Recovery** — restore systems to normal, cleanly.
7. **Lessons learned** — review what happened and improve, so it doesn't recur.

> A memory aid: **P-D-A-C-E-R-L**. Note the order — you **contain** *before* you
> **eradicate**, and **lessons learned** always comes last.

Supporting activities: **training** and **testing** (via **tabletop exercises**
and **simulations**), **root cause analysis** (finding the true underlying cause,
not just the symptom), and **threat hunting** (proactively searching for attackers
who haven't tripped an alert yet).

## Digital forensics

**Digital forensics** is collecting and preserving evidence so it holds up — in
court or an internal investigation. Doing it wrong can destroy the evidence's
value, so process is everything.

- **Legal hold** — a formal notice to preserve all potentially relevant data (stop
  deleting it) once litigation is anticipated.
- **Chain of custody** — a documented, unbroken record of who handled the evidence,
  when, and why. A gap can make evidence inadmissible.
- **Acquisition** — collecting the evidence, ideally a bit-for-bit **image** of the
  original, with a **hash** taken to prove it wasn't altered.
- **Preservation** — protecting the original and working only on copies.
- **Reporting** — documenting findings clearly and objectively.
- **E-discovery** — the legal process of identifying and producing electronic
  evidence.

### Order of volatility

> Collect the most **volatile** evidence first — it disappears fastest.

Rough order: **CPU registers/cache → RAM (memory) → network state → disk →
backups/archives**. Memory vanishes when power is cut, so you capture it before
pulling the plug; data on disk and backups can wait.

## The whole thing in one paragraph

**IAM** governs identities end to end — **provisioning/de-provisioning**,
least-privilege **permissions**, **identity proofing**, and **attestation** —
simplified by **SSO** and **federation** (via **SAML**, **OAuth**, **LDAP**), with
access decided by a model (**MAC**, **DAC**, **RBAC**, **rule-based**, or
**ABAC**) and strengthened by **MFA** that mixes factor *categories* (know/have/
are/where), good password practices or **passwordless**, and **PAM** for admin
accounts (just-in-time, vaulting, ephemeral credentials). When prevention fails,
**incident response** runs in order — **preparation, detection, analysis,
containment, eradication, recovery, lessons learned** — supported by testing,
root cause analysis, and threat hunting. Afterward, **digital forensics**
preserves evidence through **legal hold**, **chain of custody**, bit-for-bit
**acquisition** with hashing, careful **preservation**, **reporting**, and
**e-discovery**, always collecting the most **volatile** data first.

## On the exam

- The IR phase order is tested relentlessly: **Preparation → Detection → Analysis
  → Containment → Eradication → Recovery → Lessons Learned.** You **contain before
  you eradicate**, and lessons learned is always last.
- True **MFA** requires factors from **different categories**. Password + PIN =
  *not* MFA (both "something you know").
- Access models: **MAC** = system/labels (strictest), **DAC** = owner decides,
  **RBAC** = by role, **ABAC** = by attributes (most granular).
- **SAML** = enterprise web SSO/federation; **OAuth** = delegated authorization;
  **LDAP** = the directory itself.
- Forensics: **chain of custody** keeps evidence admissible; **legal hold** stops
  data from being deleted; collect by **order of volatility** (RAM before disk).
- **De-provisioning** promptly at offboarding is the fix for "ex-employee still
  had access."
- **PAM** with **just-in-time** access is the answer for limiting standing admin
  privilege.
