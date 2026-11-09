"""(ISC)² CISSP pool - Domain 8: Software Development Security.

Original, CBK-aligned practice items for the four Software Development Security
subtopics:
  * cissp_sdlc_security  - shifting security left, SDLC phases (including
                           disposal), threat modeling, and maturity models (BSIMM).
  * cissp_secure_coding  - server-side input validation, parameterized queries,
                           output encoding, and failing securely.
  * cissp_software_vulns - SQL injection, XSS, buffer overflow, CSRF.
  * cissp_devsecops      - embedding security in CI/CD, pipeline scanning, and
                           Infrastructure-as-Code security.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the keyed answer is not positionally biased,
every wrong option carries a distractor note, and each item cites the CISSP CBK
domain it draws on. Items are original and never reproduce real exam questions.
"""

QUESTIONS = [
    # ===== cissp_sdlc_security ==============================================
    {
        "id": "cissp-sw-001", "exam": "cissp", "domain": "cissp_software_dev",
        "subtopic": "cissp_sdlc_security", "difficulty": 2, "type": "mcq",
        "stem": "A project team wants to minimize the cost and effort of fixing security flaws. Where in "
                "the software development lifecycle is it MOST effective to begin incorporating security?",
        "options": [
            {"id": "A", "text": "Only after the application is deployed to production"},
            {"id": "B", "text": "As early as possible - in the requirements and design phases"},
            {"id": "C", "text": "Only during user acceptance testing"},
            {"id": "D", "text": "Only once a breach is discovered"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Building security in from the requirements and design phases ('shift left') is most "
                       "effective because defects found early are far cheaper and easier to fix.",
            "distractors": {
                "A": "Addressing security only after deployment is the most expensive and disruptive point to fix flaws.",
                "C": "Waiting until acceptance testing still leaves design-level flaws costly to remediate.",
                "D": "Reacting only after a breach means the damage has already occurred.",
            },
            "exam_pattern": "'Shift left' - integrate security from requirements/design; early fixes are far cheaper.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 8 - Security in the SDLC"],
    },
    {
        "id": "cissp-sw-002", "exam": "cissp", "domain": "cissp_software_dev",
        "subtopic": "cissp_sdlc_security", "difficulty": 2, "type": "mcq",
        "stem": "At the end of a system's life, the SDLC includes a phase to retire it securely - "
                "sanitizing data, revoking credentials, and archiving records as required. What is this "
                "phase?",
        "options": [
            {"id": "A", "text": "Requirements"},
            {"id": "B", "text": "Development"},
            {"id": "C", "text": "Disposal (decommissioning)"},
            {"id": "D", "text": "Design"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The disposal (decommissioning) phase securely retires a system - sanitizing data, "
                       "revoking access, and preserving records needed for retention.",
            "distractors": {
                "A": "Requirements defines what the system must do at the start of the lifecycle.",
                "B": "Development builds the system; it is not the end-of-life phase.",
                "D": "Design plans the architecture; it is not the retirement phase.",
            },
            "exam_pattern": "Secure end-of-life retirement (data sanitization, credential revocation) = disposal/decommissioning.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 8 - SDLC phases"],
    },
    {
        "id": "cissp-sw-003", "exam": "cissp", "domain": "cissp_software_dev",
        "subtopic": "cissp_sdlc_security", "difficulty": 3, "type": "mcq",
        "stem": "An organization wants to benchmark its software security program by comparing its actual "
                "activities against what many real organizations are observed to do, rather than following "
                "a prescriptive list of required practices. Which model is descriptive and observational "
                "in this way?",
        "options": [
            {"id": "A", "text": "BSIMM (Building Security In Maturity Model)"},
            {"id": "B", "text": "A single penetration test report"},
            {"id": "C", "text": "The OWASP Top 10 list"},
            {"id": "D", "text": "A service-level agreement"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "BSIMM is a descriptive model: it observes and measures the security activities real "
                       "organizations actually perform, serving as a benchmark rather than a prescriptive standard.",
            "distractors": {
                "B": "A single penetration test is a point-in-time assessment, not a maturity benchmark.",
                "C": "The OWASP Top 10 is an awareness list of common risks, not a maturity-benchmarking model.",
                "D": "An SLA defines service levels, unrelated to software security maturity.",
            },
            "exam_pattern": "BSIMM = descriptive (what organizations actually do); OWASP SAMM = prescriptive (what to do).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 8 - Software security maturity models"],
    },
    {
        "id": "cissp-sw-004", "exam": "cissp", "domain": "cissp_software_dev",
        "subtopic": "cissp_sdlc_security", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The design-phase activity in which a team systematically identifies, "
                "enumerates, and prioritizes potential threats and attack paths against a system (for "
                "example, using STRIDE) is called threat ________.",
        "correct": ["modeling", "modelling"],
        "explanation": {
            "correct": "Threat modeling proactively identifies and prioritizes threats and attack paths during "
                       "design, before code is written, so mitigations can be built in.",
            "exam_pattern": "Threat modeling (e.g., STRIDE) in the design phase identifies attack paths early.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 8 - Threat modeling"],
    },

    # ===== cissp_secure_coding ==============================================
    {
        "id": "cissp-sw-005", "exam": "cissp", "domain": "cissp_software_dev",
        "subtopic": "cissp_secure_coding", "difficulty": 2, "type": "mcq",
        "stem": "A web application performs input validation only in the browser using JavaScript. Why is "
                "this insufficient, and what is the BEST practice?",
        "options": [
            {"id": "A", "text": "Client-side validation is sufficient as long as the JavaScript is minified"},
            {"id": "B", "text": "Validation should be removed entirely to improve performance"},
            {"id": "C", "text": "Validation should be performed only inside the database"},
            {"id": "D", "text": "Untrusted input must be validated on the server side, because client-side checks can be bypassed"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Client-side checks run in an environment the attacker controls and can be bypassed, so "
                       "untrusted input must always be validated on the server (allowlist validation preferred).",
            "distractors": {
                "A": "Minification does not prevent an attacker from bypassing client-side checks.",
                "B": "Removing validation exposes the application to injection and malformed input.",
                "C": "Database-only checks miss application-layer logic and do not replace server-side validation.",
            },
            "exam_pattern": "Never trust client-side validation alone; always validate untrusted input on the server.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 8 - Input validation"],
    },
    {
        "id": "cissp-sw-006", "exam": "cissp", "domain": "cissp_software_dev",
        "subtopic": "cissp_secure_coding", "difficulty": 2, "type": "mcq",
        "stem": "Which secure-coding practice MOST directly prevents SQL injection by ensuring "
                "user-supplied input is treated strictly as data and never as executable query code?",
        "options": [
            {"id": "A", "text": "Parameterized queries (prepared statements)"},
            {"id": "B", "text": "Increasing the database server's RAM"},
            {"id": "C", "text": "Displaying detailed SQL error messages to users"},
            {"id": "D", "text": "Disabling TLS on the database connection"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Parameterized queries (prepared statements) bind user input as data separate from the "
                       "query structure, so input cannot change the SQL command - the primary defense against injection.",
            "distractors": {
                "B": "More RAM affects performance, not injection resistance.",
                "C": "Detailed SQL error messages aid attackers and are an information-disclosure weakness.",
                "D": "Disabling TLS weakens confidentiality and does nothing against injection.",
            },
            "exam_pattern": "Parameterized queries/prepared statements separate code from data - the primary SQLi defense.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 8 - Preventing injection"],
    },
    {
        "id": "cissp-sw-007", "exam": "cissp", "domain": "cissp_software_dev",
        "subtopic": "cissp_secure_coding", "difficulty": 3, "type": "mcq",
        "stem": "To prevent stored cross-site scripting, a developer must ensure that user-supplied "
                "content is rendered safely in the browser. Which practice MOST directly addresses this?",
        "options": [
            {"id": "A", "text": "Hashing the user's password with SHA-256"},
            {"id": "B", "text": "Output encoding/escaping user-supplied data before it is rendered in the page"},
            {"id": "C", "text": "Enabling a longer session timeout"},
            {"id": "D", "text": "Compressing the HTTP response"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Encoding/escaping untrusted data before rendering ensures the browser treats it as "
                       "text rather than executable script, directly countering XSS (alongside input validation and CSP).",
            "distractors": {
                "A": "Password hashing protects credentials, not against script injection into pages.",
                "C": "Session timeout length does not stop script execution in the page.",
                "D": "Response compression is unrelated to script injection.",
            },
            "exam_pattern": "Encode/escape untrusted output (plus input validation and CSP) to prevent XSS.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 8 - Preventing cross-site scripting"],
    },
    {
        "id": "cissp-sw-008", "exam": "cissp", "domain": "cissp_software_dev",
        "subtopic": "cissp_secure_coding", "difficulty": 2, "type": "mcq",
        "stem": "An application should be designed so that if an unexpected error or a security check "
                "failure occurs, it denies access by default rather than granting it. Which secure-design "
                "principle is this?",
        "options": [
            {"id": "A", "text": "Security through obscurity"},
            {"id": "B", "text": "Open design"},
            {"id": "C", "text": "Fail securely (fail-safe defaults - deny by default)"},
            {"id": "D", "text": "Economy of mechanism"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Failing securely (fail-safe defaults) means that when something goes wrong, the system "
                       "defaults to denying access, so a failure does not expose resources.",
            "distractors": {
                "A": "Security through obscurity relies on secrecy of design and is not a sound default-deny principle.",
                "B": "Open design holds that security should not depend on secrecy - a different principle.",
                "D": "Economy of mechanism favors simple, small designs, not the default-deny behavior described.",
            },
            "exam_pattern": "Fail securely / fail-safe defaults = on error or failure, default to denying access.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 8 - Secure design principles"],
    },

    {
        "id": "cissp-sw-016", "exam": "cissp", "domain": "cissp_software_dev",
        "subtopic": "cissp_secure_coding", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The secure-coding practice of checking that untrusted input conforms "
                "to the expected type, length, format, and range - preferably against an allowlist of "
                "acceptable values - is called input ________.",
        "correct": ["validation"],
        "explanation": {
            "correct": "Input validation verifies that untrusted input matches expectations (ideally via an "
                       "allowlist), a primary defense against injection and malformed-input attacks.",
            "exam_pattern": "Input validation (server-side, allowlist-preferred) is a core defense against "
                            "injection and malformed input.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 8 - Input validation"],
    },

    # ===== cissp_software_vulns =============================================
    {
        "id": "cissp-sw-009", "exam": "cissp", "domain": "cissp_software_dev",
        "subtopic": "cissp_software_vulns", "difficulty": 2, "type": "mcq",
        "stem": "An attacker enters ' OR '1'='1 into a login form and bypasses authentication because "
                "the input is concatenated directly into a database query. Which vulnerability is being "
                "exploited?",
        "options": [
            {"id": "A", "text": "SQL injection"},
            {"id": "B", "text": "Cross-site scripting (XSS)"},
            {"id": "C", "text": "Buffer overflow"},
            {"id": "D", "text": "Clickjacking"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Concatenating untrusted input into a SQL statement lets the attacker alter the query's "
                       "logic - a SQL injection, fixed with parameterized queries.",
            "distractors": {
                "B": "XSS injects scripts into pages viewed by other users, not database query logic.",
                "C": "A buffer overflow overwrites memory, not query logic.",
                "D": "Clickjacking tricks users into clicking disguised UI elements.",
            },
            "exam_pattern": "Untrusted input altering a database query (e.g., ' OR '1'='1) = SQL injection.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 8 - SQL injection"],
    },
    {
        "id": "cissp-sw-010", "exam": "cissp", "domain": "cissp_software_dev",
        "subtopic": "cissp_software_vulns", "difficulty": 3, "type": "mcq",
        "stem": "An attacker stores a malicious script in a forum comment so that it executes in the "
                "browser of every user who later views the comment, stealing their session cookies. Which "
                "vulnerability is this?",
        "options": [
            {"id": "A", "text": "SQL injection"},
            {"id": "B", "text": "A race condition"},
            {"id": "C", "text": "Stored cross-site scripting (XSS)"},
            {"id": "D", "text": "A SYN flood"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A script stored on the server and executed in other users' browsers when they view "
                       "the content is stored (persistent) XSS; mitigate with output encoding and a content "
                       "security policy.",
            "distractors": {
                "A": "SQL injection targets the database, not scripts running in users' browsers.",
                "B": "A race condition exploits timing between operations, not injected scripts.",
                "D": "A SYN flood is a denial-of-service attack, not script injection.",
            },
            "exam_pattern": "Malicious script stored and run in other users' browsers = stored XSS.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 8 - Cross-site scripting"],
    },
    {
        "id": "cissp-sw-011", "exam": "cissp", "domain": "cissp_software_dev",
        "subtopic": "cissp_software_vulns", "difficulty": 2, "type": "mcq",
        "stem": "A C program copies user input into a fixed-size memory buffer without checking the "
                "input's length, letting an attacker overwrite adjacent memory and potentially execute "
                "arbitrary code. Which vulnerability class is this?",
        "options": [
            {"id": "A", "text": "Cross-site request forgery"},
            {"id": "B", "text": "Buffer overflow"},
            {"id": "C", "text": "SQL injection"},
            {"id": "D", "text": "Insecure direct object reference"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Writing past the bounds of a fixed-size buffer is a buffer overflow, which can "
                       "overwrite adjacent memory and lead to code execution; mitigations include bounds "
                       "checking, safe functions, ASLR, and DEP/NX.",
            "distractors": {
                "A": "CSRF abuses an authenticated user's session to submit unwanted requests, not memory overwrites.",
                "C": "SQL injection manipulates database queries, not memory buffers.",
                "D": "An insecure direct object reference exposes objects via predictable identifiers, not buffer overwrites.",
            },
            "exam_pattern": "Writing past a fixed buffer's bounds = buffer overflow; mitigate with bounds checks, ASLR/DEP.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 8 - Buffer overflow"],
    },
    {
        "id": "cissp-sw-012", "exam": "cissp", "domain": "cissp_software_dev",
        "subtopic": "cissp_software_vulns", "difficulty": 3, "type": "mcq",
        "stem": "A logged-in user visits a malicious page that silently causes their browser to submit a "
                "funds-transfer request to their bank using the user's existing authenticated session. "
                "Which attack is this, and which control BEST mitigates it?",
        "options": [
            {"id": "A", "text": "SQL injection; input validation"},
            {"id": "B", "text": "Cross-site scripting; password hashing"},
            {"id": "C", "text": "Buffer overflow; address space layout randomization"},
            {"id": "D", "text": "Cross-site request forgery (CSRF); anti-CSRF tokens (and SameSite cookies)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Forcing an authenticated user's browser to submit an unwanted request is CSRF; "
                       "anti-CSRF tokens (and SameSite cookies) ensure requests originate from the legitimate application.",
            "distractors": {
                "A": "SQL injection targets database queries, not forged authenticated browser requests.",
                "B": "XSS injects scripts and is not mitigated by password hashing.",
                "C": "A buffer overflow corrupts memory and is unrelated to forged browser requests.",
            },
            "exam_pattern": "Forcing an authenticated browser to submit an unwanted request = CSRF; mitigate with "
                            "anti-CSRF tokens and SameSite cookies.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 8 - Cross-site request forgery"],
    },

    # ===== cissp_devsecops ==================================================
    {
        "id": "cissp-sw-013", "exam": "cissp", "domain": "cissp_software_dev",
        "subtopic": "cissp_devsecops", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants to embed automated security testing directly into its continuous "
                "integration/continuous delivery pipeline so that security is addressed throughout "
                "development rather than bolted on at the end. Which approach is this?",
        "options": [
            {"id": "A", "text": "DevSecOps"},
            {"id": "B", "text": "Waterfall development"},
            {"id": "C", "text": "Big-bang integration"},
            {"id": "D", "text": "Ad hoc, undocumented development"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "DevSecOps integrates security practices and automated testing throughout the CI/CD "
                       "pipeline, making security a continuous, shared responsibility rather than a final gate.",
            "distractors": {
                "B": "Waterfall is a sequential methodology and does not describe integrating automated security into CI/CD.",
                "C": "Big-bang integration combines all components at once late in development, opposing continuous security.",
                "D": "Ad hoc development lacks the automation and process that DevSecOps provides.",
            },
            "exam_pattern": "Embedding automated security into CI/CD and shifting left = DevSecOps.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 8 - DevSecOps"],
    },
    {
        "id": "cissp-sw-014", "exam": "cissp", "domain": "cissp_software_dev",
        "subtopic": "cissp_devsecops", "difficulty": 2, "type": "mcq",
        "stem": "In a DevSecOps pipeline, a team automatically scans application source code (SAST), "
                "running builds (DAST), and third-party dependencies before each release. What is the "
                "PRIMARY benefit of automating these checks in the pipeline?",
        "options": [
            {"id": "A", "text": "It eliminates the need for any security policy"},
            {"id": "B", "text": "It catches security issues early and consistently on every build, reducing risk before release"},
            {"id": "C", "text": "It guarantees the software will have zero vulnerabilities"},
            {"id": "D", "text": "It replaces the need for access controls in production"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Automated pipeline scanning runs on every build, catching security issues early and "
                       "consistently so they can be fixed before release - shift-left in practice.",
            "distractors": {
                "A": "Automation supports security policy; it does not replace the need for one.",
                "C": "No tool can guarantee zero vulnerabilities.",
                "D": "Pipeline scanning does not remove the need for production access controls.",
            },
            "exam_pattern": "Automated pipeline scanning (SAST/DAST/SCA) catches issues early and consistently on every build.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 8 - Pipeline security testing"],
    },
    {
        "id": "cissp-sw-015", "exam": "cissp", "domain": "cissp_software_dev",
        "subtopic": "cissp_devsecops", "difficulty": 3, "type": "mcq",
        "stem": "A team defines its infrastructure using version-controlled templates (Infrastructure as "
                "Code) and wants to prevent insecure configurations from ever being deployed. Which "
                "practice BEST achieves this?",
        "options": [
            {"id": "A", "text": "Manually reviewing production servers once a year"},
            {"id": "B", "text": "Granting all developers administrator rights to speed deployment"},
            {"id": "C", "text": "Scanning the Infrastructure-as-Code templates for misconfigurations before deployment (policy as code)"},
            {"id": "D", "text": "Disabling logging in the pipeline to improve speed"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Scanning IaC templates for insecure settings before deployment (policy/security as code) "
                       "stops misconfigurations from reaching production and scales with frequent deployments.",
            "distractors": {
                "A": "An annual manual review cannot keep pace with frequent IaC deployments.",
                "B": "Granting all developers administrator rights violates least privilege and increases risk.",
                "D": "Disabling logging removes the visibility needed to detect and investigate issues.",
            },
            "exam_pattern": "Scan IaC templates (policy/security as code) before deployment to stop insecure configurations early.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 8 - Infrastructure as Code security"],
    },
]
