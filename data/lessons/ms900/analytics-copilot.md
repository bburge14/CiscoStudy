# Analytics, Viva Insights & Microsoft 365 Copilot

Microsoft 365 doesn't just store your work — it understands it. A connective data
layer links your emails, chats, files, and calendar, and on top of that sit the
analytics tools that reveal how people work and the AI that helps them work. This
lesson covers that intelligence layer: **Microsoft Graph**, **Viva Insights**, and
**Microsoft 365 Copilot**.

## Microsoft Graph: the connective tissue

Everything intelligent in Microsoft 365 is built on one foundation.

> **Microsoft Graph** is the common layer (and API) that connects an
> organization's Microsoft 365 data — **emails, chats, files, calendar events,
> contacts, and the relationships between them**. It's what lets one tool reason
> about data created in another.

Think of Graph as the map of who works with whom, on what, and when. Both Viva
Insights and Microsoft 365 Copilot **draw on Microsoft Graph** to do their jobs —
without that shared layer, each app would be an island.

## Viva Insights and the Viva family

**Microsoft Viva** is Microsoft 365's **employee experience platform** — a family
of modules that surface wellbeing, knowledge, communications, and goals inside the
flow of work. The module the exam focuses on is Viva Insights.

> **Microsoft Viva Insights** gives **data-driven insights into productivity and
> wellbeing** — focus time, meeting habits, after-hours work, and collaboration
> patterns — to individuals, managers, and leaders, with privacy protections built
> in.

The key idea is that Insights turns the activity captured in Microsoft Graph into
*actionable guidance*: it might suggest protecting focus time, catching up on
overdue tasks, or reducing after-hours messaging. Other Viva modules you may see
named include **Viva Connections** (a personalized company intranet experience),
**Viva Learning** (training in the flow of work), **Viva Goals** (objectives and
key results), and **Viva Engage** (the communities experience we met earlier).

Alongside Viva, administrators get **usage and adoption analytics** in the
**Microsoft 365 admin center** — reports on how actively services like Teams,
Exchange, and SharePoint are being used, which helps drive adoption.

## Microsoft 365 Copilot: AI across the apps

Copilot is the headline AI capability, and it shows up throughout the suite.

> **Microsoft 365 Copilot** is an AI assistant **built into Word, Excel,
> PowerPoint, Outlook, and Teams** that can **draft content, summarize meetings and
> email threads, analyze data, and answer questions** using your organization's own
> Microsoft 365 data.

What makes Copilot more than a generic chatbot is *grounding*: it combines a large
language model with **your** content through **Microsoft Graph**, so its answers
are specific to your documents, meetings, and messages. Examples the exam draws on:

- **Copilot in Word** — draft or rewrite a document from a prompt.
- **Copilot in Excel** — explore and analyze data, suggest formulas and trends.
- **Copilot in PowerPoint** — turn a document into a first-draft deck.
- **Copilot in Outlook** — summarize long threads and draft replies.
- **Copilot in Teams** — produce an **AI-generated meeting recap** with key points,
  decisions, and action items.

### How Copilot respects security and privacy

Two points Microsoft stresses, and the exam reflects:

- **Copilot honors existing permissions.** It can only surface content the signed-in
  user *already* has access to — it never widens access.
- **Your data stays yours.** Prompts, responses, and your Microsoft 365 content are
  **not used to train** the underlying foundation models, and they remain within
  your organization's trust boundary.

### Copilot licensing and Copilot Chat

Microsoft 365 Copilot is a **paid add-on**: you buy it on top of a **qualifying
base license** (business and enterprise Microsoft 365 plans) and assign it per
user. Separately, **Microsoft 365 Copilot Chat** offers **web-grounded** AI chat
with enterprise data protection and is included more broadly; the richer,
**work-grounded** experience across your apps and Graph is what the add-on unlocks.
(We cover the commercial details further in the pricing unit.)

## Putting the layer together

Picture three stacked layers:

| Layer | What it is | Example |
|-------|-----------|---------|
| **Data** | Microsoft Graph | Your emails, files, chats, calendar |
| **Analytics** | Viva Insights + admin usage reports | "You had little focus time this week" |
| **AI** | Microsoft 365 Copilot | "Summarize this thread and draft a reply" |

Each layer depends on the one below it: Copilot and Insights are only as useful as
the Graph data they sit on.

## The whole thing in one paragraph

**Microsoft Graph** is the shared data layer that connects your Microsoft 365
emails, chats, files, and calendar, and both **Viva Insights** (data-driven
productivity and wellbeing guidance, part of the **Microsoft Viva** employee-
experience family) and **Microsoft 365 Copilot** draw on it. Copilot is an AI
assistant **built into Word, Excel, PowerPoint, Outlook, and Teams** that drafts,
summarizes, and analyzes using your own grounded data, **respects existing
permissions**, does **not train** foundation models on your content, and is sold as
a **paid add-on** on top of a qualifying base license — with **Copilot Chat**
providing a more broadly available, web-grounded experience.

## Exam focus

- **Microsoft Graph** is the common layer connecting Microsoft 365 data; **Copilot
  and Viva Insights both build on it.**
- **Viva Insights** = data-driven insights into **productivity and wellbeing**
  (focus time, meeting habits, after-hours work), part of **Microsoft Viva**.
- **Microsoft 365 Copilot** = AI **built into Word, Excel, PowerPoint, Outlook,
  and Teams**; it drafts content, summarizes meetings/email, and analyzes data,
  **grounded in your own content**. "AI meeting recap" = **Copilot in Teams**.
- Copilot **honors existing permissions** and your content is **not used to train**
  the foundation models.
- Microsoft 365 Copilot is a **paid add-on** requiring a **qualifying base
  license**; **Copilot Chat** is the more broadly available, web-grounded chat.
