# SDN, Controllers, APIs & Config-Management Tools

## Planes of operation
- **Data (forwarding) plane** — moves packets (ASIC/CEF). Fast.
- **Control plane** — decides how to forward (routing/STP). Builds the tables.
- **Management plane** — how you administer the device (SSH, SNMP, NETCONF).

## SDN and controllers
Software-Defined Networking centralizes the control plane onto a **controller**
that programs the devices. Two interface directions:
- **Northbound Interface (NBI)** — faces **up** to applications/orchestration;
  usually a **REST API**.
- **Southbound Interface (SBI)** — faces **down** to the devices; e.g.,
  **NETCONF**, OpenFlow, gRPC.

Picture the controller in the middle: apps talk down to it (NBI), it talks down
to devices (SBI). East-west is controller-to-controller.

Cisco examples: **Catalyst Center (DNA Center)** for campus intent-based
networking, **SD-Access**, **SD-WAN (vManage)**.

## Benefits of controller-based / intent-based networking
Centralized, consistent policy; faster, repeatable changes; less configuration
drift and fewer manual per-box errors; programmatic visibility. It does **not**
abolish IP addressing or routing — it manages them (watch "eliminates X
entirely" distractors).

## REST APIs
REST uses HTTP(S) with standard verbs on resources (URIs):

| Verb | Action |
|------|--------|
| GET | read |
| POST | create |
| PUT / PATCH | replace / modify |
| DELETE | remove |

HTTP status ranges: **2xx** success (200 OK, 201 Created, 204 No Content),
**3xx** redirect, **4xx** client error (400 bad request, 401 unauthorized, 403
forbidden, 404 not found), **5xx** server error. Data is usually **JSON**.

## Configuration-management tools
| Tool | Agent? | Model | Language |
|------|--------|-------|----------|
| **Ansible** | **Agentless** (SSH/NETCONF) | **Push** | YAML playbooks |
| **Puppet** | Agent | **Pull** | Puppet DSL (manifests) |
| **Chef** | Agent | **Pull** | Ruby (recipes/cookbooks) |

Ansible's agentless + push + YAML combination makes it the common fit for network
devices that can't run agents.

## Exam cues
- Northbound = up to apps (REST); Southbound = down to devices (NETCONF/OpenFlow).
- Ansible = agentless, push, YAML. Puppet/Chef = agent, pull.
- 201 Created / 401 Unauthorized / 404 Not Found — know the ranges.
