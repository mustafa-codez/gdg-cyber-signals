```
   ____ __   __ ____  _____ ____        ____ ___ ____ _   _    _    _     ____
  / ___|\ \ / /| __ )| ____|  _ \      / ___|_ _/ ___| \ | |  / \  | |   / ___|
 | |     \ V / |  _ \|  _| | |_) |_____\___ \| | |  _|  \| | / _ \ | |   \___ \
 | |___   | |  | |_) | |___|  _ <|_____|___) | | |_| | |\  |/ ___ \| |___ ___) |
  \____|  |_|  |____/|_____|_| \_\     |____/___\____|_| \_/_/   \_\_____|____/
```

# Cyber Signals

*A community cybersecurity curriculum for Google Developer Groups (GDG) online sessions.*

> **Detection is detection.** A SIEM alert, a suspicious transaction cluster, a manipulated video, a jailbroken chatbot and an anomaly in a biological sequence are all the same skill: finding a pattern in noise and proving it.

An open, self-paced, hands-on cybersecurity curriculum built for a GDG community. You do **not** need to watch any recording. Every lab is written so you can open the folder, read the explanation, copy the commands, and run everything on your own machine.

## The five tracks

| Track | Folder | What you learn |
|---|---|---|
| **Watchtower** (Blue Team) | [`tracks/watchtower-blue-team`](tracks/watchtower-blue-team) | SIEM with Wazuh, log analysis, Sigma detections, honeypots and deception, incident response |
| **Ledger** (Cybercrime) | [`tracks/ledger-cybercrime`](tracks/ledger-cybercrime) | How cybercrime operates, crypto tracing and AML basics, digital forensics, cybercrime law |
| **Scout** (OSINT) | [`tracks/scout-osint`](tracks/scout-osint) | OSINT methodology, verification, geolocation, deepfake checks |
| **Aegis** (LLM Security) | [`tracks/aegis-llm-security`](tracks/aegis-llm-security) | Prompt injection, RAG and agent attacks, guardrails, red-teaming |
| **Helix** (Bio-Cyber) | [`tracks/helix-bio-cyber`](tracks/helix-bio-cyber) | Sequence analysis, biological graph algorithms, genomic and neural data security |

Cybercrime and OSINT are deliberately **separate**: you can take either without the other.

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
git clone https://github.com/<your-org>/cyber-signals.git
cd cyber-signals
# pick a track, open its README, start with lab 01
```

Most labs need: Linux or macOS or WSL2, Python 3.10+, Docker, and git. Each lab lists anything extra.

## Suggested learning paths

- **Total beginner:** Watchtower 01 and 03, then Scout 01, then Aegis 01 and 02
- **Aspiring SOC analyst:** All of Watchtower, then Ledger 03 (forensics)
- **Aspiring investigator:** Scout 01 to 03, Ledger 01 to 04
- **AI builder:** Aegis 01 to 04
- **Biology or data-science curious:** Helix 01 to 03, then Aegis 01

## Running this as a GDG chapter
See [`GDG_SESSIONS.md`](GDG_SESSIONS.md) for the session format, online logistics, promotion checklist and feedback loop.

## Everything in one place

- [`RESOURCES.md`](RESOURCES.md): every link, platform, tool, channel, podcast and community
- [`ETHICS.md`](ETHICS.md): the rules for everything in this repo. **Read this first.**
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md): how we treat each other
- [`CONTRIBUTING.md`](CONTRIBUTING.md): add a lab, fix a typo, suggest a session
- [`templates/`](templates): incident report, case file, OSINT collection log, lab template

## Session calendar (edit per term)

| Week | Track | Session | Lab |
|---|---|---|---|
| 1 | All | Orientation, ethics, lab setup | `ETHICS.md` |
| 2 | Watchtower | Your first SIEM | [Wazuh](tracks/watchtower-blue-team/01-wazuh-siem) |
| 3 | Watchtower | Reading logs like an analyst | [Log analysis](tracks/watchtower-blue-team/02-log-analysis) |
| 4 | Watchtower | Writing detections | [Sigma](tracks/watchtower-blue-team/03-sigma-detections) |
| 5 | Watchtower | Deception: honeypots | [Cowrie](tracks/watchtower-blue-team/04-honeypots-cowrie) |
| 6 | Aegis | How LLM apps get attacked | [OWASP LLM Top 10](tracks/aegis-llm-security/01-owasp-llm-top10) |
| 7 | Aegis | Prompt injection, hands-on | [Prompt injection](tracks/aegis-llm-security/02-prompt-injection) |
| 8 | Scout | OSINT methodology | [Methodology](tracks/scout-osint/01-methodology) |
| 9 | Scout | Verifying media | [Verification](tracks/scout-osint/02-image-and-media-verification) |
| 10 | Ledger | Anatomy of cybercrime | [Cybercrime anatomy](tracks/ledger-cybercrime/01-cybercrime-anatomy) |
| 11 | Ledger | Following the money | [Crypto tracing](tracks/ledger-cybercrime/02-crypto-tracing-basics) |
| 12 | Helix | Sequences as signals | [Sequences](tracks/helix-bio-cyber/01-sequences-as-signals) |

## License

Content: CC BY 4.0. Code snippets: MIT. See `LICENSE` (add before publishing).
