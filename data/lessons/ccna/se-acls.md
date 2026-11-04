# Access Control Lists (ACLs)

An ACL is an ordered list of permit/deny rules matched **top-down, first-match
wins**, with an **implicit `deny any`** at the end that is never shown.

## Standard vs extended
| | Standard | Extended |
|--|----------|----------|
| Numbers | 1–99, 1300–1999 | 100–199, 2000–2699 |
| Matches | **source IP only** | source + destination, protocol, L4 ports |
| Placement | close to the **destination** | close to the **source** |

Standard ACLs match only the source, so placing them near the source would
over-block legitimate traffic — put them near the destination. Extended ACLs are
specific, so place them near the source to drop unwanted traffic early.

## Wildcard masks in ACLs
- `host 192.168.1.17` == `192.168.1.17 0.0.0.0` (exact match).
- `any` == `0.0.0.0 255.255.255.255` (match everything).
- `10.1.0.0 0.0.3.255` matches 10.1.0.0–10.1.3.255 (a /22).

Remember a wildcard is the **inverse** of a subnet mask (0 = must match,
1 = don't care). Swapping mask and wildcard is the classic trap.

## Named extended ACL example
```
ip access-list extended BLOCK_WEB
 deny tcp host 10.1.1.10 host 203.0.113.5 eq 80
 permit ip any any
interface Gi0/0
 ip access-group BLOCK_WEB in
```
Don't forget the `permit ip any any` — otherwise the implicit `deny any` drops
everything else.

## Order matters
A more specific `deny` must come **before** a broad `permit`, or the permit will
match first and the deny never fires. Named ACLs let you insert/delete by
sequence number:
```
ip access-list extended BLOCK_WEB
 15 deny tcp host 10.1.1.11 any eq 443
```

## Verify
```
show access-lists
show ip access-lists BLOCK_WEB
show ip interface g0/0 | include access list
```
`show access-lists` shows per-line **match counts** — invaluable for confirming
which rule is catching traffic.

## Exam cues
- Standard → near destination; extended → near source.
- Implicit `deny any` at the end of every ACL.
- First match wins; order your specific denies before broad permits.
- `host X` = `X 0.0.0.0`; `any` = `0.0.0.0 255.255.255.255`.
