# Roadmap

**Focus:** core cybersecurity (blue team) first, with spotlights on cybercrime, OSINT, LLM security, bio-cyber and building with Gemini.

Two roadmaps in one file: **[Part 1](#part-1-learner-roadmap)** is for students (where to go and in what order), and **[Part 2](#part-2-project-roadmap)** is for the project (what we plan to add).

---

## Part 1: Learner roadmap

Pick your starting point. Tick the boxes as you go (copy this file into your own notes or fork).

```
Stage 0          Stage 1            Stage 2              Stage 3
Foundations  ->  Core skills    ->  Choose a path    ->  Prove it
(Linux, Python,  (logs, SIEM,       (Defender,           (write-ups, CTFs,
 Git, ethics)     OSINT method,      Investigator,        contributions,
                  LLM risks)         AI security,         certifications)
                                     Bio-cyber, Builder)
```

### Stage 0: Foundations (2 to 4 weeks, self-paced)
- [ ] Read [`ETHICS.md`](ETHICS.md)
- [ ] Comfortable in a Linux terminal (files, permissions, `grep`, `ssh`)
- [ ] Python basics (functions, files, `pip`, virtual environments)
- [ ] Git basics (clone, commit, push, pull request)
- [ ] Networking basics (IP, DNS, ports, HTTP)
- [ ] Set up Docker and a VM
- Practice: TryHackMe Pre-Security, OverTheWire Bandit (see [`RESOURCES.md`](RESOURCES.md))

### Stage 1: Core skills (one term)
- [ ] [Watchtower 02: Log analysis](tracks/watchtower-blue-team/02-log-analysis)
- [ ] [Watchtower 01: Wazuh SIEM](tracks/watchtower-blue-team/01-wazuh-siem)
- [ ] [Watchtower 03: Sigma detections](tracks/watchtower-blue-team/03-sigma-detections)
- [ ] [Scout 01: OSINT methodology](tracks/scout-osint/01-methodology)
- [ ] [Aegis 01: OWASP LLM Top 10](tracks/aegis-llm-security/01-owasp-llm-top10)
- [ ] [Forge 01: Gemini quickstart](tracks/build-with-ai/01-gemini-quickstart)

**Milestone:** you can read a log, explain an alert, write one detection rule, run a basic verification and make a first AI API call.

### Stage 2: Choose a path (1 to 2 terms)
You can follow more than one. Each path lists the labs in order, practice platforms, and a portfolio output.

#### Path A: Defender (SOC analyst, detection engineer)
| Step | Material |
|---|---|
| 1 | Watchtower 01 to 05 |
| 2 | Ledger 03 (digital forensics basics) |
| 3 | Forge 02 (AI log triage) |
| Practice | TryHackMe SOC Level 1 path, Blue Team Labs Online, CyberDefenders, LetsDefend |
| Entry certs to consider | CompTIA Security+, Blue Team Level 1, CompTIA CySA+ |
| **Portfolio output** | A written incident report (`templates/incident-report.md`) and 3 Sigma rules mapped to ATT&CK |

#### Path B: Investigator (cybercrime, fraud, financial crime)
| Step | Material |
|---|---|
| 1 | Ledger 01 to 04 |
| 2 | Scout 01 to 03 |
| 3 | Forge 03 (AI for investigators) |
| Practice | Trace Labs ethical OSINT events, DFIR challenges, public case studies |
| Certs to consider | ACFE Certified Fraud Examiner, ACAMS CAMS (AML) |
| **Portfolio output** | A case file (`templates/case-file.md`) from a public case with verified sources and confidence levels |

#### Path C: OSINT and verification
| Step | Material |
|---|---|
| 1 | Scout 01 to 04 |
| 2 | Ledger 01 (the crime context) |
| Practice | Bellingcat guides and challenges, geolocation puzzles, Verification Handbook exercises |
| **Portfolio output** | A verification write-up with an archive, hashes and source grading |

#### Path D: AI security
| Step | Material |
|---|---|
| 1 | Aegis 01 to 04 |
| 2 | Forge 01, 02, 04 |
| Practice | Gandalf, HackAPrompt, Damn Vulnerable LLM Agent, garak and promptfoo on your own apps |
| **Portfolio output** | A small LLM app you built, a red-team report with success rates, and the fixes you applied |

#### Path E: Bio-cyber
| Step | Material |
|---|---|
| 1 | Helix 01 to 04 |
| 2 | Aegis 01 (AI risks apply to bio tools too) |
| Practice | Rosalind, Biopython tutorials, public datasets (NCBI, STRING, PDB) |
| **Portfolio output** | A reproducible notebook (sequences, graph analysis or docking) with a data-protection note |

#### Path F: Builder (security tools with AI)
| Step | Material |
|---|---|
| 1 | Forge 01 to 04 |
| 2 | Watchtower 02 and Ledger 02 (the data you will build on) |
| 3 | Aegis 02 to 04 (attack what you built) |
| **Portfolio output** | A tested, documented tool with a verifier, a README that states what data goes to the AI service, and no leaked secrets |

### Stage 3: Prove it (ongoing)
Every lab ends in a **mini project** and every track in a **capstone** (see [`PROJECTS.md`](PROJECTS.md)). Post phases as you go (see [`SHOWCASE.md`](SHOWCASE.md)).

- [ ] Publish 2 write-ups (blog, GitHub, or LinkedIn) explaining something you learned in your own words
- [ ] Contribute one fix or lab to this repo (see [`CONTRIBUTING.md`](CONTRIBUTING.md))
- [ ] Play 2 CTFs (CTFtime lists them) and write up one challenge
- [ ] Present at a showcase session
- [ ] Earn one entry-level certification that matches your path
- [ ] Build one portfolio project from your path and document it

### Where this can lead
| Interest | Example roles |
|---|---|
| Defender path | SOC analyst, detection engineer, incident responder |
| Investigator path | Cybercrime or fraud analyst, AML/financial-crime investigator, digital forensics examiner |
| OSINT path | Open-source investigator, trust-and-safety analyst, threat-intel analyst |
| AI security path | AI red-teamer, LLM application security engineer |
| Bio-cyber path | Bioinformatics security, health-data protection, research data security |
| Builder path | Security automation engineer, security tooling developer |

---

## Part 2: Project roadmap

These are **proposals**, not promises. Vote or suggest in GitHub Discussions or with the session-request issue template.

### Now: v2026-fall
- [x] Six sections: Watchtower, Ledger, Scout, Aegis, Helix, Forge
- [x] 25 labs with explanations and runnable code
- [x] Mini project per lab, capstone per track, sharing kit for GitHub and LinkedIn
- [x] Spotlight pages: why LLM security, why bio-cyber
- [x] Gemini and GDG Build with AI alignment
- [x] One-file resource list, ethics rules, templates
- [x] Two-semester plan: 7 live sessions per semester, exam-friendly
- [ ] Test every lab on Windows (WSL2), macOS and Linux and fix issues
- [ ] First live run, then collect feedback

### Next: next academic year (ideas)
Semester 2 of this year teaches Ledger and Aegis (see [`TERM_PLAN.md`](TERM_PLAN.md)). Beyond that:
- [ ] Teach **Scout** and **Helix** live (they are self-paced this year)
- [ ] **Cloud security lab** (Google Cloud IAM basics, logging and least privilege), a natural fit for a GDG
- [ ] **Windows forensics** lab (event logs, registry, Prefetch)
- [ ] **Threat intelligence** lab (indicators, MISP or OpenCTI basics)
- [ ] **Wazuh plus Cowrie integration** lab (honeypot alerts in a SIEM)
- [ ] **Arabic translations** of the key labs, so more local students can join
- [ ] Beginner **"Day 0"** pack: Linux, Python and Git crash course tailored to this repo
- [ ] Small **CTF** with challenges from each section

### Later (ideas)
- [ ] Guest speakers from industry and law enforcement-adjacent fields
- [ ] Student-run lab authoring program (mentored first pull requests)
- [ ] Inter-chapter collaboration with other GDG chapters
- [ ] Capstone: a term-long team project with a public demo day
- [ ] Mobile and web app security basics
- [ ] A "Responsible disclosure" mini-course

### How decisions are made
1. Feedback from attendees comes first (the 3-question form in [`GDG_SESSIONS.md`](GDG_SESSIONS.md)).
2. Every new lab must be self-contained, tested, ethical and use synthetic or public data.
3. Releases are tagged each term (`v2026-fall`, `v2027-spring`, ...).
