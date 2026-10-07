# Lab 03: Digital Forensics Basics

**Track:** Ledger | **Level:** Intermediate | **Time:** ~90 min

## What is it?
**Digital forensics** is the science of collecting, preserving and analysing digital evidence so it can be trusted, including in court. Three principles:

1. **Preserve**: never work on the original; work on a verified copy (a *forensic image*).
2. **Verify**: use **cryptographic hashes** (SHA-256) to prove a copy equals the original.
3. **Document**: keep a **chain of custody**, a log of who handled the evidence, when, and why.

Useful facts:
- **Deleting a file usually removes only its directory entry.** The data often remains until overwritten.
- **Metadata** (timestamps, EXIF, document properties) can tell a story the content doesn't.
- **Volatile data** (RAM) disappears at power-off, so it is collected first in live response.

## Setup (Linux or WSL2)
```bash
sudo apt update
sudo apt install -y sleuthkit libimage-exiftool-perl dosfstools binutils
```
Tools: **The Sleuth Kit** (`fls`, `icat`, `istat`), **exiftool**, `sha256sum`, `strings`. Bigger suites worth knowing: Autopsy (GUI built on Sleuth Kit), Volatility 3 (memory forensics), Eric Zimmerman's Windows tools (see `RESOURCES.md`).

## Walkthrough

### Step 1: Hashing = integrity
```bash
echo "evidence v1" > note.txt
sha256sum note.txt            # record this value
echo "evidence v2" > note.txt
sha256sum note.txt            # completely different hash
```
Change one character and the hash changes completely. This is how you prove nothing was altered.

### Step 2: Build a practice disk image and "delete" a file
```bash
dd if=/dev/zero of=practice.img bs=1M count=20
mkfs.vfat practice.img
mkdir -p mnt
sudo mount -o loop practice.img mnt
echo "secret meeting notes: transfer at 14:00" | sudo tee mnt/notes.txt
sudo cp /bin/ls mnt/tool.bin
sudo rm mnt/notes.txt
sudo umount mnt
sha256sum practice.img | tee practice.img.sha256     # hash BEFORE analysing
```

### Step 3: List files, including deleted ones
```bash
fls -r practice.img          # normal listing
fls -r -d practice.img       # only deleted entries
```
Output looks like `r/r * 5: notes.txt`. The `*` marks a deleted entry and `5` is the **inode/entry number**.

### Step 4: Recover it
```bash
icat practice.img 5 > recovered_notes.txt
cat recovered_notes.txt
```
(Use the number you saw in your own `fls` output.)

### Step 5: Metadata and strings
```bash
istat practice.img 5                   # timestamps and details
strings -n 8 practice.img | head       # human-readable text hidden in the image
exiftool some_photo.jpg                # metadata of any file you have
exiftool -gps:all some_photo.jpg       # location tags, if present
```

### Step 6: Verify nothing changed
```bash
sha256sum -c practice.img.sha256
```
It must say `OK`. If analysis changed the image, the case is compromised.

### Step 7: Chain of custody
Create `chain_of_custody.csv`:
```
item,description,sha256,collected_by,collected_utc,location,transferred_to,transferred_utc
E001,practice.img,<hash>,analyst1,2026-01-15T10:00Z,lab,analyst2,2026-01-15T11:00Z
```

## Windows pointers (no hands-on here, study these)
Registry hives, Prefetch, Amcache, Event Logs (`.evtx`), browser history and `$MFT` are rich forensic artefacts. Eric Zimmerman's free tools parse them.

## Exercises
1. Delete a *second* file, recover both, and list their timestamps.
2. Write a one-page forensic summary: what you found, how, with hash evidence.
3. Explain why powering off a suspect's running laptop may destroy evidence.

## Checkpoint
- What does a matching SHA-256 prove?
- Why work on a copy and not the original?
- What is the order of volatility?

## Go deeper
- Autopsy: https://www.autopsy.com
- Volatility 3: https://github.com/volatilityfoundation/volatility3
- SANS DFIR resources: https://www.sans.org/digital-forensics-incident-response/
- Practice: CyberDefenders DFIR challenges, TryHackMe DFIR rooms, Digital Corpora sample images
