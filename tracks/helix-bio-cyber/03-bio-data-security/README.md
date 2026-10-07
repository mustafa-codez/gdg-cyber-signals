# Lab 03: Bio-Data Security and Privacy

**Track:** Helix | **Level:** Beginner to Intermediate | **Time:** ~75 min

## What is it?
**Genomic**, **health** and **neural/brain** (EEG, fMRI) data are among the most sensitive data that exist because they are:
- **Permanent:** you can't reset your DNA like a password.
- **Identifying:** genomes are unique, and even "anonymised" genomic data can sometimes be re-identified (published research has shown surnames can be inferred from genetic markers combined with public genealogy databases).
- **Shared:** your DNA reveals information about your relatives who never consented.
- **Revealing:** may expose health risks, ancestry, and (for neural data) mental states.

Neural data in particular is the subject of emerging **"neurorights"** debates; Chile amended its constitution in 2021 to address brain-data protection.

## Threats
| Threat | Example | Control |
|---|---|---|
| Re-identification | Linking "anonymous" records using age + postcode + rare variants | k-anonymity, aggregation, controlled access |
| Data breach | Stolen genetic-testing database | Encryption, access control, monitoring |
| Insecure pipelines | Samples and results moved over unencrypted channels | TLS, signed workflows, least privilege |
| Secondary use | Data reused beyond consent | Consent management, purpose limitation, audit |
| Supply chain | Poisoned reference data or tools | Checksums, pinned versions |
| Insider misuse | Staff browsing records | Role-based access, audit logs |

## Regulation to know (overview, not legal advice)
- **GDPR** (EU): genetic, biometric and health data are *special category data* with strict rules.
- **HIPAA** (US): protects identifiable health information in covered entities.
- **Egypt Personal Data Protection Law No. 151 of 2020** and similar national laws.
- **Controlled-access repositories** (e.g. dbGaP) exist because genomic data can't simply be public.

## Setup
```bash
pip install pandas
```

## Walkthrough

### Step 1: Pseudonymise identifiers (keyed hashing)
A plain hash of an ID can be reversed by guessing IDs. Use a **keyed** hash (HMAC) with a secret key stored separately.
```python
import hmac, hashlib, os

KEY = os.environ["PSEUDO_KEY"].encode()      # export PSEUDO_KEY="long-random-secret" first

def pseudonymise(patient_id: str) -> str:
    return hmac.new(KEY, patient_id.encode(), hashlib.sha256).hexdigest()[:16]

print(pseudonymise("patient-001"))
```
Pseudonymised data is still **personal data** under many laws, because the key holder can re-link it.

### Step 2: Check k-anonymity on a synthetic dataset
**k-anonymity:** every combination of quasi-identifiers (age, postcode, sex) must appear in at least *k* records, so nobody stands out.
```python
import pandas as pd

df = pd.DataFrame({
    "age":      [34, 34, 35, 35, 61, 29],
    "postcode": ["12345", "12345", "12345", "12345", "99999", "55555"],
    "sex":      ["F", "F", "M", "M", "M", "F"],
    "variant":  ["x", "y", "x", "x", "y", "x"],   # sensitive attribute
})

quasi = ["age", "postcode", "sex"]
sizes = df.groupby(quasi).size().reset_index(name="count")
print(sizes)
print("k =", sizes["count"].min())
risky = sizes[sizes["count"] < 2]
print("Records at risk:\n", risky)
```
Fix risky groups by **generalising** (age → age bands, postcode → first 3 digits) or **suppressing** rows, then re-check.
```python
df["age_band"] = (df["age"] // 10 * 10).astype(str) + "s"
df["postcode3"] = df["postcode"].str[:3]
print(df.groupby(["age_band", "postcode3", "sex"]).size())
```

### Step 3: Integrity of references and tools
```bash
sha256sum reference_genome.fa
# compare with the checksum published by the data provider
```

### Step 4: Pipeline security checklist
- [ ] Data encrypted at rest and in transit
- [ ] Access by role; every access logged
- [ ] Separate identifiers from sequence data
- [ ] Pinned and verified tool versions (containers with digests)
- [ ] Data-retention and deletion policy
- [ ] Documented consent and purpose
- [ ] Incident response plan covering data breach notification

### Step 5: EEG/neural data thought exercise
A consumer headset streams EEG to a cloud app. List: what could be inferred, who could access it, what the retention policy should be, and what "consent" must cover.

## Exercises
1. Increase k for the synthetic table above to at least 2 using generalisation.
2. Write a one-page data-protection plan for a small research lab that stores genomic samples.
3. Compare how GDPR and one other law treat genetic data.

## Checkpoint
- Why isn't pseudonymised data "anonymous"?
- Why is genomic data uniquely hard to protect?

## Go deeper
- GDPR text and ICO/EDPB guidance
- Global Alliance for Genomics and Health (GA4GH) standards and security guidance: https://www.ga4gh.org
- NeuroRights Foundation: https://neurorightsfoundation.org
