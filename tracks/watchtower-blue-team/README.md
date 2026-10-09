# Watchtower: Blue Team

Blue team = the defenders. You detect, investigate and contain attacks. This track follows the real analyst workflow.

| # | Lab | You will learn |
|---|---|---|
| 01 | [Wazuh SIEM](01-wazuh-siem) | Install a SIEM/XDR, connect an agent, see alerts, write a custom rule, monitor file changes |
| 02 | [Log analysis](02-log-analysis) | Read auth logs, spot brute force with shell and Python |
| 03 | [Sigma detections](03-sigma-detections) | Write vendor-neutral detection rules and map them to MITRE ATT&CK |
| 04 | [Honeypots with Cowrie](04-honeypots-cowrie) | Deploy deception safely, read attacker behaviour, turn it into detections |
| 05 | [Incident response](05-incident-response) | The IR lifecycle and writing a real report |

Recommended order: 02 → 01 → 03 → 04 → 05 (log literacy makes the SIEM easier to understand).

## Capstone
Every lab ends with a mini project that is one phase of this track's capstone: **Mini SOC**. See [`CAPSTONE.md`](CAPSTONE.md).

## More free Google resources for this track
- VirusTotal: https://www.virustotal.com
- Safe Browsing site status: https://transparencyreport.google.com/safe-browsing/search
- Google Security Blog: https://security.googleblog.com
- Free book, Building Secure and Reliable Systems: https://google.github.io/building-secure-and-reliable-systems/
- Cloud Shell (browser Linux terminal): https://cloud.google.com/shell
- Full list: [`docs/google-free-resources.md`](../../docs/google-free-resources.md)
