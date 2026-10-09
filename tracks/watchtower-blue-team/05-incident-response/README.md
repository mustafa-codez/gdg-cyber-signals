# Lab 05: Incident Response

**Track:** Watchtower | **Level:** Beginner to Intermediate | **Time:** ~60 min

## What is it?
**Incident response (IR)** is the structured way an organisation handles a security incident. The widely used model (NIST SP 800-61) has four phases:

1. **Preparation**: tools, playbooks, contacts, logging in place
2. **Detection and Analysis**: confirm it's real, scope it, classify severity
3. **Containment, Eradication and Recovery**: stop the spread, remove the cause, restore safely
4. **Post-incident activity**: lessons learned, new detections

SANS uses six steps (Preparation, Identification, Containment, Eradication, Recovery, Lessons Learned). They describe the same flow.

## Why it matters
Anyone can run a scan. Professionals are valued for calm, structured response and clear reports.

## Walkthrough: investigate the lab incident
You will use the artefacts from Lab 02 (`sample_auth.log`, `detect.py`).

### Step 1: Triage
Questions to answer first:
- What happened and when? (first/last event)
- Which assets and accounts are involved?
- Is the attacker still in? (look for activity after the successful login)

### Step 2: Scope with commands
```bash
grep "Accepted password" sample_auth.log                     # successful logins
grep "sudo" sample_auth.log                                  # privilege use
grep "198.51.100.23" sample_auth.log | tail -n 5             # activity from one attacker
```

### Step 3: Containment (what you would do on a real host)
```bash
sudo passwd -l deploy                      # lock the compromised account
sudo ufw deny from 198.51.100.23           # block attacker IP (example firewall)
sudo pkill -KILL -u deploy                 # terminate the account's sessions
```
Containment preserves evidence first: do **not** wipe the machine before you've collected logs.

### Step 4: Write the report
Copy `templates/incident-report.md` and fill it in:
- Timeline in **UTC**
- IOCs (attacker IPs, usernames tried)
- ATT&CK mapping: T1110 (Brute Force), T1078 (Valid Accounts), T1003 (OS Credential Dumping)
- Recommendations: disable password SSH, enforce keys + MFA, `fail2ban`, alert on `sudo` reads of `/etc/shadow`

### Step 5: Lessons learned
Turn findings into permanent defences: a Wazuh rule (Lab 01), a Sigma rule (Lab 03), a hardening checklist.

## Exercises
1. Write the report for the second attacker IP.
2. Explain the incident in three sentences for a non-technical manager.
3. Draft a one-page playbook titled "Suspected SSH brute force".

## Mini project: Incident Report
**Build:** Write a full incident report for the lab's synthetic attack.

**Deliverables (in your own portfolio repo):** The completed `templates/incident-report.md`, with UTC timeline, IOCs, ATT&CK mapping and recommendations.

**This is a phase of the track capstone:** see [`../CAPSTONE.md`](../CAPSTONE.md).

**Share it (optional):** "I wrote my first incident report from raw logs." Follow the safe-sharing rules and templates in [`SHOWCASE.md`](../../../SHOWCASE.md).

## Checkpoint
- Why preserve evidence before containment steps like rebooting?
- What's the difference between eradication and recovery?

## Go deeper
- NIST SP 800-61 (Computer Security Incident Handling Guide)
- Practice: Blue Team Labs Online, CyberDefenders, TryHackMe SOC path (see `RESOURCES.md`)
