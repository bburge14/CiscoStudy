# SDN, Controllers, APIs & Config-Management Tools

In a traditional network, every switch and router is its own little manager. Each
one makes its own forwarding decisions and has to be configured by hand, one box
at a time. **Software-Defined Networking (SDN)** changes that by moving the
decision-making into one central brain — a **controller** — that programs all the
devices for you. Picture a city where every traffic light runs on its own timer,
versus one control center coordinating them all at once; SDN is the control
center.

To understand what the controller takes over, it helps to know that a network
device really does three separate jobs, which we call **planes**.

> **The data plane *moves* the packets, the control plane *decides* where packets
> should go, and the management plane is how *you* log in and run the device.**

The **data (forwarding) plane** is the worker that actually pushes packets out
the ports, and it's built for raw speed in hardware (ASIC/CEF). The **control
plane** is the planner: it runs things like routing protocols and STP and builds
the tables that tell the data plane what to do. The **management plane** is the
front desk where an administrator connects to operate the box, over tools like
SSH, SNMP, or NETCONF. SDN's big move is to lift the *control* plane out of each
device and centralize it on the controller.

## North and south: which way the controller talks

A controller sits in the middle and talks in two directions, and the names simply
describe which way it's facing.

The **Northbound Interface (NBI)** faces **up** toward the applications and
orchestration tools that want to tell the network what to do. This is usually a
**REST API** (more on that below). The **Southbound Interface (SBI)** faces
**down** toward the actual devices, using protocols like **NETCONF**, OpenFlow,
or gRPC. So an app hands its request down to the controller through the
northbound interface, and the controller reaches down to the switches and routers
through the southbound interface. (When two controllers talk to each other,
that's called east-west.)

Cisco's real products here include **Catalyst Center** (formerly **DNA Center**)
for campus intent-based networking, **SD-Access**, and **SD-WAN** (managed by
**vManage**).

The payoff of this controller-based, intent-based approach is consistency: policy
is set in one place, changes are fast and repeatable, there's far less
configuration drift and fewer hand-typed per-box mistakes, and you get
programmatic visibility into the whole network. One caution for exam questions,
though: SDN does **not** abolish IP addressing or routing — it still manages them.
Be suspicious of any answer that says a controller "eliminates" addressing or
routing entirely.

## REST APIs: how the apps actually ask

That northbound REST API is worth understanding because it shows up everywhere. A
**REST API** works over plain **HTTP(S)** — the same protocol your web browser
uses — and it acts on *resources* named by URIs (web addresses) using a few
standard verbs. **GET** reads something, **POST** creates something new, **PUT**
or **PATCH** replaces or modifies it, and **DELETE** removes it.

When the server answers, it includes a status code, and the first digit tells you
the category at a glance. **2xx** means success (200 OK, 201 Created, 204 No
Content). **3xx** means a redirect. **4xx** means *you* sent something wrong — 400
bad request, 401 unauthorized, 403 forbidden, 404 not found. **5xx** means the
*server* broke. The data carried back and forth is usually **JSON**, a simple text
format of names and values.

## Config-management tools: Ansible, Puppet, Chef

Separately from SDN, teams use configuration-management tools to push consistent
setups to many machines at once. The three you should recognize differ in a few
key ways, so a small table earns its place here:

| Tool | Agent? | Model | Language |
|------|--------|-------|----------|
| **Ansible** | **Agentless** (SSH/NETCONF) | **Push** | YAML playbooks |
| **Puppet** | Agent | **Pull** | Puppet DSL (manifests) |
| **Chef** | Agent | **Pull** | Ruby (recipes/cookbooks) |

The one distinction to really hold onto is Ansible's combination: it is
**agentless** (it reaches devices over SSH or NETCONF rather than needing software
installed on them), it **pushes** changes out, and it's written in **YAML**
playbooks. That agentless design is exactly why Ansible is the common fit for
network devices, which often can't run a management agent of their own. Puppet and
Chef both work the opposite way — each managed machine runs an **agent** that
**pulls** its configuration from a central server.

## The whole thing in one paragraph

SDN takes the control plane — the part of each device that decides how to forward
traffic — and centralizes it on a controller, leaving the data plane to move
packets and the management plane for you to log in. That controller talks up to
applications through its northbound interface (usually a REST API) and down to
devices through its southbound interface (NETCONF, OpenFlow, gRPC), giving you
consistent, fast, repeatable policy without abolishing addressing or routing.
REST itself is just HTTP verbs — GET to read, POST to create, PUT/PATCH to change,
DELETE to remove — with status codes grouped as 2xx success, 4xx your mistake, and
5xx the server's, usually carrying JSON. And for pushing configs, remember Ansible
stands apart as agentless, push-based, and YAML, which is why it suits network
gear, while Puppet and Chef use agents that pull.
