# Why an LLM Security Track?

> **In one line:** students are going to build with Gemini and other AI models anyway. They should know how those apps break, and how to defend them, before they ship one.

LLM security is a **spotlight** in this chapter, not the main course. The main course is core cybersecurity (blue team). LLM security earns its place because it is **core security applied to a new kind of system**.

## 1. AI is in everything now
Chatbots, coding assistants, search, support desks and "agents" that can send emails or touch files. A GDG chapter that teaches "Build with AI" is teaching people to put models into products. Security has to come with that.

## 2. It is a genuinely new attack surface
A normal program separates **code** from **data**. A language model reads instructions and data in the **same text channel**, so text it reads can steer it. That is why **prompt injection** sits at the top of the OWASP Top 10 for LLM Applications. Related risks include sensitive-data leaks, poisoned documents in retrieval systems, and agents with too much power.

## 3. It is blue-team work, not just "tricking chatbots"
Defending an AI app uses the same skills as the rest of this chapter:
| Core cyber skill | How it applies to an LLM app |
|---|---|
| Logging and monitoring | Log prompts and tool calls, alert on odd patterns |
| Detection engineering | Rules for injection attempts and data-exfiltration patterns |
| Least privilege | Give the model's tools the minimum permissions |
| Input and output validation | Treat model output as untrusted before using it |
| Incident response | What do you do when the bot leaks something? |

## 4. It matches the Google ecosystem
GDG members meet Gemini and Google's AI tools constantly. Google publishes the Secure AI Framework (SAIF), and the "Build with AI" series stresses building *safe and secure* solutions. This track is the security half of that message.

## 5. It is a skill with real portfolio value
Students can show an LLM app they built, a documented attack against a practice target, and the fix they applied. That is a stronger story than a certificate list.

## What this track is NOT
- Not about producing harmful content or breaking safety rules for fun
- Not about attacking other people's AI products
- Not a replacement for core security skills

All practice happens on provided targets (such as Gandalf) or apps students own. See `ETHICS.md`.

## What students get
- The OWASP LLM Top 10 as a working map
- A hands-on feel for prompt injection and why filters alone fail
- A defence-in-depth checklist for AI apps
- A mini project after each lab and a capstone: **Break and Harden an LLM App**

## Spotlight session: "Gandalf Live" (semester 1, week 6, a light pre-exam week)
This session is a teaser. The full Aegis track is taught live in **semester 2**.

**Length:** 60 minutes | **Setup:** none (browser only) | **Nothing due**

| Min | Block | What happens |
|---|---|---|
| 0-10 | Story hook | A support bot that was tricked into leaking an internal note (a hypothetical case) |
| 10-25 | Core idea | Instructions and data share one channel; direct vs indirect injection |
| 25-45 | Play together | Everyone plays Gandalf (https://gandalf.lakera.ai) in the browser; the host shares how each level's defence changed the attack |
| 45-55 | Map it | Match what you saw to the OWASP LLM Top 10 |
| 55-60 | Wrap | What defence-in-depth would have stopped it |

**Take-home (optional, after exams):** [Aegis 01](../tracks/aegis-llm-security/01-owasp-llm-top10) and [Aegis 02](../tracks/aegis-llm-security/02-prompt-injection).

## Where to go next
- Track: [`tracks/aegis-llm-security`](../tracks/aegis-llm-security)
- Capstone: [`tracks/aegis-llm-security/CAPSTONE.md`](../tracks/aegis-llm-security/CAPSTONE.md)
- Builder side: [`tracks/build-with-ai`](../tracks/build-with-ai)
