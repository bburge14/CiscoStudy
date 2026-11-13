# Emerging Technology & AI Security

The newest domain of SecurityX is also the fastest-moving: securing artificial
intelligence and other emerging technology. An architect must reason about threats
that did not exist a few years ago — models that can be poisoned or manipulated,
assistants that can be hijacked through the content they read, and synthetic media
convincing enough to authorize a wire transfer. This lesson teaches the threat
landscape and the defensive controls, at the level of someone setting AI
governance.

## Why AI changes the threat model

Traditional software does what its code says. A machine-learning model does what its
**data and training** taught it, and a large language model (LLM) acts on
**untrusted natural-language input** — including text it reads from documents,
web pages, and tools. That creates attack surfaces with no classical equivalent:
the *data* is an attack vector, and the *instructions* and the *data* arrive on the
same channel.

> With AI, the training data and the prompt are part of the attack surface. You can
> no longer assume input is inert or that behavior is fixed by code.

## Attacks against AI systems

### Prompt injection

An LLM assistant that can call tools and read documents will faithfully follow
instructions hidden in the content it processes. In **indirect prompt injection**,
an attacker hides instructions inside a document (or web page, or email) so that
when the model summarizes or acts on it, it executes the attacker's commands —
exfiltrating data or misusing its tools. The model cannot reliably tell *data* from
*instructions*.

Defenses are layered, because no single filter is reliable:

- **Treat all model input as untrusted** and keep the model's privileges minimal.
- **Least-privilege tool access** and **human approval** for sensitive tool actions,
  so a hijacked model cannot act destructively on its own.
- **Input/output filtering and segregation** of system instructions from user/data
  content, plus **sandboxing** of tool execution.

> Hidden instructions in a document that the model then obeys = **(indirect) prompt
> injection**. Contain it with least-privilege tool access, human approval for
> sensitive actions, and sandboxing — not with a single input filter.

### Data poisoning and adversarial inputs

- **Data (training) poisoning** — an attacker submits crafted samples to a
  continuously retrained model (e.g., a fraud detector) so that, over time, it
  learns to **misclassify the attacker's activity as benign**. Defenses: vet and
  validate training data provenance, anomaly-detect poisoned samples, control who
  can contribute training data, and monitor for model-performance drift.
- **Adversarial / evasion attacks** — carefully perturbed inputs at inference time
  that fool a model (a slightly altered image misclassified). Defenses include
  adversarial training and robust input validation.
- **Model inversion / membership inference** — querying a model to reconstruct or
  confirm its sensitive training data. Defenses: limit outputs, differential
  privacy, access control.
- **Model theft / extraction** — stealing the model (weights) or cloning it via
  query probing. Defenses: protect the artifact, rate-limit and monitor the API.

### Synthetic media and deepfakes

Generative AI makes convincing fake audio and video. A finance team receiving a
video call that **looks and sounds like the CFO** authorizing an urgent multi-million
wire — a **deepfake** — is a now-real social-engineering vector. The best control
set is not technical detection alone but **process**:

- **Out-of-band verification / callback** to a known-good number for any high-value
  or unusual transaction.
- **Dual authorization** and defined approval thresholds for wire transfers.
- **Security awareness** training on deepfake and business-email-compromise (BEC)
  tactics.

> Against a deepfake-driven wire-fraud request, the strongest defense is
> **process**: out-of-band callback verification and dual authorization — not trying
> to spot the fake in real time.

## Governing and defending AI

### Securing the AI you build and buy

- **AI supply chain** — models and datasets come from third parties; apply the same
  provenance, SBOM-style inventory, and vendor assessment you apply to software.
- **AI governance** — policy for acceptable use, data handling in prompts (no
  secrets into public models), model risk assessment, and human oversight. Frame it
  with references like the **NIST AI Risk Management Framework (AI RMF)** and the
  **OWASP Top 10 for LLM Applications**.
- **Shadow AI** — employees pasting sensitive data into unsanctioned AI tools; a
  data-governance and **DLP/CASB** problem as much as an AI one.

### AI as a defensive tool — with caveats

AI also *helps* defenders: anomaly detection, alert triage, and summarization accel-
erate the SOC. But treat AI output as **advisory** — it can **hallucinate** and be
manipulated — so keep a human in the loop for consequential decisions.

## Other emerging technology

- **Quantum computing** — the driver behind the post-quantum migration (harvest-now,
  decrypt-later); quantum key distribution (QKD) is an adjacent, physics-based key
  exchange.
- **Blockchain / distributed ledger** — tamper-evident, decentralized records;
  useful for integrity and provenance, but smart-contract code is itself
  attackable.
- **Edge computing and 5G** expand the attack surface outward, reinforcing the need
  for zero-trust and strong device identity.

## Exam focus

- **Prompt injection** (esp. **indirect**, via hidden instructions in a document the
  model reads) is defended with **least-privilege tool access, human approval for
  sensitive actions, and sandboxing** — not a single filter.
- **Data/training poisoning** makes a retrained model misclassify attacker
  activity; defend with training-data validation/provenance and drift monitoring.
- Know the AI attack families: **adversarial/evasion**, **model inversion/membership
  inference**, and **model theft/extraction**, each with its matching control.
- Against **deepfake** wire-fraud, the best control is **process**: out-of-band
  callback verification + dual authorization + awareness training.
- Govern AI with **AI governance policy, provenance/AI supply-chain checks, and
  controls on shadow AI** (DLP/CASB); reference **NIST AI RMF** / **OWASP Top 10 for
  LLMs**. Treat AI output as advisory — it can **hallucinate**.
- **Quantum** drives PQC; **blockchain** offers tamper-evident integrity but
  attackable smart contracts.
