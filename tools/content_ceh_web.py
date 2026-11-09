"""EC-Council CEH v13 pool - Domain 4.0: Web Application Hacking.

Original, objective-aligned practice items for CertLab's CEH track, covering the
three subtopics of the Web Application Hacking domain:
  * ceh_web_servers   - web-server attacks and hardening: directory traversal,
                        Nikto scanning, patch management, default credentials,
                        and information disclosure via the Server header.
  * ceh_web_apps      - OWASP Top 10 themes: cross-site scripting (stored,
                        reflected, DOM), CSRF, broken access control / IDOR, and
                        the intercepting-proxy tooling (Burp Suite, OWASP ZAP).
  * ceh_sql_injection - SQL injection classes (in-band UNION/error, inferential
                        boolean/time-based blind), the sqlmap tool, and the
                        parameterized-query defense.

Authoring rules match the other content_*.py pools: build_content.py shuffles
the A/B/C/D order per item (seeded by id), so the authored key is not
positionally biased, every wrong option carries a distractor note, and each item
names the CEH v13 module it draws on. Scope is CONCEPTUAL, authorized-assessment
exam prep only (recognize the attack, tool, or defense) - no working exploit
code, payloads, or step-by-step attack instructions, and never real or memorized
exam items.
"""

QUESTIONS = [
    # ===== ceh_web_servers ==================================================
    {
        "id": "ceh-web-001", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_web_servers", "difficulty": 1, "type": "mcq",
        "stem": "Which tool is purpose-built to scan web servers for thousands of known dangerous files, "
                "outdated server versions, and common misconfigurations?",
        "options": [
            {"id": "A", "text": "Aircrack-ng"},
            {"id": "B", "text": "John the Ripper"},
            {"id": "C", "text": "Nikto"},
            {"id": "D", "text": "Responder"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Nikto is a web-server scanner that checks for thousands of risky files/CGIs, outdated "
                       "software, and server misconfigurations.",
            "distractors": {
                "A": "Aircrack-ng cracks wireless encryption keys; it does not scan web servers.",
                "B": "John the Ripper is an offline password cracker, not a web-server scanner.",
                "D": "Responder poisons LLMNR/NBT-NS to capture hashes; it is not a web-server scanner.",
            },
            "exam_pattern": "Scan a web server for known bad files/versions/misconfigs = Nikto.",
        },
        "references": ["CEH v13 Module 13: Hacking Web Servers"],
    },
    {
        "id": "ceh-web-002", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_web_servers", "difficulty": 2, "type": "mcq",
        "stem": "By requesting a URL that contains sequences like ../../ an attacker reads files outside the "
                "web root, such as the system password file. Which web-server attack is this?",
        "options": [
            {"id": "A", "text": "Directory (path) traversal"},
            {"id": "B", "text": "SYN flood"},
            {"id": "C", "text": "ARP poisoning"},
            {"id": "D", "text": "Deauthentication attack"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Directory (path) traversal uses ../ sequences to escape the web root and access files the "
                       "server should not expose.",
            "distractors": {
                "B": "A SYN flood is a denial-of-service technique, not file access via path manipulation.",
                "C": "ARP poisoning redirects LAN traffic; it does not read server files via a URL.",
                "D": "A deauthentication attack disconnects Wi-Fi clients; it is unrelated to web paths.",
            },
            "exam_pattern": "../ sequences to escape the web root and read arbitrary files = directory/path traversal.",
        },
        "references": ["CEH v13 Module 13: Hacking Web Servers"],
    },
    {
        "id": "ceh-web-003", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_web_servers", "difficulty": 2, "type": "mcq",
        "stem": "An organization keeps getting compromised through publicly known vulnerabilities in its "
                "outdated web-server software. Which practice most directly addresses this root cause?",
        "options": [
            {"id": "A", "text": "Requiring longer user passwords"},
            {"id": "B", "text": "Disabling ICMP echo"},
            {"id": "C", "text": "Adding more server RAM"},
            {"id": "D", "text": "Timely patch and update management"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Known vulnerabilities in outdated software are closed by applying vendor patches promptly, "
                       "so disciplined patch management is the direct remedy.",
            "distractors": {
                "A": "Longer passwords do not fix a code vulnerability in the server software.",
                "B": "Disabling ICMP neither patches nor mitigates the underlying software flaw.",
                "C": "Adding RAM is a performance measure, not a vulnerability remediation.",
            },
            "exam_pattern": "Repeated compromise via known flaws in old software = fix with patch/update management.",
        },
        "references": ["CEH v13 Module 13: Hacking Web Servers"],
    },
    {
        "id": "ceh-web-004", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_web_servers", "difficulty": 1, "type": "mcq",
        "stem": "During hardening, which misconfiguration should be addressed first because attackers "
                "routinely try it against newly exposed web servers and admin consoles?",
        "options": [
            {"id": "A", "text": "Verbose comments left in HTML"},
            {"id": "B", "text": "Default or unchanged administrative credentials"},
            {"id": "C", "text": "Serving the site over HTTPS"},
            {"id": "D", "text": "Minified JavaScript"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Default/unchanged admin credentials are trivially guessed and widely documented, so they "
                       "are a top-priority hardening fix.",
            "distractors": {
                "A": "HTML comments can leak minor information but are far lower risk than default admin logins.",
                "C": "Serving over HTTPS is a good practice, not a misconfiguration to fix.",
                "D": "Minified JavaScript is a normal optimization, not a security misconfiguration.",
            },
            "exam_pattern": "Change default/admin credentials first - they are attackers' easiest win.",
        },
        "references": ["CEH v13 Module 13: Hacking Web Servers"],
    },
    {
        "id": "ceh-web-005", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_web_servers", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: Configuring a web server to suppress its detailed product and version in "
                "the HTTP Server response ______ reduces the information an attacker gains from banner grabbing.",
        "correct": ["header", "headers"],
        "explanation": {
            "correct": "The Server response header can reveal the exact web-server product and version; "
                       "suppressing or genericizing it limits footprinting (defense in depth, not a fix for any underlying flaw).",
            "distractors": {},
            "exam_pattern": "Hide the web-server version in the Server header to reduce footprinting.",
        },
        "references": ["CEH v13 Module 13: Hacking Web Servers"],
    },

    # ===== ceh_web_apps =====================================================
    {
        "id": "ceh-web-006", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_web_apps", "difficulty": 2, "type": "mcq",
        "stem": "An attacker submits a comment containing a script; every visitor who later views that comment "
                "has the script run in their browser. Which attack and variant is this?",
        "options": [
            {"id": "A", "text": "Stored (persistent) cross-site scripting (XSS)"},
            {"id": "B", "text": "Reflected XSS"},
            {"id": "C", "text": "SQL injection"},
            {"id": "D", "text": "Cross-site request forgery"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The script is saved on the server and served to every viewer, which is stored "
                       "(persistent) XSS.",
            "distractors": {
                "B": "Reflected XSS runs from a crafted request/link and is not stored server-side for all users.",
                "C": "SQL injection targets the database, not script execution in each visitor's browser.",
                "D": "CSRF forces a state-changing action using the victim's session; it does not plant a persistent script.",
            },
            "exam_pattern": "Script saved server-side and served to all viewers = stored XSS; echoed from a request = reflected.",
        },
        "references": ["CEH v13 Module 14: Hacking Web Applications"],
    },
    {
        "id": "ceh-web-007", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_web_apps", "difficulty": 2, "type": "mcq",
        "stem": "A search page echoes the user's query straight back into the HTML. An attacker emails a "
                "crafted link that runs script in the victim's browser only when the victim clicks it. Which variant is this?",
        "options": [
            {"id": "A", "text": "Stored XSS"},
            {"id": "B", "text": "Reflected XSS"},
            {"id": "C", "text": "DOM-based SQL injection"},
            {"id": "D", "text": "Clickjacking"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The payload is reflected back from the request and executes when the victim follows the "
                       "crafted link, which is reflected XSS.",
            "distractors": {
                "A": "Stored XSS persists on the server and affects all viewers, not only one who clicks a link.",
                "C": "'DOM-based SQL injection' is not a real category; it mixes unrelated terms.",
                "D": "Clickjacking tricks a user into clicking a hidden element; it does not echo script from a request.",
            },
            "exam_pattern": "Payload echoed from the request (crafted link) = reflected XSS; persisted server-side = stored.",
        },
        "references": ["CEH v13 Module 14: Hacking Web Applications"],
    },
    {
        "id": "ceh-web-008", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_web_apps", "difficulty": 3, "type": "mcq",
        "stem": "A logged-in user visits a malicious page that silently submits a form to their bank's "
                "'transfer funds' endpoint, abusing the user's existing authenticated session. Which attack is this?",
        "options": [
            {"id": "A", "text": "Reflected XSS"},
            {"id": "B", "text": "Directory traversal"},
            {"id": "C", "text": "Cross-site request forgery (CSRF)"},
            {"id": "D", "text": "Brute-force login"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "CSRF rides the victim's existing authenticated session to force a state-changing request "
                       "the user did not intend; anti-CSRF tokens are the standard defense.",
            "distractors": {
                "A": "Reflected XSS executes script; here the attack forces a request using the user's session.",
                "B": "Directory traversal reads files on the server, not forged user actions.",
                "D": "Brute-force login guesses credentials; the user here is already authenticated.",
            },
            "exam_pattern": "Force a state-changing request using the victim's active session = CSRF (anti-CSRF tokens defend).",
        },
        "references": ["CEH v13 Module 14: Hacking Web Applications"],
    },
    {
        "id": "ceh-web-009", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_web_apps", "difficulty": 1, "type": "mcq",
        "stem": "Which tool acts as an intercepting proxy, letting a tester view and modify HTTP requests "
                "between the browser and a web application?",
        "options": [
            {"id": "A", "text": "Burp Suite"},
            {"id": "B", "text": "Wireshark"},
            {"id": "C", "text": "Nmap"},
            {"id": "D", "text": "Hashcat"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Burp Suite (like OWASP ZAP) sits between the browser and the app as an intercepting proxy, "
                       "so requests and responses can be inspected and tampered with.",
            "distractors": {
                "B": "Wireshark passively captures packets but is not an inline HTTP proxy for editing requests.",
                "C": "Nmap scans ports and services; it is not a web proxy.",
                "D": "Hashcat cracks password hashes; it does not proxy HTTP.",
            },
            "exam_pattern": "Intercept and modify HTTP requests to a web app = Burp Suite (or OWASP ZAP).",
        },
        "references": ["CEH v13 Module 14: Hacking Web Applications"],
    },
    {
        "id": "ceh-web-010", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_web_apps", "difficulty": 2, "type": "mcq",
        "stem": "By changing an 'account_id' value in a URL, a user views another customer's records because "
                "the app never checks ownership. Which OWASP Top 10 category does this fall under?",
        "options": [
            {"id": "A", "text": "Security misconfiguration"},
            {"id": "B", "text": "Cryptographic failures"},
            {"id": "C", "text": "Vulnerable and outdated components"},
            {"id": "D", "text": "Broken access control (IDOR)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Reaching another user's data by tampering with an object reference and no ownership check "
                       "is an insecure direct object reference (IDOR), a form of broken access control.",
            "distractors": {
                "A": "Security misconfiguration is about insecure settings/defaults, not a missing authorization check.",
                "B": "Cryptographic failures involve weak or missing encryption, not access-control gaps.",
                "C": "Vulnerable and outdated components concern unpatched libraries, not this ownership-check flaw.",
            },
            "exam_pattern": "Change an object reference to reach data you shouldn't = IDOR, under broken access control.",
        },
        "references": ["CEH v13 Module 14: Hacking Web Applications"],
    },
    {
        "id": "ceh-web-011", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_web_apps", "difficulty": 1, "type": "mcq",
        "stem": "Which community-maintained awareness document ranks the ten most critical web application "
                "security risks and is widely used to prioritize testing and remediation?",
        "options": [
            {"id": "A", "text": "OWASP Top 10"},
            {"id": "B", "text": "The CVE list"},
            {"id": "C", "text": "NIST SP 800-53 control catalog"},
            {"id": "D", "text": "The CIS cloud benchmark"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The OWASP Top 10 is a community awareness document ranking the ten most critical web "
                       "application security risks, guiding testing priorities.",
            "distractors": {
                "B": "The CVE list enumerates specific disclosed vulnerabilities; it is not a ranked web-risk document.",
                "C": "NIST SP 800-53 is a broad security and privacy control catalog, not a web-app top ten.",
                "D": "CIS benchmarks are configuration baselines, not a ranked list of web application risks.",
            },
            "exam_pattern": "Ten most critical web app risks = OWASP Top 10.",
        },
        "references": ["CEH v13 Module 14: Hacking Web Applications"],
    },

    # ===== ceh_sql_injection ================================================
    {
        "id": "ceh-web-012", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_sql_injection", "difficulty": 1, "type": "mcq",
        "stem": "An attacker enters ' OR '1'='1 into a login field and the application concatenates it "
                "directly into a database query, changing the query's logic. Which vulnerability class is this?",
        "options": [
            {"id": "A", "text": "Cross-site scripting"},
            {"id": "B", "text": "SQL injection"},
            {"id": "C", "text": "Clickjacking"},
            {"id": "D", "text": "Session fixation"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Untrusted input altering the structure of a SQL query is SQL injection, which can bypass "
                       "authentication or expose data.",
            "distractors": {
                "A": "XSS injects script that runs in the browser, not SQL that runs in the database.",
                "C": "Clickjacking overlays UI to hijack clicks; it does not alter database queries.",
                "D": "Session fixation forces a known session ID; it is unrelated to query manipulation.",
            },
            "exam_pattern": "Untrusted input altering a SQL query = SQL injection.",
        },
        "references": ["CEH v13 Module 15: SQL Injection"],
    },
    {
        "id": "ceh-web-013", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_sql_injection", "difficulty": 3, "type": "multi",
        "stem": "Which TWO are forms of SQL injection in which the attacker infers data indirectly rather "
                "than seeing it returned directly in the response? (Choose two.)",
        "options": [
            {"id": "A", "text": "Boolean-based blind SQL injection"},
            {"id": "B", "text": "UNION-based SQL injection"},
            {"id": "C", "text": "Error-based SQL injection"},
            {"id": "D", "text": "Time-based blind SQL injection"},
        ],
        "correct": ["A", "D"],
        "explanation": {
            "correct": "Blind SQL injection infers data indirectly: boolean-based reads true/false differences in "
                       "responses, and time-based reads deliberate response delays.",
            "distractors": {
                "B": "UNION-based injection returns data directly in the application's output (in-band).",
                "C": "Error-based injection reveals data through returned database error messages (in-band).",
            },
            "exam_pattern": "Inferential/blind SQLi = boolean-based and time-based; in-band = UNION-based and error-based.",
        },
        "references": ["CEH v13 Module 15: SQL Injection"],
    },
    {
        "id": "ceh-web-014", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_sql_injection", "difficulty": 2, "type": "mcq",
        "stem": "An attacker appends a UNION SELECT to a vulnerable query to pull columns from another table "
                "into the application's normal results. Which type of SQL injection is this?",
        "options": [
            {"id": "A", "text": "UNION-based (in-band) SQL injection"},
            {"id": "B", "text": "Boolean-based blind SQL injection"},
            {"id": "C", "text": "DOM-based XSS"},
            {"id": "D", "text": "Reflected XSS"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Using UNION SELECT to merge another table's data into the displayed results is UNION-based, "
                       "an in-band technique because the data appears directly in the response.",
            "distractors": {
                "B": "Boolean-based blind injection infers data from true/false behavior, not from merged visible output.",
                "C": "DOM-based XSS is a client-side script flaw, not a SQL technique.",
                "D": "Reflected XSS executes script in the browser; it is not SQL injection.",
            },
            "exam_pattern": "UNION SELECT to merge another table into visible output = UNION-based (in-band) SQLi.",
        },
        "references": ["CEH v13 Module 15: SQL Injection"],
    },
    {
        "id": "ceh-web-015", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_sql_injection", "difficulty": 2, "type": "mcq",
        "stem": "Which coding practice most effectively prevents SQL injection by separating code from data so "
                "user input is never interpreted as part of the SQL command?",
        "options": [
            {"id": "A", "text": "Client-side input length limits"},
            {"id": "B", "text": "Hiding the database version banner"},
            {"id": "C", "text": "Base64-encoding the input"},
            {"id": "D", "text": "Parameterized queries (prepared statements)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Parameterized queries/prepared statements bind user input as data, so it can never change "
                       "the query structure - the primary SQL injection defense (with input validation).",
            "distractors": {
                "A": "Client-side limits are trivially bypassed by sending requests directly to the server.",
                "B": "Hiding the version banner is obscurity; it does not stop injection.",
                "C": "Encoding input does not prevent injection and can be decoded before the query runs.",
            },
            "exam_pattern": "Prepared statements / parameterized queries (plus input validation) = primary SQLi defense.",
        },
        "references": ["CEH v13 Module 15: SQL Injection"],
    },
    {
        "id": "ceh-web-016", "exam": "ceh", "domain": "ceh_web_hacking",
        "subtopic": "ceh_sql_injection", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The open-source tool ______ automates the detection and exploitation of "
                "SQL injection flaws and the extraction of database contents during authorized testing.",
        "correct": ["sqlmap"],
        "explanation": {
            "correct": "sqlmap automates discovering and leveraging SQL injection points and dumping database "
                       "data; in a CEH context it is used only under explicit authorization.",
            "distractors": {},
            "exam_pattern": "Automated SQL injection detection/extraction tool = sqlmap.",
        },
        "references": ["CEH v13 Module 15: SQL Injection"],
    },
]
