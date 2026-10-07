#!/usr/bin/env python3
"""Flag SSH brute force and successful logins afterwards. Usage: python3 detect.py sample_auth.log"""
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
