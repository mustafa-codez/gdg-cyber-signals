# Capstone: An AI Security Tool with a Verifier

**A Gemini-powered tool where code checks the AI**

## Goal
Ship a small, safe, documented security tool that uses Gemini and proves it doesn't blindly trust it.

## How it works
The capstone is built **one phase at a time**. Each phase is the mini project at the end of a lab, so finishing the labs means you are already finishing the capstone. Post after each phase if you like (see `SHOWCASE.md`).

| Phase | Name | From | What you deliver |
|---|---|---|---|
| 1 | **Gemini starter toolkit** | Lab 01 | A small command-line tool that asks Gemini a security question with a role, key kept in an environment variable. |
| 2 | **AI log triage tool** | Lab 02 | Triage tool with schema-validated output and at least one new verifier rule you wrote. |
| 3 | **Case-notes extractor** | Lab 03 | Extractor for a public document where code verifies every quoted claim. |
| 4 | **Safe-build checklist** | Lab 04 | Secret scanning, dependency audit and a README that states what data goes to the AI service. |

## Final assembly
Merge into one tool with tests (`pytest`), a security review (`bandit`, `gitleaks`) and a clear README.

## Gemini layer (optional, encouraged)
This **is** the Gemini layer. Document the model used, prompts, schema, the verifier and its tests.

## Definition of done
- [ ] Runs or reads from a clean clone of your own repo
- [ ] README using `templates/student-project-readme.md`
- [ ] Synthetic or public data only; no secrets, no personal data
- [ ] States honestly what AI helped with and how it was checked
- [ ] Added one thing of your own beyond the labs (a feature, test, diagram or writeup)

## Share it
Starter post (edit before use):
> I built a Gemini-powered security tool where code verifies the AI. Here's why that matters.

Hashtags: #GDG #BuildWithAI #Gemini #SecureAI #CyberSecurity

See [`../../SHOWCASE.md`](../../SHOWCASE.md) for the safe-sharing rules and templates.
