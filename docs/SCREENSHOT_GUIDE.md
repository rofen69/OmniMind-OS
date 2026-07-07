# OmniMind OS - Screenshot Guide

This guide lists the critical visual moments that should be captured as screenshots to include in your **Kaggle Writeup** and **Slide Deck**.

---

## Required Screenshots Checklist

### 1. CLI Startup Screen
- **What to show:** The primary CLI options box after launching `python -m src.main`.
- **Filename recommendation:** `01_CLI_Startup.png`
- **Key value:** Shows clean, zero-token deployability options immediately.

### 2. Heuristic Planner Graph
- **What to show:** The `🎯 EXECUTION PLAN` section from the CLI output.
- **Filename recommendation:** `02_Execution_Plan.png`
- **Key value:** Demonstrates intent parsing into capability steps.

### 3. Discovery Candidates Table
- **What to show:** The `TableRenderer` output displaying the grid of candidate agents for the `research` capability.
- **Filename recommendation:** `03_Discovery_Table.png`
- **Key value:** Proves preference-based candidate ranking (cost, license, score).

### 4. Agent Selection Success
- **What to show:** The `⚡ AGENT SELECTION` log with checkmarks (e.g. `research → LocalResearchAgent (score: 1.0, source: Local) ✅`).
- **Filename recommendation:** `04_Agent_Selection.png`
- **Key value:** Confirms successful resolution of capability.

### 5. Execution Timeline Observability
- **What to show:** The `📋 EXECUTION TIMELINE` block.
- **Filename recommendation:** `05_Execution_Timeline.png`
- **Key value:** Shows perfect explainability and auditability.

### 6. Generated Markdown File
- **What to show:** Open `workspace/quantum_computing.md` in VS Code side-by-side with the CLI.
- **Filename recommendation:** `06_Generated_Output.png`
- **Key value:** Proves end-to-end task completion (writing to local disk).

### 7. Web UI Dashboard
- **What to show:** The browser window showing the Flask Web UI homepage with logs.
- **Filename recommendation:** `07_Web_UI_Dashboard.png`
- **Key value:** Demonstrates premium presentation capabilities.

### 8. System Command Layer Output
- **What to show:** The CLI terminal after typing `agents` or `status` to show the administrative layer bypass.
- **Filename recommendation:** `08_System_Command_Layer.png`
- **Key value:** Proves implementation of the deterministic built-in layer.
