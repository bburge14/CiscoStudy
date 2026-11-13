# Authentication & the Authentication Factors

Access control starts with a simple question: *are you who you claim to be?*
Answering it well is the heart of this lesson. We'll separate the four AAA steps
that people constantly blur together, work through the authentication **factors**
and how to combine them, measure **biometrics** honestly, and trace how
**Kerberos** and the **AAA protocols** carry authentication across a network.

## Identification, authentication, authorization, accounting

These four are a pipeline, and the exam expects you to keep them distinct:

> **Identification** is making a claim ("I am user jsmith").
> **Authentication** is proving that claim (a password, a token, a fingerprint).
> **Authorization** is deciding what the proven identity may do.
> **Accounting** (auditing) is recording what they did.

Together these are **AAA** (authentication, authorization, accounting), with
identification as the entry step. A username **identifies**; a password
**authenticates**. Don't call a username an authentication method.

## The authentication factors

Authentication relies on **factors** — categories of evidence. The three classic
ones, plus two often listed:

| Factor | Means | Examples |
|--------|-------|----------|
| **Something you know** | Knowledge | Password, PIN, security question |
| **Something you have** | Possession | Smart card, hardware token, phone |
| **Something you are** | Inherence (biometric) | Fingerprint, iris, face |
| *Somewhere you are* | Location | GPS/geolocation, IP region |
| *Something you do* | Behavior | Typing rhythm, gait |

> **Multi-factor authentication (MFA)** requires evidence from **two or more
> different factor categories.** A password plus a one-time code from a token is
> MFA. A password plus a security question is **not** — both are "something you
> know."

That last point is a favorite trap: two of the *same* factor is not multi-factor,
no matter how many you stack. MFA matters because it defeats stolen passwords
alone — the attacker also needs the second factor.

## Biometrics and their error rates

Biometrics authenticate "something you are." Because a fingerprint is never read
identically twice, biometric systems are tuned with a threshold, and that
threshold trades off two errors you must know cold:

> **FAR (False Acceptance Rate)** is how often an *impostor is wrongly accepted* —
> a **Type II error**, the dangerous one. **FRR (False Rejection Rate)** is how
> often a *legitimate user is wrongly rejected* — a **Type I error**, the annoying
> one.

- Lower the threshold (more permissive) -> FRR falls but FAR rises.
- Raise the threshold (more strict) -> FAR falls but FRR rises.
- The **Crossover Error Rate (CER)**, also called the **Equal Error Rate (EER)**,
  is the point where FAR equals FRR. **Lower CER = better-performing system**, and
  it's the fairest single number for comparing biometric products.

Remember: **FAR is acceptance (Type II, security risk); FRR is rejection (Type I,
usability nuisance); CER is where they meet.**

## Tokens and one-time passwords

A hardware or software **token** provides "something you have," usually as a
rotating **one-time password (OTP)**. Two algorithms, two standards:

- **HOTP — HMAC-based One-Time Password (RFC 4226).** The moving factor is an
  **event counter**; the code changes each time you press the button and stays
  valid until used.
- **TOTP — Time-based One-Time Password (RFC 6238).** The moving factor is the
  **current time**, typically in **30-second** windows; the code expires on its
  own. TOTP is what authenticator apps use, and it builds directly on HOTP.

Both derive the code with **HMAC** from a shared secret. The distinction to
memorize: **HOTP = counter/event (RFC 4226); TOTP = time (RFC 6238).**

## Single sign-on and Kerberos

**Single sign-on (SSO)** lets a user authenticate once and then reach many
systems without re-entering credentials. It's convenient and centralizes
authentication — but it also concentrates risk, so SSO should be paired with MFA.

The classic enterprise SSO protocol is **Kerberos**, the default authentication in
Active Directory. It uses **symmetric-key** cryptography and a trusted third party,
and runs on **port 88**.

> The **Key Distribution Center (KDC)** contains an **Authentication Server (AS)**
> and a **Ticket-Granting Server (TGS)**. The AS authenticates the user and issues
> a **Ticket-Granting Ticket (TGT)**. The user later presents the TGT to the TGS
> to obtain **service tickets** for individual resources.

Because tickets are **time-stamped**, Kerberos depends on reasonably synchronized
clocks (default tolerance is about five minutes); large clock skew breaks it. The
exam loves "which component issues the initial TGT?" — the answer is the **AS**
inside the KDC.

## AAA protocols on the network

When authentication must happen against a central server (for VPNs, Wi-Fi, admin
logins), one of these carries it:

- **RADIUS** — UDP-based (auth/acct ports **1812/1813**), encrypts only the
  password, widely used for network access and 802.1X.
- **TACACS+** — Cisco-originated, **TCP port 49**, encrypts the *entire* payload,
  and separates authentication, authorization, and accounting; favored for
  device administration.
- **Diameter** — a more modern successor to RADIUS used in telecom/mobile.

A quick contrast the exam uses: **TACACS+ encrypts the whole packet and uses TCP;
RADIUS encrypts only the password and uses UDP.**

## Exam focus

- Keep the pipeline straight: **identify** (claim) -> **authenticate** (prove) ->
  **authorize** (permit) -> **account** (log). A username identifies; a password
  authenticates.
- **Factors**: know, have, are (plus *where you are*, *what you do*). **MFA = two
  or more different categories.** Password + security question is **not** MFA.
- Biometrics: **FAR = false acceptance = Type II** (security risk); **FRR = false
  rejection = Type I** (nuisance); **CER/EER** is where they're equal — **lower is
  better.**
- **HOTP = RFC 4226, counter/event-based; TOTP = RFC 6238, time-based (~30s).**
- **Kerberos**: symmetric, port **88**, **KDC = AS + TGS**; the **AS issues the
  TGT**; it's time-sensitive (clock sync required).
- **RADIUS** (UDP, encrypts only the password) vs **TACACS+** (TCP 49, encrypts
  the whole payload, AAA separated).
