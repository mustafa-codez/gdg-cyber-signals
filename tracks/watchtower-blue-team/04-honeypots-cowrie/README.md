# Lab 04: Honeypots with Cowrie

**Track:** Watchtower | **Level:** Intermediate | **Time:** ~75 min

## What is it?
A **honeypot** is a decoy system that looks valuable but has no real purpose except to be attacked. Nobody legitimate should ever touch it, so **any interaction is suspicious**. That gives defenders:
- **Early warning** (someone is scanning or brute-forcing you)
- **Threat intelligence** (attacker IPs, passwords tried, commands run, malware downloaded)
- **Detection ideas** (turn real attacker behaviour into rules)

**Cowrie** is a popular medium-interaction SSH/Telnet honeypot. It pretends to be a Linux server. Attackers "log in" to a fake shell, and Cowrie records everything they type.

Interaction levels:
| Level | Example | Risk | Intel value |
|---|---|---|---|
| Low | OpenCanary, simple port listeners | Very low | Basic |
| Medium | **Cowrie** (emulated shell) | Low | Good |
| High | Real VM left vulnerable | **High** | Very high (experts only) |

**Honeytokens** are the same idea for data: fake credentials, files or URLs that alert you when used (see https://canarytokens.org).

## Why it matters
Deception is a growing defensive layer. It's cheap, has almost no false positives, and teaches you how real attackers behave.

## Safety first (read `ETHICS.md`)
- Run it in **Docker**, bound to **localhost** (`127.0.0.1`) for this lab.
- Do **not** expose it to the internet unless you understand network isolation, monitoring and your provider's policy.
- Never place real credentials or real data inside it.

## Setup
```bash
cd labs/docker-compose/honeypot
docker compose up -d
docker ps          # cowrie should be running
```
Or without compose:
```bash
docker run -d --name cowrie -p 127.0.0.1:2222:2222 cowrie/cowrie:latest
```

## Walkthrough

### Step 1: Play the attacker (against your own honeypot)
```bash
ssh -p 2222 root@127.0.0.1
```
Cowrie accepts most passwords by default (a few are blocked in its example user database). Try `password`. You're now in a **fake** shell. Try:
```bash
whoami
uname -a
ls /
cat /etc/passwd
wget http://example.com/test.sh      # Cowrie records download attempts
exit
```

### Step 2: Read what the honeypot recorded
Cowrie writes JSON logs. Find the file:
```bash
docker exec cowrie find / -name cowrie.json 2>/dev/null
```
Typical path: `/cowrie/cowrie-git/var/log/cowrie/cowrie.json`. Then:
```bash
docker exec cowrie cat /cowrie/cowrie-git/var/log/cowrie/cowrie.json | head -n 5
```
Key `eventid` values:
- `cowrie.session.connect`: someone connected
- `cowrie.login.failed` / `cowrie.login.success`: with `username` and `password`
- `cowrie.command.input`: each command typed (`input` field)
- `cowrie.session.file_download`: attempted download (`url`)

### Step 3: Analyse with jq
```bash
LOG=/cowrie/cowrie-git/var/log/cowrie/cowrie.json
# credentials tried
docker exec cowrie cat $LOG | jq -r 'select(.eventid|startswith("cowrie.login")) | [.timestamp,.src_ip,.username,.password,.eventid]|@tsv'
# commands typed
docker exec cowrie cat $LOG | jq -r 'select(.eventid=="cowrie.command.input") | [.timestamp,.src_ip,.input]|@tsv'
```

### Step 4: Python summary
```python
import json, sys
from collections import Counter
creds, cmds = Counter(), Counter()
for line in open(sys.argv[1]):
    e = json.loads(line)
    if e["eventid"].startswith("cowrie.login"):
        creds[(e.get("username"), e.get("password"))] += 1
    elif e["eventid"] == "cowrie.command.input":
        cmds[e["input"]] += 1
print("Top credentials:", creds.most_common(5))
print("Top commands:", cmds.most_common(5))
```
Copy the log out first: `docker cp cowrie:/cowrie/cowrie-git/var/log/cowrie/cowrie.json .`

### Step 5: Turn behaviour into a detection
Real-world attackers on honeypots usually run discovery then try to download tools. A Sigma-style idea:
```yaml
title: Shell Discovery Followed By Download Tool Use
logsource: { product: linux, category: process_creation }
detection:
  discovery: { CommandLine|contains: ['uname -a', 'cat /proc/cpuinfo', 'whoami'] }
  download:  { CommandLine|contains: ['wget ', 'curl ', 'tftp '] }
  condition: discovery and download
tags: [attack.discovery, attack.t1082, attack.command_and_control, attack.t1105]
level: medium
```

### Step 6: Send honeypot logs to Wazuh (optional)
Install a Wazuh agent on the host running Cowrie and add to `ossec.conf`:
```xml
<localfile>
  <log_format>json</log_format>
  <location>/path/to/cowrie.json</location>
</localfile>
```

## Cleanup
```bash
docker compose down -v
```

## Exercises
1. Which commands do you think a real botnet would run first? Check public Cowrie research for ideas.
2. Create a free canary token at https://canarytokens.org (a "web bug" or document token), open it, and read the alert you receive.
3. Write a one-page summary of your honeypot session using `templates/incident-report.md` (treat your own test as the "incident").

## Checkpoint
- Why do honeypots have very low false positives?
- Why must a honeypot be isolated from real systems?

## Go deeper
- Cowrie: https://github.com/cowrie/cowrie and https://docs.cowrie.org
- OpenCanary: https://github.com/thinkst/opencanary
- T-Pot (multi-honeypot platform): https://github.com/telekom-security/tpotce
- Canary tokens: https://canarytokens.org
