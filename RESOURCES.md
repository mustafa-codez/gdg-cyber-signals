# Resources: Everything in One Place

> Links change. If one is dead, open an issue (`.github/ISSUE_TEMPLATE/lab-bug.md`). Items marked *(search)* have no stable URL I'm confident about: search the name.

## Contents
1. [Hands-on practice platforms](#1-hands-on-practice-platforms)
2. [Watchtower: Blue Team](#2-watchtower-blue-team)
3. [Ledger: Cybercrime, forensics, AML, law](#3-ledger-cybercrime-forensics-aml-law)
4. [Scout: OSINT](#4-scout-osint)
5. [Aegis: LLM security](#5-aegis-llm-security)
6. [Helix: Bio-Cyber](#6-helix-bio-cyber)
7. [Frameworks and standards](#7-frameworks-and-standards)
   - [Gemini and Build with AI](#gemini-and-build-with-ai)
8. [People, channels and newsletters to follow](#8-people-channels-and-newsletters-to-follow)
9. [Podcasts and books](#9-podcasts-and-books)
10. [Certifications and career paths](#10-certifications-and-career-paths)
11. [Communities and events](#11-communities-and-events)

---

## 1. Hands-on practice platforms
| Platform | Best for | Link |
|---|---|---|
| TryHackMe | Guided beginner-friendly rooms, SOC Level 1 path | https://tryhackme.com |
| Hack The Box (+ Academy) | Harder machines, structured modules | https://www.hackthebox.com |
| Blue Team Labs Online | Blue team and DFIR challenges | https://blueteamlabs.online |
| CyberDefenders | SOC, DFIR, threat hunting labs | https://cyberdefenders.org |
| LetsDefend | SOC analyst simulation | https://letsdefend.io |
| PortSwigger Web Security Academy | Free web-security training | https://portswigger.net/web-security |
| OverTheWire | Linux and wargames | https://overthewire.org |
| picoCTF | Beginner CTF | https://picoctf.org |
| CTFtime | CTF calendar | https://ctftime.org |
| Digital Corpora | Forensic practice images | https://digitalcorpora.org |
| Rosalind | Bioinformatics puzzles | https://rosalind.info |

## 2. Watchtower: Blue Team
- Wazuh documentation: https://documentation.wazuh.com
- Wazuh GitHub: https://github.com/wazuh/wazuh
- Sigma rules repository: https://github.com/SigmaHQ/sigma
- Sigma docs: https://sigmahq.io
- MITRE ATT&CK: https://attack.mitre.org
- ATT&CK Navigator: https://mitre-attack.github.io/attack-navigator/
- Cowrie honeypot: https://github.com/cowrie/cowrie and https://docs.cowrie.org
- OpenCanary: https://github.com/thinkst/opencanary
- T-Pot honeypot platform: https://github.com/telekom-security/tpotce
- Canary tokens (free honeytokens): https://canarytokens.org
- Security Onion (network defence distro): https://securityonionsolutions.com
- Elastic Security and Splunk free training (search: "Splunk Fundamentals 1 free", "Elastic Security free training")
- Atomic Red Team (safe attack simulations for testing detections): https://github.com/redcanaryco/atomic-red-team
- NIST SP 800-61 Incident Handling Guide: https://csrc.nist.gov
- SANS Reading Room (free papers): https://www.sans.org/white-papers/

## 3. Ledger: Cybercrime, forensics, AML, law
**Cybercrime and law**
- UNODC Cybercrime: https://www.unodc.org/unodc/en/cybercrime/
- Council of Europe Budapest Convention: https://www.coe.int/en/web/cybercrime/the-budapest-convention
- Europol (cybercrime, IOCTA reports): https://www.europol.europa.eu
- Interpol cybercrime: https://www.interpol.int
- FATF (AML/CFT standards and virtual-asset guidance): https://www.fatf-gafi.org
- US DOJ cybercrime press releases (search: "justice.gov cybercrime")

**Crypto tracing**
- Blockchain explorers: https://www.blockchain.com/explorer, https://etherscan.io
- Learn from blockchain-analytics firm reports and blogs (Chainalysis, Elliptic, TRM Labs: *search*)
- Book: *Tracers in the Dark* by Andy Greenberg

**Digital forensics**
- Autopsy: https://www.autopsy.com
- The Sleuth Kit: https://www.sleuthkit.org
- Volatility 3 (memory forensics): https://github.com/volatilityfoundation/volatility3
- Eric Zimmerman's tools (Windows artefacts): https://ericzimmerman.github.io
- SANS DFIR: https://www.sans.org/digital-forensics-incident-response/
- Digital Corpora images: https://digitalcorpora.org
- CAINE / SIFT Workstation forensic distros *(search)*

## 4. Scout: OSINT
- Bellingcat: https://www.bellingcat.com
- Bellingcat Online Investigation Toolkit: https://bellingcat.gitbook.io/toolkit
- OSINT Framework (tool map): https://osintframework.com
- Verification Handbook: https://verificationhandbook.com
- Trace Labs (ethical OSINT CTFs for missing persons): https://www.tracelabs.org
- Wayback Machine: https://web.archive.org
- archive.today: https://archive.ph
- crt.sh certificate search: https://crt.sh
- Reverse image: https://lens.google.com, https://tineye.com, https://yandex.com/images
- Geolocation: https://www.openstreetmap.org, https://overpass-turbo.eu, https://www.mapillary.com, https://www.suncalc.org, https://earth.google.com
- Practice: GeoGuessr, Quiztime (search), Bellingcat challenges
- Media provenance: https://c2pa.org, https://contentcredentials.org
- Human-rights video verification: https://www.witness.org
- Shodan / Censys (internet-exposed device search; use legally): https://www.shodan.io, https://censys.com

## 5. Aegis: LLM security
**Practice targets (legal, built for attacking)**
- **Gandalf** by Lakera: https://gandalf.lakera.ai
- HackAPrompt: https://www.hackaprompt.com
- Immersive Labs prompt injection challenge (search: "Immersive Labs prompt injection")
- Damn Vulnerable LLM Agent: https://github.com/WithSecureLabs/damn-vulnerable-llm-agent
- Prompt Airlines (Wiz CTF) (search: "Wiz Prompt Airlines")
- Tensor Trust game *(search)*

**Frameworks**
- OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- OWASP GenAI Security Project: https://genai.owasp.org
- MITRE ATLAS: https://atlas.mitre.org
- Google Secure AI Framework (SAIF): https://saif.google
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework

**Tools**
- garak: https://github.com/NVIDIA/garak
- promptfoo: https://github.com/promptfoo/promptfoo
- PyRIT: https://github.com/Azure/PyRIT
- Ollama (run models locally): https://ollama.com

**Reading**
- Simon Willison's blog on prompt injection: https://simonwillison.net
- Anthropic, OpenAI, Google DeepMind safety and security research pages *(search)*

## 6. Helix: Bio-Cyber
- Biopython: https://biopython.org
- NCBI (sequences, BLAST): https://www.ncbi.nlm.nih.gov, https://blast.ncbi.nlm.nih.gov
- RCSB Protein Data Bank: https://www.rcsb.org
- STRING (protein networks): https://string-db.org
- NetworkX: https://networkx.org
- AutoDock Vina: https://vina.scripps.edu and https://autodock-vina.readthedocs.io
- UCSF ChimeraX: https://www.cgl.ucsf.edu/chimerax/
- Galaxy: https://usegalaxy.org
- Rosalind: https://rosalind.info
- GA4GH (genomic data standards and security): https://www.ga4gh.org
- NeuroRights Foundation: https://neurorightsfoundation.org
- MNE-Python (EEG/MEG analysis): https://mne.tools

## 7. Frameworks and standards
- MITRE ATT&CK, ATLAS, D3FEND (defensive techniques): https://d3fend.mitre.org
- NIST Cybersecurity Framework: https://www.nist.gov/cyberframework
- CIS Controls: https://www.cisecurity.org/controls
- OWASP Top 10 (web): https://owasp.org/www-project-top-ten/
- ISO/IEC 27001 (overview, search)
- Lockheed Martin Cyber Kill Chain, Diamond Model of Intrusion Analysis *(search)*

### Google's free and underrated resources
A full, categorised list lives in [`docs/google-free-resources.md`](docs/google-free-resources.md). Highlights: VirusTotal, OSV and OSV-Scanner, deps.dev, Google CTF, Gruyere, the free Secure and Reliable Systems and SRE books, Fact Check Explorer, Dataset Search, NotebookLM, Cloud Shell, AlphaFold DB, Google Summer of Code.

### Our chapter: GDG on Campus AAST Abu Qir
- Link hub: https://bio.link/gdgaast
- Facebook: https://www.facebook.com/GDGAAST/
- Instagram: https://www.instagram.com/aast.gdgc/
- LinkedIn: https://www.linkedin.com/company/gdg-on-campus-aast-abu-qir/
- WhatsApp community: https://chat.whatsapp.com/LcIrU7sHcqFG43t1u3IPJs
- Chapter page: https://gdg.community.dev/gdg-on-campus-arab-academy-for-science-technology-and-maritime-transport-abu-qir-egypt/
- Event suggestions form: https://forms.gle/Cy4hsiuUC1S162Cj6
- More: [`docs/community-aast-abu-qir.md`](docs/community-aast-abu-qir.md)

### Gemini and Build with AI
**Start here**
- Google AI Studio (experiment and create API keys): https://aistudio.google.com
- API key page: https://aistudio.google.com/apikey
- Gemini API docs: https://ai.google.dev/gemini-api/docs
- Quickstart: https://ai.google.dev/gemini-api/docs/quickstart
- Models list (names change, check often): https://ai.google.dev/gemini-api/docs/models
- Rate limits and pricing: https://ai.google.dev/gemini-api/docs/rate-limits
- Structured output (JSON schemas): https://ai.google.dev/gemini-api/docs/structured-output
- Gemini API cookbook (examples and notebooks): https://github.com/google-gemini/cookbook
- Python SDK: `pip install google-genai` (https://github.com/googleapis/python-genai)

**Tools and platforms**
- Gemini CLI (open-source terminal agent): https://github.com/google-gemini/gemini-cli
- Google Colab (browser notebooks, no install): https://colab.research.google.com
- Vertex AI (enterprise Gemini on Google Cloud): https://cloud.google.com/vertex-ai
- Google Cloud Skills Boost (labs and learning paths): https://www.cloudskillsboost.google
- Google Developer Groups: https://developers.google.com/community/gdg
- Build with AI (community-led Gemini events, check the current season): https://developers.google.com/community/build-with-ai/faq
- GDG community platform (events): https://gdg.community.dev

**Building safely**
- Google Secure AI Framework (SAIF): https://saif.google
- OWASP Top 10 for LLM Applications (see section 5)
- Secret scanning: https://github.com/gitleaks/gitleaks, https://github.com/Yelp/detect-secrets
- Python dependency audit: https://github.com/pypa/pip-audit
- Bandit (Python security linter): https://github.com/PyCQA/bandit
- Pydantic (validate model output): https://docs.pydantic.dev

## 8. People, channels and newsletters to follow
Search these on YouTube or their sites. Channel names, not guaranteed URLs.

**General cybersecurity and blue team**
- John Hammond (malware analysis, CTFs, news)
- David Bombal (networking, security interviews)
- The Cyber Mentor / TCM Security (practical ethical hacking, SOC)
- NetworkChuck (beginner-friendly)
- LiveOverflow (deep technical)
- IppSec (HackTheBox walkthroughs)
- 13Cubed (digital forensics and incident response)
- Black Hills Information Security (webcasts)
- SANS Institute (free talks)
- Simply Cyber (careers and community)

**OSINT and investigations**
- Bellingcat (articles, videos, workshops)
- Week in OSINT newsletter (Sector035)
- The OSINT Curious Project
- Trace Labs community

**Cybercrime and threat intel**
- Brian Krebs, *KrebsOnSecurity*: https://krebsonsecurity.com
- The Hacker News (news): https://thehackernews.com
- BleepingComputer (news): https://www.bleepingcomputer.com
- The Record by Recorded Future (news)
- Microsoft, Google Threat Intelligence, Mandiant, CrowdStrike blogs *(search)*

**AI security**
- Simon Willison (blog)
- Lakera blog and Gandalf community
- OWASP GenAI project updates

**Bioinformatics**
- Rosalind community, Biostars forum: https://www.biostars.org
- Bioinformatics YouTube channels (search: "Biopython tutorial", "intro bioinformatics")

## 9. Podcasts and books
**Podcasts:** Darknet Diaries (https://darknetdiaries.com), Risky Business (https://risky.biz), Malicious Life, Hacking Humans, CyberWire Daily, 7 Minute Security.

**Books:**
- *Tracers in the Dark*, Andy Greenberg (crypto investigations)
- *Sandworm*, Andy Greenberg (state attacks)
- *The Cuckoo's Egg*, Cliff Stoll (classic investigation story)
- *Practical Malware Analysis*, Sikorski and Honig
- *The Art of Memory Forensics*, Ligh et al.
- *Applied Network Security Monitoring*, Sanders and Smith
- *Bioinformatics Data Skills*, Vince Buffalo
- *Practical Cryptography* resources (search)

## 10. Certifications and career paths
Entry level: CompTIA Security+, Google Cybersecurity Certificate, ISC2 Certified in Cybersecurity (CC), TryHackMe SOC Level 1 / Pre-Security paths.
Defensive: Blue Team Level 1 (BTL1), CompTIA CySA+, GIAC GCIH / GCFA, Splunk and Elastic certs.
Investigation and fraud: ACFE Certified Fraud Examiner, ACAMS CAMS (AML), vendor blockchain-analytics certifications.
OSINT: Trace Labs, SANS SEC487 (search).
AI security: OWASP and vendor training; no dominant cert yet.

## 11. Communities and events
- Google Developer Groups: https://developers.google.com/community/gdg
- OWASP local chapters: https://owasp.org/chapters/
- Local security meetups (search "BSides" + your region); BSides events are community-run and beginner friendly
- DEF CON (Blue Team Village, Recon Village, AI Village), Black Hat, FIRST conference *(search)*
- Discord / Reddit: r/netsec, r/blueteamsec, r/OSINT, r/cybersecurity (read community rules first)
