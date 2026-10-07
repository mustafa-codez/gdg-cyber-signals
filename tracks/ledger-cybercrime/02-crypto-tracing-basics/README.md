# Lab 02: Crypto Tracing Basics

**Track:** Ledger | **Level:** Intermediate | **Time:** ~90 min

## What is it?
Public blockchains such as Bitcoin and Ethereum are **pseudonymous, not anonymous**. Every transaction is permanently visible. **Blockchain tracing** means following funds from address to address and linking addresses to real-world entities (exchanges, services) to identify where criminals cash out.

Key concepts:
- **Address**: a pseudonymous account identifier
- **Transaction (tx)**: moves value from one or more addresses to others
- **UTXO model (Bitcoin)**: transactions consume previous outputs and create new ones. **Account model (Ethereum)**: balances per address.
- **Common-input-ownership heuristic**: addresses used together as inputs in one Bitcoin transaction are probably controlled by the same entity.
- **Peel chain**: funds move down a long chain, peeling off small amounts each hop to cash-out addresses.
- **Mixers / chain-hopping**: techniques to break the trail (swapping assets, bridging chains).
- **Attribution**: linking addresses to entities using exchange data, labels and investigative work. This is where analytics firms and legal process (subpoenas to exchanges) matter.
- **Travel Rule / KYC / AML**: regulated exchanges identify customers, which is why a deposit to an exchange is an investigative lead.

## Setup
```bash
cd labs/datasets
python3 gen_transactions.py > sample_transactions.csv
pip install pandas networkx
```

## Walkthrough

### Step 1: Look at the data
```python
import pandas as pd
df = pd.read_csv("sample_transactions.csv", parse_dates=["timestamp"])
print(df.head())
print(df.groupby("to_addr")["amount"].sum().sort_values(ascending=False).head())
```

### Step 2: Build a graph and find who receives from many victims
```python
import networkx as nx
G = nx.DiGraph()
for r in df.itertuples():
    G.add_edge(r.from_addr, r.to_addr, amount=r.amount)

# addresses that receive from many different senders = collection points
indeg = sorted(G.in_degree(), key=lambda x: x[1], reverse=True)[:5]
print(indeg)
```

### Step 3: Trace everything downstream of the collector
```python
downstream = nx.descendants(G, "scam_collector")
print(len(downstream), "addresses downstream")
print(sorted(downstream))
```

### Step 4: Detect the peel chain
A peel chain looks like: a node with exactly two outgoing transfers, one large (continues the chain), one small (cash-out).
```python
def peel_chain(G, start):
    chain, node = [start], start
    while True:
        outs = sorted(G.out_edges(node, data=True), key=lambda e: e[2]["amount"], reverse=True)
        if len(outs) != 2:
            if len(outs) == 1:
                chain.append(outs[0][1])
            break
        chain.append(outs[0][1])
        node = outs[0][1]
    return chain

print(" -> ".join(peel_chain(G, "scam_collector")))
```
The end of the chain is `exchange_deposit`. In real investigations, **that** is where you'd send a legal request to the exchange.

### Step 5: Real-world practice (read-only, public)
Use a public explorer such as https://www.blockchain.com/explorer (Bitcoin) or https://etherscan.io (Ethereum):
1. Look up any publicly labelled address (exchanges and well-known contracts are labelled).
2. Follow its incoming and outgoing transactions.
3. Note timestamps, amounts, and counterparties.

## Exercises
1. Compute total victim losses and the share peeled to cash-out wallets.
2. Add a time-based check: were hops made within minutes of each other?
3. Write a mini case file (`templates/case-file.md`) describing the trail and what you'd ask the exchange for.

## Checkpoint
- Why is "anonymous" the wrong word for Bitcoin?
- Where does the trail usually become attributable to a person?
- Why do investigators care about exchange deposits?

## Go deeper
- Reports and education from blockchain-analytics firms (see `RESOURCES.md`)
- FATF virtual-asset guidance
- Book: "Tracers in the Dark" by Andy Greenberg (non-fiction story of blockchain investigations)
