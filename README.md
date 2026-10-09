```
   ____ __   __ ____  _____ ____        ____ ___ ____ _   _    _    _     ____
  / ___|\ \ / /| __ )| ____|  _ \      / ___|_ _/ ___| \ | |  / \  | |   / ___|
 | |     \ V / |  _ \|  _| | |_) |_____\___ \| | |  _|  \| | / _ \ | |   \___ \
 | |___   | |  | |_) | |___|  _ <|_____|___) | | |_| | |\  |/ ___ \| |___ ___) |
  \____|  |_|  |____/|_____|_| \_\     |____/___\____|_| \_/_/   \_\_____|____/
```
<p align="center">
  <img src="assets/brand/google-developers.svg" alt="Google Developers" width="200">
</p>

# GDG Cyber Signals

*A community cybersecurity curriculum designed for **GDG on Campus AASTMT Abu Qir** online sessions.*

> **Detection is detection.** A SIEM alert, a suspicious transaction cluster, a manipulated video, a jailbroken chatbot and an anomaly in a biological sequence are all the same skill: finding a pattern in noise and proving it.

An open, self-paced, hands-on cybersecurity curriculum built for a GDG community. You do **not** need to watch any recording. Every lab is written so you can open the folder, read the explanation, copy the commands, and run everything on your own machine.

## Our focus: cyber first, with flavours
The core of this chapter is **real cybersecurity: blue team defence** (logs, SIEM, detections, honeypots, incident response). Around that core we add a few carefully chosen spotlights:
- **Cybercrime** and **OSINT**: how crime is investigated and how to verify claims
- **LLM security**: why [(read the why)](docs/why-llm-security.md)
- **Bio-cyber**: why [(read the why)](docs/why-bio-cyber.md)
- **Build with AI (Gemini)**: building security tools the safe way, in the GDG "Build with AI" spirit ([details](docs/gemini-and-gdg.md))

## Our chapter and community
Link hub: https://bio.link/gdgaast

