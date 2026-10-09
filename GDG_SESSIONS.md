# Running These Sessions as a GDG Chapter

## Session format (90 minutes, online)
| Time | Block | Notes |
|---|---|---|
| 0-10 | Welcome and hook | One real story that motivates the topic; remind of `ETHICS.md` |
| 10-30 | Concept | Use the lab's "What is it?" section as your script |
| 30-80 | Guided lab | Share the lab link in chat; attendees follow the README at their own pace |
| 80-90 | Challenge and Q&A | Post the challenge as a GitHub issue or discussion |

Because every lab README is self-contained, people who miss the live session can still complete it. Recording is optional, never required.

## Before the session
- [ ] Pick the lab and run it yourself on a clean machine
- [ ] Share prerequisites 3 to 5 days ahead (OS, Docker, Python version, disk space)
- [ ] Prepare a fallback for attendees who can't install (browser-only options: Gandalf, OSINT tools, Overpass Turbo, Google Colab for Python labs)
- [ ] Test screen sharing, breakout rooms, chat moderation
- [ ] Assign a co-host to watch chat and help with setup problems

## Setup support
- Use a pinned "Setup help" thread in GitHub Discussions
- Offer a 15-minute "setup clinic" before the first lab-heavy session (Wazuh needs 8 GB RAM, so provide a lighter path using the log-analysis lab)

## Safety reminders to say out loud
- Only attack the practice targets provided
- Honeypots stay on localhost
- No real personal data in OSINT or bio labs

## Term plan
See [`TERM_PLAN.md`](TERM_PLAN.md) for the two-semester plan (7 live sessions each) that avoids exam weeks 7, 12 and 16. Adjust the dates if your university changes its exam schedule; keep the order and keep the light-before-heavy balance.

## Promotion checklist
- [ ] Event page on the GDG platform with the lab link and prerequisites
- [ ] One-paragraph description for social posts
- [ ] Short "what you will build" line per session
- [ ] Use the chapter's official logo files and brand rules ([`assets/brand/README.md`](assets/brand/README.md)); never alter or recreate logos

## Feedback loop
Add a 3-question form: what worked, what was confusing, what topic next. Turn answers into issues using the session-request template.

## Growing the community
- Label beginner-friendly issues `good first lab fix`
- Invite attendees to contribute a challenge or fix a typo (their first pull request)
- Recognise contributors in the README

## Build with AI sessions
The **Forge** track fits GDG "Build with AI" style events: attendees leave with a working tool. Ask attendees to create their free Gemini API key in advance (Forge Lab 01), and remind them never to paste keys into chat or commit them. Offer Google Colab as the no-install option.

## Light weeks (6, 11, 15)
The weeks just before exams are deliberately light:
- **No installs, no new tools**, 60 minutes at most
- Browser-only (for example Gandalf) or host-led demos
- **Nothing due**; any hands-on lab is a take-home for after exams
- Semester 1 spotlights: [`docs/why-llm-security.md`](docs/why-llm-security.md) (week 6), [`docs/why-bio-cyber.md`](docs/why-bio-cyber.md) (week 11); showcase in week 15
- Semester 2 light sessions: OSINT "Verify It" (week 6), cybercrime law tabletop (week 11); showcase in week 15
- The two-semester plan is in [`TERM_PLAN.md`](TERM_PLAN.md)

## Projects and sharing
Every lab ends with a mini project and every track with a capstone ([`PROJECTS.md`](PROJECTS.md)). Run the week 15 showcase with [`SHOWCASE.md`](SHOWCASE.md): five-minute demos, README-first, safe-sharing rules read aloud.
