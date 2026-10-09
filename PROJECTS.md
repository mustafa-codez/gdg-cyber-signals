# Projects: Build Something You Can Show

Learning sticks when you **make** something. So the whole repo works like this:

```
Lab  ->  Mini project  ->  Track capstone  ->  Portfolio
(learn)  (build + share)   (big project)       (GitHub + LinkedIn)
```

## 1. Mini project (after every lab)
Every lab README ends with a **Mini project** section: a small, finished thing you can build in about an hour or two on top of what you just learned. It is also **one phase of the track capstone**, so the work adds up.

A mini project is "done" when:
- [ ] It runs (or reads) from a clean copy of your repo
- [ ] It has a short README: what it does, how to run it, what you learned
- [ ] It uses only synthetic or public data
- [ ] No secrets or personal data are in the files or git history

## 2. Track capstone (when you finish a track)
Each track has a **capstone**: the bigger project you assemble from the phases you've already built.

| Track | Capstone | Phases come from |
|---|---|---|
| Watchtower | **Mini SOC**: detect, investigate and report an attack end to end | Labs 02, 01, 03, 04, 05 |
| Ledger | **Follow the Money**: a case file with a traced transaction chain and legal map | Labs 01 to 04 |
| Scout | **Verification Dossier**: a verified, documented OSINT investigation | Labs 01 to 04 |
| Aegis | **Break and Harden an LLM App** | Labs 01 to 04 |
| Helix | **A Bio-Cyber Notebook** | Labs 01 to 04 |
| Forge | **An AI Security Tool with a Verifier** (Gemini) | Labs 01 to 04 |

Details are in each track's `CAPSTONE.md`.

## 3. Build in public: post as you go
You don't have to wait until a capstone is finished. Share **phases**:
- "I finished Part 1 of my Mini SOC: an SSH log analyzer."
- "Part 3: I wrote three Sigma rules mapped to MITRE ATT&CK."
- "Capstone done: my Mini SOC is on GitHub."

Posting a phase after each lab gives you a steady trail of proof of learning. Follow the safe-sharing rules in [`SHOWCASE.md`](SHOWCASE.md).

## 4. Your portfolio repository
Create one repo in your own account, for example `my-cyber-signals-portfolio`:
```
my-cyber-signals-portfolio/
├── README.md                  # who you are, what you built, links
├── watchtower-mini-soc/       # capstone, with phase folders
│   ├── README.md
│   ├── 01-ssh-analyzer/
│   ├── 02-wazuh-rules/
│   └── ...
├── ledger-follow-the-money/
└── ...
```
Start from [`templates/student-project-readme.md`](templates/student-project-readme.md).

## 5. Gemini as a co-pilot
Every capstone has an **optional "Gemini layer"**: a place where you use Gemini to help (explain an alert, extract case notes, harden a Gemini-powered bot). The rule is always: **AI proposes, code verifies, a human decides.** See [`docs/gemini-and-gdg.md`](docs/gemini-and-gdg.md).

## 6. Timing around the term
Projects follow the exam-friendly plan in [`TERM_PLAN.md`](TERM_PLAN.md): no deadlines in exam weeks or in the light weeks before them.

## 7. What counts as a good capstone
| Criteria | Question to ask |
|---|---|
| Works | Can a stranger run it from the README? |
| Explained | Does the README say what, why and what you learned? |
| Honest | Does it state limits, data used, and any AI help? |
| Safe | Synthetic or public data only; nothing sensitive |
| Yours | Did you add something beyond the lab (a feature, a test, a writeup)? |
