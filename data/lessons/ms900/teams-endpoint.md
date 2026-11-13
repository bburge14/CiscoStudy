# Teamwork, Collaboration & Endpoint Management

This lesson pairs two of the most practical parts of Microsoft 365: the tools
people use to *work together* (centered on Microsoft Teams) and the service IT uses
to *manage the devices* that run everything (Microsoft Intune). One is about
collaboration; the other is about keeping the laptops and phones that collaborate
secure and configured.

## Microsoft Teams: the hub for teamwork

If Microsoft 365 has a front door, it's Teams.

> **Microsoft Teams** is the hub that combines **persistent chat**, **online
> meetings** (video, audio, screen sharing), **calling**, and **shared workspaces**
> into one app, with files and other apps built right in.

Teams is organized so conversations don't get lost:

- A **team** is a group of people working together (a department, a project).
- Inside a team are **channels** — dedicated spaces for specific topics, each with
  its own conversations and files. Channels can be **standard** (visible to the
  whole team), **private** (a subset), or **shared** (including people from other
  teams or organizations).
- **Chat** handles quick one-to-one or small-group messages outside of channels.
- **Meetings** can be scheduled or started instantly, with video, screen sharing,
  recording, and AI-generated recaps.

Teams also brings other capabilities you should recognize:

- **Teams Phone** — make and receive **regular phone calls** to external numbers
  from inside Teams (with a **calling plan**), turning Teams into a full phone
  system.
- **Webinars and town halls** — structured, large-audience broadcast events.
- **Guest access and external access** — invite people from outside your
  organization to collaborate, or federate chat with other companies.

A historical note the exam likes: Teams **replaced Skype for Business** as
Microsoft's meetings and instant-messaging solution. If old documentation mentions
Skype for Business, the modern answer is **Microsoft Teams**.

### Collaborating on content

Collaboration isn't only chat — it's working on the same content at once:

- **Co-authoring** — several people open the same cloud-stored Word, Excel, or
  PowerPoint file and edit it **simultaneously**, each seeing the others' changes
  live.
- **Microsoft 365 Groups** — the membership backbone behind the scenes. Creating a
  team, for example, also provisions a group mailbox and a SharePoint site, so one
  membership list powers several services.
- **Viva Engage** (formerly **Yammer**) — an enterprise social network for
  organization-wide **communities**, announcements, and discussions that cross team
  boundaries.

## Microsoft Intune: managing the endpoints

Every one of those collaborators is working on a device, and those devices need to
be configured, secured, and kept compliant. That's endpoint management.

> **Microsoft Intune** is the cloud service to **enroll, configure, and secure**
> endpoints — laptops, desktops, phones, and tablets — **deploy apps**, and
> **enforce compliance policies**, with no on-premises management servers.

Intune centers on two complementary approaches, and knowing the difference is a
reliable exam point:

- **Mobile Device Management (MDM)** — manage the **entire enrolled device**: its
  settings, its compliance state, and the ability to **wipe the whole device**.
  Best for **corporate-owned** hardware.
- **Mobile Application Management (MAM)** — manage **only the apps and company
  data** inside them, using **app protection policies**. You can **selectively
  wipe just the work data** and leave personal content untouched. Best for
  **BYOD** (personal phones used for work).

> The rule of thumb: **MDM manages the device; MAM manages the app.** Corporate
> device → MDM. Personal device where you must protect only company data → MAM.

Two more Intune-adjacent capabilities:

- **Windows Autopilot** — provisions **brand-new devices automatically**. A device
  is shipped straight to the employee, who signs in and Autopilot configures it
  from the cloud — no manual imaging by IT.
- **Compliance policies and Conditional Access** — Intune reports whether a device
  meets your rules (encrypted, up to date, not jailbroken), and Microsoft Entra
  **Conditional Access** can then block or allow access based on that state.

## Windows 365 and Cloud PCs

Sometimes the "device" itself lives in the cloud:

- **Windows 365 (Cloud PC)** — gives each user a **personal, persistent Windows
  desktop in the cloud** that they can stream to any device, with simple,
  **fixed per-user pricing**. Their desktop, apps, and files are always there,
  whatever they sign in from.
- **Azure Virtual Desktop (AVD)** — a more flexible, highly customizable
  virtual-desktop platform billed by **Azure consumption**, aimed at IT teams that
  want fine-grained control and scaling.

The simple contrast: **Windows 365 = a fixed-price personal cloud PC**; **Azure
Virtual Desktop = flexible, consumption-priced virtual desktops.**

## The whole thing in one paragraph

**Microsoft Teams** is the collaboration hub — chat, meetings, calling, and shared
workspaces organized into **teams** and **channels**, with **Teams Phone** for
external calls — and it replaced Skype for Business; around it sit **co-authoring**,
**Microsoft 365 Groups**, and **Viva Engage** (formerly Yammer). **Microsoft
Intune** manages the endpoints people work on, using **MDM** to manage whole
corporate devices and **MAM** app-protection policies to protect company data on
**BYOD**, with **Windows Autopilot** for zero-touch setup, while **Windows 365**
delivers a fixed-price personal **Cloud PC** and **Azure Virtual Desktop** offers
flexible consumption-based virtual desktops.

## Exam focus

- **Microsoft Teams** is the single app for chat + meetings + calling + shared
  workspaces, organized into **channels**; it **replaced Skype for Business**.
  **Teams Phone** (with a calling plan) adds external phone calls.
- **Co-authoring** = multiple people editing one cloud document live. **Viva
  Engage** = the renamed **Yammer** (enterprise social/communities).
- **Microsoft Intune** = cloud endpoint management. **MDM manages the whole
  device** (corporate-owned, full wipe); **MAM with app protection policies** protects
  **only company data** on **BYOD** (selective wipe).
- **Windows Autopilot** = automatic, zero-touch provisioning of new devices.
- **Windows 365 (Cloud PC)** = a personal, persistent, **fixed-price** Windows
  desktop in the cloud; **Azure Virtual Desktop** = flexible, **consumption-priced**
  virtual desktops.
