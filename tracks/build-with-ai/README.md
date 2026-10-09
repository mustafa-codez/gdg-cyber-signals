# Forge: Build with AI

Security people who can **build** are rare and valuable. This section teaches you to use **Google Gemini** to build small, useful security tools, and to do it **safely**. It follows the GDG "Build with AI" spirit: learn by shipping something real.

| # | Lab | You will build / learn |
|---|---|---|
| 01 | [Gemini quickstart](01-gemini-quickstart) | Get an API key, make your first call, system instructions, key safety |
| 02 | [AI log triage](02-ai-log-triage) | A tool that summarises auth logs into validated JSON, with code that checks the AI's work |
| 03 | [AI for investigators](03-ai-for-investigators) | Turn public text into structured case notes, treating output as leads, not facts |
| 04 | [Build safely](04-build-safely) | Secrets, hallucinated packages, reviewing AI-written code, human-in-the-loop |

## The three rules of this section
1. **AI proposes, code verifies, humans decide.** Never let model output trigger a real action without a check.
2. **Minimise what you send.** Don't paste secrets, personal data or raw sensitive logs into any AI tool.
3. **Output is a lead, not evidence.** Verify before you rely on or share it.

Pair this with **Aegis** (how AI apps get attacked): build in Forge, then attack your own build in Aegis.

## Capstone
Every lab ends with a mini project that is one phase of this track's capstone: **An AI Security Tool with a Verifier**. See [`CAPSTONE.md`](CAPSTONE.md).

## More free Google resources for this track
- Google AI Studio: https://aistudio.google.com
- Gemini API cookbook: https://github.com/google-gemini/cookbook
- Gemini CLI: https://github.com/google-gemini/gemini-cli
- OSV-Scanner: https://github.com/google/osv-scanner
- deps.dev: https://deps.dev
- NotebookLM: https://notebooklm.google.com
- Full list: [`docs/google-free-resources.md`](../../docs/google-free-resources.md)
