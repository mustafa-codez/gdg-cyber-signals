# Showcase: Share Your Work on GitHub, LinkedIn and Social Media

Employers and communities notice people who **show their work**. This guide makes it easy, and keeps it **safe**.

## The safe-sharing rules (read first)
1. **Synthetic or public data only.** Say so: "using a synthetic log from the course".
2. **Never post secrets**: API keys, tokens, passwords. Scan before you push (Forge Lab 04).
3. **No personal data** about real people: no private individuals, no real logs from a workplace or university network, no real victims or wallet owners.
4. **No live targets.** Don't post screenshots of real systems you scanned or probed without permission.
5. **No weaponised details.** Explain the idea and the defence; don't publish step-by-step attacks on real services.
6. **Credit your sources**: tools, datasets, and anything AI helped with.
7. **Be honest about confidence.** "I found X with medium confidence" beats overclaiming.
8. Follow `ETHICS.md` and the official GDG brand rules for logos and names.

## GitHub: how to publish a project
1. Create a repo in **your own account**.
2. Use [`templates/student-project-readme.md`](templates/student-project-readme.md).
3. Add a `.gitignore` and check no keys are present:
   ```bash
   printf '.env\n*.key\n.venv/\n__pycache__/\n' >> .gitignore
   ```
4. Commit in small steps with clear messages ("Add Sigma rule for encoded PowerShell").
5. Add a screenshot or GIF of it working (of synthetic data).
6. Add topics: `cybersecurity`, `blue-team`, `gdg`, `build-with-ai`, `gemini`.
7. Pin your best 2 to 3 repos on your profile.

## LinkedIn: how to post
**Post after each phase, not only at the end.** Short and specific beats long and vague.

Structure that works:
1. **Hook** (one line): what you built
2. **What it does** (2 to 3 lines)
3. **What you learned** (2 to 3 bullets)
4. **Link** to the repo
5. **Hashtags** and a thank-you to the chapter

Use [`templates/linkedin-post.md`](templates/linkedin-post.md) for ready-to-edit versions:
- Phase post ("I finished Part 1...")
- Capstone post
- Reflection post ("3 things I learned about logs")

Good hashtags: `#GDG #GoogleDeveloperGroups #BuildWithAI #Gemini #CyberSecurity #BlueTeam #OSINT #Bioinformatics`.

You can also add a project to your LinkedIn profile under **Projects**, and mention it in your **About** and **Featured** sections.

## Other social platforms
- **X / Bluesky / Threads:** a 3 to 5 post thread: problem, approach, result, link.
- **Short video:** a 60-second screen recording of your tool running on synthetic data, with captions.
- **Blog (Medium, dev.to, your own site):** a longer write-up of one lab and what went wrong. Failures teach well.

## Tag and credit
Tag the chapter ([LinkedIn](https://www.linkedin.com/company/gdg-on-campus-aast-abu-qir/), [Instagram](https://www.instagram.com/aast.gdgc/), [Facebook](https://www.facebook.com/GDGAAST/); all links in [`docs/community-aast-abu-qir.md`](docs/community-aast-abu-qir.md)). Mention the tools you used (for example Wazuh, Sigma, Gemini). Don't claim Google or the tool authors endorse your project.

## Presenting at the showcase (week 15)
- 5 minutes: what you built, a live or recorded demo, one lesson learned
- Show the README, not just the code
- Say what you'd improve next

## Checklist before you post
- [ ] Repo runs from a clean clone
- [ ] No secrets or personal data (scan done)
- [ ] README has what, how to run, what I learned, data used, AI help
- [ ] Screenshot uses synthetic data
- [ ] Post is accurate and doesn't overclaim
