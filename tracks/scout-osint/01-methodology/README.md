# Lab 01: OSINT Methodology

**Track:** Scout | **Level:** Beginner | **Time:** ~60 min

## What is it?
Anyone can Google. Analysts follow a **process**, so results are reliable and defensible. The classic **intelligence cycle**:

1. **Direction / requirement:** Define the *question*. ("Is this charity's website a scam?")
2. **Collection:** Gather public information from many sources.
3. **Processing:** Organise, translate, verify, remove noise.
4. **Analysis:** Draw conclusions, state confidence, note gaps.
5. **Dissemination:** Report to the audience in a usable form.
6. **Feedback:** Refine the question.

## Source grading (Admiralty / NATO system)
Rate every source on two separate scales:
| Reliability of source | Credibility of information |
|---|---|
| A completely reliable | 1 confirmed by other sources |
| B usually reliable | 2 probably true |
| C fairly reliable | 3 possibly true |
| D not usually reliable | 4 doubtful |
| E unreliable | 5 improbable |
| F cannot judge | 6 cannot judge |
Example: a government registry entry corroborated twice = A1. An anonymous forum post = F6.

## Documentation habits
- Write the **requirement** and **purpose** before collecting.
- Log what you searched, when (UTC) and where (use `templates/osint-collection-log.md`).
- **Archive pages** so evidence survives deletion: https://web.archive.org (Save Page Now) and https://archive.ph.
- **Hash your screenshots/files** so you can show they weren't edited:
```bash
sha256sum screenshot_001.png >> hashes.txt
```
- Never rely on a single source. Corroborate with at least two independent ones.

## OPSEC for investigators
- Use a clean browser profile or VM; don't log in with personal accounts.
- Don't interact with targets (no friend requests, no likes).
- Some sites reveal who viewed them. Know which.
- Separate research identities from your real identity where lawful and permitted by platform rules.

## Walkthrough: a mini investigation
**Requirement:** "Is this website for a (fictional) investment company legitimate?" Use a real suspicious-looking public website from a scam-warning list, or a practice target from a CTF.

1. **Domain:** WHOIS (`whois example.com`), age, registrar, privacy-shielded?
   ```bash
   whois example.com | head -n 30
   dig +short example.com
   dig +short MX example.com
   ```
2. **Certificate history:** search the domain on https://crt.sh to see when certificates were issued and for which subdomains.
3. **Page history:** check the Wayback Machine for older versions.
4. **Company claims:** is the company in an official business registry? Is it listed by financial regulators (or on a regulator's warning list)?
5. **Images:** reverse search team photos (Lab 02). Stock photos are a classic red flag.
6. **Reputation:** scam-report databases, forums (low reliability: grade them).
7. **Write up** with confidence levels.

## Exercises
1. Complete a collection log for the mini investigation.
2. Rate each source with the A–F / 1–6 system and explain your grades.
3. Write a 5-line summary for a non-technical reader, including your confidence.

## Checkpoint
- Why separate source reliability from information credibility?
- Why archive and hash your evidence?

## Go deeper
- Bellingcat toolkit and guides (see `RESOURCES.md`)
- OSINT Framework (a map of tools by category)
- Trace Labs (ethical OSINT for missing persons, via sanctioned CTF events)
