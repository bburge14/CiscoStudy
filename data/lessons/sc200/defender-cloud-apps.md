# Microsoft Defender for Cloud Apps

Microsoft Defender for Cloud Apps (MDA) is Microsoft's **Cloud Access Security
Broker (CASB)**. A CASB sits between your users and the SaaS applications they
use and gives security teams visibility and control over cloud activity that would
otherwise be invisible. For SC-200 the heart of this topic is knowing what MDA can
see, how it connects to apps, and the crucial difference between its two real-time
control policies.

## What a CASB does: the four pillars

MDA is usually described through four jobs a CASB performs:

- **Discovery (visibility)** — find every cloud app in use, including the ones no
  one approved (shadow IT).
- **Data protection** — find and control sensitive information in cloud apps with
  DLP-style policies and sensitivity labels.
- **Threat protection** — detect compromised accounts, risky behavior, and
  malicious activity across your SaaS estate.
- **Compliance** — assess apps against regulatory and organizational requirements.

## Seeing shadow IT: Cloud Discovery

**Cloud Discovery** answers "what are my users actually using?" It analyzes
network traffic logs to surface every app that has been accessed.

> Cloud Discovery works from logs — either uploaded from firewalls and proxies
> (snapshot or continuous via a **log collector**), or streamed automatically from
> **Defender for Endpoint** on onboarded devices. Each discovered app gets a **risk
> score** so you can decide whether to **sanction** or **unsanction** it.

Marking an app *unsanctioned* can, with the Defender for Endpoint integration,
actually block access to it on managed devices — discovery that leads to control.

## Connecting sanctioned apps: app connectors

For apps you *do* approve, **app connectors** use the app's own vendor APIs to pull
in deep signal: activity logs, stored files, user accounts, and more, for services
such as Microsoft 365, Google Workspace, Salesforce, Box, and AWS.

> **App connectors are API-based and work on data at rest and after the fact.**
> They let MDA scan existing files for sensitive data and report on activity, but
> because they poll APIs they are **not** real time.

Once connected, you can write **file policies** (find files shared externally or
containing regulated data), **activity policies** (alert on risky actions), and
rely on built-in **anomaly detection policies** that use machine learning to flag
impossible travel, mass download, and other unusual behavior.

## Controlling sessions live: Conditional Access App Control

The real-time muscle comes from **Conditional Access App Control**, which routes a
user's session through MDA as a reverse proxy (in partnership with Microsoft Entra
Conditional Access). This enables two policy types that are endlessly confused —
learn the distinction cold.

| Policy | When it acts | What it controls | Example |
|--------|--------------|------------------|---------|
| **Access policy** | At **sign-in** | Allow or **block access** to the app entirely | Block sign-in to the app from unmanaged devices |
| **Session policy** | **During** the session | Monitor and limit *actions inside* the app in real time | Allow sign-in but **block download**, or apply a sensitivity label on download |

> **Access policy = can you get in at all. Session policy = what you're allowed to
> do once you're in.** If the scenario says "block the download but still let them
> work," that is a *session* policy; "block the login from this device" is an
> *access* policy.

Session policies can block or protect downloads, block uploads, block
copy/cut/paste and print, and require sensitivity labels — all while the user is
actively working.

## OAuth apps and app governance

Attackers increasingly abuse **OAuth app consent**: they trick a user into granting
a malicious third-party app standing permissions (read mail, access files) that
survive a password reset. MDA inventories OAuth apps, scores their risk by the
permissions they hold and their publisher, and lets you **revoke** risky ones. The
**app governance** add-on deepens this with behavioral detections on how OAuth apps
actually use their granted permissions.

## Detecting threats and governance actions

Beyond the policies you author, MDA ships **built-in anomaly detection** tuned for
cloud threats: **impossible travel** (sign-ins from two distant locations too close
in time to be real), **activity from infrequent countries**, **mass download** or
mass deletion, **ransomware activity**, and **unusual administrative behavior**.
These need no configuration and surface as alerts.

When something is wrong, MDA gives you **governance actions** to respond: suspend a
user, require them to sign in again, revoke risky OAuth app permissions, quarantine
or remove a shared file, or apply a sensitivity label. Policies can run these
automatically, so detection flows straight into containment.

> Impossible travel is the archetypal MDA detection — remember it as the example of
> ML-driven anomaly detection, and remember that governance actions (suspend user,
> revoke app, quarantine file) are how MDA *responds*, not just alerts.

## Where MDA fits in Defender XDR

MDA is part of Microsoft Defender XDR. Its alerts — impossible travel, mass
download, risky OAuth consent — surface in the unified portal and correlate with
endpoint, email, and identity signals into shared incidents. It also deepens
**Microsoft Entra ID** identity protection by feeding cloud-activity context into
the broader detection picture.

## Exam focus

- MDA is Microsoft's **CASB**. The four pillars: **discovery/visibility, data
  protection, threat protection, compliance.**
- **Cloud Discovery** finds **shadow IT** from traffic logs (uploaded via a **log
  collector**, or streamed from **Defender for Endpoint**) and scores app risk;
  you **sanction/unsanction** apps.
- **App connectors** are **API-based** — great for data at rest and post-hoc
  activity, but **not real time**.
- The must-know distinction: **access policy = block/allow the sign-in**; **session
  policy = control actions (block download, apply label) during the session**, both
  via **Conditional Access App Control** (reverse proxy) with Entra Conditional
  Access.
- MDA inventories and scores risky **OAuth apps**; the **app governance** add-on
  adds behavioral detection. Alerts correlate into **Defender XDR** incidents.
