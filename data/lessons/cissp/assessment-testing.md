# Assessment Strategies & Security Testing

Controls that are never tested are controls you only *hope* work. Domain 6 is about
verification: choosing the right kind of assessment, running the right tests, and
doing it with proper authorization. CISSP tests the vocabulary precisely — the gap
between "find the weakness" and "prove it can be exploited" is a favorite trap. This
lesson covers assessment strategies and the hands-on testing techniques.

## Assessment, testing, and audit

Three related words with distinct meanings:

> A **security test** exercises a specific control to see whether it works. A
> **security assessment** is a broader review of controls, often combining tests,
> interviews, and documentation review. A **security audit** is a formal,
> structured evaluation — frequently by an **independent third party** — against a
> standard, producing an opinion others can rely on.

Independence matters: the more an outside party you don't control performs the
work, the more trustworthy the result is to customers and regulators.

## Vulnerability assessment vs penetration testing

This distinction is the single most tested idea in the domain.

> A **vulnerability assessment** **finds and reports** weaknesses (usually with
> scanners) but does **not** exploit them. A **penetration test** goes further: it
> **actively exploits** weaknesses to demonstrate their real-world impact and show
> how far an attacker could get.

If management wants to know "what's wrong," run a vulnerability assessment. If they
want proof of "what an attacker could actually do," run a penetration test — and
only with explicit written authorization.

### Penetration test knowledge levels and teams

Pen tests are classified by how much the tester knows up front:

| Type | Tester's knowledge | Mimics |
|------|-------------------|--------|
| **Black box** | None (zero-knowledge) | An external attacker |
| **White box** | Full (source, architecture) | An insider / thorough review |
| **Gray box** | Partial | A user with some access |

And by team color: the **red team** attacks, the **blue team** defends, and the
**purple team** is the collaboration that feeds red-team findings back to the blue
team to improve defenses. A pen test always needs **rules of engagement**: defined
**scope**, timing, and — above all — **written authorization**, or the testers are
simply committing crimes.

## Security testing techniques

For software and systems, know which technique applies when.

- **SAST (Static Application Security Testing)** — analyzes **source code without
  executing** it. It is **white box**, runs **early in the SDLC**, and finds flaws
  like injection patterns and hardcoded secrets before the app even runs.
- **DAST (Dynamic Application Security Testing)** — tests the **running
  application** from the outside (**black box**), finding runtime and configuration
  issues SAST can't see.
- **IAST (Interactive)** — instruments the running app to combine both views.
- **Fuzzing** — bombards inputs with malformed, unexpected, or random data to
  trigger crashes and reveal input-handling bugs.
- **Manual code review** — human inspection of code (peer review); slow but catches
  logic flaws tools miss.
- **Misuse case testing** — tests what an attacker might do, not just intended use.
- **Interface testing** — verifies APIs and integration points behave securely.

> The cleanest cue: "analyze **source** code **without running** it, early" = SAST
> (white box). "Test the **running** app" = DAST (black box). "Throw malformed
> input to find crashes" = fuzzing.

## Vulnerability scanning details

Scanning underpins vulnerability assessments. Two tested nuances:

- **Authenticated (credentialed)** scans log in to the target and see far more
  (missing patches, local config) than **unauthenticated** scans, which see only
  what an outsider sees. Credentialed scans give fewer false positives.
- Findings are prioritized with **CVSS (Common Vulnerability Scoring System)**
  scores, but a raw CVSS number is not the whole story — a critical finding on an
  isolated test box may matter less than a medium one on an internet-facing crown
  jewel. Context and asset value refine the priority.

## Testing the human and process layers

Assessment isn't only technical. Mature programs also run:

- **Security control testing** across administrative and physical controls, not
  just technical ones.
- **Social-engineering tests** (phishing simulations) to measure human
  susceptibility.
- **Tabletop exercises** that walk through incident and continuity plans on paper.

> The risk-manager framing: choose the assessment that answers the *business
> question* at an acceptable risk. You don't pen-test a fragile production system
> at peak hours when a credentialed scan plus a maintenance-window test would
> answer the question more safely.

## Monitoring real behavior: synthetic vs real-user

Testing also means watching production behave over time, not just probing it once.
Two complementary techniques appear on the exam:

- **Synthetic transactions (synthetic monitoring)** — scripted, simulated
  transactions run against an application on a schedule to verify availability and
  performance proactively, often catching a problem before a real user does.
- **Real User Monitoring (RUM)** — passively captures actual user interactions to
  measure real-world experience and surface issues scripted checks miss.

Used together they answer "does the system actually work as intended?" continuously,
complementing the point-in-time tests above.

## Exam focus

- **Vulnerability assessment = find and report** (no exploitation). **Penetration
  test = actively exploit** to demonstrate impact — and needs **written
  authorization** and defined **rules of engagement/scope**.
- Pen-test knowledge: **black box** (no knowledge, external attacker), **white box**
  (full knowledge), **gray box** (partial). **Red = attack, blue = defend, purple =
  collaborate.**
- **SAST** = source, not executed, early, white box; **DAST** = running app, black
  box; **fuzzing** = malformed input to find crashes; **IAST** = instrumented
  hybrid.
- **Credentialed/authenticated scans** see more and yield fewer false positives
  than unauthenticated ones; prioritize with **CVSS** tempered by asset context.
- An **audit** (independent third party) carries more weight than a self-run test;
  pick the assessment that answers the business question **safely**.
- **Synthetic transactions** = scripted checks run proactively; **RUM** = passive
  capture of real user activity. Use both to monitor production.
