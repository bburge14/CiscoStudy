# Automation: Data Formats, NETCONF/RESTCONF, EEM & Telemetry

## Data formats
| Format | Markers | Notes |
|--------|---------|-------|
| **JSON** | `{}` object, `[]` array, `""` string, numbers, `true/false`, `null` | API default; maps cleanly to Python |
| **XML** | `<tag>value</tag>` | verbose; NETCONF's native encoding |
| **YAML** | indentation (spaces, **no tabs**), `- ` lists, `key: value` maps | Ansible playbooks |

JSON → Python: object→`dict`, array→`list`, string→`str`, bool→`bool`, null→`None`.
Navigate nested data by key/index:
```python
import json
data = json.loads(resp.text)
first = data['ietf-interfaces:interfaces']['interface'][0]['name']
```

## NETCONF vs RESTCONF
| | NETCONF | RESTCONF |
|--|---------|----------|
| Transport | SSH **830** | HTTPS **443** |
| Encoding | XML | XML or JSON |
| Style | RPC (`<edit-config>`, `<get-config>`) | REST verbs (GET/POST/PUT/PATCH/DELETE) |
| Datastores | running, **candidate**, startup | running (no candidate) |
| Transactions | **candidate + `<commit>`/`<discard-changes>`** (rollback) | none |

Both are driven by **YANG** models. NETCONF's candidate datastore gives
transactional, roll-back-able configuration; RESTCONF trades that for simple
REST/CRUD semantics.

## EEM (Embedded Event Manager)
On-box automation: an **event detector** fires **actions**.
```
event manager applet LINK_DOWN
 event syslog pattern "%LINK-3-UPDOWN.*GigabitEthernet0/1.*down"
 action 1.0 cli command "enable"
 action 1.5 cli command "show ip interface brief"
 action 2.0 syslog msg "Gi0/1 went down - captured state"
```
Event detectors include **syslog, snmp, interface, timer, counter, none**
(`event none` = run manually). Actions run CLI, send syslog/mail/SNMP, or trigger
a Tcl/Python policy.

## Model-driven telemetry (MDT)
Push-based streaming of operational data per a **subscription** — **periodic**
or **on-change** — over gRPC/gNMI (or NETCONF), using YANG paths. It replaces
high-overhead SNMP polling at scale (SNMP pulls; telemetry pushes).

## Controllers & APIs
Programmatic control via REST. Typical flow against **Catalyst Center (DNA
Center)**: `POST /dna/system/api/v1/auth/token` with credentials → receive a
token → send it in the **`X-Auth-Token`** header on every later call. (Elsewhere
you'll see `Authorization: Bearer <token>`.) Cisco controllers: Catalyst Center
(campus), vManage (SD-WAN), APIC (ACI), Meraki Dashboard API.

## Exam cues
- NETCONF = SSH 830 + candidate/commit; RESTCONF = HTTPS 443, no commit. Both YANG.
- EEM = event (syslog/snmp/timer/interface/none) → action (cli/syslog/mail).
- Telemetry pushes (periodic/on-change); SNMP polls.
- Catalyst Center auth token → `X-Auth-Token` header.
