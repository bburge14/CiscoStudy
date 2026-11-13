# Cost Management, Monitoring & Governance

Choosing cheap services is only half of cost optimization; the other half is
*seeing* where the money goes and *governing* it. AWS has a cluster of cost tools
that sound alike — Explorer, Budgets, CUR, Anomaly Detection, Trusted Advisor,
Compute Optimizer — and the exam tests whether you can pick the one that matches a
specific need: estimate, analyze, alert, attribute, or recommend. This lesson sorts
them by the job they do.

## Estimate before you build

> **AWS Pricing Calculator estimates the expected monthly cost of an architecture
> *before* you build it, based on the services and configurations you plan.**

If the stem says "estimate the cost of a planned architecture," it's the Pricing
Calculator — a planning tool, not a monitoring one.

## Analyze what you've already spent

- **AWS Cost Explorer** — visualize and analyze **historical** cost and usage trends
  over time (up to the past year or more) to find your biggest cost drivers. Reach
  for it when the need is "see trends and understand where money went."
- **AWS Cost and Usage Report (CUR)** — the **most granular** billing data:
  line-item, per-resource, per-hour, with tags, delivered to S3 so you can query it
  with Athena and build custom dashboards. Choose it when the need is maximum detail
  and custom analysis, beyond what Cost Explorer's console shows.

The split: **Cost Explorer** = ready-made visual analysis; **CUR** = raw granular
data for your own queries.

## Get alerted when spend moves

- **AWS Budgets** — set a cost or usage **threshold** and get alerted automatically
  when actual or **forecasted** spend crosses it. This is the answer for "alert me
  when monthly spend is forecast to exceed X."
- **AWS Cost Anomaly Detection** — uses **machine learning** to flag spending that
  deviates from normal patterns in ways a simple fixed threshold would miss, such as
  an unexpected spike in one service.

The distinction: **Budgets** watches a threshold *you* define; **Anomaly Detection**
learns normal and catches the unexpected.

## Attribute costs across teams and accounts

- **Cost allocation tags** — tag resources by department or project so the bill can
  be broken down and charged back to the right team.
- **Consolidated billing through AWS Organizations** — a single bill across many
  accounts, with combined usage reaching **volume pricing tiers** sooner and the
  ability to **share Savings Plans and Reserved Instance** discounts across accounts.

## Get recommendations to cut cost

Two services actively *recommend* savings:

> **AWS Trusted Advisor** runs best-practice checks across cost, security,
> performance, and more, flagging **idle or underutilized** resources (idle load
> balancers, low-utilization EC2) to save money.
>
> **AWS Compute Optimizer** uses machine learning and utilization data to recommend
> **right-sized** EC2 instances, Auto Scaling groups, EBS volumes, and Lambda
> configurations.

The nuance the exam tests: Trusted Advisor flags *idle/underused* resources broadly;
Compute Optimizer gives data-driven *right-sizing* recommendations for specific
resource types.

## A worked example

Before launching, an architect estimates the new stack with the **Pricing
Calculator**. Once live, the finance team watches trends in **Cost Explorer**, sets
an **AWS Budget** to alert when forecast spend exceeds the monthly cap, and turns on
**Cost Anomaly Detection** to catch surprise spikes. They tag every resource with
**cost allocation tags** for chargeback and roll all accounts into one
**consolidated bill** through Organizations to hit volume tiers and share Savings
Plans. Quarterly, they act on **Trusted Advisor** idle-resource findings and
**Compute Optimizer** right-sizing recommendations.

## Telling the look-alikes apart

The cost tools are among the most confused on the exam because several of them
"deal with cost." Anchor each one to the single verb that defines it:

| Verb | Service | One-line tell |
|------|---------|---------------|
| **Estimate** (future) | Pricing Calculator | Before building anything |
| **Analyze** (past, visual) | Cost Explorer | Trends and biggest drivers |
| **Export** (past, granular) | Cost & Usage Report | Line items to S3 for Athena |
| **Alert** (threshold) | AWS Budgets | You set the limit |
| **Alert** (anomaly) | Cost Anomaly Detection | ML learns "normal" |
| **Attribute** | Cost allocation tags | Chargeback by team/project |
| **Combine** | Consolidated billing | One bill, volume tiers, shared RIs/SPs |
| **Recommend** (idle) | Trusted Advisor | Flags waste across pillars |
| **Recommend** (right-size) | Compute Optimizer | ML sizing for EC2/EBS/Lambda |

A subtle pair the exam likes: **Budgets vs Cost Anomaly Detection**. If the stem
gives you a *specific number* ("alert at $5,000"), it's Budgets; if it says
"deviates from normal patterns" or "a spike a fixed threshold would miss," it's
Anomaly Detection. Another pair: **Trusted Advisor vs Compute Optimizer** — Trusted
Advisor points at *idle* resources to turn off; Compute Optimizer suggests the
*right size* for resources you keep.

## Exam focus

- Estimate a planned architecture's cost → **Pricing Calculator**.
- Analyze historical trends and cost drivers → **Cost Explorer**; most granular
  line-item data to S3 for Athena → **Cost and Usage Report (CUR)**.
- Alert when spend crosses a defined threshold (actual or forecast) → **AWS
  Budgets**; ML-based detection of unusual spend → **Cost Anomaly Detection**.
- Attribute/charge back by team or project → **cost allocation tags**; single bill +
  volume tiers + shared RIs/Savings Plans across accounts → **consolidated billing
  via Organizations**.
- Flag idle/underutilized resources → **Trusted Advisor**; ML right-sizing for
  EC2/ASG/EBS/Lambda → **Compute Optimizer**.
