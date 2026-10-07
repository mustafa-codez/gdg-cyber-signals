#!/usr/bin/env python3
"""Generate SYNTHETIC cryptocurrency-style transactions (CSV) with a hidden laundering pattern.
Addresses are fake labels, not real addresses.
Columns: tx_id, timestamp, from_addr, to_addr, amount
Usage: python3 gen_transactions.py > sample_transactions.csv
"""
import csv, random, sys
from datetime import datetime, timedelta

random.seed(11)
w = csv.writer(sys.stdout, lineterminator="\n")
w.writerow(["tx_id", "timestamp", "from_addr", "to_addr", "amount"])
t = datetime(2026, 2, 1, 9, 0)
n = 0

def tx(a, b, amt):
    global n, t
    n += 1
    t += timedelta(minutes=random.randint(1, 90))
    w.writerow([f"tx{n:04d}", t.isoformat(), a, b, round(amt, 4)])

# ordinary users trading among themselves
users = [f"user_{i:02d}" for i in range(30)]
for _ in range(150):
    a, b = random.sample(users, 2)
    tx(a, b, random.uniform(0.01, 2.0))

# scam victims paying a collector wallet
victims = [f"victim_{i:02d}" for i in range(12)]
for v in victims:
    tx(v, "scam_collector", random.uniform(0.3, 1.5))

# peel chain: collector moves funds along, peeling small amounts off to cash-out wallets
balance = 12.0
prev = "scam_collector"
for hop in range(1, 9):
    nxt = f"hop_{hop:02d}"
    peel = balance * 0.08
    tx(prev, nxt, balance - peel)
    tx(prev, f"cashout_{hop:02d}", peel)
    balance -= peel
    prev = nxt
tx(prev, "exchange_deposit", balance)
