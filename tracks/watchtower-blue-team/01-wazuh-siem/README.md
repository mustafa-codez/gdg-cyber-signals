# Lab 01: Wazuh SIEM

**Track:** Watchtower | **Level:** Beginner | **Time:** ~90 min

## What is it?
**Wazuh** is a free, open-source security platform. It combines a **SIEM** (Security Information and Event Management: collects and correlates logs) with **XDR/endpoint** features (file integrity monitoring, vulnerability detection, configuration checks).

It has three parts:
- **Agent**: small program on each monitored machine that sends logs and events.
- **Manager (server)**: analyses events against **rules** and creates **alerts**.
- **Indexer + Dashboard**: stores alerts and gives you a web UI to search them.

An analyst's daily job looks like: *alert fires → open dashboard → investigate → decide*. This lab lets you do that on your own machine.

## Why it matters
SOC (Security Operations Center) teams worldwide use SIEMs like this. Understanding rules, decoders and alerts is the core of SOC Level 1 work.

## Prerequisites
- A Linux VM (Ubuntu 22.04 or 24.04) with **4 CPU, 8 GB RAM, 50 GB disk** for the all-in-one server. (A second small VM or the same machine can be the monitored agent.)
- `curl` and `sudo` access.
- Use **VMs only** (see `ETHICS.md`).

## Setup: install the server (all-in-one)
Wazuh publishes a quickstart script. Check the **current version** on the official quickstart page first: https://documentation.wazuh.com/current/quickstart.html

```bash
# Replace <VERSION> with the version shown in the official quickstart (e.g. 4.x)
curl -sO https://packages.wazuh.com/<VERSION>/wazuh-install.sh
sudo bash ./wazuh-install.sh -a
```
At the end the installer prints an **admin username and password**. Save them.

Open the dashboard: `https://<server-ip>` (accept the self-signed certificate warning in your lab).

### Add an agent
In the dashboard: **Agents → Deploy new agent**. Choose the OS, enter the server IP, and the wizard generates the exact install command for you. Run it on the machine you want to monitor, then start the agent (the wizard shows the `systemctl` commands).

Verify:
```bash
# on the server
sudo /var/ossec/bin/agent_control -l
```
You should see your agent listed as **Active**.

## Walkthrough

### Step 1: Generate real alerts
On the **agent** machine, attempt a few failed SSH logins to a non-existent user from another machine (or the same one):
```bash
for i in $(seq 1 6); do ssh -o PreferredAuthentications=password -o PubkeyAuthentication=no fakeuser@<agent-ip>; done
```
Type a wrong password each time. In the dashboard, open **Threat Hunting / Security events** and search `fakeuser`. You should see authentication failure alerts with a **rule ID**, **level** and **MITRE ATT&CK** tag.

### Step 2: Understand an alert
Click an alert and read:
- `rule.id`, `rule.level` (severity 0 to 15), `rule.description`
- `rule.mitre.id` (ATT&CK technique)
- `data.srcip` (source IP) and `agent.name`

Rules live in `/var/ossec/ruleset/rules/` on the server. Never edit those; put your own in `/var/ossec/etc/rules/local_rules.xml`.

### Step 3: Write a custom rule
This rule fires when the built-in "SSH authentication failed" rule triggers 5 times within 60 seconds from the same IP. **First confirm the rule ID** in your dashboard (the built-in ID can differ by version) and put it in `if_matched_sid`.

```xml
<group name="local,syslog,sshd,">
  <rule id="100001" level="10" frequency="5" timeframe="60">
    <if_matched_sid>5716</if_matched_sid>
    <same_source_ip />
    <description>Possible SSH brute force: 5 failures in 60s from same IP</description>
    <mitre>
      <id>T1110</id>
    </mitre>
  </rule>
</group>
```
Apply it:
```bash
sudo nano /var/ossec/etc/rules/local_rules.xml     # add the rule
sudo /var/ossec/bin/wazuh-logtest                  # test before restarting
sudo systemctl restart wazuh-manager
```

### Step 4: Test a log line without attacking anything
`wazuh-logtest` lets you paste a log line and see which rule fires:
```bash
sudo /var/ossec/bin/wazuh-logtest
# paste this line and press Enter:
Jan 15 12:09:34 lab-server sshd[2178]: Failed password for invalid user admin from 203.0.113.45 port 51515 ssh2
```
Read the output: **Phase 1** (pre-decoding), **Phase 2** (decoding), **Phase 3** (rule match).

### Step 5: File Integrity Monitoring (FIM)
FIM alerts you when files change. On the **agent**, edit `/var/ossec/etc/ossec.conf` and inside `<syscheck>` add:
```xml
<directories check_all="yes" realtime="yes">/home/youruser/watched</directories>
```
```bash
mkdir -p ~/watched
sudo systemctl restart wazuh-agent
echo "hello" > ~/watched/note.txt
echo "tampered" >> ~/watched/note.txt
rm ~/watched/note.txt
```
In the dashboard, open the **File Integrity Monitoring** module. You should see *added*, *modified* and *deleted* events.

## Exercises
1. Find the rule ID and MITRE technique for a successful SSH login.
2. Change your custom rule to fire at **level 12** only if the source IP is **not** in `192.0.2.0/24`. (Hint: look up `<srcip negate="yes">`.)
3. Make FIM watch `/etc/passwd`. Add a user and observe the alert.
4. Load `labs/datasets/sample_auth.log` lines into `wazuh-logtest`. How many different rules trigger?

## Mini project: Custom Rule Pack v1
**Build:** Extend your custom rule work into a small rule pack with two rules (for example SSH brute force and a FIM alert) and explain each.

**Deliverables (in your own portfolio repo):** `local_rules.xml`, 2 screenshots of alerts (lab traffic only), a README saying what each rule detects and one false positive.

**This is a phase of the track capstone:** see [`../CAPSTONE.md`](../CAPSTONE.md).

**Share it (optional):** "I deployed a SIEM and wrote my first detection rules." Follow the safe-sharing rules and templates in [`SHOWCASE.md`](../../../SHOWCASE.md).

## Checkpoint
- What's the difference between an agent, a manager and an indexer?
- Why do we put custom rules in `local_rules.xml` instead of editing built-in rules?
- What does `rule.level` mean?

## Go deeper
- Docs: https://documentation.wazuh.com
- Rules syntax: search "Wazuh rules syntax" in the docs
- Practice: TryHackMe SOC Level 1 path, Blue Team Labs Online, CyberDefenders (see `RESOURCES.md`)
