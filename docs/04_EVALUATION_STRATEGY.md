# OmniMind OS - Evaluation Strategy

Evaluation is a core component of the OmniMind OS architecture, ensuring that tasks are completed accurately and securely by dynamically discovered agents.

## 1. Capability Evaluation

Every capability request is first evaluated against the Agent Catalog. The `AgentSelector` scores candidates based on:

- **Base Score:** A predefined metric of the agent's historical accuracy or stated capability.
- **Cost Efficiency:** Prioritizing free or local agents over paid API calls, subject to user preferences.
- **Latency/Availability:** Whether the agent is installed locally or requires remote invocation.

## 2. Output Evaluation (The Evaluation Agent)

OmniMind OS includes a dedicated `EvaluationAgent`. This agent is responsible for scoring the outputs of other agents.

### Heuristic Scoring (MVP)
Currently, the `EvaluationAgent` uses a heuristic-based `basic_score` function located in `src/agents/evaluation/skills.py`. It checks for:
- Minimum output length (substantive response).
- Absence of error keywords.
- Presence of completion keywords (e.g., "success").

### Future State (LLM Evaluation)
In future versions, the `EvaluationAgent` will act as an "LLM-as-a-Judge", passing the original prompt and the output to an advanced model to evaluate based on:
1. **Relevance:** Did it answer the prompt?
2. **Accuracy:** Are the facts correct?
3. **Formatting:** Did it follow the requested output format?

## 3. Execution Timeline

The `ExecutionTimeline` serves as the ultimate auditable evaluation log. By recording every step from Planner to Executor, the timeline allows users to evaluate *why* an agent was selected and *how* it performed, providing full explainability for every OS action.
