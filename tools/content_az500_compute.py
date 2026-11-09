"""Microsoft AZ-500 (Azure Security Engineer) pool - Domain 3: Secure Compute, Storage, and Databases.

Original, objective-aligned practice items for the four subtopics tracked in CertLab:
  * az500_compute_security   - VM disk encryption (Azure Disk Encryption vs
                               encryption at host), Microsoft Defender for Servers
                               plans, and container/AKS security with Defender for
                               Containers.
  * az500_storage_security   - SAS token types (user delegation vs service vs
                               account), Microsoft Entra authorization for Blob,
                               the storage firewall, disabling Shared Key, and
                               data protection (soft delete, immutable/WORM).
  * az500_database_security  - Azure SQL Transparent Data Encryption, Always
                               Encrypted, Dynamic Data Masking, Microsoft Entra
                               authentication, and Microsoft Defender for SQL.
  * az500_key_vault          - Key Vault access policies vs Azure RBAC, soft
                               delete and purge protection, Managed HSM, and
                               storing secrets/keys/certificates for managed-
                               identity access.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), and the authored answer key is spread across A/B/C/D
rather than defaulting to "A"; every wrong option carries a distractor note, and
each item names the Microsoft Learn area it draws on. Current product names are
used throughout (Microsoft Defender for Cloud / Defender for Servers / Defender
for SQL). Items are original and aligned to the public AZ-500 objectives - never
real or memorized exam items.
"""

