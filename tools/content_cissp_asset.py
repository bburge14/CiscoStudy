"""(ISC)² CISSP pool - Domain 2: Asset Security.

Original, CBK-aligned practice items for the four Asset Security subtopics:
  * cissp_data_classification      - classification schemes (government and
                                     commercial), what drives a label, and
                                     aggregation effects.
  * cissp_data_lifecycle           - data states (at rest / in transit / in use),
                                     retention, and secure disposal.
  * cissp_data_roles               - owner, custodian, steward, controller,
                                     processor, and data subject responsibilities.
  * cissp_data_protection_methods  - media sanitization, degaussing limits,
                                     tokenization, and data remanence.

Authoring rules match the other content_*.py pools: build_content.py shuffles
option order (seeded by id), so the keyed answer is not positionally biased,
every wrong option carries a distractor note, and each item cites the CISSP CBK
domain it draws on. Items are original and scenario-driven and never reproduce
real or memorized exam questions.
"""

QUESTIONS = [
    # ===== cissp_data_classification ========================================
    {
        "id": "cissp-asset-001", "exam": "cissp", "domain": "cissp_asset",
        "subtopic": "cissp_data_classification", "difficulty": 2, "type": "mcq",
        "stem": "In the U.S. government classification scheme, unauthorized disclosure of a particular "
                "data set would cause 'exceptionally grave damage' to national security. Which "
                "classification level applies?",
        "options": [
            {"id": "A", "text": "Confidential"},
            {"id": "B", "text": "Secret"},
            {"id": "C", "text": "Top Secret"},
            {"id": "D", "text": "Sensitive But Unclassified"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Top Secret is the level assigned when unauthorized disclosure would cause "
                       "'exceptionally grave damage' to national security.",
            "distractors": {
                "A": "Confidential applies when disclosure would cause 'damage' - the lowest classified tier.",
                "B": "Secret applies when disclosure would cause 'serious damage', one level below Top Secret.",
                "D": "Sensitive But Unclassified (Controlled Unclassified) is below Confidential and is not a "
                     "national-security damage tier.",
            },
            "exam_pattern": "Top Secret = exceptionally grave damage; Secret = serious damage; Confidential = damage.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 2 - Data classification schemes"],
    },
    {
        "id": "cissp-asset-002", "exam": "cissp", "domain": "cissp_asset",
        "subtopic": "cissp_data_classification", "difficulty": 2, "type": "mcq",
        "stem": "When an organization decides which classification label to assign to a data set, which "
                "factor should PRIMARILY drive that decision?",
        "options": [
            {"id": "A", "text": "The storage medium the data resides on"},
            {"id": "B", "text": "The value, sensitivity, and criticality of the data to the organization"},
            {"id": "C", "text": "The file format of the data"},
            {"id": "D", "text": "The department that created the data"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Classification is based on the data's value and the harm that its disclosure, "
                       "alteration, or loss would cause - its sensitivity and criticality - so controls match impact.",
            "distractors": {
                "A": "The storage medium is incidental; the same data keeps its classification wherever it is stored.",
                "C": "File format does not determine how sensitive the information is.",
                "D": "The originating department is not itself a measure of sensitivity or criticality.",
            },
            "exam_pattern": "Classify by value / sensitivity / criticality (impact of compromise), not by medium or format.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 2 - Classification criteria"],
    },
    {
        "id": "cissp-asset-003", "exam": "cissp", "domain": "cissp_asset",
        "subtopic": "cissp_data_classification", "difficulty": 2, "type": "mcq",
        "stem": "A private company labels data as Public, Internal, Confidential, and Restricted. What is "
                "the PRIMARY benefit of applying such a classification scheme?",
        "options": [
            {"id": "A", "text": "It ensures protective controls are applied commensurate with each data set's sensitivity"},
            {"id": "B", "text": "It guarantees that all data is encrypted regardless of label"},
            {"id": "C", "text": "It eliminates the need for access controls"},
            {"id": "D", "text": "It transfers data ownership to the custodian"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Classification lets the organization apply the right strength of controls to each data "
                       "set, protecting sensitive data cost-effectively rather than treating everything the same.",
            "distractors": {
                "B": "Classification guides control selection but does not by itself encrypt all data.",
                "C": "Classification drives access controls; it does not remove the need for them.",
                "D": "Classification does not change who owns the data; the owner remains accountable.",
            },
            "exam_pattern": "Classification matches control strength to data sensitivity (cost-effective protection).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 2 - Commercial classification"],
    },
    {
        "id": "cissp-asset-004", "exam": "cissp", "domain": "cissp_asset",
        "subtopic": "cissp_data_classification", "difficulty": 3, "type": "mcq",
        "stem": "Several individually Confidential records, when combined into one data set, reveal "
                "information that is far more sensitive than any single record. Which concern does this "
                "illustrate, and how may classification be affected?",
        "options": [
            {"id": "A", "text": "Polyinstantiation; the records should be duplicated at different levels"},
            {"id": "B", "text": "Inference only; no classification change is ever needed"},
            {"id": "C", "text": "Data remanence; the media must be purged before reuse"},
            {"id": "D", "text": "Aggregation; the combined data set may warrant a higher classification"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "Aggregation occurs when combining lower-sensitivity data yields a more sensitive "
                       "whole; the aggregated set may need to be reclassified at a higher level.",
            "distractors": {
                "A": "Polyinstantiation is a defensive technique that creates multiple versions of data, not "
                     "the problem being described.",
                "B": "Inference is deducing hidden facts from clues; the scenario describes combining records "
                     "(aggregation), and a reclassification may indeed be warranted.",
                "C": "Data remanence concerns residual data left on media, which is unrelated to combining records.",
            },
            "exam_pattern": "Aggregation - combining lower-classified data can create a higher-sensitivity whole.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 2 - Aggregation and classification"],
    },

    # ===== cissp_data_lifecycle =============================================
    {
        "id": "cissp-asset-005", "exam": "cissp", "domain": "cissp_asset",
        "subtopic": "cissp_data_lifecycle", "difficulty": 2, "type": "mcq",
        "stem": "An organization must protect sensitive records as they travel between a web client and "
                "the application server across the internet. Which data state is being protected, and "
                "which control is MOST appropriate?",
        "options": [
            {"id": "A", "text": "Data at rest; full-disk encryption"},
            {"id": "B", "text": "Data in transit; TLS"},
            {"id": "C", "text": "Data in use; secure memory enclaves"},
            {"id": "D", "text": "Data at rest; degaussing"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Data moving across a network is data in transit, best protected with transport "
                       "encryption such as TLS (or IPsec/VPN).",
            "distractors": {
                "A": "Full-disk encryption protects data at rest on storage, not data moving across the network.",
                "C": "Secure enclaves protect data in use (being processed in memory), not data in motion.",
                "D": "Degaussing is a media-sanitization method for data at rest, not a transit protection.",
            },
            "exam_pattern": "In transit = TLS/IPsec/VPN; at rest = storage encryption; in use = enclaves.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 2 - Data states and protection"],
    },
    {
        "id": "cissp-asset-006", "exam": "cissp", "domain": "cissp_asset",
        "subtopic": "cissp_data_lifecycle", "difficulty": 3, "type": "mcq",
        "stem": "A security architect notes that one data state is the MOST difficult to protect because "
                "the data must typically be decrypted and present in memory to be processed. Which state "
                "is this?",
        "options": [
            {"id": "A", "text": "Data at rest"},
            {"id": "B", "text": "Data in transit"},
            {"id": "C", "text": "Data in use"},
            {"id": "D", "text": "Data in archive"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "Data in use is being actively processed in memory and is usually decrypted at that "
                       "moment, making it the hardest state to protect; emerging controls include secure "
                       "enclaves and homomorphic encryption.",
            "distractors": {
                "A": "Data at rest can be protected effectively with storage encryption.",
                "B": "Data in transit can be protected with transport encryption such as TLS.",
                "D": "Archived data is a form of data at rest and can likewise be encrypted.",
            },
            "exam_pattern": "Data in use (in memory/processing) is the hardest state to protect.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 2 - Data states"],
    },
    {
        "id": "cissp-asset-007", "exam": "cissp", "domain": "cissp_asset",
        "subtopic": "cissp_data_lifecycle", "difficulty": 2, "type": "mcq",
        "stem": "At the end of the data lifecycle, an organization must dispose of media holding "
                "sensitive data so the information cannot be reconstructed. Which objective is the PRIMARY "
                "security driver of the disposal method chosen?",
        "options": [
            {"id": "A", "text": "Preventing data remanence from allowing recovery of the information"},
            {"id": "B", "text": "Reducing storage costs"},
            {"id": "C", "text": "Reclaiming rack space in the data center"},
            {"id": "D", "text": "Improving backup performance"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Secure disposal (clear, purge, or destroy) targets data remanence so that retired "
                       "media cannot be used to recover the sensitive data.",
            "distractors": {
                "B": "Lower storage cost is an operational benefit, not the security driver of secure disposal.",
                "C": "Reclaiming space is operational, not the reason sanitization must be thorough.",
                "D": "Backup performance is unrelated to the security purpose of media disposal.",
            },
            "exam_pattern": "Secure disposal addresses data remanence - ensure data cannot be reconstructed after retirement.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 2 - Secure data disposal"],
    },
    {
        "id": "cissp-asset-008", "exam": "cissp", "domain": "cissp_asset",
        "subtopic": "cissp_data_lifecycle", "difficulty": 2, "type": "mcq",
        "stem": "An organization is defining how long each category of records must be kept before it may "
                "be disposed of. Which policy MOST directly governs this decision?",
        "options": [
            {"id": "A", "text": "Acceptable use policy"},
            {"id": "B", "text": "Change management policy"},
            {"id": "C", "text": "Password policy"},
            {"id": "D", "text": "Data retention policy"},
        ],
        "correct": ["D"],
        "explanation": {
            "correct": "The data retention policy defines how long records are kept and when they are "
                       "disposed of, driven by legal, regulatory, and business requirements.",
            "distractors": {
                "A": "An acceptable use policy governs how users may use systems, not record retention.",
                "B": "A change management policy governs controlled changes to systems, not retention periods.",
                "C": "A password policy governs credential rules, unrelated to how long data is kept.",
            },
            "exam_pattern": "Retention periods and disposal timing = data retention policy (legal/regulatory/business driven).",
        },
        "references": ["(ISC)² CISSP CBK: Domain 2 - Data retention"],
    },

    # ===== cissp_data_roles =================================================
    {
        "id": "cissp-asset-009", "exam": "cissp", "domain": "cissp_asset",
        "subtopic": "cissp_data_roles", "difficulty": 2, "type": "mcq",
        "stem": "A data owner has classified a data set and defined its access requirements. Which "
                "responsibility now falls to the data CUSTODIAN?",
        "options": [
            {"id": "A", "text": "Deciding the data's classification level"},
            {"id": "B", "text": "Implementing and maintaining protective controls such as backups and access settings"},
            {"id": "C", "text": "Determining the purpose for which personal data is processed"},
            {"id": "D", "text": "Approving the budget for the security program"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "The custodian carries out the technical protection of the data day to day - applying "
                       "the access settings, performing backups, and maintaining the controls the owner specified.",
            "distractors": {
                "A": "Classification is the owner's decision, not the custodian's.",
                "C": "Determining the purpose of processing is the data controller's role under privacy law.",
                "D": "Budget approval is a senior-management governance function.",
            },
            "exam_pattern": "Owner decides (classify, define access); custodian implements and maintains the controls.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 2 - Data owner vs custodian"],
    },
    {
        "id": "cissp-asset-010", "exam": "cissp", "domain": "cissp_asset",
        "subtopic": "cissp_data_roles", "difficulty": 2, "type": "mcq",
        "stem": "An organization assigns a role responsible for the business context and quality of a "
                "data set - ensuring the data is accurate, consistent, and fit for its business purpose. "
                "Which role is this?",
        "options": [
            {"id": "A", "text": "Data custodian"},
            {"id": "B", "text": "Data processor"},
            {"id": "C", "text": "Data steward"},
            {"id": "D", "text": "Data subject"},
        ],
        "correct": ["C"],
        "explanation": {
            "correct": "The data steward has business responsibility for the meaning, quality, and proper use "
                       "of data, ensuring it is accurate and fit for purpose.",
            "distractors": {
                "A": "The custodian handles technical safeguarding (backups, access), not business data quality.",
                "B": "A processor processes personal data on a controller's behalf, a privacy-law role.",
                "D": "The data subject is the individual the personal data describes.",
            },
            "exam_pattern": "Data steward = business responsibility for data quality, meaning, and proper use.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 2 - Data roles"],
    },
    {
        "id": "cissp-asset-011", "exam": "cissp", "domain": "cissp_asset",
        "subtopic": "cissp_data_roles", "difficulty": 2, "type": "mcq",
        "stem": "A payroll-processing vendor handles employee personal data strictly according to the "
                "written instructions of the client company that hired it. In data-protection terms, the "
                "vendor is acting as the:",
        "options": [
            {"id": "A", "text": "Data processor"},
            {"id": "B", "text": "Data controller"},
            {"id": "C", "text": "Data owner"},
            {"id": "D", "text": "Data steward"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "A processor handles personal data on behalf of, and under the instructions of, the "
                       "controller; the vendor acting solely on the client's instructions is the processor.",
            "distractors": {
                "B": "The controller is the client company that determines the purpose and means of processing.",
                "C": "Data owner is an internal accountability role at the controller, not the external vendor.",
                "D": "The steward manages data quality and business context, not third-party processing.",
            },
            "exam_pattern": "Acts only on another party's instructions = processor; decides purpose/means = controller.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 2 - Controller vs processor"],
    },
    {
        "id": "cissp-asset-012", "exam": "cissp", "domain": "cissp_asset",
        "subtopic": "cissp_data_roles", "difficulty": 1, "type": "fill",
        "stem": "Fill in the blank: Under privacy regulations such as the GDPR, the identified or "
                "identifiable individual whose personal data is being collected and processed is called "
                "the data ________.",
        "correct": ["subject"],
        "explanation": {
            "correct": "The data subject is the living individual to whom the personal data relates.",
            "exam_pattern": "Data subject = the individual the data is about; controller decides processing; "
                            "processor carries it out.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 2 - Privacy roles"],
    },

    # ===== cissp_data_protection_methods ====================================
    {
        "id": "cissp-asset-013", "exam": "cissp", "domain": "cissp_asset",
        "subtopic": "cissp_data_protection_methods", "difficulty": 3, "type": "mcq",
        "stem": "An organization plans to sanitize decommissioned solid-state drives (SSDs) that stored "
                "confidential data. Why is degaussing a POOR choice for these drives, and what is a better "
                "option?",
        "options": [
            {"id": "A", "text": "Degaussing is too slow; a single overwrite pass is sufficient for SSDs"},
            {"id": "B", "text": "Degaussing relies on magnetic fields and does not reliably erase flash-based SSDs; cryptographic erase or physical destruction is preferred"},
            {"id": "C", "text": "Degaussing physically melts the drive; a quick reformat is preferred"},
            {"id": "D", "text": "Degaussing only works on optical media; overwriting is preferred"},
        ],
        "correct": ["B"],
        "explanation": {
            "correct": "Degaussing erases magnetic media by disrupting magnetic domains; SSDs store data in "
                       "flash cells with no magnetic domains, so degaussing is ineffective. Cryptographic "
                       "erase (crypto-shredding) or physical destruction is appropriate.",
            "distractors": {
                "A": "A single overwrite is unreliable on SSDs because wear-leveling leaves data in spare cells.",
                "C": "Degaussing uses a magnetic field and does not melt drives.",
                "D": "Degaussing targets magnetic media (HDDs, tapes), not optical media.",
            },
            "exam_pattern": "Degaussing works on magnetic media only; for SSDs use cryptographic erase or physical destruction.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 2 - Media sanitization"],
    },
    {
        "id": "cissp-asset-014", "exam": "cissp", "domain": "cissp_asset",
        "subtopic": "cissp_data_protection_methods", "difficulty": 2, "type": "mcq",
        "stem": "To reduce the number of systems that handle live payment-card numbers, a retailer "
                "replaces each card number with a surrogate value that has no exploitable meaning, keeping "
                "the real value in a secured vault. Which technique is this?",
        "options": [
            {"id": "A", "text": "Tokenization"},
            {"id": "B", "text": "Hashing"},
            {"id": "C", "text": "Full-disk encryption"},
            {"id": "D", "text": "Steganography"},
        ],
        "correct": ["A"],
        "explanation": {
            "correct": "Tokenization substitutes sensitive data with a meaningless token and keeps the real "
                       "value in a protected token vault, reducing the systems in scope (for example, for PCI DSS).",
            "distractors": {
                "B": "Hashing is one-way and cannot return the original value from a vault for later use.",
                "C": "Full-disk encryption protects stored data but does not substitute a surrogate value in processing.",
                "D": "Steganography hides data within other media; it is not a surrogate-value substitution.",
            },
            "exam_pattern": "Tokenization swaps sensitive data for a meaningless surrogate, keeping the real value vaulted.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 2 - Tokenization"],
    },
    {
        "id": "cissp-asset-015", "exam": "cissp", "domain": "cissp_asset",
        "subtopic": "cissp_data_protection_methods", "difficulty": 2, "type": "fill",
        "stem": "Fill in the blank: The residual physical representation of data that can remain on "
                "storage media even after attempts to erase or delete it is known as data ________.",
        "correct": ["remanence"],
        "explanation": {
            "correct": "Data remanence is the leftover data that persists after deletion or formatting, which "
                       "is why those actions alone are insufficient for sensitive media.",
            "exam_pattern": "Data remanence is why 'delete' or 'format' is not enough; use clear, purge, or destroy per media type.",
        },
        "references": ["(ISC)² CISSP CBK: Domain 2 - Data remanence"],
    },
]
