# Capstone: Break and Harden an LLM App

**Attack a practice target, then secure your own app**

## Goal
Show both sides: how an LLM app fails, and how you made yours harder to break, with evidence.

## How it works
The capstone is built **one phase at a time**. Each phase is the mini project at the end of a lab, so finishing the labs means you are already finishing the capstone. Post after each phase if you like (see `SHOWCASE.md`).

| Phase | Name | From | What you deliver |
|---|---|---|---|
| 1 | **LLM threat model** | Lab 01 | A table mapping a chatbot's assets to threats, OWASP IDs and controls. |
| 2 | **Injection journal and hardened bot** | Lab 02 | A Gandalf learning journal (principles, no spoilers) and a bot with three defences. |
| 3 | **Safe tools demo** | Lab 03 | A RAG-poisoning demo and an agent tool wrapper that enforces permissions in code. |
| 4 | **Red-team report** | Lab 04 | A 10-test suite and two professional findings with success rates. |

## Final assembly
Publish one repo: the vulnerable version, the hardened version, the test suite and a before/after results table.

## Gemini layer (optional, encouraged)
Make the target a **Gemini-powered** bot (Google AI Studio key). Red-team it, harden it, and re-test. State the model name and date, since behaviour changes.

## Definition of done
- [ ] Runs or reads from a clean clone of your own repo
- [ ] README using `templates/student-project-readme.md`
- [ ] Synthetic or public data only; no secrets, no personal data
- [ ] States honestly what AI helped with and how it was checked
- [ ] Added one thing of your own beyond the labs (a feature, test, diagram or writeup)

## Share it
Starter post (edit before use):
> I attacked my own LLM app, then hardened it. Before and after results inside.

Hashtags: #GDG #LLMSecurity #AIsecurity #PromptInjection #BuildWithAI #Gemini

See [`../../SHOWCASE.md`](../../SHOWCASE.md) for the safe-sharing rules and templates.
