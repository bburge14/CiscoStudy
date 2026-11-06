# Network & Printer Troubleshooting

Two of the most common help-desk tickets are "I can't get on the network" and
"the printer isn't working right." Both reward a calm, layered approach: start at
the physical connection and work up, matching each symptom to its usual cause.
This lesson gives you the symptom-to-cause map for networks and printers, plus the
tools that confirm what you suspect.

## Troubleshooting network connectivity

Work from the bottom up: is it plugged in, does it have an address, can it reach
names and the internet? The symptom usually tells you which rung broke.

### Reading the symptoms

- **No connectivity** — nothing works. Check the cable, the link lights on the
  NIC and switch, and whether the interface is enabled. No link light = a
  physical/cable problem.
- **Limited / no internet, APIPA address** — if `ipconfig` shows an address like
  **169.254.x.x**, that is an **APIPA** (automatic private, link-local) address,
  which means the PC **could not reach a DHCP server** and gave up. The fix is at
  the DHCP server or the path to it, not the PC. This is one of the most tested
  network clues.

> **169.254.x.x = DHCP failed.** The client assigned itself an APIPA address
> because no DHCP server answered. Check the DHCP server, the cable, or the switch
> path.

- **Intermittent connectivity** — comes and goes; suspect a marginal cable, a
  loose connector, interference (on Wi-Fi), or a failing port that is **flapping**
  (link bouncing up and down).
- **Slow speeds** — a duplex mismatch, a saturated link, a damaged cable forcing a
  lower speed, or Wi-Fi congestion.
- **High latency and jitter** — delay and *variation* in delay, which hurt voice
  and video; caused by congestion or a weak path.
- **Low RF / weak Wi-Fi signal** — distance, walls, or interference. Moving
  closer, changing channels, or repositioning the AP helps.
- **Wrong SSID or passphrase** — a wireless client that will not join is often
  pointed at the wrong network or has a bad saved password.

### The command-line tools

CompTIA expects you to know which command answers which question:

| Tool | Answers |
|------|---------|
| **ping** | Is the host reachable? Round-trip time? |
| **ipconfig / ifconfig / ip** | What is my IP, mask, gateway, DNS? (spot APIPA here) |
| **tracert / traceroute** | Which hops are on the path, and where does it break? |
| **nslookup / dig** | Is DNS resolving names to addresses? |

> A quick ladder: **ping 127.0.0.1** (is my TCP/IP stack alive?) → **ping the
> gateway** (is the local network OK?) → **ping 8.8.8.8** (is the internet
> reachable by IP?) → **ping/nslookup a name** (is DNS working?). The first ping
> that fails tells you the layer at fault.

> **Can reach by IP but not by name = DNS problem.** If `ping 8.8.8.8` works but
> `ping example.com` fails, name resolution is broken — check DNS settings.

### The hardware tools

- **Cable tester** — verifies a cable's wiring/continuity end to end.
- **Loopback plug** — tests whether a NIC port can send and receive.
- **Toner probe (tone generator)** — finds which cable in a bundle is which by
  sending a tone you trace with the probe.
- **Wi-Fi analyzer** — shows channels, signal strength, and congestion for
  wireless problems.
- **Crimper / punchdown tool** — terminate RJ45 plugs and patch-panel/keystone
  jacks.

## Troubleshooting printers

Printer faults are mostly **print quality**, **paper handling**, or
**connectivity**. Quality symptoms map neatly to the laser parts you learned
earlier, so lean on that.

### Print-quality symptoms

- **Faded / light print** — most often **low toner** (laser) or low ink/clogged
  heads (inkjet). Redistribute or replace the cartridge.
- **Toner smears or rubs off the page** — the **fuser** is not melting the toner
  in; a failing fuser is the cause.
- **Repeating marks or a repeated ghost image** down the page — a defect or
  scratch on the **imaging drum** (the spacing of the repeat matches the drum's
  circumference).
- **Vertical lines or streaks** — a dirty/scratched drum or debris in the path
  (laser), or a **clogged print head** (inkjet) — run the cleaning cycle.
- **Incorrect / missing colors** — on inkjet, a clogged head or empty cartridge;
  **clean and calibrate** the heads.
- **Blank pages** — out of toner/ink, or protective tape left on a new cartridge.

### Paper-handling symptoms

- **Paper jams** — wrong paper type/weight, humidity, overfilled or misaligned
  tray, or worn **pickup/separation rollers**. Clear the jam in the direction of
  travel and check the rollers.
- **Multiple pages pulled at once** or **creased/wrinkled paper** — worn rollers
  or damp/curled paper.
- **Grinding noise / finishing issues** — a mechanical fault (gear, roller, or
  stapler/finisher unit).

### Connectivity and software symptoms

- **Garbled or gibberish output** — almost always the **wrong or corrupt printer
  driver**, or the wrong page language (PCL vs PostScript). Reinstall the correct
  driver.
- **No connectivity** — the network printer dropped off Wi-Fi/Ethernet, has a
  changed IP, or the queue points at the wrong port.
- **Jobs stuck in the queue / nothing prints** — the **print spooler** is hung.
  Clear the queue and **restart the Print Spooler service**; the backed-up jobs
  then flow.
- **"Access denied" when printing** — a permissions problem on the shared printer.

> **Garbled text = wrong driver.** **Nothing prints but jobs pile up = restart the
> print spooler.** These two are near-certain exam items.

## The whole thing in one paragraph

Troubleshoot networks bottom-up: **no link light** = cable/physical; a
**169.254.x.x APIPA** address = **DHCP failed**; **intermittent** = marginal
cable/interference/port flapping; **slow/high latency/jitter** = congestion or
duplex issues; **weak RF or wrong SSID/passphrase** = Wi-Fi problems. Confirm with
**ping** (reachability), **ipconfig** (your address — spot APIPA), **tracert**
(path), and **nslookup** (DNS — "works by IP, fails by name = DNS"), plus
hardware tools like a **cable tester, loopback plug, toner probe, and Wi-Fi
analyzer**. For printers, quality faults map to parts — **faded = low toner**,
**smearing = fuser**, **repeating marks = drum**, **streaks/missing colors =
clogged head (clean/calibrate)** — paper jams point to **rollers/paper**, garbled
output means the **wrong driver**, and jobs stuck with nothing printing means
**restart the print spooler**.

## On the exam

- **169.254.x.x (APIPA)** = the client **could not reach DHCP**. Fix DHCP/the
  path, not the PC.
- **Ping by IP works, by name fails = DNS.** Use the ping ladder (loopback →
  gateway → internet IP → name) to find the broken layer.
- Tools: **ping** (reachability), **ipconfig** (local config), **tracert** (path),
  **nslookup** (DNS), **cable tester/loopback/toner probe/Wi-Fi analyzer** for
  physical and wireless faults.
- Laser quality: **faded = toner**, **smears/rubs off = fuser**, **repeating
  marks = drum**, **vertical streaks = drum/debris**.
- Inkjet **missing colors/streaks = clogged head** → clean and calibrate.
- **Garbled/gibberish output = wrong or corrupt driver** (or wrong PCL/PostScript).
- **Jobs queue up but nothing prints = hung spooler** → clear queue and restart
  the **Print Spooler** service.
- **Paper jams / multi-feed / creasing** → worn **rollers** or wrong/damp paper.
