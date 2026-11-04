# Automation: Data Formats, NETCONF/RESTCONF, EEM & Telemetry

Automation is about letting programs configure and watch your network, instead
of a human logging into each box and typing commands one at a time. Do that
across hundreds of devices and the savings are enormous — and mistakes drop,
because a script does the same thing every time.

Imagine running a chain of stores. Phoning each one to check stock is slow and
error-prone. It's far better if every store reports in the *same format* and you
can push one update to all of them at once. Network automation needs the same
two things: a shared way to write data down, and a way to send and receive it.

> **Automation works because machines agree on a shared way to write data down.**
> Once two programs format information the same way, one can read and configure
> the other with no human in the loop.

## Data formats: three ways to write the same list

Before programs can talk, they need a common format. You'll meet three.

**JSON** (JavaScript Object Notation) is the default for most APIs because it
maps cleanly onto programming data. It uses `{}` for an object, `[]` for an
array, `""` for a string, plus numbers, `true`/`false`, and `null`. **XML**
(eXtensible Markup Language) wraps everything in tags like `<tag>value</tag>`;
it's verbose, but it's NETCONF's native encoding. **YAML** (YAML Ain't Markup
Language) uses indentation with spaces — **never tabs** — along with `- ` for
list items and `key: value` for maps; it's what Ansible playbooks are written
in.

JSON is worth a closer look because it drops straight into Python. A JSON object
becomes a Python `dict`, an array becomes a `list`, a string becomes `str`, a
boolean becomes `bool`, and null becomes `None`. Once it's Python, you walk into
it by key and index:

```python
import json
data = json.loads(resp.text)
first = data['ietf-interfaces:interfaces']['interface'][0]['name']
```

That last line reads top-down: open the `interfaces` container, grab the
`interface` list, take the first item `[0]`, and read its `name`. You're just
following the nesting.

## NETCONF vs RESTCONF: two ways to configure devices

Both of these let a program read and change a device's configuration, and both
are driven by **YANG** — a modeling language that describes exactly what data a
device has and how it's structured. They differ in style.

**NETCONF** runs over **SSH on port 830**, speaks **XML**, and works in **RPC**
style — you send operations like `<edit-config>` and `<get-config>`. Its
superpower is safety through datastores: alongside the live **running** config
and the **startup** config, it has a **candidate** datastore. You stage all your
changes in the candidate, then apply them atomically with `<commit>` — or throw
them away with `<discard-changes>`. That's a true rollback, like editing a draft
and only publishing when you're sure.

**RESTCONF** runs over **HTTPS on port 443**, can speak **XML or JSON**, and
uses familiar **REST verbs** (GET, POST, PUT, PATCH, DELETE). It talks only to
the **running** datastore and has **no candidate and no transactions**. So
RESTCONF trades NETCONF's safe, roll-back-able staging for simple, familiar
REST/CRUD operations. Pick NETCONF when you want transactional safety; pick
RESTCONF when you want easy REST calls.

## EEM: "if this happens, do that" on the box itself

**EEM** (Embedded Event Manager) is automation that lives *on the device* — no
external server needed. The idea is a simple rule: an **event detector** watches
for something, and when it fires, a list of **actions** runs. Here's an applet
that reacts to an interface going down:

```
event manager applet LINK_DOWN
 event syslog pattern "%LINK-3-UPDOWN.*GigabitEthernet0/1.*down"
 action 1.0 cli command "enable"
 action 1.5 cli command "show ip interface brief"
 action 2.0 syslog msg "Gi0/1 went down - captured state"
```

Read it as a sentence: *when* a syslog message shows GigabitEthernet0/1 going
down, *then* enter enable mode, run `show ip interface brief`, and log a message
that state was captured. The numbered actions just run in order. The event could
instead be watched by other detectors — **syslog, snmp, interface, timer,
counter,** or **none** (where `event none` means you trigger it by hand).
Actions can run CLI commands, send syslog/mail/SNMP, or kick off a Tcl or Python
policy. It's a tiny, self-contained robot sitting on the router.

## Model-driven telemetry: devices that report on their own

**Model-driven telemetry (MDT)** is push-based streaming of operational data.
Instead of a server constantly asking the device for stats, the device streams
data to you according to a **subscription** — either **periodically** (every few
seconds) or **on-change** (only when a value actually changes) — over transports
like gRPC/gNMI (or NETCONF), using **YANG** paths to say exactly what to send.
It exists because old-style **SNMP** polling doesn't scale: SNMP *pulls* one
value at a time, while telemetry *pushes* a whole subscription on its own.
(You'll also meet telemetry in the assurance topic — same idea, viewed from the
monitoring side.)

## Controllers and APIs: the token handshake

Modern networks are often driven through a central controller's REST API rather
than box by box. The typical flow against **Catalyst Center** (formerly DNA
Center) is a two-step handshake worth knowing by heart. First you
`POST /dna/system/api/v1/auth/token` with your credentials, and the controller
hands back a **token**. From then on, you include that token in the
**`X-Auth-Token`** header on every later call, which proves you're already
logged in. It's exactly like getting a wristband at the door: show your ID once,
get the band, then just flash the band each time after.

(Not every API uses that header — in many others you'll see
`Authorization: Bearer <token>` instead.) Cisco's main controllers are
**Catalyst Center** for campus, **vManage** for SD-WAN, **APIC** for ACI
data-center fabric, and the **Meraki Dashboard API** for Meraki gear.

## The whole thing in one paragraph

Automation lets programs manage the network in a shared language. That language
is a data format — JSON (API default, maps to Python), XML (verbose, NETCONF's
native), or YAML (indentation, no tabs, used by Ansible). To push config,
NETCONF (SSH 830, XML, RPC, with a candidate datastore and commit/discard for
rollback) and RESTCONF (HTTPS 443, XML or JSON, REST verbs, running-only, no
transactions) both ride on YANG models. EEM automates on the box with an
event-then-action rule. Model-driven telemetry has the device push a
subscription of data periodically or on-change, where SNMP would only pull. And
to drive a controller like Catalyst Center, you POST for a token once and then
send it in the `X-Auth-Token` header on every call after.

### See it on a real device
```
POST /dna/system/api/v1/auth/token    → returns a token
X-Auth-Token: <token>                 → send this on every later call
```
