# Application & Workload Identities

People are not the only things that sign in. Scripts, web apps, functions, and
pipelines all need to authenticate to call Azure APIs — and the worst way to let
them is to paste a password or key into code. This lesson covers **workload
identities**: how applications get their own identity in Entra ID, and how
**managed identities** let Azure resources authenticate with no secret to steal.

## Applications, registrations, and service principals

When you build an app that integrates with Entra ID, two related objects appear:

- The **application registration** — the global *definition* of the app: its
  name, redirect URIs, the permissions it requests, and its credentials. There is
  one registration, in the app's home tenant.
- The **service principal** — the local *instance* of that app in a tenant: the
  identity that actually gets role assignments and signs in. An **enterprise
  application** in the portal is the service principal's face.

> Think of the **app registration as the blueprint** and the **service principal
> as the running identity** created from it. Role assignments and sign-in activity
> attach to the service principal.

A service principal authenticates with a **credential**:

- A **client secret** — a string, effectively a password. It expires and, worse,
  can be copied; treat it as sensitive and rotate it.
- A **certificate** — a public/private key pair; stronger than a secret because
  the private key can stay in hardware or Key Vault.

The problem is that *something* still has to hold that secret or certificate. That
is exactly what managed identities solve.

## Managed identities: no secret to leak

> A **managed identity** is a service principal that **Azure creates and manages
> for you**, whose credentials Azure rotates automatically and **never exposes**.
> Your code asks the platform for a token; there is no secret in your source,
> config, or Key Vault.

This is the single most important workload-identity concept on the exam. Any time
a question says "authenticate an Azure resource to another Azure service **without
storing credentials**," the answer is a managed identity.

Two flavors:

| | **System-assigned** | **User-assigned** |
|---|---|---|
| Lifecycle | Tied to one resource; deleted with it | Standalone resource; independent lifecycle |
| Sharing | One resource only | Can be assigned to **many** resources |
| Use when | A single resource needs its own identity | Several resources should share one identity, or the identity must outlive a resource |

The flow is simple: enable a managed identity on, say, a VM or Function App; give
that identity an **RBAC role** on the target (for example **Key Vault Secrets
User** on a vault, or **Storage Blob Data Reader** on a storage account); then the
code calls the **Instance Metadata Service** / Azure Identity SDK to get a token.
No password anywhere.

## Permissions, consent, and app roles

Applications request access to APIs (Microsoft Graph, your own APIs) through
**permissions**, and someone has to **consent**:

- **Delegated permissions** act **on behalf of a signed-in user** and are bounded
  by what that user can do.
- **Application permissions** act as the **app itself**, with no user present —
  used by daemons and background jobs, and more powerful, so they always require
  **admin consent**.
- **User consent** can be allowed for low-risk permissions; risky ones need an
  administrator. Restricting user consent (and using an **admin consent workflow**)
  stops "illicit consent grant" attacks where a malicious app tricks users into
  approving broad access.
- **App roles** let your application define its own roles and have Entra ID stamp
  them into tokens for authorization inside the app.

## Workload identity federation

Even service-principal certificates are a secret to manage. **Workload identity
federation** removes them for external workloads: you configure a **federated
credential** that trusts tokens from an external issuer — such as GitHub Actions,
Azure DevOps, Kubernetes, or another cloud — so the pipeline presents its *own*
token and exchanges it for an Entra token. The result is **no stored secret** for
CI/CD authenticating to Azure. It is the external-workload counterpart to managed
identities (which cover workloads running *inside* Azure).

## Protecting workload identities

Non-human identities deserve the same scrutiny as users:

- **Conditional Access for workload identities** can restrict a service principal
  to trusted network locations and block it elsewhere (a P-tier feature).
- **Entra ID Protection** surfaces **risky workload identities** (for example,
  anomalous sign-ins or leaked credentials for a service principal).
- Apply **least privilege** to their RBAC roles, scope them narrowly, and
  **review** their permissions and credentials regularly.

## Putting it together

Applications get identity through an **app registration** (the definition) and a
**service principal** (the running identity that holds roles). Service principals
can authenticate with secrets or certificates — but **managed identities** are
better because Azure owns and rotates the credential and never exposes it, so
there is **nothing to leak**; choose **system-assigned** for a single resource and
**user-assigned** to share one identity across many. Control what apps can do with
**delegated vs application permissions** and tight **consent** settings, use
**workload identity federation** to drop secrets for external CI/CD, and guard
these non-human identities with Conditional Access, ID Protection, and least
privilege.

## Exam focus

- **App registration = definition; service principal = the identity** that gets
  role assignments and signs in. An enterprise application is the service
  principal.
- **Managed identity** = a service principal Azure creates, rotates, and never
  exposes. It is the answer for "resource authenticates to another Azure service
  **without stored credentials**." **System-assigned** = 1:1 with a resource;
  **user-assigned** = shareable and independent.
- Grant the managed identity an **RBAC role** on the target (e.g. **Key Vault
  Secrets User**) — identity plus authorization, no password.
- **Application permissions** (app acting as itself, no user) always need **admin
  consent**; **delegated permissions** act on behalf of a user. Restrict **user
  consent** to block illicit-consent attacks.
- **Workload identity federation** uses a **federated credential** to trust an
  external issuer (GitHub Actions, etc.), removing stored secrets for external
  workloads.
- Secure service principals with **Conditional Access for workload identities**,
  **ID Protection** risk detection, and least-privilege, regularly reviewed roles.
