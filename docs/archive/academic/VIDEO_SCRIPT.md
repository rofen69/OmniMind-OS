# OmniMind OS - Demo Video Script & Direction

**Goal:** A tight, energetic video (2 to 3 minutes max). Do not read slides. Show action.
**Vibe:** Professional, confident, and focused on engineering architecture.

---

## Part 1: The Hook & The Problem (0:00 - 0:30)
**On Screen:** Your face (briefly) or a title slide with the OmniMind OS logo/name.
**Audio:** "Hi, I'm [Your Name]. For this capstone, I realized that building just another 'chat-with-a-pdf' bot wasn't going to cut it. The real challenge in Agentic AI is orchestration—how do we coordinate multiple, modular agents securely and transparently?"
**On Screen:** Switch to the `docs/02_SYSTEM_ARCHITECTURE.md` showing the Mermaid diagram.
**Audio:** "So I built OmniMind OS. It's a Capability-Based AI Operating System. It separates planning, discovery, and execution into strict layers."

## Part 2: The WOW Factor - Zero-Token Execution (0:30 - 1:30)
**On Screen:** Open your terminal window. Keep the text large and readable.
**Audio:** "The WOW factor of this MVP is deployability. I built a 'Zero-Token, Zero-Auth' architecture. You don't need to configure OpenAI or Gemini API keys to test my multi-agent system. It works out-of-the-box using heuristic planning and free, open APIs."
**Action:** Type `python -m src.main` and hit Enter. 
**Audio:** "Watch this. The user asks: *'Research Quantum Computing and format it as a document then save the file.'*"
**Action:** Let the terminal output run. Highlight the sections with your mouse as you speak.
**Audio:** "Notice the OS dynamically builds a 3-step execution plan. Then, the Discovery Engine kicks in. It searches the Registry, evaluates candidate agents based on score and cost, and routes the tasks."

## Part 3: Memory & Isolation (1:30 - 2:15)
**On Screen:** Show the terminal output where the Timeline is printed.
**Audio:** "Here's the magic. The Core OS doesn't know what Wikipedia is. It doesn't know how to write to a hard drive. It just orchestrates."
**Action:** Open VS Code. Briefly show `src/memory/session.py` and `src/agents/research/skills.py`.
**Audio:** "The Research Sub-Agent queries the real Wikipedia API and saves the data to the OS's Shared Memory. The Documentation Agent formats it. The File Agent writes it to disk. Strict architectural isolation."
**Action:** Open your file explorer or VS Code sidebar. Open the `workspace/` folder and show the `research_quantum_computing_and.md` file that was just created!
**Audio:** "And here is the proof. Real data, formatted and saved locally, across three cooperating agents."

## Part 4: The Future & My Journey (2:15 - 3:00)
**On Screen:** Show the `docs/05_SECURITY_GUARDRAILS.md` or `docs/DEVELOPMENT_STORY.md` file.
**Audio:** "Because of this modularity, OmniMind OS natively supports Security Guardrails, pre-execution validation, and is perfectly positioned to integrate Model Context Protocol (MCP) in Version 2. 

But more than the code, this Capstone represents my personal shift from writing every line of code manually to acting as the architect and manager of an AI agent team. I've been in apps and game development since 2013, but I've never completed a desktop application of this scale. Previously I tried AI code generators, but they often led me into unproductive loops. This course changed my workflow. Instead of treating AI as a replacement developer, I learned to use it as a team of specialized agents while remaining responsible for architecture, validation, and engineering decisions. OmniMind OS is both my capstone project and my first complete experience with AI-driven software engineering. Thank you!"

---

## 🎬 Director's Notes for Recording:
1. **Clean your desktop:** Hide unnecessary icons. Make sure your terminal font is bumped up to at least 16pt so judges can read it on laptops.
2. **Practice the timing:** If the Wikipedia API takes 2 seconds to load, use that time to explain what the Discovery Engine is doing.
3. **Be enthusiastic:** When you show the Markdown file actually appearing in the `workspace/` folder, let your excitement show. That is the moment the "Zero-Token" promise pays off.
