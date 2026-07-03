from src.core.orchestrator import Orchestrator
from src.core.planner import Planner
from src.core.registry import AgentRegistry


def main():
    print("🚀 OmniMind OS Starting...")

    planner = Planner()
    registry = AgentRegistry()

    orchestrator = Orchestrator(
        planner=planner,
        registry=registry,
    )

    user_input = "research solar cold storage in Bangladesh"

    result = orchestrator.run(user_input)

    print("\n📦 Final Output:\n")
    print(result)


if __name__ == "__main__":
    main()