**GDG on Campus AAST Abu Qir:** [link hub](https://bio.link/gdgaast) | [Facebook](https://www.facebook.com/GDGAAST/) | [Instagram](https://www.instagram.com/aast.gdgc/) | [LinkedIn](https://www.linkedin.com/company/gdg-on-campus-aast-abu-qir/) | [WhatsApp community](https://chat.whatsapp.com/LcIrU7sHcqFG43t1u3IPJs) | [Chapter page](https://gdg.community.dev/gdg-on-campus-arab-academy-for-science-technology-and-maritime-transport-abu-qir-egypt/)
All chapter links: [`docs/community-aast-abu-qir.md`](docs/community-aast-abu-qir.md). Free Google resources: [`docs/google-free-resources.md`](docs/google-free-resources.md).

## Projects you can post
Every lab ends with a **mini project**, and every track ends with a **capstone** you can put on GitHub, LinkedIn and social media. See [`PROJECTS.md`](PROJECTS.md) and [`SHOWCASE.md`](SHOWCASE.md).

## The tracks

| Track | Folder | What you learn |
|---|---|---|
| **Watchtower** (Blue Team) | [`tracks/watchtower-blue-team`](tracks/watchtower-blue-team) | SIEM with Wazuh, log analysis, Sigma detections, honeypots and deception, incident response |
| **Ledger** (Cybercrime) | [`tracks/ledger-cybercrime`](tracks/ledger-cybercrime) | How cybercrime operates, crypto tracing and AML basics, digital forensics, cybercrime law |
| **Scout** (OSINT) | [`tracks/scout-osint`](tracks/scout-osint) | OSINT methodology, verification, geolocation, deepfake checks |
| **Aegis** (LLM Security) | [`tracks/aegis-llm-security`](tracks/aegis-llm-security) | Prompt injection, RAG and agent attacks, guardrails, red-teaming |
| **Helix** (Bio-Cyber) | [`tracks/helix-bio-cyber`](tracks/helix-bio-cyber) | Sequence analysis, biological graph algorithms, genomic and neural data security |
| **Forge** (Build with AI) | [`tracks/build-with-ai`](tracks/build-with-ai) | Build security tools with **Google Gemini**: API quickstart, AI log triage, AI for investigators, building safely |

Forge is a cross-cutting section: it uses the other tracks' data and ideas to build tools. Cybercrime and OSINT are deliberately **separate**: you can take either without the other.

## How every lab is organised

Each lab folder has one `README.md` with the same flow:

1. **What is it?** A short plain-language explanation of the tool or concept
2. **Why it matters** where it shows up in real security work
3. **Setup** exact commands for your machine
4. **Walkthrough** runnable code snippets, with the expected output described
5. **Exercises** to prove you understood
6. **Checkpoint** questions you should be able to answer
7. **Go deeper** links to official docs and practice platforms

## Quick start

```bash
git clone https://github.com/<your-org>/gdg-cyber-signals.git
cd gdg-cyber-signals
# pick a track, open its README, start with lab 01
```

Most labs need: Linux or macOS or WSL2, Python 3.10+, Docker, and git. Each lab lists anything extra.

## Suggested learning paths

- **Total beginner:** Watchtower 01 and 03, then Scout 01, then Aegis 01 and 02
- **Aspiring SOC analyst:** All of Watchtower, then Ledger 03 (forensics)
- **Aspiring investigator:** Scout 01 to 03, Ledger 01 to 04
- **AI builder:** Forge 01 to 04, then Aegis 01 to 04 to attack what you built
- **Biology or data-science curious:** Helix 01 to 03, then Aegis 01

## Running this as a GDG chapter
See [`GDG_SESSIONS.md`](GDG_SESSIONS.md) for the session format, online logistics, promotion checklist and feedback loop.

## Everything in one place

- [`RESOURCES.md`](RESOURCES.md): every link, platform, tool, channel, podcast and community
- [`ETHICS.md`](ETHICS.md): the rules for everything in this repo. **Read this first.**
- [`PROJECTS.md`](PROJECTS.md): mini projects, capstones, and your portfolio repo
- [`SHOWCASE.md`](SHOWCASE.md): share on GitHub, LinkedIn and social media safely
- [`docs/`](docs): why LLM security, why bio-cyber, Gemini and GDG, [free Google resources](docs/google-free-resources.md), [our chapter's links](docs/community-aast-abu-qir.md)
- [`ROADMAP.md`](ROADMAP.md): learner paths (Defender, Investigator, OSINT, AI security, Bio-cyber, Builder) and the project roadmap
- [`TERM_PLAN.md`](TERM_PLAN.md): the 16-week, exam-friendly plan
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md): how we treat each other
- [`CONTRIBUTING.md`](CONTRIBUTING.md): add a lab, fix a typo, suggest a session
- [`templates/`](templates): incident report, case file, OSINT collection log, lab template

## Session calendar: two semesters, 7 live sessions each

The lead term spans **two semesters, two tracks each**, with **7 live sessions per semester (14 per year)**, about one every two weeks. Other labs are self-paced. Exams fall in **weeks 7, 12 and 16** (no sessions or deadlines), and the sessions in weeks **6, 11, 15** are **light**: no installs, nothing due. Full plan: [`TERM_PLAN.md`](TERM_PLAN.md).

| | Semester 1 | Semester 2 |
|---|---|---|
| **Tracks** | Watchtower (blue team) + Forge (Gemini) | Ledger (cybercrime) + Aegis (LLM security) |
| **Light spotlights** | LLM "Gandalf Live", Bio-cyber | OSINT "Verify It", Cybercrime law tabletop |
| **Capstones** | Mini SOC, AI Security Tool | Follow the Money, Break and Harden an LLM App |
| **Self-paced** | Scout, Helix, other labs | Scout, Helix, other labs |

### Semester 1: the 7 live sessions
| Week | Session | Material |
|---|---|---|
| 2 | Kickoff + reading logs like an analyst | [Watchtower 02](tracks/watchtower-blue-team/02-log-analysis) |
| 4 | Your first SIEM | [Watchtower 01](tracks/watchtower-blue-team/01-wazuh-siem) |
| **6** | **Light:** Gandalf Live (LLM security) | [Why LLM security](docs/why-llm-security.md) |
| 9 | AI log triage with a verifier | [Forge 02](tracks/build-with-ai/02-ai-log-triage) |
| **11** | **Light:** Your DNA Is a Password (bio-cyber) | [Why bio-cyber](docs/why-bio-cyber.md) |
| 13 | Capstone clinic | [Watchtower](tracks/watchtower-blue-team/CAPSTONE.md), [Forge](tracks/build-with-ai/CAPSTONE.md) |
| **15** | **Light:** Showcase and LinkedIn workshop | [`SHOWCASE.md`](SHOWCASE.md) |

Weeks 7, 12 and 16 are exams. Semester 2 (Ledger and Aegis) is in [`TERM_PLAN.md`](TERM_PLAN.md).

## Author and maintainer

**Mustafa Elmekkawi** ([@mustafa-codez](https://github.com/mustafa-codez)), Computer Science (Cybersecurity) student, creator and maintainer of GDG Cyber Signals.

Contributors are credited in the repository history and welcome via `CONTRIBUTING.md`.

## License

Content: CC BY 4.0. Code snippets: MIT. See [`LICENSE`](LICENSE).

## Brand and disclaimer
Designed for **GDG on Campus AASTMT Abu Qir**. This is community content, not an official Google product, and the views and activities here are not those of Google. Official logos and brand rules: see [`assets/brand/README.md`](assets/brand/README.md).
