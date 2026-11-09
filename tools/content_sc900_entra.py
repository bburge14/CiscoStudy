"""Microsoft SC-900 pool - Domain 2: Capabilities of Microsoft Entra.

Original, objective-aligned practice items for the four Microsoft Entra
subtopics tracked in CertLab:
  * sc9_entra_identity_types       - Microsoft Entra ID (formerly Azure AD);
                                     user, group, device, and workload
                                     identities (service principals and managed
                                     identities); external identities (B2B).
  * sc9_entra_authentication       - passwords, multifactor authentication,
                                     passwordless methods (Windows Hello, FIDO2,
                                     Microsoft Authenticator), and self-service
                                     password reset (SSPR).
  * sc9_entra_access_management    - Conditional Access (signals -> decision ->
                                     enforcement); role-based access control and
                                     Entra built-in roles.
  * sc9_entra_identity_protection  - Microsoft Entra ID Protection (risk-based
                                     policies); Entra ID Governance (entitlement
                                     management, access reviews, Privileged
                                     Identity Management); Verified ID;
                                     Permissions Management.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the key authored as "A" is not positionally
biased, every wrong option carries a distractor note, and each item cites the
Microsoft Learn (SC-900) area. Current product names are used throughout:
Microsoft Entra ID (formerly Azure Active Directory / Azure AD). Fundamentals
depth only - which capability fits a need; no numeric limits or preview trivia.
"""

