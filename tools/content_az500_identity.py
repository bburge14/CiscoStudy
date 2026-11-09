"""Microsoft AZ-500 (Azure Security Engineer) pool - Domain 1: Manage Identity and Access.

Original, objective-aligned practice items for the four Identity & Access
subtopics tracked in CertLab:
  * az500_entra_identities    - Microsoft Entra ID users/groups (assigned vs
                                dynamic), external identities (B2B collaboration
                                vs External ID for customers/B2C), and
                                administrative units.
  * az500_entra_authn_authz   - authentication (MFA, Conditional Access,
                                passwordless, SSPR, the authentication methods
                                policy) and risk-based authorization (Microsoft
                                Entra ID Protection).
  * az500_rbac_pim            - Azure RBAC (roles, scope, assignments) contrasted
                                with Entra directory roles, and Privileged
                                Identity Management (eligible vs active,
                                activation controls, access reviews).
  * az500_app_identity        - managed identities (system- vs user-assigned),
                                service principals, app registrations, and
                                application consent.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), and the authored answer key is spread across A/B/C/D
rather than defaulting to "A"; every wrong option carries a distractor note, and
each item names the Microsoft Learn area it draws on so facts stay traceable.
Current product names are used throughout: Microsoft Entra ID (formerly Azure AD),
Microsoft Defender for Cloud, Microsoft Sentinel. Items are original and aligned
to the public AZ-500 objectives - never real or memorized exam items.
"""

