# Lab 03: Sigma Detections

**Track:** Watchtower | **Level:** Intermediate | **Time:** ~75 min

## What is it?
**Sigma** is an open, vendor-neutral format for writing detection rules in YAML. Think of it as "YARA for logs" or the "Snort rules of SIEM". You write the rule once and **convert** it to Splunk, Elastic, Microsoft Sentinel, Wazuh-compatible queries, and more.

**MITRE ATT&CK** is a public knowledge base of attacker tactics and techniques (e.g. T1110 Brute Force). Good detections are tagged with the technique they catch.

## Why it matters
Detection engineering is one of the fastest-growing blue-team careers. Sharing rules in Sigma lets the community defend together.

## Setup
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install sigma-cli
sigma plugin list                     # shows available backends and pipelines
sigma plugin install splunk           # example backend
```
Official rule repo (study these): https://github.com/SigmaHQ/sigma

## Walkthrough

### Step 1: Anatomy of a rule
Save as `ps_encoded.yml`:
```yaml
title: PowerShell Launched With Encoded Command
id: 6b2a6e4e-0f3a-4a1a-9a43-3e6f3f3c1a11
status: experimental
description: Detects PowerShell started with an encoded command, often used to hide payloads
references:
  - https://attack.mitre.org/techniques/T1059/001/
author: Your Name
date: 2026/01/15
logsource:
  category: process_creation
  product: windows
detection:
  selection_img:
    Image|endswith:
      - '\powershell.exe'
      - '\pwsh.exe'
  selection_cli:
    CommandLine|contains:
      - ' -enc '
      - ' -EncodedCommand '
  condition: selection_img and selection_cli
falsepositives:
  - Legitimate admin scripts or software deployment tools
level: medium
tags:
  - attack.execution
  - attack.t1059.001
```
Key parts:
- `logsource`: which logs this applies to
- `detection`: the matching logic (`|endswith`, `|contains` are **modifiers**)
- `condition`: how the selections combine
- `falsepositives`: honest notes for the analyst
- `tags`: ATT&CK mapping

### Step 2: Convert it to a SIEM query
```bash
sigma convert -t splunk ps_encoded.yml
```
(Some backends need a *pipeline* for field names; use `sigma convert --help` and the plugin docs.)

### Step 3: A Linux rule (SSH brute force style)
```yaml
title: Many Failed SSH Logins From One Source
id: 0d7c2c4f-7e51-4b43-8b8c-2f0e9c9d1b22
status: experimental
description: Brute force indicator on SSH
logsource:
  product: linux
  service: auth
detection:
  selection:
    message|contains: 'Failed password'
  timeframe: 1m
  condition: selection | count() by src_ip > 5
level: high
tags:
  - attack.credential_access
  - attack.t1110
```

### Step 4: Test against data
Your SIEM is the real test. Convert the rule, run it against `labs/datasets/sample_auth.log` ingested in Wazuh/Elastic/Splunk, and check that only the attackers match. If normal users match, **tune** the rule.

## Exercises
1. Write a rule for `whoami /priv` or `net user /domain` run from `cmd.exe` (discovery, T1033 / T1087).
2. Browse `SigmaHQ/sigma/rules/` and find three rules for a technique you studied. What false positives do they list?
3. Tag your rules with the right ATT&CK IDs on https://attack.mitre.org

## Checkpoint
- What's the difference between a rule that is *precise* and one that is *noisy*?
- Why include `falsepositives`?

## Go deeper
- Sigma docs: https://sigmahq.io
- ATT&CK Navigator to visualise coverage: https://mitre-attack.github.io/attack-navigator/
- Practice: CyberDefenders and Blue Team Labs Online (see `RESOURCES.md`)
