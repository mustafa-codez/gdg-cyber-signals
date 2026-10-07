#!/usr/bin/env python3
"""Generate a SYNTHETIC Linux auth.log with a brute-force attack hidden in normal noise.
All IPs come from documentation ranges (RFC 5737), so none are real.
Usage: python3 gen_auth_log.py > sample_auth.log
"""
import random
from datetime import datetime, timedelta

random.seed(7)
host = "lab-server"
users = ["alice", "bob", "deploy"]
attackers = ["203.0.113.45", "198.51.100.23"]
normal_ips = ["192.0.2.10", "192.0.2.11", "192.0.2.12"]
guess_users = ["root", "admin", "test", "oracle", "ubuntu", "postgres"]

t = datetime(2026, 1, 15, 8, 0, 0)
lines = []

def stamp(dt):
    return dt.strftime("%b %e %H:%M:%S")

pid = 2000
for _ in range(60):  # normal logins
    t += timedelta(seconds=random.randint(30, 600))
    pid += 1
    u, ip = random.choice(users), random.choice(normal_ips)
    lines.append((t, f"{stamp(t)} {host} sshd[{pid}]: Accepted publickey for {u} from {ip} port {random.randint(40000, 60000)} ssh2"))

for atk in attackers:  # brute force bursts
    start = datetime(2026, 1, 15, random.randint(9, 14), random.randint(0, 59), 0)
    for _ in range(random.randint(40, 80)):
        start += timedelta(seconds=random.randint(1, 4))
        pid += 1
        g = random.choice(guess_users)
        valid = "invalid user " if g not in users else ""
        lines.append((start, f"{stamp(start)} {host} sshd[{pid}]: Failed password for {valid}{g} from {atk} port {random.randint(30000, 60000)} ssh2"))
    # the attacker eventually gets in as a weak account
    start += timedelta(seconds=3)
    lines.append((start, f"{stamp(start)} {host} sshd[{pid+1}]: Accepted password for deploy from {atk} port 51515 ssh2"))
    lines.append((start + timedelta(seconds=5), f"{stamp(start)} {host} sudo:   deploy : TTY=pts/0 ; PWD=/home/deploy ; USER=root ; COMMAND=/bin/cat /etc/shadow"))

for _, l in sorted(lines, key=lambda x: x[0]):
    print(l)
