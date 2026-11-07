"""Interactive performance-based tasks for the CompTIA tracks.

The Cisco PBQs are a live IOS CLI simulator (``studyengine.cli_sim``). On the real
CompTIA exams the PBQs are drag-and-drop, matching and ordering tasks instead, so
these are modeled declaratively and graded by comparing the learner's arrangement
to the key — no CLI. Three kinds:

* ``categorize`` — drop each item into the correct category / bucket
* ``match``      — pair each left-hand item with its correct right-hand item
* ``order``      — put the steps into the correct sequence

Every task exposes a uniform ``rows()`` view — a list of ``(key, label, choices,
correct)`` — so one renderer and one grader handle all three kinds.
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class PerfCheck:
    description: str
    passed: bool


@dataclass
class PerfTask:
    id: str
    exam: str
    domain: str
    title: str
    prompt: str
    kind: str                                   # "categorize" | "match" | "order"
    success: str = "Task resolved — nicely done."
    explain: str = ""
    # categorize
    buckets: list[str] = field(default_factory=list)
    item_bucket: dict[str, str] = field(default_factory=dict)   # item -> correct bucket
    # match
    pairs: dict[str, str] = field(default_factory=dict)          # left -> correct right
    right_options: list[str] = field(default_factory=list)       # pool to pick from (defaults to the values)
    # order
    steps: list[str] = field(default_factory=list)               # the CORRECT order

    # -- uniform view the UI iterates over ------------------------------------
    def rows(self) -> list[tuple[str, str, list[str], str]]:
        """(row_key, display_label, choices, correct_choice) for each row."""
        if self.kind == "categorize":
            return [(it, it, list(self.buckets), bucket) for it, bucket in self.item_bucket.items()]
        if self.kind == "match":
            opts = list(self.right_options) or list(self.pairs.values())
            return [(left, left, opts, right) for left, right in self.pairs.items()]
        if self.kind == "order":
            return [(f"pos{i}", f"Step {i}", list(self.steps), self.steps[i - 1])
                    for i in range(1, len(self.steps) + 1)]
        raise ValueError(f"{self.id}: unknown kind {self.kind!r}")

    def grade(self, response: dict) -> list[PerfCheck]:
        """response maps row_key -> chosen value. One PerfCheck per row (the
        description is the row label only — the correct value is NOT revealed, so
        a learner can't pass by reading the feedback)."""
        return [PerfCheck(label, response.get(key) == correct)
                for key, label, _choices, correct in self.rows()]

    def passed(self, response: dict) -> bool:
        checks = self.grade(response)
        return bool(checks) and all(c.passed for c in checks)


# ===========================================================================
# Authored tasks
# ===========================================================================
PERF_TASKS: list[PerfTask] = [
    # ---- Security+ --------------------------------------------------------
    PerfTask(
        id="secplus-pbq-controls", exam="secplus", domain="general_security_concepts",
        kind="categorize", title="Classify the security controls",
        prompt="A new compliance report asks you to sort each safeguard into its **control "
               "category**. Drop every control into the correct category.",
        buckets=["Technical", "Managerial", "Operational", "Physical"],
        item_bucket={
            "Firewall rule": "Technical",
            "Full-disk encryption": "Technical",
            "Multifactor authentication": "Technical",
            "Written security policy": "Managerial",
            "Annual risk assessment": "Managerial",
            "Security awareness training": "Operational",
            "User access reviews": "Operational",
            "Security guard at the lobby": "Physical",
            "Bollards outside the entrance": "Physical",
        },
        explain="Category = *how* the control is carried out: technology enforces technical "
                "controls; policies and governance are managerial; people performing a procedure "
                "are operational; a physical barrier is physical.",
        success="Every control is in the right category.",
    ),
    PerfTask(
        id="secplus-pbq-mitigations", exam="secplus", domain="threats_vulns_mitigations",
        kind="match", title="Match each attack to its best mitigation",
        prompt="Each row is an attack. Match it to the **single best** mitigation.",
        pairs={
            "SQL injection": "Input validation / parameterized queries",
            "Cross-site scripting (XSS)": "Output encoding",
            "Phishing": "Security awareness training",
            "ARP poisoning": "Dynamic ARP inspection",
            "Brute-force login": "Account lockout policy",
            "Tailgating": "Access control vestibule",
        },
        explain="Tie the defense to where the attack happens: injection/XSS are input/output "
                "handling, phishing is a people problem, ARP poisoning is a switch feature, "
                "brute force is stopped by lockout, tailgating is physical.",
        success="Every attack is paired with the right mitigation.",
    ),
    PerfTask(
        id="secplus-pbq-ir", exam="secplus", domain="security_operations",
        kind="order", title="Order the incident response phases",
        prompt="Put the **NIST incident response** phases in the correct order, from first to last.",
        steps=["Preparation", "Detection and analysis", "Containment", "Eradication",
               "Recovery", "Lessons learned"],
        explain="Prepare before anything happens; detect/analyze; contain to stop the spread; "
                "eradicate the cause; recover to normal; then review lessons learned.",
        success="Correct incident response order.",
    ),
    # ---- Network+ ---------------------------------------------------------
    PerfTask(
        id="netplus-pbq-ports", exam="netplus", domain="networking_concepts",
        kind="match", title="Match the service to its default port",
        prompt="Match each service/protocol to its **default port number**.",
        pairs={"SSH": "22", "DNS": "53", "DHCP (server)": "67", "HTTPS": "443",
               "SMB": "445", "RDP": "3389"},
        right_options=["22", "53", "67", "443", "445", "3389"],
        explain="SSH 22, DNS 53, DHCP 67/68, HTTPS 443, SMB 445, RDP 3389.",
        success="Every service is on the right port.",
    ),
    PerfTask(
        id="netplus-pbq-osi", exam="netplus", domain="networking_concepts",
        kind="order", title="Order the OSI layers",
        prompt="Put the **OSI model** layers in order, from **Layer 1 (bottom)** up to **Layer 7**.",
        steps=["Physical", "Data Link", "Network", "Transport", "Session",
               "Presentation", "Application"],
        explain="Please Do Not Throw Sausage Pizza Away — Physical, Data Link, Network, "
                "Transport, Session, Presentation, Application.",
        success="OSI layers in the right order.",
    ),
    PerfTask(
        id="netplus-pbq-ts", exam="netplus", domain="network_troubleshooting",
        kind="order", title="Order the troubleshooting methodology",
        prompt="Put the **CompTIA 7-step troubleshooting methodology** in order.",
        steps=["Identify the problem", "Establish a theory of probable cause",
               "Test the theory to determine the cause", "Establish a plan of action",
               "Implement the solution or escalate", "Verify full system functionality",
               "Document findings, actions, and outcomes"],
        explain="Identify → theory → test theory → plan → implement/escalate → verify → document.",
        success="Correct troubleshooting order.",
    ),
    # ---- A+ Core 1 --------------------------------------------------------
    PerfTask(
        id="aplus1-pbq-raid", exam="aplus1", domain="hardware",
        kind="match", title="Match each RAID level to its behavior",
        prompt="Match each **RAID level** to what it actually does.",
        pairs={
            "RAID 0": "Striping, no redundancy (speed/capacity)",
            "RAID 1": "Mirroring (exact copy on two disks)",
            "RAID 5": "Striping with distributed parity",
            "RAID 10": "A stripe of mirrored pairs",
        },
        explain="0 = stripe (fast, no fault tolerance), 1 = mirror, 5 = stripe + parity "
                "(survive one disk), 10 = mirror then stripe.",
        success="Every RAID level is matched correctly.",
    ),
    PerfTask(
        id="aplus1-pbq-laser", exam="aplus1", domain="hardware",
        kind="order", title="Order the laser printing process",
        prompt="Put the **seven steps of the laser imaging process** in order.",
        steps=["Processing", "Charging", "Exposing", "Developing", "Transferring",
               "Fusing", "Cleaning"],
        explain="Processing, Charging, Exposing, Developing, Transferring, Fusing, Cleaning.",
        success="Correct laser imaging order.",
    ),
    PerfTask(
        id="aplus1-pbq-cloud", exam="aplus1", domain="virtualization_cloud",
        kind="categorize", title="Classify the cloud service models",
        prompt="Sort each offering into the **cloud service model** it represents.",
        buckets=["IaaS", "PaaS", "SaaS"],
        item_bucket={
            "Rented virtual machines you manage the OS on": "IaaS",
            "Raw cloud storage and networking you configure": "IaaS",
            "A managed runtime/database to deploy your code on": "PaaS",
            "A developer platform with the OS/middleware managed for you": "PaaS",
            "Web-based email used in a browser": "SaaS",
            "A CRM application accessed entirely online": "SaaS",
        },
        explain="IaaS = you manage the OS and up; PaaS = you manage just your app/data; "
                "SaaS = you just use the finished application.",
        success="Every service is in the right model.",
    ),
    # ---- A+ Core 2 --------------------------------------------------------
    PerfTask(
        id="aplus2-pbq-malware", exam="aplus2", domain="security_a2",
        kind="order", title="Order the malware removal procedure",
        prompt="Put CompTIA's **best-practice malware removal** steps in order.",
        steps=["Investigate and verify malware symptoms", "Quarantine the infected systems",
               "Disable System Restore (in Windows)",
               "Remediate: update anti-malware, then scan and remove",
               "Schedule scans and run updates",
               "Re-enable System Restore and create a restore point",
               "Educate the end user"],
        explain="Verify → quarantine → disable System Restore → remediate → schedule scans → "
                "re-enable System Restore → educate the user.",
        success="Correct malware removal order.",
    ),
    PerfTask(
        id="aplus2-pbq-cmd", exam="aplus2", domain="operating_systems",
        kind="match", title="Match the command to what it does",
        prompt="Match each **command-line tool** to its function.",
        pairs={
            "ipconfig": "Show the IP configuration",
            "sfc": "Scan and repair protected system files",
            "chkdsk": "Check a disk for errors",
            "gpupdate": "Refresh Group Policy settings",
            "nslookup": "Query DNS name resolution",
            "ping": "Test reachability to a host",
        },
        explain="ipconfig = IP info, sfc = system file checker, chkdsk = disk check, "
                "gpupdate = apply policy, nslookup = DNS, ping = reachability.",
        success="Every command is matched correctly.",
    ),
    PerfTask(
        id="aplus2-pbq-backup", exam="aplus2", domain="operational_procedures",
        kind="match", title="Match each backup type to its description",
        prompt="Match each **backup type** to how it works.",
        pairs={
            "Full": "Copies all selected data every time",
            "Incremental": "Copies data changed since the last backup of any type",
            "Differential": "Copies data changed since the last full backup",
            "Synthetic full": "Merges a full plus later increments into a new full",
        },
        explain="Incremental = since last backup (small, slow restore); differential = since "
                "last full (grows, faster restore); synthetic = assembled server-side.",
        success="Every backup type is matched correctly.",
    ),

    # ===== Security+ (round 2) =============================================
    PerfTask(
        id="secplus-pbq-crypto", exam="secplus", domain="general_security_concepts",
        kind="match", title="Match each algorithm to its cryptographic role",
        prompt="Match each **algorithm / primitive** to what it is used for.",
        pairs={
            "AES": "Symmetric encryption",
            "RSA": "Asymmetric encryption",
            "SHA-256": "Hashing (integrity)",
            "Diffie-Hellman": "Key exchange",
            "HMAC": "Message authentication",
            "bcrypt": "Password hashing / key stretching",
        },
        explain="AES = symmetric (one shared key); RSA = asymmetric (public/private); SHA = hash; "
                "DH = agree on a key over an open channel; HMAC = keyed integrity; bcrypt = slow "
                "password hashing.",
        success="Every algorithm is in the right role.",
    ),
    PerfTask(
        id="secplus-pbq-controltypes", exam="secplus", domain="general_security_concepts",
        kind="categorize", title="Classify the control by TYPE",
        prompt="Sort each control into its **control type** (what it does relative to an incident).",
        buckets=["Preventive", "Detective", "Corrective", "Deterrent"],
        item_bucket={
            "Firewall rule blocking a port": "Preventive",
            "Disabling an unused account": "Preventive",
            "IDS alert on suspicious traffic": "Detective",
            "Reviewing audit logs": "Detective",
            "Restoring a server from backup": "Corrective",
            "Isolating and re-imaging a host": "Corrective",
            "Warning banner at logon": "Deterrent",
            "Visible 'monitored premises' signage": "Deterrent",
        },
        explain="Before = preventive (stop it) or deterrent (discourage it); during/after-spotting "
                "= detective; after-to-fix = corrective.",
        success="Every control is the right type.",
    ),
    PerfTask(
        id="secplus-pbq-accessmodels", exam="secplus", domain="security_operations",
        kind="match", title="Match the access-control model",
        prompt="Match each **access control model** to how access is decided.",
        pairs={
            "MAC (Mandatory)": "System-enforced labels/clearances users can't change",
            "DAC (Discretionary)": "The data owner grants access at their discretion",
            "RBAC (Role-based)": "Access follows the user's job role / group",
            "ABAC (Attribute-based)": "Access from attributes (dept, time, location)",
            "Rule-based": "System-wide rules (e.g., an ACL by time of day)",
        },
        explain="MAC = labels set by the system; DAC = owner decides; RBAC = by role; "
                "ABAC = by attributes; rule-based = global rules.",
        success="Every model is matched correctly.",
    ),
    PerfTask(
        id="secplus-pbq-volatility", exam="secplus", domain="security_operations",
        kind="order", title="Order of volatility (forensics)",
        prompt="In digital forensics you collect evidence **most-volatile first**. Put these in "
               "order from most volatile to least.",
        steps=["CPU cache and registers", "RAM (system memory)", "Swap / page file",
               "Data on disk", "Remote logs / monitoring data", "Backups and archival media"],
        explain="RFC 3227: registers/cache → RAM → swap → disk → remote logs → backups.",
        success="Correct order of volatility.",
    ),
    PerfTask(
        id="secplus-pbq-authproto", exam="secplus", domain="security_operations",
        kind="match", title="Match the identity / AAA protocol",
        prompt="Match each **protocol** to its primary use.",
        pairs={
            "RADIUS": "Network-access AAA (UDP)",
            "TACACS+": "Device administration AAA (TCP, per-command)",
            "SAML": "Web single sign-on assertions (IdP ↔ SP)",
            "Kerberos": "Ticket-based auth on a Windows domain",
            "OAuth 2.0": "Delegated authorization with access tokens",
            "LDAP": "Directory lookups / authentication",
        },
        explain="RADIUS = network access; TACACS+ = device admin; SAML = web SSO; Kerberos = "
                "domain tickets; OAuth = delegated authz; LDAP = the directory itself.",
        success="Every protocol is matched correctly.",
    ),

    # ===== Network+ (round 2) =============================================
    PerfTask(
        id="netplus-pbq-dns", exam="netplus", domain="network_operations",
        kind="match", title="Match each DNS record type",
        prompt="Match each **DNS record type** to what it does.",
        pairs={
            "A": "Maps a name to an IPv4 address",
            "AAAA": "Maps a name to an IPv6 address",
            "CNAME": "Alias from one name to another name",
            "MX": "Mail server for the domain",
            "PTR": "Reverse lookup — IP address to name",
            "NS": "Authoritative name server for the zone",
            "TXT": "Text data (SPF / DKIM / verification)",
        },
        explain="A = IPv4, AAAA = IPv6, CNAME = alias, MX = mail, PTR = reverse, NS = name server, "
                "TXT = text (SPF/DKIM).",
        success="Every record type is matched correctly.",
    ),
    PerfTask(
        id="netplus-pbq-dora", exam="netplus", domain="network_operations",
        kind="order", title="Order the DHCP lease (DORA)",
        prompt="Put the **DHCP four-step lease** process in order.",
        steps=["Discover (client broadcasts)", "Offer (server offers an address)",
               "Request (client requests that address)", "Acknowledge (server confirms the lease)"],
        explain="D-O-R-A: Discover, Offer, Request, Acknowledge.",
        success="Correct DORA order.",
    ),
    PerfTask(
        id="netplus-pbq-tcpudp", exam="netplus", domain="networking_concepts",
        kind="categorize", title="TCP or UDP?",
        prompt="Sort each service by the **transport protocol** it normally uses.",
        buckets=["TCP", "UDP"],
        item_bucket={
            "HTTPS (443)": "TCP", "SSH (22)": "TCP", "FTP control (21)": "TCP", "SMTP (25)": "TCP",
            "DHCP (67/68)": "UDP", "TFTP (69)": "UDP", "SNMP (161)": "UDP", "NTP (123)": "UDP",
        },
        explain="Reliable, connection-oriented sessions = TCP; lightweight, fire-and-forget = UDP.",
        success="Every service is on the right transport.",
    ),
    PerfTask(
        id="netplus-pbq-tools", exam="netplus", domain="network_troubleshooting",
        kind="match", title="Match the troubleshooting tool",
        prompt="Match each **tool** to the job it does.",
        pairs={
            "ping": "Test reachability to a host",
            "traceroute / tracert": "Show the path hop by hop",
            "nslookup / dig": "Query DNS resolution",
            "tone generator & probe": "Locate / trace a specific cable",
            "OTDR": "Find a fault and its distance on fiber",
            "Wi-Fi analyzer": "Check channel overlap and signal strength",
        },
        explain="Match the symptom to the tool — reachability (ping), path (traceroute), name "
                "resolution (nslookup), cable tracing (toner), fiber fault (OTDR), RF (analyzer).",
        success="Every tool is matched correctly.",
    ),
    PerfTask(
        id="netplus-pbq-media", exam="netplus", domain="network_implementation",
        kind="match", title="Match the cable / connector to its use",
        prompt="Match each **medium or connector** to what it's used for.",
        pairs={
            "Cat 6": "10 Gbps Ethernet up to ~55 m",
            "Single-mode fiber": "Long-distance (kilometre) runs",
            "Multimode fiber": "Shorter, high-speed fiber runs",
            "RJ11": "Telephone / DSL",
            "Coaxial (RG-6)": "Cable internet (DOCSIS)",
            "LC connector": "Terminating a fiber strand",
        },
        explain="Copper Cat ratings for Ethernet; SMF = long haul, MMF = short/fast; RJ11 = phone; "
                "coax = cable; LC = a small fiber connector.",
        success="Every medium is matched correctly.",
    ),

    # ===== A+ Core 1 (round 2) ============================================
    PerfTask(
        id="aplus1-pbq-connectors", exam="aplus1", domain="hardware",
        kind="match", title="Match each connector to its use",
        prompt="Match each **connector** to what it carries.",
        pairs={
            "RJ45": "Wired Ethernet",
            "HDMI": "Digital video + audio",
            "SATA": "Internal drive data",
            "DisplayPort": "Digital video",
            "RJ11": "Telephone / DSL modem",
            "USB-C": "Reversible data / power / video",
        },
        explain="RJ45 = Ethernet, HDMI/DisplayPort = video, SATA = drive, RJ11 = phone, USB-C = "
                "do-it-all reversible.",
        success="Every connector is matched correctly.",
    ),
    PerfTask(
        id="aplus1-pbq-ts", exam="aplus1", domain="hw_net_troubleshooting",
        kind="order", title="Order the CompTIA troubleshooting steps",
        prompt="Put the **CompTIA six-step troubleshooting method** in order.",
        steps=["Identify the problem", "Establish a theory of probable cause",
               "Test the theory to determine the cause",
               "Establish a plan of action and implement it",
               "Verify full system functionality (and add preventive measures)",
               "Document findings, actions, and outcomes"],
        explain="Identify → theory → test → plan & implement → verify + prevent → document.",
        success="Correct troubleshooting order.",
    ),
    PerfTask(
        id="aplus1-pbq-display", exam="aplus1", domain="mobile_devices",
        kind="match", title="Match the display technology",
        prompt="Match each **panel technology** to its defining trait.",
        pairs={
            "IPS": "Best color accuracy and viewing angles",
            "TN": "Cheapest and fastest, but poor angles",
            "OLED": "Per-pixel lighting, true blacks",
            "VA": "High contrast, a middle ground",
        },
        explain="IPS = color/angles, TN = cheap/fast, OLED = true black, VA = contrast.",
        success="Every panel is matched correctly.",
    ),
    PerfTask(
        id="aplus1-pbq-internet", exam="aplus1", domain="networking_a1",
        kind="match", title="Match the internet connection type",
        prompt="Match each **internet connection** to its characteristic.",
        pairs={
            "Fiber": "Fastest, symmetric, low latency",
            "Cable (DOCSIS)": "Shared coax, fast download",
            "DSL": "Runs over phone lines, distance-limited",
            "Satellite": "Available almost anywhere, high latency",
            "Cellular (5G)": "Mobile wireless broadband",
        },
        explain="Fiber fastest; cable shared; DSL phone-line/distance; satellite high latency; "
                "cellular mobile.",
        success="Every connection is matched correctly.",
    ),
    PerfTask(
        id="aplus1-pbq-printers", exam="aplus1", domain="hardware",
        kind="match", title="Match the printer type",
        prompt="Match each **printer type** to how it prints.",
        pairs={
            "Laser": "Toner fused to the page (drum + fuser)",
            "Inkjet": "Liquid ink sprayed through nozzles",
            "Thermal": "Heats special paper (receipts)",
            "Impact (dot-matrix)": "Pins strike a ribbon — multipart forms",
            "3D (FDM)": "Extrudes melted filament layer by layer",
        },
        explain="Laser = toner/fuser, inkjet = ink nozzles, thermal = heat on paper, impact = "
                "pins/ribbon, 3D FDM = filament.",
        success="Every printer is matched correctly.",
    ),

    # ===== A+ Core 2 (round 2) ============================================
    PerfTask(
        id="aplus2-pbq-cmdos", exam="aplus2", domain="operating_systems",
        kind="categorize", title="Windows or Linux command?",
        prompt="Sort each **command** by the operating system it belongs to.",
        buckets=["Windows", "Linux"],
        item_bucket={
            "ipconfig": "Windows", "sfc /scannow": "Windows", "chkdsk": "Windows", "gpupdate": "Windows",
            "ls": "Linux", "chmod": "Linux", "sudo": "Linux", "apt-get": "Linux",
        },
        explain="ipconfig/sfc/chkdsk/gpupdate are Windows; ls/chmod/sudo/apt are Linux (ifconfig/ip "
                "is the Linux counterpart to ipconfig).",
        success="Every command is on the right OS.",
    ),
    PerfTask(
        id="aplus2-pbq-social", exam="aplus2", domain="security_a2",
        kind="match", title="Match the social-engineering attack",
        prompt="Match each **attack** to its description.",
        pairs={
            "Phishing": "Fraudulent email sent to many users",
            "Vishing": "Scam over a voice call",
            "Whaling": "Phishing aimed at executives",
            "Tailgating": "Following someone through a secure door",
            "Shoulder surfing": "Watching someone enter credentials",
            "Dumpster diving": "Recovering sensitive info from the trash",
        },
        explain="Phishing (email), vishing (voice), whaling (execs), tailgating (door), shoulder "
                "surfing (watching), dumpster diving (trash).",
        success="Every attack is matched correctly.",
    ),
    PerfTask(
        id="aplus2-pbq-editions", exam="aplus2", domain="operating_systems",
        kind="categorize", title="Home or Pro feature?",
        prompt="Sort each Windows feature by the **minimum edition** that provides it.",
        buckets=["In Windows Home", "Requires Pro or higher"],
        item_bucket={
            "Microsoft Defender Antivirus": "In Windows Home",
            "File History backups": "In Windows Home",
            "Microsoft Store": "In Windows Home",
            "Sign in with a Microsoft account": "In Windows Home",
            "Join an Active Directory domain": "Requires Pro or higher",
            "BitLocker drive encryption": "Requires Pro or higher",
            "Local Group Policy Editor (gpedit)": "Requires Pro or higher",
            "Host a Remote Desktop session": "Requires Pro or higher",
        },
        explain="Domain join, BitLocker, gpedit and RDP-host all start at Pro; Defender, File "
                "History, the Store and MSA sign-in are in Home.",
        success="Every feature is in the right edition.",
    ),
    PerfTask(
        id="aplus2-pbq-destruction", exam="aplus2", domain="security_a2",
        kind="categorize", title="Classify the data-destruction method",
        prompt="Sort each method by whether it **physically destroys** the drive or **sanitizes** "
               "it for reuse.",
        buckets=["Physical destruction", "Sanitize for reuse"],
        item_bucket={
            "Shredding the drive": "Physical destruction",
            "Drilling through the platters": "Physical destruction",
            "Degaussing (magnetic wipe)": "Physical destruction",
            "Incinerating the media": "Physical destruction",
            "Secure erase / ATA wipe": "Sanitize for reuse",
            "Low-level / full overwrite": "Sanitize for reuse",
            "Drive-wipe utility (multiple passes)": "Sanitize for reuse",
        },
        explain="Shred/drill/degauss/incinerate destroy the media; secure-erase/overwrite wipe it "
                "so the drive can be reused. (Degaussing only works on magnetic drives, not SSDs.)",
        success="Every method is in the right category.",
    ),
    PerfTask(
        id="aplus2-pbq-change", exam="aplus2", domain="operational_procedures",
        kind="order", title="Order the change-management process",
        prompt="Put the **change-management** steps in the order they should happen.",
        steps=["Document the proposed change (purpose and scope)",
               "Perform a risk analysis",
               "Get approval from the change board",
               "Implement in a maintenance window (with a backout plan ready)",
               "Test and verify the change",
               "Document the outcome"],
        explain="Propose → assess risk → approve → implement (with a rollback plan) → verify → "
                "document.",
        success="Correct change-management order.",
    ),
]

_BY_ID = {t.id: t for t in PERF_TASKS}


def get_perf_task(task_id: str) -> PerfTask:
    return _BY_ID[task_id]


def perf_tasks_for(exam: str) -> list[PerfTask]:
    return [t for t in PERF_TASKS if t.exam == exam]


def is_perf_task(task_id: str) -> bool:
    return task_id in _BY_ID
