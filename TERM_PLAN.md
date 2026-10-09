# Term Plan: Two Semesters, Lean and Exam-Friendly

The GDG lead term spans **two semesters**. Each semester teaches **two tracks**, with **7 live sessions** (about one every two weeks). That is **14 live sessions for the year**. Everything between sessions is **self-paced**, because every lab is a self-contained README. Join and follow the chapter: https://bio.link/gdgaast

> **Assumption:** each semester has 16 weeks with exams in **weeks 7, 12 and 16**. If the second semester's exam weeks differ, slide the plan; the order stays.

## The year at a glance
| | Semester 1 | Semester 2 |
|---|---|---|
| **Tracks** | **Watchtower** (blue team, the core) + **Forge** (build with Gemini) | **Ledger** (cybercrime) + **Aegis** (LLM security) |
| **Light spotlights** | LLM "Gandalf Live" (week 6), Bio-cyber (week 11) | OSINT "Verify It" (week 6), Cybercrime law tabletop (week 11) |
| **Capstones** | Mini SOC, AI Security Tool with a Verifier | Follow the Money, Break and Harden an LLM App |
| **Live sessions** | **7** | **7** |
| **Self-paced** | All other labs, plus Scout and Helix | All other labs, plus Scout and Helix |

## Why 7 per semester
- 16 weeks minus 3 exam weeks = 13 usable weeks. Half of that, one session every two weeks, gives **7**.
- Each semester = 1 kickoff-with-a-lab, 2 key labs, 2 light spotlights, 1 capstone clinic, 1 showcase.
- **Live sessions teach the key lab of each track; the other labs are self-paced** with the READMEs, mini projects and capstone phases.
- Sessions run 60 to 90 minutes. Light sessions run 60 minutes at most.

## Principles
1. **No live session in exam weeks (7, 12, 16).** Only optional light reading.
2. **No deadlines in exam weeks.** Anything due moves to the Sunday after the next live session.
3. **Light weeks (6, 11, 15):** *no installs, no new tools, 60 minutes at most, browser-only or host-led, nothing due.*
4. **Cyber first:** semester 1 is Watchtower, the core of the chapter.
5. **Self-paced by design:** nobody falls behind if they miss a session.
6. **Announce early:** prerequisites 7 days ahead, a reminder 24 hours before.
7. **Projects as the thread:** every lab ends with a mini project and each track with a capstone ([`PROJECTS.md`](PROJECTS.md), [`SHOWCASE.md`](SHOWCASE.md)).

---

## Semester 1: Watchtower and Forge

| Week | Type | Session | Material | Load |
|---|---|---|---|---|
| 1 | Self-paced | Setup pre-work | [`ETHICS.md`](ETHICS.md): install Docker, Python, Git | Light |
| **2** | **Live** | **Kickoff + reading logs like an analyst** | [Watchtower 02](tracks/watchtower-blue-team/02-log-analysis), [chapter links](docs/community-aast-abu-qir.md) | Light-medium |
| 3 | Self-paced | Optional: Watchtower 03 (Sigma) | [Watchtower 03](tracks/watchtower-blue-team/03-sigma-detections) | Optional |
| **4** | **Live** | **Your first SIEM** | [Watchtower 01](tracks/watchtower-blue-team/01-wazuh-siem) | Heavy |
| 5 | Self-paced | Optional: honeypots | [Watchtower 04](tracks/watchtower-blue-team/04-honeypots-cowrie) | Optional |
| **6** | **Live (light)** | **Spotlight: Gandalf Live (LLM teaser)** | [Why LLM security](docs/why-llm-security.md): browser only | **Very light** |
| **7** | **EXAMS** | No session | Optional reading: [Watchtower 05](tracks/watchtower-blue-team/05-incident-response) | None |
| 8 | Self-paced | Prep: get a Gemini key | [Forge 01](tracks/build-with-ai/01-gemini-quickstart) | Light |
| **9** | **Live** | **AI log triage with a verifier** | [Forge 02](tracks/build-with-ai/02-ai-log-triage) | Medium |
| 10 | Self-paced | Optional: Forge 03 and 04 | [Forge 03](tracks/build-with-ai/03-ai-for-investigators), [Forge 04](tracks/build-with-ai/04-build-safely) | Optional |
| **11** | **Live (light)** | **Spotlight: Your DNA Is a Password You Can't Reset** | [Why bio-cyber](docs/why-bio-cyber.md): host-led demos | **Very light** |
| **12** | **EXAMS** | No session | Optional reading: [Ledger 01](tracks/ledger-cybercrime/01-cybercrime-anatomy) (preview of semester 2) | None |
| **13** | **Live** | **Capstone clinic: Mini SOC and AI tool** | [Watchtower capstone](tracks/watchtower-blue-team/CAPSTONE.md), [Forge capstone](tracks/build-with-ai/CAPSTONE.md) | Medium |
| 14 | Self-paced | Finish your capstone | [`PROJECTS.md`](PROJECTS.md) | Optional |
| **15** | **Live (light)** | **Showcase and LinkedIn workshop** | [`SHOWCASE.md`](SHOWCASE.md) | **Very light** |
| **16** | **EXAMS** | No session | Async: feedback form, semester 2 vote | None |

