# Lab 03: AI for Investigators

**Track:** Forge | **Level:** Intermediate | **Time:** ~75 min

## What is it?
Investigators drown in text: press releases, court documents, reports, chat logs. LLMs can **extract and organise** that text into structured notes much faster than reading it all manually. The danger is that models also **invent** details. This lab teaches the safe pattern: use AI to *find and structure leads*, then verify each one against the source.

Use only **public** text (government press releases, published indictments, security-vendor reports). **No private individuals' data.** See `ETHICS.md`.

## Setup
```bash
pip install -U google-genai pydantic
export GEMINI_API_KEY="..."
```
Pick one public law-enforcement press release or published threat report and save its text as `source.txt`.

## Walkthrough

### Step 1: Define the structure you want
```python
from typing import Literal, Optional
from pydantic import BaseModel

class Quote(BaseModel):
    text: str            # EXACT text copied from the source supporting the claim

class Entity(BaseModel):
    name: str
    kind: Literal["person", "organisation", "malware", "domain", "wallet", "location", "other"]
    role: str
    evidence: Quote

class CaseNotes(BaseModel):
    crime_type: str
    summary: str
    entities: list[Entity]
    timeline: list[str]
    laws_mentioned: list[str]
```
Requiring an **exact supporting quote** for every claim is the trick: it makes verification mechanical.

### Step 2: Ask Gemini to extract, and forbid guessing
```python
import os
from google import genai
from google.genai import types

client = genai.Client()
MODEL = os.environ.get("GEMINI_MODEL", "gemini-3-flash-preview")
source = open("source.txt", encoding="utf-8").read()

resp = client.models.generate_content(
    model=MODEL,
    contents="Extract case notes from the document. Use ONLY information in the document. "
             "For each entity, copy an exact supporting quote. If something is not stated, leave it out.\n\n"
             "DOCUMENT:\n" + source,
    config=types.GenerateContentConfig(
        response_mime_type="application/json", response_schema=CaseNotes, temperature=0.0),
)
notes = CaseNotes.model_validate_json(resp.text)
```

### Step 3: Verify every quote exists in the source
```python
import re
norm = lambda s: re.sub(r"\s+", " ", s).strip().lower()
src = norm(source)

for e in notes.entities:
    ok = norm(e.evidence.text) in src
    print(("VERIFIED " if ok else "UNVERIFIED"), e.kind, e.name)
```
Anything `UNVERIFIED` is treated as a hallucination until a human finds it in the source.

### Step 4: Export to a case file
Write the verified items into `templates/case-file.md`'s evidence log, with the source URL, retrieval date (UTC), a hash of `source.txt` and an archive link:
```bash
sha256sum source.txt
```

### Step 5: What AI must not do here
- Don't ask it to identify people from photos.
- Don't ask it to find private information about individuals.
- Don't treat its conclusions as attribution. Attribution needs corroborated evidence.

## Exercises
1. Run the pipeline on two different public documents. How many entities were unverified?
2. Add a field `confidence` and a rule that low-confidence items are listed separately.
3. Compare results at temperature 0 and 1. What changes?

## Mini project: Case-Notes Extractor
**Build:** Run the extractor on a public document and document the verification.

**Deliverables (in your own portfolio repo):** The script, the verified/unverified entity table and a note on how many claims failed verification.

**This is a phase of the track capstone:** see [`../CAPSTONE.md`](../CAPSTONE.md).

**Share it (optional):** "I used Gemini to extract case notes, then checked every quote in code." Follow the safe-sharing rules and templates in [`SHOWCASE.md`](../../../SHOWCASE.md).

## Checkpoint
- Why require exact quotes?
- Why is an AI summary a *lead* and not *evidence*?

## Go deeper
- Structured output: https://ai.google.dev/gemini-api/docs/structured-output
- Pair with Ledger Lab 01 (cybercrime anatomy) and Scout Lab 01 (source grading)
