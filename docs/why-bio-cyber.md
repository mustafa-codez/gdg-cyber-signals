# Why a Bio-Cyber Track?

> **In one line:** biology runs on data, that data is some of the most sensitive on earth, and the skills used to analyse it are the same pattern-finding skills defenders use every day.

Bio-cyber is a **spotlight** in this chapter, not the main course. It gives the chapter a distinctive identity and a different way to practise the core security mindset.

## 1. Detection is detection
| Biology | Cybersecurity |
|---|---|
| Align two DNA sequences to find similar regions | Compare two binaries or scripts to find the same malware family |
| k-mers for fast sequence search | The same trick behind fuzzy hashing and similarity search |
| Protein interaction networks, finding hubs | Attack graphs, finding chokepoints |
| Shortest path between two proteins | Easiest attacker route to the database |

Students who learn one side of this table understand the other faster.

## 2. Bio data is the most sensitive data
Genomes, health records and brain recordings (EEG) are **permanent** (you can't reset your DNA), **identifying** (even "anonymous" genomic data can sometimes be re-identified), **shared** (your DNA reveals things about relatives) and **revealing** (health, ancestry, mental states). Protecting these pipelines is a real security-engineering job: access control, encryption, pseudonymisation, consent, auditing.

## 3. Data protection law is catching up
Genetic and health data get special treatment in laws such as GDPR, and national laws such as Egypt's Personal Data Protection Law (No. 151 of 2020). Understanding both the technology and the rules is a rare, valuable combination. (General education, not legal advice.)

## 4. A distinctive angle for this chapter
Most student security communities cover the same web and network topics. A computational bio-cyber strand makes this chapter memorable and gives members a story to tell: *"I applied security thinking to biological data."*

## 5. Computer science students can contribute immediately
You don't need a biology degree. Sequence analysis and graph algorithms are programming and data skills. The track starts from scratch.

## Boundaries
- **Computational only:** sequences, networks, data protection. No wet-lab or pathogen content.
- **Public or synthetic data only**, never real personal samples.
- Docking and bioinformatics results are **estimates**, not medical advice.
See `ETHICS.md`.

## What students get
- A first working feel for sequences, alignment and k-mers
- Graph algorithms used on a protein network *and* an attack graph
- A practical bio-data protection checklist (pseudonymisation, k-anonymity)
- A mini project after each lab and a capstone: **A Bio-Cyber Notebook**

## Spotlight session: "Your DNA Is a Password You Can't Reset" (semester 1, week 11, a light pre-exam week)
Helix is not taught as a full live track this year, so this spotlight is the live introduction; the labs are self-paced.

**Length:** 60 minutes | **Setup for students:** none (the host runs the demos) | **Nothing due**

| Min | Block | What happens |
|---|---|---|
| 0-10 | Hook | Why you can reset a password but not a genome |
| 10-25 | Sequences as signals | Host demo: align two short sequences; show k-mer similarity |
| 25-35 | Same idea, security side | The host runs k-mers on two script snippets: one family vs unrelated |
| 35-50 | Paper game | Pen-and-paper **k-anonymity** exercise on a tiny made-up table: who can be singled out? |
| 50-60 | Discussion | What should a lab promise people whose data it holds? |

**Take-home (optional, after exams):** [Helix 01](../tracks/helix-bio-cyber/01-sequences-as-signals) and [Helix 03](../tracks/helix-bio-cyber/03-bio-data-security).

## Where to go next
- Track: [`tracks/helix-bio-cyber`](../tracks/helix-bio-cyber)
- Capstone: [`tracks/helix-bio-cyber/CAPSTONE.md`](../tracks/helix-bio-cyber/CAPSTONE.md)
