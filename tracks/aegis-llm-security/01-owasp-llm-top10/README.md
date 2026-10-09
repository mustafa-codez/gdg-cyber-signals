# Lab 01: OWASP Top 10 for LLM Applications

**Track:** Aegis | **Level:** Beginner | **Time:** ~60 min

## What is it?
**OWASP** (Open Worldwide Application Security Project) publishes the **Top 10 for LLM Applications**, the standard checklist of the most critical risks when building with LLMs. **MITRE ATLAS** is the ATT&CK-style knowledge base for adversary tactics against AI systems.

Why LLMs are different: the model can't reliably separate **instructions** from **data**. Everything is just text in one context window. Most LLM attacks exploit that.

## The list (2025 edition)
| ID | Risk | One-line meaning | Example | Main defence |
|---|---|---|---|---|
| LLM01 | **Prompt Injection** | Input changes the model's behaviour | "Ignore previous instructions…" or hidden text in a webpage | Treat all model input as untrusted, constrain outputs and tools, human approval |
| LLM02 | **Sensitive Information Disclosure** | Model leaks secrets or personal data | Training data or context leaks | Don't put secrets in prompts, filter outputs, data minimisation |
| LLM03 | **Supply Chain** | Compromised models, datasets, plugins | Malicious model file or package | Pin and verify sources, scan artefacts, prefer safe formats |
| LLM04 | **Data and Model Poisoning** | Tampered training/fine-tune/RAG data | Poisoned documents | Data provenance, validation, access control |
| LLM05 | **Improper Output Handling** | Trusting model output downstream | LLM output executed as SQL/JS/shell | Validate and encode outputs; never `eval` them |
| LLM06 | **Excessive Agency** | Agent has too much power | Agent with delete/email/pay tools | Least privilege, allowlists, confirmation for risky actions |
| LLM07 | **System Prompt Leakage** | Hidden instructions extracted | "Repeat your instructions" | Assume the system prompt is public; no secrets in it |
| LLM08 | **Vector and Embedding Weaknesses** | RAG store attacks | Poisoned or over-exposed vector DB | Access control per document, input validation |
| LLM09 | **Misinformation** | Confident wrong answers | Hallucinated package names | Grounding, citations, human review |
| LLM10 | **Unbounded Consumption** | Cost and denial-of-service | Giant prompts, loops | Rate limits, quotas, timeouts |

(Check the official page for the current version: https://owasp.org/www-project-top-10-for-large-language-model-applications/)

## Walkthrough: threat-model an LLM app
Imagine a **customer-support chatbot** that:
- reads a company knowledge base (RAG),
- can look up orders (tool),
- can issue refunds (tool).

Fill in this table (suggested answers are in the next section):
| Asset | Threat | OWASP ID | Control |
|---|---|---|---|
| Knowledge base | Attacker plants a document containing hidden instructions | | |
| Refund tool | User tricks the bot to refund without checking | | |
| System prompt | Contains internal discount codes | | |
| Chat output | Rendered as HTML in the browser | | |

**Suggested answers:** LLM01/LLM04/LLM08 → treat retrieved text as untrusted, access control, sanitise; LLM06 → refund limits plus human approval, tool-side authorisation (don't trust the model); LLM07/LLM02 → never put secrets in prompts; LLM05 → escape output (XSS).

## The golden security principle for LLM apps
**Never rely on the model to enforce security.** Enforce permissions, limits and validation in **normal code outside the model**, because the model can always be talked out of its instructions.

## Exercises
1. Pick an AI product you use. List three assets and map threats to OWASP IDs.
2. Read one real public LLM incident write-up and map it to the list.
3. Look up three techniques in MITRE ATLAS: https://atlas.mitre.org

## Mini project: LLM Threat Model
**Build:** Threat-model an imagined AI app.

**Deliverables (in your own portfolio repo):** A table of assets, threats, OWASP IDs and controls for a support chatbot with tools.

**This is a phase of the track capstone:** see [`../CAPSTONE.md`](../CAPSTONE.md).

**Share it (optional):** "I threat-modelled an AI chatbot using the OWASP LLM Top 10." Follow the safe-sharing rules and templates in [`SHOWCASE.md`](../../../SHOWCASE.md).

## Checkpoint
- Why can't a system prompt be a security boundary?
- What is "excessive agency", and what is the fix?

## Go deeper
- OWASP GenAI Security Project: https://genai.owasp.org
- MITRE ATLAS: https://atlas.mitre.org
- Google Secure AI Framework (SAIF): https://saif.google
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
