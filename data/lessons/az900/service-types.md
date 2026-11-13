# Cloud Service Types: IaaS, PaaS & SaaS

The cloud is not one thing you buy — it is a spectrum of how *much* the provider
manages for you. At one end you rent bare infrastructure and do almost everything
yourself; at the other you just log in and use finished software. The three
classic points on that spectrum are **IaaS**, **PaaS**, and **SaaS**. Knowing
which is which, and who is responsible for what in each, is one of the most
heavily tested ideas on the whole exam.

## The spectrum of control

Remember the shared responsibility line from earlier? The service type is what
decides *where* that line sits. As you move from IaaS to PaaS to SaaS, you hand
more and more of the stack — operating system, runtime, application — to the
provider, and you keep less to manage yourself.

> **IaaS (Infrastructure as a Service):** the provider gives you the raw building
> blocks — virtual machines, storage, and networks — and you manage everything
> from the operating system up. Most control, most responsibility.

> **PaaS (Platform as a Service):** the provider manages the infrastructure *and*
> the operating system and runtime, and you just deploy and manage your
> application and data. A middle ground that removes server chores.

> **SaaS (Software as a Service):** the provider delivers finished software over
> the internet. You simply use it — usually on a per-user subscription — and
> manage nothing underneath but your own data and users.

### A kitchen analogy

A well-worn way to remember this is dinner:

- **IaaS** is like renting a fully equipped kitchen. The building, power, and
  appliances are provided, but *you* bring the ingredients and do all the cooking
  (you manage the OS, patching, and the app).
- **PaaS** is like a meal-kit service. The ingredients are measured and the recipe
  is written; you just assemble and cook your dish (you deploy your app; the
  platform handles the rest).
- **SaaS** is like going to a restaurant. You order, you eat, you leave. Someone
  else bought the food, cooked it, and will wash up (you just use the software).

## Who is responsible for what

Here is the division of labor that the exam probes relentlessly. "The OS" is the
hinge: in IaaS it is yours; in PaaS and SaaS it belongs to the provider.

| Responsibility | IaaS | PaaS | SaaS |
|----------------|------|------|------|
| Physical datacenter, hosts, network | Provider | Provider | Provider |
| **Operating system** (patching, updates) | **You** | **Provider** | **Provider** |
| Runtime / middleware | You | Provider | Provider |
| Application | You | You (your app) | Provider |
| **Data, identities, access** | **You** | **You** | **You** |

Two patterns to lock in:

- In **PaaS**, the **provider patches and maintains the operating system** — that
  is the whole point of PaaS; you stop babysitting servers.
- If you **move a workload from PaaS back to IaaS**, the responsibility that
  **returns to you is managing and patching the operating system** (and the
  runtime). You traded convenience for control.

And no matter which you choose, **data, identities, and access always stay with
you** — the right-hand column never changes.

## When to use each

The exam rewards matching a scenario to the right service type. Train your ear for
the keywords.

### Choose IaaS when you need control

Pick **IaaS** when you must keep full control of the operating system and the
server configuration:

- **Lift-and-shift migrations** — moving existing servers to Azure "with minimal
  changes" while keeping full control of each OS. IaaS virtual machines mirror
  what you ran on-premises.
- **Legacy or specialized workloads** — an application that needs specific
  **OS-level drivers** or particular low-level server settings. Only IaaS gives
  you that depth of control.

The tell is any phrase like "full control of the OS," "install drivers," or
"minimal changes to existing servers."

### Choose PaaS when you want to build without the plumbing

Pick **PaaS** when you want to develop, run, and scale an application **without
managing the underlying servers or operating system**. You bring your code; the
platform handles the OS, patching, and scaling. The tell is "deploy an app without
managing the OS/servers."

### Choose SaaS when you just need finished software

Pick **SaaS** when you want **ready-made software, with no servers to manage, paid
per user**:

- A small business that wants finished **accounting and email** software with
  nothing to run or patch — that is SaaS.
- Staff who **sign in and use ready-made email and productivity apps** over the
  internet, managing none of the servers underneath — SaaS again. (Microsoft 365
  is the familiar example.)

The tell is "ready-made/finished software," "per-user subscription," and "no
servers to manage."

## The whole spectrum in one breath

IaaS rents you raw infrastructure and leaves the OS and app to you (control);
PaaS hands you a managed platform so you only bring your application (balance);
SaaS gives you finished software you simply use (convenience). The operating
system is the dividing line — yours in IaaS, the provider's in PaaS and SaaS — and
your data and identities remain yours in every case.

## Exam focus

- **IaaS** = you manage the OS and up; **most control**. Best for lift-and-shift
  migrations and workloads needing full OS control or special drivers.
- **PaaS** = provider manages the OS/runtime; **you manage only your app and
  data**. The provider patches the OS. Best for building/hosting apps without
  server management.
- **SaaS** = provider manages everything but your data and users; **finished
  software, per-user subscription**. Best for ready-made email/office/accounting
  apps.
- The **operating system** is the hinge: provider's job in **PaaS and SaaS**,
  your job in **IaaS**. Moving **PaaS → IaaS** returns **OS management** to you.
- **Data, identities, and access** stay with the customer in **all three** types.
