# NETCONF, RESTCONF & Data Formats

## Model-driven management
Instead of screen-scraping CLI, modern management uses **YANG** data models — a
structured schema describing a device's configuration and state. NETCONF and
RESTCONF are two protocols that read/write those models.

## NETCONF vs RESTCONF
| | **NETCONF** | **RESTCONF** |
|--|-------------|--------------|
| Transport | **SSH, TCP 830** | **HTTPS, TCP 443** |
| Style | RPC-based (`<edit-config>`, `<get>`) | REST (HTTP verbs) |
| Encoding | **XML** | **XML or JSON** |
| Datastores | running, **candidate**, startup | running (no candidate/commit) |
| Transactions | yes (candidate + `<commit>`, rollback) | no candidate/commit semantics |

Both are built on **YANG**. NETCONF's candidate datastore lets you stage, then
`<commit>` (or `<discard-changes>`) atomically — safe, roll-back-able changes.
RESTCONF maps CRUD onto HTTP verbs (GET/POST/PUT/PATCH/DELETE) against a URI like
`/restconf/data/ietf-interfaces:interfaces`.

Enable on IOS-XE:
```
netconf-yang
restconf
ip http secure-server
```

## Data formats
### JSON
```json
{
  "hostname": "R1",
  "uptime": 3600,
  "enabled": true,
  "interfaces": ["Gi0/0", "Gi0/1", "Lo0"]
}
```
Types: `{}` object, `[]` array, `"string"`, number, `true`/`false`, `null`.
Here `interfaces` is an **array** (list); `enabled` is a **boolean**.

### XML
Tag-based (`<hostname>R1</hostname>`); verbose; NETCONF's native encoding.

### YAML
Whitespace-significant (spaces, **never tabs**); `- ` for list items,
`key: value` for maps; used by Ansible playbooks.

## Mapping to Python
JSON decodes to Python types: object→`dict`, array→`list`, string→`str`,
true/false→`bool`, null→`None`. Navigate with `['key']` and `[index]`:
```python
name = data['ietf-interfaces:interfaces']['interface'][0]['name']
```

## Verify
```
show netconf-yang sessions
show running-config | include netconf|restconf
```

## Exam cues
- NETCONF = SSH **830**, XML, datastores + commit. RESTCONF = HTTPS **443**,
  XML/JSON, HTTP verbs.
- Both ride on **YANG**.
- JSON `[]` = array/list; `{}` = object/dict.
