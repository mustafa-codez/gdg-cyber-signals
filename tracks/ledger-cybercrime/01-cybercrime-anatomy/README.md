# Lab 01: Anatomy of Cybercrime

**Track:** Ledger | **Level:** Beginner | **Time:** ~45 min (reading and analysis, no tools)

## What is it?
Modern cybercrime is an **economy**, not just lone hackers. Specialists sell services to each other. Understanding the supply chain tells you where to detect and disrupt it.

## The ecosystem
| Role | What they do |
|---|---|
| Initial access broker | Sells footholds into networks (stolen credentials, exposed RDP/VPN) |
| Malware developer | Builds stealers, loaders, ransomware, sold as a service (MaaS / RaaS) |
| Affiliate / operator | Runs the attack using someone else's tooling |
| Money mule | Receives and forwards stolen funds, often unaware or coerced |
| Launderer / cash-out | Mixers, chain-hopping, exchanges, OTC brokers, gift cards |
| Infrastructure provider | Bulletproof hosting, domain registrars, proxies |

## Major crime types and where they leave traces
| Crime | How it works | Typical traces |
|---|---|---|
| **Phishing / BEC** | Trick a person into giving credentials or paying a fake invoice | Email headers, look-alike domains, bank transfers |
| **Investment / romance scams ("pig butchering")** | Long manipulation, then a fake trading platform | Fake sites, wallet addresses, chat logs |
| **Ransomware** | Encrypt and/or steal data, demand crypto | Ransom note, wallet address, leak site, negotiation chats |
| **Credential stuffing / account takeover** | Reuse leaked passwords | Login anomalies, IP clusters |
| **Online marketplace fraud** | Fake shops and sellers | Domain age, WHOIS, payment processors |
| **Money laundering** | Layer funds to hide origin | Transaction graphs, exchange deposits |

## Walkthrough: case study analysis
Pick a **public** case: a published indictment, a law-enforcement press release (Europol, US DOJ, Interpol, national police), or a threat report from a reputable security firm.

Fill this table:
| Question | Your answer |
|---|---|
| What was the crime and its victims? | |
| What was the criminal business model? | |
| What infrastructure did they use? | |
| How did they move or hide money? | |
| What led investigators to them? (technical + human) | |
| Which laws were used? | |
| What could have *prevented* or *detected* it earlier? | |

## The investigator's mindset
1. Crime needs **money flows** and **infrastructure**, and both leave traces.
2. Criminals make mistakes: reused usernames, reused wallets, real IPs, sloppy OPSEC.
3. Attribution is hard and slow. Be careful with confidence levels.
4. Evidence must be **collected lawfully** and **documented** to be useful.

## Exercises
1. Map one real case to MITRE ATT&CK techniques.
2. Draw the money flow as a diagram.
3. Write three "red flags" a bank or exchange could monitor for this crime type (AML typologies).

## Checkpoint
- Why is it useful to disrupt *infrastructure* and *cash-out* rather than only chase individuals?
- What's the difference between an indicator of compromise and evidence for court?

## Go deeper
- UNODC cybercrime resources, Europol IOCTA reports, FATF typology reports (links in `RESOURCES.md`)
- Podcast: Darknet Diaries (real cybercrime stories)
