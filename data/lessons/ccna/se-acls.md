# Access Control Lists (ACLs)

Imagine a bouncer standing at a door with a printed guest list. Each person
walks up, and the bouncer reads the list from the top, line by line, looking
for a rule about this person. The moment one line matches, the bouncer acts on
it — let them in or turn them away — and stops reading. That is exactly what a
router does with an **Access Control List (ACL)**: it is an ordered list of
permit ("let it through") and deny ("drop it") rules, and the router checks
traffic against them from the top down.

The part people forget is what happens when nobody on the list matches. There
is one more rule you never see written, sitting silently at the very bottom:

> **A router reads an ACL top-down and acts on the *first* rule that matches,
> then stops. If nothing matches, an invisible `deny any` at the end throws the
> traffic away.**

That hidden `deny any` (often called the *implicit deny*) is why an ACL that has
only permit rules will still block anything you forgot to mention. Keep it in
mind — it is the single biggest source of "but I never told it to block that!"
surprises.

## Two flavors: standard and extended

ACLs come in two kinds, and the difference is simply *how much they are allowed
to look at.*

A **standard ACL** can only look at one thing: where the traffic came **from**
(its source IP address). That's all. Standard ACLs use the number ranges
**1–99** and **1300–1999**.

An **extended ACL** can look at much more: the source *and* the destination, the
protocol, and the Layer 4 **port** numbers (a port is the number that says "this
is web traffic" or "this is SSH"). Extended ACLs use **100–199** and
**2000–2699**.

This difference decides *where you should put each one*, and the reasoning is
worth understanding rather than memorizing. A standard ACL only knows the
source, so if you placed it near the source it would block that sender's traffic
to *everywhere* — including the places it's perfectly allowed to go. To avoid
that over-blocking, you put a **standard ACL close to the destination**, where it
only affects traffic actually arriving there. An extended ACL is precise — it
knows source, destination, and port — so it can safely drop exactly the unwanted
traffic right where it starts. You put an **extended ACL close to the source** to
throw that traffic out early, before it wastes bandwidth crossing the whole
network.

## Wildcard masks: a quick refresher

ACLs match groups of addresses using a **wildcard mask**, which is the mirror
image of a subnet mask: a **0 means "this bit must match"** and a **1 means
"don't care."** Two shorthands save you typing. Writing `host 192.168.1.17` means
that one exact address — it is the same as writing `192.168.1.17 0.0.0.0`.
Writing `any` means every address — the same as `0.0.0.0 255.255.255.255`. And a
wider range like `10.1.0.0 0.0.3.255` matches everything from `10.1.0.0` to
`10.1.3.255` (that's a /22). The classic trap is swapping the subnet mask and the
wildcard — they look alike but mean opposite things, so always check which one
the command wants.

## Walking through a real one

Here's a named extended ACL that blocks one PC from reaching one web server and
lets everything else through:

```
ip access-list extended BLOCK_WEB
 deny tcp host 10.1.1.10 host 203.0.113.5 eq 80
 permit ip any any
interface Gi0/0
 ip access-group BLOCK_WEB in
```

Read it the way the router does. First line: if this is TCP from `10.1.1.10` to
`203.0.113.5` on port 80 (web), drop it. Second line: permit everything else.
That second line matters enormously — without that `permit ip any any`, the
invisible `deny any` at the bottom would silently drop *all* other traffic too.
Finally, `ip access-group BLOCK_WEB in` is what actually sticks the list onto an
interface and in a direction; until you do that, the ACL does nothing at all.

## Order is everything

Because the first match wins, the *order* of your rules changes the outcome. A
specific `deny` must come **before** a broad `permit` that would also match —
otherwise the permit catches the traffic first and your deny never gets a turn.
With named ACLs you don't have to retype the whole list to fix this; you can
slide a rule into a spot using a sequence number:

```
ip access-list extended BLOCK_WEB
 15 deny tcp host 10.1.1.11 any eq 443
```

That inserts a new deny at line 15, wherever that falls in the order.

## The whole thing in one paragraph

An ACL is an ordered list of permit/deny rules that a router checks top-down,
acting on the first match and ignoring the rest, with a hidden `deny any` that
drops anything no rule allowed. A standard ACL matches the source address only,
so you place it near the destination to avoid over-blocking; an extended ACL
matches source, destination, protocol, and ports, so you place it near the
source to drop unwanted traffic early. Match groups of addresses with wildcard
masks (where `host X` is one address and `any` is all of them), always remember
to permit the traffic you *do* want so the implicit deny doesn't eat it, and put
specific denies ahead of broad permits so they actually fire.

### See it on a real device
```
show access-lists
show ip access-lists BLOCK_WEB
show ip interface g0/0 | include access list
```
The `show access-lists` output includes a match count on each line, which is the
fastest way to confirm which rule is actually catching your traffic.
