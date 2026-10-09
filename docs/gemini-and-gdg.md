# Gemini and the GDG "Build with AI" Spirit

This chapter lives inside Google Developer Groups, so **Gemini** and the **Build with AI** theme run through the repo. At the same time, the chapter's core is **real cybersecurity**, so AI is a *co-pilot*, never a replacement for understanding.

## What "Build with AI" is
Build with AI is a global series of community-led events where developers learn to build safe, secure and scalable solutions with Google's AI models, including Gemini. Events are run by local organisers, and Google supports the series with technical content. The series has a season each year, so **check the current season, branding and materials** on the official page before you promote anything: https://developers.google.com/community/build-with-ai/faq

## How Gemini shows up here
| Track | "Gemini layer" (optional, in the capstone) | The verification rule |
|---|---|---|
| Watchtower | Gemini explains an alert and suggests next steps | Code checks the facts against the log |
| Ledger | Gemini extracts case notes from a *public* document | Every claim needs an exact quote that code finds in the source |
| Scout | Gemini summarises *public* sources you already collected | You grade each source and verify claims manually |
| Aegis | Gemini is the target: you build and harden a Gemini-powered bot | Red-team it with garak or promptfoo and report success rates |
| Helix | Gemini explains notebook results or code | You re-run the code and check the numbers yourself |
| Forge | The core: build AI security tools | Pydantic schemas plus a verifier |

## The rule
**AI proposes, code verifies, humans decide.** Never act on model output without a check, never send secrets or real personal data, and say when AI helped.

## Practical setup
- Get a free key in Google AI Studio: https://aistudio.google.com/apikey
- Docs and quickstart: https://ai.google.dev/gemini-api/docs/quickstart
- Models change often: https://ai.google.dev/gemini-api/docs/models
- No install? Use Google Colab: https://colab.research.google.com
- Walkthrough: [`tracks/build-with-ai`](../tracks/build-with-ai)

## Running Build with AI style sessions
- Make it **hands-on**: attendees leave having built something.
- Keep it **safe and secure**: that is both the Google message and this chapter's identity.
- Suggest attendees post their project (see [`SHOWCASE.md`](../SHOWCASE.md)).
- Ask the chapter organisers about official event pages, speaker support and branding.
- GDG event listings live on the community platform: https://gdg.community.dev

## Honest limits
- This repo is community content. It is **not** an official Google product, and Google doesn't endorse it.
- Use official GDG logos and wording only as the brand guidelines allow.
