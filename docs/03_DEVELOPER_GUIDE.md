# OmniMind OS - Developer Guide

Welcome to the OmniMind OS developer documentation. This guide outlines how to build, extend, and maintain the OS.

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- `pip`

### Local Setup
```bash
git clone <repository-url>
cd OmniMind-OS
pip install -r requirements.txt
python -m src.main
```

## 🏗 Architecture Principles

To maintain system integrity, all developers must adhere to the following principles:

1. **Never bypass the Planner:** All execution must flow through the `Orchestrator` using a `Plan`.
2. **Never call an agent directly from the UI:** Always use the discovery and selection pipeline.
3. **Always register new agents through AgentRegistry:** Do not hardcode agent instantiations in the orchestrator.
4. **Memory must never execute code:** State storage is strictly passive.
5. **Discovery must never auto-install agents:** Installation of remote agents (GitHub, HF) requires explicit permission.
6. **Every new capability must be evaluated:** Provide a scoring heuristic in `evaluation/skills.py`.
7. **Every feature must preserve modularity:** Do not create circular dependencies between `core/`, `discovery/`, and `agents/`.

## 🛠 Adding a New Agent

1. Create a new folder under `src/agents/<domain>/`.
2. Implement `agent.py` extending `BaseAgent`.
3. Implement `skills.py` for isolated domain logic.
4. Register the agent in `src/core/registry.py` under `_register_builtin_agents()`.
5. Add metadata to `src/discovery/resolver.py` so the agent can be discovered.

## 🔧 Adding a New Tool

1. Create `my_tool.py` in `src/tools/`.
2. Register it in `src/core/registry.py` inside the `ToolManager` initialization.
3. Tools can be invoked by returning a capability prefixed with `tool:` (e.g., `tool:git`).

## 🧪 Testing

Currently, testing relies on running the CLI demo:
```bash
python -m src.main
```
Future versions will include a `pytest` suite for unit testing components in isolation.