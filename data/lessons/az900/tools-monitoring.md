# Management Tools & Monitoring

Once resources are running, you need ways to *manage* them and ways to *watch*
them. Azure offers several interfaces for issuing commands and several services for
observing health, performance, cost, and security. The exam expects you to pick the
right tool from a short description. This lesson splits into the management tools
you use to operate Azure and the monitoring tools that tell you how everything is
doing.

## Tools for managing Azure

You can reach Azure through whichever interface fits the task — clicking, scripting,
or automating.

> - **The Azure portal** is the web-based graphical console: a browser dashboard for
>   creating and managing resources by pointing and clicking. Great for learning and
>   one-off tasks.
> - **Azure CLI** is a cross-platform command-line tool (`az` commands) for
>   scripting Azure from Bash, Windows, or macOS.
> - **Azure PowerShell** manages Azure through PowerShell cmdlets (the `Az` module),
>   popular with Windows administrators.
> - **Azure Cloud Shell** is a browser-based shell built into the portal, offering
>   Bash or PowerShell with the tools preinstalled — no local setup required.

Two more management capabilities worth knowing:

- **Infrastructure as code** — **ARM templates** and **Bicep** let you define
  resources declaratively in a file so deployments are repeatable and version-
  controlled.
- **Azure Arc** — extends Azure management and governance **beyond Azure** to
  on-premises, other clouds, and edge servers and Kubernetes clusters, so you can
  manage non-Azure resources as if they lived in Azure.

The portal, CLI, PowerShell, and REST APIs are also the classic example of Azure's
**manageability** — several different ways to do the same management jobs.

## Tools for monitoring and health

### Azure Monitor

> **Azure Monitor is the platform-wide service that collects, analyzes, and acts on
> telemetry from your resources.** It is the umbrella that gathers two fundamentally
> different kinds of data: metrics and logs.

> - **Metrics** are **numerical values captured at regular intervals** — a
>   time-series like CPU percentage or request count. They are lightweight and good
>   for near-real-time charts and alerts.
> - **Logs** are **records of events with varying structure**, stored in Log
>   Analytics and queried with the Kusto Query Language (KQL). They are richer and
>   better for deep investigation.

That metrics-vs-logs distinction — **numeric time-series vs. detailed event
records** — is exactly what the exam asks you to recognize.

### Application Insights

> **Application Insights is an Azure Monitor feature for application performance
> monitoring.** It tracks a **live application's response times, request failures,
> and availability from the user's perspective**, and helps developers find
> bottlenecks and errors.

When a scenario is about watching a running **web app's performance and
availability as users experience it**, the answer is **Application Insights**.

### Azure Advisor

> **Azure Advisor is a free, personalized recommendation engine** that analyzes your
> resources and suggests improvements across five areas: **cost, security,
> reliability, operational excellence, and performance.**

Advisor is the tool that **surfaces a specific cost-optimization recommendation** —
for instance, flagging a **consistently underused VM that should be resized or shut
down** to save money. If a question asks which service recommends right-sizing an
idle VM, it is Advisor.

### Azure Service Health

> **Azure Service Health tells you whether an Azure platform problem is affecting
> the services and regions *you* use** — ongoing **service outages**, **planned
> maintenance**, and health advisories, personalized to your resources.

Note the distinction: Service Health is about the **health of Azure itself** (is the
platform having an incident?), whereas Azure Monitor and Advisor are about the
health of **your** resources. When an operations team needs to know if an **Azure
outage or planned maintenance** is hitting them, that is **Service Health**.

### Microsoft Defender for Cloud

> **Microsoft Defender for Cloud (formerly Azure Security Center) continuously
> assesses the security posture of your resources and protects workloads against
> threats — across Azure and your hybrid and multicloud environments.**

It gives you a **secure score** to track and improve your posture and provides
threat protection for workloads. When a company wants to **continuously assess and
strengthen security posture** (including hybrid/multicloud) and protect workloads,
the answer is **Defender for Cloud**.

## Service-level agreements (SLAs)

Finally, a concept that spans management and trust:

> **A service-level agreement (SLA) is a formal, published commitment from Microsoft
> about the expected performance and uptime of a service** — for example, a
> guaranteed availability percentage — along with the service credits you receive if
> Microsoft falls short.

Fundamentals to keep in mind:

- Different services (and tiers) carry **different SLAs**; a higher tier often
  offers a stronger guarantee.
- When you chain services together, the overall **composite SLA** can be *lower*
  than any single component's, because more moving parts mean more chances to fail.
- Some **free** services carry no financial SLA at all.

## Choosing the right tool

A compact map of the monitoring/health tools:

| You need to… | Use |
|--------------|-----|
| Collect metrics and logs from resources | **Azure Monitor** |
| Watch a live app's performance/availability for users | **Application Insights** |
| Get right-sizing, cost, security, and reliability tips | **Azure Advisor** |
| Know if an Azure outage/maintenance affects you | **Azure Service Health** |
| Assess and improve security posture; protect workloads | **Microsoft Defender for Cloud** |

## Bringing it together

Manage Azure through the **portal** (GUI), **CLI** and **PowerShell** (scripting),
**Cloud Shell** (browser shell), and **ARM/Bicep** (infrastructure as code), and
extend that reach to non-Azure machines with **Azure Arc**. Observe your estate with
**Azure Monitor** (metrics = numeric time-series, logs = event records),
**Application Insights** (app performance), and **Azure Advisor**
(recommendations); learn about platform incidents from **Service Health**; and
strengthen security with **Defender for Cloud** — all underpinned by **SLAs** that
state what each service promises.

## Exam focus

- **Portal** = web GUI; **CLI**/**PowerShell** = command-line scripting; **Cloud
  Shell** = browser-based shell, nothing to install; **ARM/Bicep** = infrastructure
  as code; **Azure Arc** = manage on-prem/multicloud resources from Azure.
- **Azure Monitor**: **metrics** are **numeric time-series**; **logs** are
  **detailed event records** queried with KQL. **Application Insights** monitors a
  live **app's** response times, failures, and availability for users.
- **Azure Advisor** = personalized recommendations (cost, security, reliability,
  operational excellence, performance); it flags **underused VMs to resize/shut
  down**.
- **Azure Service Health** = whether an **Azure platform outage or maintenance**
  affects the services you use. **Microsoft Defender for Cloud** = assess/strengthen
  **security posture** and protect workloads across Azure, hybrid, and multicloud.
- An **SLA** is Microsoft's **formal uptime/performance commitment**; combining
  services can lower the **composite** SLA, and some free tiers have none.
