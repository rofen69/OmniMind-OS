from src.core.orchestrator import Orchestrator
from src.core.planner import Planner
from src.core.registry import AgentRegistry
from src.ui.table_renderer import TableRenderer


def run_demo():
    print("🚀 OmniMind OS (Capstone Demo Mode)")

    planner = Planner()
    registry = AgentRegistry()
    orchestrator = Orchestrator(planner, registry)

    user_input = "research solar cold storage in Bangladesh"

    result = orchestrator.run(user_input)

    print("\n📦 EXECUTION TRACE:\n")

    print(result)
    print(TableRenderer.render("CANDIDATE AGENTS", 
    result["candidate_agents"]["research"]
))


if __name__ == "__main__":
    run_demo()