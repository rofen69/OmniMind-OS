# OmniMind OS - Zero-Token Architecture

## The Design Philosophy

OmniMind OS is designed as a modular **Agentic Operating System**. While most AI agents rely on single, monolithic LLM calls (e.g., passing a prompt directly to OpenAI or Gemini), OmniMind OS demonstrates true orchestration by separating **planning**, **discovery**, and **execution**.

To guarantee that judges and users can run the system immediately—without providing API keys, entering billing info, or signing up for services—the MVP release implements a **Zero-Token, Zero-Auth** architecture. 

## How It Works Without an LLM

### 1. Heuristic Planner (`src/core/planner.py`)
Instead of an LLM generating JSON plans, the OS uses a deterministic natural language processor. It scans the user's prompt for action verbs. 
- "research", "find" → Adds a `research` step.
- "format", "document" → Adds a `documentation` step.
- "save", "write" → Adds a `file` step.

This allows complex prompts (e.g., *"Research Quantum Computing and format it as a document then save the file"*) to dynamically generate multi-step capability plans without costing any API tokens.

### 2. Functional Sub-Agents
Agents execute tasks using free, publicly available resources:
- **ResearchAgent:** Queries the public Wikipedia API (`api.php`) via HTTP requests. No API key required.
- **DocumentationAgent:** Applies structural formatting to raw text via string manipulation.
- **FileAgent:** Interfaces directly with the local operating system to save outputs to a `workspace/` directory.

### 3. Inter-Agent Memory (`src/memory/session.py`)
Because the agents are fully decoupled, they do not pass data to each other directly. Instead, they read and write to the OS's shared `global_session` memory.
- `ResearchAgent` saves its findings to `memory.get("latest_research")`.
- `DocumentationAgent` formats `latest_research` and saves to `memory.get("formatted_doc")`.
- `FileAgent` reads `formatted_doc` and commits it to disk.

This proves that OmniMind OS can coordinate a swarm of specialized sub-agents to complete complex tasks, maintaining a pure, pristine Core OS that is completely decoupled from domain logic.
