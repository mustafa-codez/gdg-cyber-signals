# Lab 04: Build Safely with AI

**Track:** Forge | **Level:** Beginner to Intermediate | **Time:** ~60 min

## What is it?
AI coding assistants (Gemini in your editor, Gemini CLI, chat tools) speed up building, and speed up mistakes. This lab is the safety checklist for using AI to write code, and for putting AI inside your own tools.

## Risks and fixes
| Risk | Example | Fix |
|---|---|---|
| **Secret leakage** | Pasting an API key or customer log into a chat | Never paste secrets; use env vars; use fake data |
| **Committed keys** | `GEMINI_API_KEY` ends up on GitHub | `.gitignore` + secret scanning |
| **Hallucinated packages** | AI suggests a library that doesn't exist; an attacker registers that name ("slopsquatting") | Check every dependency on the official registry before installing |
| **Insecure code** | SQL built by string concatenation, `eval`, weak crypto | Review and test; run security linters |
| **Over-trust** | Shipping code you don't understand | Read it, run it, test it |
| **Prompt injection in your own app** | User text hijacks your Gemini calls | See Aegis labs; validate outputs in code |
| **Data protection** | Sending personal data to a third party | Minimise, anonymise, check terms and policy |

## Setup
```bash
pip install bandit pip-audit pytest
# secret scanner (pick one)
pip install detect-secrets
# or install gitleaks: https://github.com/gitleaks/gitleaks
```

## Walkthrough

### Step 1: Keep secrets out of git
```bash
printf '.env\n*.key\n__pycache__/\n.venv/\n' >> .gitignore
python3 -m detect_secrets scan > .secrets.baseline     # scan the repo
```
With gitleaks:
```bash
gitleaks detect --source . -v
```
If a real key was ever committed, **revoke it**. Deleting the file isn't enough, because git history keeps it.

### Step 2: Verify dependencies before installing
AI said `pip install fastsecurity-utils`? Check first:
```bash
pip index versions fastsecurity-utils      # does it exist? who maintains it?
```
Then open the package's page on https://pypi.org, check the maintainer, release history, linked source repo and download counts. New, tiny, unknown packages with plausible names are suspicious.

Audit what you already use:
```bash
pip-audit
```

### Step 3: Review AI-written code with a linter
Ask an assistant for "a Flask endpoint that searches users by name", save it as `app.py`, then:
```bash
bandit -r app.py
```
Typical findings: SQL injection from string formatting, `debug=True`, `subprocess` with `shell=True`. Fix by hand using parameterised queries:
```python
# BAD (injection)
cur.execute(f"SELECT * FROM users WHERE name = '{name}'")
# GOOD
cur.execute("SELECT * FROM users WHERE name = ?", (name,))
```

### Step 4: Test it
```python
# test_app.py
def test_rejects_injection():
    result = search_users("x' OR '1'='1")
    assert result == []
```
```bash
pytest -q
```

### Step 5: Gemini CLI (optional)
Google's open-source terminal agent: https://github.com/google-gemini/gemini-cli. If you use any coding agent:
- Run it in a project folder with **no secrets** inside.
- Read every command before approving it.
- Use version control so you can undo changes.

### Step 6: A "definition of done" for AI-assisted tools
- [ ] I understand every line I ship
- [ ] Dependencies verified and audited
- [ ] No secrets in code or history
- [ ] Inputs validated; model outputs validated in code
- [ ] Risky actions need human approval
- [ ] Tested, including malicious inputs
- [ ] README states what data goes to the AI service

## Exercises
1. Intentionally commit a fake key (`AKIA...` style dummy string) to a test repo and watch the scanner catch it.
2. Ask an AI assistant for a package recommendation, then verify each name on PyPI.
3. Run `bandit` on the Forge Lab 02 and Lab 03 code. Fix anything it flags.

## Mini project: Safe-Build Checklist
**Build:** Apply the checklist to one of your own projects.

**Deliverables (in your own portfolio repo):** A repo with `.gitignore`, a secret scan result, a dependency audit and a README listing data sent to AI services.

**This is a phase of the track capstone:** see [`../CAPSTONE.md`](../CAPSTONE.md).

**Share it (optional):** "I audited my AI project for leaked keys and risky dependencies." Follow the safe-sharing rules and templates in [`SHOWCASE.md`](../../../SHOWCASE.md).

## Checkpoint
- Why is deleting a leaked key from the repo not enough?
- What's "slopsquatting"?

## Go deeper
- OWASP Top 10 for LLM Applications (LLM03 supply chain, LLM05 output handling): see Aegis Lab 01
- Google Secure AI Framework: https://saif.google
