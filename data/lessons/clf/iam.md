# Identity and Access Management (IAM)

Every action in AWS — launching a server, reading a file, deleting a database — is
a request that must be authorized. The service that decides *who can do what* is
**AWS Identity and Access Management (IAM)**. Get IAM wrong and you either lock
yourself out or, far worse, leave the door open. This lesson covers the building
blocks and the rules that decide every request.

## Authentication vs. authorization

Two words that sound alike but mean different things:

- **Authentication** is proving *who you are* — signing in with a password, an
  access key, or a second factor.
- **Authorization** is deciding *what you're allowed to do* once you're in —
  governed by policies.

IAM handles both. You authenticate as some identity, then IAM authorizes each
request against the policies attached to that identity.

## The root user: powerful and dangerous

When you first create an AWS account, you get the **root user** — the email
address you signed up with. It has **complete, unrestricted access** to
everything, including billing and the ability to close the account.

> Because the root user can do *anything*, you should **not use it for everyday
> tasks.** Secure it with a strong password and **MFA**, then lock it away and work
> as a limited IAM identity instead.

A handful of rare tasks genuinely require root (like changing the account's
root email or password, or closing the account), but day-to-day work should never
touch it.

## The IAM building blocks

Four pieces do most of the work. Learn how they relate.

| Element | What it is |
|---------|------------|
| **User** | A permanent identity for one person or application — has long-term credentials (password and/or access keys). |
| **Group** | A collection of users that share a set of permissions. Attach a policy to the group, and every member inherits it. |
| **Role** | An identity with permissions that is **assumed temporarily** — it has **no long-term credentials**. Used by services, EC2 instances, and federated users. |
| **Policy** | A **JSON document** that lists permissions (allow or deny specific actions on specific resources). Policies are what actually grant access; you attach them to users, groups, or roles. |

> **Groups** are the clean way to manage people: put users in a group and assign
> the group's policy, rather than attaching policies to each user one by one.
> Note a group is *not* an identity you can log in as — it's just a container for
> permissions.

### Policies in brief

A policy is JSON that says, in effect, "Allow (or Deny) these **actions** on these
**resources**, optionally under these **conditions**." You rarely write them from
scratch at this level — AWS provides many **managed policies** (like
`AmazonS3ReadOnlyAccess`) you can attach directly.

## Roles and federation: access without passwords

Roles are the concept beginners find trickiest, so slow down here. A **role** is a
set of permissions that an entity *assumes* to get **temporary credentials**,
instead of logging in as a user with a stored password.

Where roles shine:

- **For AWS services** — an EC2 instance that needs to read from S3 is given a
  role, so your application never has to store access keys on the server. This is
  the recommended, secure pattern.
- **For cross-account access** — let a user in one account assume a role in
  another.
- **For identity federation** — let people who already have identities elsewhere
  (your corporate directory, Google, etc.) sign in to AWS.

> **Identity federation** lets users authenticate with an **existing external
> identity provider** and **assume an IAM role for temporary credentials**, so you
> don't create a separate IAM user for everyone. "Use our existing corporate
> logins, no new AWS passwords" = federation via roles.

### IAM Identity Center

For managing **workforce** access across many AWS accounts, AWS offers **IAM
Identity Center** (the successor to the service formerly called **AWS Single
Sign-On / AWS SSO**). It gives employees one sign-on to all the accounts and
applications they're entitled to, and it connects to your existing identity
source. If a scenario is about central single sign-on for a team across multiple
accounts, think IAM Identity Center — and remember the old name "AWS SSO" refers
to the same thing.

## Multi-factor authentication

A password alone can be phished or guessed. **Multi-factor authentication (MFA)**
adds a second factor — a code from an app or hardware device — so that:

> With **MFA** enabled, a stolen password **alone is not enough** to sign in; the
> attacker would also need the second factor. Enable MFA on the root user and all
> privileged identities.

MFA is one of the single highest-value security steps on the whole exam. Whenever
an answer is "protect the account even if the password leaks," it's MFA.

## How IAM decides: the evaluation rules

When a request comes in, IAM applies a consistent logic. Two rules matter at this
level:

1. **Default deny (implicit deny).** If nothing explicitly allows an action, it is
   denied. Permissions are not granted unless a policy says so.
2. **Explicit deny always wins.** If *any* policy explicitly denies the action, it
   is denied — even if another policy allows it.

> The precedence to memorize: **an explicit Deny overrides any Allow.** If a user
> is allowed S3 access by a group policy but another attached policy explicitly
> denies a specific bucket, access to that bucket is **denied.**

Put simply: you need an explicit allow *and* no explicit deny to be permitted.

## Least privilege

The guiding principle behind all of this is **least privilege**: grant each
identity only the permissions it needs to do its job, and nothing more. Start with
no access and add what's required, rather than granting broad access and trying to
claw it back. Least privilege limits the blast radius if a credential is ever
compromised.

## The whole thing in one paragraph

**IAM** controls who can do what in AWS. The all-powerful **root user** should be
locked away behind MFA and used almost never; day-to-day work happens as **IAM
users** (ideally organized into **groups**) or through **roles** that grant
**temporary credentials** to services and to **federated** external identities.
**Policies** (JSON) actually grant the permissions, evaluated by two rules —
**default deny** and **explicit deny overrides allow** — all guided by **least
privilege**, with **MFA** adding a second factor so a stolen password isn't enough.
For workforce single sign-on across many accounts, use **IAM Identity Center**
(formerly AWS SSO).

## Exam focus

- **Root user** = unlimited power; **don't use it daily**, enable **MFA**, and lock
  it away. Work as limited IAM identities instead.
- **User** = permanent identity with long-term credentials; **group** = a
  permissions container for users (not something you log in as); **role** =
  assumed for **temporary** credentials, no stored password; **policy** = the JSON
  that grants access.
- **Roles** are the secure way to give **EC2/services** and **cross-account** or
  **federated** users access without embedding access keys.
- **Identity federation** = sign in with an **existing external identity provider**
  and assume a role for temporary credentials.
- **MFA** means a **stolen password alone won't get in** — the top "protect even
  if the password leaks" answer.
- Evaluation: **default deny**, and **an explicit Deny overrides any Allow.**
- Follow **least privilege** — grant only what's needed.
- **IAM Identity Center** (formerly **AWS SSO**) handles workforce single sign-on
  across multiple accounts.
