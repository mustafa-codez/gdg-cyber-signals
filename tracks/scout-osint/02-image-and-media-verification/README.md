# Lab 02: Image and Media Verification

**Track:** Scout | **Level:** Beginner | **Time:** ~60 min

## What is it?
Viral images and videos are often **old, edited, mislabelled or AI-generated**. Verification asks four questions (the "Verification Handbook" approach):

1. **Provenance:** Is this the original? Who first posted it?
2. **Source:** Who is the uploader and can they be trusted?
3. **Date:** When was it captured?
4. **Location:** Where was it captured?

## Setup
```bash
sudo apt install -y libimage-exiftool-perl ffmpeg
pip install pillow
```

## Walkthrough

### Step 1: Reverse image search
Upload or paste the image URL into several engines, because each has different coverage:
- Google Lens: https://lens.google.com
- TinEye: https://tineye.com
- Yandex Images: https://yandex.com/images
- Bing Visual Search: https://www.bing.com/visualsearch

Look for the **earliest** appearance. If an "event from today" image appeared three years ago, it's recycled.

### Step 2: Metadata (EXIF)
```bash
exiftool photo.jpg
exiftool -DateTimeOriginal -Make -Model -GPSLatitude -GPSLongitude photo.jpg
```
Caution: most social platforms **strip** metadata, and metadata can be edited, so treat it as a clue, not proof. No EXIF isn't suspicious by itself.

Python version:
```python
from PIL import Image
from PIL.ExifTags import TAGS

img = Image.open("photo.jpg")
exif = img.getexif()
for tag_id, value in exif.items():
    print(TAGS.get(tag_id, tag_id), ":", value)
```

### Step 3: Video: extract frames and search them
```bash
mkdir -p frames
ffmpeg -i video.mp4 -vf fps=1 frames/f_%03d.png
```
Reverse-search distinctive frames (a sign, a landmark, a face of a public figure at a public event).

### Step 4: Look for manipulation
- Inconsistent shadows, lighting or reflections
- Repeated patterns (cloning), warped straight lines, mismatched noise or resolution
- Odd text on signs (AI images often garble text)
- Error Level Analysis tools (e.g. FotoForensics) can hint at edits, but they give **false positives**. Never rely on one tool.

### Step 5: Check the context
- Search keywords from the claim in the local language.
- Check the uploader's history: when was the account created, what else do they post?
- Compare with other images of the same event from independent sources.

### Step 6: Preserve it
```bash
sha256sum photo.jpg >> hashes.txt
```
Archive the original post URL at https://web.archive.org and https://archive.ph.

### Step 7: Strip your own metadata before sharing
```bash
exiftool -all= -overwrite_original photo_to_share.jpg
```

## Exercises
1. Pick a viral image from a public fact-check site and reproduce the fact-checker's steps *before* reading their conclusion.
2. Find a photo you took, read its EXIF, then strip it and compare.
3. Complete `templates/osint-collection-log.md` for one verification.

## Checkpoint
- Why is a missing EXIF block not proof of fakery?
- Which verification question can reverse image search answer best?

## Go deeper
- Verification Handbook: https://verificationhandbook.com
- First Draft / Bellingcat guides (see `RESOURCES.md`)
- InVID-WeVerify browser plugin (video verification toolkit)
