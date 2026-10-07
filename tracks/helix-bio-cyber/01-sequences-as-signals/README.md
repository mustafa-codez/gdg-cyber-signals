# Lab 01: Sequences as Signals

**Track:** Helix | **Level:** Beginner | **Time:** ~75 min

## What is it?
Biology stores information in **sequences**:
- **DNA:** a string over A, C, G, T
- **RNA:** like DNA with U instead of T
- **Protein:** a string over 20 amino-acid letters

**Bioinformatics** asks questions like "how similar are these two sequences?" The core tool is **sequence alignment**: line up two sequences to find matching regions even when letters are inserted, deleted or changed.
- **Global alignment** compares whole sequences; **local alignment** finds the best matching region.
- **BLAST** is the famous tool that searches a database for similar sequences: https://blast.ncbi.nlm.nih.gov

## The security connection
Detection is detection. Malware families, phishing kits and binaries are also sequences (bytes, API calls, opcodes), and defenders use the **same ideas**: similarity search, k-mers, alignment and clustering, to group variants of the same family and spot new ones.

## Setup
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install biopython
```

## Walkthrough

### Step 1: Sequences in Python
```python
from Bio.Seq import Seq
dna = Seq("ATGGCCATTGTAATGGGCCGCTGA")
print(dna.complement())
print(dna.reverse_complement())
print(dna.transcribe())       # DNA -> RNA
print(dna.translate())        # DNA -> protein (stop codon shown as *)
```

### Step 2: Fetch a real public sequence from NCBI
```python
from Bio import Entrez, SeqIO
Entrez.email = "you@example.com"      # NCBI asks for a real contact email
handle = Entrez.efetch(db="nucleotide", id="NM_000546", rettype="fasta", retmode="text")
record = SeqIO.read(handle, "fasta")
print(record.id, len(record.seq))
print(record.seq[:60])
```
(NM_000546 is a public human gene transcript. Any accession from https://www.ncbi.nlm.nih.gov works.)

### Step 3: Align two sequences
```python
from Bio import Align
aligner = Align.PairwiseAligner()
aligner.mode = "local"
alignment = aligner.align("ACCGGTATC", "GGTAT")[0]
print(alignment)
print("score:", alignment.score)
```
Expected: the region `GGTAT` matches perfectly with score 5.

Change the scoring to see how it affects results:
```python
aligner.match_score = 2
aligner.mismatch_score = -1
aligner.open_gap_score = -2
aligner.extend_gap_score = -0.5
```

### Step 4: k-mers (the trick behind fast similarity)
A **k-mer** is every substring of length k. Similar sequences share many k-mers.
```python
def kmers(s, k=4):
    return {s[i:i+k] for i in range(len(s) - k + 1)}

def jaccard(a, b, k=4):
    A, B = kmers(a, k), kmers(b, k)
    return len(A & B) / len(A | B)

print(jaccard("ACGTACGTGGA", "ACGTACGTGGC"))   # similar -> 0.75
print(jaccard("ACGTACGTGGA", "TTTTCCCCAAAA"))  # different -> 0.0
```

### Step 5: The same trick on "security" strings
Compare two scripts or two sequences of API calls:
```python
a = "CreateFile ReadFile WriteFile RegSetValue CreateProcess"
b = "CreateFile ReadFile WriteFile RegSetValue CreateService"
c = "ConnectSocket Send Recv CloseSocket"
tokens = lambda s: s.split()
def kmer_tokens(t, k=2): return {tuple(t[i:i+k]) for i in range(len(t)-k+1)}
def sim(x, y):
    X, Y = kmer_tokens(tokens(x)), kmer_tokens(tokens(y))
    return len(X & Y) / len(X | Y)
print(sim(a, b), sim(a, c))
```
Variants of the same family score high; unrelated behaviour scores 0. Real tools use hashing tricks (e.g. fuzzy hashes like ssdeep/TLSH) for speed.

## Exercises
1. Reverse-complement a sequence and verify the original comes back after another reverse-complement.
2. Fetch two related sequences and compute their k-mer similarity for k = 3, 5, 8. How does k change the result?
3. Explain in a paragraph how alignment and fuzzy hashing are cousins.

## Checkpoint
- What's the difference between local and global alignment?
- Why do k-mers make large-scale similarity search fast?

## Go deeper
- Biopython tutorial: https://biopython.org/DIST/docs/tutorial/Tutorial.html
- Rosalind (bioinformatics puzzles): https://rosalind.info
- NCBI BLAST: https://blast.ncbi.nlm.nih.gov
- Galaxy (point-and-click bioinformatics): https://usegalaxy.org
