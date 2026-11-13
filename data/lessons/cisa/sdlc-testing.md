# The SDLC & Software Testing

Software doesn't become trustworthy by accident. The **systems development life
cycle (SDLC)** is the disciplined path from idea to retired system, and
**testing** is how the organization proves — before go-live — that the system
does what the business needs and nothing it shouldn't. For the auditor, the SDLC
is a sequence of control gates to review, always from the sidelines.

## The phases of the SDLC

While models differ in naming, a classic SDLC moves through these stages:

1. **Feasibility** — is the project viable and worth doing?
2. **Requirements** — define what the system must do, in business terms.
3. **Design** — specify how it will meet those requirements (architecture, data,
   interfaces, and the controls built in).
4. **Development** — build and code the solution.
5. **Testing** — verify it works and meets requirements.
6. **Implementation** — convert data, deploy, and go live.
7. **Maintenance** — operate, fix, and enhance over its life.

One economic fact dominates CISA's view of the SDLC:

> The **cost to correct a defect rises sharply** as a project moves through the
> life cycle. An error is **cheapest to fix in the earliest phases
> (requirements and design)** and most expensive once the system is in
> production. Getting requirements and design right is the highest-leverage
> control in the whole cycle.

That is why the auditor cares so much about controls early: a missing requirement
or a design flaw caught at the design review costs a conversation; the same flaw
caught after go-live can cost a re-build.

## Development approaches

Not every project follows a strict, linear path. Know the main approaches and
their trade-offs:

- **Waterfall** — sequential phases, each completed before the next begins.
  Predictable and well-documented, but inflexible if requirements change late.
- **Agile / iterative** — build in short increments with continuous user feedback.
  Flexible and fast to deliver value, but demands strong discipline to keep
  documentation and controls from lagging.
- **Prototyping** — build a quick working model to refine requirements; the risk
  is an unfinished prototype being rushed into production.
- **RAD (rapid application development)** — compressed timelines using tools and
  reusable components.

The auditor doesn't mandate a methodology, but does check that whatever approach
is used still produces the control essentials: approved requirements, design
reviews, testing, and change control.

## Testing: proving it works

Testing moves from the smallest pieces up to the whole system in the hands of its
users. Know the levels and their order.

| Test level | What it checks | Who typically runs it |
|------------|----------------|-----------------------|
| **Unit testing** | Individual programs/modules in isolation | Developers |
| **Integration testing** | Modules working together, interfaces between them | Developers/testers |
| **System testing** | The complete system against its specifications | Testers |
| **User acceptance testing (UAT)** | The system meets **business requirements** | **End users** |

> **UAT is the final gate before go-live.** It is performed **by end users** to
> confirm the system meets the **business requirements** — not merely that the
> code runs. Sign-off from the business, not from IT, is what UAT provides.

Two more testing ideas appear frequently:

- **Regression testing** — re-running tests after a change to confirm that the
  change didn't break something that previously worked. Essential whenever code
  is modified.
- **Test data and environments** — testing should use a separate environment with
  representative data; using *live production data* for testing raises
  confidentiality concerns and usually calls for masking or sanitizing sensitive
  values.

Two further distinctions worth recognizing: **white-box** testing examines the
internal logic and code paths (the tester can see inside), while **black-box**
testing checks inputs and outputs without knowledge of the internals (as a user
would). And **functional** testing confirms the system does what it should, while
**non-functional** testing covers qualities like performance, load, and security.

## Controls the auditor expects

Two structural controls recur across every development effort:

> **Separate development, test, and production environments**, and never let
> developers hold update access to production. This enforces segregation of duties
> across the build-and-release path: code is written in development, proven in
> test, and promoted to production by a separate function.

And the auditor's own posture stays constant:

> The appropriate role of the IS auditor during development is to **review
> controls and risks at each phase in an advisory capacity, without assuming
> management responsibilities** or making the project's decisions. Reviewing early
> and throughout — rather than only at the end — is how the auditor adds the most
> value while preserving independence.

Think of the SDLC like building a house: it is far cheaper to redraw a blueprint
(requirements/design) than to move a load-bearing wall after the house is built
(production). The auditor is the inspector who reviews at each stage — foundation,
framing, wiring — not the contractor who swings the hammer.

## Exam focus

- Defects are **cheapest to fix in requirements/design (earliest phases)** and
  costliest in production — so controls early matter most.
- Know the approaches: **waterfall** (sequential), **agile/iterative**
  (incremental with feedback), **prototyping**, **RAD**.
- Testing order: **unit → integration → system → UAT**. **UAT is run by end users
  to confirm business requirements** and is the **final gate before go-live**.
- **Regression testing** re-checks that a change didn't break existing function;
  avoid using **live production data** for testing without masking.
- Keep **development, test, and production separate**, with no developer update
  access to production. The auditor reviews controls at each phase **advisorily**,
  never taking management decisions.