QUESTIONS = [
    # ===== az500_entra_identities ===========================================
    {
        "id": "az500-id-001", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_entra_identities", "difficulty": 1, "type": "mcq",
        "stem": "A partner firm's engineers need to collaborate on a shared Azure resource using their "
                "own existing work accounts, without your organization creating or managing passwords for "
                "them. Which Microsoft Entra capability should you use?",
        "options": [
            {"id": "A", "text": "Create member user accounts for each engineer in your tenant"},
            {"id": "B", "text": "Invite them as Microsoft Entra B2B collaboration (guest) users"},
            {"id": "C", "text": "Deploy Microsoft Entra Domain Services"},
            {"id": "D", "text": "Share one service account across the whole partner team"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Microsoft Entra B2B collaboration invites external users as guests who sign in "
                       "with their own home-tenant credentials, so you never create or manage their passwords.",
            "distractors": {
                "A": "Creating member accounts means you own their credentials and lifecycle - the opposite "
                     "of the requirement and far more administrative overhead.",
                "C": "Entra Domain Services provides managed domain services (LDAP/Kerberos/NTLM) for legacy "
                     "workloads, not external partner collaboration.",
                "D": "A shared account destroys individual accountability and auditing and is a security anti-pattern.",
            },
            "exam_pattern": "External collaborators who bring their own identity = Entra B2B guest invite, "
                            "not new member accounts or shared accounts.",
        },
        "references": ["Microsoft Learn (AZ-500): Microsoft Entra External ID - B2B collaboration"],
    },
    {
        "id": "az500-id-002", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_entra_identities", "difficulty": 2, "type": "mcq",
        "stem": "You want group membership to update automatically as a user's department attribute "
                "changes, so license and access assignments always track the department with no manual "
                "upkeep. Which configuration meets this best?",
        "options": [
            {"id": "A", "text": "An assigned security group whose members are added manually"},
            {"id": "B", "text": "A Microsoft 365 group whose owner reviews membership each month"},
            {"id": "C", "text": "A dynamic security group with a membership rule on the department attribute"},
            {"id": "D", "text": "An administrative unit that contains the department's users"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "A dynamic membership group evaluates an attribute-based rule and automatically adds "
                       "or removes members as their attributes change, so membership self-maintains.",
            "distractors": {
                "A": "Assigned groups require manual membership edits, so they drift out of sync as attributes change.",
                "B": "Owner-reviewed membership is still manual and periodic, not automatic and attribute-driven.",
                "D": "An administrative unit scopes delegated administration over a set of objects; it does not "
                     "auto-populate membership for licensing or access.",
            },
            "exam_pattern": "Automatic, attribute-driven membership = dynamic group with a membership rule (needs Entra ID P1).",
        },
        "references": ["Microsoft Learn (AZ-500): Microsoft Entra dynamic membership groups"],
    },
    {
        "id": "az500-id-003", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_entra_identities", "difficulty": 2, "type": "mcq",
        "stem": "A regional helpdesk should be able to reset passwords only for users in the Finance "
                "business unit, not for the entire directory. Which Microsoft Entra feature scopes their "
                "administrative role to just those users?",
        "options": [
            {"id": "A", "text": "Administrative units"},
            {"id": "B", "text": "Dynamic groups"},
            {"id": "C", "text": "Conditional Access"},
            {"id": "D", "text": "Azure management groups"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Administrative units let you scope a Microsoft Entra directory role (such as "
                       "Password Administrator) to a subset of the directory, so the helpdesk acts only on Finance users.",
            "distractors": {
                "B": "Dynamic groups automate membership but do not restrict the scope of an admin role.",
                "C": "Conditional Access governs sign-in conditions, not the scope of delegated administration.",
                "D": "Azure management groups organize Azure subscriptions for governance, not Entra directory-role scope.",
            },
            "exam_pattern": "Scope a directory role to a subset of users/devices/groups = administrative units.",
        },
        "references": ["Microsoft Learn (AZ-500): Microsoft Entra administrative units"],
    },
    {
        "id": "az500-id-004", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_entra_identities", "difficulty": 2, "type": "mcq",
        "stem": "Your company is building a public retail app and needs millions of consumers to sign up "
                "and sign in with social or local accounts, fully branded as your app. Which identity "
                "solution is designed for this customer-facing scenario?",
        "options": [
            {"id": "A", "text": "Microsoft Entra B2B collaboration"},
            {"id": "B", "text": "Microsoft Entra Privileged Identity Management"},
            {"id": "C", "text": "Microsoft Entra Domain Services"},
            {"id": "D", "text": "Microsoft Entra External ID for customers (Azure AD B2C)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Entra External ID for customers (the evolution of Azure AD B2C) is the customer "
                       "identity and access management (CIAM) solution for consumer sign-up/sign-in with social or "
                       "local accounts and full app branding.",
            "distractors": {
                "A": "B2B collaboration invites business partners into your tenant; it is not for mass consumer sign-up.",
                "B": "PIM manages just-in-time privileged access for administrators, unrelated to consumer identity.",
                "C": "Entra Domain Services provides managed domain services for legacy workloads, not consumer identity.",
            },
            "exam_pattern": "Consumer/customer-facing sign-up (CIAM) = External ID for customers / B2C; partner "
                            "collaboration = B2B.",
        },
        "references": ["Microsoft Learn (AZ-500): Microsoft Entra External ID - B2B vs customer (B2C) identities"],
    },
    {
        "id": "az500-id-005", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_entra_identities", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: A Microsoft Entra group whose membership is recalculated automatically "
                "from a rule evaluated against user or device attributes (such as department or country), "
                "rather than edited by hand, is called a ________ membership group.",
        "correct": ["dynamic"],
        "explanation": {
            "correct": "Dynamic membership groups use an attribute-based rule; Entra automatically adds or "
                       "removes members as their attributes change, unlike assigned (static) groups that are edited manually.",
            "exam_pattern": "Attribute-rule, auto-updating membership = dynamic group; manual membership = assigned group.",
        },
        "references": ["Microsoft Learn (AZ-500): Microsoft Entra dynamic membership groups"],
    },

    # ===== az500_entra_authn_authz ==========================================
    {
        "id": "az500-id-006", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_entra_authn_authz", "difficulty": 2, "type": "mcq",
        "stem": "Policy requires multifactor authentication only when users reach the finance app from "
                "outside the corporate network, while in-office access stays seamless. Which control "
                "implements this location-aware requirement?",
        "options": [
            {"id": "A", "text": "Enable security defaults on the tenant"},
            {"id": "B", "text": "A Conditional Access policy targeting the app with a named-location "
                               "condition and a grant control requiring MFA"},
            {"id": "C", "text": "Legacy per-user MFA enabled for every user"},
            {"id": "D", "text": "A self-service password reset (SSPR) policy"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Conditional Access evaluates signals (here, named location and target app) and applies "
                       "a grant control; requiring MFA only from outside the trusted location meets the requirement.",
            "distractors": {
                "A": "Security defaults apply one baseline MFA behavior to everyone and cannot be tailored by app or location.",
                "C": "Legacy per-user MFA always prompts regardless of location, so in-office access would not stay seamless.",
                "D": "SSPR lets users reset their own passwords; it does not enforce MFA on app access.",
            },
            "exam_pattern": "Conditional, signal-based access (location/app/risk) = Conditional Access (needs Entra ID P1); "
                            "security defaults are all-or-nothing.",
        },
        "references": ["Microsoft Learn (AZ-500): Conditional Access policies and conditions"],
    },
    {
        "id": "az500-id-007", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_entra_authn_authz", "difficulty": 2, "type": "mcq",
        "stem": "You must remove passwords for a group of administrators by issuing phishing-resistant "
                "hardware keys they tap to sign in. Which authentication method should you deploy?",
        "options": [
            {"id": "A", "text": "FIDO2 security keys"},
            {"id": "B", "text": "SMS text-message codes"},
            {"id": "C", "text": "Security questions"},
            {"id": "D", "text": "A Temporary Access Pass as the permanent sign-in method"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "FIDO2 security keys are a phishing-resistant, passwordless method; the user proves "
                       "possession of the hardware key instead of entering a password.",
            "distractors": {
                "B": "SMS is a weak second factor vulnerable to SIM-swap and interception, and it is not passwordless.",
                "C": "Security questions are knowledge-based secrets (the weakest factor) and are not passwordless.",
                "D": "A Temporary Access Pass is a time-limited onboarding/recovery credential, not a permanent method.",
            },
            "exam_pattern": "Phishing-resistant passwordless = FIDO2 security keys, Windows Hello for Business, or "
                            "Microsoft Authenticator passwordless sign-in.",
        },
        "references": ["Microsoft Learn (AZ-500): Passwordless authentication options for Microsoft Entra ID"],
    },
    {
        "id": "az500-id-008", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_entra_authn_authz", "difficulty": 1, "type": "mcq",
        "stem": "The helpdesk is overwhelmed by password-reset calls. Which Microsoft Entra feature lets "
                "users securely reset or unlock their own accounts after verifying registered authentication "
                "methods?",
        "options": [
            {"id": "A", "text": "Privileged Identity Management (PIM)"},
            {"id": "B", "text": "Conditional Access"},
            {"id": "C", "text": "Self-service password reset (SSPR)"},
            {"id": "D", "text": "Microsoft Entra Connect"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "SSPR lets users reset or unlock their own accounts after passing registered "
                       "authentication methods, cutting helpdesk password calls.",
            "distractors": {
                "A": "PIM manages time-bound privileged role activation, not end-user password resets.",
                "B": "Conditional Access evaluates sign-in conditions; it does not reset passwords.",
                "D": "Entra Connect synchronizes on-premises AD to Entra ID (and enables password writeback that "
                     "supports SSPR); it is not itself the self-service reset portal.",
            },
            "exam_pattern": "Users reset their own passwords after proving identity = SSPR (with writeback for hybrid).",
        },
        "references": ["Microsoft Learn (AZ-500): Self-service password reset"],
    },
    {
        "id": "az500-id-009", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_entra_authn_authz", "difficulty": 3, "type": "mcq",
        "stem": "You want sign-ins that Microsoft Entra flags as high risk (for example, from anonymous "
                "IP addresses or atypical travel) to automatically force the user to complete MFA. Which "
                "capability provides this risk signal and automated response?",
        "options": [
            {"id": "A", "text": "An Azure Policy with a DeployIfNotExists effect"},
            {"id": "B", "text": "A network security group rule"},
            {"id": "C", "text": "Microsoft Defender for Cloud Secure Score"},
            {"id": "D", "text": "A Microsoft Entra ID Protection sign-in risk policy enforced through Conditional Access"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Microsoft Entra ID Protection detects sign-in and user risk and, through a risk-based "
                       "Conditional Access policy, can automatically require MFA or a secure password change.",
            "distractors": {
                "A": "Azure Policy governs Azure resource configuration, not identity sign-in risk.",
                "B": "NSG rules filter network traffic by IP/port; they do not evaluate identity risk.",
                "C": "Secure Score measures resource security posture; it does not score or remediate user sign-in risk.",
            },
            "exam_pattern": "Detect risky sign-ins/users and auto-remediate (MFA / password change) = Entra ID "
                            "Protection risk policies (needs Entra ID P2), enforced via Conditional Access.",
        },
        "references": ["Microsoft Learn (AZ-500): Microsoft Entra ID Protection risk-based policies"],
    },
    {
        "id": "az500-id-010", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_entra_authn_authz", "difficulty": 2, "type": "multi",
        "stem": "In a Conditional Access policy, which TWO of the following are valid grant controls you "
                "can require before access is allowed? (Choose two.)",
        "options": [
            {"id": "A", "text": "Require multifactor authentication"},
            {"id": "B", "text": "Require the device to be marked compliant or Microsoft Entra hybrid joined"},
            {"id": "C", "text": "Encrypt the virtual machine's OS disk"},
            {"id": "D", "text": "Apply a CanNotDelete resource lock"},
        ],
        "correct": ["A", "B"],
        "explanation": {
            "correct": "Conditional Access grant controls include requiring MFA and requiring a compliant or "
                       "Entra hybrid joined device (among others such as approved client app or password change).",
            "distractors": {
                "C": "Disk encryption protects VM data at rest; it is not a Conditional Access grant control.",
                "D": "Resource locks prevent accidental deletion/modification of Azure resources; they are unrelated "
                     "to sign-in grant controls.",
            },
            "exam_pattern": "CA grant controls = require MFA, compliant/hybrid-joined device, approved client app, "
                            "password change, terms of use, or block access.",
        },
        "references": ["Microsoft Learn (AZ-500): Conditional Access grant controls"],
    },
    {
        "id": "az500-id-011", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_entra_authn_authz", "difficulty": 2, "type": "mcq",
        "stem": "To reduce MFA-fatigue attacks in which users accidentally approve fraudulent push "
                "prompts, which Microsoft Authenticator control - managed centrally in the authentication "
                "methods policy - should you enforce?",
        "options": [
            {"id": "A", "text": "Allow SMS as the only second factor"},
            {"id": "B", "text": "Number matching, where the user types a displayed number to approve"},
            {"id": "C", "text": "Disable MFA from trusted locations"},
            {"id": "D", "text": "Add security questions on top of the push"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Number matching forces the user to enter a number shown on the sign-in screen into the "
                       "Authenticator prompt, so a blind 'Approve' tap cannot satisfy a fraudulent request.",
            "distractors": {
                "A": "Falling back to SMS weakens security and does not address accidental push approvals.",
                "C": "Disabling MFA increases risk and does nothing to stop fraudulent approvals.",
                "D": "Security questions are weak knowledge factors and do not prevent blind push approval.",
            },
            "exam_pattern": "Number matching (plus additional context) in the authentication methods policy counters "
                            "MFA-fatigue / push-bombing.",
        },
        "references": ["Microsoft Learn (AZ-500): Microsoft Authenticator number matching / authentication methods policy"],
    },

    # ===== az500_rbac_pim ===================================================
    {
        "id": "az500-id-012", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_rbac_pim", "difficulty": 2, "type": "mcq",
        "stem": "A user with the Contributor role on a resource group tries to grant a colleague access to "
                "a VM and is denied. Which role lets them manage access (assign roles) without giving them "
                "full ownership of the resources?",
        "options": [
            {"id": "A", "text": "Reader"},
            {"id": "B", "text": "Owner"},
            {"id": "C", "text": "User Access Administrator"},
            {"id": "D", "text": "A second Contributor assignment at subscription scope"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "User Access Administrator grants exactly the ability to manage user access (assign Azure "
                       "roles) without granting full control over the resources themselves.",
            "distractors": {
                "A": "Reader is view-only and cannot assign access at all.",
                "B": "Owner can manage access but also grants full control of the resources - more than the stated need.",
                "D": "Contributor at any scope can manage resources but explicitly cannot assign roles (manage access).",
            },
            "exam_pattern": "Manage access without full control = User Access Administrator; Contributor does everything "
                            "except assign roles.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure built-in roles - Owner, Contributor, User Access Administrator"],
    },
    {
        "id": "az500-id-013", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_rbac_pim", "difficulty": 2, "type": "mcq",
        "stem": "You assign the Reader role to a group at the subscription scope. How does this affect "
                "resource groups and resources inside that subscription?",
        "options": [
            {"id": "A", "text": "It is inherited by all resource groups and resources in the subscription"},
            {"id": "B", "text": "It applies only to the subscription object and to no child resources"},
            {"id": "C", "text": "It must be reassigned individually on every resource group"},
            {"id": "D", "text": "It overrides any more privileged role assigned at a narrower scope"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure RBAC assignments are inherited downward, so a role granted at the subscription scope "
                       "applies to every resource group and resource beneath it.",
            "distractors": {
                "B": "RBAC flows downward; a subscription-level assignment reaches child resource groups and resources.",
                "C": "Inheritance makes per-resource-group reassignment unnecessary for the inherited permissions.",
                "D": "Azure RBAC is additive; a broader assignment never strips a more privileged role granted at a "
                     "narrower scope.",
            },
            "exam_pattern": "RBAC scopes nest (management group > subscription > resource group > resource); permissions "
                            "are inherited downward and are additive.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure RBAC scope and inheritance"],
    },
    {
        "id": "az500-id-014", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_rbac_pim", "difficulty": 3, "type": "mcq",
        "stem": "An engineer holds the Microsoft Entra User Administrator directory role but has no Azure "
                "RBAC assignment on any subscription. What can they do?",
        "options": [
            {"id": "A", "text": "Manage virtual machines and storage accounts in the subscription"},
            {"id": "B", "text": "Manage users and some directory objects in Microsoft Entra ID, but not Azure resources"},
            {"id": "C", "text": "Assign Azure RBAC roles at the subscription scope"},
            {"id": "D", "text": "Nothing, because Entra roles and Azure RBAC roles are the same system"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Entra directory roles such as User Administrator govern the directory/tenant (managing users, "
                       "groups, etc.), but grant no access to Azure resources, which require a separate Azure RBAC assignment.",
            "distractors": {
                "A": "Managing Azure resources requires an Azure RBAC role on the resource/scope, which they lack.",
                "C": "Assigning Azure roles requires Owner or User Access Administrator in Azure RBAC, not an Entra role.",
                "D": "Entra (directory) roles and Azure RBAC are separate systems with separate scopes, not the same.",
            },
            "exam_pattern": "Entra roles govern the directory/tenant; Azure RBAC governs Azure resources - distinct, "
                            "granted separately.",
        },
        "references": ["Microsoft Learn (AZ-500): Microsoft Entra roles vs Azure RBAC roles"],
    },
    {
        "id": "az500-id-015", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_rbac_pim", "difficulty": 2, "type": "mcq",
        "stem": "To enforce least privilege, administrators should hold no standing Owner access and "
                "instead request it only when needed, for a limited time with justification. How should you "
                "configure their assignment in Privileged Identity Management?",
        "options": [
            {"id": "A", "text": "Make them eligible for the role, activated on demand, rather than permanently active"},
            {"id": "B", "text": "Assign the Owner role as a permanently active assignment"},
            {"id": "C", "text": "Add them to Owner directly in Azure RBAC with no PIM involvement"},
            {"id": "D", "text": "Grant them the Reader role instead"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "An eligible PIM assignment grants no standing access; the user activates it just-in-time for "
                       "a bounded period with justification (and optionally MFA/approval), which is least privilege.",
            "distractors": {
                "B": "A permanently active assignment is standing access - the opposite of just-in-time least privilege.",
                "C": "A direct, always-on RBAC assignment bypasses PIM's time-bound activation and approval.",
                "D": "Reader cannot perform Owner tasks, so it fails the operational requirement.",
            },
            "exam_pattern": "Just-in-time privileged access = PIM eligible assignment the user activates; active = standing access.",
        },
        "references": ["Microsoft Learn (AZ-500): PIM eligible vs active assignments"],
    },
    {
        "id": "az500-id-016", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_rbac_pim", "difficulty": 3, "type": "mcq",
        "stem": "For a privileged PIM role you want every activation to be time-limited and to require the "
                "requester to supply a justification, pass MFA, and get an approver's sign-off. Which "
                "configuration achieves this?",
        "options": [
            {"id": "A", "text": "Convert the assignment to active with no expiration"},
            {"id": "B", "text": "Disable MFA on activation to speed access"},
            {"id": "C", "text": "On the eligible assignment, require MFA, require justification, require "
                               "approval, and set a maximum activation duration"},
            {"id": "D", "text": "Replace PIM with a standing Owner assignment plus an alert"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "PIM role settings let you require MFA, justification, and approval on activation and cap the "
                       "activation duration, enforcing time-bound, accountable privilege.",
            "distractors": {
                "A": "An active, non-expiring assignment removes the time limit and approval entirely.",
                "B": "Disabling MFA weakens the activation control the requirement explicitly asks for.",
                "D": "A standing Owner assignment defeats just-in-time access; an alert does not enforce approval or time limits.",
            },
            "exam_pattern": "PIM activation controls = require MFA + justification + approval, with a maximum duration "
                            "(and optional ticket info).",
        },
        "references": ["Microsoft Learn (AZ-500): Configure PIM role activation settings"],
    },
    {
        "id": "az500-id-017", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_rbac_pim", "difficulty": 2, "type": "mcq",
        "stem": "Auditors require periodic confirmation that privileged role holders still need their "
                "access, with recertification by the user or their manager. Which Microsoft Entra capability "
                "automates this recurring recertification?",
        "options": [
            {"id": "A", "text": "Conditional Access"},
            {"id": "B", "text": "Azure Policy"},
            {"id": "C", "text": "Resource locks"},
            {"id": "D", "text": "Access reviews"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Access reviews schedule recurring attestation of group membership, app access, or role "
                       "assignments, with reviewers (self, manager, or designated) approving or removing access.",
            "distractors": {
                "A": "Conditional Access governs sign-in conditions, not periodic recertification of role membership.",
                "B": "Azure Policy governs resource configuration, not attestation of user access.",
                "C": "Resource locks prevent deletion/modification of resources; they do not review access.",
            },
            "exam_pattern": "Recurring recertification/attestation of access = Entra access reviews (ID Governance / PIM).",
        },
        "references": ["Microsoft Learn (AZ-500): Microsoft Entra access reviews"],
    },
    {
        "id": "az500-id-018", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_rbac_pim", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: In Microsoft Entra Privileged Identity Management, a role assignment "
                "that a user must activate (with justification, and often MFA or approval) before it can be "
                "used - rather than one that is always on - is called an ________ assignment.",
        "correct": ["eligible"],
        "explanation": {
            "correct": "An eligible assignment grants no standing access; the user activates it just-in-time for a "
                       "limited period. An active assignment, by contrast, is always on.",
            "exam_pattern": "PIM: eligible = activate on demand (JIT); active = standing access.",
        },
        "references": ["Microsoft Learn (AZ-500): PIM eligible vs active assignments"],
    },

    # ===== az500_app_identity ===============================================
    {
        "id": "az500-id-019", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_app_identity", "difficulty": 2, "type": "mcq",
        "stem": "A single managed identity must be shared by three virtual machines so they all reach the "
                "same storage account under one set of role assignments, and it must survive if any one VM "
                "is deleted. Which identity type fits?",
        "options": [
            {"id": "A", "text": "A system-assigned managed identity on each VM"},
            {"id": "B", "text": "One user-assigned managed identity attached to all three VMs"},
            {"id": "C", "text": "A service principal with a client secret embedded in code"},
            {"id": "D", "text": "The VM's local administrator account"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A user-assigned managed identity is a standalone resource that can be attached to many "
                       "resources and has its own lifecycle, so it is shared across the VMs and survives any single VM's deletion.",
            "distractors": {
                "A": "System-assigned identities are 1:1 with a resource and deleted with it, so they cannot be shared "
                     "or outlive the VM.",
                "C": "Embedding a secret in code is a credential-management risk and defeats the purpose of managed identities.",
                "D": "A local admin account is not an Entra identity and cannot be granted Azure RBAC to storage.",
            },
            "exam_pattern": "Shared/reusable, lifecycle-independent identity = user-assigned managed identity; "
                            "system-assigned = 1:1, tied to one resource's lifecycle.",
        },
        "references": ["Microsoft Learn (AZ-500): Managed identities - system-assigned vs user-assigned"],
    },
    {
        "id": "az500-id-020", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_app_identity", "difficulty": 1, "type": "mcq",
        "stem": "What is the primary security benefit of using a managed identity for an Azure web app "
                "that needs to read secrets from Azure Key Vault?",
        "options": [
            {"id": "A", "text": "No credentials are stored in code or configuration; Azure issues and rotates them automatically"},
            {"id": "B", "text": "It disables all network access to the Key Vault"},
            {"id": "C", "text": "It encrypts the Key Vault contents with a customer-managed key"},
            {"id": "D", "text": "It grants the app Owner rights on the subscription"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A managed identity lets the app authenticate to Entra ID and Key Vault with no secret stored "
                       "anywhere; Azure manages and rotates the underlying credential.",
            "distractors": {
                "B": "A managed identity authenticates the app; it does not configure the Key Vault's networking.",
                "C": "Managed identities handle authentication, not the vault's encryption-key configuration.",
                "D": "You grant a managed identity least-privilege access (for example, Key Vault Secrets User), not subscription Owner.",
            },
            "exam_pattern": "Managed identity = no secrets in code; Azure handles credential issuance/rotation. Pair "
                            "with least-privilege RBAC.",
        },
        "references": ["Microsoft Learn (AZ-500): What are managed identities for Azure resources"],
    },
    {
        "id": "az500-id-021", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_app_identity", "difficulty": 3, "type": "mcq",
        "stem": "You register a new application in Microsoft Entra ID. Which statement correctly describes "
                "the objects created and their relationship?",
        "options": [
            {"id": "A", "text": "Only a service principal is created; there is no application object"},
            {"id": "B", "text": "An application object is created in every tenant that uses the app, with no service principal"},
            {"id": "C", "text": "A single application (registration) object defines the app globally, and a "
                               "service principal is created in each tenant to represent it locally for sign-in and permissions"},
            {"id": "D", "text": "App registrations and enterprise applications are unrelated and never linked"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The app registration creates one global application object (the blueprint) in the home "
                       "tenant; a service principal (the enterprise application) is created in each tenant where the app "
                       "is used to hold its local identity, sign-in, and permission grants.",
            "distractors": {
                "A": "Registration creates both an application object and a service principal, not a service principal alone.",
                "B": "The application object is a single global definition in the home tenant; it is not duplicated per tenant.",
                "D": "The enterprise application is the service principal (local instance) of the registration; they are linked.",
            },
            "exam_pattern": "App registration = global application object (blueprint); service principal / enterprise "
                            "application = the local tenant instance that gets permissions and sign-in.",
        },
        "references": ["Microsoft Learn (AZ-500): Application and service principal objects in Microsoft Entra ID"],
    },
    {
        "id": "az500-id-022", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_app_identity", "difficulty": 2, "type": "mcq",
        "stem": "A third-party app requests Microsoft Graph permissions that would read data for all users "
                "in the tenant. You must stop individual users from approving such tenant-wide access "
                "themselves. Which approach enforces this?",
        "options": [
            {"id": "A", "text": "Delete the app registration after each use"},
            {"id": "B", "text": "Give every user the Global Administrator role"},
            {"id": "C", "text": "Add the app to a dynamic group"},
            {"id": "D", "text": "Restrict user consent and require admin consent (with the admin consent "
                               "workflow) for high-privilege or unverified apps"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Configuring user consent settings to restrict or disable user consent, and routing requests "
                       "through the admin consent workflow, ensures only an administrator can grant privileged or tenant-wide permissions.",
            "distractors": {
                "A": "Deleting registrations is not a consent control and is impractical for governing third-party apps.",
                "B": "Granting everyone Global Administrator is severe over-privilege and would let anyone consent to anything.",
                "C": "Dynamic groups automate membership; they do not govern application consent.",
            },
            "exam_pattern": "Restrict user consent + require admin consent (and use the admin consent workflow) to "
                            "limit illicit-consent/OAuth attacks.",
        },
        "references": ["Microsoft Learn (AZ-500): Configure user and admin consent / consent framework"],
    },
    {
        "id": "az500-id-023", "exam": "az500", "domain": "az500_identity_access",
        "subtopic": "az500_app_identity", "difficulty": 2, "type": "mcq",
        "stem": "An automation service principal currently authenticates with a long-lived client secret "
                "kept in a pipeline variable. Which change most improves its credential security?",
        "options": [
            {"id": "A", "text": "Replace the client secret with a certificate credential (or a managed "
                               "identity where supported) and rotate it regularly"},
            {"id": "B", "text": "Extend the client secret's expiration to several years to avoid rotation"},
            {"id": "C", "text": "Reuse the same secret across all automation accounts for consistency"},
            {"id": "D", "text": "Grant the service principal Owner so it never fails on permissions"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Certificate credentials are stronger than shared client secrets, and a managed identity "
                       "removes the stored credential entirely where it can be used; both, with rotation, reduce exposure.",
            "distractors": {
                "B": "Lengthening the secret's lifetime increases exposure if it leaks; it does not improve security.",
                "C": "Reusing one secret widens the blast radius and breaks isolation if it is compromised.",
                "D": "Over-privileging to Owner violates least privilege and is unrelated to credential strength.",
            },
            "exam_pattern": "Prefer managed identities; otherwise use certificate credentials over client secrets, keep "
                            "least privilege, and rotate.",
        },
        "references": ["Microsoft Learn (AZ-500): Secure service principals and application credentials"],
    },
]
