"""
Multiple Scenarios Demo

Demonstrates OmniMind OS with multiple consecutive scenarios and ANSI colors.
"""
import logging
import sys
import io

# Force UTF-8 encoding for Windows terminals
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from src.core.orchestrator import Orchestrator
from src.core.planner import Planner
from src.core.registry import AgentRegistry
from src.ui.table_renderer import TableRenderer

logging.basicConfig(level=logging.WARNING, format='%(levelname)s: %(message)s')


def run_demo(user_input: str) -> None:
    """Run a single demo scenario with ANSI colors."""
    print(f"\n🧠 \033[1mOmniMind OS v1.0 — Agentic Capability-Based AI Operating System\033[0m")
    print(f"\n📥 \033[94mUSER INPUT:\033[0m \"{user_input}\"")

    planner = Planner()
    registry = AgentRegistry()
    orchestrator = Orchestrator(planner, registry)

    result = orchestrator.run(user_input)

    if "error" in result:
        print(f"\n❌ \033[91mERROR:\033[0m {result['error']}")
        return

    print("\n🎯 \033[93mEXECUTION PLAN\033[0m")
    for i, step in enumerate(result.get("plan", []), 1):
        print(f"  Step {i}: [{step['capability']}] → \"{step['task']}\"")

    print("\n🔍 \033[96mAGENT DISCOVERY\033[0m")
    for cap, candidates in result.get("candidate_agents", {}).items():
        print(f"  Capability: {cap}")
        print(TableRenderer.render(f"Candidates for '{cap}'", candidates))

    print("⚡ \033[95mAGENT SELECTION\033[0m")
    for cap, agent in result.get("selected_agents", {}).items():
        print(f"  {cap} → {agent['name']} (score: {agent['score']}, source: {agent['source']}) ✅")

    print("\n📊 \033[92mEXECUTION RESULTS\033[0m")
    for i, res in enumerate(result.get("results", []), 1):
        print(f"  Step {i}: {res}")

    print("\n📋 \033[97mEXECUTION TIMELINE\033[0m")
    for i, tl in enumerate(result.get("timeline", []), 1):
        print(f"  [{i}] {tl['capability']} → {tl['selected_agent']} ({tl['source']}) → {tl['status']} ✅")

    print(f"\n✅ \033[92mExecution complete. {len(result.get('plan', []))} step(s) processed.\033[0m\n")
    print("=" * 80)


def main() -> None:
    scenarios = [
        "research solar cold storage in Bangladesh",
        "find latest advancements in solid-state batteries"
    ]
    
    for scenario in scenarios:
        run_demo(scenario)


if __name__ == "__main__":
    main()
