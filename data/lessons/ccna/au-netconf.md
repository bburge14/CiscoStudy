# NETCONF, RESTCONF & Data Formats

For years, the only way to set up a router or switch was to log in and type
commands at the **command line** (the CLI, short for *command-line interface*),
then read the text it printed back. That's fine for a person. But when you want a
*program* to configure hundreds of devices, it falls apart. The program has to
pretend to be a human — send a command, then squint at the reply and fish the
useful bits out of text that was written for human eyes. People call this
"screen-scraping," and it breaks the moment the wording of a message changes.

Modern management fixes this with one simple idea: hand the device a structured
**form** to fill in, instead of a wall of text to read.

## The shared blueprint: YANG

Picture a standard paper form — the kind where every field is labeled and sits in
a fixed spot: name here, date there, address below. If every office agrees to use
the *same* form, a machine can fill it out and read it back with no guessing.

**YANG** is that agreed-upon blueprint. It's a *data model* — a structured
description of everything a device has: its **configuration** (the settings you
choose) and its **state** (live readings like uptime, or whether a port is up).
YANG doesn't send anything by itself. Its whole job is to define the *shape* of
the form, so both sides agree on what the fields are and what goes in them.

> **YANG is the shared blueprint of what a device looks like. NETCONF and
> RESTCONF are two delivery services that carry filled-in forms to the device and
> bring the answers back.**

Both of them are built on YANG. That's the one sentence to keep. Now meet the two
delivery services — they do the same job in two different styles.

## NETCONF: the careful one

**NETCONF** (Network Configuration Protocol) travels inside **SSH** — the same
secure, encrypted login channel you already use — on **TCP port 830**. It speaks
**XML**, a tag-based language you'll see in a moment.

The way you talk to it is by calling little named actions, called **RPCs**
(*remote procedure calls* — you're asking the device to run a procedure for you).
The two you'll meet most are `<get>` to read something and `<edit-config>` to
change something.

Here's what makes NETCONF special, and why engineers trust it for risky changes.
A device running NETCONF keeps its settings in more than one place, called
**datastores**: the **running** store is the live config in effect right now,
**startup** is what loads after a reboot, and **candidate** is a scratch copy — a
draft. You can pile all your changes into the candidate without touching the live
device at all. When everything is staged and you're happy, you send one
`<commit>` and every change lands at once (this all-or-nothing behavior is called
a *transaction*). Changed your mind? `<discard-changes>` throws the draft away and
nothing ever happened. That safety net — stage, then commit or roll back — is the
reason NETCONF exists.

## RESTCONF: the web-style one

**RESTCONF** does the same job using the everyday machinery of the web. It rides
on **HTTPS** — exactly what your browser uses for secure sites — on **TCP port
443**. Instead of special RPCs, it uses the ordinary **HTTP verbs** every website
already speaks: `GET` to read, `POST` to create, `PUT` and `PATCH` to update, and
`DELETE` to remove. (Those four jobs — create, read, update, delete — are often
shortened to *CRUD*.) And it can speak either **XML or JSON**, your choice. You
point at the piece you want with a web-style address, a **URI** (like a URL), for
example `/restconf/data/ietf-interfaces:interfaces`.

The trade-off: RESTCONF works against the **running** datastore only. There's
**no candidate and no commit** — each request takes effect on its own, the moment
you send it. So it's simpler and friendlier to anyone who's used a web API, but it
lacks NETCONF's stage-everything-then-commit safety.

To turn both on, an IOS-XE device needs just a few lines:

```
netconf-yang
restconf
ip http secure-server
```

## The data formats they speak

A quick tour of the three text formats you'll meet, since the protocols above
carry their data in them.

**JSON** (JavaScript Object Notation) is the one you'll see most. It has only a
handful of building blocks: curly braces `{}` hold an **object** (a bundle of
labeled fields, just like our form); square brackets `[]` hold an **array** (an
ordered list); then plain values — a `"string"` in quotes, a number, `true`/
`false` (a yes/no value called a **boolean**), and `null` (nothing there). Here's
a device described in JSON:

```json
{
  "hostname": "R1",
  "uptime": 3600,
  "enabled": true,
  "interfaces": ["Gi0/0", "Gi0/1", "Lo0"]
}
```

Read it top to bottom: the hostname is the string `"R1"`, uptime is the number
`3600`, `enabled` is the boolean `true`, and `interfaces` is an **array** — a list
of three port names.

**XML** (eXtensible Markup Language) carries the same information with opening and
closing tags, like `<hostname>R1</hostname>`. It's more verbose — lots of typing —
and it's NETCONF's native encoding.

**YAML** is the one where spacing matters: you line things up with **spaces, never
tabs**. A `- ` marks each item in a list, and `key: value` is a labeled field.
It's what Ansible playbooks are written in.

## Reading JSON in Python

JSON lines up almost perfectly with the data types Python already has, which is
why they're such a natural pair. A JSON object becomes a Python `dict`, an array
becomes a `list`, a string becomes `str`, `true`/`false` become `bool`, and
`null` becomes `None`.

Once it's in Python, you walk into the data one step at a time: use `['key']` to
open a labeled field and `[index]` to grab an item from a list by its position
(counting from 0). So this line:

```python
name = data['ietf-interfaces:interfaces']['interface'][0]['name']
```

reads as: start at `data`, open the `ietf-interfaces:interfaces` field, open
`interface` inside it (which is a list), take the **first** item `[0]`, and read
its `name`. One hop at a time, left to right.

## The whole thing in one paragraph

Instead of a program pretending to be a human typing CLI commands, model-driven
management hands the device a structured form. **YANG** is the blueprint for that
form — it describes a device's config and state — and **NETCONF** and **RESTCONF**
are the two protocols that fill it in and read it back. NETCONF is the careful
one: it rides on SSH (port 830), speaks XML, and lets you stage changes in a
candidate datastore and then `<commit>` them all at once or discard them.
RESTCONF is the web-style one: it rides on HTTPS (port 443), uses plain HTTP
verbs, speaks XML or JSON, and writes straight to the running config with no
commit step. The data itself travels as JSON, XML, or YAML — and JSON maps so
cleanly onto Python's dicts and lists that you can walk into it one key or index
at a time.

### See it on a real device

```
show netconf-yang sessions
show running-config | include netconf|restconf
```
