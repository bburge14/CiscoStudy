"""Microsoft AZ-500 (Azure Security Engineer) round-2 expansion pool.

Deepens the verified AZ-500 bank with ~116 additional original, objective-aligned
items across all four exam domains, bringing the track to roughly 200 questions.
These items are NON-DUPLICATE with the round-1 pools (content_az500_identity.py,
content_az500_network.py, content_az500_compute.py, content_az500_secops.py): they
explore new angles within the same blueprint subtopics rather than restating the
first 84 items.

Distribution follows the exam domain weights:
  * az500_identity_access        (28%) - 33 items
  * az500_networking             (22%) - 25 items
  * az500_compute_storage_db     (25%) - 29 items
  * az500_security_operations    (25%) - 29 items

Authoring rules match the other content_*.py pools: build_content.py shuffles the
A/B/C/D order (seeded by id) so the authored key is not biased to any slot; every
wrong option carries a distractor note; each item names the Microsoft Learn area it
draws on. Current product names are used throughout: Microsoft Entra ID, Microsoft
Defender for Cloud, Microsoft Sentinel. Ids are prefixed az500-<area>-r2-NNN to stay
unique against the round-1 ids (az500-<area>-NNN). Items are original and aligned to
the public AZ-500 objectives - never real or memorized exam items.
"""

