# Troubleshooting Methodology & Tools

The troubleshooting domain is the largest on the exam, and it starts with a process
you must know in order. Then it tests the tools you reach for at each step. This
lesson does the method first, then the software and hardware tools that put it into
practice.

## The 7-step methodology

CompTIA teaches a specific **seven-step** process, and the exam will ask you to put
the steps in order or name the step a scenario is in. Learn them as a sequence:

1. **Identify the problem.** Gather information, question users, identify symptoms,
   determine if anything recently **changed**, and duplicate the problem if you can.
   Approach multiple problems individually.
2. **Establish a theory of probable cause.** Question the obvious first. Consider the
   OSI model — work top-to-bottom or bottom-to-top.
3. **Test the theory to determine the cause.** If it's confirmed, move on. If not,
   form a new theory — or **escalate** if it's beyond you.
4. **Establish a plan of action** to resolve the problem, and identify the potential
   **effects** of your fix.
5. **Implement the solution** — or escalate as necessary.
6. **Verify full system functionality** and, if applicable, implement **preventive
   measures** so it doesn't recur.
7. **Document** findings, actions, outcomes, and lessons learned.

> Two things the exam hammers: **"what changed?"** belongs to **step 1 (identify)**,
> and **documenting** is always the **last** step — never skip it. A mnemonic for the
> order: "**I**dentify, **T**heory, **T**est, **P**lan, **I**mplement, **V**erify,
> **D**ocument."

A few principles ride along with the steps:

- **Don't guess-and-swap randomly** — follow the method so you actually learn the
  cause.
- **Change one thing at a time** so you know what fixed it.
- **Bottom-up** (start at Layer 1 — is it plugged in?) is often fastest for physical
  symptoms; **top-down** suits application complaints; **divide and conquer** starts
  in the middle.

## Software connectivity tools

These are the commands you run to pinpoint where connectivity breaks. Know what each
tells you.

| Tool | What it does |
|------|--------------|
| **ping** | Tests reachability and round-trip time with ICMP echo |
| **traceroute / tracert** | Shows each router hop to a destination, with latency |
| **nslookup / dig** | Queries DNS — resolves names, checks records |
| **ipconfig / ifconfig / ip** | Shows a host's IP, mask, gateway, DNS |
| **arp -a** | Shows the MAC-to-IP table (catch ARP problems) |
| **netstat** | Shows active connections and listening ports |
| **nmap** | Scans hosts for open ports and services |
| **tcpdump / Wireshark** | Captures and inspects actual packets |
| **pathping / mtr** | Combines ping and traceroute over time |
| **route** | Views or edits the local routing table |

How you actually use them, in order of depth:

> **ping** answers "is it reachable?" If ping to an IP works but names fail, it's
> **DNS** — confirm with **nslookup**. If a far host is unreachable, **traceroute**
> shows *where* the path dies (the last hop that answers is near the break). When you
> need to see the real traffic — wrong ports, malformed packets, no reply — capture
> with **tcpdump** or Wireshark.

A classic sequence: `ping 127.0.0.1` (is my own stack alive?) → `ping` my gateway (is
the local link good?) → `ping` a public IP like `8.8.8.8` (is routing out working?) →
`ping` a name (is DNS working?). Each step isolates one layer.

> **ping 8.8.8.8 succeeds but `ping google.com` fails = DNS problem**, because IP
> routing clearly works and only name resolution is broken. This exact scenario is a
> near-certain exam item.

`ipconfig`/`ip` is where you catch an **APIPA** address (`169.254.x.x`) — the tell
that DHCP failed — or a wrong gateway/mask. `netstat` and `nmap` reveal which ports
are open, useful when a *service*, not the network, is the problem.

## Hardware tools

When the problem is physical — a bad cable, a dead run, no signal — software can't
help. These are the field tools:

| Tool | What it finds |
|------|---------------|
| **Cable tester** | Continuity and correct pinout of a copper cable |
| **Toner probe (fox & hound)** | Which cable/jack is which in a bundle |
| **Loopback plug** | Tests a port by looping its transmit to receive |
| **Optical power / light meter** | Measures signal strength on fiber |
| **OTDR** | Finds the distance to a break or fault on fiber |
| **Multimeter** | Voltage, continuity, resistance (power issues) |
| **Punchdown tool** | Seats wires into a 110 block / patch panel |
| **Crimper** | Attaches an RJ45 connector to a cable |
| **Wi-Fi analyzer** | Shows channels, signal, interference, rogue APs |
| **Spectrum analyzer** | Finds non-Wi-Fi RF interference |

> Match the tool to the symptom: **toner probe** to *trace and identify* a mystery
> cable in a bundle; **cable tester** to prove a cable's wiring is *good*; **OTDR** to
> locate *where* a fiber is broken; **Wi-Fi analyzer** to find channel overlap and
> rogue access points.

## Walking one problem through the method

Let's tie it together with a short scenario: *a user says "the internet is down."*

1. **Identify** — you ask what exactly fails and learn web pages won't load, and that
   it started this morning (something changed overnight).
2. **Theory** — could be the cable, DHCP, the gateway, or DNS. You question the
   obvious first.
3. **Test** — `ipconfig` shows a valid address and gateway (not APIPA), so DHCP is
   fine. `ping 8.8.8.8` succeeds but `ping google.com` fails. That confirms the
   theory: it's **DNS**.
4. **Plan** — you'll point the client at a known-good DNS server, and note it will
   only affect name resolution, nothing else.
5. **Implement** — you fix the DNS setting (or flush the cache).
6. **Verify** — `ping google.com` now resolves and pages load; you confirm other
   sites work too.
7. **Document** — you record the cause, the fix, and that the DNS server had changed,
   so the next person isn't starting from scratch.

The methodology tells you *where* to look; these tools tell you *what's wrong* once
you're there. Together they're most of the troubleshooting domain. The next lesson
applies them to specific cabling, service, and performance faults.

## On the exam

- Know the **7 steps in order**: identify → theory → test → plan → implement → verify
  → **document**. "What changed?" is step 1; **document** is always last.
- Expect "which step is this scenario in?" and ordering questions. Change one thing
  at a time; bottom-up for physical, top-down for application issues.
- **ping** = reachability (ICMP), **traceroute** = per-hop path and where it breaks,
  **nslookup/dig** = DNS, **ipconfig/ip** = local addressing (spot APIPA),
  **tcpdump/Wireshark** = packet capture, **netstat/nmap** = ports.
- The signature case: **ping to IP works, ping to name fails → DNS.**
- Hardware tools by job: **toner probe** traces a cable, **cable tester** verifies
  wiring, **loopback plug** tests a port, **OTDR/light meter** for fiber, **Wi-Fi/
  spectrum analyzer** for wireless interference.
