# System Hacking Concepts

This lesson covers phases three through five of the methodology — **gaining
access, maintaining access, and clearing tracks** — at the *concept* level. The
goal is recognition: you should be able to name the class of a credential attack,
explain what a post-exploitation tool does, and state the defense. We deliberately
do not walk through how to run any of this; an ethical hacker proves a weakness
exists under authorization and then helps close it.

## From access to control

Once an attacker has a foothold, three things usually follow.

> **System hacking is the sequence of gaining access, escalating privilege to gain
> more control, maintaining that access over time, and finally clearing tracks to
> hide the activity.**

The engine of most of this is **credentials**. If an attacker can get a valid
username and password (or the hash of one), many defenses simply let them in.

## Credential and password attacks (by category)

You need to recognize the *class* of attack from a description:

- **Dictionary attack** — tries a list of likely passwords.
- **Brute force** — tries every possible combination; slow but thorough.
- **Hybrid** — dictionary words plus mutations (adding numbers, symbols).
- **Rainbow table** — uses precomputed hash tables to reverse unsalted hashes fast.
  The defense is **salting** (adding a unique random value before hashing), which
  makes precomputation useless.
- **Credential stuffing** — reuses username/password pairs leaked from *other*
  breaches, betting people reuse passwords.
- **Password spraying** — tries *one* common password against *many* accounts to
  stay under lockout thresholds.

Attacks are **online** (against a live service, where lockout and rate limits
apply) or **offline** (against stolen hashes, where only compute speed matters).
Hash-cracking tools you should know *by name* include **John the Ripper** and
**Hashcat** — they attempt to recover passwords from captured hashes.

## Credential theft and abuse concepts

Modern attacks often skip cracking and steal credential material directly:

- **Mimikatz** — the best-known post-exploitation tool for pulling plaintext
  passwords, **NTLM hashes**, and **Kerberos tickets** out of the memory of the
  Windows **LSASS** process.
- **Pass-the-Hash / Pass-the-Ticket** — reuse a stolen hash or ticket to
  authenticate *without ever knowing the password*.
- **Kerberoasting** — any authenticated domain user requests Kerberos service
  tickets for accounts that have a **Service Principal Name (SPN)**, then cracks
  those tickets **offline** to recover the service account's password.
- **LLMNR/NBT-NS poisoning** — abuses legacy Windows name-resolution fallbacks to
  capture authentication material on a LAN.

> The shared lesson: credentials in memory, on the wire, and in tickets are all
> targets. Defenses aim to reduce what can be stolen and to detect reuse.

## Privilege escalation

A foothold is rarely enough; attackers want *more* rights.

| Type | Meaning |
|------|---------|
| **Vertical** | Move to a higher privilege level (user → admin/root) |
| **Horizontal** | Move sideways to another account at the same level |

Escalation typically abuses **unpatched kernel/software flaws, weak file or
service permissions, misconfigured privileged tasks, or over-broad rights**. The
defense is **least privilege**, prompt **patching**, and removing the
misconfigurations that make escalation possible.

## Maintaining access and clearing tracks

To keep control, attackers plant **backdoors**, create rogue **accounts**, or
install **rootkits** that hide their presence deep in the system. **Steganography**
(hiding data inside images or other files) can conceal tools or stolen data. To
cover up, they target the **logs** — clearing or editing event logs, disabling
auditing, and **timestomping** (falsifying file timestamps).

That is exactly why log integrity matters so much on defense: if logs can be
silently erased, the whole incident record disappears.

## The defensive playbook

Every technique above has a counter, and the exam rewards knowing them:

- **Strong, unique passwords plus MFA** — defeats stuffing, spraying and most
  cracking value.
- **Account lockout / rate limiting** — blunts online guessing.
- **Salting and strong hashing** (bcrypt, scrypt, Argon2, PBKDF2) — kills rainbow
  tables.
- **Least privilege and tiered admin** — limits escalation and lateral movement.
- **Patch management** — closes the flaws escalation relies on.
- **Credential Guard / LSASS protection** and **disabling LLMNR/NBT-NS** — reduce
  credential theft.
- **Centralized, tamper-resistant logging** forwarded to a **SIEM** — so clearing
  local logs does not erase the evidence.
- **EDR** and behavioral monitoring — to catch the tools and patterns above.

## The attacker's economy of effort

A theme ties this lesson together: attackers prefer **stealing or reusing
credentials** over noisy exploitation, because a valid login looks like legitimate
activity. That is why identity-centric defenses — MFA, least privilege, and watching
for anomalous logins and credential use — now matter as much as patching. If you
make credentials hard to steal, hard to reuse, and loud when abused, you have closed
the path that most real intrusions actually take.

## Exam focus

- **Mimikatz** extracts plaintext passwords, **NTLM hashes**, and **Kerberos
  tickets** from **LSASS** memory. **Kerberoasting** cracks **SPN** service tickets
  **offline**.
- Match the attack class: **spraying** = one password, many accounts; **stuffing**
  = reused breached credentials; **rainbow table** = precomputed hashes (beaten by
  **salting**); **brute force** = every combination.
- **Vertical vs horizontal** privilege escalation — up to higher rights vs across
  to a peer account.
- **Pass-the-Hash** authenticates with a stolen hash, no password needed.
- Maintaining access = backdoors, rootkits, steganography; clearing tracks =
  editing/clearing logs and timestomping — so **protect and centralize logs**.
- Top defenses: **MFA, least privilege, patching, salted strong hashing, account
  lockout, and tamper-resistant logging**.
