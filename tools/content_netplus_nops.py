"""CompTIA Network+ N10-009 — Domain 3.0 Network Operations EXPANSION pool.

Original, objective-aligned items that deepen the base Network+ bank
(`content_netplus.py`) for the Network Operations domain to real exam depth.
Same authoring rules as the other pools: original content mapped to the public
exam objectives, never real exam items. build_content.py shuffles option order,
so the answer key here is not positionally biased.

Covers all five 3.0 sub-topics: network_documentation, network_monitoring,
disaster_recovery, dns_dhcp_services, snmp_logging_np. IDs begin at
netplus-nops-101 to avoid colliding with the base pool (netplus-nops-001..006).
"""

QUESTIONS = [
    # ===== 3.0 Network Operations :: network_documentation ==================
    {
        "id": "netplus-nops-101", "exam": "netplus", "domain": "network_operations",
        "subtopic": "network_documentation", "difficulty": 2, "type": "mcq",
        "stem": "A team keeps creating duplicate IP assignments and has no central record of "
                "which addresses are in use, reserved, or free across many subnets. Which "
                "solution BEST addresses this?",
        "options": [
            {"id": "A", "text": "IPAM (IP Address Management)"},
            {"id": "B", "text": "A rack diagram"},
            {"id": "C", "text": "A service-level agreement (SLA)"},
            {"id": "D", "text": "A wireless site survey"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "IPAM centralizes tracking of IP address usage, subnets, reservations, and "
                       "often integrated DNS/DHCP, replacing error-prone spreadsheets and preventing "
                       "duplicate assignments.",
            "distractors": {
                "B": "A rack diagram shows front/rear equipment placement by rack unit, not IP usage.",
                "C": "An SLA defines agreed service metrics with a provider; it tracks no addresses.",
                "D": "A site survey assesses wireless RF coverage for AP placement, unrelated to IP tracking.",
            },
            "exam_pattern": "Central IP/subnet/DNS/DHCP record = IPAM; it solves duplicate-IP and 'who has what' problems.",
        },
    },
    {
        "id": "netplus-nops-102", "exam": "netplus", "domain": "network_operations",
        "subtopic": "network_documentation", "difficulty": 1, "type": "mcq",
        "stem": "A data-center technician needs a document showing which rack unit (RU) each "
                "server and switch occupies, front and rear, to plan a new install. Which "
                "document provides this?",
        "options": [
            {"id": "A", "text": "A rack diagram"},
            {"id": "B", "text": "A logical network diagram"},
            {"id": "C", "text": "An asset inventory"},
            {"id": "D", "text": "An IP address management (IPAM) report"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A rack diagram maps the RU-by-RU placement of equipment in a rack (front and "
                       "rear), used to plan space, cabling, power, and airflow.",
            "distractors": {
                "B": "A logical diagram shows IP subnets, VLANs, and routing relationships, not physical RU slots.",
                "C": "An asset inventory lists devices, serials, and owners but not their physical rack positions.",
                "D": "An IPAM report tracks address usage, not equipment placement in a rack.",
            },
            "exam_pattern": "Rack diagram = physical RU placement of gear in a rack.",
        },
    },
    {
        "id": "netplus-nops-103", "exam": "netplus", "domain": "network_operations",
        "subtopic": "network_documentation", "difficulty": 2, "type": "mcq",
        "stem": "After a wireless site survey, an engineer produces a color-gradient overlay on "
                "the floor plan showing RF signal strength in each area of the building. What is "
                "this output called?",
        "options": [
            {"id": "A", "text": "A heat map"},
            {"id": "B", "text": "A rack diagram"},
            {"id": "C", "text": "A logical network diagram"},
            {"id": "D", "text": "A physical/wiring diagram"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A wireless heat map overlays color-coded signal strength (and interference) onto "
                       "the floor plan, the key deliverable of a site survey for planning AP placement.",
            "distractors": {
                "B": "A rack diagram shows equipment placement by rack unit, not RF coverage.",
                "C": "A logical diagram shows IP/VLAN/routing relationships, not signal strength.",
                "D": "A physical/wiring diagram documents cable runs and port terminations, not RF coverage.",
            },
            "exam_pattern": "Wireless heat map = color-coded RF coverage over a floor plan (produced by a site survey).",
        },
    },
    {
        "id": "netplus-nops-104", "exam": "netplus", "domain": "network_operations",
        "subtopic": "network_documentation", "difficulty": 2, "type": "mcq",
        "stem": "Before a scheduled firewall rule modification, the team submits a request, has it "
                "reviewed and approved by stakeholders, schedules a maintenance window, and "
                "prepares a rollback plan. Which process is being followed?",
        "options": [
            {"id": "A", "text": "Change management"},
            {"id": "B", "text": "Incident response"},
            {"id": "C", "text": "Asset lifecycle management"},
            {"id": "D", "text": "Baseline configuration review"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Change management governs planned changes through a documented request, approval, "
                       "scheduling, implementation, and rollback plan to limit risk and keep an audit trail.",
            "distractors": {
                "B": "Incident response reacts to an unplanned security event or outage, not a scheduled change.",
                "C": "Asset lifecycle management tracks hardware/software from procurement to retirement (incl. EOL/EOS).",
                "D": "A baseline configuration is a documented known-good config; comparing to it is not the approval workflow.",
            },
            "exam_pattern": "Request + approval + maintenance window + rollback = change management.",
        },
    },
    {
        "id": "netplus-nops-105", "exam": "netplus", "domain": "network_operations",
        "subtopic": "network_documentation", "difficulty": 3, "type": "mcq",
        "stem": "A vendor publishes a date after which a router model will receive no further "
                "software updates, security patches, or technical support. Which hardware/software "
                "lifecycle milestone does this describe?",
        "options": [
            {"id": "A", "text": "End-of-support (EOS)"},
            {"id": "B", "text": "End-of-life (EOL) announcement"},
            {"id": "C", "text": "Recovery point objective (RPO)"},
            {"id": "D", "text": "Mean time between failures (MTBF)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "End-of-support (EOS/EOSL) is the date after which the vendor provides no more patches, "
                       "updates, or support, leaving the device a growing security risk that should be replaced.",
            "distractors": {
                "B": "An EOL announcement marks that a product is being discontinued/no longer sold, but patches and "
                     "support may continue until the later EOS date.",
                "C": "RPO is a disaster-recovery data-loss target, not a product lifecycle milestone.",
                "D": "MTBF is a reliability statistic (average time between failures), not a support cutoff.",
            },
            "exam_pattern": "EOL = no longer sold; EOS/EOSL = no more patches or support (plan replacement for security).",
        },
    },

    # ===== 3.0 Network Operations :: network_monitoring =====================
    {
        "id": "netplus-nops-106", "exam": "netplus", "domain": "network_operations",
        "subtopic": "network_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "A VoIP engineer finds that voice packets arrive with inconsistent inter-packet "
                "delay, causing choppy audio, even though the average latency is acceptable. "
                "Which performance metric describes this variation in delay?",
        "options": [
            {"id": "A", "text": "Jitter"},
            {"id": "B", "text": "Latency"},
            {"id": "C", "text": "Packet loss"},
            {"id": "D", "text": "Bandwidth"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Jitter is the variation in packet-to-packet delay. Even with acceptable average latency, "
                       "high jitter breaks real-time audio/video and must be buffered or controlled with QoS.",
            "distractors": {
                "B": "Latency is the absolute delay, which the scenario says is acceptable; the problem is its variation.",
                "C": "Packet loss is packets never arriving (gaps/dropouts), a different symptom than uneven timing.",
                "D": "Bandwidth is link capacity, not the timing variation of delivered packets.",
            },
            "exam_pattern": "Jitter = variation in latency (hurts VoIP/video); latency = delay; loss = dropped packets.",
        },
    },
    {
        "id": "netplus-nops-107", "exam": "netplus", "domain": "network_operations",
        "subtopic": "network_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "A security operations team wants one platform that collects logs from firewalls, "
                "servers, and switches, correlates events across all of them, and raises alerts on "
                "suspicious patterns. Which solution fits BEST?",
        "options": [
            {"id": "A", "text": "A SIEM"},
            {"id": "B", "text": "An SNMP trap receiver"},
            {"id": "C", "text": "A NetFlow collector"},
            {"id": "D", "text": "A protocol analyzer"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A SIEM (Security Information and Event Management) aggregates logs from many sources, "
                       "correlates them, and generates alerts/dashboards — centralized security monitoring.",
            "distractors": {
                "B": "An SNMP trap receiver collects device state notifications; it does not correlate multi-source logs.",
                "C": "A NetFlow collector aggregates traffic-flow records (who talks to whom), not multi-source log events.",
                "D": "A protocol analyzer decodes captured packets; it is not a centralized log-correlation platform.",
            },
            "exam_pattern": "Aggregate + correlate + alert across many log sources = SIEM.",
        },
    },
    {
        "id": "netplus-nops-108", "exam": "netplus", "domain": "network_operations",
        "subtopic": "network_monitoring", "difficulty": 2, "type": "mcq",
        "stem": "To troubleshoot a malformed application handshake, an engineer must inspect the "
                "actual bytes and header fields of individual frames traversing a switch port. "
                "Which approach is MOST appropriate?",
        "options": [
            {"id": "A", "text": "A packet capture with a protocol analyzer via a port mirror (SPAN) or TAP"},
            {"id": "B", "text": "SNMP polling of the interface's counters"},
            {"id": "C", "text": "Reviewing the syslog server"},
            {"id": "D", "text": "Exporting NetFlow records"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Seeing the real frame contents and header fields requires capturing packets with a "
                       "protocol analyzer, typically fed by a SPAN/port-mirror session or a physical TAP.",
            "distractors": {
                "B": "SNMP polling returns counters/health totals, not the contents of individual frames.",
                "C": "Syslog carries device event messages, not the raw bytes of captured frames.",
                "D": "NetFlow summarizes conversation metadata (IPs, ports, byte counts), not full packet payloads.",
            },
            "exam_pattern": "Need the actual packet contents/headers = packet capture (sniffer/protocol analyzer via SPAN/TAP).",
        },
    },
    {
        "id": "netplus-nops-109", "exam": "netplus", "domain": "network_operations",
        "subtopic": "network_monitoring", "difficulty": 1, "type": "mcq",
        "stem": "A wiring closet repeatedly overheats, causing switches to shut down. Which "
                "monitoring addition would alert staff BEFORE the equipment fails again?",
        "options": [
            {"id": "A", "text": "Temperature and humidity environmental sensors"},
            {"id": "B", "text": "A SIEM log-correlation rule"},
            {"id": "C", "text": "NetFlow traffic collection"},
            {"id": "D", "text": "A wireless heat map"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Environmental sensors (temperature, humidity, and often power/water/airflow) monitor the "
                       "physical conditions of IDF/MDF/data-center spaces and alert before heat causes shutdowns.",
            "distractors": {
                "B": "A SIEM correlates logs; it cannot read closet temperature unless a sensor feeds it data.",
                "C": "NetFlow accounts for traffic volume and has nothing to do with temperature.",
                "D": "A wireless heat map shows RF coverage, not thermal/environmental conditions.",
            },
            "exam_pattern": "Overheating/physical conditions = environmental sensors (temp/humidity/power) in the IDF/MDF.",
        },
    },
    {
        "id": "netplus-nops-110", "exam": "netplus", "domain": "network_operations",
        "subtopic": "network_monitoring", "difficulty": 3, "type": "multi",
        "stem": "While diagnosing a flaky link, an engineer reviews a switch interface's "
                "statistics. Which TWO counters point to a physical-layer problem such as bad "
                "cabling, EMI, or a duplex mismatch? (Choose two.)",
        "options": [
            {"id": "A", "text": "CRC (FCS) errors"},
            {"id": "B", "text": "Late collisions"},
            {"id": "C", "text": "DHCP decline messages"},
            {"id": "D", "text": "Successfully forwarded unicast packets"},
        ],
        "correct": ["A", "B"],
        "select_count": 2,
        "explanation": {
            "correct": "Rising CRC/FCS errors indicate corrupted frames (bad cable, connector, EMI, or duplex "
                       "mismatch), and late collisions are a classic sign of a duplex mismatch — both are "
                       "Layer 1 indicators found in interface statistics.",
            "distractors": {
                "C": "A DHCP decline is a client addressing event, not an interface error counter.",
                "D": "Successfully forwarded unicasts are normal traffic, not an error indicator.",
            },
            "exam_pattern": "L1 health shows in error counters: CRC/FCS errors, runts, giants, late collisions (cabling/EMI/duplex).",
        },
    },

    # ===== 3.0 Network Operations :: disaster_recovery ======================
    {
        "id": "netplus-nops-111", "exam": "netplus", "domain": "network_operations",
        "subtopic": "disaster_recovery", "difficulty": 1, "type": "mcq",
        "stem": "Management states that after a failure the e-commerce site must be back online "
                "within 2 hours. Which metric does this 2-hour target define?",
        "options": [
            {"id": "A", "text": "RTO (Recovery Time Objective)"},
            {"id": "B", "text": "RPO (Recovery Point Objective)"},
            {"id": "C", "text": "MTBF (Mean Time Between Failures)"},
            {"id": "D", "text": "MTTR (Mean Time To Repair)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "RTO is the maximum tolerable time to restore service after an outage — the '2 hours to "
                       "be back online' target is an RTO.",
            "distractors": {
                "B": "RPO is the tolerable amount of DATA loss (how far back the last recovery point is), not restore time.",
                "C": "MTBF is the average uptime between failures, a reliability statistic, not a recovery goal.",
                "D": "MTTR is the average/actual time taken to repair a failure (a measured value), not the business target.",
            },
            "exam_pattern": "RTO = how long until service is back UP (goal); RPO = how much DATA can be lost; MTTR/MTBF are measured stats.",
        },
    },
    {
        "id": "netplus-nops-112", "exam": "netplus", "domain": "network_operations",
        "subtopic": "disaster_recovery", "difficulty": 2, "type": "mcq",
        "stem": "An organization needs a recovery facility that is fully equipped and running with "
                "near-real-time replicated data so it can take over operations within minutes of a "
                "disaster. Which site type is this?",
        "options": [
            {"id": "A", "text": "Hot site"},
            {"id": "B", "text": "Warm site"},
            {"id": "C", "text": "Cold site"},
            {"id": "D", "text": "Cloud archive"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A hot site is fully operational with hardware, connectivity, and continuously replicated "
                       "data, enabling near-immediate failover — the fastest and most expensive option.",
            "distractors": {
                "B": "A warm site has hardware and connectivity but needs data restore and setup, so recovery takes hours to days.",
                "C": "A cold site provides only space and power; equipment and data must be brought in, giving the longest recovery.",
                "D": "A cloud archive stores backup data cheaply but is not a ready-to-run operational facility.",
            },
            "exam_pattern": "Cold (space/power only) < warm (equipped, needs data) < hot (live + replicated, fastest/costliest).",
        },
    },
    {
        "id": "netplus-nops-113", "exam": "netplus", "domain": "network_operations",
        "subtopic": "disaster_recovery", "difficulty": 3, "type": "mcq",
        "stem": "A backup scheme takes a full backup every Sunday and, each weeknight, backs up all "
                "data changed SINCE SUNDAY'S FULL. To restore data as of Thursday evening, which "
                "backup sets are required and what is this scheme called?",
        "options": [
            {"id": "A", "text": "The Sunday full plus Thursday's set — 2 sets — a differential scheme"},
            {"id": "B", "text": "The Sunday full plus every nightly set through Thursday — an incremental scheme"},
            {"id": "C", "text": "Only Thursday's set — a snapshot scheme"},
            {"id": "D", "text": "Every nightly set but not the full — an incremental scheme"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Backing up everything changed since the last FULL is a differential. Restoring needs only the "
                       "full plus the most recent differential (Sunday full + Thursday) = 2 sets.",
            "distractors": {
                "B": "That describes incremental (each set holds changes since the PREVIOUS backup), which needs the full + all increments.",
                "C": "A snapshot is a point-in-time image, not this cumulative-since-full chain.",
                "D": "Incremental still requires the base full to restore, and this scheme is differential, not incremental.",
            },
            "exam_pattern": "Differential = changes since last FULL (restore = full + 1 diff); incremental = changes since last BACKUP (restore = full + all increments).",
        },
    },
    {
        "id": "netplus-nops-114", "exam": "netplus", "domain": "network_operations",
        "subtopic": "disaster_recovery", "difficulty": 2, "type": "mcq",
        "stem": "Two routers share a single virtual IP address acting as the default gateway, so if "
                "the active router fails the standby takes over the virtual IP with no client "
                "reconfiguration. Which type of protocol provides this?",
        "options": [
            {"id": "A", "text": "A First Hop Redundancy Protocol (FHRP) such as VRRP or HSRP"},
            {"id": "B", "text": "A routing protocol such as OSPF"},
            {"id": "C", "text": "Spanning Tree Protocol (STP)"},
            {"id": "D", "text": "Link aggregation (LACP)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An FHRP (VRRP, HSRP, or GLBP) presents a shared virtual gateway IP/MAC; one router is "
                       "active and another standby, giving hosts gateway redundancy with no reconfiguration on failover.",
            "distractors": {
                "B": "OSPF exchanges routes between routers but does not present a shared virtual gateway IP to end hosts.",
                "C": "STP prevents Layer 2 switching loops; it provides no default-gateway failover.",
                "D": "LACP bundles physical links for bandwidth/redundancy between two devices, not a virtual gateway.",
            },
            "exam_pattern": "Shared virtual gateway IP + active/standby failover = FHRP (HSRP/VRRP/GLBP).",
        },
    },
    {
        "id": "netplus-nops-115", "exam": "netplus", "domain": "network_operations",
        "subtopic": "disaster_recovery", "difficulty": 2, "type": "multi",
        "stem": "An administrator deploys two firewalls in an active-active high-availability "
                "cluster. Which TWO statements accurately describe active-active compared with "
                "active-passive? (Choose two.)",
        "options": [
            {"id": "A", "text": "Both nodes process traffic simultaneously, increasing aggregate throughput"},
            {"id": "B", "text": "The standby node sits idle until the primary fails"},
            {"id": "C", "text": "Load is shared across both nodes during normal operation"},
            {"id": "D", "text": "Only one node ever forwards traffic at a time"},
        ],
        "correct": ["A", "C"],
        "select_count": 2,
        "explanation": {
            "correct": "In active-active, both nodes are live at once and share the load, so the pair also delivers "
                       "more aggregate capacity than a single node — not just failover.",
            "distractors": {
                "B": "A standby that sits idle until failover describes active-PASSIVE, not active-active.",
                "D": "Forwarding through only one node at a time is active-passive; active-active forwards through both concurrently.",
            },
            "exam_pattern": "Active-active = both nodes work and share load (more capacity); active-passive = standby idle until failover.",
        },
    },

    # ===== 3.0 Network Operations :: dns_dhcp_services ======================
    {
        "id": "netplus-nops-116", "exam": "netplus", "domain": "network_operations",
        "subtopic": "dns_dhcp_services", "difficulty": 1, "type": "mcq",
        "stem": "A client must resolve a hostname to an IPv6 address. Which DNS record type returns "
                "that answer?",
        "options": [
            {"id": "A", "text": "AAAA"},
            {"id": "B", "text": "A"},
            {"id": "C", "text": "PTR"},
            {"id": "D", "text": "CNAME"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The AAAA ('quad-A') record maps a hostname to a 128-bit IPv6 address.",
            "distractors": {
                "B": "An A record maps a hostname to a 32-bit IPv4 address, not IPv6.",
                "C": "A PTR record is used for reverse lookups (IP address back to a name).",
                "D": "A CNAME is an alias pointing to another canonical name; it returns no address itself.",
            },
            "exam_pattern": "A = IPv4, AAAA = IPv6, PTR = reverse lookup, CNAME = alias.",
        },
    },
    {
        "id": "netplus-nops-117", "exam": "netplus", "domain": "network_operations",
        "subtopic": "dns_dhcp_services", "difficulty": 3, "type": "mcq",
        "stem": "An administrator wants a specific network printer to ALWAYS receive the same IP "
                "address from DHCP, tied to its MAC address, while still being managed by the DHCP "
                "server. Which configuration achieves this?",
        "options": [
            {"id": "A", "text": "A DHCP reservation"},
            {"id": "B", "text": "A DHCP exclusion"},
            {"id": "C", "text": "A shorter scope lease time"},
            {"id": "D", "text": "A DHCP relay (IP helper)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A reservation binds a chosen IP to the device's MAC in the DHCP scope, so DHCP always "
                       "hands that host the same address while still managing it centrally.",
            "distractors": {
                "B": "An exclusion removes addresses from the pool so DHCP never assigns them; you would then have to static-assign the printer manually.",
                "C": "A shorter lease just renews more often; it does not pin a specific address to the host.",
                "D": "An IP helper forwards DHCP requests across subnets; it does not reserve an address.",
            },
            "exam_pattern": "Reservation = DHCP always gives a set IP to a MAC; exclusion = addresses DHCP must NOT assign.",
        },
    },
    {
        "id": "netplus-nops-118", "exam": "netplus", "domain": "network_operations",
        "subtopic": "dns_dhcp_services", "difficulty": 2, "type": "mcq",
        "stem": "Clients on VLAN 20 receive no address from the central DHCP server on VLAN 10 "
                "because their broadcast Discover never leaves the local subnet. Which "
                "configuration on the VLAN 20 gateway resolves this?",
        "options": [
            {"id": "A", "text": "An IP helper-address (DHCP relay) pointing to the DHCP server"},
            {"id": "B", "text": "A DHCP exclusion range on VLAN 20"},
            {"id": "C", "text": "DHCP snooping on the uplink"},
            {"id": "D", "text": "A shorter lease duration"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Routers do not forward broadcasts, so a DHCP relay / IP helper-address on the client-side "
                       "gateway converts the broadcast Discover to a unicast and forwards it to the server across subnets.",
            "distractors": {
                "B": "An exclusion merely withholds some addresses; it does not forward cross-subnet DHCP requests.",
                "C": "DHCP snooping is a security filter against rogue DHCP servers; it does not relay Discover messages.",
                "D": "Lease duration has no effect on whether requests reach the server across subnets.",
            },
            "exam_pattern": "DHCP broadcast can't cross a router → configure IP helper-address (DHCP relay) on the client's gateway.",
        },
    },
    {
        "id": "netplus-nops-119", "exam": "netplus", "domain": "network_operations",
        "subtopic": "dns_dhcp_services", "difficulty": 3, "type": "mcq",
        "stem": "A workstation sends a query to its configured DNS server, which then performs the "
                "full lookup on the client's behalf — querying root, TLD, and other servers until "
                "it returns the final answer and caches it. In this exchange the client's DNS "
                "server is acting as what?",
        "options": [
            {"id": "A", "text": "A recursive resolver"},
            {"id": "B", "text": "An authoritative name server"},
            {"id": "C", "text": "A root hint"},
            {"id": "D", "text": "A reverse-lookup zone"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A recursive resolver does the full legwork for the client (root → TLD → authoritative), "
                       "returns the final answer, and caches it. The client itself makes only one (recursive) request.",
            "distractors": {
                "B": "An authoritative server holds and answers only for its own zone data; it does not chase the whole chain for clients.",
                "C": "Root hints are the preconfigured addresses of the root servers a resolver starts from, not a role the server plays.",
                "D": "A reverse-lookup zone maps IP addresses to names (PTR); it is a zone type, not this resolving behavior.",
            },
            "exam_pattern": "Recursive resolver does the work (root→TLD→authoritative) and caches; authoritative answers only for its own zone.",
        },
    },
    {
        "id": "netplus-nops-120", "exam": "netplus", "domain": "network_operations",
        "subtopic": "dns_dhcp_services", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants assurance that DNS responses are authentic and have not been "
                "forged or tampered with, using cryptographic signatures on the records. Which "
                "technology provides this?",
        "options": [
            {"id": "A", "text": "DNSSEC"},
            {"id": "B", "text": "A chain of CNAME aliases"},
            {"id": "C", "text": "A longer DHCP lease"},
            {"id": "D", "text": "Split-horizon (internal/external) DNS"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "DNSSEC digitally signs DNS records (RRSIG/DNSKEY/DS) so resolvers can validate that answers "
                       "are authentic and unmodified, defeating spoofing/cache poisoning. Note it validates, it does not encrypt.",
            "distractors": {
                "B": "Chaining CNAMEs is only aliasing; it adds no authentication or integrity check.",
                "C": "DHCP lease length is unrelated to DNS record authenticity.",
                "D": "Split-horizon serves different answers to internal vs external clients but does not cryptographically sign or validate records.",
            },
            "exam_pattern": "DNSSEC = signatures that validate record authenticity/integrity (not confidentiality — DoH/DoT handle encryption).",
        },
    },

    # ===== 3.0 Network Operations :: snmp_logging_np ========================
    {
        "id": "netplus-nops-121", "exam": "netplus", "domain": "network_operations",
        "subtopic": "snmp_logging_np", "difficulty": 2, "type": "mcq",
        "stem": "A security review requires that all SNMP management traffic be both authenticated "
                "AND encrypted. Which SNMP version must be deployed to meet this requirement?",
        "options": [
            {"id": "A", "text": "SNMPv3"},
            {"id": "B", "text": "SNMPv2c"},
            {"id": "C", "text": "SNMPv1"},
            {"id": "D", "text": "SNMPv2c with a long community string"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Only SNMPv3 adds a security model with authentication (authNoPriv) and optional privacy/"
                       "encryption (authPriv); it is the version required when SNMP must be authenticated and encrypted.",
            "distractors": {
                "B": "SNMPv2c relies on a cleartext community string — no real authentication framework and no encryption.",
                "C": "SNMPv1 is the oldest version, also community-based and sent in cleartext.",
                "D": "Lengthening a community string does not add authentication or encryption; it is still cleartext v2c.",
            },
            "exam_pattern": "Authentication + encryption for SNMP = SNMPv3 (authPriv); v1/v2c use cleartext community strings.",
        },
    },
    {
        "id": "netplus-nops-122", "exam": "netplus", "domain": "network_operations",
        "subtopic": "snmp_logging_np", "difficulty": 2, "type": "mcq",
        "stem": "An administrator wants managed devices to IMMEDIATELY notify the SNMP manager the "
                "moment an interface goes down, instead of waiting for the next scheduled query. "
                "Which SNMP mechanism provides this?",
        "options": [
            {"id": "A", "text": "SNMP traps (agent-initiated notifications)"},
            {"id": "B", "text": "SNMP polling (manager-initiated GET requests)"},
            {"id": "C", "text": "A MIB walk"},
            {"id": "D", "text": "Syslog facility codes"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A trap (or inform) is an unsolicited, agent-initiated message pushed to the manager the "
                       "instant an event occurs, so notification is immediate rather than waiting for the next poll.",
            "distractors": {
                "B": "Polling is the manager querying agents on a schedule, so a failure is not seen until the next poll interval.",
                "C": "A MIB walk retrieves a tree of OIDs on demand — still manager-initiated, not event-driven.",
                "D": "Syslog facility codes categorize log sources; they are not an SNMP notification mechanism.",
            },
            "exam_pattern": "Trap/inform = agent pushes an event to the manager; GET/poll = manager pulls on a schedule.",
        },
    },
    {
        "id": "netplus-nops-123", "exam": "netplus", "domain": "network_operations",
        "subtopic": "snmp_logging_np", "difficulty": 2, "type": "mcq",
        "stem": "While correlating syslog entries from many devices during an incident, the analyst "
                "finds the timestamps don't line up, making it impossible to order events. Which "
                "service should be deployed to fix this?",
        "options": [
            {"id": "A", "text": "NTP to synchronize device clocks to a common time source"},
            {"id": "B", "text": "A higher minimum syslog severity level"},
            {"id": "C", "text": "SNMPv3 on all devices"},
            {"id": "D", "text": "A larger DHCP scope"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Correlatable, orderable log timestamps require every device to share the same accurate clock, "
                       "so all devices should sync to a common NTP time source.",
            "distractors": {
                "B": "Severity level only filters which messages are logged; it does not align clocks.",
                "C": "SNMPv3 secures SNMP; it does not synchronize time for log timestamps.",
                "D": "DHCP scope size has nothing to do with the accuracy or alignment of log timestamps.",
            },
            "exam_pattern": "Consistent, correlatable log timestamps across devices = NTP (sync all devices to the same time source).",
        },
    },
    {
        "id": "netplus-nops-124", "exam": "netplus", "domain": "network_operations",
        "subtopic": "snmp_logging_np", "difficulty": 3, "type": "mcq",
        "stem": "In SNMP, a manager retrieves a value identified by a hierarchical numeric string "
                "(for example 1.3.6.1.2.1.1.3.0 for system uptime). What is this identifier called, "
                "and where is its definition stored?",
        "options": [
            {"id": "A", "text": "An OID, defined in a MIB"},
            {"id": "B", "text": "A community string, stored on the agent"},
            {"id": "C", "text": "A trap, stored on the manager"},
            {"id": "D", "text": "A syslog facility, stored on the resolver"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The dotted-number string is an Object Identifier (OID) that uniquely addresses a managed "
                       "object; the MIB is the database/definitions that describe those objects and their OIDs.",
            "distractors": {
                "B": "A community string is the shared password used by SNMP v1/v2c, not an object identifier.",
                "C": "A trap is an unsolicited event notification, not the identifier of a polled value.",
                "D": "A syslog facility categorizes log messages and is unrelated to SNMP object naming.",
            },
            "exam_pattern": "MIB = the definitions/database; OID = the dotted-number address of a specific object; agent holds values, manager queries them.",
        },
    },
]