QUESTIONS = [
    # ===== az500_compute_security ===========================================
    {
        "id": "az500-comp-001", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_compute_security", "difficulty": 2, "type": "mcq",
        "stem": "You must encrypt the OS and data disk volumes of existing Azure VMs using BitLocker on "
                "Windows and dm-crypt on Linux, with the encryption keys stored in Azure Key Vault. Which "
                "capability provides this?",
        "options": [
            {"id": "A", "text": "Platform storage service encryption (SSE) for managed disks only"},
            {"id": "B", "text": "Azure Disk Encryption (ADE)"},
            {"id": "C", "text": "Transparent Data Encryption (TDE)"},
            {"id": "D", "text": "Always Encrypted"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Azure Disk Encryption uses BitLocker (Windows) or dm-crypt (Linux) inside the guest to "
                       "encrypt OS and data volumes, with the encryption keys and secrets stored in Azure Key Vault.",
            "distractors": {
                "A": "Platform SSE automatically encrypts managed disks at rest with platform-managed keys, but it is "
                     "not in-guest BitLocker/dm-crypt volume encryption with keys you control in Key Vault.",
                "C": "TDE encrypts databases (such as Azure SQL) at rest, not VM OS/data volumes.",
                "D": "Always Encrypted protects sensitive database columns from the database engine, not VM disk volumes.",
            },
            "exam_pattern": "Guest volume encryption with BitLocker/dm-crypt + keys in Key Vault = Azure Disk Encryption (ADE).",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Disk Encryption for virtual machines"],
    },
    {
        "id": "az500-comp-002", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_compute_security", "difficulty": 3, "type": "mcq",
        "stem": "You want VM temp disks, OS/data disk caches, and disk data encrypted at the Azure host "
                "itself (end to end, before data leaves the host) without running an in-guest encryption "
                "agent. Which feature should you enable?",
        "options": [
            {"id": "A", "text": "Encryption at host"},
            {"id": "B", "text": "Azure Disk Encryption (ADE)"},
            {"id": "C", "text": "A customer-managed key on a storage account firewall"},
            {"id": "D", "text": "Just-in-time VM access"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Encryption at host encrypts the VM's temp disk, disk caches, and data flows at the host, with "
                       "no in-guest agent, providing end-to-end encryption before data leaves the host.",
            "distractors": {
                "B": "ADE encrypts volumes inside the guest OS with BitLocker/dm-crypt (an in-guest agent), not at the host.",
                "C": "Storage account firewalls/CMKs do not encrypt VM host caches or temp disks.",
                "D": "JIT controls management-port exposure; it is not disk encryption.",
            },
            "exam_pattern": "Host-level, agentless end-to-end disk/cache/temp encryption = encryption at host; in-guest "
                            "BitLocker/dm-crypt = Azure Disk Encryption.",
        },
        "references": ["Microsoft Learn (AZ-500): Encryption at host vs Azure Disk Encryption"],
    },
    {
        "id": "az500-comp-003", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_compute_security", "difficulty": 2, "type": "mcq",
        "stem": "You enable Microsoft Defender for Servers to get endpoint detection and response on your "
                "VMs, plus file integrity monitoring and just-in-time VM access. These capabilities beyond "
                "core EDR are provided by which plan?",
        "options": [
            {"id": "A", "text": "The free foundational CSPM tier"},
            {"id": "B", "text": "Defender for Servers Plan 1 only"},
            {"id": "C", "text": "Microsoft Entra ID P2"},
            {"id": "D", "text": "Defender for Servers Plan 2"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Defender for Servers Plan 2 provides everything in Plan 1 plus file integrity monitoring, "
                       "just-in-time VM access, agentless scanning, OS configuration assessment, and more.",
            "distractors": {
                "A": "Foundational CSPM is free posture management; it does not provide server EDR, FIM, or JIT.",
                "B": "Plan 1 focuses on EDR via the Defender for Endpoint integration; FIM and JIT are Plan 2 features.",
                "C": "Entra ID P2 covers identity features (PIM, ID Protection), not server workload protection.",
            },
            "exam_pattern": "Defender for Servers Plan 1 = EDR (Defender for Endpoint integration); Plan 2 adds JIT, "
                            "file integrity monitoring, agentless scanning, and OS config assessment.",
        },
        "references": ["Microsoft Learn (AZ-500): Select a Defender for Servers plan"],
    },
    {
        "id": "az500-comp-004", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_compute_security", "difficulty": 2, "type": "mcq",
        "stem": "Before images are deployed to Azure Kubernetes Service, you must scan images in Azure "
                "Container Registry for known vulnerabilities and detect runtime threats in the cluster. "
                "Which Defender for Cloud plan provides this?",
        "options": [
            {"id": "A", "text": "Defender for Servers"},
            {"id": "B", "text": "Defender for Storage"},
            {"id": "C", "text": "Defender for Containers"},
            {"id": "D", "text": "Defender for Key Vault"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Microsoft Defender for Containers scans container registry images for vulnerabilities and "
                       "provides runtime threat detection for Kubernetes clusters such as AKS.",
            "distractors": {
                "A": "Defender for Servers protects VM-based workloads, not container registry images or AKS runtime.",
                "B": "Defender for Storage detects threats to storage accounts, not container images.",
                "D": "Defender for Key Vault detects anomalous vault access, not container vulnerabilities.",
            },
            "exam_pattern": "Container registry image scanning + Kubernetes runtime threat detection = Microsoft "
                            "Defender for Containers.",
        },
        "references": ["Microsoft Learn (AZ-500): Microsoft Defender for Containers"],
    },
    {
        "id": "az500-comp-005", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_compute_security", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: Azure Disk ________ uses BitLocker on Windows and dm-crypt on Linux to "
                "encrypt the operating-system and data disk volumes of a virtual machine, with its keys held "
                "in Azure Key Vault.",
        "correct": ["encryption"],
        "explanation": {
            "correct": "Azure Disk Encryption (ADE) encrypts VM OS and data volumes using BitLocker (Windows) or "
                       "dm-crypt (Linux), storing the keys and secrets in Azure Key Vault.",
            "exam_pattern": "ADE = Azure Disk Encryption; in-guest BitLocker/dm-crypt with keys in Key Vault.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Disk Encryption for virtual machines"],
    },

    # ===== az500_storage_security ===========================================
    {
        "id": "az500-comp-006", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_storage_security", "difficulty": 3, "type": "mcq",
        "stem": "You must issue a time-limited SAS for a blob container and want it signed with Microsoft "
                "Entra credentials rather than the storage account key, so it can be revoked by revoking the "
                "identity and does not depend on the account key. Which SAS type should you use?",
        "options": [
            {"id": "A", "text": "An account SAS"},
            {"id": "B", "text": "A user delegation SAS"},
            {"id": "C", "text": "A service SAS"},
            {"id": "D", "text": "A stored access policy on the account key"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "A user delegation SAS is signed with a key obtained from Microsoft Entra credentials (not the "
                       "account key), is the most secure SAS type, and has a maximum 7-day lifetime tied to that delegation key.",
            "distractors": {
                "A": "An account SAS is signed with the storage account key and can span services; it is not secured "
                     "with Entra credentials.",
                "C": "A service SAS is also signed with the account key and limited to one service; it is not Entra-secured.",
                "D": "A stored access policy constrains a service SAS but is still account-key based, not Entra-signed.",
            },
            "exam_pattern": "Most secure SAS = user delegation SAS (signed with Entra credentials, max 7 days); account "
                            "and service SAS are signed with the account key.",
        },
        "references": ["Microsoft Learn (AZ-500): Grant limited access with SAS - user delegation SAS"],
    },
    {
        "id": "az500-comp-007", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_storage_security", "difficulty": 2, "type": "mcq",
        "stem": "Which statement correctly distinguishes an account SAS from a service SAS in Azure Storage?",
        "options": [
            {"id": "A", "text": "An account SAS can delegate access to multiple services (such as Blob and Queue) and "
                               "to service-level operations, while a service SAS is limited to a single service"},
            {"id": "B", "text": "A service SAS can span multiple services, while an account SAS is limited to one"},
            {"id": "C", "text": "Both are signed with Microsoft Entra credentials"},
            {"id": "D", "text": "Neither type can be time-limited"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "The account SAS is the broader token: it can cover multiple services and service-level "
                       "operations, whereas a service SAS is scoped to one service. Both are signed with the account key.",
            "distractors": {
                "B": "This is reversed; the account SAS is the broader of the two.",
                "C": "Both the account and service SAS are signed with the storage account key, not Entra credentials "
                     "(that is the user delegation SAS).",
                "D": "Both SAS types are time-limited via their start/expiry parameters.",
            },
            "exam_pattern": "Account SAS = multiple services + service-level ops (account-key signed); service SAS = one "
                            "service (account-key signed); user delegation SAS = Entra-signed.",
        },
        "references": ["Microsoft Learn (AZ-500): Types of shared access signatures"],
    },
    {
        "id": "az500-comp-008", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_storage_security", "difficulty": 2, "type": "mcq",
        "stem": "Instead of distributing storage account keys, you want an application's managed identity to "
                "read and write blobs, authorized by Microsoft Entra ID with least privilege. Which "
                "assignment accomplishes this?",
        "options": [
            {"id": "A", "text": "Grant the identity the Owner role on the subscription"},
            {"id": "B", "text": "Share the account key (key1) with the application"},
            {"id": "C", "text": "Assign the built-in Storage Blob Data Contributor role to the identity at the container "
                               "or account scope"},
            {"id": "D", "text": "Create a service SAS and embed it in the app"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Storage Blob Data Contributor is the Entra data-plane role that grants read/write to blob data; "
                       "assigning it to the managed identity at the needed scope gives least-privilege Entra-authorized access.",
            "distractors": {
                "A": "Subscription Owner is massive over-privilege and is not the data-plane role for blob access.",
                "B": "Sharing the account key is exactly the practice you are trying to avoid, and it grants full access.",
                "D": "A service SAS is account-key based, not Entra authorization, and is not least-privilege role-based access.",
            },
            "exam_pattern": "Entra-authorized blob data access = assign a Storage Blob Data role (Reader/Contributor/"
                            "Owner) to the identity; avoid account keys.",
        },
        "references": ["Microsoft Learn (AZ-500): Authorize access to blobs using Microsoft Entra ID"],
    },
    {
        "id": "az500-comp-009", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_storage_security", "difficulty": 2, "type": "mcq",
        "stem": "You must ensure a storage account accepts connections only from a specific virtual network "
                "and a short list of corporate public IP ranges, denying all other networks. Which storage "
                "feature enforces this?",
        "options": [
            {"id": "A", "text": "Blob soft delete"},
            {"id": "B", "text": "Transparent Data Encryption"},
            {"id": "C", "text": "A stored access policy"},
            {"id": "D", "text": "The storage account firewall (allow selected networks/IP ranges, default deny)"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "The storage account firewall restricts access to selected virtual networks and IP ranges with a "
                       "default-deny posture (and can be combined with private endpoints).",
            "distractors": {
                "A": "Soft delete recovers deleted data; it does not restrict source networks.",
                "B": "TDE is a database encryption feature, not a storage network control.",
                "C": "A stored access policy manages SAS constraints, not account-level network filtering.",
            },
            "exam_pattern": "Restrict a storage account to selected VNets/IP ranges with default-deny = the storage "
                            "account firewall (plus private endpoints).",
        },
        "references": ["Microsoft Learn (AZ-500): Configure Azure Storage firewalls and virtual networks"],
    },
    {
        "id": "az500-comp-010", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_storage_security", "difficulty": 2, "type": "multi",
        "stem": "To protect blobs from accidental or malicious deletion and overwrite, which TWO storage "
                "capabilities should you enable? (Choose two.)",
        "options": [
            {"id": "A", "text": "Blob soft delete (and container soft delete)"},
            {"id": "B", "text": "Dynamic Data Masking"},
            {"id": "C", "text": "Immutable storage with a time-based retention policy (WORM)"},
            {"id": "D", "text": "A user-defined route"},
        ],
        "correct": ["A", "C"],
        "explanation": {
            "correct": "Soft delete lets you recover deleted blobs/containers within a retention window, and immutable "
                       "storage (WORM) with time-based retention or legal hold prevents data from being modified or deleted.",
            "distractors": {
                "B": "Dynamic Data Masking obscures sensitive data in SQL query results; it has nothing to do with blob retention.",
                "D": "A user-defined route controls network next-hops, not data protection.",
            },
            "exam_pattern": "Guard blobs from deletion/overwrite with soft delete, versioning, and immutable (WORM) "
                            "retention/legal hold.",
        },
        "references": ["Microsoft Learn (AZ-500): Data protection for Azure Blob Storage (soft delete, immutable storage)"],
    },
    {
        "id": "az500-comp-011", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_storage_security", "difficulty": 2, "type": "mcq",
        "stem": "Your security baseline mandates that applications authenticate to storage with Microsoft "
                "Entra ID and that storage account key access be eliminated wherever possible. Which setting "
                "enforces that the account keys can no longer be used for authorization?",
        "options": [
            {"id": "A", "text": "Set 'Allow storage account key access' to Disabled (disallow Shared Key authorization)"},
            {"id": "B", "text": "Enable blob soft delete"},
            {"id": "C", "text": "Rotate the account keys daily"},
            {"id": "D", "text": "Add a CanNotDelete lock to the account"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Disallowing Shared Key authorization (setting account key access to Disabled) forces all requests "
                       "to use Microsoft Entra authorization, eliminating key-based access.",
            "distractors": {
                "B": "Soft delete protects data from deletion; it does not disable key-based authentication.",
                "C": "Rotating keys keeps key authorization in use; it does not eliminate it.",
                "D": "A resource lock prevents deletion/modification of the resource; it does not block Shared Key authorization.",
            },
            "exam_pattern": "Enforce Entra-only data access by disallowing Shared Key authorization on the storage account.",
        },
        "references": ["Microsoft Learn (AZ-500): Prevent Shared Key authorization for Azure Storage"],
    },

    # ===== az500_database_security ==========================================
    {
        "id": "az500-comp-012", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_database_security", "difficulty": 2, "type": "mcq",
        "stem": "An Azure SQL Database must have its data files, log files, and backups encrypted at rest, "
                "transparently to applications and with no code changes. Which feature provides this?",
        "options": [
            {"id": "A", "text": "Always Encrypted"},
            {"id": "B", "text": "Dynamic Data Masking"},
            {"id": "C", "text": "Transparent Data Encryption (TDE)"},
            {"id": "D", "text": "A network security group"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "TDE encrypts the database data, log files, and backups at rest transparently to the application, "
                       "using a service-managed or customer-managed (BYOK) key.",
            "distractors": {
                "A": "Always Encrypted protects specific sensitive columns from the engine and needs client-side keys/"
                     "driver changes; it is not whole-database at-rest encryption.",
                "B": "Dynamic Data Masking only obfuscates data in query results; it does not encrypt data at rest.",
                "D": "An NSG filters network traffic; it does not encrypt database storage.",
            },
            "exam_pattern": "Whole-database encryption at rest, transparent to the app = TDE (service-managed or "
                            "customer-managed/BYOK key).",
        },
        "references": ["Microsoft Learn (AZ-500): Transparent Data Encryption for Azure SQL"],
    },
    {
        "id": "az500-comp-013", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_database_security", "difficulty": 3, "type": "mcq",
        "stem": "Regulations require that certain columns (such as national ID numbers) never appear in "
                "plaintext to the Azure SQL database engine or to database administrators, and are decrypted "
                "only inside the client application. Which feature meets this?",
        "options": [
            {"id": "A", "text": "Always Encrypted"},
            {"id": "B", "text": "Transparent Data Encryption (TDE)"},
            {"id": "C", "text": "Auditing"},
            {"id": "D", "text": "Dynamic Data Masking"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Always Encrypted keeps designated columns encrypted on the server and decrypts them only in the "
                       "client driver with keys the database engine never sees, so the engine and DBAs cannot read plaintext.",
            "distractors": {
                "B": "TDE encrypts at rest, but the engine processes plaintext in memory, so DBAs and the engine can see the data.",
                "C": "Auditing records access; it does not keep data encrypted from the engine or DBAs.",
                "D": "Dynamic Data Masking only masks data in result sets; the underlying data stays visible to privileged users and the engine.",
            },
            "exam_pattern": "Keep sensitive columns encrypted from the engine/DBAs and decrypt only client-side (data in "
                            "use) = Always Encrypted (client holds the keys).",
        },
        "references": ["Microsoft Learn (AZ-500): Always Encrypted for Azure SQL"],
    },
    {
        "id": "az500-comp-014", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_database_security", "difficulty": 2, "type": "mcq",
        "stem": "Support staff should see only the last four digits of credit-card numbers in query "
                "results, but the stored data must remain unchanged and privileged users should still see "
                "full values. Which Azure SQL feature fits, and what is its key limitation?",
        "options": [
            {"id": "A", "text": "Always Encrypted; it encrypts the column so no one can read it"},
            {"id": "B", "text": "Dynamic Data Masking; it obfuscates data in the result set only and is not a substitute "
                               "for encryption or access control"},
            {"id": "C", "text": "Transparent Data Encryption; it hides specific columns at rest"},
            {"id": "D", "text": "Auditing; it masks values in the audit log"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Dynamic Data Masking masks data in query results for unprivileged users while leaving stored "
                       "data unchanged, but it is a presentation-layer control only - not encryption or real access control.",
            "distractors": {
                "A": "Always Encrypted encrypts the column end to end; it does not provide role-based partial masking in results.",
                "C": "TDE encrypts the whole database at rest and does not mask specific fields in results.",
                "D": "Auditing records events; it does not mask returned query data.",
            },
            "exam_pattern": "Dynamic Data Masking = presentation-layer obfuscation in results only; it is not encryption, "
                            "and privileged users/queries can still reveal data.",
        },
        "references": ["Microsoft Learn (AZ-500): Dynamic Data Masking for Azure SQL"],
    },
    {
        "id": "az500-comp-015", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_database_security", "difficulty": 2, "type": "mcq",
        "stem": "You want to eliminate SQL logins with passwords on an Azure SQL Database and instead let "
                "administrators and apps authenticate with centrally governed, MFA-capable identities. Which "
                "approach should you configure?",
        "options": [
            {"id": "A", "text": "Enable TDE with a customer-managed key"},
            {"id": "B", "text": "Use the sa account for all access"},
            {"id": "C", "text": "Issue a service SAS to each user"},
            {"id": "D", "text": "Configure Microsoft Entra authentication (set an Entra admin) and use Entra identities "
                               "and managed identities"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Setting a Microsoft Entra admin and using Entra users, groups, and managed identities lets you "
                       "authenticate with centrally governed identities that can require MFA and Conditional Access, replacing SQL passwords.",
            "distractors": {
                "A": "TDE encrypts data at rest; it is unrelated to how users authenticate.",
                "B": "Relying on a shared high-privilege account is an anti-pattern and is not centrally governed or MFA-capable.",
                "C": "SAS tokens are a storage concept and do not apply to Azure SQL authentication.",
            },
            "exam_pattern": "Centralized, MFA-capable DB sign-in = Microsoft Entra authentication for Azure SQL (set the "
                            "Entra admin; use Entra users/groups/managed identities).",
        },
        "references": ["Microsoft Learn (AZ-500): Microsoft Entra authentication for Azure SQL"],
    },
    {
        "id": "az500-comp-016", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_database_security", "difficulty": 2, "type": "mcq",
        "stem": "You need vulnerability assessment scans and alerts for anomalous activities such as "
                "potential SQL injection and access from unusual locations on your Azure SQL databases. "
                "Which capability provides both?",
        "options": [
            {"id": "A", "text": "Microsoft Defender for SQL"},
            {"id": "B", "text": "Dynamic Data Masking"},
            {"id": "C", "text": "Transparent Data Encryption"},
            {"id": "D", "text": "A resource lock"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Microsoft Defender for SQL bundles a vulnerability assessment and advanced threat protection that "
                       "alerts on anomalous activities such as potential SQL injection and access from unusual locations.",
            "distractors": {
                "B": "Dynamic Data Masking obfuscates result data; it does not scan for vulnerabilities or detect threats.",
                "C": "TDE encrypts at rest; it provides no vulnerability assessment or threat alerts.",
                "D": "A resource lock prevents deletion/modification; it does not detect threats.",
            },
            "exam_pattern": "Vulnerability assessment + advanced threat protection (SQLi, anomalous access) for databases "
                            "= Microsoft Defender for SQL.",
        },
        "references": ["Microsoft Learn (AZ-500): Microsoft Defender for SQL"],
    },

    # ===== az500_key_vault ==================================================
    {
        "id": "az500-comp-017", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_key_vault", "difficulty": 3, "type": "mcq",
        "stem": "You are standardizing how permissions to an Azure Key Vault's secrets and keys are granted "
                "and want to manage vault data-plane access the same way as other Azure resources - with "
                "role assignments that can be scoped and inherited. Which permission model should you choose?",
        "options": [
            {"id": "A", "text": "The legacy vault access policy model"},
            {"id": "B", "text": "The Azure RBAC permission model for Key Vault"},
            {"id": "C", "text": "Shared Key authorization"},
            {"id": "D", "text": "A service SAS on the vault"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The Azure RBAC permission model lets you grant Key Vault data-plane access with role assignments "
                       "(for example, Key Vault Secrets User) that honor Azure scope and inheritance; Microsoft recommends it over access policies.",
            "distractors": {
                "A": "The access policy model grants permissions per vault and is not integrated with Azure RBAC scoping/inheritance.",
                "C": "Shared Key authorization is a storage-account concept, not a Key Vault model.",
                "D": "SAS tokens are a storage feature; Key Vault does not use SAS for access.",
            },
            "exam_pattern": "Key Vault has two permission models - legacy vault access policies and Azure RBAC; RBAC "
                            "(roles like Key Vault Secrets User) is the recommended, scope/inheritance-aware model.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Key Vault access policies vs Azure RBAC"],
    },
    {
        "id": "az500-comp-018", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_key_vault", "difficulty": 2, "type": "mcq",
        "stem": "To prevent an administrator - or an attacker who gains rights - from permanently and "
                "immediately destroying keys in a Key Vault, you must ensure deleted objects are recoverable "
                "for a retention period and cannot be purged early. Which settings achieve this?",
        "options": [
            {"id": "A", "text": "Disable soft delete and add a resource lock"},
            {"id": "B", "text": "Enable soft delete only"},
            {"id": "C", "text": "Enable soft delete and purge protection"},
            {"id": "D", "text": "Rotate the keys more frequently"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Soft delete makes deleted vaults/objects recoverable within the retention period, and purge "
                       "protection blocks early permanent deletion (purge) until that period elapses; together they stop immediate destruction.",
            "distractors": {
                "A": "Disabling soft delete removes recoverability entirely, the opposite of the goal.",
                "B": "Soft delete alone still allows a privileged user to purge within the retention window; purge "
                     "protection is needed to block early purge.",
                "D": "Rotation changes key material on a schedule; it does not prevent permanent deletion.",
            },
            "exam_pattern": "Soft delete = recover deleted vault/objects within retention; purge protection = block "
                            "permanent deletion until retention elapses.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Key Vault soft delete and purge protection"],
    },
    {
        "id": "az500-comp-019", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_key_vault", "difficulty": 3, "type": "mcq",
        "stem": "A compliance mandate requires cryptographic keys to be protected by single-tenant, FIPS "
                "140-2 Level 3 validated hardware security modules that your organization fully controls. "
                "Which Azure option meets this?",
        "options": [
            {"id": "A", "text": "Azure Key Vault Managed HSM"},
            {"id": "B", "text": "The Key Vault Standard tier with software-protected keys"},
            {"id": "C", "text": "Storage account customer-managed keys stored in a Standard vault"},
            {"id": "D", "text": "Dynamic Data Masking"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Azure Key Vault Managed HSM is a fully managed, single-tenant, highly available service that "
                       "protects keys with FIPS 140-2 Level 3 validated HSMs under the customer's control.",
            "distractors": {
                "B": "The Standard tier uses software-protected keys and does not meet single-tenant Level 3 HSM requirements.",
                "C": "Where the key is referenced does not change that a Standard vault is not a single-tenant Level 3 HSM.",
                "D": "Dynamic Data Masking is a database feature unrelated to key-protection hardware.",
            },
            "exam_pattern": "Single-tenant, fully controlled FIPS 140-2 Level 3 HSM = Azure Key Vault Managed HSM; "
                            "Premium vaults offer multi-tenant HSM-backed keys.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Key Vault Managed HSM"],
    },
    {
        "id": "az500-comp-020", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_key_vault", "difficulty": 1, "type": "mcq",
        "stem": "An application needs to retrieve a database connection string and a TLS certificate at "
                "runtime without storing either in its code. Which Azure service should hold these, and how "
                "should the app authenticate to it?",
        "options": [
            {"id": "A", "text": "A storage account accessed with the account key"},
            {"id": "B", "text": "An NSG accessed by IP allowlist"},
            {"id": "C", "text": "A SQL table protected by Dynamic Data Masking"},
            {"id": "D", "text": "Azure Key Vault, accessed using the app's managed identity with a least-privilege role"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Azure Key Vault centrally stores secrets, keys, and certificates; the app should read them using "
                       "its managed identity granted a least-privilege Key Vault role (for example, Key Vault Secrets User).",
            "distractors": {
                "A": "Storage accounts are not the secret-management service, and account keys are exactly the kind of "
                     "secret you should avoid embedding.",
                "B": "An NSG is a network filter; it does not store secrets or certificates.",
                "C": "A SQL table with masking is not a secret store and does not provide certificate management.",
            },
            "exam_pattern": "Centralize secrets/keys/certificates in Key Vault; let apps fetch them via a managed "
                            "identity with a least-privilege Key Vault role.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Key Vault - secrets, keys, and certificates"],
    },
    {
        "id": "az500-comp-021", "exam": "az500", "domain": "az500_compute_storage_db",
        "subtopic": "az500_key_vault", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: Azure Key Vault is a centralized service for safeguarding three kinds of "
                "objects: secrets (such as passwords and connection strings), cryptographic keys, and "
                "________ (such as TLS/SSL items it can also provision and auto-renew).",
        "correct": ["certificates", "certificate"],
        "explanation": {
            "correct": "Key Vault manages secrets, keys, and certificates; for certificates it can store, provision, "
                       "manage, and auto-renew TLS/SSL certificates in integration with certificate authorities.",
            "exam_pattern": "Key Vault safeguards secrets, keys, and certificates - one service for all three object types.",
        },
        "references": ["Microsoft Learn (AZ-500): Azure Key Vault - secrets, keys, and certificates"],
    },
]
