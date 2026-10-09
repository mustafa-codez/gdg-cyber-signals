# Lab 04: Deepfake Verification

**Track:** Scout | **Level:** Intermediate | **Time:** ~75 min

## What is it?
A **deepfake** is synthetic or manipulated media created by AI: a face swap, a cloned voice, a fully generated image or video. They're used in fraud (fake CEO voice calls, fake investment endorsements), disinformation and harassment.

**The honest truth:** automated "deepfake detectors" are unreliable and become outdated quickly. Strong verification combines **context, provenance and multiple checks**, not a single detector score.

## The verification stack
1. **Context and provenance first:** Who posted it first? Is there an original recording? Do trusted outlets or the person's official channels carry it?
2. **Provenance technology:**
   - **C2PA / Content Credentials** (https://c2pa.org): cryptographically signed metadata that records how media was created and edited.
   - **Invisible watermarks** (e.g. Google's SynthID) can mark AI-generated content from supporting tools.
   Absence of credentials proves nothing; presence from a trusted signer is a strong signal.
3. **Visual and audio artefacts** (weak signals, improving constantly):
   - Mouth and teeth that blur, ear/hair edges that shimmer, inconsistent blinking, odd hands
   - Lighting that doesn't match the scene, reflections that don't match
   - Voice that lacks natural breaths, background noise that is too clean or loops
4. **Behavioural red flags** (most useful in fraud): urgency, secrecy, unusual payment requests, new phone number. **Verify through a second channel.**
5. **Technical checks:** metadata, frame-by-frame review, reverse image search of frames.

## Setup
```bash
sudo apt install -y ffmpeg exiftool
pip install c2pa-python    # optional: reads Content Credentials
```

## Walkthrough

### Step 1: Break the video into frames
```bash
mkdir -p frames
ffmpeg -i suspect.mp4 -vf "fps=5" frames/f_%04d.png
```
Inspect frames where the face turns or is partly covered by a hand, since artefacts often appear there.

### Step 2: Look at the audio waveform
```bash
ffmpeg -i suspect.mp4 -vn -acodec pcm_s16le -ar 16000 audio.wav
```
Open `audio.wav` in Audacity and view the spectrogram. Cloned audio sometimes shows unnatural cut-offs above certain frequencies or perfectly smooth noise floors. Treat as a clue only.

### Step 3: Check metadata
```bash
exiftool suspect.mp4
```
Note the encoder, creation date and tool. Many social platforms re-encode and strip data.

### Step 4: Check for Content Credentials
Upload to a Content Credentials verification site (search "Content Credentials verify" via https://contentcredentials.org) or use the c2pa tooling, and read the "manifest".

### Step 5: The "second channel" rule
For any urgent request (voice note, video message from an executive, family member in trouble):
1. Hang up.
2. Call back on a number you already know.
3. Use a pre-agreed **family/team code word** for emergencies.

### Step 6: Write the verdict
Use confidence language: "No evidence of manipulation found, provenance not established," or "Multiple indicators of synthetic generation, original source not found."

## Policy angle (discussion questions)
- Should AI-generated content be labelled by law? By platforms?
- Who is liable when a deepfake commits fraud: creator, platform, tool provider?
- How do provenance standards deal with privacy for journalists and activists?

## Exercises
1. Find three public examples of debunked deepfakes. What clue exposed each?
2. Create a one-page "How to verify a suspicious video" guide for your family.
3. Run the verification stack on an AI-generated image from a free image generator and document what each step shows.

## Mini project: Deepfake Verification Guide
**Build:** Write a short guide others can follow.

**Deliverables (in your own portfolio repo):** A one-page guide (PDF or Markdown) with the verification stack and the second-channel rule.

**This is a phase of the track capstone:** see [`../CAPSTONE.md`](../CAPSTONE.md).

**Share it (optional):** "I made a one-page guide on how to check suspicious videos." Follow the safe-sharing rules and templates in [`SHOWCASE.md`](../../../SHOWCASE.md).

## Checkpoint
- Why isn't a detector score enough?
- Why does the second-channel rule beat technical detection for fraud?

## Go deeper
- C2PA: https://c2pa.org
- Witness (human-rights video verification): https://www.witness.org
- Aegis track, Lab 04 for AI red-teaming
