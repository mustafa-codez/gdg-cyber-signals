# Lab 01: Gemini Quickstart

**Track:** Forge | **Level:** Beginner | **Time:** ~45 min

## What is it?
**Gemini** is Google's family of AI models. You can use it three ways:
- **Gemini app / AI Studio:** chat in the browser (https://aistudio.google.com) to experiment with prompts.
- **Gemini API:** call the model from your own code (this lab).
- **Vertex AI:** the enterprise version on Google Cloud, with more controls (https://cloud.google.com/vertex-ai).

An **API key** identifies your project to Google. Treat it like a password.

Model names and free-tier limits **change often**. Always check the current list: https://ai.google.dev/gemini-api/docs/models

## Setup
1. Create a key in Google AI Studio: https://aistudio.google.com/apikey
2. Install the SDK (Python 3.9+):
```bash
pip install -U google-genai
```
3. Store the key in an environment variable, never in code:
```bash
# macOS / Linux
export GEMINI_API_KEY="paste-your-key"
# Windows PowerShell
$env:GEMINI_API_KEY="paste-your-key"
```
No install? Use Google Colab: https://colab.research.google.com (add the key via the "Secrets" tab).

## Walkthrough

### Step 1: Hello, Gemini
```python
from google import genai

client = genai.Client()     # reads GEMINI_API_KEY from the environment

MODEL = "gemini-3-flash-preview"   # check the models page; names change

resp = client.models.generate_content(
    model=MODEL,
    contents="Explain what a SIEM is in two sentences for a beginner.",
)
print(resp.text)
```

### Step 2: System instructions (give it a role and rules)
```python
from google.genai import types

resp = client.models.generate_content(
    model=MODEL,
    contents="What does 'Failed password for invalid user admin' mean?",
    config=types.GenerateContentConfig(
        system_instruction="You are a SOC mentor. Answer in 3 bullets. Say 'I'm not sure' if unsure.",
        temperature=0.2,
    ),
)
print(resp.text)
```
Lower `temperature` = more consistent answers, which is useful for analysis tasks.

### Step 3: Multi-turn chat
```python
chat = client.chats.create(model=MODEL)
print(chat.send_message("Explain MITRE ATT&CK in one paragraph.").text)
print(chat.send_message("Now give me 3 example techniques.").text)
```

### Step 4: Handle errors and limits
Free tiers have **rate limits**. Wrap calls and retry politely:
```python
import time
def ask(prompt, retries=3):
    for i in range(retries):
        try:
            return client.models.generate_content(model=MODEL, contents=prompt).text
        except Exception as e:
            print("error:", e)
            time.sleep(2 ** i)
    return None
```
Limits and pricing: https://ai.google.dev/gemini-api/docs/rate-limits

### Step 5: Protect your key
- Never commit it. Add `.env` to `.gitignore`.
- If a key leaks, **delete it in AI Studio immediately** and create a new one.
- Scan your repo before pushing (Lab 04).

## Exercises
1. Ask the same question at temperature 0 and 1.5. Compare.
2. Write a system instruction that makes Gemini act as a "phishing email explainer" and test it on a harmless sample.
3. Try a prompt-injection attempt against your own system instruction (see Aegis Lab 02). Did it hold?

## Mini project: Gemini Starter Toolkit
**Build:** Build a tiny CLI that asks Gemini a security question with a chosen role.

**Deliverables (in your own portfolio repo):** `ask.py` reading the key from an environment variable, an error-handling retry, and a README (no key in the repo).

**This is a phase of the track capstone:** see [`../CAPSTONE.md`](../CAPSTONE.md).

**Share it (optional):** "I made my first Gemini-powered security helper." Follow the safe-sharing rules and templates in [`SHOWCASE.md`](../../../SHOWCASE.md).

## Checkpoint
- Why store the key in an environment variable?
- What does a system instruction do, and why is it not a security boundary?

## Go deeper
- Docs: https://ai.google.dev/gemini-api/docs
- Quickstart: https://ai.google.dev/gemini-api/docs/quickstart
- Cookbook (examples): https://github.com/google-gemini/cookbook
