"""(ISC)² Certified in Cybersecurity (CC) pool - Round 2 (deepening expansion).

Second-round, original, objective-aligned practice items across all five CC
domains. These extend the round-1 pools (content_isc2cc_principles/bcdr/access/
network/secops.py) with NEW, non-duplicate angles on the SAME entry-level scope -
no advanced content. Items are tagged to the exact blueprint domain/subtopic keys
and distributed by exam weight (principles 26%, network 24%, access 22%,
operations 18%, BC/DR & IR 10%).

Authoring rules match the other content_*.py pools: build_content.py shuffles the
A/B/C/D order (seeded by id), so the authored key is not positionally biased, every
wrong option carries a distractor note, each fill item lists accepted answers, and
each item names the (ISC)² CC exam-outline area it draws on. Entry-level depth only -
core, well-established facts, never real or memorized exam items.
"""

QUESTIONS = [

    # =====================================================================
    # DOMAIN 1 - SECURITY PRINCIPLES (cc_security_principles)
    # =====================================================================

    # ----- cc_cia_triad --------------------------------------------------
    {
        "id": "isc2cc-prin-r2-001",
        "exam": "isc2cc",
        "domain": "cc_security_principles",
        "subtopic": "cc_cia_triad",
        "difficulty": 2,
        "type": "mcq",
        "stem": "An email system attaches a verifiable digital signature to each message so a sender cannot later deny having sent it. Which security concept does this provide?",
        "options": [
            {
                "id": "A",
                "text": "Availability"
            },
            {
                "id": "B",
                "text": "Non-repudiation"
            },
            {
                "id": "C",
                "text": "Integrity"
            },
            {
                "id": "D",
                "text": "Confidentiality"
            }
        ],
        "correct": [
            "B"
        ],
        "explanation": {
            "correct": "Non-repudiation provides proof of origin so a party cannot credibly deny an action - here, that they sent the message.",
            "distractors": {
                "A": "Availability is about systems/data being reachable when needed, not proof of who acted.",
                "C": "Integrity ensures the message was not altered; the specific 'cannot deny sending it' property is non-repudiation.",
                "D": "Confidentiality keeps content secret; it does not establish undeniable proof of the sender."
            },
            "exam_pattern": "'Cannot deny having done it' / proof of origin = non-repudiation."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 1 - Foundational concepts (non-repudiation)"
        ]
    },
    {
        "id": "isc2cc-prin-r2-002",
        "exam": "isc2cc",
        "domain": "cc_security_principles",
        "subtopic": "cc_cia_triad",
        "difficulty": 2,
        "type": "mcq",
        "stem": "A company runs two redundant servers in a failover cluster so that if one fails, the other instantly takes over and the service stays reachable. Which element of the CIA triad does this design protect?",
        "options": [
            {
                "id": "A",
                "text": "Confidentiality"
            },
            {
                "id": "B",
                "text": "Integrity"
            },
            {
                "id": "C",
                "text": "Availability"
            },
            {
                "id": "D",
                "text": "Non-repudiation"
            }
        ],
        "correct": [
            "C"
        ],
        "explanation": {
            "correct": "Availability ensures systems and data remain accessible when needed; redundancy and failover keep the service reachable despite a component failure.",
            "distractors": {
                "A": "Confidentiality is about preventing disclosure, not keeping a service running.",
                "B": "Integrity is about accuracy of data, not uptime of the service.",
                "D": "Non-repudiation is proof of an action's origin, unrelated to redundancy."
            },
            "exam_pattern": "Redundancy / failover / uptime = availability."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 1 - CIA triad (availability)"
        ]
    },
    {
        "id": "isc2cc-prin-r2-003",
        "exam": "isc2cc",
        "domain": "cc_security_principles",
        "subtopic": "cc_cia_triad",
        "difficulty": 1,
        "type": "mcq",
        "stem": "A pharmacy's system must guarantee that a stored medication dose is exactly what the doctor entered - accurate, complete, and unaltered. Which CIA element is this requirement about?",
        "options": [
            {
                "id": "A",
                "text": "Integrity"
            },
            {
                "id": "B",
                "text": "Availability"
            },
            {
                "id": "C",
                "text": "Confidentiality"
            },
            {
                "id": "D",
                "text": "Authentication"
            }
        ],
        "correct": [
            "A"
        ],
        "explanation": {
            "correct": "Integrity is the assurance that data is accurate, complete, and unaltered - exactly what a correct, trustworthy medication dose requires.",
            "distractors": {
                "B": "Availability is about the data being reachable, not about it being accurate.",
                "C": "Confidentiality is about limiting who can view the data, not its accuracy.",
                "D": "Authentication verifies identity; it is a mechanism, not one of the three CIA elements."
            },
            "exam_pattern": "Accurate, complete, unaltered, trustworthy data = integrity."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 1 - CIA triad (integrity)"
        ]
    },
    {
        "id": "isc2cc-prin-r2-004",
        "exam": "isc2cc",
        "domain": "cc_security_principles",
        "subtopic": "cc_cia_triad",
        "difficulty": 1,
        "type": "fill",
        "stem": "Confidentiality, integrity, and availability are the three core goals of information security, collectively known by the three-letter acronym ___.",
        "correct": [
            "CIA",
            "CIA triad",
            "C.I.A."
        ],
        "explanation": {
            "correct": "Confidentiality, Integrity, and Availability together form the CIA triad - the foundational model of information-security goals.",
            "exam_pattern": "Confidentiality + Integrity + Availability = the CIA triad."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 1 - CIA triad (the triad)"
        ]
    },
    {
        "id": "isc2cc-prin-r2-005",
        "exam": "isc2cc",
        "domain": "cc_security_principles",
        "subtopic": "cc_cia_triad",
        "difficulty": 2,
        "type": "mcq",
        "stem": "A printed report marked 'Confidential' is left sitting in a shared printer tray where anyone walking by can read it. Which element of the CIA triad is most at risk?",
        "options": [
            {
                "id": "A",
                "text": "Availability"
            },
            {
                "id": "B",
                "text": "Integrity"
            },
            {
                "id": "C",
                "text": "Confidentiality"
            },
            {
                "id": "D",
                "text": "Non-repudiation"
            }
        ],
        "correct": [
            "C"
        ],
        "explanation": {
            "correct": "Confidentiality is about preventing disclosure to unauthorized people; an exposed confidential printout risks exactly that.",
            "distractors": {
                "A": "Availability concerns reachability; the document is reachable - that is the problem, not a loss of access.",
                "B": "Integrity concerns unauthorized change; the document was not altered, only exposed.",
                "D": "Non-repudiation is proof of an action's origin, unrelated to a document being left out."
            },
            "exam_pattern": "Unauthorized viewing / exposure of sensitive data = confidentiality risk."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 1 - CIA triad (confidentiality)"
        ]
    },
    {
        "id": "isc2cc-prin-r2-006",
        "exam": "isc2cc",
        "domain": "cc_security_principles",
        "subtopic": "cc_cia_triad",
        "difficulty": 2,
        "type": "mcq",
        "stem": "An employee accidentally deletes the only copy of a project folder, and there is no backup, so no one can access the files anymore. Which CIA element has been harmed?",
        "options": [
            {
                "id": "A",
                "text": "Confidentiality"
            },
            {
                "id": "B",
                "text": "Availability"
            },
            {
                "id": "C",
                "text": "Integrity"
            },
            {
                "id": "D",
                "text": "Non-repudiation"
            }
        ],
        "correct": [
            "B"
        ],
        "explanation": {
            "correct": "Availability is the assurance that data is accessible when needed; losing the only copy makes the data unavailable, even though no attacker was involved.",
            "distractors": {
                "A": "Confidentiality concerns disclosure; the data was not exposed, it became inaccessible.",
                "C": "Integrity concerns unauthorized modification; deletion with no copy is a loss of access, not altered content.",
                "D": "Non-repudiation is about proving who performed an action, not about losing access to data."
            },
            "exam_pattern": "Data lost / unreachable (even by accident) = availability loss."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 1 - CIA triad (availability)"
        ]
    },

    # ----- cc_risk_management --------------------------------------------
    {
        "id": "isc2cc-prin-r2-007",
        "exam": "isc2cc",
        "domain": "cc_security_principles",
        "subtopic": "cc_risk_management",
        "difficulty": 2,
        "type": "mcq",
        "stem": "In risk terms, which statement best defines 'risk'?",
        "options": [
            {
                "id": "A",
                "text": "A weakness in a system that could be exploited"
            },
            {
                "id": "B",
                "text": "The potential for loss when a threat exploits a vulnerability, judged by its likelihood and impact"
            },
            {
                "id": "C",
                "text": "Any circumstance or event with the potential to cause harm"
            },
            {
                "id": "D",
                "text": "A safeguard put in place to reduce exposure"
            }
        ],
        "correct": [
            "B"
        ],
        "explanation": {
            "correct": "Risk is the potential for loss or harm when a threat exploits a vulnerability; it is assessed from the likelihood of occurrence and the impact if it does.",
            "distractors": {
                "A": "A weakness that can be exploited is a vulnerability, one input to risk - not risk itself.",
                "C": "A circumstance or event that can cause harm is a threat, not the overall risk.",
                "D": "A safeguard that reduces exposure is a control, which lowers risk rather than defining it."
            },
            "exam_pattern": "Risk = likelihood x impact of a threat exploiting a vulnerability."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 1 - Risk terms (risk)"
        ]
    },
    {
        "id": "isc2cc-prin-r2-008",
        "exam": "isc2cc",
        "domain": "cc_security_principles",
        "subtopic": "cc_risk_management",
        "difficulty": 2,
        "type": "mcq",
        "stem": "When assessing a risk, the term for the probability that a given threat will actually exploit a vulnerability is the:",
        "options": [
            {
                "id": "A",
                "text": "Likelihood"
            },
            {
                "id": "B",
                "text": "Impact"
            },
            {
                "id": "C",
                "text": "Asset value"
            },
            {
                "id": "D",
                "text": "Residual risk"
            }
        ],
        "correct": [
            "A"
        ],
        "explanation": {
            "correct": "Likelihood is the probability or chance that a threat will successfully exploit a vulnerability within a given period.",
            "distractors": {
                "B": "Impact is the magnitude of harm if the event occurs, not the probability that it will.",
                "C": "Asset value is what the protected resource is worth, not the chance of an event.",
                "D": "Residual risk is what remains after controls are applied, not the probability of the threat."
            },
            "exam_pattern": "Probability a threat exploits a vulnerability = likelihood; the resulting harm = impact."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 1 - Risk terms (likelihood)"
        ]
    },
    {
        "id": "isc2cc-prin-r2-009",
        "exam": "isc2cc",
        "domain": "cc_security_principles",
        "subtopic": "cc_risk_management",
        "difficulty": 2,
        "type": "mcq",
        "stem": "A risk assessment estimates that if a server room floods, the business would lose $500,000 and two weeks of operations. This estimate of the consequences or severity is the risk's:",
        "options": [
            {
                "id": "A",
                "text": "Likelihood"
            },
            {
                "id": "B",
                "text": "Impact"
            },
            {
                "id": "C",
                "text": "Threat"
            },
            {
                "id": "D",
                "text": "Vulnerability"
            }
        ],
        "correct": [
            "B"
        ],
        "explanation": {
            "correct": "Impact is the magnitude of harm or loss that results when a threat exploits a vulnerability - here, the money and downtime a flood would cost.",
            "distractors": {
                "A": "Likelihood is the probability the flood happens, not how much it would cost.",
                "C": "A threat is the potential source of harm (the flood), not the measured consequence.",
                "D": "A vulnerability is the weakness (e.g., no flood protection), not the resulting loss."
            },
            "exam_pattern": "The size of the harm/consequence if it happens = impact."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 1 - Risk terms (impact)"
        ]
    },
    {
        "id": "isc2cc-prin-r2-010",
        "exam": "isc2cc",
        "domain": "cc_security_principles",
        "subtopic": "cc_risk_management",
        "difficulty": 1,
        "type": "mcq",
        "stem": "To reduce a risk, a company installs a web application firewall and fixes its software flaws, lowering both the chance and the effect of an attack. Which risk-treatment option is this?",
        "options": [
            {
                "id": "A",
                "text": "Risk acceptance"
            },
            {
                "id": "B",
                "text": "Risk avoidance"
            },
            {
                "id": "C",
                "text": "Risk mitigation (reduction)"
            },
            {
                "id": "D",
                "text": "Risk transference"
            }
        ],
        "correct": [
            "C"
        ],
        "explanation": {
            "correct": "Risk mitigation applies controls to reduce the likelihood and/or impact of a risk - exactly what adding a firewall and patching flaws does.",
            "distractors": {
                "A": "Acceptance means taking no action and absorbing the risk, not adding controls.",
                "B": "Avoidance means stopping the risky activity entirely, which the company did not do.",
                "D": "Transference shifts the loss to a third party (e.g., insurance); controls do not transfer it."
            },
            "exam_pattern": "Add controls to lower likelihood/impact = mitigation (reduction)."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 1 - Risk treatment (mitigation)"
        ]
    },
    {
        "id": "isc2cc-prin-r2-011",
        "exam": "isc2cc",
        "domain": "cc_security_principles",
        "subtopic": "cc_risk_management",
        "difficulty": 2,
        "type": "mcq",
        "stem": "After analysis, managers decide a particular risk is so small, and the cost of any control so high, that they will simply take no further action and absorb the risk if it occurs. This choice is:",
        "options": [
            {
                "id": "A",
                "text": "Risk mitigation"
            },
            {
                "id": "B",
                "text": "Risk avoidance"
            },
            {
                "id": "C",
                "text": "Risk acceptance"
            },
            {
                "id": "D",
                "text": "Risk transference"
            }
        ],
        "correct": [
            "C"
        ],
        "explanation": {
            "correct": "Risk acceptance is the informed decision to take no additional action and bear the risk, typically when the cost of a control outweighs the expected loss.",
            "distractors": {
                "A": "Mitigation would add controls to reduce the risk, which they chose not to do.",
                "B": "Avoidance would stop the activity entirely; acceptance continues it as-is.",
                "D": "Transference shifts the loss to a third party; here the organization keeps it."
            },
            "exam_pattern": "Knowingly take no action and absorb the risk = acceptance."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 1 - Risk treatment (acceptance)"
        ]
    },
    {
        "id": "isc2cc-prin-r2-012",
        "exam": "isc2cc",
        "domain": "cc_security_principles",
        "subtopic": "cc_risk_management",
        "difficulty": 1,
        "type": "mcq",
        "stem": "In risk management, anything of value to the organization that needs protection - such as data, hardware, facilities, or people - is called a(n):",
        "options": [
            {
                "id": "A",
                "text": "Threat"
            },
            {
                "id": "B",
                "text": "Asset"
            },
            {
                "id": "C",
                "text": "Vulnerability"
            },
            {
                "id": "D",
                "text": "Control"
            }
        ],
        "correct": [
            "B"
        ],
        "explanation": {
            "correct": "An asset is anything of value to the organization - information, systems, equipment, facilities, or people - that warrants protection.",
            "distractors": {
                "A": "A threat is a potential source of harm, not the valuable thing being protected.",
                "C": "A vulnerability is a weakness that could be exploited, not an item of value.",
                "D": "A control is a safeguard that protects assets, not the asset itself."
            },
            "exam_pattern": "The valuable thing you protect = asset."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 1 - Risk terms (asset)"
        ]
    },
    {
        "id": "isc2cc-prin-r2-013",
        "exam": "isc2cc",
        "domain": "cc_security_principles",
        "subtopic": "cc_risk_management",
        "difficulty": 2,
        "type": "fill",
        "stem": "The risk that still remains after security controls and safeguards have been applied is called ___ risk. (one word)",
        "correct": [
            "residual"
        ],
        "explanation": {
            "correct": "Residual risk is the risk left over after controls have reduced the original (inherent) risk; management decides whether that remaining level is acceptable.",
            "exam_pattern": "Risk left over after controls are applied = residual risk."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 1 - Risk terms (residual risk)"
        ]
    },

    # ----- cc_security_controls ------------------------------------------
    {
        "id": "isc2cc-prin-r2-014",
        "exam": "isc2cc",
        "domain": "cc_security_principles",
        "subtopic": "cc_security_controls",
        "difficulty": 2,
        "type": "mcq",
        "stem": "Right after a malware infection is found, antivirus software quarantines and removes the malicious files and the system is returned to a known-good state. By function, this is a ___ control.",
        "options": [
            {
                "id": "A",
                "text": "Preventive"
            },
            {
                "id": "B",
                "text": "Corrective"
            },
            {
                "id": "C",
                "text": "Detective"
            },
            {
                "id": "D",
                "text": "Deterrent"
            }
        ],
        "correct": [
            "B"
        ],
        "explanation": {
            "correct": "A corrective control acts after an incident to fix the problem and restore normal operation - here, removing the malware and cleaning the system.",
            "distractors": {
                "A": "A preventive control would have stopped the infection before it occurred.",
                "C": "A detective control only identifies/alerts that something happened; it does not remove the malware.",
                "D": "A deterrent control discourages attackers; it does not remediate an infection."
            },
            "exam_pattern": "Fixes/remediates after the event = corrective."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 1 - Security controls (corrective)"
        ]
    },
    {
        "id": "isc2cc-prin-r2-015",
        "exam": "isc2cc",
        "domain": "cc_security_principles",
        "subtopic": "cc_security_controls",
        "difficulty": 2,
        "type": "mcq",
        "stem": "A company posts prominent 'Warning: area under 24-hour video surveillance and monitored access' signs at its entrances to discourage would-be intruders. By function, the signs are a ___ control.",
        "options": [
            {
                "id": "A",
                "text": "Deterrent"
            },
            {
                "id": "B",
                "text": "Corrective"
            },
            {
                "id": "C",
                "text": "Detective"
            },
            {
                "id": "D",
                "text": "Recovery"
            }
        ],
        "correct": [
            "A"
        ],
        "explanation": {
            "correct": "A deterrent control discourages a potential attacker from acting; a visible warning sign aims to make an intruder think twice.",
            "distractors": {
                "B": "A corrective control fixes problems after an incident; a sign does not remediate anything.",
                "C": "A detective control records/alerts on events (the cameras themselves); the sign's role is to discourage.",
                "D": "A recovery control restores operations after damage; a warning sign does not."
            },
            "exam_pattern": "Discourages an attacker from trying (warning signs, visible guards) = deterrent."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 1 - Security controls (deterrent)"
        ]
    },
    {
        "id": "isc2cc-prin-r2-016",
        "exam": "isc2cc",
        "domain": "cc_security_principles",
        "subtopic": "cc_security_controls",
        "difficulty": 2,
        "type": "mcq",
        "stem": "Encryption, firewalls, and antivirus software are all implemented in hardware or software. By CATEGORY, these are ___ controls.",
        "options": [
            {
                "id": "A",
                "text": "Physical"
            },
            {
                "id": "B",
                "text": "Administrative (managerial)"
            },
            {
                "id": "C",
                "text": "Technical (logical)"
            },
            {
                "id": "D",
                "text": "Deterrent"
            }
        ],
        "correct": [
            "C"
        ],
        "explanation": {
            "correct": "Technical (logical) controls are implemented in hardware or software - firewalls, encryption, antivirus, and access-control lists are classic examples.",
            "distractors": {
                "A": "Physical controls are tangible barriers like locks, fences, and guards, not software.",
                "B": "Administrative controls are policies, procedures, and training, not technology settings.",
                "D": "'Deterrent' is a control function, not one of the three categories (technical/physical/administrative)."
            },
            "exam_pattern": "Implemented in hardware/software = technical (logical) controls."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 1 - Security controls (technical)"
        ]
    },
    {
        "id": "isc2cc-prin-r2-017",
        "exam": "isc2cc",
        "domain": "cc_security_principles",
        "subtopic": "cc_security_controls",
        "difficulty": 3,
        "type": "mcq",
        "stem": "A legacy system cannot support multifactor authentication, so the company adds an alternative safeguard - restricting that system to a tightly monitored, isolated network - to achieve comparable protection. This alternative safeguard is a ___ control.",
        "options": [
            {
                "id": "A",
                "text": "Compensating"
            },
            {
                "id": "B",
                "text": "Preventive"
            },
            {
                "id": "C",
                "text": "Detective"
            },
            {
                "id": "D",
                "text": "Deterrent"
            }
        ],
        "correct": [
            "A"
        ],
        "explanation": {
            "correct": "A compensating control is an alternative measure put in place when the primary control is not feasible, providing a comparable level of protection.",
            "distractors": {
                "B": "'Preventive' names what a control does; the point here is that it substitutes for an infeasible control (compensating).",
                "C": "A detective control finds events after the fact; this safeguard substitutes for a missing preventive control.",
                "D": "A deterrent discourages attackers; it is not specifically a stand-in for an unavailable control."
            },
            "exam_pattern": "Alternative that stands in for an infeasible primary control = compensating."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 1 - Security controls (compensating)"
        ]
    },
    {
        "id": "isc2cc-prin-r2-018",
        "exam": "isc2cc",
        "domain": "cc_security_principles",
        "subtopic": "cc_security_controls",
        "difficulty": 2,
        "type": "mcq",
        "stem": "After a ransomware attack, the team restores the encrypted servers from clean backups to return operations to normal. Restoring service and data from backups after an incident is primarily a ___ control.",
        "options": [
            {
                "id": "A",
                "text": "Preventive"
            },
            {
                "id": "B",
                "text": "Deterrent"
            },
            {
                "id": "C",
                "text": "Recovery"
            },
            {
                "id": "D",
                "text": "Detective"
            }
        ],
        "correct": [
            "C"
        ],
        "explanation": {
            "correct": "A recovery control restores systems, data, and operations to normal after a disruptive event - restoring from backup is a textbook recovery control.",
            "distractors": {
                "A": "A preventive control stops the incident up front; restoring afterward does not prevent it.",
                "B": "A deterrent discourages attackers; it does not restore lost data.",
                "D": "A detective control identifies that an event happened; it does not bring systems back."
            },
            "exam_pattern": "Restore operations/data after damage (e.g., from backup) = recovery; remove the cause = corrective."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 1 - Security controls (recovery)"
        ]
    },
    {
        "id": "isc2cc-prin-r2-019",
        "exam": "isc2cc",
        "domain": "cc_security_principles",
        "subtopic": "cc_security_controls",
        "difficulty": 3,
        "type": "multi",
        "stem": "A manager reviews a list of safeguards. Which TWO are TECHNICAL (logical) controls? (Choose two.)",
        "options": [
            {
                "id": "A",
                "text": "Full-disk encryption on laptops"
            },
            {
                "id": "B",
                "text": "Antivirus software on servers"
            },
            {
                "id": "C",
                "text": "A locked server-room door"
            },
            {
                "id": "D",
                "text": "A written data-handling policy"
            }
        ],
        "correct": [
            "A",
            "B"
        ],
        "explanation": {
            "correct": "Full-disk encryption and antivirus software are implemented in software/hardware, so both are technical (logical) controls.",
            "distractors": {
                "C": "A locked door is a tangible barrier - a physical control.",
                "D": "A written policy is an administrative (managerial) control, not a technology setting."
            },
            "exam_pattern": "Hardware/software = technical; barriers/guards = physical; policies/training = administrative."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 1 - Security controls (categories)"
        ]
    },

    # ----- cc_isc2_ethics ------------------------------------------------
    {
        "id": "isc2cc-prin-r2-020",
        "exam": "isc2cc",
        "domain": "cc_security_principles",
        "subtopic": "cc_isc2_ethics",
        "difficulty": 2,
        "type": "mcq",
        "stem": "A security tester is pressured by a client to omit a serious finding from the final report so the client 'looks better.' The tester refuses, insisting the report be truthful and accurate. Which (ISC)² canon most directly supports refusing?",
        "options": [
            {
                "id": "A",
                "text": "Protect society, the common good, and the infrastructure"
            },
            {
                "id": "B",
                "text": "Act honorably, honestly, justly, responsibly, and legally"
            },
            {
                "id": "C",
                "text": "Provide diligent and competent service to principals"
            },
            {
                "id": "D",
                "text": "Advance and protect the profession"
            }
        ],
        "correct": [
            "B"
        ],
        "explanation": {
            "correct": "The second canon requires acting honestly and with integrity; refusing to falsify or hide findings in a report is a direct application of it.",
            "distractors": {
                "A": "Protecting society addresses public safety and infrastructure, not the honesty of this report.",
                "C": "Serving principals concerns competent, diligent work; here the core issue is honesty/integrity.",
                "D": "Advancing the profession concerns the field's reputation, not this specific act of honesty."
            },
            "exam_pattern": "Honesty, integrity, and legality of conduct = Canon II (act honorably/honestly)."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 1 - (ISC)² Code of Ethics (Canon II)"
        ]
    },
    {
        "id": "isc2cc-prin-r2-021",
        "exam": "isc2cc",
        "domain": "cc_security_principles",
        "subtopic": "cc_isc2_ethics",
        "difficulty": 2,
        "type": "mcq",
        "stem": "An (ISC)² member mentors newcomers, upholds the certification's reputation, and never misrepresents their credentials. Which canon are they fulfilling?",
        "options": [
            {
                "id": "A",
                "text": "Advance and protect the profession"
            },
            {
                "id": "B",
                "text": "Protect society, the common good, and the infrastructure"
            },
            {
                "id": "C",
                "text": "Act honorably, honestly, justly, responsibly, and legally"
            },
            {
                "id": "D",
                "text": "Provide diligent and competent service to principals"
            }
        ],
        "correct": [
            "A"
        ],
        "explanation": {
            "correct": "The fourth canon is to advance and protect the profession - mentoring, safeguarding the certification's reputation, and representing credentials truthfully all serve it.",
            "distractors": {
                "B": "Protecting society is about public safety and infrastructure, not the profession's standing.",
                "C": "Acting honestly governs personal conduct; the emphasis here is specifically on the profession's reputation.",
                "D": "Serving principals concerns duty to employers/clients, not the profession as a whole."
            },
            "exam_pattern": "Reputation of the field, mentoring, honest credentials = Canon IV (advance/protect the profession)."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 1 - (ISC)² Code of Ethics (Canon IV)"
        ]
    },
    {
        "id": "isc2cc-prin-r2-022",
        "exam": "isc2cc",
        "domain": "cc_security_principles",
        "subtopic": "cc_isc2_ethics",
        "difficulty": 3,
        "type": "mcq",
        "stem": "The (ISC)² Code of Ethics lists its four canons in a deliberate order. When two canons appear to conflict, how are they meant to be applied?",
        "options": [
            {
                "id": "A",
                "text": "In the order presented, so the first canon (protect society) takes precedence"
            },
            {
                "id": "B",
                "text": "In reverse order, putting the employer's interests first"
            },
            {
                "id": "C",
                "text": "Whichever canon is most convenient for the member at the time"
            },
            {
                "id": "D",
                "text": "They can never conflict, so order does not matter"
            }
        ],
        "correct": [
            "A"
        ],
        "explanation": {
            "correct": "The canons are intended to be applied in the order given; the first canon - protect society, the common good, and the infrastructure - takes precedence over the others.",
            "distractors": {
                "B": "The employer (principal) canon does not outrank protecting society; that reverses the intended priority.",
                "C": "Ethics are not applied by convenience; the order is deliberate and principled.",
                "D": "Canons can appear to conflict; that is exactly why the ordering/precedence exists."
            },
            "exam_pattern": "Apply canons in order; Canon I (protect society) outranks the rest."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 1 - (ISC)² Code of Ethics (order/precedence)"
        ]
    },
    {
        "id": "isc2cc-prin-r2-023",
        "exam": "isc2cc",
        "domain": "cc_security_principles",
        "subtopic": "cc_isc2_ethics",
        "difficulty": 2,
        "type": "mcq",
        "stem": "What can happen to an (ISC)² member who is found, through the organization's peer-review process, to have seriously violated the Code of Ethics?",
        "options": [
            {
                "id": "A",
                "text": "Nothing - the Code is only a loose suggestion"
            },
            {
                "id": "B",
                "text": "They are automatically arrested by law enforcement"
            },
            {
                "id": "C",
                "text": "They can be sanctioned, up to and including revocation of their certification"
            },
            {
                "id": "D",
                "text": "They must pay a cash fine to the other members"
            }
        ],
        "correct": [
            "C"
        ],
        "explanation": {
            "correct": "The Code is binding on members; a serious, substantiated violation can lead to sanctions, including loss (revocation) of the (ISC)² certification.",
            "distractors": {
                "A": "The Code is mandatory for members, not optional - violations have real consequences.",
                "B": "(ISC)² is a professional body; it sanctions members, it does not arrest anyone.",
                "D": "The consequence is professional sanction/decertification, not a fine paid to members."
            },
            "exam_pattern": "Serious Code violations can cost a member their (ISC)² certification."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 1 - (ISC)² Code of Ethics (enforcement)"
        ]
    },

    # ----- cc_governance_policies ----------------------------------------
    {
        "id": "isc2cc-prin-r2-024",
        "exam": "isc2cc",
        "domain": "cc_security_principles",
        "subtopic": "cc_governance_policies",
        "difficulty": 1,
        "type": "mcq",
        "stem": "A document offers recommended - but optional - advice on choosing strong passphrases, which staff 'should' follow where practical. In the governance hierarchy, this non-mandatory recommendation is a:",
        "options": [
            {
                "id": "A",
                "text": "Standard"
            },
            {
                "id": "B",
                "text": "Guideline"
            },
            {
                "id": "C",
                "text": "Policy"
            },
            {
                "id": "D",
                "text": "Procedure"
            }
        ],
        "correct": [
            "B"
        ],
        "explanation": {
            "correct": "A guideline provides recommended, non-mandatory advice or best practice; compliance is encouraged but not required.",
            "distractors": {
                "A": "A standard is a mandatory, specific requirement, not optional advice.",
                "C": "A policy is a high-level, mandatory statement of intent, not a recommendation.",
                "D": "A procedure is a required step-by-step set of instructions, not optional guidance."
            },
            "exam_pattern": "Recommended / optional best practice = guideline; mandatory specific rule = standard."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 1 - Governance (guideline)"
        ]
    },
    {
        "id": "isc2cc-prin-r2-025",
        "exam": "isc2cc",
        "domain": "cc_security_principles",
        "subtopic": "cc_governance_policies",
        "difficulty": 2,
        "type": "mcq",
        "stem": "A company defines a minimum set of security settings - screen lock, disk encryption, firewall enabled - that EVERY laptop must meet before it is issued. This required minimum configuration is called a:",
        "options": [
            {
                "id": "A",
                "text": "Guideline"
            },
            {
                "id": "B",
                "text": "Baseline"
            },
            {
                "id": "C",
                "text": "Procedure"
            },
            {
                "id": "D",
                "text": "Regulation"
            }
        ],
        "correct": [
            "B"
        ],
        "explanation": {
            "correct": "A baseline defines the minimum level of security (a standard configuration) that all systems of a given type must meet.",
            "distractors": {
                "A": "A guideline is optional advice, not a mandatory minimum every device must meet.",
                "C": "A procedure lists ordered steps for a task, not a minimum configuration standard.",
                "D": "A regulation is an externally imposed legal requirement, not an internal configuration minimum."
            },
            "exam_pattern": "Mandatory minimum security configuration for all systems = baseline."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 1 - Governance (baseline)"
        ]
    },
    {
        "id": "isc2cc-prin-r2-026",
        "exam": "isc2cc",
        "domain": "cc_security_principles",
        "subtopic": "cc_governance_policies",
        "difficulty": 2,
        "type": "mcq",
        "stem": "HIPAA and GDPR require organizations to protect certain personal data, and non-compliance can bring legal penalties. Compared with an internal policy, these externally imposed legal requirements are examples of:",
        "options": [
            {
                "id": "A",
                "text": "Guidelines"
            },
            {
                "id": "B",
                "text": "Laws and regulations"
            },
            {
                "id": "C",
                "text": "Procedures"
            },
            {
                "id": "D",
                "text": "Internal standards"
            }
        ],
        "correct": [
            "B"
        ],
        "explanation": {
            "correct": "Laws and regulations are externally imposed, legally enforceable requirements; HIPAA and GDPR are classic examples that carry legal penalties for non-compliance.",
            "distractors": {
                "A": "Guidelines are optional internal advice, not legally enforceable external mandates.",
                "C": "Procedures are internal step-by-step instructions, not external legal requirements.",
                "D": "Standards here are internal mandatory specs; HIPAA/GDPR are external laws/regulations."
            },
            "exam_pattern": "Externally imposed, legally enforceable = laws/regulations; internal = policy/standard/procedure/guideline."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 1 - Governance (laws and regulations)"
        ]
    },
    {
        "id": "isc2cc-prin-r2-027",
        "exam": "isc2cc",
        "domain": "cc_security_principles",
        "subtopic": "cc_governance_policies",
        "difficulty": 1,
        "type": "mcq",
        "stem": "Information such as a person's full name combined with their Social Security number, which can be used to identify a specific individual, is known as:",
        "options": [
            {
                "id": "A",
                "text": "Personally Identifiable Information (PII)"
            },
            {
                "id": "B",
                "text": "Public information"
            },
            {
                "id": "C",
                "text": "Metadata"
            },
            {
                "id": "D",
                "text": "Ciphertext"
            }
        ],
        "correct": [
            "A"
        ],
        "explanation": {
            "correct": "PII is any information that can identify a specific individual (e.g., name plus SSN); it requires protection and careful handling for privacy.",
            "distractors": {
                "B": "Public information is freely available and not sensitive, unlike identifying personal data.",
                "C": "Metadata is data about data (e.g., a file's timestamp), not identifying personal information.",
                "D": "Ciphertext is encrypted data, not a category of personal information."
            },
            "exam_pattern": "Data that identifies a specific person = PII (privacy-sensitive)."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 1 - Privacy (PII)"
        ]
    },
    {
        "id": "isc2cc-prin-r2-028",
        "exam": "isc2cc",
        "domain": "cc_security_principles",
        "subtopic": "cc_governance_policies",
        "difficulty": 2,
        "type": "mcq",
        "stem": "The principle that individuals have the right to control how their personal information is collected, used, and shared is best described as:",
        "options": [
            {
                "id": "A",
                "text": "Availability"
            },
            {
                "id": "B",
                "text": "Privacy"
            },
            {
                "id": "C",
                "text": "Non-repudiation"
            },
            {
                "id": "D",
                "text": "Redundancy"
            }
        ],
        "correct": [
            "B"
        ],
        "explanation": {
            "correct": "Privacy is the right of individuals to control the collection, use, and sharing of their personal information.",
            "distractors": {
                "A": "Availability is about systems/data being reachable, not control over personal information.",
                "C": "Non-repudiation is proof of an action's origin, unrelated to personal-data control.",
                "D": "Redundancy is duplicating components for reliability, not a privacy principle."
            },
            "exam_pattern": "Individuals' control over their personal data = privacy."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 1 - Privacy (definition)"
        ]
    },
    {
        "id": "isc2cc-prin-r2-029",
        "exam": "isc2cc",
        "domain": "cc_security_principles",
        "subtopic": "cc_governance_policies",
        "difficulty": 2,
        "type": "mcq",
        "stem": "In a well-governed organization, who holds ultimate responsibility for formally approving and endorsing the enterprise information security policy?",
        "options": [
            {
                "id": "A",
                "text": "The help desk"
            },
            {
                "id": "B",
                "text": "Individual end users"
            },
            {
                "id": "C",
                "text": "Senior (executive) management"
            },
            {
                "id": "D",
                "text": "The external auditors"
            }
        ],
        "correct": [
            "C"
        ],
        "explanation": {
            "correct": "Senior management owns, approves, and endorses the security policy, setting the tone and providing the authority and resources behind it.",
            "distractors": {
                "A": "The help desk operates support processes; it does not approve enterprise policy.",
                "B": "End users must follow the policy but do not approve it.",
                "D": "Auditors assess compliance with the policy; they do not approve or own it."
            },
            "exam_pattern": "Security policy is owned/approved at the top - by senior management."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 1 - Governance (policy ownership)"
        ]
    },

    # =====================================================================
    # DOMAIN 2 - BC, DR & INCIDENT RESPONSE (cc_bcdr_ir)
    # =====================================================================

    # ----- cc_incident_response ------------------------------------------
    {
        "id": "isc2cc-bcdr-r2-001",
        "exam": "isc2cc",
        "domain": "cc_bcdr_ir",
        "subtopic": "cc_incident_response",
        "difficulty": 2,
        "type": "mcq",
        "stem": "Malware has been removed and the exploited vulnerability patched. The team now restores the cleaned servers to production and carefully monitors them to confirm they operate normally. Which incident-response phase is this?",
        "options": [
            {
                "id": "A",
                "text": "Containment"
            },
            {
                "id": "B",
                "text": "Eradication"
            },
            {
                "id": "C",
                "text": "Recovery"
            },
            {
                "id": "D",
                "text": "Preparation"
            }
        ],
        "correct": [
            "C"
        ],
        "explanation": {
            "correct": "Recovery restores affected systems to normal operation and verifies they are clean and functioning, after the threat has been contained and eradicated.",
            "distractors": {
                "A": "Containment limits the spread of an active incident; it happens before eradication and recovery.",
                "B": "Eradication removes the threat and its cause; that step has just been completed here.",
                "D": "Preparation is the readiness work done before any incident occurs."
            },
            "exam_pattern": "Restore cleaned systems to normal and confirm = recovery (after containment + eradication)."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 2 - Incident response (recovery)"
        ]
    },
    {
        "id": "isc2cc-bcdr-r2-002",
        "exam": "isc2cc",
        "domain": "cc_bcdr_ir",
        "subtopic": "cc_incident_response",
        "difficulty": 2,
        "type": "mcq",
        "stem": "An alert fires, and the response team examines logs to confirm whether a real security incident is occurring and to determine its scope and severity. Which incident-response phase is this?",
        "options": [
            {
                "id": "A",
                "text": "Preparation"
            },
            {
                "id": "B",
                "text": "Detection and analysis"
            },
            {
                "id": "C",
                "text": "Containment"
            },
            {
                "id": "D",
                "text": "Recovery"
            }
        ],
        "correct": [
            "B"
        ],
        "explanation": {
            "correct": "Detection and analysis is the phase where the team identifies a possible incident and analyzes evidence to confirm it and understand its scope and severity.",
            "distractors": {
                "A": "Preparation builds plans, tools, and training before incidents happen.",
                "C": "Containment acts to limit spread after the incident is confirmed, not to confirm it.",
                "D": "Recovery restores systems after the threat is removed, not the initial confirmation step."
            },
            "exam_pattern": "Confirm it's a real incident and size it up = detection and analysis."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 2 - Incident response (detection and analysis)"
        ]
    },
    {
        "id": "isc2cc-bcdr-r2-003",
        "exam": "isc2cc",
        "domain": "cc_bcdr_ir",
        "subtopic": "cc_incident_response",
        "difficulty": 2,
        "type": "mcq",
        "stem": "An investigation confirms that an attacker actually accessed and copied a database of customers' personal data. An incident in which protected data is confirmed to have been exposed to unauthorized parties is specifically called a:",
        "options": [
            {
                "id": "A",
                "text": "An event"
            },
            {
                "id": "B",
                "text": "A data breach"
            },
            {
                "id": "C",
                "text": "A vulnerability"
            },
            {
                "id": "D",
                "text": "A false positive"
            }
        ],
        "correct": [
            "B"
        ],
        "explanation": {
            "correct": "A data breach is a confirmed incident in which sensitive or protected data is actually accessed or disclosed to unauthorized parties.",
            "distractors": {
                "A": "An event is any observable occurrence; most events are harmless and are not breaches.",
                "C": "A vulnerability is a weakness that could be exploited, not a confirmed data exposure.",
                "D": "A false positive is an alert that turns out to be benign, the opposite of a confirmed breach."
            },
            "exam_pattern": "Confirmed unauthorized access/disclosure of protected data = breach."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 2 - Incident terminology (breach)"
        ]
    },
    {
        "id": "isc2cc-bcdr-r2-004",
        "exam": "isc2cc",
        "domain": "cc_bcdr_ir",
        "subtopic": "cc_incident_response",
        "difficulty": 1,
        "type": "mcq",
        "stem": "An employee notices their computer behaving strangely and suspects malware. According to good incident-response practice, what should they do FIRST?",
        "options": [
            {
                "id": "A",
                "text": "Report it promptly to the help desk or security team per the incident-response procedure"
            },
            {
                "id": "B",
                "text": "Try to delete suspicious files themselves to 'fix' it"
            },
            {
                "id": "C",
                "text": "Ignore it unless it happens again"
            },
            {
                "id": "D",
                "text": "Immediately reformat the hard drive on their own"
            }
        ],
        "correct": [
            "A"
        ],
        "explanation": {
            "correct": "Users should promptly report a suspected incident through the proper channel so trained responders can act; quick reporting is critical to limiting damage.",
            "distractors": {
                "B": "Deleting files can destroy evidence and tip off or worsen the situation; responders should handle it.",
                "C": "Ignoring a suspected incident lets it spread and delays response.",
                "D": "Reformatting destroys evidence and may be unnecessary; that is a responder decision, not a first user step."
            },
            "exam_pattern": "Users: report suspected incidents quickly through the right channel - don't investigate or wipe on your own."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 2 - Incident response (reporting)"
        ]
    },

    # ----- cc_business_continuity ----------------------------------------
    {
        "id": "isc2cc-bcdr-r2-005",
        "exam": "isc2cc",
        "domain": "cc_bcdr_ir",
        "subtopic": "cc_business_continuity",
        "difficulty": 3,
        "type": "mcq",
        "stem": "The longest period a critical business function can be unavailable before the organization suffers unacceptable or irreparable harm is known as the:",
        "options": [
            {
                "id": "A",
                "text": "Recovery Point Objective (RPO)"
            },
            {
                "id": "B",
                "text": "Maximum Tolerable Downtime (MTD)"
            },
            {
                "id": "C",
                "text": "Recovery Time Objective (RTO)"
            },
            {
                "id": "D",
                "text": "Mean Time To Repair (MTTR)"
            }
        ],
        "correct": [
            "B"
        ],
        "explanation": {
            "correct": "Maximum Tolerable Downtime (MTD) is the absolute limit a function can be down before the harm becomes unacceptable; recovery objectives must fit inside it.",
            "distractors": {
                "A": "RPO is the maximum acceptable data loss, measured in time, not the total downtime limit.",
                "C": "RTO is the target time to restore service and must be shorter than the MTD; it is not the hard limit itself.",
                "D": "MTTR is the average time to repair a failed component, a reliability metric, not the tolerance limit."
            },
            "exam_pattern": "Hard limit a function can be down before serious harm = MTD; RTO must be < MTD."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 2 - Business continuity (MTD)"
        ]
    },
    {
        "id": "isc2cc-bcdr-r2-006",
        "exam": "isc2cc",
        "domain": "cc_bcdr_ir",
        "subtopic": "cc_business_continuity",
        "difficulty": 2,
        "type": "mcq",
        "stem": "To test its plans without disrupting live systems, a team gathers in a room and talks through, step by step, how they would respond to a hypothetical disaster in order to find gaps. This low-impact test is a:",
        "options": [
            {
                "id": "A",
                "text": "Full-interruption test"
            },
            {
                "id": "B",
                "text": "Tabletop exercise"
            },
            {
                "id": "C",
                "text": "Penetration test"
            },
            {
                "id": "D",
                "text": "Vulnerability scan"
            }
        ],
        "correct": [
            "B"
        ],
        "explanation": {
            "correct": "A tabletop exercise is a discussion-based walkthrough of a plan; participants talk through a scenario to find gaps without touching production systems.",
            "distractors": {
                "A": "A full-interruption test actually shuts down production to switch to recovery - the highest-impact test, not this.",
                "C": "A penetration test probes for exploitable security weaknesses, not continuity-plan gaps.",
                "D": "A vulnerability scan finds technical flaws in systems, not plan gaps via discussion."
            },
            "exam_pattern": "Discussion-based plan walkthrough = tabletop exercise (lowest impact)."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 2 - Business continuity (plan testing)"
        ]
    },
    {
        "id": "isc2cc-bcdr-r2-007",
        "exam": "isc2cc",
        "domain": "cc_bcdr_ir",
        "subtopic": "cc_business_continuity",
        "difficulty": 2,
        "type": "mcq",
        "stem": "After a major outage, limited staff and resources mean not everything can be recovered at once. Which systems should be restored FIRST?",
        "options": [
            {
                "id": "A",
                "text": "The most critical/essential business functions, as prioritized by the business impact analysis"
            },
            {
                "id": "B",
                "text": "Whichever systems happen to be easiest to fix"
            },
            {
                "id": "C",
                "text": "The systems belonging to the most senior employees"
            },
            {
                "id": "D",
                "text": "The newest systems, regardless of importance"
            }
        ],
        "correct": [
            "A"
        ],
        "explanation": {
            "correct": "Recovery priority follows criticality: the business impact analysis (BIA) identifies the most essential functions, which are restored first.",
            "distractors": {
                "B": "Ease of repair does not reflect business importance; critical functions may be harder but must come first.",
                "C": "Seniority of the owner does not determine a function's criticality to the mission.",
                "D": "Newness is irrelevant; importance to the business drives recovery order."
            },
            "exam_pattern": "Restore most critical functions first, per the BIA."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 2 - Business continuity (recovery priorities)"
        ]
    },

    # ----- cc_disaster_recovery ------------------------------------------
    {
        "id": "isc2cc-bcdr-r2-008",
        "exam": "isc2cc",
        "domain": "cc_bcdr_ir",
        "subtopic": "cc_disaster_recovery",
        "difficulty": 2,
        "type": "mcq",
        "stem": "An organization wants an alternate site that already has hardware and network connectivity in place but needs current data loaded before it can take over - balancing cost against recovery speed. This is a:",
        "options": [
            {
                "id": "A",
                "text": "Hot site"
            },
            {
                "id": "B",
                "text": "Cold site"
            },
            {
                "id": "C",
                "text": "Warm site"
            },
            {
                "id": "D",
                "text": "Reciprocal agreement"
            }
        ],
        "correct": [
            "C"
        ],
        "explanation": {
            "correct": "A warm site is partially equipped - hardware and connectivity are ready, but current data must be restored - making it a middle ground in cost and recovery time.",
            "distractors": {
                "A": "A hot site is fully equipped with current data and ready almost immediately (costliest).",
                "B": "A cold site has only space, power, and cooling - no ready hardware - so it is slowest.",
                "D": "A reciprocal agreement shares another organization's facility; it is not a partially equipped standby site."
            },
            "exam_pattern": "Equipped but data not current, middle cost/speed = warm site."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 2 - Disaster recovery (recovery sites)"
        ]
    },
    {
        "id": "isc2cc-bcdr-r2-009",
        "exam": "isc2cc",
        "domain": "cc_bcdr_ir",
        "subtopic": "cc_disaster_recovery",
        "difficulty": 2,
        "type": "mcq",
        "stem": "Which backup type copies ALL selected data every time it runs - taking the longest to create but allowing the simplest restore from a single backup set?",
        "options": [
            {
                "id": "A",
                "text": "Full backup"
            },
            {
                "id": "B",
                "text": "Incremental backup"
            },
            {
                "id": "C",
                "text": "Differential backup"
            },
            {
                "id": "D",
                "text": "Snapshot"
            }
        ],
        "correct": [
            "A"
        ],
        "explanation": {
            "correct": "A full backup copies all selected data each time; it uses the most time and storage but restores from just that one set, making recovery the simplest.",
            "distractors": {
                "B": "An incremental backup copies only changes since the last backup of any type; a restore needs the full plus every increment.",
                "C": "A differential backup copies changes since the last full; a restore needs the full plus the latest differential.",
                "D": "A snapshot is a point-in-time image of a system/volume, not a copy-everything backup job."
            },
            "exam_pattern": "Copies everything each run, single-set restore = full backup."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 2 - Disaster recovery (backup types)"
        ]
    },
    {
        "id": "isc2cc-bcdr-r2-010",
        "exam": "isc2cc",
        "domain": "cc_bcdr_ir",
        "subtopic": "cc_disaster_recovery",
        "difficulty": 3,
        "type": "mcq",
        "stem": "A backup job copies only the data changed since the last backup of ANY kind. Backups are quick to make, but a full restore requires the last full backup PLUS every one of these jobs applied in order. Which backup type is this?",
        "options": [
            {
                "id": "A",
                "text": "Differential backup"
            },
            {
                "id": "B",
                "text": "Incremental backup"
            },
            {
                "id": "C",
                "text": "Full backup"
            },
            {
                "id": "D",
                "text": "Mirror backup"
            }
        ],
        "correct": [
            "B"
        ],
        "explanation": {
            "correct": "An incremental backup captures only what changed since the last backup of any type, so each run is small, but a restore needs the full backup plus every incremental in order.",
            "distractors": {
                "A": "A differential copies changes since the last FULL; a restore needs only the full plus the newest differential.",
                "C": "A full backup copies everything each time; it is not 'only changes since the last backup.'",
                "D": "A mirror keeps an exact live copy of the source; it is not the described chained change-based backup."
            },
            "exam_pattern": "Changes since last ANY backup, restore = full + all increments in order = incremental."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 2 - Disaster recovery (backup types)"
        ]
    },
    {
        "id": "isc2cc-bcdr-r2-011",
        "exam": "isc2cc",
        "domain": "cc_bcdr_ir",
        "subtopic": "cc_disaster_recovery",
        "difficulty": 2,
        "type": "mcq",
        "stem": "Why should an organization keep copies of its backups at a separate, geographically distant location?",
        "options": [
            {
                "id": "A",
                "text": "So a local disaster such as a fire or flood cannot destroy both the production systems and their backups"
            },
            {
                "id": "B",
                "text": "So the backups run noticeably faster"
            },
            {
                "id": "C",
                "text": "So the backups no longer need to be encrypted"
            },
            {
                "id": "D",
                "text": "So restores never need to be tested"
            }
        ],
        "correct": [
            "A"
        ],
        "explanation": {
            "correct": "Off-site, geographically separate backups survive a disaster that strikes the primary site, ensuring a recoverable copy still exists.",
            "distractors": {
                "B": "Off-site storage does not make backups run faster; it is about surviving local disasters.",
                "C": "Backups of sensitive data should still be encrypted regardless of where they are stored.",
                "D": "Restores must still be tested; location does not remove that need."
            },
            "exam_pattern": "Off-site/geographically separate copies survive a disaster that hits the primary site."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 2 - Disaster recovery (off-site backups)"
        ]
    },

    # =====================================================================
    # DOMAIN 3 - ACCESS CONTROLS CONCEPTS (cc_access_controls)
    # =====================================================================

    # ----- cc_access_control_concepts ------------------------------------
    {
        "id": "isc2cc-acc-r2-001",
        "exam": "isc2cc",
        "domain": "cc_access_controls",
        "subtopic": "cc_access_control_concepts",
        "difficulty": 2,
        "type": "mcq",
        "stem": "When a user opens a report file, which element is the OBJECT in access-control terms?",
        "options": [
            {
                "id": "A",
                "text": "The report file (the passive resource being accessed)"
            },
            {
                "id": "B",
                "text": "The user requesting access"
            },
            {
                "id": "C",
                "text": "The program the user clicked"
            },
            {
                "id": "D",
                "text": "The authentication server"
            }
        ],
        "correct": [
            "A"
        ],
        "explanation": {
            "correct": "An object is the passive resource that is acted upon - here, the report file being accessed.",
            "distractors": {
                "B": "The user is the active entity requesting access - that is the subject, not the object.",
                "C": "The program acts on the user's behalf and is part of the subject, not the passive resource.",
                "D": "The authentication server is a system component, not the resource being accessed in this action."
            },
            "exam_pattern": "Passive resource acted upon = object; active requester = subject."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 3 - Access control concepts (objects)"
        ]
    },
    {
        "id": "isc2cc-acc-r2-002",
        "exam": "isc2cc",
        "domain": "cc_access_controls",
        "subtopic": "cc_access_control_concepts",
        "difficulty": 1,
        "type": "mcq",
        "stem": "A user has already proven their identity by logging in. The system now determines which files and functions they are allowed to use. This step is:",
        "options": [
            {
                "id": "A",
                "text": "Identification"
            },
            {
                "id": "B",
                "text": "Authentication"
            },
            {
                "id": "C",
                "text": "Authorization"
            },
            {
                "id": "D",
                "text": "Accounting"
            }
        ],
        "correct": [
            "C"
        ],
        "explanation": {
            "correct": "Authorization determines what an authenticated subject is permitted to do - which resources and actions they may access.",
            "distractors": {
                "A": "Identification is claiming an identity (e.g., entering a username), which came earlier.",
                "B": "Authentication proves the claimed identity; it precedes deciding what the user may do.",
                "D": "Accounting records what the user does after access, not what they are allowed to do."
            },
            "exam_pattern": "Decide what an authenticated user may do = authorization (after identification + authentication)."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 3 - Access control concepts (authorization)"
        ]
    },
    {
        "id": "isc2cc-acc-r2-003",
        "exam": "isc2cc",
        "domain": "cc_access_controls",
        "subtopic": "cc_access_control_concepts",
        "difficulty": 2,
        "type": "mcq",
        "stem": "A firewall is configured so that any traffic not specifically permitted by a rule is blocked. This secure default posture is called:",
        "options": [
            {
                "id": "A",
                "text": "Implicit (default) deny"
            },
            {
                "id": "B",
                "text": "Implicit allow"
            },
            {
                "id": "C",
                "text": "Separation of duties"
            },
            {
                "id": "D",
                "text": "Single sign-on"
            }
        ],
        "correct": [
            "A"
        ],
        "explanation": {
            "correct": "Implicit (default) deny blocks anything not explicitly allowed, a secure default that supports least privilege.",
            "distractors": {
                "B": "Implicit allow permits anything not explicitly blocked - the insecure opposite.",
                "C": "Separation of duties splits a critical task among people; it is not a default-access rule.",
                "D": "Single sign-on is an authentication convenience, unrelated to a deny-by-default rule."
            },
            "exam_pattern": "Block unless explicitly allowed = implicit/default deny."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 3 - Access control concepts (default deny)"
        ]
    },
    {
        "id": "isc2cc-acc-r2-004",
        "exam": "isc2cc",
        "domain": "cc_access_controls",
        "subtopic": "cc_access_control_concepts",
        "difficulty": 3,
        "type": "mcq",
        "stem": "Over five years an employee moved through three departments. Each move added new permissions, but none were ever removed, so she now has far more access than her current job needs. This accumulation is called:",
        "options": [
            {
                "id": "A",
                "text": "Least privilege"
            },
            {
                "id": "B",
                "text": "Privilege creep (permission creep)"
            },
            {
                "id": "C",
                "text": "Separation of duties"
            },
            {
                "id": "D",
                "text": "Privilege escalation"
            }
        ],
        "correct": [
            "B"
        ],
        "explanation": {
            "correct": "Privilege creep is the gradual accumulation of access rights as a person changes roles without old permissions being revoked - it violates least privilege.",
            "distractors": {
                "A": "Least privilege is the goal (minimum needed access); creep is the failure to maintain it.",
                "C": "Separation of duties splits a task among people; it is not about one person's accumulated rights.",
                "D": "Privilege escalation is an attack that gains higher rights, not gradual buildup through legitimate role changes."
            },
            "exam_pattern": "Access piling up across role changes, never pruned = privilege creep (fix with access reviews)."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 3 - Access control concepts (privilege creep)"
        ]
    },
    {
        "id": "isc2cc-acc-r2-005",
        "exam": "isc2cc",
        "domain": "cc_access_controls",
        "subtopic": "cc_access_control_concepts",
        "difficulty": 2,
        "type": "mcq",
        "stem": "A bank periodically moves employees through different duties and requires them to take their full vacation, so that any hidden fraud is more likely to surface while someone else covers their work. These practices are:",
        "options": [
            {
                "id": "A",
                "text": "Job rotation and mandatory vacation"
            },
            {
                "id": "B",
                "text": "Least privilege"
            },
            {
                "id": "C",
                "text": "Defense in depth"
            },
            {
                "id": "D",
                "text": "Single sign-on"
            }
        ],
        "correct": [
            "A"
        ],
        "explanation": {
            "correct": "Job rotation and mandatory vacation are administrative controls that expose fraud and reduce over-reliance on any one person by ensuring others perform their duties.",
            "distractors": {
                "B": "Least privilege limits how much access a person has; it is not about rotating duties or forcing time off.",
                "C": "Defense in depth layers multiple controls; it does not describe rotating staff or mandatory vacation.",
                "D": "Single sign-on is an authentication convenience, unrelated to fraud-detection staffing practices."
            },
            "exam_pattern": "Rotate duties / force time off to surface hidden fraud = job rotation & mandatory vacation."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 3 - Access control concepts (job rotation)"
        ]
    },
    {
        "id": "isc2cc-acc-r2-006",
        "exam": "isc2cc",
        "domain": "cc_access_controls",
        "subtopic": "cc_access_control_concepts",
        "difficulty": 2,
        "type": "mcq",
        "stem": "In a software release process, one engineer writes the code, but a different, authorized person must review and approve it before it is deployed to production. Which principle does this enforce?",
        "options": [
            {
                "id": "A",
                "text": "Least privilege"
            },
            {
                "id": "B",
                "text": "Need to know"
            },
            {
                "id": "C",
                "text": "Separation of duties"
            },
            {
                "id": "D",
                "text": "Implicit deny"
            }
        ],
        "correct": [
            "C"
        ],
        "explanation": {
            "correct": "Separation of duties splits a sensitive process so no single person controls it end to end; requiring a second person to approve and deploy enforces exactly that.",
            "distractors": {
                "A": "Least privilege limits each person's access level; it does not require splitting a task across people.",
                "B": "Need to know restricts access to specific information, not the division of process steps.",
                "D": "Implicit deny is a default-block rule, not the splitting of a sensitive task among people."
            },
            "exam_pattern": "No single person controls a sensitive process end to end = separation of duties."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 3 - Access control concepts (separation of duties)"
        ]
    },

    # ----- cc_physical_access --------------------------------------------
    {
        "id": "isc2cc-acc-r2-007",
        "exam": "isc2cc",
        "domain": "cc_access_controls",
        "subtopic": "cc_physical_access",
        "difficulty": 1,
        "type": "mcq",
        "stem": "Employees gain entry to the office by tapping an ID card against a reader by the door. The card-and-reader system is a physical access control based on:",
        "options": [
            {
                "id": "A",
                "text": "An access badge (something the employee carries), read by a card reader"
            },
            {
                "id": "B",
                "text": "A biometric body trait"
            },
            {
                "id": "C",
                "text": "A bollard"
            },
            {
                "id": "D",
                "text": "A honeypot"
            }
        ],
        "correct": [
            "A"
        ],
        "explanation": {
            "correct": "An access badge or proximity card is something the employee carries; a reader checks it to grant or deny physical entry.",
            "distractors": {
                "B": "A biometric reads a body trait (fingerprint, face), not a carried card.",
                "C": "A bollard is a post that blocks vehicles; it does not grant person-by-person entry.",
                "D": "A honeypot is a decoy computer system, not a physical door control."
            },
            "exam_pattern": "Tap-to-enter ID card = access badge / proximity card (something you have)."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 3 - Physical access controls (badges)"
        ]
    },
    {
        "id": "isc2cc-acc-r2-008",
        "exam": "isc2cc",
        "domain": "cc_access_controls",
        "subtopic": "cc_physical_access",
        "difficulty": 2,
        "type": "mcq",
        "stem": "A data-center door grants entry only after scanning an authorized person's fingerprint. This control authenticates people using:",
        "options": [
            {
                "id": "A",
                "text": "A password (something you know)"
            },
            {
                "id": "B",
                "text": "A biometric trait (something you are)"
            },
            {
                "id": "C",
                "text": "A smart card (something you have)"
            },
            {
                "id": "D",
                "text": "A security question"
            }
        ],
        "correct": [
            "B"
        ],
        "explanation": {
            "correct": "A fingerprint is a biometric - a 'something you are' factor - used here to control physical entry.",
            "distractors": {
                "A": "A password is knowledge-based (something you know), not a scanned body trait.",
                "C": "A smart card is a possession (something you have), not a biometric.",
                "D": "A security question is knowledge-based, not a physical biometric trait."
            },
            "exam_pattern": "Fingerprint/iris/face at a door = biometric (something you are)."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 3 - Physical access controls (biometrics)"
        ]
    },
    {
        "id": "isc2cc-acc-r2-009",
        "exam": "isc2cc",
        "domain": "cc_access_controls",
        "subtopic": "cc_physical_access",
        "difficulty": 1,
        "type": "mcq",
        "stem": "A tall perimeter fence around a facility primarily serves to:",
        "options": [
            {
                "id": "A",
                "text": "Encrypt network traffic leaving the building"
            },
            {
                "id": "B",
                "text": "Deter and delay unauthorized people from entering the grounds"
            },
            {
                "id": "C",
                "text": "Detect malware on employee laptops"
            },
            {
                "id": "D",
                "text": "Filter firewall rules"
            }
        ],
        "correct": [
            "B"
        ],
        "explanation": {
            "correct": "A fence is a physical control that deters and delays intruders, forming a first line of perimeter defense around a site.",
            "distractors": {
                "A": "Encryption is a technical control for data; a fence does nothing to network traffic.",
                "C": "Malware detection is a technical/host control, unrelated to a perimeter fence.",
                "D": "Firewall rules are a network control; a fence has no role in traffic filtering."
            },
            "exam_pattern": "Perimeter fence = physical deterrent/barrier (first line of defense)."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 3 - Physical access controls (perimeter barriers)"
        ]
    },
    {
        "id": "isc2cc-acc-r2-010",
        "exam": "isc2cc",
        "domain": "cc_access_controls",
        "subtopic": "cc_physical_access",
        "difficulty": 2,
        "type": "mcq",
        "stem": "A lobby installs a waist-high barrier that admits exactly one person for each valid badge scan, making it hard for a second person to slip through behind them. This control is a:",
        "options": [
            {
                "id": "A",
                "text": "Turnstile"
            },
            {
                "id": "B",
                "text": "Bollard"
            },
            {
                "id": "C",
                "text": "CCTV camera"
            },
            {
                "id": "D",
                "text": "Firewall"
            }
        ],
        "correct": [
            "A"
        ],
        "explanation": {
            "correct": "A turnstile admits one person per valid credential, helping prevent tailgating in busy entrances.",
            "distractors": {
                "B": "A bollard stops vehicles; it does not meter people one at a time.",
                "C": "A CCTV camera records activity but does not physically restrict who passes.",
                "D": "A firewall filters network traffic; it is not a physical entry barrier."
            },
            "exam_pattern": "One-person-per-credential barrier in a lobby = turnstile (anti-tailgating)."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 3 - Physical access controls (turnstile)"
        ]
    },
    {
        "id": "isc2cc-acc-r2-011",
        "exam": "isc2cc",
        "domain": "cc_access_controls",
        "subtopic": "cc_physical_access",
        "difficulty": 1,
        "type": "fill",
        "stem": "Installing bright exterior ___ around a building at night deters intruders and helps security cameras capture clear images. (one word)",
        "correct": [
            "lighting",
            "lights",
            "light"
        ],
        "explanation": {
            "correct": "Exterior lighting is a physical control that discourages intruders and improves the usefulness of surveillance cameras after dark.",
            "exam_pattern": "Bright exterior lighting = physical deterrent that also aids surveillance."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 3 - Physical access controls (lighting)"
        ]
    },
    {
        "id": "isc2cc-acc-r2-012",
        "exam": "isc2cc",
        "domain": "cc_access_controls",
        "subtopic": "cc_physical_access",
        "difficulty": 2,
        "type": "mcq",
        "stem": "To reduce the chance that a laptop is physically stolen from an open desk in a shared workspace, an employee can secure it with a:",
        "options": [
            {
                "id": "A",
                "text": "VPN"
            },
            {
                "id": "B",
                "text": "Stronger password"
            },
            {
                "id": "C",
                "text": "Cable lock anchoring it to the desk"
            },
            {
                "id": "D",
                "text": "Full-disk encryption"
            }
        ],
        "correct": [
            "C"
        ],
        "explanation": {
            "correct": "A cable lock physically tethers the laptop to a fixed object, deterring and delaying theft of the device itself.",
            "distractors": {
                "A": "A VPN encrypts network traffic; it does nothing to stop someone carrying the laptop away.",
                "B": "A strong password protects login access but not the physical device from being taken.",
                "D": "Full-disk encryption protects the DATA if the laptop is stolen, but it does not prevent the theft."
            },
            "exam_pattern": "Tether the device = cable lock (physical); encryption protects the data, not against theft."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 3 - Physical access controls (device locks)"
        ]
    },

    # ----- cc_logical_access ---------------------------------------------
    {
        "id": "isc2cc-acc-r2-013",
        "exam": "isc2cc",
        "domain": "cc_access_controls",
        "subtopic": "cc_logical_access",
        "difficulty": 2,
        "type": "mcq",
        "stem": "On a file server, each file has an attached list specifying which users or groups may read, write, or execute it. This list is called a(n):",
        "options": [
            {
                "id": "A",
                "text": "Access control list (ACL)"
            },
            {
                "id": "B",
                "text": "Access control matrix"
            },
            {
                "id": "C",
                "text": "Security clearance"
            },
            {
                "id": "D",
                "text": "Biometric template"
            }
        ],
        "correct": [
            "A"
        ],
        "explanation": {
            "correct": "An access control list (ACL) is attached to a resource and specifies which subjects have which permissions on it.",
            "distractors": {
                "B": "An access control matrix is the whole subject-by-object table; an ACL is one resource's column/list.",
                "C": "A security clearance is a label granted to a subject, not a per-resource permission list.",
                "D": "A biometric template is stored authentication data, not a resource's permission list."
            },
            "exam_pattern": "Per-resource list of who can do what = access control list (ACL)."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 3 - Logical access controls (ACL)"
        ]
    },
    {
        "id": "isc2cc-acc-r2-014",
        "exam": "isc2cc",
        "domain": "cc_access_controls",
        "subtopic": "cc_logical_access",
        "difficulty": 3,
        "type": "mcq",
        "stem": "Access decisions are made by system-wide rules applied uniformly to everyone - for example, 'no one may log in between midnight and 5 a.m.' or firewall rules that filter by port. This is:",
        "options": [
            {
                "id": "A",
                "text": "Role-Based Access Control (RBAC)"
            },
            {
                "id": "B",
                "text": "Rule-Based Access Control"
            },
            {
                "id": "C",
                "text": "Discretionary Access Control (DAC)"
            },
            {
                "id": "D",
                "text": "Need to know"
            }
        ],
        "correct": [
            "B"
        ],
        "explanation": {
            "correct": "Rule-based access control applies uniform, system-enforced rules (such as time-of-day restrictions or firewall filters) to all subjects alike.",
            "distractors": {
                "A": "RBAC ties access to a user's job role, not to uniform global rules applied to everyone.",
                "C": "DAC lets the resource owner decide access case by case, not system-wide rules.",
                "D": "Need to know restricts access to specific information, not via global rules."
            },
            "exam_pattern": "Uniform global rules (time-of-day, firewall) = rule-based; by job role = role-based (RBAC)."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 3 - Logical access controls (rule-based)"
        ]
    },
    {
        "id": "isc2cc-acc-r2-015",
        "exam": "isc2cc",
        "domain": "cc_access_controls",
        "subtopic": "cc_logical_access",
        "difficulty": 3,
        "type": "mcq",
        "stem": "A recognized weakness of Discretionary Access Control (DAC) is that:",
        "options": [
            {
                "id": "A",
                "text": "access depends on each owner's judgment, so a careless owner - or malware running with the owner's rights - can grant access too broadly"
            },
            {
                "id": "B",
                "text": "the system enforces fixed labels the user cannot change"
            },
            {
                "id": "C",
                "text": "permissions are tied rigidly to predefined job roles"
            },
            {
                "id": "D",
                "text": "no authentication is required at all"
            }
        ],
        "correct": [
            "A"
        ],
        "explanation": {
            "correct": "Because DAC leaves access to each owner's discretion, a careless owner or malware acting with the owner's privileges can over-share resources - a key DAC weakness.",
            "distractors": {
                "B": "System-enforced fixed labels the user cannot change describe MAC, not DAC.",
                "C": "Permissions tied to predefined job roles describe RBAC, not DAC.",
                "D": "DAC still requires authentication; access control always verifies identity first."
            },
            "exam_pattern": "DAC = owner decides, so its risk is over-sharing by owners/malware with the owner's rights."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 3 - Logical access controls (DAC)"
        ]
    },
    {
        "id": "isc2cc-acc-r2-016",
        "exam": "isc2cc",
        "domain": "cc_access_controls",
        "subtopic": "cc_logical_access",
        "difficulty": 2,
        "type": "mcq",
        "stem": "A user logs in once in the morning and then reaches email, the HR portal, and the file share without re-entering credentials. This convenience is provided by:",
        "options": [
            {
                "id": "A",
                "text": "Single sign-on (SSO)"
            },
            {
                "id": "B",
                "text": "Multifactor authentication"
            },
            {
                "id": "C",
                "text": "Mandatory Access Control"
            },
            {
                "id": "D",
                "text": "A password manager"
            }
        ],
        "correct": [
            "A"
        ],
        "explanation": {
            "correct": "Single sign-on lets a user authenticate once and gain access to multiple systems through one trusted session, without logging in again to each.",
            "distractors": {
                "B": "Multifactor authentication adds verification factors; it does not reduce how many times you log in.",
                "C": "Mandatory Access Control enforces labels/clearances; it is not a single-login convenience.",
                "D": "A password manager stores and fills individual passwords, but each application still authenticates you separately."
            },
            "exam_pattern": "Authenticate once, reach many systems = single sign-on (SSO)."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 3 - Logical access controls (SSO)"
        ]
    },
    {
        "id": "isc2cc-acc-r2-017",
        "exam": "isc2cc",
        "domain": "cc_access_controls",
        "subtopic": "cc_logical_access",
        "difficulty": 1,
        "type": "mcq",
        "stem": "Which of the following is a LOGICAL (technical) access control rather than a physical one?",
        "options": [
            {
                "id": "A",
                "text": "A username-and-password login on a workstation"
            },
            {
                "id": "B",
                "text": "A door lock"
            },
            {
                "id": "C",
                "text": "A security guard"
            },
            {
                "id": "D",
                "text": "A perimeter fence"
            }
        ],
        "correct": [
            "A"
        ],
        "explanation": {
            "correct": "A username-and-password login is enforced in software, making it a logical (technical) access control.",
            "distractors": {
                "B": "A door lock is a tangible barrier - a physical control.",
                "C": "A security guard is a person providing physical protection - a physical control.",
                "D": "A perimeter fence is a physical barrier, not a software-enforced control."
            },
            "exam_pattern": "Enforced in software (logins, permissions, encryption) = logical; barriers/guards = physical."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 3 - Logical access controls (logical vs. physical)"
        ]
    },
    {
        "id": "isc2cc-acc-r2-018",
        "exam": "isc2cc",
        "domain": "cc_access_controls",
        "subtopic": "cc_logical_access",
        "difficulty": 3,
        "type": "mcq",
        "stem": "A table whose rows are subjects (users) and columns are objects (resources), with each cell listing that user's permissions on that resource, is called an access control:",
        "options": [
            {
                "id": "A",
                "text": "Matrix"
            },
            {
                "id": "B",
                "text": "Vestibule"
            },
            {
                "id": "C",
                "text": "Honeypot"
            },
            {
                "id": "D",
                "text": "Baseline"
            }
        ],
        "correct": [
            "A"
        ],
        "explanation": {
            "correct": "An access control matrix is a table mapping each subject (row) to each object (column), with the cell holding that subject's rights to that object.",
            "distractors": {
                "B": "An access control vestibule is a physical two-door entry booth, not a permissions table.",
                "C": "A honeypot is a decoy system used to lure attackers, not an access-rights table.",
                "D": "A baseline is a minimum security configuration, not a subject-by-object rights table."
            },
            "exam_pattern": "Subjects x objects rights table = access control matrix (a single row/column = a capability list / ACL)."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 3 - Logical access controls (access control matrix)"
        ]
    },

    # ----- cc_identity_management ----------------------------------------
    {
        "id": "isc2cc-acc-r2-019",
        "exam": "isc2cc",
        "domain": "cc_access_controls",
        "subtopic": "cc_identity_management",
        "difficulty": 1,
        "type": "mcq",
        "stem": "A user authenticates with a password and, separately, a PIN. Both of these belong to which authentication factor category?",
        "options": [
            {
                "id": "A",
                "text": "Something you have"
            },
            {
                "id": "B",
                "text": "Something you are"
            },
            {
                "id": "C",
                "text": "Something you know"
            },
            {
                "id": "D",
                "text": "Somewhere you are"
            }
        ],
        "correct": [
            "C"
        ],
        "explanation": {
            "correct": "Passwords and PINs are knowledge-based secrets, so both fall in the 'something you know' factor category.",
            "distractors": {
                "A": "'Something you have' is a physical possession such as a token or smart card, not a secret you recall.",
                "B": "'Something you are' is a biometric trait like a fingerprint, not a password or PIN.",
                "D": "'Somewhere you are' is a location-based factor, not a memorized secret."
            },
            "exam_pattern": "Password/PIN/passphrase = something you know; a password plus a PIN is still one factor type."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 3 - Identity management (authentication factors)"
        ]
    },
    {
        "id": "isc2cc-acc-r2-020",
        "exam": "isc2cc",
        "domain": "cc_access_controls",
        "subtopic": "cc_identity_management",
        "difficulty": 1,
        "type": "mcq",
        "stem": "A phone unlocks by scanning the owner's face. Which authentication factor category is a facial scan?",
        "options": [
            {
                "id": "A",
                "text": "Something you know"
            },
            {
                "id": "B",
                "text": "Something you have"
            },
            {
                "id": "C",
                "text": "Something you are"
            },
            {
                "id": "D",
                "text": "Somewhere you are"
            }
        ],
        "correct": [
            "C"
        ],
        "explanation": {
            "correct": "A facial scan is a biometric measurement of a physical trait, which is the 'something you are' factor.",
            "distractors": {
                "A": "'Something you know' is a secret like a password, not a body trait.",
                "B": "'Something you have' is a possessed object such as a token, not a biometric.",
                "D": "'Somewhere you are' is a location factor, not a biometric trait."
            },
            "exam_pattern": "Fingerprint/face/iris scan = something you are (biometric)."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 3 - Identity management (authentication factors)"
        ]
    },
    {
        "id": "isc2cc-acc-r2-021",
        "exam": "isc2cc",
        "domain": "cc_access_controls",
        "subtopic": "cc_identity_management",
        "difficulty": 2,
        "type": "mcq",
        "stem": "Why should every user have their own unique account instead of sharing a common login?",
        "options": [
            {
                "id": "A",
                "text": "So that actions can be traced to a specific individual (accountability)"
            },
            {
                "id": "B",
                "text": "Because shared logins are easier for everyone to remember"
            },
            {
                "id": "C",
                "text": "To reduce the total number of passwords the company must create"
            },
            {
                "id": "D",
                "text": "Because unique accounts are required before a device can use Wi-Fi"
            }
        ],
        "correct": [
            "A"
        ],
        "explanation": {
            "correct": "Unique accounts let the system attribute each action to one person, which is essential for accountability, auditing, and investigations.",
            "distractors": {
                "B": "Ease of memory is not a security goal; shared logins destroy accountability.",
                "C": "Unique accounts actually mean more credentials, not fewer; the goal is traceability.",
                "D": "Wi-Fi access does not require individual accounts; the reason is accountability."
            },
            "exam_pattern": "Unique IDs (no shared accounts) = actions traceable to a person = accountability."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 3 - Identity management (accountability)"
        ]
    },
    {
        "id": "isc2cc-acc-r2-022",
        "exam": "isc2cc",
        "domain": "cc_access_controls",
        "subtopic": "cc_identity_management",
        "difficulty": 2,
        "type": "mcq",
        "stem": "An employee is terminated on Friday. From a security standpoint, what should happen to their user accounts and access?",
        "options": [
            {
                "id": "A",
                "text": "They should be disabled/revoked immediately (deprovisioned)"
            },
            {
                "id": "B",
                "text": "They should be left active in case the person returns"
            },
            {
                "id": "C",
                "text": "The login should be shared with their replacement"
            },
            {
                "id": "D",
                "text": "They should be removed only at the next annual audit"
            }
        ],
        "correct": [
            "A"
        ],
        "explanation": {
            "correct": "Access should be revoked immediately on termination (prompt deprovisioning) to prevent misuse of a former employee's credentials.",
            "distractors": {
                "B": "Leaving accounts active creates an unmonitored path an ex-employee or attacker could abuse.",
                "C": "Sharing the login destroys accountability and exposes access; the replacement needs their own account.",
                "D": "Waiting until an annual audit leaves the account exploitable for months."
            },
            "exam_pattern": "Disable/revoke access promptly when someone leaves = deprovisioning (offboarding)."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 3 - Identity management (deprovisioning)"
        ]
    },
    {
        "id": "isc2cc-acc-r2-023",
        "exam": "isc2cc",
        "domain": "cc_access_controls",
        "subtopic": "cc_identity_management",
        "difficulty": 2,
        "type": "mcq",
        "stem": "Withdrawing cash at an ATM requires inserting a bank card AND entering a PIN. Why does this qualify as multifactor authentication?",
        "options": [
            {
                "id": "A",
                "text": "It combines something you have (the card) with something you know (the PIN)"
            },
            {
                "id": "B",
                "text": "Because the PIN is a numeric code"
            },
            {
                "id": "C",
                "text": "Because the card is made of plastic"
            },
            {
                "id": "D",
                "text": "Because two different PINs are entered"
            }
        ],
        "correct": [
            "A"
        ],
        "explanation": {
            "correct": "The card is a possession (something you have) and the PIN is a secret (something you know); combining two different factor types makes it multifactor.",
            "distractors": {
                "B": "The PIN being numeric is irrelevant; what matters is combining two different factor types.",
                "C": "The card's material does not make it a factor; it counts as a possession regardless.",
                "D": "Two PINs would both be 'something you know' - the same factor type - which is not multifactor."
            },
            "exam_pattern": "Card + PIN = have + know = two different factor types = MFA."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 3 - Identity management (MFA)"
        ]
    },
    {
        "id": "isc2cc-acc-r2-024",
        "exam": "isc2cc",
        "domain": "cc_access_controls",
        "subtopic": "cc_identity_management",
        "difficulty": 1,
        "type": "fill",
        "stem": "The process of creating a new employee's accounts and granting them the access appropriate to their role when they join is called account ___. (one word)",
        "correct": [
            "provisioning",
            "provision"
        ],
        "explanation": {
            "correct": "Provisioning is creating accounts and granting appropriate access during onboarding; removing that access when the person leaves is deprovisioning.",
            "exam_pattern": "Create accounts/grant access on joining = provisioning; remove on leaving = deprovisioning."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 3 - Identity management (provisioning)"
        ]
    },

    # =====================================================================
    # DOMAIN 4 - NETWORK SECURITY (cc_network_security)
    # =====================================================================

    # ----- cc_network_concepts -------------------------------------------
    {
        "id": "isc2cc-net-r2-001",
        "exam": "isc2cc",
        "domain": "cc_network_security",
        "subtopic": "cc_network_concepts",
        "difficulty": 2,
        "type": "mcq",
        "stem": "A live voice-over-IP call needs low latency and can tolerate a few lost packets, so it avoids the overhead of connection setup and retransmission. Which transport-layer protocol best fits?",
        "options": [
            {
                "id": "A",
                "text": "TCP"
            },
            {
                "id": "B",
                "text": "UDP"
            },
            {
                "id": "C",
                "text": "ARP"
            },
            {
                "id": "D",
                "text": "HTTP"
            }
        ],
        "correct": [
            "B"
        ],
        "explanation": {
            "correct": "UDP is connectionless and has low overhead, trading guaranteed delivery for speed - ideal for real-time traffic like VoIP and streaming.",
            "distractors": {
                "A": "TCP is reliable but adds connection setup and retransmission overhead/latency that real-time media avoids.",
                "C": "ARP resolves IP addresses to MAC addresses on a LAN; it is not a transport protocol for voice.",
                "D": "HTTP is an application-layer protocol, not the transport choice described here."
            },
            "exam_pattern": "Fast, connectionless, tolerant of loss (VoIP/streaming) = UDP; reliable = TCP."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 4 - Network concepts (TCP vs. UDP)"
        ]
    },
    {
        "id": "isc2cc-net-r2-002",
        "exam": "isc2cc",
        "domain": "cc_network_security",
        "subtopic": "cc_network_concepts",
        "difficulty": 1,
        "type": "mcq",
        "stem": "How many bits long is an IPv6 address?",
        "options": [
            {
                "id": "A",
                "text": "32 bits"
            },
            {
                "id": "B",
                "text": "48 bits"
            },
            {
                "id": "C",
                "text": "64 bits"
            },
            {
                "id": "D",
                "text": "128 bits"
            }
        ],
        "correct": [
            "D"
        ],
        "explanation": {
            "correct": "An IPv6 address is 128 bits long, giving a vastly larger address space than IPv4.",
            "distractors": {
                "A": "32 bits is the length of an IPv4 address, not IPv6.",
                "B": "48 bits is the length of a MAC (hardware) address.",
                "C": "64 bits is not the size of a full IPv6 address (it is the typical interface-ID portion only)."
            },
            "exam_pattern": "IPv6 = 128 bits; IPv4 = 32 bits; MAC = 48 bits."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 4 - Network concepts (IPv4/IPv6 addressing)"
        ]
    },
    {
        "id": "isc2cc-net-r2-003",
        "exam": "isc2cc",
        "domain": "cc_network_security",
        "subtopic": "cc_network_concepts",
        "difficulty": 2,
        "type": "mcq",
        "stem": "Which well-known port is used by DNS to resolve domain names to IP addresses?",
        "options": [
            {
                "id": "A",
                "text": "80"
            },
            {
                "id": "B",
                "text": "443"
            },
            {
                "id": "C",
                "text": "53"
            },
            {
                "id": "D",
                "text": "25"
            }
        ],
        "correct": [
            "C"
        ],
        "explanation": {
            "correct": "DNS uses well-known port 53 to handle name-resolution queries and responses.",
            "distractors": {
                "A": "Port 80 is used by unencrypted HTTP web traffic.",
                "B": "Port 443 is used by HTTPS (encrypted web) traffic.",
                "D": "Port 25 is used by SMTP for sending email."
            },
            "exam_pattern": "DNS = 53, HTTP = 80, HTTPS = 443, SMTP = 25, SSH = 22."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 4 - Network concepts (ports/protocols)"
        ]
    },
    {
        "id": "isc2cc-net-r2-004",
        "exam": "isc2cc",
        "domain": "cc_network_security",
        "subtopic": "cc_network_concepts",
        "difficulty": 2,
        "type": "mcq",
        "stem": "An Ethernet switch forwards frames based on MAC (hardware) addresses. At which OSI layer does a traditional switch primarily operate?",
        "options": [
            {
                "id": "A",
                "text": "Layer 1 - Physical"
            },
            {
                "id": "B",
                "text": "Layer 2 - Data Link"
            },
            {
                "id": "C",
                "text": "Layer 3 - Network"
            },
            {
                "id": "D",
                "text": "Layer 4 - Transport"
            }
        ],
        "correct": [
            "B"
        ],
        "explanation": {
            "correct": "A traditional switch operates at Layer 2 (Data Link), forwarding frames based on MAC addresses within a local network.",
            "distractors": {
                "A": "Layer 1 (Physical) deals with cabling and signals, not MAC-based forwarding decisions.",
                "C": "Layer 3 (Network) uses IP addresses for routing between networks - the job of a router.",
                "D": "Layer 4 (Transport) manages end-to-end delivery with TCP/UDP, not frame switching."
            },
            "exam_pattern": "Switch/MAC/frames = Layer 2; router/IP/packets = Layer 3."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 4 - Network concepts (OSI model)"
        ]
    },
    {
        "id": "isc2cc-net-r2-005",
        "exam": "isc2cc",
        "domain": "cc_network_security",
        "subtopic": "cc_network_concepts",
        "difficulty": 1,
        "type": "mcq",
        "stem": "How many layers does the OSI reference model define?",
        "options": [
            {
                "id": "A",
                "text": "Seven"
            },
            {
                "id": "B",
                "text": "Four"
            },
            {
                "id": "C",
                "text": "Five"
            },
            {
                "id": "D",
                "text": "Three"
            }
        ],
        "correct": [
            "A"
        ],
        "explanation": {
            "correct": "The OSI model defines seven layers: Physical, Data Link, Network, Transport, Session, Presentation, and Application.",
            "distractors": {
                "B": "Four layers is the common depiction of the TCP/IP model, not the OSI model.",
                "C": "Five is sometimes used for a simplified TCP/IP stack, not the OSI model.",
                "D": "Three does not match any standard reference model's layer count."
            },
            "exam_pattern": "OSI = 7 layers; TCP/IP model is often shown as 4 layers."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 4 - Network concepts (OSI model)"
        ]
    },
    {
        "id": "isc2cc-net-r2-006",
        "exam": "isc2cc",
        "domain": "cc_network_security",
        "subtopic": "cc_network_concepts",
        "difficulty": 2,
        "type": "mcq",
        "stem": "Which of the following is a PRIVATE IPv4 address - reserved for internal networks and not routable on the public internet?",
        "options": [
            {
                "id": "A",
                "text": "192.168.10.10"
            },
            {
                "id": "B",
                "text": "8.8.8.8"
            },
            {
                "id": "C",
                "text": "72.14.200.5"
            },
            {
                "id": "D",
                "text": "203.0.113.47"
            }
        ],
        "correct": [
            "A"
        ],
        "explanation": {
            "correct": "192.168.0.0-192.168.255.255 is one of the RFC 1918 private ranges reserved for internal use and not routed on the public internet.",
            "distractors": {
                "B": "8.8.8.8 is a well-known public DNS address, routable on the internet.",
                "C": "72.14.200.5 is a public, internet-routable address.",
                "D": "203.0.113.0/24 is a reserved documentation range (RFC 5737, TEST-NET-3), not one of the RFC 1918 private ranges."
            },
            "exam_pattern": "RFC 1918 private ranges: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 4 - Network concepts (IPv4 addressing)"
        ]
    },
    {
        "id": "isc2cc-net-r2-007",
        "exam": "isc2cc",
        "domain": "cc_network_security",
        "subtopic": "cc_network_concepts",
        "difficulty": 1,
        "type": "fill",
        "stem": "The protocol that automatically assigns IP addresses and other network settings to devices when they join a network is abbreviated ___. (acronym)",
        "correct": [
            "DHCP"
        ],
        "explanation": {
            "correct": "DHCP (Dynamic Host Configuration Protocol) automatically assigns IP addresses, subnet masks, gateways, and DNS servers to devices as they connect.",
            "exam_pattern": "Automatic IP assignment = DHCP; name-to-IP resolution = DNS."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 4 - Network concepts (addressing services)"
        ]
    },

    # ----- cc_network_threats_attacks ------------------------------------
    {
        "id": "isc2cc-net-r2-008",
        "exam": "isc2cc",
        "domain": "cc_network_security",
        "subtopic": "cc_network_threats_attacks",
        "difficulty": 2,
        "type": "mcq",
        "stem": "A type of malware attaches itself to a legitimate program or file and runs only when the user opens that host file, then spreads to other files. Which malware is this?",
        "options": [
            {
                "id": "A",
                "text": "Worm"
            },
            {
                "id": "B",
                "text": "Virus"
            },
            {
                "id": "C",
                "text": "Trojan horse"
            },
            {
                "id": "D",
                "text": "Spyware"
            }
        ],
        "correct": [
            "B"
        ],
        "explanation": {
            "correct": "A virus attaches to a host file and typically requires the user to run that file to execute and spread to other files.",
            "distractors": {
                "A": "A worm self-propagates across networks with no host file and no user action.",
                "C": "A Trojan is disguised as legitimate software the user installs; it does not infect host files to spread.",
                "D": "Spyware's defining trait is covert surveillance, not attaching to and infecting host files."
            },
            "exam_pattern": "Needs a host file + user action to run/spread = virus; self-spreads alone = worm."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 4 - Threats/attacks (malware types)"
        ]
    },
    {
        "id": "isc2cc-net-r2-009",
        "exam": "isc2cc",
        "domain": "cc_network_security",
        "subtopic": "cc_network_threats_attacks",
        "difficulty": 2,
        "type": "mcq",
        "stem": "A program advertised as a free game looks harmless, but once the user installs and runs it, it secretly opens a backdoor for an attacker. Which malware type is this?",
        "options": [
            {
                "id": "A",
                "text": "Worm"
            },
            {
                "id": "B",
                "text": "Trojan horse"
            },
            {
                "id": "C",
                "text": "Virus"
            },
            {
                "id": "D",
                "text": "Ransomware"
            }
        ],
        "correct": [
            "B"
        ],
        "explanation": {
            "correct": "A Trojan horse disguises itself as desirable, legitimate software; when the user installs it, it performs hidden malicious actions such as opening a backdoor.",
            "distractors": {
                "A": "A worm self-replicates across networks without being disguised as a useful program the user installs.",
                "C": "A virus infects other host files to spread; a Trojan's trick is disguise and user installation.",
                "D": "Ransomware encrypts data and demands payment; the defining trait here is the deceptive disguise."
            },
            "exam_pattern": "Disguised as something useful, user installs it, hidden malicious payload = Trojan."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 4 - Threats/attacks (malware types)"
        ]
    },
    {
        "id": "isc2cc-net-r2-010",
        "exam": "isc2cc",
        "domain": "cc_network_security",
        "subtopic": "cc_network_threats_attacks",
        "difficulty": 2,
        "type": "mcq",
        "stem": "Malware is installed that quietly records a user's keystrokes and browsing habits and sends them to an attacker, without obviously harming the system. This is:",
        "options": [
            {
                "id": "A",
                "text": "Ransomware"
            },
            {
                "id": "B",
                "text": "Spyware"
            },
            {
                "id": "C",
                "text": "A worm"
            },
            {
                "id": "D",
                "text": "Adware"
            }
        ],
        "correct": [
            "B"
        ],
        "explanation": {
            "correct": "Spyware covertly monitors and collects information about a user - keystrokes, browsing, credentials - and reports it to an attacker.",
            "distractors": {
                "A": "Ransomware encrypts data and demands payment; it does not quietly spy.",
                "C": "A worm's defining trait is self-propagation, not covert surveillance.",
                "D": "Adware displays unwanted ads; the defining trait here is secret monitoring and data theft."
            },
            "exam_pattern": "Secretly monitors/collects user activity = spyware (keyloggers are a type)."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 4 - Threats/attacks (malware types)"
        ]
    },
    {
        "id": "isc2cc-net-r2-011",
        "exam": "isc2cc",
        "domain": "cc_network_security",
        "subtopic": "cc_network_threats_attacks",
        "difficulty": 3,
        "type": "mcq",
        "stem": "Instead of a mass email, an attacker sends a specific accounts-payable clerk a personalized message that references a real project and appears to come from a manager, urgently requesting a wire transfer. This targeted attack is:",
        "options": [
            {
                "id": "A",
                "text": "Generic (bulk) phishing"
            },
            {
                "id": "B",
                "text": "Spear phishing"
            },
            {
                "id": "C",
                "text": "A DDoS attack"
            },
            {
                "id": "D",
                "text": "SQL injection"
            }
        ],
        "correct": [
            "B"
        ],
        "explanation": {
            "correct": "Spear phishing is a targeted, personalized phishing attack aimed at a specific individual, using tailored details to appear credible.",
            "distractors": {
                "A": "Generic phishing is untargeted and sent in bulk; this message is customized for one person.",
                "C": "A DDoS floods a service to deny availability; it does not trick an individual via a tailored email.",
                "D": "SQL injection manipulates database queries through input; it is not a deceptive targeted email."
            },
            "exam_pattern": "Targeted, personalized phishing at a specific person = spear phishing; aimed at a top executive = whaling."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 4 - Threats/attacks (phishing)"
        ]
    },
    {
        "id": "isc2cc-net-r2-012",
        "exam": "isc2cc",
        "domain": "cc_network_security",
        "subtopic": "cc_network_threats_attacks",
        "difficulty": 2,
        "type": "mcq",
        "stem": "An attacker's tool rapidly tries millions of password combinations against a login until it finds the one that works. This password attack is called a:",
        "options": [
            {
                "id": "A",
                "text": "Brute-force attack"
            },
            {
                "id": "B",
                "text": "Phishing attack"
            },
            {
                "id": "C",
                "text": "Man-in-the-middle attack"
            },
            {
                "id": "D",
                "text": "Denial-of-service attack"
            }
        ],
        "correct": [
            "A"
        ],
        "explanation": {
            "correct": "A brute-force attack systematically tries many password combinations until the correct one is found; strong passwords and account lockouts defend against it.",
            "distractors": {
                "B": "Phishing tricks a user into revealing credentials; it does not guess them by trial.",
                "C": "A man-in-the-middle attack intercepts communications; it is not password guessing.",
                "D": "A denial-of-service attack disrupts availability; it does not crack a password."
            },
            "exam_pattern": "Trying many password combinations until one works = brute-force attack."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 4 - Threats/attacks (password attacks)"
        ]
    },
    {
        "id": "isc2cc-net-r2-013",
        "exam": "isc2cc",
        "domain": "cc_network_security",
        "subtopic": "cc_network_threats_attacks",
        "difficulty": 1,
        "type": "mcq",
        "stem": "An attacker telephones an employee, pretends to be a trusted executive, and uses urgency and authority to trick the employee into revealing information - exploiting human trust rather than any software flaw. This general category of attack is:",
        "options": [
            {
                "id": "A",
                "text": "A brute-force attack"
            },
            {
                "id": "B",
                "text": "A buffer overflow"
            },
            {
                "id": "C",
                "text": "A worm"
            },
            {
                "id": "D",
                "text": "Social engineering"
            }
        ],
        "correct": [
            "D"
        ],
        "explanation": {
            "correct": "Social engineering manipulates people into divulging information or taking actions, exploiting human trust and psychology rather than technical vulnerabilities.",
            "distractors": {
                "A": "A brute-force attack guesses credentials by trial; it does not manipulate a person.",
                "B": "A buffer overflow exploits a software flaw in memory handling, not human trust.",
                "C": "A worm is self-spreading malware, not the manipulation of a person."
            },
            "exam_pattern": "Manipulating people (not software) to divulge info or act = social engineering."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 4 - Threats/attacks (social engineering)"
        ]
    },
    {
        "id": "isc2cc-net-r2-014",
        "exam": "isc2cc",
        "domain": "cc_network_security",
        "subtopic": "cc_network_threats_attacks",
        "difficulty": 2,
        "type": "mcq",
        "stem": "A trusted employee with legitimate access deliberately copies confidential customer data to sell it to a competitor. This is an example of a(n):",
        "options": [
            {
                "id": "A",
                "text": "External hacker"
            },
            {
                "id": "B",
                "text": "Insider threat"
            },
            {
                "id": "C",
                "text": "DDoS attack"
            },
            {
                "id": "D",
                "text": "Phishing victim"
            }
        ],
        "correct": [
            "B"
        ],
        "explanation": {
            "correct": "An insider threat is posed by someone with legitimate access - such as an employee - who misuses that access to harm the organization.",
            "distractors": {
                "A": "An external hacker lacks authorized access; the actor here is a trusted insider.",
                "C": "A DDoS attack floods a service for availability; it is not data theft by a trusted person.",
                "D": "A phishing victim is deceived into acting; here the employee is the deliberate wrongdoer."
            },
            "exam_pattern": "A trusted person misusing legitimate access = insider threat."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 4 - Threats/attacks (insider threat)"
        ]
    },

    # ----- cc_network_defense --------------------------------------------
    {
        "id": "isc2cc-net-r2-015",
        "exam": "isc2cc",
        "domain": "cc_network_security",
        "subtopic": "cc_network_defense",
        "difficulty": 2,
        "type": "mcq",
        "stem": "A security appliance passively monitors network traffic and raises an alert when it detects suspicious patterns, but it does NOT block the traffic itself. This device is a(n):",
        "options": [
            {
                "id": "A",
                "text": "Intrusion Prevention System (IPS)"
            },
            {
                "id": "B",
                "text": "Router"
            },
            {
                "id": "C",
                "text": "Load balancer"
            },
            {
                "id": "D",
                "text": "Intrusion Detection System (IDS)"
            }
        ],
        "correct": [
            "D"
        ],
        "explanation": {
            "correct": "An IDS monitors traffic and alerts on suspicious activity but does not block it; responding to the alert is left to staff or other controls.",
            "distractors": {
                "A": "An IPS sits inline and actively blocks malicious traffic - more than the monitor-and-alert role described.",
                "B": "A router forwards packets between networks; it is not a dedicated detection/alerting sensor.",
                "C": "A load balancer distributes traffic for performance; it does not detect intrusions."
            },
            "exam_pattern": "Monitors and only alerts = IDS; sits inline and blocks = IPS."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 4 - Network defense (IDS vs. IPS)"
        ]
    },
    {
        "id": "isc2cc-net-r2-016",
        "exam": "isc2cc",
        "domain": "cc_network_security",
        "subtopic": "cc_network_defense",
        "difficulty": 1,
        "type": "mcq",
        "stem": "Which host-based control is designed to detect, quarantine, and remove viruses, Trojans, and other malicious software on a computer?",
        "options": [
            {
                "id": "A",
                "text": "A VPN"
            },
            {
                "id": "B",
                "text": "A load balancer"
            },
            {
                "id": "C",
                "text": "DNS"
            },
            {
                "id": "D",
                "text": "Antivirus / anti-malware software"
            }
        ],
        "correct": [
            "D"
        ],
        "explanation": {
            "correct": "Antivirus/anti-malware software scans a host to detect, quarantine, and remove malicious programs, often using signatures and behavior analysis.",
            "distractors": {
                "A": "A VPN encrypts remote traffic; it does not scan a host for malware.",
                "B": "A load balancer distributes traffic for performance/availability, not malware removal.",
                "C": "DNS resolves names to IP addresses; it has no malware-removal function."
            },
            "exam_pattern": "Detect/quarantine/remove malware on a host = antivirus / anti-malware."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 4 - Network defense (endpoint protection)"
        ]
    },
    {
        "id": "isc2cc-net-r2-017",
        "exam": "isc2cc",
        "domain": "cc_network_security",
        "subtopic": "cc_network_defense",
        "difficulty": 2,
        "type": "mcq",
        "stem": "When securing a modern wireless network, which encryption standard should be used instead of the long-broken, insecure WEP?",
        "options": [
            {
                "id": "A",
                "text": "WEP with a longer key"
            },
            {
                "id": "B",
                "text": "An open (no-encryption) network"
            },
            {
                "id": "C",
                "text": "MAC-address filtering alone"
            },
            {
                "id": "D",
                "text": "WPA2 or WPA3"
            }
        ],
        "correct": [
            "D"
        ],
        "explanation": {
            "correct": "WPA2 and WPA3 provide strong, modern Wi-Fi encryption and should replace WEP, which is obsolete and easily broken.",
            "distractors": {
                "A": "WEP is fundamentally flawed; a longer key does not make it secure.",
                "B": "An open network applies no encryption at all, leaving traffic exposed.",
                "C": "MAC filtering is easily spoofed and provides no encryption; it is not a substitute for WPA2/WPA3."
            },
            "exam_pattern": "Use WPA2/WPA3 for Wi-Fi; WEP is obsolete and insecure."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 4 - Network defense (wireless security)"
        ]
    },
    {
        "id": "isc2cc-net-r2-018",
        "exam": "isc2cc",
        "domain": "cc_network_security",
        "subtopic": "cc_network_defense",
        "difficulty": 2,
        "type": "mcq",
        "stem": "An intermediary server sits between internal users and the internet, forwarding their web requests, caching content, and able to filter or log the sites they visit while hiding internal IP addresses. This is a:",
        "options": [
            {
                "id": "A",
                "text": "DHCP server"
            },
            {
                "id": "B",
                "text": "Honeypot"
            },
            {
                "id": "C",
                "text": "Network hub"
            },
            {
                "id": "D",
                "text": "Proxy server"
            }
        ],
        "correct": [
            "D"
        ],
        "explanation": {
            "correct": "A proxy server forwards user requests on their behalf, can filter and log web access, and hides internal client addresses behind it.",
            "distractors": {
                "A": "A DHCP server assigns IP addresses; it does not broker and filter web requests.",
                "B": "A honeypot is a decoy to lure attackers, not an intermediary for users' web traffic.",
                "C": "A hub simply repeats traffic to all ports; it does not forward or filter web requests."
            },
            "exam_pattern": "Intermediary that forwards/filters user web requests and hides clients = proxy server."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 4 - Network defense (proxy)"
        ]
    },
    {
        "id": "isc2cc-net-r2-019",
        "exam": "isc2cc",
        "domain": "cc_network_security",
        "subtopic": "cc_network_defense",
        "difficulty": 3,
        "type": "mcq",
        "stem": "A security team deploys a deliberately vulnerable-looking decoy system that holds no real data, purely to attract attackers, waste their time, and study their techniques. This decoy is a:",
        "options": [
            {
                "id": "A",
                "text": "Firewall"
            },
            {
                "id": "B",
                "text": "DMZ"
            },
            {
                "id": "C",
                "text": "VPN gateway"
            },
            {
                "id": "D",
                "text": "Honeypot"
            }
        ],
        "correct": [
            "D"
        ],
        "explanation": {
            "correct": "A honeypot is an intentionally enticing decoy system used to attract and observe attackers and divert them from real assets.",
            "distractors": {
                "A": "A firewall filters traffic by rules; it is not a decoy designed to be attacked.",
                "B": "A DMZ hosts real public-facing services in an isolated segment, not a fake decoy.",
                "C": "A VPN gateway terminates encrypted tunnels; it is not a decoy system."
            },
            "exam_pattern": "Decoy system built to lure and study attackers = honeypot."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 4 - Network defense (honeypot)"
        ]
    },
    {
        "id": "isc2cc-net-r2-020",
        "exam": "isc2cc",
        "domain": "cc_network_security",
        "subtopic": "cc_network_defense",
        "difficulty": 2,
        "type": "mcq",
        "stem": "To tightly control what runs on company workstations, administrators configure them so that ONLY a pre-approved set of applications may execute and everything else is blocked by default. This approach is called:",
        "options": [
            {
                "id": "A",
                "text": "Denylisting (blacklisting)"
            },
            {
                "id": "B",
                "text": "Patching"
            },
            {
                "id": "C",
                "text": "Encryption"
            },
            {
                "id": "D",
                "text": "Application allowlisting (whitelisting)"
            }
        ],
        "correct": [
            "D"
        ],
        "explanation": {
            "correct": "Allowlisting permits only explicitly approved applications to run and blocks all others by default - a strong default-deny posture for software execution.",
            "distractors": {
                "A": "Denylisting blocks known-bad items and allows everything else - the opposite default.",
                "B": "Patching fixes known vulnerabilities; it does not restrict which apps may run.",
                "C": "Encryption protects data confidentiality; it does not control application execution."
            },
            "exam_pattern": "Permit only approved items, block all else = allowlisting; block known-bad, allow rest = denylisting."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 4 - Network defense (allowlisting)"
        ]
    },
    {
        "id": "isc2cc-net-r2-021",
        "exam": "isc2cc",
        "domain": "cc_network_security",
        "subtopic": "cc_network_defense",
        "difficulty": 2,
        "type": "mcq",
        "stem": "The most extreme way to isolate a highly sensitive system is to keep it physically disconnected from the internet and all untrusted networks. This isolation is known as a(n):",
        "options": [
            {
                "id": "A",
                "text": "VPN tunnel"
            },
            {
                "id": "B",
                "text": "DMZ"
            },
            {
                "id": "C",
                "text": "Single sign-on"
            },
            {
                "id": "D",
                "text": "Air gap"
            }
        ],
        "correct": [
            "D"
        ],
        "explanation": {
            "correct": "An air gap physically isolates a system from untrusted networks, so there is no network path an attacker can traverse to reach it.",
            "distractors": {
                "A": "A VPN tunnel connects a device over the internet - the opposite of physical isolation.",
                "B": "A DMZ is an isolated segment that is still network-connected to host public services.",
                "C": "Single sign-on is an authentication convenience, not network isolation."
            },
            "exam_pattern": "Physically disconnected from all untrusted networks = air gap (strongest isolation)."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 4 - Network defense (segmentation/isolation)"
        ]
    },

    # ----- cc_secure_infrastructure --------------------------------------
    {
        "id": "isc2cc-net-r2-022",
        "exam": "isc2cc",
        "domain": "cc_network_security",
        "subtopic": "cc_secure_infrastructure",
        "difficulty": 2,
        "type": "mcq",
        "stem": "A cloud provider rents out virtual machines, storage, and networking, and the customer installs and manages the operating systems and applications on top. Which cloud service model is this?",
        "options": [
            {
                "id": "A",
                "text": "Software as a Service (SaaS)"
            },
            {
                "id": "B",
                "text": "Platform as a Service (PaaS)"
            },
            {
                "id": "C",
                "text": "Infrastructure as a Service (IaaS)"
            },
            {
                "id": "D",
                "text": "On-premises hosting"
            }
        ],
        "correct": [
            "C"
        ],
        "explanation": {
            "correct": "IaaS provides raw infrastructure - VMs, storage, networking - while the customer manages the operating systems and applications running on it.",
            "distractors": {
                "A": "SaaS delivers a finished, provider-managed application; the customer does not manage the OS.",
                "B": "PaaS provides a managed platform for deploying code, without the customer managing VMs/OS.",
                "D": "On-premises hosting means the customer owns and runs the hardware itself, not rented cloud infrastructure."
            },
            "exam_pattern": "Rent raw VMs/storage/network, customer manages OS/apps = IaaS."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 4 - Secure infrastructure (cloud service models)"
        ]
    },
    {
        "id": "isc2cc-net-r2-023",
        "exam": "isc2cc",
        "domain": "cc_network_security",
        "subtopic": "cc_secure_infrastructure",
        "difficulty": 2,
        "type": "mcq",
        "stem": "A cloud provider supplies a managed platform - operating system, runtime, and tools - so developers can deploy their own application code without managing the underlying servers. This model is:",
        "options": [
            {
                "id": "A",
                "text": "Infrastructure as a Service (IaaS)"
            },
            {
                "id": "B",
                "text": "Software as a Service (SaaS)"
            },
            {
                "id": "C",
                "text": "Colocation"
            },
            {
                "id": "D",
                "text": "Platform as a Service (PaaS)"
            }
        ],
        "correct": [
            "D"
        ],
        "explanation": {
            "correct": "PaaS provides a managed platform (OS, runtime, tools) on which developers deploy their own applications, without managing the underlying servers.",
            "distractors": {
                "A": "IaaS provides raw infrastructure the customer must configure and manage (OS included).",
                "B": "SaaS delivers a finished application to end users, not a platform for deploying code.",
                "C": "Colocation is renting data-center space for your own hardware, not a managed cloud platform."
            },
            "exam_pattern": "Managed platform for developers to deploy code = PaaS."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 4 - Secure infrastructure (cloud service models)"
        ]
    },
    {
        "id": "isc2cc-net-r2-024",
        "exam": "isc2cc",
        "domain": "cc_network_security",
        "subtopic": "cc_secure_infrastructure",
        "difficulty": 2,
        "type": "mcq",
        "stem": "A single organization uses cloud infrastructure dedicated exclusively to itself - not shared with other tenants - to gain greater control over security and compliance. This deployment model is a:",
        "options": [
            {
                "id": "A",
                "text": "Public cloud"
            },
            {
                "id": "B",
                "text": "Hybrid cloud"
            },
            {
                "id": "C",
                "text": "Community cloud"
            },
            {
                "id": "D",
                "text": "Private cloud"
            }
        ],
        "correct": [
            "D"
        ],
        "explanation": {
            "correct": "A private cloud is dedicated to one organization, giving it more control over security, compliance, and configuration than a shared environment.",
            "distractors": {
                "A": "A public cloud is shared, multi-tenant infrastructure open to many customers.",
                "B": "A hybrid cloud combines public and private; the scenario describes a single dedicated environment.",
                "C": "A community cloud is shared among several organizations with common needs, not one exclusive tenant."
            },
            "exam_pattern": "Cloud dedicated to one organization only = private cloud."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 4 - Secure infrastructure (cloud deployment models)"
        ]
    },
    {
        "id": "isc2cc-net-r2-025",
        "exam": "isc2cc",
        "domain": "cc_network_security",
        "subtopic": "cc_secure_infrastructure",
        "difficulty": 2,
        "type": "mcq",
        "stem": "Internet-connected devices such as smart cameras, thermostats, and sensors (IoT) are often a security concern mainly because they:",
        "options": [
            {
                "id": "A",
                "text": "Are always fully encrypted and patched by default"
            },
            {
                "id": "B",
                "text": "Cannot be connected to a network at all"
            },
            {
                "id": "C",
                "text": "Are completely immune to malware"
            },
            {
                "id": "D",
                "text": "Frequently ship with weak or default credentials and are rarely patched, expanding the attack surface"
            }
        ],
        "correct": [
            "D"
        ],
        "explanation": {
            "correct": "Many IoT devices ship with weak or default credentials, limited security features, and infrequent patching, which enlarges the organization's attack surface.",
            "distractors": {
                "A": "IoT devices are often NOT well-secured by default; that is precisely the concern.",
                "B": "IoT devices are network-connected by definition; that connectivity is part of the risk.",
                "C": "IoT devices can absolutely be compromised by malware (e.g., botnets), not immune."
            },
            "exam_pattern": "IoT risk = weak default credentials, infrequent patching, larger attack surface."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 4 - Secure infrastructure (IoT basics)"
        ]
    },
    {
        "id": "isc2cc-net-r2-026",
        "exam": "isc2cc",
        "domain": "cc_network_security",
        "subtopic": "cc_secure_infrastructure",
        "difficulty": 2,
        "type": "mcq",
        "stem": "To keep critical servers running through a brief power outage until a generator starts or power returns, a data center relies on a(n):",
        "options": [
            {
                "id": "A",
                "text": "HVAC system"
            },
            {
                "id": "B",
                "text": "Firewall"
            },
            {
                "id": "C",
                "text": "RAID array"
            },
            {
                "id": "D",
                "text": "Uninterruptible Power Supply (UPS)"
            }
        ],
        "correct": [
            "D"
        ],
        "explanation": {
            "correct": "A UPS provides battery backup that bridges short power interruptions, keeping equipment running and supporting availability until generators or utility power resume.",
            "distractors": {
                "A": "HVAC controls temperature and humidity, not power continuity.",
                "B": "A firewall filters network traffic; it has no role in power backup.",
                "C": "A RAID array provides disk redundancy, not protection against a power outage."
            },
            "exam_pattern": "Battery backup bridging a power gap = UPS (an availability control)."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 4 - Secure infrastructure (data-center power)"
        ]
    },

    # =====================================================================
    # DOMAIN 5 - SECURITY OPERATIONS (cc_security_operations)
    # =====================================================================

    # ----- cc_data_security ----------------------------------------------
    {
        "id": "isc2cc-ops-r2-001",
        "exam": "isc2cc",
        "domain": "cc_security_operations",
        "subtopic": "cc_data_security",
        "difficulty": 1,
        "type": "mcq",
        "stem": "Files stored on a server's hard drive, in a database, or on a backup tape - not currently moving or being processed - are in which data state?",
        "options": [
            {
                "id": "A",
                "text": "Data in transit"
            },
            {
                "id": "B",
                "text": "Data in use"
            },
            {
                "id": "C",
                "text": "Data at rest"
            },
            {
                "id": "D",
                "text": "Data in motion"
            }
        ],
        "correct": [
            "C"
        ],
        "explanation": {
            "correct": "Data at rest is stored data sitting on a disk, database, or backup medium; it is commonly protected with storage (at-rest) encryption.",
            "distractors": {
                "A": "Data in transit is moving across a network, not sitting in storage.",
                "B": "Data in use is loaded in memory and actively processed, not stored at rest.",
                "D": "'Data in motion' is another name for data in transit, not stored data."
            },
            "exam_pattern": "Stored on disk/db/tape = at rest; moving on a network = in transit; being processed = in use."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 5 - Data security (data states)"
        ]
    },
    {
        "id": "isc2cc-ops-r2-002",
        "exam": "isc2cc",
        "domain": "cc_security_operations",
        "subtopic": "cc_data_security",
        "difficulty": 2,
        "type": "mcq",
        "stem": "Data that is currently loaded into a computer's memory and actively being read or processed by an application is in which state?",
        "options": [
            {
                "id": "A",
                "text": "Data at rest"
            },
            {
                "id": "B",
                "text": "Data in transit"
            },
            {
                "id": "C",
                "text": "Data archived"
            },
            {
                "id": "D",
                "text": "Data in use"
            }
        ],
        "correct": [
            "D"
        ],
        "explanation": {
            "correct": "Data in use is data loaded in memory/registers and actively being processed by a running application.",
            "distractors": {
                "A": "Data at rest is stored and idle on disk or other media, not actively processed.",
                "B": "Data in transit is moving across a network, not being processed in memory.",
                "C": "'Archived' is a long-term storage situation (a form of at rest), not active processing."
            },
            "exam_pattern": "Loaded in memory and being processed = data in use."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 5 - Data security (data states)"
        ]
    },
    {
        "id": "isc2cc-ops-r2-003",
        "exam": "isc2cc",
        "domain": "cc_security_operations",
        "subtopic": "cc_data_security",
        "difficulty": 2,
        "type": "mcq",
        "stem": "A company is discarding old hard drives that held sensitive data. Which method most reliably ensures the data cannot be recovered?",
        "options": [
            {
                "id": "A",
                "text": "Deleting the files and emptying the recycle bin"
            },
            {
                "id": "B",
                "text": "A quick reformat of the drive"
            },
            {
                "id": "C",
                "text": "Physical destruction (e.g., shredding or pulverizing the drive)"
            },
            {
                "id": "D",
                "text": "Renaming the files"
            }
        ],
        "correct": [
            "C"
        ],
        "explanation": {
            "correct": "Physically destroying the drive (shredding, pulverizing) makes the data unrecoverable - the most reliable sanitization for media being discarded.",
            "distractors": {
                "A": "Deleting files and emptying the recycle bin leaves the underlying data recoverable with tools.",
                "B": "A quick reformat does not truly erase the data; much can still be recovered.",
                "D": "Renaming files changes only labels; the data content remains fully intact."
            },
            "exam_pattern": "Delete/format = recoverable; physical destruction (or verified wipe/degauss) = unrecoverable."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 5 - Data security (secure destruction)"
        ]
    },
    {
        "id": "isc2cc-ops-r2-004",
        "exam": "isc2cc",
        "domain": "cc_security_operations",
        "subtopic": "cc_data_security",
        "difficulty": 2,
        "type": "mcq",
        "stem": "A system inspects outbound email and USB transfers and blocks files containing credit-card or Social Security numbers from leaving the organization. This control is called:",
        "options": [
            {
                "id": "A",
                "text": "A VPN"
            },
            {
                "id": "B",
                "text": "Antivirus"
            },
            {
                "id": "C",
                "text": "A load balancer"
            },
            {
                "id": "D",
                "text": "Data Loss Prevention (DLP)"
            }
        ],
        "correct": [
            "D"
        ],
        "explanation": {
            "correct": "Data Loss Prevention (DLP) detects and blocks sensitive data from leaving the organization through channels like email, web, and removable media.",
            "distractors": {
                "A": "A VPN encrypts a remote connection; it does not inspect content to prevent data exfiltration.",
                "B": "Antivirus detects malware; it is not designed to recognize and block sensitive-data transfers.",
                "C": "A load balancer distributes traffic for performance; it does not stop data leakage."
            },
            "exam_pattern": "Detect/block sensitive data leaving the org = Data Loss Prevention (DLP)."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 5 - Data security (data handling)"
        ]
    },

    # ----- cc_system_hardening -------------------------------------------
    {
        "id": "isc2cc-ops-r2-005",
        "exam": "isc2cc",
        "domain": "cc_security_operations",
        "subtopic": "cc_system_hardening",
        "difficulty": 2,
        "type": "mcq",
        "stem": "Part of hardening a new server is to turn off every network service and close every port that the server's role does not actually require. The main reason is to:",
        "options": [
            {
                "id": "A",
                "text": "Improve the server's graphics performance"
            },
            {
                "id": "B",
                "text": "Make the server easier to discover from the internet"
            },
            {
                "id": "C",
                "text": "Increase the number of running services"
            },
            {
                "id": "D",
                "text": "Reduce the attack surface by removing unnecessary entry points"
            }
        ],
        "correct": [
            "D"
        ],
        "explanation": {
            "correct": "Disabling unneeded services and closing unused ports removes potential entry points, shrinking the attack surface an adversary could exploit.",
            "distractors": {
                "A": "Hardening is a security measure; it is unrelated to graphics performance.",
                "B": "Making a server easier to discover increases exposure - the opposite of hardening.",
                "C": "More running services means a larger attack surface, which hardening aims to reduce."
            },
            "exam_pattern": "Turn off unneeded services/ports = shrink the attack surface (core hardening)."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 5 - System hardening (attack surface)"
        ]
    },
    {
        "id": "isc2cc-ops-r2-006",
        "exam": "isc2cc",
        "domain": "cc_security_operations",
        "subtopic": "cc_system_hardening",
        "difficulty": 2,
        "type": "mcq",
        "stem": "When hardening a system, what should be done with default, guest, and former-employee accounts that are not needed?",
        "options": [
            {
                "id": "A",
                "text": "Leave them all enabled for convenience"
            },
            {
                "id": "B",
                "text": "Share them among the team"
            },
            {
                "id": "C",
                "text": "Give them administrator rights"
            },
            {
                "id": "D",
                "text": "Disable or remove them so they cannot be used as entry points"
            }
        ],
        "correct": [
            "D"
        ],
        "explanation": {
            "correct": "Unneeded default, guest, and ex-employee accounts should be disabled or removed; unused accounts are common footholds for attackers.",
            "distractors": {
                "A": "Leaving unused accounts enabled leaves extra, often unmonitored, entry points open.",
                "B": "Sharing accounts destroys accountability and widens exposure.",
                "C": "Granting admin rights to unneeded accounts dramatically increases risk."
            },
            "exam_pattern": "Hardening disables/removes unused and default accounts."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 5 - System hardening (account management)"
        ]
    },
    {
        "id": "isc2cc-ops-r2-007",
        "exam": "isc2cc",
        "domain": "cc_security_operations",
        "subtopic": "cc_system_hardening",
        "difficulty": 3,
        "type": "mcq",
        "stem": "Configuring each system to provide only the applications, services, and capabilities required for its specific role - and nothing extra - reflects the principle of:",
        "options": [
            {
                "id": "A",
                "text": "Least privilege"
            },
            {
                "id": "B",
                "text": "Defense in depth"
            },
            {
                "id": "C",
                "text": "Separation of duties"
            },
            {
                "id": "D",
                "text": "Least functionality"
            }
        ],
        "correct": [
            "D"
        ],
        "explanation": {
            "correct": "Least functionality means a system runs only the features and services it needs for its role, reducing the attack surface.",
            "distractors": {
                "A": "Least privilege is about limiting a user/account's access rights, not a system's installed features.",
                "B": "Defense in depth layers multiple controls; it does not specifically mean minimal system features.",
                "C": "Separation of duties splits a task among people; it is unrelated to minimizing a system's capabilities."
            },
            "exam_pattern": "A system runs only what it needs = least functionality; a user gets only the access they need = least privilege."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 5 - System hardening (least functionality)"
        ]
    },
    {
        "id": "isc2cc-ops-r2-008",
        "exam": "isc2cc",
        "domain": "cc_security_operations",
        "subtopic": "cc_system_hardening",
        "difficulty": 2,
        "type": "mcq",
        "stem": "Before rolling out a newly released vendor security patch to all production servers, what is the recommended best practice?",
        "options": [
            {
                "id": "A",
                "text": "Apply it to every production server immediately with no testing"
            },
            {
                "id": "B",
                "text": "Wait a full year before applying any patches"
            },
            {
                "id": "C",
                "text": "Apply it only after the vendor retires the product"
            },
            {
                "id": "D",
                "text": "Test the patch in a non-production (test) environment first to catch problems"
            }
        ],
        "correct": [
            "D"
        ],
        "explanation": {
            "correct": "Patches should be tested in a non-production environment first to catch compatibility or stability problems, then deployed - balancing security with reliability.",
            "distractors": {
                "A": "Applying untested patches straight to production risks outages from unforeseen issues.",
                "B": "Waiting a year leaves known vulnerabilities exposed for far too long.",
                "C": "Waiting until end-of-life means never remediating in time; patches should be applied promptly after testing."
            },
            "exam_pattern": "Test patches in staging, then deploy promptly - security balanced with stability."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 5 - System hardening (patch management)"
        ]
    },

    # ----- cc_security_policies_ops --------------------------------------
    {
        "id": "isc2cc-ops-r2-009",
        "exam": "isc2cc",
        "domain": "cc_security_operations",
        "subtopic": "cc_security_policies_ops",
        "difficulty": 3,
        "type": "mcq",
        "stem": "An IT team maintains a documented, known-good inventory of every system's approved settings and tracks any deviation from it. This discipline is called:",
        "options": [
            {
                "id": "A",
                "text": "Incident response"
            },
            {
                "id": "B",
                "text": "Risk acceptance"
            },
            {
                "id": "C",
                "text": "Configuration management"
            },
            {
                "id": "D",
                "text": "Data classification"
            }
        ],
        "correct": [
            "C"
        ],
        "explanation": {
            "correct": "Configuration management maintains and tracks the known-good configuration baseline of systems, detecting and controlling deviations from it.",
            "distractors": {
                "A": "Incident response handles security incidents after they occur, not routine configuration tracking.",
                "B": "Risk acceptance is a decision to tolerate a risk, not a configuration-tracking discipline.",
                "D": "Data classification labels information by sensitivity; it is unrelated to system configurations."
            },
            "exam_pattern": "Maintain/track the known-good configuration baseline = configuration management; approve/test changes = change management."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 5 - Security operations (configuration management)"
        ]
    },
    {
        "id": "isc2cc-ops-r2-010",
        "exam": "isc2cc",
        "domain": "cc_security_operations",
        "subtopic": "cc_security_policies_ops",
        "difficulty": 2,
        "type": "mcq",
        "stem": "Collecting logs from systems and network devices and regularly reviewing them to spot suspicious activity and support later investigations is the practice of:",
        "options": [
            {
                "id": "A",
                "text": "Encryption"
            },
            {
                "id": "B",
                "text": "Patching"
            },
            {
                "id": "C",
                "text": "Data classification"
            },
            {
                "id": "D",
                "text": "Logging and monitoring"
            }
        ],
        "correct": [
            "D"
        ],
        "explanation": {
            "correct": "Logging and monitoring records events and reviews them to detect anomalies and support investigations and accountability.",
            "distractors": {
                "A": "Encryption protects confidentiality of data; it does not record and review events.",
                "B": "Patching fixes vulnerabilities; it is not the collection and review of logs.",
                "C": "Data classification labels information by sensitivity; it is not event logging."
            },
            "exam_pattern": "Record events + review for anomalies = logging and monitoring (key to detection/accountability)."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 5 - Security operations (logging and monitoring)"
        ]
    },
    {
        "id": "isc2cc-ops-r2-011",
        "exam": "isc2cc",
        "domain": "cc_security_operations",
        "subtopic": "cc_security_policies_ops",
        "difficulty": 1,
        "type": "mcq",
        "stem": "A policy specifies that financial records must be kept for seven years and then securely destroyed. This type of policy is a:",
        "options": [
            {
                "id": "A",
                "text": "Acceptable use policy"
            },
            {
                "id": "B",
                "text": "Password policy"
            },
            {
                "id": "C",
                "text": "Data retention policy"
            },
            {
                "id": "D",
                "text": "Change-management policy"
            }
        ],
        "correct": [
            "C"
        ],
        "explanation": {
            "correct": "A data retention policy defines how long different records must be kept and when they are to be securely disposed of.",
            "distractors": {
                "A": "An acceptable use policy governs how staff may use systems, not record-keeping periods.",
                "B": "A password policy sets credential rules, not how long records are retained.",
                "D": "A change-management policy governs system changes, not data retention schedules."
            },
            "exam_pattern": "How long to keep records and when to destroy them = data retention policy."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 5 - Security operations (policies)"
        ]
    },
    {
        "id": "isc2cc-ops-r2-012",
        "exam": "isc2cc",
        "domain": "cc_security_operations",
        "subtopic": "cc_security_policies_ops",
        "difficulty": 2,
        "type": "mcq",
        "stem": "A policy requires employees to lock their screens and lock away any sensitive documents whenever they leave their desks, so passers-by cannot view confidential information. This is a:",
        "options": [
            {
                "id": "A",
                "text": "Acceptable use policy"
            },
            {
                "id": "B",
                "text": "Incident response policy"
            },
            {
                "id": "C",
                "text": "Data retention policy"
            },
            {
                "id": "D",
                "text": "Clean desk policy"
            }
        ],
        "correct": [
            "D"
        ],
        "explanation": {
            "correct": "A clean desk policy requires staff to secure papers and lock screens when away, protecting the confidentiality of sensitive information.",
            "distractors": {
                "A": "An acceptable use policy defines permitted system use, not desk/document tidiness.",
                "B": "An incident response policy covers handling security incidents, not desk security.",
                "C": "A data retention policy covers how long records are kept, not securing a workspace."
            },
            "exam_pattern": "Secure papers and lock screens when away = clean desk policy (protects confidentiality)."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 5 - Security operations (policies)"
        ]
    },

    # ----- cc_security_awareness -----------------------------------------
    {
        "id": "isc2cc-ops-r2-013",
        "exam": "isc2cc",
        "domain": "cc_security_operations",
        "subtopic": "cc_security_awareness",
        "difficulty": 2,
        "type": "mcq",
        "stem": "An attacker calls the HR department posing as an external auditor and invents a convincing back-story to persuade staff to hand over employee records. Inventing a fabricated scenario or identity to extract information is the social-engineering technique of:",
        "options": [
            {
                "id": "A",
                "text": "Tailgating"
            },
            {
                "id": "B",
                "text": "Brute-forcing"
            },
            {
                "id": "C",
                "text": "Pretexting"
            },
            {
                "id": "D",
                "text": "Patching"
            }
        ],
        "correct": [
            "C"
        ],
        "explanation": {
            "correct": "Pretexting is social engineering in which the attacker invents a believable scenario/identity (the 'pretext') to gain trust and extract information.",
            "distractors": {
                "A": "Tailgating is physically following someone through a secured door, not inventing a story over the phone.",
                "B": "Brute-forcing guesses passwords by trial; it does not manipulate a person with a fabricated story.",
                "D": "Patching is a system-maintenance task, not a social-engineering technique."
            },
            "exam_pattern": "Fabricated scenario/identity to extract info = pretexting."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 5 - Security awareness (social engineering)"
        ]
    },
    {
        "id": "isc2cc-ops-r2-014",
        "exam": "isc2cc",
        "domain": "cc_security_operations",
        "subtopic": "cc_security_awareness",
        "difficulty": 2,
        "type": "mcq",
        "stem": "Attackers scatter USB flash drives labeled 'Payroll 2024' in the company parking lot, hoping a curious employee will plug one into a work computer and run the malware on it. This technique is called:",
        "options": [
            {
                "id": "A",
                "text": "A DDoS attack"
            },
            {
                "id": "B",
                "text": "Configuring a firewall rule"
            },
            {
                "id": "C",
                "text": "War-driving"
            },
            {
                "id": "D",
                "text": "Baiting"
            }
        ],
        "correct": [
            "D"
        ],
        "explanation": {
            "correct": "Baiting lures victims with something tempting - like an intriguingly labeled USB drive - so that curiosity leads them to trigger the attack themselves.",
            "distractors": {
                "A": "A DDoS attack floods a service with traffic; it does not rely on a planted tempting item.",
                "B": "A firewall rule is a defensive configuration, not an attack technique.",
                "C": "War-driving is searching for wireless networks from a vehicle, not leaving infected bait."
            },
            "exam_pattern": "Luring victims with tempting bait (e.g., infected USB drives) = baiting."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 5 - Security awareness (social engineering)"
        ]
    },
    {
        "id": "isc2cc-ops-r2-015",
        "exam": "isc2cc",
        "domain": "cc_security_operations",
        "subtopic": "cc_security_awareness",
        "difficulty": 2,
        "type": "multi",
        "stem": "A security-awareness course teaches employees to spot phishing emails. Which TWO of the following are common red flags of a phishing message? (Choose two.)",
        "options": [
            {
                "id": "A",
                "text": "An urgent threat demanding you act immediately or lose access"
            },
            {
                "id": "B",
                "text": "A sender address that does not match the organization it claims to be from"
            },
            {
                "id": "C",
                "text": "An expected, link-free message from a colleague you know"
            },
            {
                "id": "D",
                "text": "A newsletter you knowingly subscribed to"
            }
        ],
        "correct": [
            "A",
            "B"
        ],
        "explanation": {
            "correct": "Manufactured urgency/threats and a mismatched sender address are classic phishing red flags designed to pressure you and disguise the real source.",
            "distractors": {
                "C": "An expected, link-free message from a known colleague is normal traffic, not a phishing indicator.",
                "D": "A newsletter you deliberately subscribed to is expected mail, not a red flag."
            },
            "exam_pattern": "Phishing red flags: urgency/threats, mismatched sender/domain, unexpected links/attachments, requests for credentials."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 5 - Security awareness (phishing recognition)"
        ]
    },
    {
        "id": "isc2cc-ops-r2-016",
        "exam": "isc2cc",
        "domain": "cc_security_operations",
        "subtopic": "cc_security_awareness",
        "difficulty": 1,
        "type": "mcq",
        "stem": "In a crowded coffee shop, an attacker sitting nearby watches over a victim's shoulder to read the password as they type it. This low-tech technique is called:",
        "options": [
            {
                "id": "A",
                "text": "Phishing"
            },
            {
                "id": "B",
                "text": "Tailgating"
            },
            {
                "id": "C",
                "text": "Shoulder surfing"
            },
            {
                "id": "D",
                "text": "A man-in-the-middle attack"
            }
        ],
        "correct": [
            "C"
        ],
        "explanation": {
            "correct": "Shoulder surfing is directly observing someone as they enter a credential or PIN; a privacy screen and awareness of surroundings help prevent it.",
            "distractors": {
                "A": "Phishing uses deceptive messages, not direct over-the-shoulder observation.",
                "B": "Tailgating is following someone through a secured door, not watching them type.",
                "D": "A man-in-the-middle attack intercepts network traffic electronically, not by eye."
            },
            "exam_pattern": "Directly observing someone enter a credential/PIN = shoulder surfing."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 5 - Security awareness (social engineering)"
        ]
    },

    # ----- cc_encryption_basics ------------------------------------------
    {
        "id": "isc2cc-ops-r2-017",
        "exam": "isc2cc",
        "domain": "cc_security_operations",
        "subtopic": "cc_encryption_basics",
        "difficulty": 2,
        "type": "mcq",
        "stem": "Which of the following is a widely used SYMMETRIC encryption algorithm that uses the same key to encrypt and decrypt?",
        "options": [
            {
                "id": "A",
                "text": "RSA"
            },
            {
                "id": "B",
                "text": "SHA-256"
            },
            {
                "id": "C",
                "text": "Diffie-Hellman"
            },
            {
                "id": "D",
                "text": "AES"
            }
        ],
        "correct": [
            "D"
        ],
        "explanation": {
            "correct": "AES (Advanced Encryption Standard) is a symmetric cipher that uses one shared key to encrypt and decrypt; it is fast and widely used for bulk data.",
            "distractors": {
                "A": "RSA is an asymmetric algorithm using a public/private key pair, not a single shared key.",
                "B": "SHA-256 is a hashing algorithm (one-way), not an encryption algorithm.",
                "C": "Diffie-Hellman is a key-exchange method, not a bulk encryption cipher."
            },
            "exam_pattern": "Same key to encrypt/decrypt, fast, bulk data = symmetric (e.g., AES)."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 5 - Encryption basics (symmetric)"
        ]
    },
    {
        "id": "isc2cc-ops-r2-018",
        "exam": "isc2cc",
        "domain": "cc_security_operations",
        "subtopic": "cc_encryption_basics",
        "difficulty": 2,
        "type": "mcq",
        "stem": "Which algorithm is an ASYMMETRIC (public-key) algorithm that uses a matched public/private key pair?",
        "options": [
            {
                "id": "A",
                "text": "AES"
            },
            {
                "id": "B",
                "text": "DES"
            },
            {
                "id": "C",
                "text": "RSA"
            },
            {
                "id": "D",
                "text": "MD5"
            }
        ],
        "correct": [
            "C"
        ],
        "explanation": {
            "correct": "RSA is an asymmetric (public-key) algorithm that uses a public key and a matching private key for encryption/decryption and digital signatures.",
            "distractors": {
                "A": "AES is a symmetric cipher using a single shared key, not a key pair.",
                "B": "DES is an older symmetric cipher, not an asymmetric one.",
                "D": "MD5 is a hashing algorithm, not an encryption algorithm with a key pair."
            },
            "exam_pattern": "Public/private key pair = asymmetric (e.g., RSA); single shared key = symmetric (e.g., AES)."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 5 - Encryption basics (asymmetric)"
        ]
    },
    {
        "id": "isc2cc-ops-r2-019",
        "exam": "isc2cc",
        "domain": "cc_security_operations",
        "subtopic": "cc_encryption_basics",
        "difficulty": 3,
        "type": "mcq",
        "stem": "A sender creates a digital signature on a document using their private key; recipients verify it with the sender's public key. A valid digital signature primarily assures the recipient of the message's:",
        "options": [
            {
                "id": "A",
                "text": "Confidentiality - the contents are hidden from everyone"
            },
            {
                "id": "B",
                "text": "Faster transmission speed"
            },
            {
                "id": "C",
                "text": "Automatic removal of any viruses"
            },
            {
                "id": "D",
                "text": "Integrity and origin - the sender cannot deny signing it (non-repudiation)"
            }
        ],
        "correct": [
            "D"
        ],
        "explanation": {
            "correct": "A digital signature verifies that the message was not altered (integrity) and came from the holder of the private key (authenticity/non-repudiation).",
            "distractors": {
                "A": "Signing does not hide the content; confidentiality requires encrypting the message, a separate step.",
                "B": "A signature does not speed up transmission; it provides assurance, not performance.",
                "C": "A digital signature does not scan for or remove malware."
            },
            "exam_pattern": "Sign with PRIVATE key, verify with PUBLIC key -> integrity + authenticity + non-repudiation (not secrecy)."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 5 - Encryption basics (digital signatures)"
        ]
    },
    {
        "id": "isc2cc-ops-r2-020",
        "exam": "isc2cc",
        "domain": "cc_security_operations",
        "subtopic": "cc_encryption_basics",
        "difficulty": 1,
        "type": "fill",
        "stem": "In cryptography, the original readable data that is fed into an encryption algorithm (before it becomes unreadable ciphertext) is called ___. (one word)",
        "correct": [
            "plaintext",
            "cleartext"
        ],
        "explanation": {
            "correct": "Plaintext (or cleartext) is the original readable input to encryption; the encrypted, unreadable output is called ciphertext.",
            "exam_pattern": "Readable input = plaintext/cleartext; encrypted output = ciphertext."
        },
        "references": [
            "(ISC)² CC Exam Outline: Domain 5 - Encryption basics (terminology)"
        ]
    },
]
