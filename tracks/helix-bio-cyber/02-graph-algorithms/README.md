# Lab 02: Graph Algorithms for Biological and Attack Networks

**Track:** Helix | **Level:** Intermediate | **Time:** ~75 min

## What is it?
A **graph** has **nodes** (things) and **edges** (relationships).
- In biology: nodes are proteins, edges are interactions (a **protein-protein interaction, PPI, network**).
- In security: nodes are hosts or accounts, edges are "can reach" or "can log in to" (an **attack graph**).

The same algorithms answer both:
| Algorithm | Biology question | Security question |
|---|---|---|
| **Shortest path (Dijkstra)** | Strongest chain of interactions between two proteins | Easiest route from the internet to the database |
| **Centrality** | Which protein is a hub? | Which host is a chokepoint to protect? |
| **Connected components / communities** | Functional modules | Network segments, botnet clusters |

**Dijkstra's algorithm** finds the lowest-cost path in a graph with non-negative edge weights. To find the *most reliable* path, convert confidence `p` into a cost such as `-log(p)` so cheap edges = trustworthy ones.

## Setup
```bash
pip install networkx matplotlib
```
Real PPI data: https://string-db.org (download a small network for a public example).

## Walkthrough

### Step 1: A toy interaction network
```python
import math, networkx as nx

G = nx.Graph()
interactions = [   # (protein A, protein B, confidence 0..1)
    ("P1", "P2", 0.95), ("P2", "P3", 0.90), ("P1", "P4", 0.60),
    ("P4", "P3", 0.70), ("P3", "P5", 0.85), ("P2", "P6", 0.40),
    ("P6", "P5", 0.55),
]
for a, b, p in interactions:
    G.add_edge(a, b, confidence=p, cost=-math.log(p))
```

### Step 2: Most reliable path
```python
path = nx.dijkstra_path(G, "P1", "P5", weight="cost")
cost = nx.dijkstra_path_length(G, "P1", "P5", weight="cost")
reliability = math.exp(-cost)
print(path, round(reliability, 3))
```
The combined reliability is the product of the edge confidences along the path.

### Step 3: Find hubs
```python
deg = nx.degree_centrality(G)
btw = nx.betweenness_centrality(G, weight="cost")
for n in sorted(G, key=btw.get, reverse=True):
    print(n, round(deg[n], 2), round(btw[n], 2))
```
**Betweenness** is high for nodes many shortest paths pass through, i.e. chokepoints.

### Step 4: The same code as an attack graph
```python
A = nx.DiGraph()
steps = [   # (from, to, difficulty 1..10)
    ("internet", "web-server", 3), ("web-server", "app-server", 4),
    ("internet", "vpn", 6), ("vpn", "app-server", 2),
    ("app-server", "database", 5), ("web-server", "database", 9),
]
for a, b, d in steps:
    A.add_edge(a, b, difficulty=d)

route = nx.dijkstra_path(A, "internet", "database", weight="difficulty")
print("Easiest attacker route:", route)

# Which single node, if hardened or removed, forces the attacker onto a harder route?
for node in ["web-server", "app-server", "vpn"]:
    H = A.copy(); H.remove_node(node)
    try:
        print(node, "removed ->", nx.dijkstra_path_length(H, "internet", "database", weight="difficulty"))
    except nx.NetworkXNoPath:
        print(node, "removed -> NO PATH (critical chokepoint)")
```
Defenders use exactly this logic to decide where to put controls first.

### Step 5: Draw it
```python
import matplotlib.pyplot as plt
nx.draw(G, with_labels=True, node_color="#444", font_color="white", edge_color="#888")
plt.savefig("network.png", dpi=150)
```

## Exercises
1. Add a node and edges to the attack graph (e.g. a phishing path to an employee laptop). How does the easiest route change?
2. Download a small STRING network for a public protein and load it with `pandas` + `networkx`. Which proteins have the highest betweenness?
3. Find all nodes within 2 hops of your target node with `nx.single_source_shortest_path_length(G, node, cutoff=2)`.

## Checkpoint
- Why transform confidence with `-log(p)`?
- What does high betweenness mean in each domain?

## Go deeper
- NetworkX docs: https://networkx.org
- STRING database: https://string-db.org
- MITRE Caldera / BloodHound (attack-graph tools in security)
