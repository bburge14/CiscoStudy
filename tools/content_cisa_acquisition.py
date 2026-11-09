"""ISACA CISA pool - Domain 3: IS Acquisition, Development and Implementation.

Original, objective-aligned practice items for the four Domain 3 subtopics
tracked in the study engine:
  * cisa_project_management  - feasibility study, critical path / CPM, PERT
                               three-point estimates, function point analysis,
                               project steering-committee governance.
  * cisa_sdlc                - SDLC phases and the cost of fixing defects, the
                               IS auditor's advisory role across phases, testing
                               types (unit/integration/UAT/regression), user
                               involvement in requirements.
  * cisa_system_migration    - data conversion controls (reconciliation of
                               counts/control totals), changeover strategies
                               (parallel/phased/pilot/direct big-bang), fallback
                               (backout) planning.
  * cisa_post_implementation - post-implementation review objectives, timing,
                               reviewer independence, benefits realization.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so a keyed answer is not positionally biased, every
wrong option carries a distractor note, and each item names the ISACA CISA
Review Manual area it draws on. Items are written from the independent IS
auditor's control-and-risk mindset. All items are ORIGINAL and aligned to public
exam objectives - never real or memorized exam items.
"""

QUESTIONS = [
    # ===== cisa_project_management ==========================================
    {
        "id": "cisa-acq-001", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_project_management", "difficulty": 1, "type": "mcq",
        "stem": "What is the PRIMARY purpose of a feasibility study conducted at the start of a system "
                "development project?",
        "options": [
            {"id": "A", "text": "To write the detailed program code"},
            {"id": "B", "text": "To train end users on the new system"},
            {"id": "C", "text": "To determine whether the proposed solution is viable and worth pursuing"},
            {"id": "D", "text": "To migrate the production data"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A feasibility study evaluates whether the proposed project is technically, economically, "
                       "and operationally viable before significant resources are committed.",
            "distractors": {
                "A": "Coding happens later in the build phase, after the project is approved.",
                "B": "User training occurs near implementation, not during feasibility.",
                "D": "Data migration is an implementation activity, not a feasibility purpose.",
            },
            "exam_pattern": "Feasibility study = is the project viable / worth doing, before committing resources?",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — Feasibility study"],
    },
    {
        "id": "cisa-acq-002", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_project_management", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: In project network scheduling, the longest sequence of dependent "
                "activities, which determines the shortest possible project duration, is called the "
                "______ path.",
        "correct": ["critical", "critical path"],
        "explanation": {
            "correct": "The critical path is the longest path through the activity network; its activities have "
                       "zero slack/float, so any delay to them delays the entire project.",
            "distractors": {},
            "exam_pattern": "Critical path = longest path, zero float; it sets the minimum project duration.",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — Critical path method (CPM)"],
    },
    {
        "id": "cisa-acq-003", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_project_management", "difficulty": 2, "type": "mcq",
        "stem": "Which project estimation technique uses three time estimates - optimistic, most likely, "
                "and pessimistic - to account for uncertainty in activity durations?",
        "options": [
            {"id": "A", "text": "Gantt charting"},
            {"id": "B", "text": "PERT (Program Evaluation and Review Technique)"},
            {"id": "C", "text": "Function point analysis"},
            {"id": "D", "text": "Rapid application development"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "PERT uses three time estimates (optimistic, most likely, pessimistic) per activity to "
                       "model uncertainty and compute an expected duration.",
            "distractors": {
                "A": "A Gantt chart displays a schedule as bars; it does not use three-point estimates.",
                "C": "Function point analysis estimates software size, not activity-duration uncertainty.",
                "D": "RAD is a development approach, not an estimation technique.",
            },
            "exam_pattern": "Three-point (optimistic/likely/pessimistic) duration estimates = PERT.",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — Project scheduling (PERT)"],
    },
    {
        "id": "cisa-acq-004", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_project_management", "difficulty": 3, "type": "mcq",
        "stem": "Which technique estimates the size of a software project based on the functionality "
                "delivered from the user's perspective, independent of the technology used?",
        "options": [
            {"id": "A", "text": "Function point analysis"},
            {"id": "B", "text": "Critical path method"},
            {"id": "C", "text": "Lines-of-code counting after coding"},
            {"id": "D", "text": "Earned value analysis"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Function point analysis sizes software by the functions delivered to the user (inputs, "
                       "outputs, inquiries, files, interfaces), independent of the programming language or platform.",
            "distractors": {
                "B": "The critical path method schedules activities; it does not size software.",
                "C": "Counting lines of code is language-dependent and only possible after coding, unlike up-front function points.",
                "D": "Earned value measures project performance against plan, not functional size.",
            },
            "exam_pattern": "Size by delivered functionality, technology-independent = function points.",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — Software size estimation (function points)"],
    },
    {
        "id": "cisa-acq-005", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_project_management", "difficulty": 3, "type": "multi",
        "stem": "Which TWO are PRIMARY responsibilities of a project steering committee? (Choose two.)",
        "options": [
            {"id": "A", "text": "Approving the project plan, budget, and major changes"},
            {"id": "B", "text": "Writing the application's unit test scripts"},
            {"id": "C", "text": "Reviewing project progress against milestones and resolving escalated issues"},
            {"id": "D", "text": "Performing the daily data entry for the new system"},
        ],
        "correct": ["A", "C"],
        "explanation": {
            "correct": "A steering committee provides project governance - approving plans, budgets, and major "
                       "changes and reviewing progress against milestones while resolving escalated issues.",
            "distractors": {
                "B": "Writing unit tests is a developer/tester task, not a steering-committee responsibility.",
                "D": "Daily data entry is an operational task, not project governance.",
            },
            "exam_pattern": "Steering committee governs the project (approve, monitor, resolve); it does not do the hands-on build work.",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — Project governance and steering committee"],
    },

    # ===== cisa_sdlc ========================================================
    {
        "id": "cisa-acq-006", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_sdlc", "difficulty": 2, "type": "mcq",
        "stem": "In which SDLC phase is it generally LEAST costly to correct an error?",
        "options": [
            {"id": "A", "text": "Implementation"},
            {"id": "B", "text": "Post-implementation / maintenance"},
            {"id": "C", "text": "System testing"},
            {"id": "D", "text": "Requirements and design (the earliest phases)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Defects are cheapest to fix the earlier they are caught; an error in requirements or "
                       "design costs far less to correct than the same error found in testing, implementation, or production.",
            "distractors": {
                "A": "Fixing errors during implementation is more expensive than catching them in requirements/design.",
                "B": "Errors found in production/maintenance are the most expensive to correct.",
                "C": "Errors found in system testing cost more than those caught in requirements/design.",
            },
            "exam_pattern": "Cost to fix a defect rises sharply across the SDLC - cheapest at requirements/design.",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — SDLC phases and defect cost"],
    },
    {
        "id": "cisa-acq-007", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_sdlc", "difficulty": 2, "type": "mcq",
        "stem": "What is the appropriate role of the IS auditor during a system development project?",
        "options": [
            {"id": "A", "text": "To take over project management and make the design decisions"},
            {"id": "B", "text": "To review controls and risks at each phase in an advisory capacity, without assuming management responsibilities"},
            {"id": "C", "text": "To approve the project budget on behalf of the business"},
            {"id": "D", "text": "To write and sign off on the user acceptance test results"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The IS auditor should review the adequacy of controls and risk management at each SDLC "
                       "phase in an advisory, independent capacity - participating without making the management "
                       "decisions that would later impair independence.",
            "distractors": {
                "A": "Taking over project management and design decisions would impair the auditor's independence.",
                "C": "Approving the budget is a management decision, not an audit role.",
                "D": "Performing and signing off on UAT is the users' and management's responsibility.",
            },
            "exam_pattern": "Auditor advises on controls at each phase but never takes management decisions (preserve independence).",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — Auditor's role in the SDLC"],
    },
    {
        "id": "cisa-acq-008", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_sdlc", "difficulty": 1, "type": "mcq",
        "stem": "Which type of testing is performed by end users to confirm that the system meets "
                "business requirements before it goes live?",
        "options": [
            {"id": "A", "text": "Unit testing"},
            {"id": "B", "text": "Integration testing"},
            {"id": "C", "text": "User acceptance testing (UAT)"},
            {"id": "D", "text": "Stress testing"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "User acceptance testing is performed by the end users/business to validate that the "
                       "system satisfies the agreed business requirements before production go-live.",
            "distractors": {
                "A": "Unit testing checks individual program modules, usually by developers.",
                "B": "Integration testing verifies that modules work together, not business acceptance.",
                "D": "Stress testing evaluates performance under extreme load, not business-requirement acceptance.",
            },
            "exam_pattern": "Users confirm business requirements are met = UAT (the final gate before go-live).",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — Testing types (UAT)"],
    },
    {
        "id": "cisa-acq-009", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_sdlc", "difficulty": 2, "type": "mcq",
        "stem": "Which type of testing verifies that recent changes to a system have not adversely "
                "affected existing, previously working functionality?",
        "options": [
            {"id": "A", "text": "Regression testing"},
            {"id": "B", "text": "Unit testing"},
            {"id": "C", "text": "Acceptance testing"},
            {"id": "D", "text": "Penetration testing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Regression testing re-tests existing functionality after a change to confirm that the "
                       "change did not break anything that previously worked.",
            "distractors": {
                "B": "Unit testing validates a single new or changed module in isolation, not the surrounding existing functionality.",
                "C": "Acceptance testing confirms the system meets business requirements, not specifically that changes left prior functions intact.",
                "D": "Penetration testing probes security weaknesses, not functional regressions.",
            },
            "exam_pattern": "Make sure a change didn't break what already worked = regression testing.",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — Testing types (regression)"],
    },
    {
        "id": "cisa-acq-010", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_sdlc", "difficulty": 2, "type": "mcq",
        "stem": "Inadequate involvement of users during the requirements-definition phase MOST likely "
                "results in:",
        "options": [
            {"id": "A", "text": "Lower hardware costs"},
            {"id": "B", "text": "A system that does not meet business needs"},
            {"id": "C", "text": "Faster regulatory approval"},
            {"id": "D", "text": "Stronger database encryption"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "If users are not adequately involved in defining requirements, the delivered system is "
                       "likely to miss the actual business needs, leading to rework, low adoption, or outright failure.",
            "distractors": {
                "A": "User involvement has no direct relationship to lowering hardware cost.",
                "C": "It does not speed regulatory approval.",
                "D": "Encryption strength is a design/security decision unrelated to user involvement in requirements.",
            },
            "exam_pattern": "Weak user involvement in requirements -> a system that fails to meet business needs.",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — Requirements definition and user involvement"],
    },

    # ===== cisa_system_migration ============================================
    {
        "id": "cisa-acq-011", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_system_migration", "difficulty": 2, "type": "mcq",
        "stem": "During a data conversion from a legacy system to a new system, which control BEST "
                "ensures that all data was transferred completely and accurately?",
        "options": [
            {"id": "A", "text": "Encrypting the data while it is in transit"},
            {"id": "B", "text": "Training the users on the new system"},
            {"id": "C", "text": "Reconciling record counts and control totals between the source and target systems"},
            {"id": "D", "text": "Scheduling the conversion for a weekend"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Reconciling record counts and control (hash/financial) totals between the old and new "
                       "systems provides direct evidence that the data was converted completely and accurately.",
            "distractors": {
                "A": "Encryption protects confidentiality in transit but does not prove completeness or accuracy of the conversion.",
                "B": "User training does not verify the conversion.",
                "D": "Timing the cutover reduces disruption but does not confirm data integrity.",
            },
            "exam_pattern": "Prove conversion completeness/accuracy by reconciling record counts and control totals (old vs. new).",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — Data conversion and migration controls"],
    },
    {
        "id": "cisa-acq-012", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_system_migration", "difficulty": 2, "type": "mcq",
        "stem": "Which system conversion (changeover) approach provides the GREATEST assurance by running "
                "the old and new systems simultaneously and comparing their results?",
        "options": [
            {"id": "A", "text": "Parallel changeover"},
            {"id": "B", "text": "Direct (big-bang) changeover"},
            {"id": "C", "text": "Pilot changeover in one location only"},
            {"id": "D", "text": "No changeover plan"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "In a parallel changeover, the old and new systems run together and their outputs are "
                       "compared, so errors in the new system can be caught before the old one is retired - the lowest-risk approach.",
            "distractors": {
                "B": "Direct/big-bang switches everything at once with no fallback, the highest-risk approach.",
                "C": "A pilot limits exposure to one site but does not run both systems in parallel across the organization for comparison.",
                "D": "Having no changeover plan is not a controlled approach at all.",
            },
            "exam_pattern": "Run old + new together and compare = parallel (safest, but costly).",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — Changeover (conversion) strategies"],
    },
    {
        "id": "cisa-acq-013", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_system_migration", "difficulty": 2, "type": "mcq",
        "stem": "An organization plans to retire its old system and switch entirely to the new one on a "
                "single date with no parallel-run fallback. Which conversion approach is this, and what is "
                "its key characteristic?",
        "options": [
            {"id": "A", "text": "Pilot conversion, which limits exposure to one unit"},
            {"id": "B", "text": "Phased conversion, which introduces modules gradually"},
            {"id": "C", "text": "Parallel conversion, which runs both systems together"},
            {"id": "D", "text": "Direct (big-bang) conversion, which carries the highest risk because there is no fallback"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Switching entirely on one date with no parallel run is a direct/big-bang conversion; it "
                       "is the highest-risk approach because there is no fallback if the new system fails.",
            "distractors": {
                "A": "Pilot conversion deploys to one unit first, not the whole organization at once.",
                "B": "Phased conversion introduces the system in increments, not all at once.",
                "C": "Parallel conversion runs both systems together, the opposite of this scenario.",
            },
            "exam_pattern": "One-shot switch, no fallback = direct/big-bang = highest risk.",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — Changeover (conversion) strategies"],
    },
    {
        "id": "cisa-acq-014", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_system_migration", "difficulty": 3, "type": "mcq",
        "stem": "Before a critical system goes live using a direct cutover, what should be the IS "
                "auditor's PRIMARY concern?",
        "options": [
            {"id": "A", "text": "Whether the project finished under budget"},
            {"id": "B", "text": "Whether a tested fallback (backout) plan exists in case the new system fails"},
            {"id": "C", "text": "Whether the vendor's logo appears on the login screen"},
            {"id": "D", "text": "Whether the old system used the same programming language"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "With a direct cutover there is no parallel safety net, so the existence of a tested "
                       "fallback/backout plan is the auditor's primary concern to avoid an unrecoverable failure.",
            "distractors": {
                "A": "Budget performance matters but is secondary to the ability to recover from a failed cutover.",
                "C": "Branding is irrelevant to cutover risk.",
                "D": "The old system's language does not address the risk of a failed go-live.",
            },
            "exam_pattern": "Direct cutover's biggest risk is no fallback - look for a tested backout plan.",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — Fallback and go-live controls"],
    },

    # ===== cisa_post_implementation =========================================
    {
        "id": "cisa-acq-015", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_post_implementation", "difficulty": 2, "type": "mcq",
        "stem": "What is the PRIMARY objective of a post-implementation review (PIR)?",
        "options": [
            {"id": "A", "text": "To write the system's requirements"},
            {"id": "B", "text": "To perform user acceptance testing"},
            {"id": "C", "text": "To determine whether the system met its objectives and delivered the expected benefits, and to capture lessons learned"},
            {"id": "D", "text": "To select the project manager"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A PIR evaluates whether the implemented system achieved its intended objectives and "
                       "business benefits (including ROI) and identifies lessons learned for future projects.",
            "distractors": {
                "A": "Requirements are defined at the start of the project, not reviewed after go-live.",
                "B": "UAT occurs before go-live, not as the purpose of a PIR.",
                "D": "Selecting the project manager happens at project initiation.",
            },
            "exam_pattern": "PIR = did the live system meet its objectives/benefits, and what did we learn?",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — Post-implementation review"],
    },
    {
        "id": "cisa-acq-016", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_post_implementation", "difficulty": 2, "type": "mcq",
        "stem": "When should a post-implementation review normally be conducted?",
        "options": [
            {"id": "A", "text": "Before the requirements are finalized"},
            {"id": "B", "text": "After the system has been in production long enough for its benefits and performance to be assessed"},
            {"id": "C", "text": "During the coding phase"},
            {"id": "D", "text": "Immediately after the feasibility study"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A PIR is conducted after the system has operated in production for a sufficient, "
                       "representative period so that actual benefits, costs, and performance can be meaningfully assessed.",
            "distractors": {
                "A": "There is nothing implemented to review before requirements are finalized.",
                "C": "During coding the system is not yet implemented.",
                "D": "The feasibility study is at project start, long before implementation.",
            },
            "exam_pattern": "Run the PIR once the system has stabilized in production, so real benefits can be measured.",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — Post-implementation review timing"],
    },
    {
        "id": "cisa-acq-017", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_post_implementation", "difficulty": 3, "type": "mcq",
        "stem": "To ensure objectivity, who is BEST positioned to conduct a post-implementation review?",
        "options": [
            {"id": "A", "text": "An independent party not involved in the system's development"},
            {"id": "B", "text": "The lead developer who wrote most of the code"},
            {"id": "C", "text": "The vendor that sold the system"},
            {"id": "D", "text": "The project manager who delivered the project"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An independent reviewer who was not involved in building the system provides the most "
                       "objective assessment of whether objectives and benefits were achieved.",
            "distractors": {
                "B": "The lead developer has a self-review conflict and cannot objectively assess their own work.",
                "C": "The vendor has a commercial interest in a favorable result.",
                "D": "The project manager is invested in the project's apparent success, reducing objectivity.",
            },
            "exam_pattern": "For objectivity, the PIR should be done by someone independent of the development effort.",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — Post-implementation review independence"],
    },
    {
        "id": "cisa-acq-018", "exam": "cisa", "domain": "cisa_acquisition_dev",
        "subtopic": "cisa_post_implementation", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Confirming that a completed project actually delivered the business "
                "benefits promised in its business case is known as benefits ______.",
        "correct": ["realization", "realisation", "benefits realization", "benefits realisation"],
        "explanation": {
            "correct": "Benefits realization compares the actual outcomes against the benefits projected in the "
                       "business case to confirm the investment delivered its expected value.",
            "distractors": {},
            "exam_pattern": "Did we actually get the benefits the business case promised? = benefits realization.",
        },
        "references": ["ISACA CISA Review Manual: Domain 3 — Benefits realization"],
    },
]
