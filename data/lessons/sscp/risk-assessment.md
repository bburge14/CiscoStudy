# Risk Management & Security Assessment

Security is not about eliminating risk — that's impossible — but about
*understanding* it and deciding, deliberately, what to do about it. This lesson
gives you the risk vocabulary every practitioner shares, the simple arithmetic
that turns risk into dollars, the four ways an organization can respond, and the
assessments that go out and *find* the weaknesses in the first place.

## The building blocks of risk

> A **threat** is a potential cause of harm (a hacker, malware, a flood). A
> **vulnerability** is a weakness that a threat could exploit (an unpatched
> server, a weak password). **Risk** is the intersection of the two — the
> likelihood that a threat exploits a vulnerability, and the impact if it does.

So **risk = threat x vulnerability**, weighted by **asset value**. Remove either
side and the risk drops: patch the vulnerability (no weakness to exploit) or the
threat loses its target. A few more terms:

- **Asset** — what you're protecting, and its value.
- **Likelihood** and **impact** — the two axes of every risk; a risk that is both
  likely and high-impact is your top priority.
- **Exposure** — the extent to which an asset is susceptible to loss.

## Quantitative risk analysis: putting a number on it

When you can assign dollar values, **quantitative** analysis gives a defensible
number. Memorize this chain — it's one of the most tested calculations on the
exam:

> **SLE (Single Loss Expectancy) = AV (Asset Value) x EF (Exposure Factor).**
> **ALE (Annualized Loss Expectancy) = SLE x ARO (Annualized Rate of
> Occurrence).**

Walk through it:

- **AV** — what the asset is worth (say, $100,000).
- **EF** — the fraction of value lost in one incident (say, 25% = 0.25).
- **SLE** — loss per single event = 100,000 x 0.25 = **$50,000**.
- **ARO** — how many times per year you expect it (say, 2).
- **ALE** — expected yearly loss = 50,000 x 2 = **$100,000**.

The ALE is the number you compare against the cost of a control: if a safeguard
costs $30,000/year and cuts the ALE from $100,000 to $20,000, it saves $80,000 —
worth it. **Qualitative** analysis, by contrast, uses ratings (High/Medium/Low,
or a risk matrix) instead of dollars; it's faster and works when hard numbers
aren't available, but it's subjective.

## Responding to risk

Once a risk is understood, the organization chooses one of four responses — know
all four and be able to spot each in a scenario:

| Response | What it means | Example |
|----------|---------------|---------|
| **Avoid** | Stop the risky activity entirely | Cancel the feature that created the exposure |
| **Mitigate (reduce)** | Apply controls to lower likelihood/impact | Patch, add MFA, deploy a firewall |
| **Transfer (share)** | Shift the financial impact to a third party | **Buy cyber-insurance**; outsource |
| **Accept** | Consciously tolerate the risk | Document and accept a low residual risk |

A fifth concept ties them together: **residual risk** is what remains *after*
controls are applied. You can never reach zero, so management formally **accepts**
the residual risk that's left. The acceptable amount is set by the organization's
**risk appetite (tolerance)**. The ongoing list of identified risks, their
owners, and treatment decisions lives in the **risk register**.

> Buying insurance is **transference** — it doesn't reduce the chance of an
> incident, it moves the financial loss. Applying a control is **mitigation**.
> The exam reliably tests this distinction.

## Security assessment: finding the weaknesses

You can't manage risk you haven't discovered. **Security assessments** probe
systems for weaknesses, and the two headline types are constantly contrasted:

> A **vulnerability assessment** *identifies and catalogs* weaknesses (usually via
> automated scanning) but does **not** exploit them. A **penetration test** goes
> further and *actively exploits* discovered weaknesses to demonstrate real-world
> impact.

- A **vulnerability scan** is broad, automated, and safe — it tells you what
  *might* be exploitable. An **authenticated (credentialed) scan** logs in to see
  what an insider could, finding far more than an unauthenticated one.
- A **penetration test** is narrower, often manual, and proves what an attacker
  could actually achieve. Pen tests come in **black-box** (no prior knowledge),
  **white-box** (full knowledge), and **gray-box** (partial) flavors.

Scanning produces results you must interpret:

- A **false positive** is a reported flaw that doesn't actually exist — manual
  verification shows the vulnerability isn't there. False positives waste time and
  erode trust in the tool.
- A **false negative** is a real flaw the scan *missed* — more dangerous, because
  you don't know it's there.

Finally, distinguish an **assessment** from an **audit**: an assessment is
typically an internal, improvement-focused review of control effectiveness, while
an **audit** is a more formal, often independent evaluation against a standard or
regulation, producing findings for compliance.

## Exam focus

- **Risk = threat x vulnerability**, weighted by asset value and expressed as
  **likelihood x impact.** Remove the threat *or* the vulnerability to reduce it.
- Memorize the math: **SLE = AV x EF**, **ALE = SLE x ARO.** Be ready to compute
  ALE from a word problem.
- Four risk responses: **avoid, mitigate, transfer, accept.** **Insurance =
  transference**; **a control = mitigation.** **Residual risk** is what's left;
  management **accepts** it per the **risk appetite**.
- **Vulnerability assessment = find/catalog (no exploit); penetration test =
  exploit to prove impact.** Credentialed scans see more.
- A **false positive** = reported-but-not-real; a **false negative** = real-but-
  missed (worse). An **audit** is a formal evaluation against a standard.