**Tally: 7 live sessions** (weeks 2, 4, 6, 9, 11, 13, 15).

## Semester 2: Ledger and Aegis

| Week | Type | Session | Material | Load |
|---|---|---|---|---|
| 1 | Self-paced | Recap and Gemini key refresh | [`SHOWCASE.md`](SHOWCASE.md) | Light |
| **2** | **Live** | **Kickoff + anatomy of cybercrime (case discussion)** | [Ledger 01](tracks/ledger-cybercrime/01-cybercrime-anatomy) | Light-medium |
| 3 | Self-paced | Optional: forensics | [Ledger 03](tracks/ledger-cybercrime/03-digital-forensics-basics) | Optional |
| **4** | **Live** | **Following the money** | [Ledger 02](tracks/ledger-cybercrime/02-crypto-tracing-basics) | Medium-heavy |
| 5 | Self-paced | Pre-read: OWASP LLM Top 10 | [Aegis 01](tracks/aegis-llm-security/01-owasp-llm-top10) | Light |
| **6** | **Live (light)** | **Spotlight: Verify It (OSINT, browser only)** | [Scout 01](tracks/scout-osint/01-methodology), [Scout 02](tracks/scout-osint/02-image-and-media-verification) | **Very light** |
| **7** | **EXAMS** | No session | Optional reading: [Ledger 04](tracks/ledger-cybercrime/04-cybercrime-law) | None |
| 8 | Self-paced | Optional: set up the local LLM | [Aegis 02](tracks/aegis-llm-security/02-prompt-injection) setup | Optional |
| **9** | **Live** | **Prompt injection, hands-on** | [Aegis 02](tracks/aegis-llm-security/02-prompt-injection) | Medium |
| 10 | Self-paced | Optional: RAG and agents | [Aegis 03](tracks/aegis-llm-security/03-rag-and-agent-security) | Optional |
| **11** | **Live (light)** | **Cybercrime law tabletop: who has jurisdiction?** | [Ledger 04](tracks/ledger-cybercrime/04-cybercrime-law) | **Very light** |
| **12** | **EXAMS** | No session | Optional reading: [why bio-cyber](docs/why-bio-cyber.md) | None |
| **13** | **Live** | **Red-team and capstone clinic** | [Aegis 04](tracks/aegis-llm-security/04-red-teaming), [Ledger capstone](tracks/ledger-cybercrime/CAPSTONE.md), [Aegis capstone](tracks/aegis-llm-security/CAPSTONE.md) | Medium |
| 14 | Self-paced | Finish your capstone | [`PROJECTS.md`](PROJECTS.md) | Optional |
| **15** | **Live (light)** | **Year showcase and handover plan** | [`SHOWCASE.md`](SHOWCASE.md) | **Very light** |
| **16** | **EXAMS** | No session | Async: feedback, next-year plan | None |

**Tally: 7 live sessions** (weeks 2, 4, 6, 9, 11, 13, 15).

## What about Scout and Helix?
They stay in the repo, fully usable:
- **Spotlights:** Helix (semester 1, week 11) and Scout (semester 2, week 6) get a light live taste.
- **Self-paced:** every lab, mini project and capstone works without a live session. Strong members can lead or co-teach them.
- **Next year:** a future lead (or you) can teach them live. See [`ROADMAP.md`](ROADMAP.md).

## If you have even less time
Keep the kickoff, the two light sessions and the showcase, and drop to **3 sessions per semester** (the key lab, a spotlight, the showcase). The repo still works as a self-study course.

## Session-day checklist
- [ ] Post the session and prerequisites 7 days ahead; reminder at 24 hours
- [ ] Run the lab yourself on a clean machine (not needed for light weeks)
- [ ] Co-host assigned for chat and setup help
- [ ] Post the mini project as a GitHub issue; due after the next live, non-light session
- [ ] After: a short "what we covered" note and the 3-question feedback form

## Exam-week etiquette
- One short good-luck post at the start of each exam week with the optional reading link.
- A single open "office hours" thread; no pressure to reply the same day.
- A quick recap before any new topic in the week after exams.

## Milestones
| When | Milestone |
|---|---|
| Sem 1, week 4 | A SIEM running with a custom rule |
| Sem 1, week 9 | First Gemini triage tool running |
| Sem 1, week 15 | Showcase, release tagged `v2026-fall` |
| Sem 2, week 4 | A synthetic peel chain traced |
| Sem 2, week 13 | An LLM app attacked and hardened |
| Sem 2, week 15 | Year showcase, release tagged `v2027-spring` |

## End-of-semester tasks
- Tag a release (`git tag v2026-fall && git push --tags`)
- Publish feedback results as an issue
- Thank contributors in the README
- Draft the next semester's plan from the feedback
