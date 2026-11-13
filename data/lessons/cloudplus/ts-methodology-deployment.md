# Troubleshooting Methodology & Deployment Issues

When something breaks, the difference between a fast fix and a long outage is
*discipline*. This lesson covers the structured **troubleshooting methodology**
CompTIA teaches across its certifications, and then the specific failures that
plague **deployments** — the broken releases, bad templates, and quota errors that
keep a build from going live.

## The CompTIA troubleshooting methodology

CompTIA uses one consistent, ordered method. Follow it in sequence; the exam often
asks "what's the *next* step."

> 1. **Identify the problem.** Gather information, question users, reproduce the
>    issue, and note recent changes. *Most incidents follow a change* — "what
>    changed?" is the single best question.
> 2. **Establish a theory of probable cause.** Form a hypothesis; question the
>    obvious and simple first before exotic explanations.
> 3. **Test the theory to determine the cause.** Prove it. If the theory is
>    confirmed, move on; if not, form a new theory or **escalate**.
> 4. **Establish a plan of action** to resolve the problem, accounting for
>    potential side effects.
> 5. **Implement the solution** (or escalate if it's beyond your scope/authority).
> 6. **Verify full system functionality** and, where possible, implement
>    **preventive measures** so it doesn't recur.
> 7. **Document** findings, actions, outcomes, and lessons learned.

Two rules make the method work in practice:

- **Change one thing at a time** and re-test, so you know which change actually
  fixed (or broke) something.
- **Narrow the search deliberately.** **Top-down** starts at the application and
  works toward infrastructure; **bottom-up** starts at the physical/network layer
  and works up; **divide-and-conquer** starts in the middle and halves the problem
  space each step. Pick the one that reaches the fault fastest.

Documentation (step 7) isn't bureaucracy — it builds the knowledge base that makes
the next identical incident a two-minute fix, and it feeds the preventive measures.

## Troubleshooting deployment issues

Cloud deployments are automated, so when they fail the cause is usually in the
code, the template, or the account's limits — not a physical fault. Work the
categories:

### Template and configuration errors

- **Syntax and validation errors** — a malformed IaC template or YAML manifest
  (bad indentation, a missing field). Most tools offer a **validate/plan** step;
  run it before applying. The error message and line number are your first clue.
- **Misconfiguration** — valid syntax but wrong values (wrong region, wrong subnet,
  wrong instance type). Compare against a known-good environment.
- **Version mismatch** — the template targets an API, module, or image version
  that changed. Pin versions and read the provider/tool changelog.

### Dependency and ordering failures

- **Missing or circular dependencies** — a resource is created before the thing it
  needs exists (an instance referencing a security group that isn't built yet).
  Declarative tools usually resolve ordering, but explicit dependencies may be
  required.
- **Failed artifacts** — the pipeline tried to deploy an image or package that
  didn't build or isn't in the registry. Check the build stage first; a deploy can
  only be as good as its artifact.

### Capacity, quota, and permission failures

- **Service quotas / limits exceeded** — the account hit a cap (e.g., max instances
  or IP addresses in a region). The fix is a **limit-increase request**, which
  takes time — anticipate it before a big launch.
- **Insufficient capacity** — the provider has no free capacity for a specific
  instance type in a zone; try another type or zone.
- **Insufficient permissions (IAM)** — the pipeline's service account lacks a
  permission for a resource it must create. Deployment logs show an
  "access denied" / authorization error; grant the missing least-privilege
  permission rather than over-granting admin.

### When it fails mid-deploy

A partial deployment can leave resources half-created. Favor tools and pipelines
that **roll back automatically** to the last known-good state on failure, and
design deploys to be **idempotent** so a retry is safe. After fixing the root
cause, re-run the pipeline rather than hand-patching the live environment — hand
patches become tomorrow's configuration drift.

> The quickest triage for a failed deploy: **read the error in the deployment/
> pipeline log first.** Cloud deploy failures almost always emit a specific message
> (validation error, quota exceeded, access denied, dependency not found) that
> names the category — don't theorize before reading it.

### Knowing when to escalate

Step 5 of the methodology explicitly allows **escalation**, and it is a decision,
not a failure. Escalate when the fix is outside your authority (a quota increase or
a billing change only an account owner can approve), outside your scope (a
suspected provider-side outage — check the provider's **status/health dashboard**
before burning hours chasing your own config), or when an SLA clock makes getting
help faster than solving it alone. When you escalate, hand over what you already
did: the symptoms, the theories you tested and ruled out, and the exact error
text. That context is what turns an escalation into a fast resolution instead of a
restart.

Finally, treat **communication** as part of troubleshooting. Keep stakeholders
updated on impact and expected recovery, and record the timeline — both feed the
post-incident review and the documentation in step 7 that prevents the next
occurrence.

## Exam focus

- Memorize the **ordered methodology**: identify → theory of probable cause → test
  the theory → plan of action → implement (or escalate) → verify + preventive
  measures → **document**. The exam loves "what's the **next** step."
- **"What changed?"** is the highest-value question; **change one variable at a
  time**; and choose **top-down, bottom-up, or divide-and-conquer** to reach the
  fault fastest.
- Deployment failures cluster into **template/syntax errors, misconfiguration,
  version mismatches, dependency/artifact failures, quota-or-capacity limits, and
  IAM permission errors.** **Validate/plan before apply.**
- A **quota exceeded** error needs a **limit-increase request** (plan ahead); an
  **access denied** error needs a missing **least-privilege permission**, not admin.
- Prefer **automatic rollback** and **idempotent** deploys; fix the code and
  **re-run the pipeline** instead of hand-patching live resources (which causes
  drift). **Read the deployment log first** — it names the category.
