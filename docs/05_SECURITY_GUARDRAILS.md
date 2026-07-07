# OmniMind OS - Security & Guardrails

Security is integrated at the very first layer of OmniMind OS. Before the Planner ever processes a request, it passes through the `Guardrails` module.

## 1. Input Validation

The `Guardrails` class (`src/core/guardrails.py`) currently enforces:
- **Length limits:** Preventing massive context-window attacks (e.g., rejecting inputs > 2000 characters).
- **Emptiness checks:** Rejecting empty or whitespace-only inputs.

## 2. Architecture Security

- **No Auto-Execution of Code:** The Planner only generates declarative `Plan` objects. It does not execute generated code directly.
- **Sandboxed Agent Invocation:** Agents are isolated objects. They interact with the OS only through their `execute()` method and shared memory, preventing rogue agents from modifying the orchestrator.
- **Safe Fallback:** If an MCP tool or external agent fails to load, the system degrades gracefully using local stubs (e.g., the ADK Adapter's safe-import pattern).

## 3. Future Security Capabilities

Future versions of OmniMind OS will introduce:
- **Human-in-the-Loop (HITL):** Requiring explicit user approval before executing destructive actions (e.g., `git push`, file deletion).
- **Prompt Sanitization:** Stripping known prompt-injection attack vectors before passing requests to LLM agents.
- **Role-Based Access Control (RBAC):** Defining what tools an agent is permitted to invoke via the `permissions.py` module.
