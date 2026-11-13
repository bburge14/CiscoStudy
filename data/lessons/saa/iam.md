# IAM: Identities, Roles & Access Control

Every AWS exam question that starts with "who is allowed to do what" lands here.
AWS Identity and Access Management (IAM) is the front door to every service, and
the Solutions Architect exam tests whether you can grant *exactly* the access a
workload needs — no more — using the right mechanism. This lesson walks through
how IAM makes decisions, the identities you attach permissions to, and the
federation and analysis tools that scale access across many accounts.

## How IAM decides: the evaluation order

IAM permissions are expressed as JSON **policies** made of statements, each with an
`Effect` (Allow or Deny), one or more `Action`s (like `s3:GetObject`), and the
`Resource`s they apply to. When a principal makes a request, AWS collects every
policy that could apply and runs a fixed decision process.

> **The golden rule: an explicit `Deny` always wins. Access is granted only if
> some policy explicitly allows it and nothing explicitly denies it. With no
> matching allow, the default is an implicit deny.**

So the precedence is: **explicit Deny → explicit Allow → implicit (default)
deny.** If one policy allows `s3:DeleteObject` and another attached to the same
user denies it, the request is denied — it does not matter which was attached
last, or that an allow exists "somewhere."

- **Identity-based policies** attach to a user, group, or role and say what *that
  identity* can do.
- **Resource-based policies** attach to a resource (an S3 bucket policy, an SQS
  queue policy) and say *who* may use it. These are how you grant another AWS
  account access without making anything public.
- **Permissions boundaries** and **Service Control Policies** set a *ceiling* —
  they never grant anything, they only cap what an identity could ever be allowed.

## The identities you grant to

| Identity | What it is | Typical use |
|----------|-----------|-------------|
| **Root user** | The account owner, unlimited power | Almost never — lock it down |
| **IAM user** | A long-lived identity with a password and/or access keys | A specific human or legacy app |
| **IAM group** | A bucket of users sharing policies | Apply "Developers" permissions once |
| **IAM role** | A set of permissions assumed temporarily, with no stored credentials | EC2, Lambda, cross-account, federation |

### Roles are the architect's favorite tool

A **role** has a policy for *what it can do* and a **trust policy** for *who may
assume it*. Assuming a role hands back short-lived credentials from **AWS STS**
(Security Token Service), so nothing long-lived is ever stored on a server.

> **When an application on EC2 needs to call AWS, attach an IAM role to the
> instance (an instance profile). Never bake access keys into the AMI, user data,
> or code.** The same principle covers Lambda execution roles and ECS task roles.

For **cross-account** access, create a role in the target account whose trust
policy names the calling account; the application in account A assumes the role in
account B with STS and gets temporary credentials. No permanent keys cross the
boundary. When the party assuming the role is an outside **third-party SaaS
vendor**, add an agreed **external ID** condition to the trust policy — this
blocks the "confused deputy" problem where another customer of that vendor tricks
it into using your role.

## Writing least-privilege policies

The exam rewards the *narrowest* answer. A policy granting `Action: "*"` on
`Resource: "*"` is the classic finding to remediate.

- **Least privilege** — scope every statement to only the actions and resources
  actually required, then widen only if something breaks.
- **MFA conditions** — require `aws:MultiFactorAuthPresent` to be `true` for
  sensitive actions (deleting production resources, for example) so a stolen
  password alone cannot trigger them.
- **Permissions boundary** — when you let developers create their own roles, attach
  a boundary so the roles they build can never exceed a defined maximum, even if
  the developer writes an over-broad policy.

### Protect the root user

The root user should be treated like a fire-alarm key.

> **Root user best practice: enable MFA on it, delete its access keys, and do all
> day-to-day work as an IAM principal with only the permissions needed.**

## Scaling access across accounts and users

Real environments have dozens of accounts and thousands of workforce users. Match
the scenario to the service:

- **AWS Organizations + Service Control Policies (SCPs)** — organization-wide
  guardrails attached to an OU or account. An SCP *restricts* what IAM principals
  in that account can do; it never *grants* access on its own. If an SCP denies a
  service, no policy inside the account can re-enable it.
- **AWS IAM Identity Center** (successor to AWS SSO) — lets workforce users sign in
  once with your corporate directory and receive federated, temporary access to
  many accounts through permission sets. This is the answer for enterprise
  single sign-on across Organizations.
- **Amazon Cognito user pools** — a sign-up/sign-in directory for *your
  application's* end users, including social logins (Google, Apple). Cognito is
  for app users, not for your own employees managing AWS.
- **IAM Access Analyzer** — continuously inspects resource policies and reports
  which buckets, roles, and KMS keys are shared with external accounts or the
  public, so unintended external access is caught early.

A quick way to keep the last three straight: **Identity Center = your workforce**,
**Cognito = your app's customers**, **Access Analyzer = who can see in from
outside**.

## A worked example

An application in a production account must read a DynamoDB table in a separate
security account, with no long-lived credentials. The right design: create a role
in the security account whose trust policy trusts the production account, grant it
read-only DynamoDB permissions, and have the application assume it with STS. Short-
lived credentials, scoped to one table, revocable at any time — a textbook secure
answer.

## Exam focus

- Decision logic: **explicit Deny > Allow > implicit deny.** An explicit deny can
  never be overridden; with no allow, the request is denied by default.
- EC2/Lambda calling AWS → **attach an IAM role**, never embed access keys.
- Cross-account access → a **role assumed via STS**; for a **third-party vendor**
  add an **external ID** condition to the trust policy.
- **Permissions boundary** caps what a created role can do; **SCPs** are
  Organization guardrails that restrict but never grant.
- Enterprise SSO across many accounts → **IAM Identity Center**. App end-user
  sign-in with social providers → **Amazon Cognito user pools**.
- Find resources shared externally → **IAM Access Analyzer**. Require MFA for an
  action → condition on **`aws:MultiFactorAuthPresent`**.
- Root user → **enable MFA, remove access keys, use an IAM admin** for daily work;
  everywhere else apply **least privilege**.
