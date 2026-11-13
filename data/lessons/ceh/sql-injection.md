# SQL Injection

SQL injection has been near the top of every web-risk list for two decades because
the root cause is so common: an application builds a database query by gluing user
input directly into it. This lesson classifies the injection types the exam tests
and, as always, treats them conceptually — the point is to recognize the class and
know that **parameterized queries** are the fix, not to write attack strings.

## What SQL injection is

> **SQL injection (SQLi) is supplying input that a web application unsafely places
> into a database query, so the input is interpreted as SQL commands rather than
> data.** The root cause is mixing untrusted data with query code.

A classic illustration is an authentication bypass: if a login query concatenates
the username and password fields, crafted input that makes the query's condition
**always evaluate true** can log an attacker in without valid credentials. The
takeaway is conceptual — data and code were never separated — not the specific
string that does it.

## The types of SQL injection

CEH expects you to match a description to the injection class.

### In-band (results come back in the response)

- **Error-based** — provokes database error messages that leak data or structure.
- **Union-based** — uses the SQL `UNION` operator to append the results of an
  attacker's query onto the application's own results.

### Blind / inferential (no direct data in the response)

When the app returns no data or errors, attackers *infer* answers one bit at a
time:

- **Boolean-based blind** — crafts conditions that change the page between two
  observable states (true vs false) to read data indirectly.
- **Time-based blind** — makes the database **pause** on a true condition, reading
  data from how long the response takes.

### Out-of-band

> **Out-of-band SQLi** is used when results cannot return in the HTTP response: the
> attacker makes the database send the stolen data to an attacker-controlled server
> over a side channel such as **DNS or HTTP**.

### Second-order (stored)

> **Second-order (stored) SQL injection** occurs when malicious input is safely
> stored on first submission but is later used unsafely by a **different query**, so
> the injection **fires during a subsequent operation** rather than at the moment of
> input.

Second-order is dangerous precisely because the input looked harmless when it
arrived — the vulnerability is in the later, trusting query.

## Impact and tooling

A successful SQLi can read or modify data, bypass authentication, and in some
configurations reach the underlying OS. For recognition: **sqlmap** is the
widely-known tool that automates the detection and exploitation of SQL injection in
authorized testing. Name it and move on; the exam cares that you know what it does.

## Defending against SQL injection

The defenses form a clear hierarchy, and the top one is non-negotiable:

- **Parameterized queries / prepared statements** — the primary, definitive fix.
  They send the query structure and the user data **separately**, so input can
  never be parsed as SQL. If a question asks the single best defense, this is it.
- **Stored procedures** — effective *when written to use parameters*, not dynamic
  SQL.
- **Input validation / allowlisting** — accept only expected formats; defense in
  depth, not a substitute for parameterization.
- **Least-privilege database account** — the app's account should hold only the
  rights it needs, so a successful injection does less damage.
- **Error handling** — return generic errors so the app does not leak structure
  (which directly blunts error-based SQLi).
- **A WAF** — filters many known patterns as an additional layer, but code-level
  fixes come first.

> One sentence to remember: **SQL injection exists because data and code are mixed,
> and parameterized queries fix it by keeping them apart.**

## Why vulnerable queries exist

The flaw is architectural, not accidental: the application treats a query as one
long string and pastes user input into the middle of it. The database then has no
way to tell where the developer's command ends and the user's data begins — so data
that happens to look like SQL is executed as SQL. Parameterized queries remove the
ambiguity by sending the command template and the values on separate channels, so
the database always knows which is which.

Think of a paper form with fixed printed questions and blank boxes for answers.
Concatenation erases the line between question and box, letting someone write new
questions into the answer box; parameterization keeps the printed questions and the
answer boxes permanently separate.

## What a successful injection exposes

Depending on the database account's rights, SQLi can read entire tables (credentials,
personal data), modify or delete records, bypass authentication, and — where the
account is over-privileged — reach stored procedures that touch the operating
system. This is exactly why a **least-privilege database account** limits the blast
radius even when a query is vulnerable. Modern **ORMs and query builders**
parameterize automatically and are a strong default, but they still offer raw-SQL
"escape hatches" that reintroduce the risk if used carelessly.

## Exam focus

- **SQLi** = untrusted input interpreted as SQL because data and query code are
  concatenated.
- Match the class: **error-based** (leaks via errors), **union-based** (`UNION`
  appends results), **boolean-blind** (true/false page states), **time-based blind**
  (response delay), **out-of-band** (exfil via **DNS/HTTP**), and **second-order/
  stored** (stored safely, fires in a **later** query).
- **Parameterized queries / prepared statements** are the **single best defense** —
  they separate data from code. Add least-privilege DB accounts, input validation,
  safe stored procedures, and a WAF for depth.
- **sqlmap** is the tool that automates SQLi in authorized assessments.
