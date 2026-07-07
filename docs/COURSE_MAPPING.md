# OmniMind OS - Kaggle Course Concept Mapping

This document provides a direct bridge between the core concepts taught in the Google AI Agent Course and their concrete implementation within the OmniMind OS repository.

---

## 1. Core Architecture Concepts

### Agent System (Multi-Agent Swarm)
- **Concept:** Isolation of specialized agents coordinating together instead of a single monolithic model.
- **Repository Location:** [src/agents/](file:///c:/Users/rofen/Documents/Compare/Repo_B_Antigravity/OmniMind-OS_PRE_ANTIGRAVITY/src/agents/)
- **Details:** Features isolated sub-agents representing different domains (`LocalResearchAgent`, `FileAgent`, `DocumentationAgent`, and `EvaluationAgent`) that interact only via shared memory.

### Planner
- **Concept:** Goal decomposition; breaking natural language prompts into sequential, capability-based execution steps.
- **Repository Location:** [src/core/planner.py](file:///c:/Users/rofen/Documents/Compare/Repo_B_Antigravity/OmniMind-OS_PRE_ANTIGRAVITY/src/core/planner.py)
- **Details:** Uses a deterministic regex-based parser to break user inputs into sequential `Step` objects containing capability tags.

### Agent Registry
- **Concept:** Central directory and interface manager for all loaded agents and tools.
- **Repository Location:** [src/core/registry.py](file:///c:/Users/rofen/Documents/Compare/Repo_B_Antigravity/OmniMind-OS_PRE_ANTIGRAVITY/src/core/registry.py)
- **Details:** Holds active instances of all agents and registers system tools (Git, API).

### Agent Discovery
- **Concept:** Dynamic querying of agents capable of fulfilling a capability, returning candidates across local and remote sources.
- **Repository Location:** [src/discovery/catalog.py](file:///c:/Users/rofen/Documents/Compare/Repo_B_Antigravity/OmniMind-OS_PRE_ANTIGRAVITY/src/discovery/catalog.py) & [src/discovery/resolver.py](file:///c:/Users/rofen/Documents/Compare/Repo_B_Antigravity/OmniMind-OS_PRE_ANTIGRAVITY/src/discovery/resolver.py)
- **Details:** Annotates candidate agents based on installation status and queries capability resolver catalogs.

### Capability Resolution & Selection
- **Concept:** Evaluating agent candidates based on constraints and user preferences (scoring, licensing, cost).
- **Repository Location:** [src/discovery/selector.py](file:///c:/Users/rofen/Documents/Compare/Repo_B_Antigravity/OmniMind-OS_PRE_ANTIGRAVITY/src/discovery/selector.py)
- **Details:** The `AgentSelector` filters discovered candidates based on user preferences and chooses the optimal agent for the current task step.

---

## 2. Advanced Course Concepts

### Memory (Session Isolation)
- **Concept:** Global session state shared across agents to pass context without direct agent-to-agent prompting.
- **Repository Location:** [src/memory/session.py](file:///c:/Users/rofen/Documents/Compare/Repo_B_Antigravity/OmniMind-OS_PRE_ANTIGRAVITY/src/memory/session.py) & [src/memory/memory.py](file:///c:/Users/rofen/Documents/Compare/Repo_B_Antigravity/OmniMind-OS_PRE_ANTIGRAVITY/src/memory/memory.py)
- **Details:** Holds global session keys (`latest_research`, `formatted_doc`) that agents read and write during execution.

### Evaluation
- **Concept:** Scoring output quality post-execution.
- **Repository Location:** [src/agents/evaluation/agent.py](file:///c:/Users/rofen/Documents/Compare/Repo_B_Antigravity/OmniMind-OS_PRE_ANTIGRAVITY/src/agents/evaluation/agent.py) & [skills.py](file:///c:/Users/rofen/Documents/Compare/Repo_B_Antigravity/OmniMind-OS_PRE_ANTIGRAVITY/src/agents/evaluation/skills.py)
- **Details:** Evaluates the generated output length and formatting to assign a basic quality score.

### Security & Guardrails
- **Concept:** Intercepting inputs and enforcing security policies before LLM/Planner interaction.
- **Repository Location:** [src/core/guardrails.py](file:///c:/Users/rofen/Documents/Compare/Repo_B_Antigravity/OmniMind-OS_PRE_ANTIGRAVITY/src/core/guardrails.py) & [src/security/](file:///c:/Users/rofen/Documents/Compare/Repo_B_Antigravity/OmniMind-OS_PRE_ANTIGRAVITY/src/security/)
- **Details:** Enforces character limits (<2000 chars) and emptiness checks on incoming raw user queries. The `src/security/` folder contains structural stubs for future RBAC and advanced policies.

### Model Context Protocol (MCP)
- **Concept:** Standardized client/server architecture for connecting models to external filesystems and database APIs.
- **Repository Location:** [src/mcp/client.py](file:///c:/Users/rofen/Documents/Compare/Repo_B_Antigravity/OmniMind-OS_PRE_ANTIGRAVITY/src/mcp/client.py)
- **Details:** Exposes a structural MCP client stub that connects the tool manager to external protocol parameters.

### Google ADK
- **Concept:** Safe adapter wrappers for ADK-compliant agents.
- **Repository Location:** [src/integrations/adk/adapter.py](file:///c:/Users/rofen/Documents/Compare/Repo_B_Antigravity/OmniMind-OS_PRE_ANTIGRAVITY/src/integrations/adk/adapter.py)
- **Details:** Isolates ADK agent registration using a safe-import `ImportError` fallback so the MVP doesn't break if dependencies are absent.

### Deployability (Zero-Token Execution)
- **Concept:** Instantly executable environments for validation and Portability.
- **Repository Location:** [boot.py](file:///c:/Users/rofen/Documents/Compare/Repo_B_Antigravity/OmniMind-OS_PRE_ANTIGRAVITY/boot.py) & [src/main.py](file:///c:/Users/rofen/Documents/Compare/Repo_B_Antigravity/OmniMind-OS_PRE_ANTIGRAVITY/src/main.py)
- **Details:** Decouples core execution from expensive LLM API tokens, running locally with free Wikipedia lookups and standard Python modules.
