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
]

_BY_ID = {t.id: t for t in PERF_TASKS}


def get_perf_task(task_id: str) -> PerfTask:
    return _BY_ID[task_id]


def perf_tasks_for(exam: str) -> list[PerfTask]:
    return [t for t in PERF_TASKS if t.exam == exam]


def is_perf_task(task_id: str) -> bool:
    return task_id in _BY_ID
