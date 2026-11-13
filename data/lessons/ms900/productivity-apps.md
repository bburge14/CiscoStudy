# Core Productivity Apps & Deployment

Microsoft 365 is, at its core, a big toolbox. Over 45% of the exam is about knowing
*which tool does which job* — so the most valuable skill here is matching a
business need to the right app or service. This lesson covers the everyday
productivity apps and cloud services, then how the desktop apps actually get onto
users' computers and stay updated.

## The familiar desktop apps

These are the applications most people picture when they hear "Office":

- **Word** — documents: letters, reports, contracts.
- **Excel** — spreadsheets: numbers, formulas, charts, analysis.
- **PowerPoint** — presentations and slide decks.
- **Outlook** — the email, calendar, and contacts *client* (the app you read mail
  in).
- **OneNote** — a free-form digital notebook.

A useful distinction the exam draws: **Outlook is the client app** you use to read
and send mail, while **Exchange Online is the back-end service** that actually
hosts the mailboxes. One is the window; the other is the post office behind it.

## The cloud services that back them

Behind the apps sit cloud services that store and move your content:

> **Exchange Online** hosts business **email, calendars, and contacts** in the
> cloud, with no on-premises mail server to run. **SharePoint Online** provides
> **team sites and intranet pages** with shared document libraries. **OneDrive**
> gives each user **personal cloud storage** that syncs across devices.

Keep these three straight — they're a frequent source of "which service?"
questions:

| Need | Service |
|------|---------|
| Cloud-hosted business email, calendars, contacts | **Exchange Online** |
| A shared intranet / team site with news and document libraries | **SharePoint Online** |
| Personal cloud storage synced across my devices, share individual files | **OneDrive** |

The quick rule: **SharePoint is shared/team storage and sites; OneDrive is your
personal storage.** Files you work on alone live in OneDrive; files a team
co-manages live in a SharePoint document library (often surfaced through Teams).

## The wider app family

Microsoft 365 includes many smaller, purpose-built apps. You don't need deep
expertise — just recognize what each is *for*:

- **Microsoft Forms** — quick online **surveys and auto-graded quizzes** with
  response charts.
- **Microsoft Bookings** — lets customers **self-schedule appointments**.
- **Microsoft Lists** — track information in smart, structured lists.
- **Microsoft Planner** and **To Do** — **task management** for teams and
  individuals.
- **Microsoft Loop** — collaborative "components" that stay in sync wherever
  they're pasted.
- **Microsoft Stream** — a place for **video** content across the organization.
- **Visio** (diagrams) and **Project** (project management) — specialized apps,
  often licensed as add-ons.
- The **Power Platform** — **Power BI** (business-intelligence dashboards),
  **Power Apps** (low-code apps), **Power Automate** (workflow automation), and
  **Power Pages** (external websites).

When a scenario says "send a short survey and see response charts," the answer is
**Forms**; "let customers book time slots" is **Bookings**; "interactive data
dashboards" is **Power BI**.

## How the apps get deployed

Now, the installation side. The modern Office apps don't use the old-style
Windows Installer (MSI). They use a streaming technology:

> **Click-to-Run** is the streaming install-and-update technology for Microsoft 365
> Apps. It downloads the apps quickly, lets users start working before the
> download finishes, and keeps them **updated automatically** in the background.

Organizations have several ways to roll the apps out:

- **Self-install from the portal** — users sign in to the Microsoft 365 portal and
  install the apps themselves (great for small teams).
- **Office Deployment Tool (ODT)** — a configurable tool for scripted,
  customized installs.
- **Cloud Update / the Microsoft 365 Apps admin center** — Microsoft's recommended
  cloud-based way to manage updates centrally with no local infrastructure.
- **Microsoft Intune or Configuration Manager** — enterprise management tools push
  the apps to managed devices (we'll meet Intune in the next lesson).

And for devices that can't install software at all, **Office for the web** runs
Word, Excel, and PowerPoint right in the browser — a contractor on a locked-down
PC can still view and lightly edit files with nothing installed.

## Update channels: controlling *when* features arrive

Because Microsoft 365 Apps update continuously, organizations need a way to control
*how fast* new features reach users. That control is the **update channel**:

- **Current Channel** — the **default**. New features arrive **as soon as they're
  ready**, with no fixed schedule. Best for users who want the latest capabilities.
- **Monthly Enterprise Channel** — feature and security updates land on a
  **predictable monthly schedule** (the second Tuesday of the month). Best when IT
  wants consistency and time to validate.
- **Semi-Annual Enterprise Channel** — **historically** the least frequent cadence
  (feature updates twice a year), for devices needing extensive testing. **As of
  mid-2026 Microsoft unified its feature cadence into the Monthly Enterprise
  Channel**, so it is no longer a distinct slower track — the name persists through
  the transition, but expect monthly delivery.

> The trade-off is **newest features vs. predictability and testing time.** Pick
> **Current Channel** for the latest features fastest; move pilot or stable
> machines to **Monthly** or **Semi-Annual Enterprise Channel** when you want
> fewer, more predictable changes.

A related choice is **32-bit vs 64-bit**; 64-bit is the default and is
recommended for modern PCs handling large files.

## The whole thing in one paragraph

Microsoft 365's apps split into the desktop clients (**Word, Excel, PowerPoint,
Outlook, OneNote**) and the cloud services behind them: **Exchange Online** (email
and calendars), **SharePoint Online** (team sites and shared libraries), and
**OneDrive** (personal storage) — with a wide family of purpose-built apps like
**Forms**, **Bookings**, **Planner**, **Loop**, and the **Power Platform**. The
desktop apps install through **Click-to-Run** (self-service, the Office Deployment
Tool, Cloud Update, or Intune), while **Office for the web** needs no install, and
**update channels** (**Current**, **Monthly Enterprise**, **Semi-Annual
Enterprise**) control how quickly new features reach users.

## Exam focus

- Map needs to services: cloud **email/calendars** = **Exchange Online**; **team
  site/intranet with shared libraries** = **SharePoint Online**; **personal cloud
  storage** = **OneDrive**. **Outlook** is the client; **Exchange Online** is the
  service behind it.
- Niche apps by purpose: **Forms** = surveys/quizzes, **Bookings** =
  appointment scheduling, **Power BI** = BI dashboards, **Planner/To Do** = tasks.
- **Click-to-Run** is the streaming install-and-auto-update technology for
  Microsoft 365 Apps (replacing the old MSI installer).
- **Office for the web** = free, browser-based, no install, for restricted or
  shared devices.
- Update channels control *when* features arrive: **Current Channel** (default,
  continuous), **Monthly Enterprise Channel** (predictable monthly), **Semi-Annual
  Enterprise Channel** (least frequent, for extensive testing).