QUESTIONS = [
    # ===== sc9_entra_identity_types =========================================
    {
        "id": "sc900-entra-001", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_identity_types", "difficulty": 1, "type": "mcq",
        "stem": "Which Microsoft service is a cloud-based identity and access management service, formerly "
                "known as Azure Active Directory (Azure AD)?",
        "options": [
            {"id": "A", "text": "Microsoft Entra ID"},
            {"id": "B", "text": "Microsoft Intune"},
            {"id": "C", "text": "Microsoft Defender XDR"},
            {"id": "D", "text": "Microsoft Purview"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Entra ID is Microsoft's cloud-based identity and access management service, "
                       "and it is the product formerly called Azure Active Directory (Azure AD).",
            "distractors": {
                "B": "Microsoft Intune is an endpoint/device management service, not the identity directory.",
                "C": "Microsoft Defender XDR is an extended detection and response suite, not an identity service.",
                "D": "Microsoft Purview is the compliance and data governance suite, not the identity service.",
            },
            "exam_pattern": "Cloud identity and access management, formerly Azure AD = Microsoft Entra ID.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Entra ID"],
    },
    {
        "id": "sc900-entra-002", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_identity_types", "difficulty": 2, "type": "mcq",
        "stem": "An Azure web app needs to access Azure Key Vault without developers storing or rotating any "
                "credentials in code. Which Microsoft Entra identity type should the app use?",
        "options": [
            {"id": "A", "text": "A managed identity"},
            {"id": "B", "text": "A guest user account"},
            {"id": "C", "text": "A named user account with a password"},
            {"id": "D", "text": "A security group"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A managed identity is an automatically managed identity in Entra ID for an Azure "
                       "resource, letting it authenticate to services like Key Vault with no credentials in code.",
            "distractors": {
                "B": "A guest account represents an external person, not an Azure resource, and still needs credential handling.",
                "C": "A named user with a password is exactly the credential-management burden managed identities remove.",
                "D": "A security group is a collection of identities for assigning access, not an identity an app signs in as.",
            },
            "exam_pattern": "Azure resource needs credential-free access to Azure services = managed identity.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the identity types (workload identities)"],
    },
    {
        "id": "sc900-entra-003", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_identity_types", "difficulty": 2, "type": "mcq",
        "stem": "Applications, services, and automation tools that need to access resources are represented in "
                "Microsoft Entra ID by which category of identity?",
        "options": [
            {"id": "A", "text": "Workload identities (such as service principals and managed identities)"},
            {"id": "B", "text": "Guest users"},
            {"id": "C", "text": "Device identities only"},
            {"id": "D", "text": "Administrative units"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Workload identities - including service principals and managed identities - represent "
                       "apps, services, and automation so they can authenticate and be granted access.",
            "distractors": {
                "B": "Guest users represent external people, not applications or services.",
                "C": "Device identities represent computers and phones, not the apps/services themselves.",
                "D": "An administrative unit is a container for scoping administration, not an identity for a workload.",
            },
            "exam_pattern": "Apps/services/automation that need access = workload identities (service principals, managed identities).",
        },
        "references": ["Microsoft Learn (SC-900): Describe the identity types"],
    },
    {
        "id": "sc900-entra-004", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_identity_types", "difficulty": 1, "type": "mcq",
        "stem": "An administrator wants to assign the same access rights to many users at once rather than "
                "configuring each user individually. Which Microsoft Entra object should they use?",
        "options": [
            {"id": "A", "text": "A group"},
            {"id": "B", "text": "A service principal"},
            {"id": "C", "text": "A managed identity"},
            {"id": "D", "text": "A Conditional Access policy"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Groups let administrators manage access for many users (or devices) at once by assigning "
                       "rights to the group instead of to each member.",
            "distractors": {
                "B": "A service principal is an identity for an application, not a way to group users for access.",
                "C": "A managed identity is an app identity for Azure resources, not a grouping of users.",
                "D": "A Conditional Access policy enforces access conditions; it does not bundle users for assignment.",
            },
            "exam_pattern": "Assign access to many users at once = use a group.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the identity types (groups)"],
    },
    {
        "id": "sc900-entra-005", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_identity_types", "difficulty": 2, "type": "mcq",
        "stem": "Two partner companies want their employees to collaborate using each employee's existing "
                "credentials from their home organization, appearing as guest users in the host tenant. Which "
                "Microsoft Entra external identities capability enables this?",
        "options": [
            {"id": "A", "text": "B2B collaboration"},
            {"id": "B", "text": "Microsoft Entra External ID for customers (CIAM; formerly Azure AD B2C)"},
            {"id": "C", "text": "Managed identities"},
            {"id": "D", "text": "Conditional Access"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "B2B collaboration (part of external identities) invites external partners as guests who "
                       "sign in with their own home credentials, with no separate account to manage.",
            "distractors": {
                "B": "External ID for customers (CIAM, formerly Azure AD B2C) is for customer/consumer sign-up and sign-in to your apps, not partner employees collaborating as guests.",
                "C": "Managed identities are for Azure resources, not external human collaborators.",
                "D": "Conditional Access enforces access conditions; it does not provide the external-collaboration mechanism.",
            },
            "exam_pattern": "Partners collaborate as guests with their own credentials = B2B collaboration.",
        },
        "references": ["Microsoft Learn (SC-900): Describe external identities (B2B)"],
    },
    {
        "id": "sc900-entra-006", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_identity_types", "difficulty": 2, "type": "multi",
        "stem": "Microsoft Entra ID secures several categories of identities. Which TWO of the following are "
                "identity types that Entra ID manages? (Choose two.)",
        "options": [
            {"id": "A", "text": "Users (including internal members and external guests)"},
            {"id": "B", "text": "Workload identities (such as service principals and managed identities)"},
            {"id": "C", "text": "Physical network cables"},
            {"id": "D", "text": "Azure region pairs"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Entra ID manages users, groups, devices, and workload identities. Users and workload "
                       "identities are two of those categories.",
            "distractors": {
                "C": "Physical cables are hardware, not identities managed by a directory.",
                "D": "Region pairs are a datacenter-resiliency concept, not an identity type.",
            },
            "exam_pattern": "Entra identity types: users, groups, devices, workload identities.",
        },
        "references": ["Microsoft Learn (SC-900): Describe the identity types"],
    },
    {
        "id": "sc900-entra-007", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_identity_types", "difficulty": 1, "type": "fill",
        "stem": "Microsoft Entra ID is the current name for the cloud identity service formerly called Azure "
                "AD. In that former name, 'AD' stood for Active ___. Enter the missing one-word term.",
        "correct": ["directory"],
        "explanation": {
            "correct": "Azure AD stood for Azure Active Directory; Microsoft renamed the service to Microsoft "
                       "Entra ID.",
            "distractors": {},
            "exam_pattern": "Azure AD = Azure Active Directory, now rebranded Microsoft Entra ID.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Entra ID"],
    },

    # ===== sc9_entra_authentication =========================================
    {
        "id": "sc900-entra-008", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_authentication", "difficulty": 1, "type": "mcq",
        "stem": "Which authentication approach requires a user to provide two or more different verification "
                "factors - for example, a password plus an approval on their phone - to sign in?",
        "options": [
            {"id": "A", "text": "Multifactor authentication (MFA)"},
            {"id": "B", "text": "Single sign-on (SSO)"},
            {"id": "C", "text": "Single-factor authentication"},
            {"id": "D", "text": "Federation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "MFA requires two or more verification factors from different categories, strengthening "
                       "sign-in security beyond a single password.",
            "distractors": {
                "B": "SSO reduces the number of sign-ins across apps; it does not add verification factors.",
                "C": "Single-factor authentication uses just one factor (typically a password) - the opposite of MFA.",
                "D": "Federation is a trust between identity systems, not a multi-factor sign-in requirement.",
            },
            "exam_pattern": "Two or more different factors at sign-in = MFA.",
        },
        "references": ["Microsoft Learn (SC-900): Describe multifactor authentication"],
    },
    {
        "id": "sc900-entra-009", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_authentication", "difficulty": 2, "type": "fill",
        "stem": "Multifactor authentication combines factors from at least two different categories: something "
                "you know, something you have, and something you ___. Enter the missing one-word term.",
        "correct": ["are"],
        "explanation": {
            "correct": "The three factor categories are something you know (password/PIN), something you have "
                       "(phone/token), and something you are (biometric).",
            "distractors": {},
            "exam_pattern": "Factor categories: know, have, are (knowledge, possession, biometric/inherence).",
        },
        "references": ["Microsoft Learn (SC-900): Describe multifactor authentication"],
    },
    {
        "id": "sc900-entra-010", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_authentication", "difficulty": 2, "type": "multi",
        "stem": "Which TWO of the following are passwordless authentication methods supported by Microsoft "
                "Entra ID? (Choose two.)",
        "options": [
            {"id": "A", "text": "Windows Hello for Business"},
            {"id": "B", "text": "FIDO2 security keys"},
            {"id": "C", "text": "A username and a password"},
            {"id": "D", "text": "A knowledge-based security question"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Passwordless methods in Entra ID include Windows Hello for Business, FIDO2 security keys, "
                       "and passwordless phone sign-in with the Microsoft Authenticator app.",
            "distractors": {
                "C": "A username and password is the password-based method that passwordless sign-in replaces.",
                "D": "A security question is a shared secret (knowledge factor), not a passwordless method.",
            },
            "exam_pattern": "Passwordless = Windows Hello, FIDO2 keys, Microsoft Authenticator phone sign-in.",
        },
        "references": ["Microsoft Learn (SC-900): Describe passwordless authentication"],
    },
    {
        "id": "sc900-entra-011", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_authentication", "difficulty": 2, "type": "mcq",
        "stem": "A company wants employees to reset their own forgotten passwords after verifying identity with "
                "registered methods, without calling the help desk. Which Microsoft Entra feature provides this?",
        "options": [
            {"id": "A", "text": "Self-service password reset (SSPR)"},
            {"id": "B", "text": "Conditional Access"},
            {"id": "C", "text": "Privileged Identity Management (PIM)"},
            {"id": "D", "text": "Multifactor authentication (MFA)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "SSPR lets users reset or unlock their own passwords after verifying with registered "
                       "authentication methods, reducing help-desk calls.",
            "distractors": {
                "B": "Conditional Access enforces access conditions at sign-in; it does not perform password resets.",
                "C": "PIM manages just-in-time activation of privileged roles, not end-user password resets.",
                "D": "MFA adds verification factors; it is not the self-service reset capability (though SSPR relies on verification).",
            },
            "exam_pattern": "Users reset their own forgotten passwords = self-service password reset (SSPR).",
        },
        "references": ["Microsoft Learn (SC-900): Describe self-service password reset"],
    },
    {
        "id": "sc900-entra-012", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_authentication", "difficulty": 2, "type": "mcq",
        "stem": "Which Microsoft app can serve as an authentication method, supporting push-notification "
                "approvals, one-time passcodes, and passwordless phone sign-in?",
        "options": [
            {"id": "A", "text": "Microsoft Authenticator"},
            {"id": "B", "text": "Microsoft Intune"},
            {"id": "C", "text": "Microsoft Sentinel"},
            {"id": "D", "text": "Microsoft Purview"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Microsoft Authenticator app provides push approvals, time-based one-time passcodes, "
                       "and passwordless phone sign-in as authentication methods.",
            "distractors": {
                "B": "Intune manages devices and apps; it is not an authentication-method app.",
                "C": "Sentinel is a SIEM/SOAR security operations tool, not an authenticator.",
                "D": "Purview is the compliance suite, not an authentication app.",
            },
            "exam_pattern": "Push approvals, OTP codes, passwordless phone sign-in = Microsoft Authenticator.",
        },
        "references": ["Microsoft Learn (SC-900): Describe authentication methods"],
    },

    # ===== sc9_entra_access_management ======================================
    {
        "id": "sc900-entra-013", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_access_management", "difficulty": 2, "type": "mcq",
        "stem": "Which Microsoft Entra feature evaluates signals such as user, location, device state, and "
                "sign-in risk, and then allows, blocks, or requires extra controls (like MFA) before granting "
                "access to an app?",
        "options": [
            {"id": "A", "text": "Conditional Access"},
            {"id": "B", "text": "Single sign-on (SSO)"},
            {"id": "C", "text": "Self-service password reset (SSPR)"},
            {"id": "D", "text": "Entitlement management"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Conditional Access brings signals together, makes a decision, and enforces it - for "
                       "example, requiring MFA or blocking access based on conditions.",
            "distractors": {
                "B": "SSO lets a user sign in once for many apps; it does not evaluate signals to allow or block access.",
                "C": "SSPR handles password resets, not conditional access decisions.",
                "D": "Entitlement management governs access packages and requests, not real-time sign-in decisions.",
            },
            "exam_pattern": "Signals -> decision -> enforcement (allow/block/require MFA) = Conditional Access.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Conditional Access"],
    },
    {
        "id": "sc900-entra-014", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_access_management", "difficulty": 3, "type": "mcq",
        "stem": "A company wants to require multifactor authentication only when a user signs in from an "
                "unfamiliar location or from an unmanaged device, but not otherwise. What should they configure?",
        "options": [
            {"id": "A", "text": "A Conditional Access policy"},
            {"id": "B", "text": "A security group"},
            {"id": "C", "text": "A managed identity"},
            {"id": "D", "text": "Password hash synchronization"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A Conditional Access policy can require MFA only under specific conditions, such as "
                       "risky locations or unmanaged/noncompliant devices, leaving normal sign-ins untouched.",
            "distractors": {
                "B": "A security group assigns access to members but cannot impose conditional, signal-based MFA.",
                "C": "A managed identity is an app identity for Azure resources, not a sign-in policy mechanism.",
                "D": "Password hash synchronization syncs credentials for hybrid identity; it does not enforce conditional MFA.",
            },
            "exam_pattern": "Require MFA only under certain conditions (location/device/risk) = Conditional Access policy.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Conditional Access"],
    },
    {
        "id": "sc900-entra-015", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_access_management", "difficulty": 2, "type": "mcq",
        "stem": "In a Conditional Access policy, inputs such as the user or group, the location, the device "
                "platform and state, and the application being accessed are collectively referred to as the:",
        "options": [
            {"id": "A", "text": "Signals"},
            {"id": "B", "text": "Licenses"},
            {"id": "C", "text": "Roles"},
            {"id": "D", "text": "Secrets"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Conditional Access gathers signals (user, location, device, application, risk), uses "
                       "them to make a decision, and then enforces that decision.",
            "distractors": {
                "B": "Licenses determine feature entitlements, not the per-sign-in inputs a policy evaluates.",
                "C": "Roles define administrative permissions; they are not the full set of Conditional Access inputs.",
                "D": "Secrets are credentials such as keys and passwords, not Conditional Access inputs.",
            },
            "exam_pattern": "Conditional Access inputs (user/location/device/app/risk) = signals.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Conditional Access"],
    },
    {
        "id": "sc900-entra-016", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_access_management", "difficulty": 2, "type": "mcq",
        "stem": "A company wants to grant each administrator only the permissions their job requires by "
                "assigning them to predefined roles. Which access-control model is this?",
        "options": [
            {"id": "A", "text": "Role-based access control (RBAC)"},
            {"id": "B", "text": "File-owner discretionary access control"},
            {"id": "C", "text": "Conditional Access"},
            {"id": "D", "text": "Federation"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "RBAC grants permissions by assigning identities to roles that carry only the needed "
                       "rights, supporting least-privilege administration.",
            "distractors": {
                "B": "Discretionary access control lets resource owners set permissions individually; it is not role-based assignment.",
                "C": "Conditional Access decides whether to allow a sign-in; it does not assign permission sets via roles.",
                "D": "Federation establishes trust between identity systems, not a permissions-by-role model.",
            },
            "exam_pattern": "Permissions granted via roles for least privilege = RBAC.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Entra role-based access control"],
    },
    {
        "id": "sc900-entra-017", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_access_management", "difficulty": 2, "type": "mcq",
        "stem": "Which built-in Microsoft Entra role grants the broadest, most privileged access across the "
                "tenant and should therefore be assigned to as few people as possible?",
        "options": [
            {"id": "A", "text": "Global Administrator"},
            {"id": "B", "text": "Reports Reader"},
            {"id": "C", "text": "Helpdesk Administrator"},
            {"id": "D", "text": "Guest user"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The Global Administrator role has the most extensive privileges in a tenant, so "
                       "best practice is to grant it to the fewest possible people.",
            "distractors": {
                "B": "Reports Reader can only view reporting data - a narrow, low-privilege role.",
                "C": "Helpdesk Administrator handles limited support tasks (such as resetting some passwords), not full tenant control.",
                "D": "Guest user is an external collaborator identity, not a privileged administrative role.",
            },
            "exam_pattern": "Most privileged built-in Entra role = Global Administrator (assign sparingly).",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Entra built-in roles"],
    },

    # ===== sc9_entra_identity_protection ====================================
    {
        "id": "sc900-entra-018", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_identity_protection", "difficulty": 2, "type": "mcq",
        "stem": "Which Microsoft Entra capability uses signals and machine learning to detect risky sign-ins "
                "and risky users, and can automatically require MFA or block access through risk-based policies?",
        "options": [
            {"id": "A", "text": "Microsoft Entra ID Protection"},
            {"id": "B", "text": "Privileged Identity Management (PIM)"},
            {"id": "C", "text": "Entitlement management"},
            {"id": "D", "text": "Self-service password reset (SSPR)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Entra ID Protection detects identity risk (risky sign-ins and users) and can "
                       "automate responses such as requiring MFA or blocking access via risk-based policies.",
            "distractors": {
                "B": "PIM manages time-limited activation of privileged roles; it does not detect sign-in risk.",
                "C": "Entitlement management handles access packages and request workflows, not risk detection.",
                "D": "SSPR lets users reset passwords; it does not detect or remediate identity risk.",
            },
            "exam_pattern": "Detect risky sign-ins/users with ML and auto-remediate = Microsoft Entra ID Protection.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Entra ID Protection"],
    },
    {
        "id": "sc900-entra-019", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_identity_protection", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants administrators to request just-in-time, time-limited activation of "
                "privileged roles with approval and auditing, instead of holding standing administrative access. "
                "Which capability provides this?",
        "options": [
            {"id": "A", "text": "Privileged Identity Management (PIM)"},
            {"id": "B", "text": "Self-service password reset (SSPR)"},
            {"id": "C", "text": "B2B collaboration"},
            {"id": "D", "text": "Conditional Access"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "PIM (part of Microsoft Entra ID Governance) provides just-in-time, time-bound privileged "
                       "role activation with approval workflows and auditing to reduce standing admin access.",
            "distractors": {
                "B": "SSPR resets user passwords; it does not manage privileged role activation.",
                "C": "B2B collaboration invites external guests; it is unrelated to just-in-time admin access.",
                "D": "Conditional Access enforces sign-in conditions but does not provide time-limited role elevation.",
            },
            "exam_pattern": "Just-in-time, time-limited privileged role activation with approval = PIM.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Privileged Identity Management"],
    },
    {
        "id": "sc900-entra-020", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_identity_protection", "difficulty": 2, "type": "mcq",
        "stem": "A company must periodically have managers confirm whether users still need their current group "
                "memberships and app access, removing those who no longer do. Which Microsoft Entra ID Governance "
                "feature automates this recurring attestation?",
        "options": [
            {"id": "A", "text": "Access reviews"},
            {"id": "B", "text": "Password hash synchronization"},
            {"id": "C", "text": "Multifactor authentication (MFA)"},
            {"id": "D", "text": "Managed identities"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Access reviews let organizations periodically recertify users' access to groups, apps, "
                       "and roles, removing access that is no longer needed.",
            "distractors": {
                "B": "Password hash synchronization is a hybrid-identity sync mechanism, not an access attestation tool.",
                "C": "MFA strengthens sign-in; it does not review whether existing access is still appropriate.",
                "D": "Managed identities are app identities for Azure resources, unrelated to recertifying user access.",
            },
            "exam_pattern": "Periodically recertify/attest who still needs access = access reviews.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Entra ID Governance (access reviews)"],
    },
    {
        "id": "sc900-entra-021", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_identity_protection", "difficulty": 2, "type": "mcq",
        "stem": "An organization wants to bundle groups, applications, and SharePoint sites into access packages "
                "that users - including external partners - can request, with approval workflows and automatic "
                "expiration. Which Microsoft Entra ID Governance feature is this?",
        "options": [
            {"id": "A", "text": "Entitlement management"},
            {"id": "B", "text": "Conditional Access"},
            {"id": "C", "text": "Microsoft Entra ID Protection"},
            {"id": "D", "text": "Self-service password reset (SSPR)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Entitlement management uses access packages to govern access requests, approvals, and "
                       "expiration for internal and external users.",
            "distractors": {
                "B": "Conditional Access decides sign-in access in real time; it does not package and govern access requests.",
                "C": "ID Protection detects identity risk; it does not manage access packages.",
                "D": "SSPR resets passwords; it has nothing to do with access packages.",
            },
            "exam_pattern": "Access packages with request/approval/expiration = entitlement management.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Entra ID Governance (entitlement management)"],
    },
    {
        "id": "sc900-entra-022", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_identity_protection", "difficulty": 2, "type": "mcq",
        "stem": "Which Microsoft Entra capability implements decentralized identity, letting organizations "
                "issue, and users hold and present, tamper-evident verifiable credentials (for example, proof "
                "of employment or a completed certification)?",
        "options": [
            {"id": "A", "text": "Microsoft Entra Verified ID"},
            {"id": "B", "text": "Microsoft Entra ID Protection"},
            {"id": "C", "text": "Privileged Identity Management (PIM)"},
            {"id": "D", "text": "Conditional Access"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Entra Verified ID is a decentralized identity solution for issuing and "
                       "verifying verifiable credentials that users control in a digital wallet.",
            "distractors": {
                "B": "ID Protection detects and remediates identity risk; it does not issue verifiable credentials.",
                "C": "PIM governs privileged role activation, not verifiable credentials.",
                "D": "Conditional Access enforces access policies; it is not a verifiable-credential issuer.",
            },
            "exam_pattern": "Issue/verify portable verifiable credentials (decentralized identity) = Entra Verified ID.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Entra Verified ID"],
    },
    {
        "id": "sc900-entra-023", "exam": "sc900", "domain": "sc9_entra",
        "subtopic": "sc9_entra_identity_protection", "difficulty": 2, "type": "mcq",
        "stem": "Which Microsoft Entra product is a cloud infrastructure entitlement management (CIEM) solution "
                "that discovers, monitors, and right-sizes identity permissions across Azure, AWS, and Google "
                "Cloud?",
        "options": [
            {"id": "A", "text": "Microsoft Entra Permissions Management"},
            {"id": "B", "text": "Microsoft Sentinel"},
            {"id": "C", "text": "Microsoft Purview"},
            {"id": "D", "text": "Self-service password reset (SSPR)"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Entra Permissions Management is a CIEM solution that provides visibility into "
                       "and control over permissions across Azure, AWS, and Google Cloud.",
            "distractors": {
                "B": "Microsoft Sentinel is a SIEM/SOAR platform, not a multicloud permissions-management tool.",
                "C": "Microsoft Purview is the compliance and data governance suite, not a CIEM product.",
                "D": "SSPR is a password-reset feature, unrelated to multicloud permission right-sizing.",
            },
            "exam_pattern": "Multicloud (Azure/AWS/GCP) permission discovery and right-sizing (CIEM) = Entra Permissions Management.",
        },
        "references": ["Microsoft Learn (SC-900): Describe Microsoft Entra Permissions Management"],
    },
]
