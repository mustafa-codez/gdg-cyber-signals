# Lab 02: Log Analysis

**Track:** Watchtower | **Level:** Beginner | **Time:** ~60 min

## What is it?
A **log** is a timestamped record of something that happened (a login, a command, a connection). **Log analysis** means reading those records to answer: *What happened? Who did it? When? From where? Was it normal?*

The Linux file `/var/log/auth.log` (Debian/Ubuntu) or `/var/log/secure` (RHEL) records authentication events: SSH logins, `sudo` use, failed passwords.

## Why it matters
Every incident investigation starts with logs. SIEMs automate this, but if you can't read raw logs you can't trust or tune a SIEM.

## Setup
No target needed. We use a **synthetic** log containing a hidden brute-force attack.
```bash
cd labs/datasets
python3 gen_auth_log.py > sample_auth.log
wc -l sample_auth.log
```

## Walkthrough

### Step 1: Get familiar
```bash
head -n 5 sample_auth.log
grep -c "Failed password" sample_auth.log
grep -c "Accepted" sample_auth.log
```
Anatomy of a line:
`Jan 15 12:09:34  lab-server  sshd[2178]:  Failed password for invalid user admin from 203.0.113.45 port 51515 ssh2`
= time, host, program[pid], message.

### Step 2: Who is attacking? (top failing IPs)
```bash
grep "Failed password" sample_auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr
```
`awk '{print $(NF-3)}'` prints the 4th field from the end, which is the IP. `sort | uniq -c | sort -nr` counts and ranks.

### Step 3: Which usernames were guessed?
```bash
grep "Failed password" sample_auth.log | grep -oP 'for (invalid user )?\K\S+' | sort | uniq -c | sort -nr
```

### Step 4: Did any attacker succeed? (the question that matters)
```bash
for ip in $(grep "Failed password" sample_auth.log | awk '{print $(NF-3)}' | sort -u); do
  grep "Accepted" sample_auth.log | grep "$ip"
done
```
If an IP with many failures later has an **Accepted** line, assume compromise.

### Step 5: What did they do after?
```bash
grep -A2 "Accepted password" sample_auth.log
grep "sudo" sample_auth.log
```
A weak account used `sudo` to read `/etc/shadow`: credential theft (MITRE T1003.008).

### Step 6: Automate it in Python
```python
#!/usr/bin/env python3
import re, sys
from collections import Counter, defaultdict

fail = re.compile(r"Failed password for (?:invalid user )?(\S+) from (\S+)")
ok = re.compile(r"Accepted \w+ for (\S+) from (\S+)")

failures = Counter()
success = defaultdict(list)

for line in open(sys.argv[1]):
    m = fail.search(line)
    if m:
        failures[m.group(2)] += 1
    m = ok.search(line)
    if m:
        success[m.group(2)].append(m.group(1))

THRESHOLD = 10
for ip, n in failures.most_common():
    if n >= THRESHOLD:
        flag = "  <-- SUCCESSFUL LOGIN AFTER BRUTE FORCE" if ip in success else ""
        print(f"{ip:18} {n:4} failures{flag}")
```
Run: `python3 detect.py sample_auth.log` (the script is also saved in this folder as `detect.py`)

## Exercises
1. Add a timeline: print first and last failure time per attacker.
2. Add detection of "many different usernames from one IP" (username spraying).
3. Write the findings using `templates/incident-report.md`.

## Mini project: SSH Attack Analyzer
**Build:** Turn `detect.py` into a small tool that prints a timeline per attacker and writes a short Markdown report.

**Deliverables (in your own portfolio repo):** `analyzer.py`, a sample report, and a README that explains the findings in plain language.

**This is a phase of the track capstone:** see [`../CAPSTONE.md`](../CAPSTONE.md).

**Share it (optional):** "I built a log analyzer that spots brute force followed by a successful login." Follow the safe-sharing rules and templates in [`SHOWCASE.md`](../../../SHOWCASE.md).

## Checkpoint
- Why is a successful login after many failures the critical signal?
- What MITRE techniques did you observe? (T1110 Brute Force, T1078 Valid Accounts, T1003 Credential Dumping)

## Go deeper
- `man grep`, `man awk`, `man journalctl`
- On real systems: `journalctl -u ssh --since "1 hour ago"` and `last`, `lastb`
- TryHackMe "Linux Fundamentals" and "Splunk/Elastic" rooms (see `RESOURCES.md`)
