# Capstone: Mini SOC

**Detect, investigate and report an attack end to end**

## Goal
Build a small defender's toolkit that takes a synthetic attack from raw logs to a finished incident report.

## How it works
The capstone is built **one phase at a time**. Each phase is the mini project at the end of a lab, so finishing the labs means you are already finishing the capstone. Post after each phase if you like (see `SHOWCASE.md`).

| Phase | Name | From | What you deliver |
|---|---|---|---|
| 1 | **SSH attack analyzer** | Lab 02 | A Python script that finds brute force and a successful login afterwards, with a timeline. |
| 2 | **SIEM rule pack** | Lab 01 | Wazuh deployed in a lab VM with 2 custom rules and screenshots of the alerts (synthetic or lab traffic only). |
| 3 | **Sigma rule pack** | Lab 03 | 3 Sigma rules mapped to MITRE ATT&CK, each with a false-positive note. |
| 4 | **Honeypot intelligence note** | Lab 04 | A one-page report from your own localhost Cowrie session, plus one detection idea. |
| 5 | **Incident report** | Lab 05 | A complete incident report for the synthetic attack, with timeline, IOCs and recommendations. |

## Final assembly
Combine phases 1 to 5 into one repo called `mini-soc` with a top-level README that tells the story: attack -> detection -> investigation -> report.

## Gemini layer (optional, encouraged)
Add a script that sends only **computed facts** to Gemini and asks it to rank sources and suggest actions. Verify the answer in code (see Forge Lab 02). Note in the README what AI did and how you checked it.

## Definition of done
- [ ] Runs or reads from a clean clone of your own repo
- [ ] README using `templates/student-project-readme.md`
- [ ] Synthetic or public data only; no secrets, no personal data
- [ ] States honestly what AI helped with and how it was checked
- [ ] Added one thing of your own beyond the labs (a feature, test, diagram or writeup)

## Share it
Starter post (edit before use):
> I built a Mini SOC: logs -> detections -> incident report. Here's what I learned about detection engineering.

Hashtags: #GDG #BlueTeam #SOC #Wazuh #Sigma #CyberSecurity

See [`../../SHOWCASE.md`](../../SHOWCASE.md) for the safe-sharing rules and templates.