QUESTIONS = [
    # ======================================================================
    # DOMAIN 1 - Manage Identity and Access (az500_identity_access)
    # ======================================================================

    # ----- az500_entra_identities -----------------------------------------
    {
        "id": "az500-id-r2-001", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_entra_identities", "difficulty": 2, "type": "mcq",
        "stem": "You are lifting a legacy line-of-business application to Azure VMs. The app needs to "
                "domain-join and authenticate users with LDAP and Kerberos/NTLM, but you do not want to "
                "deploy or manage domain controllers. Which service meets this?",
        "options": [
            {"id": "A", "text": "Microsoft Entra Domain Services"},
            {"id": "B", "text": "Microsoft Entra B2B collaboration"},
            {"id": "C", "text": "Microsoft Entra ID Protection"},
            {"id": "D", "text": "Microsoft Entra Connect"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Entra Domain Services provides a managed domain (LDAP, Kerberos, NTLM, "
                       "domain join, group policy) without you deploying, patching, or managing domain controllers.",
            "distractors": {
                "B": "B2B collaboration invites external guests with their own credentials; it provides no managed domain for legacy apps.",
                "C": "ID Protection detects identity risk; it does not supply LDAP/Kerberos domain services.",
                "D": "Entra Connect synchronizes on-premises AD to Entra ID; it does not host a managed domain for VMs to join.",
            },
            "exam_pattern": "Managed domain (LDAP/Kerberos/NTLM/domain-join) with no DCs to manage = Microsoft Entra Domain Services.",
        },
        "references": ["Microsoft Learn (AZ-500): What is Microsoft Entra Domain Services"],
    },
    {
        "id": "az500-id-r2-002", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_entra_identities", "difficulty": 2, "type": "mcq",
        "stem": "You are building a dynamic security group that must contain every user whose department "
                "attribute is Sales. Which membership rule expression is correct?",
        "options": [
            {"id": "A", "text": "user.department -contains Sales"},
            {"id": "B", "text": "(user.department -eq \"Sales\")"},
            {"id": "C", "text": "department == 'Sales'"},
            {"id": "D", "text": "match(user, Sales)"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Dynamic membership rules use the form (property -operator \"value\"); -eq tests equality, so "
                       "(user.department -eq \"Sales\") selects users whose department equals Sales.",
            "distractors": {
                "A": "-contains checks whether a multi-valued property includes a value; it is the wrong operator for a single-valued equality test, and the quotes are missing.",
                "C": "== and single quotes are not valid dynamic membership rule syntax (that is programming syntax, not the rule builder).",
                "D": "match(...) is not a valid dynamic membership operator or function.",
            },
            "exam_pattern": "Dynamic rule syntax = (user.<attribute> -eq \"value\"); -eq/-ne/-startsWith/-contains are the operators.",
        },
        "references": ["Microsoft Learn (AZ-500): Dynamic membership rules for groups"],
    },
    {
        "id": "az500-id-r2-003", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_entra_identities", "difficulty": 3, "type": "mcq",
        "stem": "You delegate helpdesk administration with administrative units (AUs) but do not want to "
                "add members to each AU by hand as staff move between offices. Which capability keeps an AU's "
                "membership current automatically from a user attribute?",
        "options": [
            {"id": "A", "text": "A dynamic (rule-based) administrative unit"},
            {"id": "B", "text": "A Conditional Access named location"},
            {"id": "C", "text": "A role-assignable group"},
            {"id": "D", "text": "Group-based licensing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A dynamic administrative unit is populated by an attribute rule, so users are added to or "
                       "removed from the AU automatically as their attributes (such as office or department) change.",
            "distractors": {
                "B": "A named location defines IP/geography for Conditional Access; it does not populate an AU.",
                "C": "A role-assignable group can hold Entra role assignments, but it does not scope or auto-populate an administrative unit.",
                "D": "Group-based licensing assigns licenses to a group's members; it does not manage AU membership.",
            },
            "exam_pattern": "Auto-populate an administrative unit from an attribute rule = dynamic administrative unit (needs Entra ID P1).",
        },
        "references": ["Microsoft Learn (AZ-500): Dynamic membership rules for administrative units"],
    },
    {
        "id": "az500-id-r2-004", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_entra_identities", "difficulty": 2, "type": "multi",
        "stem": "You are creating emergency access (break-glass) accounts so admins are never locked out of "
                "the tenant. Which TWO practices are recommended for these accounts? (Choose two.)",
        "options": [
            {"id": "A", "text": "Make them cloud-only accounts (not synchronized from on-premises AD)"},
            {"id": "B", "text": "Exclude them from Conditional Access policies that could block their own sign-in"},
            {"id": "C", "text": "Share one account among all administrators to simplify recovery"},
            {"id": "D", "text": "Assign them the Reader role so they cannot cause damage"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Break-glass accounts should be cloud-only (so an on-premises outage or sync problem cannot "
                       "block them) and excluded from Conditional Access policies that could otherwise lock them out; they are highly privileged, monitored, and used only in emergencies.",
            "distractors": {
                "C": "A shared account destroys individual accountability; emergency accounts must still be attributable and tightly monitored.",
                "D": "Reader cannot perform recovery actions; break-glass accounts need Global Administrator so they can restore access in an emergency.",
            },
            "exam_pattern": "Break-glass = 2+ cloud-only Global Admin accounts, excluded from blocking CA, stored securely, and alerted on use.",
        },
        "references": ["Microsoft Learn (AZ-500): Manage emergency access accounts in Microsoft Entra ID"],
    },
    {
        "id": "az500-id-r2-005", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_entra_identities", "difficulty": 3, "type": "mcq",
        "stem": "Guests from a trusted partner tenant already satisfy MFA in their home tenant. You want your "
                "tenant to accept (trust) that MFA claim so guests are not prompted twice. Where do you configure this?",
        "options": [
            {"id": "A", "text": "In each Conditional Access policy's session controls"},
            {"id": "B", "text": "In cross-tenant access settings (inbound trust settings)"},
            {"id": "C", "text": "In the authentication methods policy"},
            {"id": "D", "text": "In the storage account firewall"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Cross-tenant access settings let you configure inbound trust so your tenant accepts MFA "
                       "(and compliant/hybrid-joined device) claims satisfied in the guest's home tenant, avoiding a second prompt.",
            "distractors": {
                "A": "Session controls govern in-session behavior (sign-in frequency, app-enforced restrictions); they do not establish cross-tenant MFA trust.",
                "C": "The authentication methods policy manages which methods users can register/use in your tenant, not trust of another tenant's MFA.",
                "D": "A storage account firewall filters network access to storage and is unrelated to B2B MFA trust.",
            },
            "exam_pattern": "Trust MFA/device claims from a partner Entra tenant for B2B guests = cross-tenant access settings (inbound trust).",
        },
        "references": ["Microsoft Learn (AZ-500): Cross-tenant access settings for B2B collaboration"],
    },
    {
        "id": "az500-id-r2-006", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_entra_identities", "difficulty": 2, "type": "mcq",
        "stem": "You want every member of a security group to automatically receive a Microsoft 365 E5 "
                "license, with licenses added or removed as group membership changes. Which Microsoft Entra "
                "feature provides this?",
        "options": [
            {"id": "A", "text": "Group-based licensing"},
            {"id": "B", "text": "Administrative units"},
            {"id": "C", "text": "Access reviews"},
            {"id": "D", "text": "Entitlement management access packages"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Group-based licensing assigns product licenses to a group; Entra automatically grants licenses "
                       "to new members and reclaims them from users who leave the group.",
            "distractors": {
                "B": "Administrative units scope delegated administration; they do not assign licenses.",
                "C": "Access reviews recertify access; they do not provision licenses based on membership.",
                "D": "Access packages bundle resource access for request/approval workflows; licensing by group membership is group-based licensing (needs Entra ID P1).",
            },
            "exam_pattern": "Assign/reclaim licenses automatically by group membership = group-based licensing (Entra ID P1).",
        },
        "references": ["Microsoft Learn (AZ-500): Group-based licensing in Microsoft Entra ID"],
    },
    {
        "id": "az500-id-r2-007", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_entra_identities", "difficulty": 2, "type": "mcq",
        "stem": "To limit what invited guest users can discover, you must stop guests from enumerating other "
                "users and groups in your directory, restricting them to their own profile and their own "
                "group memberships. Which setting enforces this?",
        "options": [
            {"id": "A", "text": "Set guest user access to the most restrictive level in External collaboration settings"},
            {"id": "B", "text": "Enable security defaults"},
            {"id": "C", "text": "Create a Conditional Access policy requiring MFA for guests"},
            {"id": "D", "text": "Assign guests the Global Reader role"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The 'Guest user access restrictions' option in External collaboration settings can be set to "
                       "the most restrictive level, limiting guests to their own directory objects and blocking enumeration of other users/groups.",
            "distractors": {
                "B": "Security defaults enforce baseline MFA and block legacy auth; they do not restrict guest directory enumeration.",
                "C": "Requiring MFA strengthens guest sign-in but does not limit what a signed-in guest can read in the directory.",
                "D": "Global Reader grants broad read access across the tenant - the opposite of restricting a guest.",
            },
            "exam_pattern": "Limit guest directory visibility = Guest user access restrictions (most restrictive) in External collaboration settings.",
        },
        "references": ["Microsoft Learn (AZ-500): Restrict guest access permissions in Microsoft Entra ID"],
    },
    {
        "id": "az500-id-r2-008", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_entra_identities", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: To grant access to Azure resources or applications through a role or an "
                "access assignment, you use a ________ group; a distribution group (used only for email) "
                "cannot be used for access management.",
        "correct": ["security"],
        "explanation": {
            "correct": "A security group (or a Microsoft 365 group) can be the principal of an access or role "
                       "assignment; distribution groups are mail-only and cannot be used to grant access.",
            "exam_pattern": "Access/role assignment principal = security group (or M365 group); distribution groups are email-only.",
        },
        "references": ["Microsoft Learn (AZ-500): Microsoft Entra group types for access management"],
    },

    # ----- az500_entra_authn_authz ----------------------------------------
    {
        "id": "az500-id-r2-009", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_entra_authn_authz", "difficulty": 2, "type": "mcq",
        "stem": "Audit shows that legacy authentication protocols (such as IMAP, POP, and SMTP AUTH) are "
                "being used to bypass your MFA requirement, because they cannot present an MFA challenge. "
                "What is the most effective way to close this gap?",
        "options": [
            {"id": "A", "text": "Lengthen password expiration so users change passwords less often"},
            {"id": "B", "text": "A Conditional Access policy that blocks legacy authentication clients"},
            {"id": "C", "text": "Enable SSPR for all users"},
            {"id": "D", "text": "Add security questions as a second factor"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Legacy authentication clients cannot perform MFA, so attackers use them to bypass it. A "
                       "Conditional Access policy that blocks legacy authentication forces clients onto modern auth where MFA can be enforced.",
            "distractors": {
                "A": "Password expiration does nothing to stop legacy protocols from bypassing MFA.",
                "C": "SSPR lets users reset passwords; it does not block legacy authentication.",
                "D": "Security questions are a weak factor and do not address the legacy-protocol bypass at all.",
            },
            "exam_pattern": "Legacy auth bypasses MFA - block it with a Conditional Access policy (the vast majority of password-spray hits legacy auth).",
        },
        "references": ["Microsoft Learn (AZ-500): Block legacy authentication with Conditional Access"],
    },
    {
        "id": "az500-id-r2-010", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_entra_authn_authz", "difficulty": 2, "type": "mcq",
        "stem": "Before enforcing a new Conditional Access policy tenant-wide, you want to see exactly who "
                "and what it would affect - and whether it would block anyone - without actually enforcing "
                "the grant controls. Which policy state do you use?",
        "options": [
            {"id": "A", "text": "On"},
            {"id": "B", "text": "Off"},
            {"id": "C", "text": "Report-only"},
            {"id": "D", "text": "Disabled with a resource lock"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Report-only mode evaluates the policy against real sign-ins and logs what the result would "
                       "have been, without enforcing grant/session controls, so you can validate impact before turning it On.",
            "distractors": {
                "A": "On enforces the policy immediately - exactly what you want to avoid until you have validated impact.",
                "B": "Off disables the policy entirely, so it is not evaluated and produces no impact data.",
                "D": "Resource locks protect Azure resources from deletion; they are unrelated to Conditional Access evaluation modes.",
            },
            "exam_pattern": "Test a Conditional Access policy's impact without enforcing it = report-only mode (see results in sign-in logs / What If).",
        },
        "references": ["Microsoft Learn (AZ-500): Conditional Access report-only mode"],
    },
    {
        "id": "az500-id-r2-011", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_entra_authn_authz", "difficulty": 3, "type": "mcq",
        "stem": "For access to a highly sensitive app, policy must require specifically phishing-resistant "
                "methods (FIDO2 security keys, Windows Hello for Business, or certificate-based auth) and "
                "reject ordinary SMS or Authenticator push. Which Conditional Access grant control expresses this?",
        "options": [
            {"id": "A", "text": "Require multifactor authentication"},
            {"id": "B", "text": "Require authentication strength (Phishing-resistant MFA)"},
            {"id": "C", "text": "Require approved client app"},
            {"id": "D", "text": "Require password change"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Authentication strengths let a Conditional Access policy require a specific set of methods; "
                       "the built-in 'Phishing-resistant MFA' strength permits only FIDO2, Windows Hello for Business, and certificate-based authentication.",
            "distractors": {
                "A": "'Require MFA' accepts any registered second factor, including SMS or push - it cannot mandate phishing-resistant methods specifically.",
                "C": "'Require approved client app' governs which mobile apps may access data; it does not specify authentication strength.",
                "D": "'Require password change' forces a password reset; it is not a method-strength control.",
            },
            "exam_pattern": "Mandate a specific (e.g. phishing-resistant) method set in Conditional Access = authentication strengths, not the generic 'require MFA'.",
        },
        "references": ["Microsoft Learn (AZ-500): Conditional Access authentication strengths"],
    },
    {
        "id": "az500-id-r2-012", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_entra_authn_authz", "difficulty": 2, "type": "mcq",
        "stem": "A new employee has no password and no registered MFA method yet, but must bootstrap "
                "passwordless sign-in (register a FIDO2 key or Windows Hello) on their first day. Which "
                "time-limited credential lets them onboard?",
        "options": [
            {"id": "A", "text": "A Temporary Access Pass (TAP)"},
            {"id": "B", "text": "A permanent SMS code"},
            {"id": "C", "text": "A shared service account password"},
            {"id": "D", "text": "A client secret"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A Temporary Access Pass is a time-limited passcode an admin issues so a user can sign in and "
                       "register passwordless methods (or recover a lost credential) without an existing password or MFA method.",
            "distractors": {
                "B": "SMS is not a bootstrap onboarding credential and is not passwordless; a permanent code would be a standing weakness.",
                "C": "Sharing a service account violates individual accountability and does not register the user's own methods.",
                "D": "A client secret authenticates an application/service principal, not a human onboarding to passwordless sign-in.",
            },
            "exam_pattern": "Time-limited onboarding/recovery credential to register passwordless methods = Temporary Access Pass (TAP).",
        },
        "references": ["Microsoft Learn (AZ-500): Configure a Temporary Access Pass"],
    },
    {
        "id": "az500-id-r2-013", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_entra_authn_authz", "difficulty": 3, "type": "mcq",
        "stem": "Microsoft Entra ID Protection flags a user as high USER risk because their credentials "
                "appeared in a known breach (leaked credentials). What should the automated user-risk policy "
                "require to remediate the account?",
        "options": [
            {"id": "A", "text": "Block all access permanently"},
            {"id": "B", "text": "Require a secure password change (self-remediation via MFA)"},
            {"id": "C", "text": "Require the device to be hybrid joined"},
            {"id": "D", "text": "Do nothing, because user risk cannot be remediated"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Leaked credentials raise user risk; the user-risk policy requires a secure password change "
                       "(after MFA), which remediates the account and lowers its risk. Sign-in risk, by contrast, typically requires MFA.",
            "distractors": {
                "A": "A permanent block is disruptive and unnecessary; a secure password change self-remediates the leaked-credential risk.",
                "C": "Requiring a hybrid-joined device is a device control and does not remediate a leaked password.",
                "D": "User risk is remediable - a secure password change clears it; that is the whole point of the user-risk policy.",
            },
            "exam_pattern": "User risk (e.g. leaked credentials) -> require secure password change; sign-in risk -> require MFA (both via ID Protection + Conditional Access, Entra ID P2).",
        },
        "references": ["Microsoft Learn (AZ-500): Microsoft Entra ID Protection user risk policy"],
    },
    {
        "id": "az500-id-r2-014", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_entra_authn_authz", "difficulty": 2, "type": "mcq",
        "stem": "You want corporate Windows devices to sign in passwordless with a biometric or PIN that "
                "unlocks a device-bound private key, giving phishing-resistant authentication tied to the "
                "specific device. Which method is this?",
        "options": [
            {"id": "A", "text": "SMS one-time passcode"},
            {"id": "B", "text": "Windows Hello for Business"},
            {"id": "C", "text": "Security questions"},
            {"id": "D", "text": "Pass-through authentication"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Windows Hello for Business replaces passwords with a device-bound asymmetric credential "
                       "unlocked by biometrics or a PIN; the private key never leaves the device, making it phishing-resistant.",
            "distractors": {
                "A": "SMS codes are a weak, interceptable second factor and are not passwordless.",
                "C": "Security questions are knowledge-based secrets - the weakest factor, not a device-bound passwordless credential.",
                "D": "Pass-through authentication validates passwords against on-premises AD; it is a password-based hybrid method, not passwordless Hello.",
            },
            "exam_pattern": "Device-bound biometric/PIN passwordless sign-in with keys that never leave the device = Windows Hello for Business.",
        },
        "references": ["Microsoft Learn (AZ-500): Windows Hello for Business overview"],
    },
    {
        "id": "az500-id-r2-015", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_entra_authn_authz", "difficulty": 3, "type": "mcq",
        "stem": "When you disable a user or an admin revokes their sessions, you need the change enforced in "
                "near real time at the resource (for example Exchange Online) instead of waiting up to an hour "
                "for the access token to expire. Which capability provides this?",
        "options": [
            {"id": "A", "text": "Continuous access evaluation (CAE)"},
            {"id": "B", "text": "Self-service password reset"},
            {"id": "C", "text": "A longer token lifetime"},
            {"id": "D", "text": "Security defaults"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Continuous access evaluation lets Entra ID and supporting resources react to critical events "
                       "(account disabled, password reset, session revoked, risk detected) in near real time, rather than waiting for the access token to expire.",
            "distractors": {
                "B": "SSPR lets users reset their own passwords; it does not accelerate token revocation at resources.",
                "C": "A longer token lifetime makes the problem worse by extending how long a stale token stays valid.",
                "D": "Security defaults enforce baseline MFA/legacy-auth blocking; they do not provide near-real-time revocation.",
            },
            "exam_pattern": "Near-real-time revocation of access on critical events (no waiting for token expiry) = continuous access evaluation (CAE).",
        },
        "references": ["Microsoft Learn (AZ-500): Continuous access evaluation in Microsoft Entra ID"],
    },
    {
        "id": "az500-id-r2-016", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_entra_authn_authz", "difficulty": 1, "type": "mcq",
        "stem": "A small organization on the free Microsoft Entra ID tier wants a one-click baseline that "
                "requires all users to register and use MFA, forces MFA for admins, and blocks legacy "
                "authentication - with no per-app customization. What should they enable?",
        "options": [
            {"id": "A", "text": "A custom Conditional Access policy per application"},
            {"id": "B", "text": "Security defaults"},
            {"id": "C", "text": "Privileged Identity Management"},
            {"id": "D", "text": "Microsoft Entra ID Protection"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Security defaults are a free, all-or-nothing baseline that enforces MFA registration/use, "
                       "requires MFA for privileged actions, and blocks legacy authentication, without the granular control (or licensing) of Conditional Access.",
            "distractors": {
                "A": "Per-app Conditional Access policies require Entra ID P1 and are the opposite of a single no-customization baseline.",
                "C": "PIM manages just-in-time privileged roles (P2) and is not a tenant-wide MFA baseline.",
                "D": "ID Protection provides risk-based policies (P2); it is not the free one-click baseline.",
            },
            "exam_pattern": "Free, all-or-nothing MFA + legacy-auth-block baseline = security defaults; granular control = Conditional Access (P1).",
        },
        "references": ["Microsoft Learn (AZ-500): Security defaults in Microsoft Entra ID"],
    },
    {
        "id": "az500-id-r2-017", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_entra_authn_authz", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: In a Conditional Access policy, grant controls decide whether to allow "
                "access, while ________ controls restrict what happens within the session (for example "
                "sign-in frequency or app-enforced restrictions on unmanaged devices).",
        "correct": ["session"],
        "explanation": {
            "correct": "Session controls limit in-session behavior - sign-in frequency, persistent browser session, "
                       "app-enforced restrictions, and Conditional Access App Control - after access is granted.",
            "exam_pattern": "Conditional Access: grant controls = allow/block + requirements; session controls = limits within the session.",
        },
        "references": ["Microsoft Learn (AZ-500): Conditional Access session controls"],
    },

    # ----- az500_rbac_pim -------------------------------------------------
    {
        "id": "az500-id-r2-018", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_rbac_pim", "difficulty": 3, "type": "mcq",
        "stem": "No built-in Azure role matches a need: operators must restart virtual machines but must not "
                "be able to start, stop, delete, or change them. What should you create?",
        "options": [
            {"id": "A", "text": "A custom Azure role with only the restart action in Actions and a defined AssignableScopes"},
            {"id": "B", "text": "A Conditional Access policy"},
            {"id": "C", "text": "An Azure Policy with a Deny effect"},
            {"id": "D", "text": "A Microsoft Entra directory role"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A custom Azure role lets you specify exactly the control-plane operations allowed (Actions, "
                       "with NotActions and AssignableScopes); granting only the VM restart action meets least privilege when no built-in role fits.",
            "distractors": {
                "B": "Conditional Access governs identity sign-in conditions, not which Azure resource operations a principal may perform.",
                "C": "An Azure Policy Deny blocks noncompliant resource configurations; it does not define what actions a user is permitted.",
                "D": "Entra directory roles govern the directory/tenant, not granular Azure resource operations like restarting a VM.",
            },
            "exam_pattern": "No built-in Azure role fits -> author a custom role (Actions/NotActions/DataActions/AssignableScopes) for least privilege.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure custom roles"],
    },
    {
        "id": "az500-id-r2-019", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_rbac_pim", "difficulty": 3, "type": "mcq",
        "stem": "A principal holds a role that includes Microsoft.Storage/storageAccounts/read but cannot "
                "read the blobs' contents. In an Azure role definition, which element grants data-plane "
                "operations such as reading blob data?",
        "options": [
            {"id": "A", "text": "Actions"},
            {"id": "B", "text": "NotActions"},
            {"id": "C", "text": "DataActions"},
            {"id": "D", "text": "AssignableScopes"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "DataActions grant data-plane operations (such as reading blob content); Actions grant "
                       "management-plane (control-plane) operations on the resource itself. Reading the account object is not the same as reading its data.",
            "distractors": {
                "A": "Actions cover control-plane operations (managing the storage account), not reading the data inside it.",
                "B": "NotActions subtract permissions from Actions; they do not grant data-plane access.",
                "D": "AssignableScopes defines where the role can be assigned, not which operations it grants.",
            },
            "exam_pattern": "Control plane = Actions/NotActions; data plane (e.g. blob contents) = DataActions/NotDataActions.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure role definition - Actions vs DataActions"],
    },
    {
        "id": "az500-id-r2-020", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_rbac_pim", "difficulty": 3, "type": "mcq",
        "stem": "A user has Owner on a resource group, yet is explicitly prevented from deleting a specific "
                "storage account there by a deny assignment. Why does the deny assignment win?",
        "options": [
            {"id": "A", "text": "Because Azure RBAC is additive and role assignments always override deny assignments"},
            {"id": "B", "text": "Because deny assignments block specified actions and take precedence over role assignments"},
            {"id": "C", "text": "Because Owner does not include delete permissions"},
            {"id": "D", "text": "Because a deny assignment is the same as a ReadOnly resource lock"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Azure RBAC is additive through role assignments, but deny assignments explicitly block "
                       "specified actions and take precedence, so the Owner cannot perform the denied delete. Deny assignments are typically created by Azure (for example by managed apps), not directly by users.",
            "distractors": {
                "A": "Role assignments do not override deny assignments; deny takes precedence.",
                "C": "Owner does include delete; the block comes from the deny assignment, not a missing permission.",
                "D": "A resource lock is a separate mechanism; a deny assignment denies specific actions to specific principals and is not the same as a lock.",
            },
            "exam_pattern": "RBAC is additive, but a deny assignment overrides role assignments for the actions it denies.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure deny assignments"],
    },
    {
        "id": "az500-id-r2-021", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_rbac_pim", "difficulty": 3, "type": "mcq",
        "stem": "A Global Administrator must temporarily manage Azure RBAC assignments across every "
                "subscription in the tenant - but currently has no access to the subscriptions. Which action "
                "grants this without a per-subscription assignment?",
        "options": [
            {"id": "A", "text": "Enable 'Access management for Azure resources' (elevate access) to gain User Access Administrator at root scope"},
            {"id": "B", "text": "Assign themselves Reader on each subscription"},
            {"id": "C", "text": "Create a Conditional Access policy for admins"},
            {"id": "D", "text": "Add themselves to a dynamic group"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A Global Administrator can toggle 'Access management for Azure resources' (elevate access), "
                       "which grants the User Access Administrator role at the root scope (/), letting them manage role assignments across all subscriptions; it should be turned off again after use.",
            "distractors": {
                "B": "Reader is view-only and cannot manage role assignments, and it would still be per-subscription.",
                "C": "Conditional Access governs sign-in, not Azure resource access scope.",
                "D": "A dynamic group automates membership; it does not grant tenant-root Azure resource access.",
            },
            "exam_pattern": "Global Admin needs tenant-wide Azure access -> elevate access to get User Access Administrator at root (/), then disable it afterward.",
        },
        "references": ["Microsoft Learn (AZ-500): Elevate access to manage all Azure subscriptions"],
    },
    {
        "id": "az500-id-r2-022", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_rbac_pim", "difficulty": 2, "type": "mcq",
        "stem": "You want to assign a Microsoft Entra directory role (for example Helpdesk Administrator) to "
                "a group so you can manage its members in one place and use PIM for Groups. What must be true "
                "of the group?",
        "options": [
            {"id": "A", "text": "It must be a distribution group"},
            {"id": "B", "text": "It must be a dynamic membership group"},
            {"id": "C", "text": "It must be created as a role-assignable group (isAssignableToRole = true)"},
            {"id": "D", "text": "It must be an administrative unit"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Only a role-assignable group (created with isAssignableToRole set, assigned-membership, and "
                       "extra protections) can hold Microsoft Entra directory role assignments; this is required to govern it with PIM for Groups.",
            "distractors": {
                "A": "Distribution groups are mail-only and cannot hold role assignments.",
                "B": "Role-assignable groups must use assigned membership; dynamic membership is not supported for role-assignable groups.",
                "D": "An administrative unit scopes delegated administration; it is not a group you assign a role to.",
            },
            "exam_pattern": "Assign an Entra role to a group / use PIM for Groups = create a role-assignable group (isAssignableToRole, assigned membership, protected).",
        },
        "references": ["Microsoft Learn (AZ-500): Use Microsoft Entra role-assignable groups"],
    },
    {
        "id": "az500-id-r2-023", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_rbac_pim", "difficulty": 3, "type": "mcq",
        "stem": "Membership of a sensitive security group grants access to production. You want users to hold "
                "no standing membership and instead activate membership just-in-time, with approval and a time "
                "limit. Which capability provides this?",
        "options": [
            {"id": "A", "text": "PIM for Groups (eligible group membership)"},
            {"id": "B", "text": "Dynamic membership rules"},
            {"id": "C", "text": "A Conditional Access policy on the group"},
            {"id": "D", "text": "Group-based licensing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "PIM for Groups makes users eligible for group membership (or ownership), which they activate "
                       "just-in-time with the configured controls (justification, MFA, approval, maximum duration), so they hold no standing access.",
            "distractors": {
                "B": "Dynamic rules auto-populate membership continuously; they provide no just-in-time activation or approval.",
                "C": "Conditional Access governs sign-in conditions, not time-bound group membership activation.",
                "D": "Group-based licensing assigns licenses by membership; it does not provide JIT membership.",
            },
            "exam_pattern": "Just-in-time, approved, time-bound membership of a group = PIM for Groups (eligible membership).",
        },
        "references": ["Microsoft Learn (AZ-500): Privileged Identity Management for Groups"],
    },
    {
        "id": "az500-id-r2-024", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_rbac_pim", "difficulty": 2, "type": "mcq",
        "stem": "An engineer needs to manage virtual machines in a single resource group only. Following "
                "least privilege, how should you assign the Virtual Machine Contributor role?",
        "options": [
            {"id": "A", "text": "At the management group scope"},
            {"id": "B", "text": "At the subscription scope"},
            {"id": "C", "text": "At that resource group scope"},
            {"id": "D", "text": "At the tenant root scope"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Assign the role at the narrowest scope that satisfies the need - here the specific resource "
                       "group - so the engineer cannot manage VMs elsewhere; RBAC inherits downward, so a broader scope would over-grant.",
            "distractors": {
                "A": "A management group scope would grant the role across many subscriptions - far beyond one resource group.",
                "B": "A subscription scope would let them manage VMs in every resource group in the subscription.",
                "D": "The tenant root scope is the broadest possible scope - the opposite of least privilege.",
            },
            "exam_pattern": "Least privilege = assign at the narrowest scope that meets the need (resource > resource group > subscription > management group).",
        },
        "references": ["Microsoft Learn (AZ-500): Azure RBAC best practices - least privilege scope"],
    },
    {
        "id": "az500-id-r2-025", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_rbac_pim", "difficulty": 2, "type": "mcq",
        "stem": "Security wants to be warned when privileged-access hygiene slips - for example when there "
                "are too many Global Administrators, roles are assigned outside PIM, or accounts activate roles "
                "they never use. Which Privileged Identity Management feature surfaces these?",
        "options": [
            {"id": "A", "text": "PIM alerts"},
            {"id": "B", "text": "Azure Monitor metrics"},
            {"id": "C", "text": "Resource locks"},
            {"id": "D", "text": "Network security groups"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "PIM generates security alerts for risky privileged-access conditions (too many admins, roles "
                       "assigned outside PIM, stale/unused roles, admins without MFA), so you can investigate and tighten configuration.",
            "distractors": {
                "B": "Azure Monitor metrics track resource performance/health, not PIM role-hygiene conditions.",
                "C": "Resource locks prevent deletion/modification of resources; they do not evaluate privileged-access hygiene.",
                "D": "NSGs filter network traffic and are unrelated to privileged role governance.",
            },
            "exam_pattern": "Warnings about privileged-role hygiene (too many admins, roles outside PIM, stale roles) = PIM alerts.",
        },
        "references": ["Microsoft Learn (AZ-500): Configure security alerts in Privileged Identity Management"],
    },
    {
        "id": "az500-id-r2-026", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_rbac_pim", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: An Azure role assignment is the combination of a security principal, a "
                "role definition, and a ________ - the level (management group, subscription, resource group, "
                "or resource) at which the access applies.",
        "correct": ["scope"],
        "explanation": {
            "correct": "Scope is the set of resources the access applies to; Azure role assignments nest from "
                       "management group to subscription to resource group to resource, inheriting downward.",
            "exam_pattern": "Role assignment = principal + role definition + scope; scopes inherit downward.",
        },
        "references": ["Microsoft Learn (AZ-500): Understand scope for Azure RBAC"],
    },

    # ----- az500_app_identity ---------------------------------------------
    {
        "id": "az500-id-r2-027", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_app_identity", "difficulty": 3, "type": "mcq",
        "stem": "A GitHub Actions workflow must deploy to Azure without any stored client secret or "
                "certificate, exchanging the pipeline's own token for a Microsoft Entra token. Which feature "
                "enables this secretless trust?",
        "options": [
            {"id": "A", "text": "Workload identity federation (federated credentials)"},
            {"id": "B", "text": "A long-lived client secret stored as a pipeline variable"},
            {"id": "C", "text": "A user delegation SAS"},
            {"id": "D", "text": "A Temporary Access Pass"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Workload identity federation configures a federated credential on an app registration (or "
                       "user-assigned managed identity) that trusts an external issuer's token (GitHub, another cloud, Kubernetes), so the workload gets Entra tokens with no stored secret.",
            "distractors": {
                "B": "A stored client secret is exactly the long-lived credential federation eliminates, and it can leak.",
                "C": "A user delegation SAS grants limited access to storage data; it does not authenticate a CI/CD workload to Entra ID.",
                "D": "A Temporary Access Pass is a human onboarding/recovery credential, not a workload trust mechanism.",
            },
            "exam_pattern": "Secretless trust for external workloads (GitHub Actions, other clouds, K8s) = workload identity federation (federated credentials).",
        },
        "references": ["Microsoft Learn (AZ-500): Workload identity federation"],
    },
    {
        "id": "az500-id-r2-028", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_app_identity", "difficulty": 2, "type": "mcq",
        "stem": "Which statement correctly describes the lifecycle of a system-assigned managed identity on "
                "an Azure VM?",
        "options": [
            {"id": "A", "text": "It is a standalone resource you can attach to several VMs"},
            {"id": "B", "text": "It is created with the VM, is 1:1 with it, and is deleted automatically when the VM is deleted"},
            {"id": "C", "text": "It persists after the VM is deleted so you can reuse it"},
            {"id": "D", "text": "It requires you to store and rotate its client secret"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A system-assigned managed identity is tied 1:1 to its resource; Azure creates it with the "
                       "resource and deletes it when the resource is deleted, and no credential is ever exposed to you.",
            "distractors": {
                "A": "Sharing one identity across resources describes a user-assigned managed identity, not a system-assigned one.",
                "C": "A system-assigned identity does not outlive its resource; a user-assigned identity is the one with an independent lifecycle.",
                "D": "Managed identities never require you to store or rotate a secret - Azure manages the credential.",
            },
            "exam_pattern": "System-assigned MI = 1:1 with the resource, deleted with it; user-assigned MI = standalone, shareable, independent lifecycle.",
        },
        "references": ["Microsoft Learn (AZ-500): Managed identity types and lifecycle"],
    },
    {
        "id": "az500-id-r2-029", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_app_identity", "difficulty": 3, "type": "mcq",
        "stem": "A background daemon with no signed-in user must call Microsoft Graph to read all users' "
                "profiles. Which kind of Microsoft Graph permission must it be granted, and how is it consented?",
        "options": [
            {"id": "A", "text": "A delegated permission, consented by each user at sign-in"},
            {"id": "B", "text": "An application permission, granted with admin consent"},
            {"id": "C", "text": "A user delegation SAS scoped to Graph"},
            {"id": "D", "text": "An Azure RBAC role on the subscription"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A daemon runs with no user context, so it needs an application (app-only) permission, which "
                       "requires administrator consent because it applies tenant-wide without a signed-in user.",
            "distractors": {
                "A": "Delegated permissions act on behalf of a signed-in user - there is no user in a background daemon.",
                "C": "SAS tokens grant access to Azure Storage data, not Microsoft Graph API permissions.",
                "D": "Azure RBAC governs Azure resource management, not Microsoft Graph API permission scopes.",
            },
            "exam_pattern": "No signed-in user (daemon/service) = application (app-only) Graph permission + admin consent; with a user = delegated permission.",
        },
        "references": ["Microsoft Learn (AZ-500): Microsoft Graph application vs delegated permissions"],
    },
    {
        "id": "az500-id-r2-030", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_app_identity", "difficulty": 2, "type": "mcq",
        "stem": "To reduce the attack surface from rogue or risky OAuth apps, you must ensure that only "
                "administrators - not ordinary users - can create new app registrations in the tenant. Which "
                "setting enforces this?",
        "options": [
            {"id": "A", "text": "Set 'Users can register applications' to No in user settings"},
            {"id": "B", "text": "Enable blob soft delete"},
            {"id": "C", "text": "Assign all users the Application Developer role"},
            {"id": "D", "text": "Create a dynamic group of applications"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Setting 'Users can register applications' to No in the tenant's user settings removes the "
                       "default-user ability to create app registrations, so only privileged roles can register apps.",
            "distractors": {
                "B": "Blob soft delete protects storage data from deletion; it has nothing to do with app registration rights.",
                "C": "Application Developer grants users the ability to register apps - the opposite of restricting it.",
                "D": "Dynamic groups automate membership; they do not control who may register applications.",
            },
            "exam_pattern": "Restrict who can create app registrations = set 'Users can register applications' to No (default user permissions).",
        },
        "references": ["Microsoft Learn (AZ-500): Restrict who can create applications"],
    },
    {
        "id": "az500-id-r2-031", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_app_identity", "difficulty": 3, "type": "mcq",
        "stem": "You must block a service principal (workload identity) from authenticating unless the "
                "request comes from a trusted IP range. Which capability lets you apply such a location-based "
                "policy to a non-human identity?",
        "options": [
            {"id": "A", "text": "Conditional Access for workload identities"},
            {"id": "B", "text": "Self-service password reset"},
            {"id": "C", "text": "A network security group on the app"},
            {"id": "D", "text": "A resource lock"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Conditional Access for workload identities applies policies (such as blocking by location) to "
                       "service principals/managed identities, extending conditional controls to non-human identities (requires Workload Identities Premium).",
            "distractors": {
                "B": "SSPR is for human users resetting passwords; it does not apply policy to a service principal.",
                "C": "An NSG filters network traffic to resources; it does not evaluate a workload identity's sign-in conditions.",
                "D": "A resource lock prevents resource deletion/modification; it does not gate authentication by location.",
            },
            "exam_pattern": "Apply Conditional Access (e.g. location block) to a service principal/managed identity = Conditional Access for workload identities.",
        },
        "references": ["Microsoft Learn (AZ-500): Conditional Access for workload identities"],
    },
    {
        "id": "az500-id-r2-032", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_app_identity", "difficulty": 2, "type": "mcq",
        "stem": "You enable a system-assigned managed identity on a function app so it can read a Key Vault "
                "secret, but calls still fail with an authorization error. What is the most likely missing step?",
        "options": [
            {"id": "A", "text": "The identity has not been granted an access role on the Key Vault (for example Key Vault Secrets User)"},
            {"id": "B", "text": "The function app needs a public IP address"},
            {"id": "C", "text": "The Key Vault must be deleted and recreated"},
            {"id": "D", "text": "You must embed the account key in the app settings"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Enabling a managed identity only creates the identity; it has no permissions until you grant "
                       "it access - for example assigning Key Vault Secrets User (RBAC) or a secret-get access policy on the vault.",
            "distractors": {
                "B": "A public IP is unrelated to Entra authorization; the failure is a missing access grant, not networking.",
                "C": "Recreating the vault does not grant the identity access and would lose configuration.",
                "D": "Embedding a key reintroduces the very secret managed identities exist to eliminate; it is not the fix.",
            },
            "exam_pattern": "A managed identity has no access until you assign it a role/policy - enabling the identity is only half the configuration.",
        },
        "references": ["Microsoft Learn (AZ-500): Grant a managed identity access to a resource"],
    },
    {
        "id": "az500-id-r2-033", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_app_identity", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: When an application is registered, Microsoft Entra creates one global "
                "application object plus, in each tenant where the app is used, a service ________ (the "
                "enterprise application) that holds the local sign-in and permission grants.",
        "correct": ["principal"],
        "explanation": {
            "correct": "The service principal is the local tenant instance of an application; it is what receives "
                       "permission grants and is used for sign-in, while the application object is the single global blueprint.",
            "exam_pattern": "App registration = global application object; service principal (enterprise application) = per-tenant local instance.",
        },
        "references": ["Microsoft Learn (AZ-500): Application and service principal objects"],
    },

    # ======================================================================
    # DOMAIN 2 - Secure Networking (az500_networking)
    # ======================================================================

    # ----- az500_network_security -----------------------------------------
    {
        "id": "az500-net-r2-001", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_network_security", "difficulty": 2, "type": "mcq",
        "stem": "A newly created network security group has no custom rules. A VM in its subnet can still "
                "receive traffic from other VMs in the same virtual network but not unsolicited traffic from "
                "the internet. Which built-in behavior explains this?",
        "options": [
            {"id": "A", "text": "The default rules: AllowVnetInBound permits intra-VNet traffic and DenyAllInBound blocks the rest"},
            {"id": "B", "text": "An implicit allow-all inbound rule"},
            {"id": "C", "text": "Azure Firewall is filtering the traffic"},
            {"id": "D", "text": "A user-defined route is dropping internet traffic"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Every NSG has default rules you cannot delete: AllowVnetInBound (65000) permits traffic "
                       "within the virtual network, AllowAzureLoadBalancerInBound (65001) permits the load balancer, and DenyAllInBound (65500) blocks everything else inbound.",
            "distractors": {
                "B": "There is no implicit allow-all inbound; the final default inbound rule is DenyAllInBound.",
                "C": "An NSG does not require Azure Firewall; the default NSG rules alone produce this behavior.",
                "D": "A UDR controls routing/next-hop, not inbound allow/deny; the NSG default rules are responsible.",
            },
            "exam_pattern": "NSG default rules: AllowVnetInBound 65000, AllowAzureLoadBalancerInBound 65001, DenyAllInBound 65500 (and outbound mirrors); user rules use 100-4096.",
        },
        "references": ["Microsoft Learn (AZ-500): Network security group default security rules"],
    },
    {
        "id": "az500-net-r2-002", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_network_security", "difficulty": 2, "type": "mcq",
        "stem": "You must allow VMs outbound access to Azure Storage without hard-coding Azure datacenter IP "
                "ranges that change over time, and have the ranges stay current automatically. Which NSG "
                "capability do you use in the rule?",
        "options": [
            {"id": "A", "text": "An application security group"},
            {"id": "B", "text": "A service tag (for example, Storage)"},
            {"id": "C", "text": "A user-defined route"},
            {"id": "D", "text": "A private endpoint"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Service tags represent a managed group of Azure service IP ranges (such as Storage, Sql, or "
                       "AzureCloud) that Microsoft keeps updated, so you reference the tag in a rule instead of maintaining IP lists.",
            "distractors": {
                "A": "Application security groups group your own VMs by workload, not Azure service IP ranges.",
                "C": "A UDR controls next-hop routing; it does not provide managed service IP ranges for NSG rules.",
                "D": "A private endpoint gives a PaaS service a private IP; it is not an NSG rule construct for Azure service ranges.",
            },
            "exam_pattern": "Reference Azure service IP ranges that stay current = service tags; group your own VMs = application security groups.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure service tags for network security groups"],
    },
    {
        "id": "az500-net-r2-003", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_network_security", "difficulty": 3, "type": "mcq",
        "stem": "You want a single NSG rule to cover several source IP prefixes, multiple destination ports, "
                "and several application security groups at once, instead of many near-identical rules. Which "
                "feature allows this?",
        "options": [
            {"id": "A", "text": "Augmented security rules"},
            {"id": "B", "text": "Forced tunneling"},
            {"id": "C", "text": "DNAT rules"},
            {"id": "D", "text": "Stored access policies"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Augmented security rules let one NSG rule list multiple IP addresses/ranges, multiple ports, "
                       "and multiple service tags or application security groups, simplifying rule sets that would otherwise need many entries.",
            "distractors": {
                "B": "Forced tunneling redirects outbound traffic to an on-premises or firewall next hop; it is a routing concept, not NSG rule consolidation.",
                "C": "DNAT rules are an Azure Firewall feature for inbound translation, not an NSG rule-authoring feature.",
                "D": "Stored access policies constrain storage SAS tokens; they are unrelated to NSG rules.",
            },
            "exam_pattern": "Combine many prefixes/ports/ASGs into one NSG rule = augmented security rules.",
        },
        "references": ["Microsoft Learn (AZ-500): Augmented security rules in network security groups"],
    },
    {
        "id": "az500-net-r2-004", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_network_security", "difficulty": 2, "type": "mcq",
        "stem": "You are deploying Azure Firewall into a hub virtual network. Which of the following is a "
                "deployment requirement?",
        "options": [
            {"id": "A", "text": "A dedicated subnet named AzureFirewallSubnet (at least /26) and a public IP address"},
            {"id": "B", "text": "A subnet named GatewaySubnet of exactly /29"},
            {"id": "C", "text": "A private endpoint in every spoke"},
            {"id": "D", "text": "A ReadOnly resource lock on the virtual network"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure Firewall must be deployed into a dedicated subnet named AzureFirewallSubnet that is at "
                       "least /26, and it is assigned one or more public IP addresses for outbound SNAT and management.",
            "distractors": {
                "B": "GatewaySubnet is for VPN/ExpressRoute gateways, not Azure Firewall, and the name/size shown is wrong for the firewall.",
                "C": "Private endpoints are not a prerequisite for deploying Azure Firewall.",
                "D": "A resource lock protects resources from deletion; it is not a firewall deployment requirement.",
            },
            "exam_pattern": "Azure Firewall needs its own subnet named AzureFirewallSubnet (>=/26) plus a public IP; the VPN/ER gateway uses GatewaySubnet.",
        },
        "references": ["Microsoft Learn (AZ-500): Deploy Azure Firewall - subnet and public IP requirements"],
    },
    {
        "id": "az500-net-r2-005", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_network_security", "difficulty": 3, "type": "mcq",
        "stem": "You want Azure Firewall to automatically alert on and drop traffic to or from IP addresses "
                "and domains that Microsoft Threat Intelligence flags as known-malicious. Which setting do you "
                "configure?",
        "options": [
            {"id": "A", "text": "Threat intelligence-based filtering set to 'Alert and deny'"},
            {"id": "B", "text": "A DNAT rule"},
            {"id": "C", "text": "An NSG service tag rule"},
            {"id": "D", "text": "Forced tunneling"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure Firewall's threat intelligence-based filtering uses the Microsoft Threat Intelligence "
                       "feed; set to 'Alert and deny', it both alerts on and blocks traffic to/from known-malicious IPs and FQDNs.",
            "distractors": {
                "B": "A DNAT rule translates inbound traffic to internal resources; it does not evaluate threat intelligence.",
                "C": "An NSG service tag rule references Azure service ranges; it is not a threat-intelligence block list.",
                "D": "Forced tunneling redirects outbound traffic to a next hop; it is not threat-intelligence filtering.",
            },
            "exam_pattern": "Block known-bad IPs/FQDNs on Azure Firewall = threat intelligence-based filtering set to 'Alert and deny' (vs 'Alert only').",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Firewall threat intelligence-based filtering"],
    },
    {
        "id": "az500-net-r2-006", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_network_security", "difficulty": 3, "type": "mcq",
        "stem": "You manage several Azure Firewalls across regions and want to define base rules once in a "
                "parent policy that child policies inherit, with rule collection groups ordered by priority. "
                "Which object provides this?",
        "options": [
            {"id": "A", "text": "Classic firewall rules configured per firewall"},
            {"id": "B", "text": "Azure Firewall Policy (which supports parent/child inheritance)"},
            {"id": "C", "text": "A network security group"},
            {"id": "D", "text": "A route table"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Azure Firewall Policy is a central resource you can structure hierarchically: a parent policy "
                       "holds base rules that child policies inherit, and rule collection groups are evaluated by priority, letting you manage many firewalls consistently.",
            "distractors": {
                "A": "Classic rules are configured per firewall and do not support hierarchical inheritance or central management.",
                "C": "An NSG is a per-subnet/NIC 5-tuple filter, not a hierarchical firewall policy.",
                "D": "A route table directs next-hop routing; it does not define firewall rules or inheritance.",
            },
            "exam_pattern": "Central, inheritable, priority-ordered firewall rules across firewalls = Azure Firewall Policy (parent/child), not classic rules.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Firewall Policy and rule collection groups"],
    },
    {
        "id": "az500-net-r2-007", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_network_security", "difficulty": 2, "type": "mcq",
        "stem": "You must publish an internal web server (private IP) so that specific inbound internet "
                "traffic on a public IP and port is translated to that server through Azure Firewall. Which "
                "rule type do you create?",
        "options": [
            {"id": "A", "text": "An application rule"},
            {"id": "B", "text": "A network rule"},
            {"id": "C", "text": "A DNAT rule"},
            {"id": "D", "text": "An NSG inbound allow rule only"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A DNAT (destination network address translation) rule on Azure Firewall translates inbound "
                       "traffic hitting the firewall's public IP/port to an internal private IP/port, publishing the service.",
            "distractors": {
                "A": "Application rules allow outbound access by FQDN/HTTP(S); they do not translate inbound traffic.",
                "B": "Network rules filter by IP/port/protocol but do not perform inbound destination translation.",
                "D": "An NSG rule can allow traffic but cannot translate a public IP/port to a different internal address the way DNAT does.",
            },
            "exam_pattern": "Publish/translate inbound internet traffic to an internal resource through Azure Firewall = DNAT rule.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Firewall DNAT rules"],
    },
    {
        "id": "az500-net-r2-008", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_network_security", "difficulty": 2, "type": "mcq",
        "stem": "After an incident you need a record of which flows an NSG allowed and denied, so you can "
                "analyze traffic patterns and top talkers over time. Which capability captures this?",
        "options": [
            {"id": "A", "text": "NSG flow logs (via Network Watcher), optionally with Traffic Analytics"},
            {"id": "B", "text": "A diagnostic setting on a Key Vault"},
            {"id": "C", "text": "Microsoft Entra sign-in logs"},
            {"id": "D", "text": "A stored access policy"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "NSG flow logs (through Network Watcher) record allowed/denied 5-tuple flows to a storage "
                       "account; Traffic Analytics can then process them into insights such as top talkers and traffic patterns.",
            "distractors": {
                "B": "A Key Vault diagnostic setting logs vault operations, not network flows through an NSG.",
                "C": "Entra sign-in logs record authentication events, not network traffic allowed/denied by an NSG.",
                "D": "A stored access policy constrains storage SAS tokens; it does not capture flow records.",
            },
            "exam_pattern": "Record allowed/denied network flows for analysis = NSG flow logs (Network Watcher) + Traffic Analytics.",
        },
        "references": ["Microsoft Learn (AZ-500): NSG flow logs and Traffic Analytics"],
    },
    {
        "id": "az500-net-r2-009", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_network_security", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: A network security group is ________, meaning that when it allows an "
                "inbound flow, the return (response) traffic is automatically permitted without needing a "
                "separate outbound rule.",
        "correct": ["stateful"],
        "explanation": {
            "correct": "Because NSGs are stateful, they track established flows and automatically allow the return "
                       "traffic for a permitted connection, so you do not author a matching reverse rule.",
            "exam_pattern": "NSGs are stateful - allow a flow and its return traffic is permitted automatically.",
        },
        "references": ["Microsoft Learn (AZ-500): How network security groups work (stateful)"],
    },

    # ----- az500_private_connectivity -------------------------------------
    {
        "id": "az500-net-r2-010", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_private_connectivity", "difficulty": 3, "type": "mcq",
        "stem": "You are creating a private endpoint for a storage account that must be reachable privately "
                "for blob access but NOT for file shares. How do you scope the private endpoint to just blob?",
        "options": [
            {"id": "A", "text": "Select the target sub-resource (group ID) 'blob' when creating the private endpoint"},
            {"id": "B", "text": "Disable the storage account firewall"},
            {"id": "C", "text": "Create a service endpoint for Microsoft.Storage instead"},
            {"id": "D", "text": "Add a public IP to the file endpoint"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A private endpoint targets a specific sub-resource (group ID) of the service - for storage, "
                       "'blob', 'file', 'queue', 'table', etc. - so selecting 'blob' gives a private IP for blob only; file would need its own private endpoint.",
            "distractors": {
                "B": "Disabling the firewall broadens exposure and does not scope the private endpoint to a sub-resource.",
                "C": "A service endpoint applies at the subnet to the whole service and does not create a per-sub-resource private IP.",
                "D": "Adding a public IP is contrary to private connectivity and does not scope blob vs file.",
            },
            "exam_pattern": "A private endpoint targets one sub-resource (group ID, e.g. blob/file) - use a separate endpoint per sub-resource you need.",
        },
        "references": ["Microsoft Learn (AZ-500): Private endpoint target sub-resources (group IDs)"],
    },
    {
        "id": "az500-net-r2-011", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_private_connectivity", "difficulty": 2, "type": "mcq",
        "stem": "A consumer in another subscription requests a private endpoint connection to your Private "
                "Link-enabled service. The connection shows as Pending. What determines whether traffic can "
                "flow?",
        "options": [
            {"id": "A", "text": "The resource owner must approve the pending private endpoint connection"},
            {"id": "B", "text": "The consumer must open port 443 on their NSG"},
            {"id": "C", "text": "A UDR must be added automatically"},
            {"id": "D", "text": "The connection auto-approves after 24 hours"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Private endpoint connections use an approval workflow: when created with manual approval, the "
                       "connection stays Pending until the resource owner approves it, which is how cross-subscription/tenant access is controlled.",
            "distractors": {
                "B": "Opening an NSG port does not approve a Private Link connection; the owner's approval is required.",
                "C": "No UDR is auto-added to approve the connection; approval is an explicit owner action.",
                "D": "Pending connections do not auto-approve on a timer; they require explicit approval (or rejection).",
            },
            "exam_pattern": "Private endpoint connection approval workflow: manual approval leaves it Pending until the resource owner approves.",
        },
        "references": ["Microsoft Learn (AZ-500): Manage private endpoint connections (approval workflow)"],
    },
    {
        "id": "az500-net-r2-012", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_private_connectivity", "difficulty": 3, "type": "mcq",
        "stem": "A subnet uses a service endpoint for Azure Storage. To prevent data exfiltration, you must "
                "ensure that subnet can reach ONLY your approved storage accounts over that endpoint, not any "
                "storage account in Azure. What do you apply?",
        "options": [
            {"id": "A", "text": "A service endpoint policy listing the allowed storage accounts"},
            {"id": "B", "text": "A private DNS zone"},
            {"id": "C", "text": "A network security group deny rule for the Storage service tag"},
            {"id": "D", "text": "A CanNotDelete lock on the subnet"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A service endpoint policy filters virtual network traffic over service endpoints to a specific "
                       "allow-list of Azure Storage accounts, preventing exfiltration to unapproved storage accounts.",
            "distractors": {
                "B": "A private DNS zone resolves names for private endpoints; it does not restrict which storage accounts a service endpoint can reach.",
                "C": "Denying the Storage service tag would block all storage, not restrict to approved accounts.",
                "D": "A resource lock prevents deletion/modification; it does not filter which storage accounts are reachable.",
            },
            "exam_pattern": "Restrict a service-endpoint subnet to specific approved storage accounts (anti-exfiltration) = service endpoint policies.",
        },
        "references": ["Microsoft Learn (AZ-500): Virtual network service endpoint policies"],
    },
    {
        "id": "az500-net-r2-013", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_private_connectivity", "difficulty": 2, "type": "mcq",
        "stem": "To make a private endpoint's DNS records maintain themselves (create/update/delete the A "
                "record in privatelink.blob.core.windows.net as the endpoint changes), what should you "
                "associate with the private endpoint?",
        "options": [
            {"id": "A", "text": "A private DNS zone group linking the endpoint to the privatelink zone"},
            {"id": "B", "text": "A public DNS CNAME to the storage account"},
            {"id": "C", "text": "A service endpoint policy"},
            {"id": "D", "text": "A user-defined route"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A private DNS zone group ties the private endpoint to the appropriate privatelink zone (for "
                       "example privatelink.blob.core.windows.net) and automatically manages the DNS records as the endpoint is created, changed, or deleted.",
            "distractors": {
                "B": "A public CNAME would keep clients resolving to the public endpoint, defeating private resolution.",
                "C": "A service endpoint policy restricts service-endpoint targets; it does not manage private-endpoint DNS records.",
                "D": "A UDR directs routing; it does not create or maintain DNS records.",
            },
            "exam_pattern": "Automatic private-endpoint DNS = private DNS zone group bound to the privatelink.<service> zone linked to the VNet.",
        },
        "references": ["Microsoft Learn (AZ-500): Private endpoint DNS zone group integration"],
    },
    {
        "id": "az500-net-r2-014", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_private_connectivity", "difficulty": 2, "type": "mcq",
        "stem": "Your team wants to connect to Bastion-protected VMs using the native Windows RDP/SSH client "
                "and the az CLI (not just the portal), plus use shareable links. Which Azure Bastion SKU is "
                "required for these capabilities?",
        "options": [
            {"id": "A", "text": "Developer"},
            {"id": "B", "text": "Basic"},
            {"id": "C", "text": "Standard (or higher)"},
            {"id": "D", "text": "No SKU supports native client connections"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Native client support, IP-based connection, custom ports, host scaling, and shareable links "
                       "are Standard-tier (or higher) features; the Basic tier offers portal-based RDP/SSH without them, and Developer is a minimal shared option.",
            "distractors": {
                "A": "The Developer SKU is a lightweight, shared option for dev/test and lacks these advanced features.",
                "B": "Basic provides portal-based RDP/SSH but not native client, IP-based connection, custom ports, or shareable links.",
                "D": "Native client connections are supported - specifically on the Standard SKU and above.",
            },
            "exam_pattern": "Bastion native client / IP-based connection / shareable links / host scaling = Standard SKU (Premium adds session recording + private-only).",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Bastion SKU feature comparison"],
    },
    {
        "id": "az500-net-r2-015", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_private_connectivity", "difficulty": 2, "type": "mcq",
        "stem": "Two virtual networks in the same region must communicate privately over the Microsoft "
                "backbone with low latency, without routing through the public internet or a VPN gateway. "
                "What should you configure?",
        "options": [
            {"id": "A", "text": "Virtual network peering"},
            {"id": "B", "text": "A point-to-site VPN"},
            {"id": "C", "text": "A private endpoint in each VNet"},
            {"id": "D", "text": "Azure Front Door"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Virtual network peering connects two VNets directly over the Microsoft backbone with private "
                       "IP connectivity and low latency, and needs no gateway (peering is non-transitive).",
            "distractors": {
                "B": "A point-to-site VPN connects individual clients to a VNet over the internet; it is not the way to join two VNets privately on the backbone.",
                "C": "Private endpoints connect to a specific PaaS resource, not two whole VNets to each other.",
                "D": "Front Door is a global HTTP(S) entry/CDN service, not private VNet-to-VNet connectivity.",
            },
            "exam_pattern": "Private, low-latency VNet-to-VNet over the Microsoft backbone = VNet peering (non-transitive, no gateway needed).",
        },
        "references": ["Microsoft Learn (AZ-500): Virtual network peering"],
    },
    {
        "id": "az500-net-r2-016", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_private_connectivity", "difficulty": 2, "type": "mcq",
        "stem": "Compliance requires that hybrid connectivity between on-premises and Azure use a private, "
                "dedicated connection that does not traverse the public internet at all. Which service meets "
                "this?",
        "options": [
            {"id": "A", "text": "A site-to-site VPN over the internet"},
            {"id": "B", "text": "Azure ExpressRoute"},
            {"id": "C", "text": "Azure Bastion"},
            {"id": "D", "text": "A public load balancer"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "ExpressRoute provides a private, dedicated connection from on-premises to Azure through a "
                       "connectivity provider; the traffic does not go over the public internet, meeting the requirement.",
            "distractors": {
                "A": "A site-to-site VPN is encrypted but still traverses the public internet, so it does not meet a 'no public internet' mandate.",
                "C": "Bastion brokers RDP/SSH to VMs; it is not a hybrid on-premises-to-Azure WAN connection.",
                "D": "A public load balancer distributes internet-facing traffic; it is not private hybrid connectivity.",
            },
            "exam_pattern": "Private, dedicated, no-public-internet hybrid link = ExpressRoute; encrypted-over-internet = site-to-site VPN.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure ExpressRoute vs VPN connectivity"],
    },
    {
        "id": "az500-net-r2-017", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_private_connectivity", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: To deploy Azure Bastion (Basic/Standard/Premium), the virtual network "
                "must contain a dedicated subnet named ________ that is at least a /26.",
        "correct": ["AzureBastionSubnet"],
        "explanation": {
            "correct": "Azure Bastion requires a dedicated subnet named exactly AzureBastionSubnet (at least /26) in "
                       "the same virtual network; the subnet must not contain other resources.",
            "exam_pattern": "Bastion subnet = AzureBastionSubnet (>=/26); Azure Firewall subnet = AzureFirewallSubnet (>=/26); gateway = GatewaySubnet.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Bastion configuration - AzureBastionSubnet"],
    },

    # ----- az500_edge_protection ------------------------------------------
    {
        "id": "az500-net-r2-018", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_edge_protection", "difficulty": 2, "type": "mcq",
        "stem": "You deploy a WAF policy on Application Gateway in Detection mode, confirm it would catch "
                "attacks in the logs, and now need it to actually block malicious requests. What change do "
                "you make?",
        "options": [
            {"id": "A", "text": "Switch the WAF policy to Prevention mode"},
            {"id": "B", "text": "Delete the managed rule set"},
            {"id": "C", "text": "Disable the WAF policy"},
            {"id": "D", "text": "Move the app behind Azure Bastion"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "In Detection mode a WAF only logs matches; switching to Prevention mode makes it actively "
                       "block or challenge requests that match its rules. Detection is for tuning; Prevention is for enforcement.",
            "distractors": {
                "B": "Deleting the managed rule set removes the detections entirely, which is the opposite of blocking attacks.",
                "C": "Disabling the WAF stops all inspection, so nothing is blocked.",
                "D": "Bastion provides secure VM management access; it does not perform web application firewalling.",
            },
            "exam_pattern": "WAF Detection = log only (tuning); Prevention = block/enforce. Validate in Detection, then move to Prevention.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure WAF Detection and Prevention modes"],
    },
    {
        "id": "az500-net-r2-019", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_edge_protection", "difficulty": 2, "type": "multi",
        "stem": "Beyond the managed OWASP rule set, which TWO protections can you add with Azure WAF custom "
                "rules? (Choose two.)",
        "options": [
            {"id": "A", "text": "Rate limiting (throttle requests from a client exceeding a threshold)"},
            {"id": "B", "text": "Geo-match filtering (allow or block by source country/region)"},
            {"id": "C", "text": "Encrypting the web app's database at rest"},
            {"id": "D", "text": "Rotating the storage account keys"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "WAF custom rules support rate-limiting rules (throttle clients above a request threshold) and "
                       "geo-match conditions (allow/block by source geography), in addition to IP/size/string match conditions.",
            "distractors": {
                "C": "Database encryption at rest (TDE) is a data-layer control, not a WAF custom rule.",
                "D": "Rotating storage keys is storage credential hygiene and has nothing to do with WAF request filtering.",
            },
            "exam_pattern": "WAF custom rules = rate limiting, geo-match, IP/string/size match (layered on top of managed OWASP rules).",
        },
        "references": ["Microsoft Learn (AZ-500): Azure WAF custom rules (rate limiting, geo-match)"],
    },
    {
        "id": "az500-net-r2-020", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_edge_protection", "difficulty": 3, "type": "mcq",
        "stem": "You need adaptive DDoS mitigation with telemetry for a handful of standalone public IP "
                "addresses, and want to pay per protected IP rather than enabling protection for an entire "
                "virtual network. Which option fits?",
        "options": [
            {"id": "A", "text": "Azure DDoS IP Protection"},
            {"id": "B", "text": "Azure DDoS Network Protection"},
            {"id": "C", "text": "The free always-on infrastructure protection only"},
            {"id": "D", "text": "A network security group rate-limit rule"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure DDoS IP Protection is a per-public-IP SKU that adds adaptive tuning, telemetry, and "
                       "mitigation on individual IPs - ideal when you want to protect a few addresses and pay per IP, rather than the per-VNet Network Protection plan.",
            "distractors": {
                "B": "Network Protection protects all public IPs on protected virtual networks and is billed at the plan level - more than needed for a few IPs.",
                "C": "The free platform (infrastructure) protection is always on but untuned, with no per-resource telemetry, metrics, or alerting.",
                "D": "An NSG cannot absorb or adaptively mitigate a volumetric DDoS attack.",
            },
            "exam_pattern": "Per-IP tuned DDoS mitigation = DDoS IP Protection; per-VNet = DDoS Network Protection; untuned free baseline = infrastructure protection.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure DDoS Protection tiers (IP Protection vs Network Protection)"],
    },
    {
        "id": "az500-net-r2-021", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_edge_protection", "difficulty": 3, "type": "mcq",
        "stem": "To inspect encrypted outbound HTTPS with Azure Firewall Premium TLS inspection, the firewall "
                "must decrypt and re-encrypt the traffic. What must you provide for this to work?",
        "options": [
            {"id": "A", "text": "An intermediate CA certificate (provided via Azure Key Vault) that the firewall uses to generate certificates on the fly"},
            {"id": "B", "text": "A user delegation SAS"},
            {"id": "C", "text": "A public IP on every backend server"},
            {"id": "D", "text": "A ReadOnly resource lock on the firewall"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "TLS inspection requires the firewall to act as a trusted intermediate CA; you supply an "
                       "intermediate CA certificate (referenced from Key Vault via the firewall's managed identity) so it can decrypt, inspect, and re-encrypt the session.",
            "distractors": {
                "B": "A SAS grants limited storage data access; it is unrelated to providing a CA certificate for TLS inspection.",
                "C": "Backend public IPs are not required for TLS inspection; an intermediate CA certificate is.",
                "D": "A resource lock prevents deletion/modification and does nothing to enable TLS inspection.",
            },
            "exam_pattern": "Azure Firewall Premium TLS inspection needs an intermediate CA certificate (from Key Vault) so the firewall can decrypt and re-encrypt.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Firewall Premium TLS inspection and certificates"],
    },
    {
        "id": "az500-net-r2-022", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_edge_protection", "difficulty": 3, "type": "mcq",
        "stem": "Azure Firewall Premium's IDPS is currently in 'Alert only' mode and is detecting but not "
                "stopping a known exploit signature. What change actively blocks matching traffic?",
        "options": [
            {"id": "A", "text": "Set the IDPS mode to 'Alert and deny'"},
            {"id": "B", "text": "Disable threat intelligence"},
            {"id": "C", "text": "Switch the firewall to the Standard tier"},
            {"id": "D", "text": "Add a DNAT rule for the signature"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The IDPS (intrusion detection and prevention system) can run in 'Alert only' (detect/log) or "
                       "'Alert and deny' (detect and block). Setting it to 'Alert and deny' makes it drop traffic matching malicious signatures.",
            "distractors": {
                "B": "Disabling threat intelligence removes another protection and does not make IDPS block.",
                "C": "The Standard tier has no IDPS at all, so switching to it removes the capability.",
                "D": "A DNAT rule translates inbound traffic; it is not how IDPS blocks a signature match.",
            },
            "exam_pattern": "Make Firewall Premium IDPS block (not just detect) = set IDPS mode to 'Alert and deny' (Standard tier has no IDPS).",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Firewall Premium IDPS signatures and modes"],
    },
    {
        "id": "az500-net-r2-023", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_edge_protection", "difficulty": 2, "type": "mcq",
        "stem": "A compliance rule says all client connections to your web app through Application Gateway "
                "must negotiate TLS 1.2 or higher and disallow older protocol versions. Where do you enforce "
                "this?",
        "options": [
            {"id": "A", "text": "In the Application Gateway SSL/TLS policy (set a minimum protocol version)"},
            {"id": "B", "text": "In a network security group rule"},
            {"id": "C", "text": "In a user-defined route"},
            {"id": "D", "text": "In the storage account firewall"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Application Gateway's SSL/TLS policy lets you set a minimum protocol version (and cipher "
                       "suites), so you can require TLS 1.2+ and reject older, weaker protocol versions at the gateway listener.",
            "distractors": {
                "B": "An NSG filters by IP/port, not by TLS protocol version.",
                "C": "A UDR controls routing next-hop and cannot enforce TLS versions.",
                "D": "The storage account firewall governs storage network access; it does not set the web app gateway's TLS policy.",
            },
            "exam_pattern": "Enforce minimum TLS version/cipher at the web edge = Application Gateway SSL/TLS policy.",
        },
        "references": ["Microsoft Learn (AZ-500): Application Gateway TLS policy (minimum protocol version)"],
    },
    {
        "id": "az500-net-r2-024", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_edge_protection", "difficulty": 3, "type": "mcq",
        "stem": "Users must reach your web app only through Azure Front Door, and the origin web servers must "
                "not be publicly reachable at all. Which Front Door capability lets the origin stay private?",
        "options": [
            {"id": "A", "text": "Private Link origin (Front Door connects to the origin over Private Link)"},
            {"id": "B", "text": "A public IP on the origin protected by an NSG"},
            {"id": "C", "text": "A service endpoint on the origin subnet"},
            {"id": "D", "text": "Azure Bastion in front of the origin"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure Front Door Premium can connect to an origin over Private Link, so the backend has no "
                       "public endpoint and is reachable only through Front Door, shrinking the attack surface.",
            "distractors": {
                "B": "A public IP (even with an NSG) leaves the origin internet-reachable, which the requirement forbids.",
                "C": "A service endpoint optimizes a subnet's path to Azure PaaS; it does not make Front Door reach a private origin.",
                "D": "Bastion is for RDP/SSH management, not for private web traffic from Front Door to an origin.",
            },
            "exam_pattern": "Lock a web origin to Front Door only (no public endpoint) = Front Door Premium Private Link origin.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Front Door Private Link origins"],
    },
    {
        "id": "az500-net-r2-025", "exam": "az500", "domain": "az500_networking",
        "subtopic": "az500_edge_protection", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: Azure Web Application Firewall's managed rule sets are based on the "
                "________ Core Rule Set (CRS), which detects common web attacks such as SQL injection and "
                "cross-site scripting.",
        "correct": ["OWASP"],
        "explanation": {
            "correct": "Azure WAF's managed rules derive from the OWASP Core Rule Set (CRS), providing baseline "
                       "protection against common web attacks; you layer custom rules on top.",
            "exam_pattern": "WAF managed rules = OWASP Core Rule Set (CRS); add custom rules (rate limit, geo-match, bot) on top.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure WAF managed rule sets (OWASP CRS)"],
    },

    # ======================================================================
    # DOMAIN 3 - Secure Compute, Storage, and Databases (az500_compute_storage_db)
    # ======================================================================

    # ----- az500_compute_security -----------------------------------------
    {
        "id": "az500-comp-r2-001", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_compute_security", "difficulty": 2, "type": "multi",
        "stem": "You enable Trusted Launch on a Generation 2 VM to defend against boot-level rootkits and "
                "bootkits. Which TWO features does Trusted Launch rely on? (Choose two.)",
        "options": [
            {"id": "A", "text": "Secure Boot (only signed, trusted boot components are loaded)"},
            {"id": "B", "text": "A virtual Trusted Platform Module (vTPM) for measured boot and attestation"},
            {"id": "C", "text": "An in-guest BitLocker agent keyed from Key Vault"},
            {"id": "D", "text": "A user delegation SAS on the OS disk"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Trusted Launch combines Secure Boot (blocks unsigned/malicious boot components) with a vTPM "
                       "(enables measured boot and remote attestation of boot integrity), protecting against rootkits and bootkits on Gen2 VMs.",
            "distractors": {
                "C": "BitLocker in-guest with Key Vault describes Azure Disk Encryption (volume encryption), not Trusted Launch's boot protections.",
                "D": "A SAS grants limited storage access and has nothing to do with VM boot integrity.",
            },
            "exam_pattern": "Trusted Launch = Secure Boot + vTPM (+ optional boot integrity monitoring) for Gen2 VMs against boot-level malware.",
        },
        "references": ["Microsoft Learn (AZ-500): Trusted launch for Azure virtual machines"],
    },
    {
        "id": "az500-comp-r2-002", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_compute_security", "difficulty": 3, "type": "mcq",
        "stem": "A regulated workload requires that VM memory be encrypted and isolated even from the "
                "hypervisor and Azure host operators while the workload runs (data-in-use protection in a "
                "hardware trusted execution environment). Which option provides this?",
        "options": [
            {"id": "A", "text": "A standard VM with Azure Disk Encryption"},
            {"id": "B", "text": "An Azure confidential VM (hardware-based TEE, e.g. AMD SEV-SNP)"},
            {"id": "C", "text": "Encryption at host on a standard VM"},
            {"id": "D", "text": "A VM with only a ReadOnly resource lock"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Azure confidential VMs run in a hardware-based trusted execution environment (for example AMD "
                       "SEV-SNP) that encrypts memory in use and isolates the VM from the hypervisor, host, and even Azure operators - protecting data in use.",
            "distractors": {
                "A": "Azure Disk Encryption protects data at rest on the disks; it does not encrypt or isolate memory in use.",
                "C": "Encryption at host protects disk/cache/temp data at rest at the host; it is not in-use memory isolation from the hypervisor.",
                "D": "A resource lock prevents deletion/modification; it provides no confidential-computing protection.",
            },
            "exam_pattern": "Protect data in use / isolate memory from the host and hypervisor = confidential VMs (hardware TEE, e.g. AMD SEV-SNP).",
        },
        "references": ["Microsoft Learn (AZ-500): Azure confidential VMs and confidential computing"],
    },
    {
        "id": "az500-comp-r2-003", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_compute_security", "difficulty": 3, "type": "mcq",
        "stem": "Managed disks are already encrypted at rest with platform-managed keys, but policy now "
                "requires you to control the encryption key in your own Key Vault and be able to rotate or "
                "revoke it. What should you configure for the disks?",
        "options": [
            {"id": "A", "text": "A disk encryption set referencing a customer-managed key in Key Vault"},
            {"id": "B", "text": "Dynamic Data Masking"},
            {"id": "C", "text": "A service endpoint for Microsoft.Storage"},
            {"id": "D", "text": "A stored access policy"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A disk encryption set binds managed-disk server-side encryption to a customer-managed key in "
                       "Key Vault, so you control key rotation and revocation instead of relying solely on platform-managed keys.",
            "distractors": {
                "B": "Dynamic Data Masking obscures SQL result columns; it has nothing to do with managed-disk encryption keys.",
                "C": "A service endpoint optimizes a subnet's path to storage; it does not supply a CMK for disks.",
                "D": "A stored access policy constrains storage SAS tokens, not disk encryption keys.",
            },
            "exam_pattern": "Customer-managed key for managed-disk server-side encryption = disk encryption set + key in Key Vault.",
        },
        "references": ["Microsoft Learn (AZ-500): Server-side encryption of managed disks with customer-managed keys"],
    },
    {
        "id": "az500-comp-r2-004", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_compute_security", "difficulty": 2, "type": "mcq",
        "stem": "You enable Microsoft Defender for Servers Plan 1 (not Plan 2). Which core capability does "
                "Plan 1 deliver?",
        "options": [
            {"id": "A", "text": "Endpoint detection and response through the integrated Microsoft Defender for Endpoint"},
            {"id": "B", "text": "File integrity monitoring"},
            {"id": "C", "text": "Agentless vulnerability and malware scanning"},
            {"id": "D", "text": "Just-in-time VM access"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Defender for Servers Plan 1 centers on EDR via the integrated Microsoft Defender for Endpoint "
                       "(automatic onboarding and licensing); the richer posture/response features are in Plan 2.",
            "distractors": {
                "B": "File integrity monitoring is a Plan 2 feature, not included in Plan 1.",
                "C": "Agentless scanning (vulnerabilities, malware, secrets) is a Plan 2 capability.",
                "D": "Just-in-time VM access is part of Plan 2, not Plan 1.",
            },
            "exam_pattern": "Defender for Servers Plan 1 = Defender for Endpoint EDR; Plan 2 adds FIM, agentless scanning, JIT, OS config assessment, and more.",
        },
        "references": ["Microsoft Learn (AZ-500): Select a Defender for Servers plan (Plan 1 vs Plan 2)"],
    },
    {
        "id": "az500-comp-r2-005", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_compute_security", "difficulty": 2, "type": "mcq",
        "stem": "You want to assess VMs for vulnerabilities, installed software, secrets, and malware WITHOUT "
                "deploying or maintaining an agent on each machine. Which Microsoft Defender for Servers "
                "capability provides this?",
        "options": [
            {"id": "A", "text": "Agentless machine scanning (Defender for Servers Plan 2)"},
            {"id": "B", "text": "Azure Disk Encryption"},
            {"id": "C", "text": "A network security group"},
            {"id": "D", "text": "Transparent Data Encryption"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Agentless machine scanning in Defender for Servers Plan 2 takes snapshots of disks to assess "
                       "software inventory, vulnerabilities, secrets, and malware without installing an agent on the VM.",
            "distractors": {
                "B": "Azure Disk Encryption encrypts volumes; it does not scan for vulnerabilities or malware.",
                "C": "An NSG filters traffic; it does not perform vulnerability or malware assessment.",
                "D": "TDE encrypts databases at rest and is unrelated to agentless VM scanning.",
            },
            "exam_pattern": "Scan VMs for vulns/software/secrets/malware without an agent = agentless scanning (Defender for Servers Plan 2 / Defender CSPM).",
        },
        "references": ["Microsoft Learn (AZ-500): Agentless machine scanning in Defender for Servers"],
    },
    {
        "id": "az500-comp-r2-006", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_compute_security", "difficulty": 3, "type": "mcq",
        "stem": "On an Azure Kubernetes Service cluster you want to authorize access to Kubernetes resources "
                "using Microsoft Entra identities and Azure role assignments, so you can stop distributing "
                "local kubeconfig admin credentials. What do you enable?",
        "options": [
            {"id": "A", "text": "Microsoft Entra integration with Azure RBAC for Kubernetes Authorization"},
            {"id": "B", "text": "A user delegation SAS for the cluster"},
            {"id": "C", "text": "Dynamic Data Masking"},
            {"id": "D", "text": "A storage account firewall"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Enabling Microsoft Entra integration with Azure RBAC for Kubernetes Authorization lets you "
                       "control cluster access with Entra identities and Azure role assignments (and disable local accounts), replacing shared kubeconfig admin certs.",
            "distractors": {
                "B": "A SAS is a storage data access token; it does not authorize Kubernetes API operations.",
                "C": "Dynamic Data Masking is a SQL feature, unrelated to AKS authorization.",
                "D": "A storage account firewall restricts storage network access, not Kubernetes RBAC.",
            },
            "exam_pattern": "Govern AKS access with Entra identities + Azure RBAC for Kubernetes (and disable local accounts) instead of shared kubeconfig.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure RBAC for Kubernetes Authorization with Microsoft Entra"],
    },
    {
        "id": "az500-comp-r2-007", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_compute_security", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: Encryption at ________ encrypts a VM's temporary disk, OS/data disk "
                "caches, and the data flowing to Azure Storage at the Azure server itself, with no in-guest "
                "encryption agent required.",
        "correct": ["host"],
        "explanation": {
            "correct": "Encryption at host performs the encryption on the Azure host before data leaves it, covering "
                       "temp disks and caches end to end without an in-guest agent (unlike Azure Disk Encryption).",
            "exam_pattern": "Agentless, host-level encryption of temp disk/caches/flows = encryption at host; in-guest BitLocker/dm-crypt = Azure Disk Encryption.",
        },
        "references": ["Microsoft Learn (AZ-500): Encryption at host for Azure VMs"],
    },

    # ----- az500_storage_security -----------------------------------------
    {
        "id": "az500-comp-r2-008", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_storage_security", "difficulty": 3, "type": "mcq",
        "stem": "You issued a service SAS to a partner with a one-year expiry, and now need to revoke it "
                "immediately without rotating the storage account keys. What should the SAS have been tied to "
                "so you can invalidate it server-side?",
        "options": [
            {"id": "A", "text": "A stored access policy (which you can modify or delete to revoke the SAS)"},
            {"id": "B", "text": "A private endpoint"},
            {"id": "C", "text": "A resource lock"},
            {"id": "D", "text": "A service tag"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A service SAS bound to a stored access policy can be revoked server-side by editing or deleting "
                       "that policy, without rotating account keys; an ad-hoc SAS not tied to a policy can only be invalidated by rotating the signing key.",
            "distractors": {
                "B": "A private endpoint controls network reachability; it does not revoke an issued SAS token.",
                "C": "A resource lock prevents resource deletion/modification; it cannot invalidate a SAS.",
                "D": "A service tag is an IP-range construct for NSG/firewall rules; it has no bearing on SAS revocation.",
            },
            "exam_pattern": "Revoke a service SAS without rotating keys = tie it to a stored access policy, then modify/delete the policy.",
        },
        "references": ["Microsoft Learn (AZ-500): Define a stored access policy to control a service SAS"],
    },
    {
        "id": "az500-comp-r2-009", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_storage_security", "difficulty": 1, "type": "mcq",
        "stem": "A security baseline requires that all client access to an Azure Storage account use "
                "encrypted connections only, rejecting any plain HTTP request. Which account setting enforces "
                "this?",
        "options": [
            {"id": "A", "text": "Enable 'Secure transfer required' (HTTPS only)"},
            {"id": "B", "text": "Enable blob soft delete"},
            {"id": "C", "text": "Enable infrastructure encryption"},
            {"id": "D", "text": "Add a CanNotDelete lock"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The 'Secure transfer required' setting forces all requests over HTTPS (and secure SMB), "
                       "rejecting unencrypted HTTP; you can also raise the minimum TLS version.",
            "distractors": {
                "B": "Soft delete recovers deleted data; it does not enforce encrypted connections.",
                "C": "Infrastructure encryption adds a second encryption layer at rest; it does not govern transport security.",
                "D": "A resource lock blocks deletion/modification; it does not require HTTPS.",
            },
            "exam_pattern": "Reject plain HTTP to storage = Secure transfer required (HTTPS only); tighten further with minimum TLS version.",
        },
        "references": ["Microsoft Learn (AZ-500): Require secure transfer for Azure Storage"],
    },
    {
        "id": "az500-comp-r2-010", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_storage_security", "difficulty": 3, "type": "mcq",
        "stem": "Beyond the default single layer of encryption at rest, a regulatory requirement mandates TWO "
                "independent layers of encryption for data at rest in a storage account, using separate keys "
                "and algorithms. Which feature provides this?",
        "options": [
            {"id": "A", "text": "Infrastructure encryption (double encryption at rest)"},
            {"id": "B", "text": "Secure transfer required"},
            {"id": "C", "text": "Blob versioning"},
            {"id": "D", "text": "A user delegation SAS"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Infrastructure encryption adds a second, independent layer of encryption at the infrastructure "
                       "level on top of the default service-level encryption, so data is encrypted twice with separate keys; it must be enabled when the account is created.",
            "distractors": {
                "B": "Secure transfer required protects data in transit, not a second at-rest encryption layer.",
                "C": "Blob versioning retains previous blob versions; it is not an encryption feature.",
                "D": "A user delegation SAS is an access-granting token, not an encryption layer.",
            },
            "exam_pattern": "Two independent at-rest encryption layers for storage = infrastructure encryption (enable at account creation).",
        },
        "references": ["Microsoft Learn (AZ-500): Enable infrastructure encryption for double encryption"],
    },
    {
        "id": "az500-comp-r2-011", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_storage_security", "difficulty": 2, "type": "mcq",
        "stem": "Your organization must own and control the key that encrypts blob and file data at rest in a "
                "storage account, with the ability to rotate and audit it. What do you configure?",
        "options": [
            {"id": "A", "text": "Customer-managed keys for the storage account, stored in Azure Key Vault"},
            {"id": "B", "text": "Dynamic Data Masking on the account"},
            {"id": "C", "text": "A network security group on the storage subnet"},
            {"id": "D", "text": "A point-to-site VPN"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Configuring customer-managed keys points the storage account's encryption at a key you control "
                       "in Key Vault (or Managed HSM), so you manage rotation, access, and revocation and can audit key use.",
            "distractors": {
                "B": "Dynamic Data Masking is a SQL result-masking feature and does not encrypt storage.",
                "C": "An NSG filters network traffic; it does not control the storage encryption key.",
                "D": "A VPN provides connectivity; it is unrelated to storage encryption keys.",
            },
            "exam_pattern": "Control the storage at-rest encryption key = customer-managed keys in Key Vault (vs Microsoft-managed keys by default).",
        },
        "references": ["Microsoft Learn (AZ-500): Customer-managed keys for Azure Storage encryption"],
    },
    {
        "id": "az500-comp-r2-012", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_storage_security", "difficulty": 2, "type": "mcq",
        "stem": "You want every change to a blob to automatically preserve the prior content as a separate, "
                "recoverable version, so an overwrite can be rolled back. Which storage feature should you "
                "enable?",
        "options": [
            {"id": "A", "text": "Blob versioning"},
            {"id": "B", "text": "A stored access policy"},
            {"id": "C", "text": "Transparent Data Encryption"},
            {"id": "D", "text": "A service endpoint"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Blob versioning automatically keeps previous versions of a blob when it is modified or deleted, "
                       "so you can read or restore an earlier version after an unwanted overwrite.",
            "distractors": {
                "B": "A stored access policy manages SAS constraints; it does not retain blob versions.",
                "C": "TDE encrypts databases at rest; it does not version blobs.",
                "D": "A service endpoint optimizes network pathing to storage; it provides no versioning.",
            },
            "exam_pattern": "Auto-retain previous blob content for rollback = blob versioning (pair with soft delete for deletion recovery).",
        },
        "references": ["Microsoft Learn (AZ-500): Blob versioning"],
    },
    {
        "id": "az500-comp-r2-013", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_storage_security", "difficulty": 3, "type": "mcq",
        "stem": "For compliance you apply a time-based retention policy (immutable WORM) to a blob container "
                "and must guarantee that NO ONE - including administrators - can shorten or remove it during "
                "the retention period. What must you do?",
        "options": [
            {"id": "A", "text": "Leave the policy unlocked so it can be adjusted if needed"},
            {"id": "B", "text": "Lock the time-based retention policy"},
            {"id": "C", "text": "Replace it with a legal hold tag only"},
            {"id": "D", "text": "Apply a ReadOnly resource lock to the storage account"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "An unlocked time-based retention policy is for testing and can be shortened or removed; locking "
                       "the policy makes it immutable so it cannot be shortened or deleted (it can only be extended), meeting WORM compliance.",
            "distractors": {
                "A": "An unlocked policy can still be modified or removed, so it does not guarantee immutability.",
                "C": "A legal hold holds data until the tag is cleared but is not a fixed time-based retention guarantee; the requirement is a locked time-based policy.",
                "D": "A ReadOnly resource lock governs management operations on the resource, not WORM immutability of blob data.",
            },
            "exam_pattern": "Guaranteed WORM immutability = lock the time-based retention policy (unlocked = test only; locked can only be extended).",
        },
        "references": ["Microsoft Learn (AZ-500): Immutable storage - locked vs unlocked time-based retention"],
    },
    {
        "id": "az500-comp-r2-014", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_storage_security", "difficulty": 2, "type": "mcq",
        "stem": "To make sure no container in a storage account can ever be configured for anonymous public "
                "read access, which single account-level setting should you apply?",
        "options": [
            {"id": "A", "text": "Disallow Blob anonymous access at the storage account level"},
            {"id": "B", "text": "Enable blob soft delete"},
            {"id": "C", "text": "Rotate the account keys"},
            {"id": "D", "text": "Enable blob versioning"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Setting 'Allow Blob anonymous access' to Disabled at the account level overrides any "
                       "container-level anonymous settings, guaranteeing no container can be made publicly readable.",
            "distractors": {
                "B": "Soft delete recovers deleted data; it does not prevent anonymous public access.",
                "C": "Rotating keys is credential hygiene and does not disable anonymous access.",
                "D": "Versioning retains prior blob versions; it does not control public access.",
            },
            "exam_pattern": "Guarantee no anonymous blob access = disallow Blob anonymous access at the account (overrides container settings).",
        },
        "references": ["Microsoft Learn (AZ-500): Disallow anonymous public read access to a storage account"],
    },
    {
        "id": "az500-comp-r2-015", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_storage_security", "difficulty": 3, "type": "mcq",
        "stem": "An Azure Files SMB share must authorize cloud-only Microsoft Entra users with NTFS "
                "permissions, and clients should not need line-of-sight to any domain controller. Which "
                "identity source for Azure Files meets this?",
        "options": [
            {"id": "A", "text": "On-premises Active Directory Domain Services (AD DS)"},
            {"id": "B", "text": "Microsoft Entra Kerberos"},
            {"id": "C", "text": "The storage account key for every user"},
            {"id": "D", "text": "A shared access signature per user"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Microsoft Entra Kerberos authentication for Azure Files lets Microsoft Entra ID issue Kerberos "
                       "tickets so Entra-joined clients authenticate to the SMB share without needing network line-of-sight to domain controllers - well suited to cloud-only identities.",
            "distractors": {
                "A": "AD DS requires clients to reach on-premises domain controllers for Kerberos, which the requirement forbids.",
                "C": "Account keys grant full shared-key access with no per-user NTFS identity, defeating identity-based authorization.",
                "D": "A per-user SAS is a token-based grant, not identity-based SMB authentication with NTFS permissions.",
            },
            "exam_pattern": "Azure Files identity-based SMB auth: AD DS, Entra Domain Services, or Entra Kerberos; Entra Kerberos suits cloud-only users with no DC line-of-sight.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Files identity-based authentication (Microsoft Entra Kerberos)"],
    },

    # ----- az500_database_security ----------------------------------------
    {
        "id": "az500-comp-r2-016", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_database_security", "difficulty": 2, "type": "mcq",
        "stem": "Transparent Data Encryption already protects your Azure SQL database at rest, but auditors "
                "now require that your organization own and control the TDE protector key and be able to "
                "revoke it. What should you configure?",
        "options": [
            {"id": "A", "text": "TDE with a customer-managed key (BYOK), with the TDE protector stored in Azure Key Vault"},
            {"id": "B", "text": "Always Encrypted on every column"},
            {"id": "C", "text": "Dynamic Data Masking"},
            {"id": "D", "text": "A storage account firewall"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Switching TDE to a customer-managed key (Bring Your Own Key) stores the TDE protector in Key "
                       "Vault under your control, so you manage rotation and can revoke access to the key, rendering the database inaccessible if needed.",
            "distractors": {
                "B": "Always Encrypted protects specific columns from the engine; it is not the whole-database at-rest key-ownership control the auditors want.",
                "C": "Dynamic Data Masking obscures result data; it does not provide at-rest key ownership.",
                "D": "A storage account firewall controls network access to storage, not the SQL TDE protector key.",
            },
            "exam_pattern": "Own/revoke the TDE encryption key = TDE with customer-managed key (BYOK) in Key Vault; default TDE uses a service-managed key.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure SQL TDE with customer-managed key (BYOK)"],
    },
    {
        "id": "az500-comp-r2-017", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_database_security", "difficulty": 3, "type": "mcq",
        "stem": "Columns are protected with Always Encrypted, but the application now needs to run range "
                "comparisons and LIKE pattern searches on those encrypted columns server-side, and encrypt "
                "existing data in place. Which enhancement enables these richer operations?",
        "options": [
            {"id": "A", "text": "Always Encrypted with secure enclaves"},
            {"id": "B", "text": "Transparent Data Encryption"},
            {"id": "C", "text": "Dynamic Data Masking"},
            {"id": "D", "text": "A read-only replica"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Always Encrypted with secure enclaves lets the engine process encrypted data inside a protected "
                       "memory enclave, enabling pattern matching (LIKE), range comparisons, and in-place encryption while keys stay outside the engine's normal reach.",
            "distractors": {
                "B": "TDE encrypts at rest and leaves plaintext visible to the engine; it does not add enclave-based rich queries on protected columns.",
                "C": "Dynamic Data Masking only masks result output; it does not enable computations over encrypted data.",
                "D": "A read-only replica scales reads; it does not enable rich operations on encrypted columns.",
            },
            "exam_pattern": "Rich queries (range, LIKE) and in-place encryption on Always Encrypted columns = secure enclaves.",
        },
        "references": ["Microsoft Learn (AZ-500): Always Encrypted with secure enclaves"],
    },
    {
        "id": "az500-comp-r2-018", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_database_security", "difficulty": 2, "type": "mcq",
        "stem": "To satisfy a compliance mandate, you must retain a detailed record of database events "
                "(logins, queries, schema changes) from an Azure SQL database and send it to a Log Analytics "
                "workspace for retention and analysis. Which feature do you enable?",
        "options": [
            {"id": "A", "text": "Azure SQL auditing"},
            {"id": "B", "text": "Transparent Data Encryption"},
            {"id": "C", "text": "Dynamic Data Masking"},
            {"id": "D", "text": "A resource lock"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure SQL auditing records database events and can write the audit trail to a Log Analytics "
                       "workspace (or storage account or event hub) for retention, alerting, and compliance reporting.",
            "distractors": {
                "B": "TDE encrypts data at rest; it does not record a database event trail.",
                "C": "Dynamic Data Masking obscures result data; it does not produce an audit log.",
                "D": "A resource lock prevents deletion/modification; it does not audit database activity.",
            },
            "exam_pattern": "Record DB events for compliance to Log Analytics/Storage/Event Hub = Azure SQL auditing.",
        },
        "references": ["Microsoft Learn (AZ-500): Auditing for Azure SQL Database"],
    },
    {
        "id": "az500-comp-r2-019", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_database_security", "difficulty": 3, "type": "mcq",
        "stem": "A review flags that an Azure SQL logical server has 'Allow Azure services and resources to "
                "access this server' enabled, which permits connections from any Azure service IP. To tighten "
                "this to only your own workloads, what is the best action?",
        "options": [
            {"id": "A", "text": "Disable that setting and use a private endpoint (or specific firewall rules) for your workloads"},
            {"id": "B", "text": "Enable Dynamic Data Masking"},
            {"id": "C", "text": "Rotate the server admin password"},
            {"id": "D", "text": "Add a CanNotDelete lock to the server"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The 'Allow Azure services...' toggle is broad because it admits traffic from any Azure "
                       "tenant's services. Turning it off and using a private endpoint (or narrowly scoped firewall rules/VNet rules) restricts access to only your intended workloads.",
            "distractors": {
                "B": "Dynamic Data Masking hides result columns; it does not restrict which networks can connect.",
                "C": "Rotating the admin password is good hygiene but does not narrow the broad network allowance.",
                "D": "A resource lock prevents deletion/modification; it does not change network access.",
            },
            "exam_pattern": "'Allow Azure services' is broad - disable it and use private endpoint or specific firewall/VNet rules for least exposure.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure SQL network access - firewall and 'Allow Azure services'"],
    },
    {
        "id": "az500-comp-r2-020", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_database_security", "difficulty": 3, "type": "mcq",
        "stem": "A financial application must be able to cryptographically prove that historical records in "
                "an Azure SQL database have not been tampered with, even by a database administrator. Which "
                "feature provides this tamper-evidence?",
        "options": [
            {"id": "A", "text": "Azure SQL ledger"},
            {"id": "B", "text": "Transparent Data Encryption"},
            {"id": "C", "text": "Dynamic Data Masking"},
            {"id": "D", "text": "Geo-replication"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure SQL ledger provides tamper-evidence: cryptographic hashing (a Merkle-tree/blockchain-like "
                       "structure) lets you verify that ledger-table data has not been altered, even by a privileged user, supporting trust and audit.",
            "distractors": {
                "B": "TDE encrypts at rest but offers no proof that data was not changed by an authorized user.",
                "C": "Dynamic Data Masking obscures output; it does not provide integrity proof.",
                "D": "Geo-replication provides availability/DR copies; it does not prove tamper-evidence.",
            },
            "exam_pattern": "Cryptographic tamper-evidence/integrity proof for DB records = Azure SQL ledger (updatable/append-only ledger tables).",
        },
        "references": ["Microsoft Learn (AZ-500): Azure SQL Database ledger"],
    },
    {
        "id": "az500-comp-r2-021", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_database_security", "difficulty": 2, "type": "mcq",
        "stem": "Microsoft Defender for SQL's vulnerability assessment keeps flagging a configuration your "
                "team has formally accepted as an approved exception, creating noise. How do you make future "
                "scans treat it as expected and report only new deviations?",
        "options": [
            {"id": "A", "text": "Approve a baseline for the vulnerability assessment so scans report deviations from it"},
            {"id": "B", "text": "Disable Defender for SQL entirely"},
            {"id": "C", "text": "Delete the database and recreate it"},
            {"id": "D", "text": "Turn off auditing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The vulnerability assessment lets you set an approved baseline; once a result is baselined, scans "
                       "treat it as the accepted state and report only deviations, reducing noise while preserving detection of new issues.",
            "distractors": {
                "B": "Disabling Defender for SQL removes all threat protection and assessment, not just the one finding.",
                "C": "Recreating the database is drastic and does not configure the assessment baseline.",
                "D": "Turning off auditing removes the activity record and does not affect the vulnerability assessment baseline.",
            },
            "exam_pattern": "Silence accepted VA findings and alert only on change = approve a vulnerability assessment baseline (Defender for SQL).",
        },
        "references": ["Microsoft Learn (AZ-500): SQL vulnerability assessment baselines in Defender for SQL"],
    },
    {
        "id": "az500-comp-r2-022", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_database_security", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: Dynamic Data ________ obscures sensitive values (for example, showing "
                "only the last four digits of a card number) in query results for unprivileged users, without "
                "changing the data stored in the database.",
        "correct": ["masking"],
        "explanation": {
            "correct": "Dynamic Data Masking is a presentation-layer control that masks results for unprivileged users; "
                       "the underlying data is unchanged and privileged users still see full values, so it is not a substitute for encryption or access control.",
            "exam_pattern": "Result-set obfuscation for unprivileged users, stored data unchanged = Dynamic Data Masking (not encryption).",
        },
        "references": ["Microsoft Learn (AZ-500): Dynamic Data Masking for Azure SQL"],
    },

    # ----- az500_key_vault ------------------------------------------------
    {
        "id": "az500-comp-r2-023", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_key_vault", "difficulty": 2, "type": "mcq",
        "stem": "Using the Azure RBAC permission model for a Key Vault, an application's managed identity "
                "must be able to READ secret values but not create, update, or delete secrets. Which built-in "
                "role should you assign at the vault scope?",
        "options": [
            {"id": "A", "text": "Key Vault Administrator"},
            {"id": "B", "text": "Key Vault Secrets Officer"},
            {"id": "C", "text": "Key Vault Secrets User"},
            {"id": "D", "text": "Key Vault Reader"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Key Vault Secrets User grants read access to secret values (get/list) at the data plane - exactly "
                       "what an app needs to fetch secrets, and no more.",
            "distractors": {
                "A": "Key Vault Administrator grants full data-plane management of keys, secrets, and certificates - far more than reading secrets.",
                "B": "Key Vault Secrets Officer can create, update, and delete secrets, exceeding read-only.",
                "D": "Key Vault Reader grants read access to vault metadata/properties but not to secret values.",
            },
            "exam_pattern": "Read secret values only = Key Vault Secrets User; manage secrets = Secrets Officer; metadata only = Key Vault Reader.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure RBAC built-in roles for Key Vault"],
    },
    {
        "id": "az500-comp-r2-024", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_key_vault", "difficulty": 2, "type": "mcq",
        "stem": "You restrict a Key Vault's firewall to selected virtual networks and IP ranges, but now a "
                "legitimate Azure platform operation (such as ARM template deployment referencing the vault) "
                "is blocked. Which option lets trusted first-party services through without opening the vault "
                "broadly?",
        "options": [
            {"id": "A", "text": "Enable 'Allow trusted Microsoft services to bypass this firewall'"},
            {"id": "B", "text": "Disable soft delete"},
            {"id": "C", "text": "Switch to the access policy model"},
            {"id": "D", "text": "Delete the private endpoint"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The 'Allow trusted Microsoft services to bypass this firewall' option permits a defined set of "
                       "trusted first-party services to reach the vault even when the firewall is restricting network access, without widening the allowed networks.",
            "distractors": {
                "B": "Soft delete governs recoverability of deleted objects; it is unrelated to firewall bypass for trusted services.",
                "C": "Switching permission models changes authorization, not the network firewall's trusted-services exception.",
                "D": "Deleting a private endpoint reduces private connectivity; it does not grant trusted-service firewall bypass.",
            },
            "exam_pattern": "Let first-party Azure services reach a firewalled Key Vault = enable 'Allow trusted Microsoft services to bypass this firewall'.",
        },
        "references": ["Microsoft Learn (AZ-500): Configure Azure Key Vault networking (trusted services)"],
    },
    {
        "id": "az500-comp-r2-025", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_key_vault", "difficulty": 2, "type": "mcq",
        "stem": "To reduce the risk from long-lived cryptographic keys, you want Key Vault to automatically "
                "generate a new version of a key on a defined schedule. What should you configure?",
        "options": [
            {"id": "A", "text": "A key rotation policy on the key"},
            {"id": "B", "text": "Purge protection"},
            {"id": "C", "text": "A stored access policy"},
            {"id": "D", "text": "A diagnostic setting"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A key rotation policy lets Key Vault automatically rotate a key (create a new version) at a set "
                       "interval and notify before expiry, reducing reliance on manual rotation.",
            "distractors": {
                "B": "Purge protection blocks early permanent deletion of vaults/objects; it does not rotate keys.",
                "C": "A stored access policy constrains storage SAS tokens, not Key Vault key rotation.",
                "D": "A diagnostic setting routes logs; it does not rotate keys.",
            },
            "exam_pattern": "Automatic scheduled key rotation = key rotation policy (auto-rotate + near-expiry notification).",
        },
        "references": ["Microsoft Learn (AZ-500): Configure cryptographic key auto-rotation in Key Vault"],
    },
    {
        "id": "az500-comp-r2-026", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_key_vault", "difficulty": 2, "type": "mcq",
        "stem": "A TLS certificate stored in Key Vault keeps expiring and causing outages because nobody "
                "renews it in time. How can Key Vault handle renewal for a certificate issued by an "
                "integrated certificate authority?",
        "options": [
            {"id": "A", "text": "Set a certificate policy with an auto-renewal (lifetime) action"},
            {"id": "B", "text": "Enable blob versioning"},
            {"id": "C", "text": "Store the certificate as a plain secret instead"},
            {"id": "D", "text": "Add a CanNotDelete lock to the vault"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A Key Vault certificate policy can define a lifetime action to automatically renew (or email a "
                       "notification) before expiry; with an integrated CA, Key Vault can renew the certificate automatically.",
            "distractors": {
                "B": "Blob versioning is a storage feature, unrelated to certificate renewal.",
                "C": "Storing it as a plain secret loses the certificate lifecycle management and auto-renewal entirely.",
                "D": "A resource lock prevents deletion/modification; it does not renew certificates.",
            },
            "exam_pattern": "Auto-renew TLS certificates = Key Vault certificate policy with a lifetime/auto-renew action (with an integrated CA).",
        },
        "references": ["Microsoft Learn (AZ-500): Key Vault certificates and auto-renewal policies"],
    },
    {
        "id": "az500-comp-r2-027", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_key_vault", "difficulty": 3, "type": "mcq",
        "stem": "Which statement best distinguishes Azure Key Vault Managed HSM from the Key Vault Premium "
                "tier?",
        "options": [
            {"id": "A", "text": "Managed HSM is single-tenant with a customer-controlled security domain, while Premium is a multi-tenant service that also supports software-protected keys"},
            {"id": "B", "text": "Premium is single-tenant, while Managed HSM is multi-tenant"},
            {"id": "C", "text": "Only Premium can store HSM-protected keys"},
            {"id": "D", "text": "Managed HSM cannot store cryptographic keys"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Managed HSM is a single-tenant service whose security domain (root of trust) the customer "
                       "controls and which stores HSM-protected keys only; the Premium vault is multi-tenant, HSM-backed, and also supports software-protected keys.",
            "distractors": {
                "B": "This is reversed: Managed HSM is single-tenant; Premium (standard Key Vault) is multi-tenant.",
                "C": "Premium stores HSM-backed keys, but Managed HSM also stores HSM-protected keys (only HSM-protected keys, in fact).",
                "D": "Managed HSM is purpose-built to store and manage cryptographic keys in HSMs.",
            },
            "exam_pattern": "Managed HSM = single-tenant, customer-controlled security domain, HSM-only keys; Premium vault = multi-tenant, HSM-backed + software keys.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Key Vault Managed HSM vs Premium vault"],
    },
    {
        "id": "az500-comp-r2-028", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_key_vault", "difficulty": 2, "type": "mcq",
        "stem": "You want an Azure App Service app to pull a connection string from Key Vault at runtime "
                "WITHOUT any Key Vault SDK code in the app, resolving the secret automatically through the "
                "app's managed identity. Which approach does this?",
        "options": [
            {"id": "A", "text": "A Key Vault reference in the app settings (for example @Microsoft.KeyVault(...))"},
            {"id": "B", "text": "Embedding the account key in web.config"},
            {"id": "C", "text": "A stored access policy"},
            {"id": "D", "text": "A service tag rule"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A Key Vault reference in an App Service/Functions app setting (@Microsoft.KeyVault(...)) is "
                       "resolved by the platform using the app's managed identity, so the secret is injected at runtime with no SDK code and no secret in configuration files.",
            "distractors": {
                "B": "Embedding the account key is exactly the hard-coded secret you are trying to avoid.",
                "C": "A stored access policy constrains storage SAS; it does not inject Key Vault secrets into App Service.",
                "D": "A service tag is an NSG/firewall IP construct; it does not retrieve secrets.",
            },
            "exam_pattern": "Inject Key Vault secrets into App Service with no SDK code = Key Vault references resolved by the app's managed identity.",
        },
        "references": ["Microsoft Learn (AZ-500): Use Key Vault references in Azure App Service"],
    },
    {
        "id": "az500-comp-r2-029", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_key_vault", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: Key Vault ________ protection prevents a deleted vault or object from "
                "being permanently removed (purged) before its soft-delete retention period elapses, blocking "
                "immediate malicious destruction.",
        "correct": ["purge"],
        "explanation": {
            "correct": "Soft delete makes deleted vaults/objects recoverable during the retention period, and purge "
                       "protection prevents anyone from permanently purging them early, so an attacker or mistaken admin cannot destroy keys immediately.",
            "exam_pattern": "Soft delete = recover within retention; purge protection = block early permanent deletion until retention elapses.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Key Vault soft delete and purge protection"],
    },

    # ======================================================================
    # DOMAIN 4 - Manage Security Operations (az500_security_operations)
    # ======================================================================

    # ----- az500_defender_for_cloud ---------------------------------------
    {
        "id": "az500-ops-r2-001", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_defender_for_cloud", "difficulty": 2, "type": "mcq",
        "stem": "In Microsoft Defender for Cloud, a security recommendation offers a 'Fix' button. What does "
                "using it accomplish, and how does it relate to Secure Score?",
        "options": [
            {"id": "A", "text": "It applies the remediation to the affected resources, and completing recommendations raises your Secure Score"},
            {"id": "B", "text": "It permanently deletes the noncompliant resource"},
            {"id": "C", "text": "It lowers your Secure Score as a penalty"},
            {"id": "D", "text": "It only emails the recommendation and changes nothing"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Fix action applies the recommended remediation to the unhealthy resources; as "
                       "recommendations within a security control are completed, your Secure Score increases (controls are weighted).",
            "distractors": {
                "B": "Fix remediates configuration; it does not delete the resource.",
                "C": "Remediating raises, not lowers, Secure Score; unaddressed recommendations keep it low.",
                "D": "Fix performs the remediation rather than merely notifying.",
            },
            "exam_pattern": "Remediate recommendations (manually or via Fix) to raise Secure Score; score is grouped into weighted security controls.",
        },
        "references": ["Microsoft Learn (AZ-500): Remediate security recommendations in Defender for Cloud"],
    },
    {
        "id": "az500-ops-r2-002", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_defender_for_cloud", "difficulty": 3, "type": "mcq",
        "stem": "When a specific Defender for Cloud security alert fires, you want to automatically run a "
                "custom response - for example, open a ticket and quarantine a resource - built as a Logic "
                "App. Which Defender for Cloud feature triggers it?",
        "options": [
            {"id": "A", "text": "Workflow automation"},
            {"id": "B", "text": "Secure Score"},
            {"id": "C", "text": "The regulatory compliance dashboard"},
            {"id": "D", "text": "Just-in-time VM access"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Workflow automation in Defender for Cloud triggers a Logic App when alerts or recommendations "
                       "matching your criteria occur, enabling automated responses such as ticketing or remediation.",
            "distractors": {
                "B": "Secure Score measures posture; it does not trigger automated workflows.",
                "C": "The regulatory compliance dashboard maps posture to standards; it does not run response workflows.",
                "D": "JIT VM access time-boxes management-port exposure; it is not an alert-triggered automation engine.",
            },
            "exam_pattern": "Auto-run a Logic App on a Defender for Cloud alert/recommendation = workflow automation.",
        },
        "references": ["Microsoft Learn (AZ-500): Workflow automation in Microsoft Defender for Cloud"],
    },
    {
        "id": "az500-ops-r2-003", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_defender_for_cloud", "difficulty": 2, "type": "mcq",
        "stem": "Your organization runs workloads in AWS and Google Cloud as well as Azure, and wants a "
                "single posture-management and recommendations view across all three in Microsoft Defender "
                "for Cloud. What do you configure?",
        "options": [
            {"id": "A", "text": "Connect the AWS and GCP accounts using Defender for Cloud's multicloud connectors"},
            {"id": "B", "text": "Deploy a VPN gateway to each cloud"},
            {"id": "C", "text": "Create a private endpoint in each cloud"},
            {"id": "D", "text": "Enable blob soft delete"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Defender for Cloud provides native multicloud connectors for AWS and GCP; connecting those "
                       "accounts brings their resources into Defender for Cloud for posture assessment, recommendations, and (optionally) workload protection.",
            "distractors": {
                "B": "A VPN provides network connectivity, not Defender for Cloud multicloud onboarding.",
                "C": "Private endpoints give private access to a PaaS resource; they do not onboard other clouds.",
                "D": "Blob soft delete is storage data protection, unrelated to multicloud posture.",
            },
            "exam_pattern": "Assess AWS/GCP alongside Azure in Defender for Cloud = native multicloud connectors (AWS/GCP).",
        },
        "references": ["Microsoft Learn (AZ-500): Connect AWS and GCP accounts to Microsoft Defender for Cloud"],
    },
    {
        "id": "az500-ops-r2-004", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_defender_for_cloud", "difficulty": 2, "type": "mcq",
        "stem": "In Microsoft Defender for Cloud, what is the key difference between a security "
                "'recommendation' and a security 'alert'?",
        "options": [
            {"id": "A", "text": "A recommendation identifies a posture/configuration weakness to harden (CSPM); an alert indicates an active or attempted threat detected on a resource (CWPP)"},
            {"id": "B", "text": "They are identical and interchangeable"},
            {"id": "C", "text": "A recommendation is an active attack; an alert is a hardening suggestion"},
            {"id": "D", "text": "Alerts only appear in the activity log, never in Defender for Cloud"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Recommendations are posture-management findings (fix a misconfiguration to reduce risk), while "
                       "alerts are produced by the workload protection plans when a threat or suspicious activity is detected on a resource.",
            "distractors": {
                "B": "They serve different purposes - posture hardening vs threat detection - and are not interchangeable.",
                "C": "This reverses the definitions; recommendations harden posture and alerts flag active threats.",
                "D": "Security alerts are surfaced in Defender for Cloud (and can be exported to Sentinel), not only the activity log.",
            },
            "exam_pattern": "Recommendation = posture/CSPM hardening; alert = active threat detection/CWPP (mapped to MITRE ATT&CK).",
        },
        "references": ["Microsoft Learn (AZ-500): Security alerts and recommendations in Defender for Cloud"],
    },
    {
        "id": "az500-ops-r2-005", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_defender_for_cloud", "difficulty": 2, "type": "mcq",
        "stem": "You must continuously stream Defender for Cloud security alerts and recommendations to a "
                "Log Analytics workspace and to an Event Hub that feeds a third-party SIEM. Which feature do "
                "you use?",
        "options": [
            {"id": "A", "text": "Continuous export"},
            {"id": "B", "text": "A resource lock"},
            {"id": "C", "text": "Just-in-time VM access"},
            {"id": "D", "text": "Adaptive application controls"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Continuous export streams Defender for Cloud alerts, recommendations, Secure Score, and more to "
                       "a Log Analytics workspace or Event Hub, which is the standard way to feed an external SIEM or long-term store.",
            "distractors": {
                "B": "A resource lock prevents deletion/modification; it does not export security data.",
                "C": "JIT VM access manages port exposure; it is not a data export mechanism.",
                "D": "Adaptive application controls allowlist applications; they do not export alerts/recommendations.",
            },
            "exam_pattern": "Stream Defender for Cloud alerts/recommendations to Log Analytics or Event Hub (for a SIEM) = continuous export.",
        },
        "references": ["Microsoft Learn (AZ-500): Continuous export of Defender for Cloud data"],
    },
    {
        "id": "az500-ops-r2-006", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_defender_for_cloud", "difficulty": 2, "type": "mcq",
        "stem": "By default, which security standard does Microsoft Defender for Cloud apply to generate the "
                "baseline set of security recommendations for your Azure resources?",
        "options": [
            {"id": "A", "text": "PCI DSS"},
            {"id": "B", "text": "The Microsoft Cloud Security Benchmark (MCSB)"},
            {"id": "C", "text": "ISO 27001 only"},
            {"id": "D", "text": "A custom initiative you must author first"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The Microsoft Cloud Security Benchmark is applied by default and drives the default security "
                       "recommendations and Secure Score; you can add other standards (PCI DSS, ISO 27001, etc.) to the compliance dashboard.",
            "distractors": {
                "A": "PCI DSS is an optional standard you add to the compliance dashboard, not the applied default.",
                "C": "ISO 27001 is also optional to add; it is not the default baseline.",
                "D": "You do not need to author a custom initiative first - MCSB is applied out of the box.",
            },
            "exam_pattern": "Defender for Cloud's default applied standard = Microsoft Cloud Security Benchmark (MCSB); add others for compliance mapping.",
        },
        "references": ["Microsoft Learn (AZ-500): Microsoft Cloud Security Benchmark in Defender for Cloud"],
    },
    {
        "id": "az500-ops-r2-007", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_defender_for_cloud", "difficulty": 3, "type": "mcq",
        "stem": "You need threat detection for suspicious control-plane (management) operations against Azure "
                "Resource Manager - for example, anomalous or risky resource-management activity from a "
                "compromised account or toolkit. Which Defender plan targets this?",
        "options": [
            {"id": "A", "text": "Microsoft Defender for Resource Manager"},
            {"id": "B", "text": "Microsoft Defender for Storage"},
            {"id": "C", "text": "Microsoft Defender for Key Vault"},
            {"id": "D", "text": "Microsoft Defender for Containers"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Defender for Resource Manager monitors the Azure Resource Manager control plane and "
                       "alerts on suspicious or anomalous resource-management operations, such as those from known attack toolkits or risky patterns.",
            "distractors": {
                "B": "Defender for Storage detects threats to storage accounts (malware uploads, anomalous access), not ARM control-plane operations.",
                "C": "Defender for Key Vault detects anomalous vault access, not ARM management-layer threats.",
                "D": "Defender for Containers protects registry images and Kubernetes runtime, not the ARM control plane.",
            },
            "exam_pattern": "Threat detection for the Azure Resource Manager control/management plane = Defender for Resource Manager (match the plan to the resource layer).",
        },
        "references": ["Microsoft Learn (AZ-500): Microsoft Defender for Resource Manager"],
    },
    {
        "id": "az500-ops-r2-008", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_defender_for_cloud", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: CSPM, the Defender for Cloud pillar focused on assessing configuration, "
                "producing recommendations, and driving Secure Score, stands for cloud security ________ "
                "management.",
        "correct": ["posture"],
        "explanation": {
            "correct": "Cloud security posture management (CSPM) covers inventory, recommendations, Secure Score, and "
                       "(in the paid Defender CSPM plan) attack path analysis and the cloud security explorer; workload protection (CWPP) is the threat-detection side.",
            "exam_pattern": "CSPM = cloud security posture management (hardening/Secure Score); CWPP = cloud workload protection (threat alerts).",
        },
        "references": ["Microsoft Learn (AZ-500): Cloud security posture management (CSPM) in Defender for Cloud"],
    },

    # ----- az500_sentinel_ops ---------------------------------------------
    {
        "id": "az500-ops-r2-009", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_sentinel_ops", "difficulty": 3, "type": "mcq",
        "stem": "A detection must run as close to real time as possible, firing within roughly a minute of "
                "the data arriving rather than on a longer schedule. Which Microsoft Sentinel analytics rule "
                "type should you use?",
        "options": [
            {"id": "A", "text": "A near-real-time (NRT) rule"},
            {"id": "B", "text": "A scheduled rule that runs once per day"},
            {"id": "C", "text": "An anomaly rule"},
            {"id": "D", "text": "A workbook"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Near-real-time (NRT) rules are a limited subset of scheduled rules designed to run about once a "
                       "minute, giving the fastest Sentinel detection for time-sensitive scenarios.",
            "distractors": {
                "B": "A daily scheduled rule introduces up to a day of latency - far from near real time.",
                "C": "Anomaly rules apply ML to baseline behavior over time; they are not the minute-level detection mechanism.",
                "D": "A workbook visualizes data; it does not run detections.",
            },
            "exam_pattern": "Fastest (~1-minute) Sentinel detection = near-real-time (NRT) rule; standard detection = scheduled rule.",
        },
        "references": ["Microsoft Learn (AZ-500): Near-real-time (NRT) analytics rules in Microsoft Sentinel"],
    },
    {
        "id": "az500-ops-r2-010", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_sentinel_ops", "difficulty": 3, "type": "mcq",
        "stem": "You want Microsoft Sentinel to automatically correlate multiple low-fidelity alerts and "
                "anomalies across products into a single high-fidelity, multistage attack incident using "
                "machine learning, enabled by default. Which capability is this?",
        "options": [
            {"id": "A", "text": "Fusion (multistage attack detection)"},
            {"id": "B", "text": "A watchlist"},
            {"id": "C", "text": "A single scheduled rule"},
            {"id": "D", "text": "A hunting query"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Fusion is Sentinel's built-in, ML-based multistage attack detection; it correlates signals and "
                       "alerts (including from scheduled rules and other products) into high-fidelity incidents and is enabled by default.",
            "distractors": {
                "B": "A watchlist is reference data for use in queries/rules; it does not correlate alerts into incidents.",
                "C": "A single scheduled rule evaluates one query; it does not perform cross-product ML correlation.",
                "D": "A hunting query proactively searches data; it is not automated multistage correlation.",
            },
            "exam_pattern": "ML correlation of low-fidelity signals into multistage attack incidents = Fusion (on by default).",
        },
        "references": ["Microsoft Learn (AZ-500): Multistage attack detection (Fusion) in Microsoft Sentinel"],
    },
    {
        "id": "az500-ops-r2-011", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_sentinel_ops", "difficulty": 2, "type": "mcq",
        "stem": "You want Microsoft Sentinel to baseline normal behavior for users and devices and flag "
                "deviations (such as a user suddenly accessing resources they never touch) as a risk signal "
                "for investigation. Which capability provides this?",
        "options": [
            {"id": "A", "text": "User and entity behavior analytics (UEBA)"},
            {"id": "B", "text": "Data connectors"},
            {"id": "C", "text": "Workbooks"},
            {"id": "D", "text": "A stored access policy"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "UEBA in Sentinel builds behavioral baselines for users and entities and surfaces anomalous "
                       "activity and entity insights, enriching investigations with behavior-based risk.",
            "distractors": {
                "B": "Data connectors ingest sources; they do not perform behavioral analytics.",
                "C": "Workbooks visualize data; they do not baseline entity behavior.",
                "D": "A stored access policy is a storage SAS control, unrelated to Sentinel UEBA.",
            },
            "exam_pattern": "Behavioral baselining of users/entities to flag anomalies = UEBA in Microsoft Sentinel.",
        },
        "references": ["Microsoft Learn (AZ-500): User and entity behavior analytics (UEBA) in Microsoft Sentinel"],
    },
    {
        "id": "az500-ops-r2-012", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_sentinel_ops", "difficulty": 2, "type": "mcq",
        "stem": "Analysts need to import a curated list of VIP executive accounts and reference it inside "
                "analytics rules and hunting queries in Microsoft Sentinel. Which feature stores this "
                "reference data?",
        "options": [
            {"id": "A", "text": "A watchlist"},
            {"id": "B", "text": "A playbook"},
            {"id": "C", "text": "A data connector"},
            {"id": "D", "text": "An automation rule"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A watchlist imports and stores reference data (such as VIP users or approved IP ranges) that you "
                       "can join to or filter by in analytics rules, hunting queries, and investigations.",
            "distractors": {
                "B": "A playbook is an automated response workflow (Logic App), not reference data storage.",
                "C": "A data connector ingests log sources; it is not a curated reference list.",
                "D": "An automation rule orchestrates incident handling; it does not store reference lists.",
            },
            "exam_pattern": "Curated reference data (VIPs, allow-lists) for use in rules/hunts = a Sentinel watchlist.",
        },
        "references": ["Microsoft Learn (AZ-500): Use watchlists in Microsoft Sentinel"],
    },
    {
        "id": "az500-ops-r2-013", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_sentinel_ops", "difficulty": 3, "type": "mcq",
        "stem": "Your SOC subscribes to a feed of malicious IPs, domains, and file hashes. You want Microsoft "
                "Sentinel to ingest these indicators of compromise and automatically raise alerts when they "
                "appear in your logs. What do you use?",
        "options": [
            {"id": "A", "text": "Threat intelligence (import indicators via a TI connector), with Microsoft Sentinel analytics rules that match them"},
            {"id": "B", "text": "A workbook"},
            {"id": "C", "text": "A stored access policy"},
            {"id": "D", "text": "A diagnostic setting"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Sentinel threat intelligence ingests indicators of compromise (via connectors such as TAXII or "
                       "the Defender TI/Upload API) and the built-in TI-matching analytics rules raise alerts when those indicators appear in ingested data.",
            "distractors": {
                "B": "A workbook visualizes data; it does not ingest or match threat-intel indicators.",
                "C": "A stored access policy is a storage SAS control, unrelated to Sentinel threat intelligence.",
                "D": "A diagnostic setting routes logs; it does not import indicators or match them.",
            },
            "exam_pattern": "Ingest IOCs and alert on matches in Sentinel = threat intelligence (TI connector) + TI-matching analytics rules.",
        },
        "references": ["Microsoft Learn (AZ-500): Threat intelligence in Microsoft Sentinel"],
    },
    {
        "id": "az500-ops-r2-014", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_sentinel_ops", "difficulty": 2, "type": "mcq",
        "stem": "An analyst proactively searches Microsoft Sentinel data with KQL for suspicious patterns "
                "before any alert fires, and wants to mark noteworthy findings to pin and revisit during an "
                "investigation. Which TWO Sentinel capabilities support this workflow?",
        "options": [
            {"id": "A", "text": "Hunting queries and bookmarks"},
            {"id": "B", "text": "Playbooks and automation rules"},
            {"id": "C", "text": "Data connectors and watchlists"},
            {"id": "D", "text": "Workbooks and dashboards"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Hunting queries let analysts proactively search data with KQL before alerts exist, and bookmarks "
                       "let them preserve and annotate interesting query results to revisit or promote into an incident.",
            "distractors": {
                "B": "Playbooks and automation rules automate response to incidents; they are not the proactive hunt + bookmark workflow.",
                "C": "Data connectors ingest data and watchlists store reference data; neither is the hunt-and-bookmark pairing.",
                "D": "Workbooks and dashboards visualize data; they do not provide hunting bookmarks.",
            },
            "exam_pattern": "Proactive KQL threat hunting + preserving findings = hunting queries and bookmarks.",
        },
        "references": ["Microsoft Learn (AZ-500): Hunt for threats and use bookmarks in Microsoft Sentinel"],
    },
    {
        "id": "az500-ops-r2-015", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_sentinel_ops", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: A Microsoft Sentinel ________ provides interactive dashboards and "
                "visualizations over workspace data (built on Azure Monitor's visualization feature), helping "
                "you monitor and present security data.",
        "correct": ["workbook"],
        "explanation": {
            "correct": "Workbooks are interactive, customizable visual reports over Log Analytics data; they visualize "
                       "and monitor data but do not generate alerts or run response actions.",
            "exam_pattern": "Sentinel visualization/dashboards = workbooks; detections = analytics rules; response = playbooks/automation rules.",
        },
        "references": ["Microsoft Learn (AZ-500): Visualize data with Microsoft Sentinel workbooks"],
    },

    # ----- az500_monitoring_logging ---------------------------------------
    {
        "id": "az500-ops-r2-016", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_monitoring_logging", "difficulty": 2, "type": "mcq",
        "stem": "You are collecting guest-OS logs and performance data from Azure VMs into a Log Analytics "
                "workspace. The legacy Log Analytics agent (MMA) is retired. Which current agent and "
                "configuration object should you use?",
        "options": [
            {"id": "A", "text": "The Azure Monitor Agent (AMA), configured with data collection rules (DCRs)"},
            {"id": "B", "text": "The Log Analytics agent configured with a workspace key"},
            {"id": "C", "text": "A network security group with flow logs"},
            {"id": "D", "text": "A stored access policy"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Azure Monitor Agent replaced the retired Log Analytics/MMA agent; it uses data collection "
                       "rules (DCRs) to define what to collect and where to send it, giving targeted, flexible collection.",
            "distractors": {
                "B": "The Log Analytics agent (MMA) is retired; new collection should use AMA with DCRs.",
                "C": "NSG flow logs capture network flows, not guest-OS logs/metrics.",
                "D": "A stored access policy is a storage SAS control, unrelated to agent-based collection.",
            },
            "exam_pattern": "Current VM log/metric collection = Azure Monitor Agent (AMA) + data collection rules (DCRs); the MMA/Log Analytics agent is retired.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Monitor Agent and data collection rules"],
    },
    {
        "id": "az500-ops-r2-017", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_monitoring_logging", "difficulty": 2, "type": "multi",
        "stem": "When an Azure Monitor alert fires, an action group carries out the response. Which TWO of "
                "the following can an action group do? (Choose two.)",
        "options": [
            {"id": "A", "text": "Send an email or SMS notification"},
            {"id": "B", "text": "Trigger a Logic App, Azure Function, or Automation runbook"},
            {"id": "C", "text": "Encrypt a virtual machine's OS disk"},
            {"id": "D", "text": "Create a user-defined route"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Action groups notify (email, SMS, push, voice) and take action (webhook, Logic App, Azure "
                       "Function, Automation runbook, Event Hub, ITSM), so you can both alert people and trigger automated responses.",
            "distractors": {
                "C": "Encrypting a disk is a compute/storage configuration task, not an action-group action.",
                "D": "Creating a UDR is a networking configuration action, not something an action group performs.",
            },
            "exam_pattern": "Action group = notifications (email/SMS/push/voice) + actions (webhook/Logic App/Function/runbook/Event Hub/ITSM).",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Monitor action groups"],
    },
    {
        "id": "az500-ops-r2-018", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_monitoring_logging", "difficulty": 3, "type": "mcq",
        "stem": "You ingest very high-volume, verbose firewall logs that you rarely query interactively and "
                "mostly use for occasional investigation. To cut ingestion cost while still storing them, "
                "which Log Analytics table plan should you choose for that table?",
        "options": [
            {"id": "A", "text": "The Basic logs plan"},
            {"id": "B", "text": "The Analytics (interactive) plan"},
            {"id": "C", "text": "Disable the table entirely"},
            {"id": "D", "text": "Store them only in Key Vault"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Basic logs plan offers lower-cost ingestion for high-volume, verbose data at the expense of "
                       "full interactive analytics features, which suits logs you query only occasionally for investigation.",
            "distractors": {
                "B": "The Analytics plan gives full query/alerting but costs more per GB - overkill for rarely queried verbose logs.",
                "C": "Disabling the table loses the data you still need for investigations.",
                "D": "Key Vault stores secrets/keys/certificates, not bulk log tables.",
            },
            "exam_pattern": "High-volume, rarely queried logs = Basic logs plan (cheaper ingestion, limited query); rich analytics = Analytics plan.",
        },
        "references": ["Microsoft Learn (AZ-500): Log Analytics table plans (Analytics vs Basic)"],
    },
    {
        "id": "az500-ops-r2-019", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_monitoring_logging", "difficulty": 2, "type": "mcq",
        "stem": "A compliance mandate requires security logs in a Log Analytics workspace to be retained for "
                "seven years at the lowest cost, while only the most recent 90 days need fast interactive "
                "query. How should you configure retention?",
        "options": [
            {"id": "A", "text": "Set a short interactive retention period and enable long-term archive for the remaining years"},
            {"id": "B", "text": "Keep all seven years in interactive retention"},
            {"id": "C", "text": "Export the logs to Key Vault"},
            {"id": "D", "text": "Disable retention after 90 days"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A Log Analytics table supports interactive retention plus long-term archive; keep ~90 days "
                       "interactive for fast query and archive the rest (up to years) at lower cost, running search jobs or restores when needed.",
            "distractors": {
                "B": "Keeping all seven years interactive is far more expensive than archiving older data.",
                "C": "Key Vault is for secrets/keys/certificates, not multi-year log retention.",
                "D": "Disabling retention after 90 days deletes the data, violating the seven-year requirement.",
            },
            "exam_pattern": "Long cheap retention + short fast query = interactive retention + long-term archive on the Log Analytics table.",
        },
        "references": ["Microsoft Learn (AZ-500): Configure data retention and archive in Log Analytics"],
    },
    {
        "id": "az500-ops-r2-020", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_monitoring_logging", "difficulty": 2, "type": "mcq",
        "stem": "Traffic to a VM is being dropped and you need to confirm whether an NSG rule is allowing or "
                "denying a specific source/destination/port, and see the effective security rules on the NIC. "
                "Which tool helps you diagnose this?",
        "options": [
            {"id": "A", "text": "Azure Network Watcher (IP flow verify and effective security rules)"},
            {"id": "B", "text": "Azure Key Vault"},
            {"id": "C", "text": "Microsoft Sentinel watchlists"},
            {"id": "D", "text": "A stored access policy"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Network Watcher's IP flow verify tells you whether a given 5-tuple is allowed or denied and which "
                       "rule decides it, and effective security rules shows the combined NSG rules applied to a NIC - ideal for diagnosing blocked traffic.",
            "distractors": {
                "B": "Key Vault stores secrets/keys/certificates; it does not diagnose network rules.",
                "C": "Sentinel watchlists store reference data, not NSG rule diagnostics.",
                "D": "A stored access policy is a storage SAS control, unrelated to network diagnostics.",
            },
            "exam_pattern": "Diagnose NSG allow/deny and effective rules = Azure Network Watcher (IP flow verify, effective security rules).",
        },
        "references": ["Microsoft Learn (AZ-500): Diagnose network traffic with Azure Network Watcher"],
    },
    {
        "id": "az500-ops-r2-021", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_monitoring_logging", "difficulty": 2, "type": "mcq",
        "stem": "You must stream a resource's platform logs in near real time to a non-Azure (third-party) "
                "SIEM that ingests from a streaming endpoint. In the resource's diagnostic setting, which "
                "destination do you select?",
        "options": [
            {"id": "A", "text": "An event hub"},
            {"id": "B", "text": "A Key Vault"},
            {"id": "C", "text": "A network security group"},
            {"id": "D", "text": "A route table"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A diagnostic setting can send platform logs/metrics to a Log Analytics workspace, a storage "
                       "account, or an event hub; an event hub is the streaming destination used to forward to non-Azure SIEMs and other external consumers.",
            "distractors": {
                "B": "Key Vault is not a diagnostic-setting destination; it stores secrets/keys/certificates.",
                "C": "An NSG filters traffic; it is not a log destination.",
                "D": "A route table directs routing; it cannot receive diagnostic logs.",
            },
            "exam_pattern": "Diagnostic setting destinations = Log Analytics, Storage, Event Hub; stream to an external SIEM via Event Hub.",
        },
        "references": ["Microsoft Learn (AZ-500): Diagnostic settings destinations (event hub for SIEM)"],
    },
    {
        "id": "az500-ops-r2-022", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_monitoring_logging", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: The Azure ________ log records subscription-level control-plane "
                "(management) operations - who created, updated, or deleted a resource, and when - and is "
                "distinct from a resource's data-plane logs.",
        "correct": ["activity"],
        "explanation": {
            "correct": "The Azure activity log captures control-plane operations at the subscription level; data-plane "
                       "operations within a resource are captured by that resource's logs via diagnostic settings.",
            "exam_pattern": "Control-plane (who did what to a resource) = Azure activity log; data-plane = resource logs via diagnostic settings.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Monitor activity log"],
    },

    # ----- az500_governance_policy ----------------------------------------
    {
        "id": "az500-ops-r2-023", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_governance_policy", "difficulty": 3, "type": "mcq",
        "stem": "You want Azure Policy to automatically deploy a diagnostic setting to any resource that "
                "lacks one, bringing it into compliance after creation. Which effect do you use, and what "
                "does the assignment require?",
        "options": [
            {"id": "A", "text": "DeployIfNotExists, which requires a managed identity for remediation"},
            {"id": "B", "text": "Deny, which blocks the resource outright"},
            {"id": "C", "text": "Audit, which only records noncompliance"},
            {"id": "D", "text": "Disabled, which turns the policy off"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "DeployIfNotExists (DINE) deploys a related resource (here a diagnostic setting) when it is "
                       "missing; because it makes changes, the assignment needs a managed identity (with appropriate roles) to perform the remediation.",
            "distractors": {
                "B": "Deny blocks noncompliant creations; it does not deploy a missing related resource.",
                "C": "Audit only logs noncompliance; it does not deploy anything.",
                "D": "Disabled turns the policy off, so nothing is evaluated or deployed.",
            },
            "exam_pattern": "Auto-deploy a missing related resource for compliance = DeployIfNotExists (needs a managed identity + remediation task).",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Policy DeployIfNotExists effect"],
    },
    {
        "id": "az500-ops-r2-024", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_governance_policy", "difficulty": 2, "type": "mcq",
        "stem": "To enforce a tagging standard, you want Azure Policy to add or update a required cost-center "
                "tag on resources during creation or update, rather than just flagging the missing tag. Which "
                "effect does this?",
        "options": [
            {"id": "A", "text": "Modify"},
            {"id": "B", "text": "Audit"},
            {"id": "C", "text": "Deny"},
            {"id": "D", "text": "Disabled"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Modify effect adds, updates, or removes properties or tags (such as applying the cost-center "
                       "tag) on create/update, and like DeployIfNotExists it needs a managed identity to remediate existing resources.",
            "distractors": {
                "B": "Audit only records the missing tag; it does not add it.",
                "C": "Deny blocks the noncompliant resource rather than fixing the tag.",
                "D": "Disabled turns the policy off, so it does nothing.",
            },
            "exam_pattern": "Add/update tags or properties via policy = Modify effect (needs a managed identity); Append can add but Modify also updates/removes.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Policy Modify effect"],
    },
    {
        "id": "az500-ops-r2-025", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_governance_policy", "difficulty": 2, "type": "mcq",
        "stem": "You want to report (not block) any VM that does NOT have an associated required extension or "
                "related resource, so you can see which machines are missing it. Which Azure Policy effect "
                "fits?",
        "options": [
            {"id": "A", "text": "AuditIfNotExists"},
            {"id": "B", "text": "Deny"},
            {"id": "C", "text": "Append"},
            {"id": "D", "text": "Modify"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "AuditIfNotExists evaluates whether a related resource (such as an extension) exists and marks the "
                       "resource noncompliant (audit) when it is missing, without blocking or changing anything.",
            "distractors": {
                "B": "Deny blocks creation; it does not simply report the missing related resource.",
                "C": "Append adds fields to the request; it does not audit the absence of a related resource.",
                "D": "Modify changes properties/tags; it does not just report missing related resources.",
            },
            "exam_pattern": "Report when a related resource/config is missing = AuditIfNotExists; deploy it = DeployIfNotExists.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Policy AuditIfNotExists effect"],
    },
    {
        "id": "az500-ops-r2-026", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_governance_policy", "difficulty": 3, "type": "mcq",
        "stem": "A DeployIfNotExists policy was assigned after many noncompliant resources already existed. "
                "The new policy does not retroactively fix them. What do you run to bring the existing "
                "resources into compliance?",
        "options": [
            {"id": "A", "text": "A remediation task (using the assignment's managed identity)"},
            {"id": "B", "text": "A resource lock"},
            {"id": "C", "text": "A new management group"},
            {"id": "D", "text": "A diagnostic setting"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "DeployIfNotExists/Modify policies only act on new or updated resources by default; a remediation "
                       "task applies the effect to existing resources, using the assignment's managed identity to make the changes.",
            "distractors": {
                "B": "A resource lock prevents deletion/modification; it does not remediate policy compliance.",
                "C": "A management group organizes subscriptions; it does not run remediation.",
                "D": "A diagnostic setting routes logs; it does not remediate existing noncompliant resources.",
            },
            "exam_pattern": "Bring pre-existing resources into compliance for DINE/Modify = run a remediation task (managed identity applies the change).",
        },
        "references": ["Microsoft Learn (AZ-500): Remediate noncompliant resources with Azure Policy"],
    },
    {
        "id": "az500-ops-r2-027", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_governance_policy", "difficulty": 3, "type": "mcq",
        "stem": "One legacy resource legitimately cannot meet a policy assigned at the subscription, and you "
                "must suppress its noncompliance for that specific resource with a documented justification "
                "and an expiration date - without weakening the policy elsewhere. What do you create?",
        "options": [
            {"id": "A", "text": "A policy exemption scoped to that resource"},
            {"id": "B", "text": "A ReadOnly resource lock"},
            {"id": "C", "text": "A new initiative"},
            {"id": "D", "text": "A deny assignment"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A policy exemption excludes a specific scope or resource from evaluation of an assignment, with a "
                       "category (waiver/mitigated), optional expiration, and justification - so one resource is exempt while the policy still applies everywhere else.",
            "distractors": {
                "B": "A resource lock prevents deletion/modification; it does not exempt a resource from a policy.",
                "C": "Creating an initiative bundles policies; it does not exempt a single resource.",
                "D": "A deny assignment blocks actions on resources; it is not a policy-compliance exemption.",
            },
            "exam_pattern": "Suppress a single resource's policy noncompliance with justification/expiry = a policy exemption.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Policy exemptions"],
    },
    {
        "id": "az500-ops-r2-028", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_governance_policy", "difficulty": 2, "type": "mcq",
        "stem": "You must prevent ALL changes - including configuration updates, not just deletion - to a "
                "production resource while you investigate an incident. Which resource lock do you apply?",
        "options": [
            {"id": "A", "text": "A CanNotDelete lock"},
            {"id": "B", "text": "A ReadOnly lock"},
            {"id": "C", "text": "An Azure Policy Audit effect"},
            {"id": "D", "text": "A network security group"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A ReadOnly lock blocks all modifications and deletion, allowing only read operations - stronger "
                       "than CanNotDelete, which still permits configuration changes. ReadOnly matches the 'no changes at all' requirement.",
            "distractors": {
                "A": "A CanNotDelete lock blocks deletion but still allows configuration changes, so it does not fully freeze the resource.",
                "C": "An Audit policy only reports noncompliance; it does not block changes.",
                "D": "An NSG filters network traffic; it does not prevent resource modification.",
            },
            "exam_pattern": "Block all changes (read-only) = ReadOnly lock; block only deletion but allow changes = CanNotDelete lock.",
        },
        "references": ["Microsoft Learn (AZ-500): Lock resources - ReadOnly vs CanNotDelete"],
    },
    {
        "id": "az500-ops-r2-029", "exam": "az500", "domain": "az500_security_operations",
        "subtopic": "az500_governance_policy", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: The Azure Policy ________ (such as Deny, Audit, Modify, or "
                "DeployIfNotExists) determines what happens when a resource does not satisfy the policy rule.",
        "correct": ["effect"],
        "explanation": {
            "correct": "The effect defines the policy's behavior on a noncompliant resource - from auditing to blocking "
                       "to remediating - and some effects (Modify, DeployIfNotExists) require a managed identity to remediate.",
            "exam_pattern": "Azure Policy effect = what happens on noncompliance (Deny/Audit/Append/Modify/DeployIfNotExists/AuditIfNotExists/Disabled/Manual/DenyAction).",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Policy definition effects"],
    },
]
