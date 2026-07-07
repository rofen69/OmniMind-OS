"""
Main Application Entry Point

Demonstrates the OmniMind OS capabilities via CLI.
"""
import logging
import sys
import io
import time

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

from src.core.orchestrator import Orchestrator
from src.core.planner import Planner
from src.core.registry import AgentRegistry
from src.ui.table_renderer import TableRenderer

# Configure logging for the demo
logging.basicConfig(level=logging.WARNING, format='%(levelname)s: %(message)s')


def interactive_selection_callback(capability, candidates, default_chosen):
    """Callback to allow user to pick an agent interactively."""
    print(f"\n🔍 AGENT DISCOVERY")
    print(f"  Capability: {capability}")
    candidates_dicts = [
        {
            "#": idx + 1,
            "name": a.name,
            "source": a.source,
            "installed": getattr(a, "installed", False),
            "cost": a.cost,
            "license": a.license,
            "score": a.score,
            "limitations": a.limitations,
            "requirements": a.requirements,
        }
        for idx, a in enumerate(candidates)
    ]
    print(TableRenderer.render(f"Candidates for '{capability}'", candidates_dicts))
    
    print(f"\n  [Auto-select would choose: {default_chosen.name}]")
    choice = input(f"  Enter agent number to select (or press Enter for Auto-select): ").strip()
    
    if not choice:
        return default_chosen
        
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(candidates):
            return candidates[idx]
            
    print(f"  ⚠️ Invalid selection '{choice}'. Falling back to auto-select.")
    return default_chosen


def run_demo() -> None:
    """
    Run the primary demo scenario for OmniMind OS.
    Does not use ANSI colors for broader terminal compatibility.
    """
    print(f"\n" + "="*75)
    print(f"🧠 OmniMind OS v1.0 — Agentic Capability-Based AI Operating System")
    print("="*75)
    
    print("\n🌐 LAUNCH OPTIONS:")
    print("  [1] Launch Premium Web Interface (Recommended - Auto-installs dependencies)")
    print("  [2] Continue in Terminal CLI")
    
    while True:
        choice = input("\n>> Select interface [1-2]: ").strip()
        if choice == "1":
            print("\n🚀 Transferring control to Bootstrapper...")
            import boot
            boot.install_requirements()
            success = boot.launch_web_ui()
            if success:
                return
            else:
                print("\n💻 Gracefully falling back to the Terminal CLI...\n")
                break
        elif choice == "2":
            break
        elif choice.lower() in ['exit', 'quit']:
            print("Goodbye!")
            return
        else:
            print("⚠️ Invalid choice. Please enter 1 or 2.")
    
    print("\n" + "="*75)
    print("Welcome to OmniMind OS! This system dynamically routes tasks to AI agents.")
    print("-" * 75 + "\n")
    
    # Give VS Code / Windows terminals a moment to render the startup text
    # before we allow rapid-pasting, preventing visual overwrite glitches.
    time.sleep(0.5)

    planner = Planner()
    registry = AgentRegistry()
    orchestrator = Orchestrator(planner, registry)

    while True:
        try:
            sys.stdout.flush()
            time.sleep(0.05)
            
            # Drain keyboard buffer on Windows to prevent paste-interweaving
            if sys.platform == 'win32':
                import msvcrt
                while msvcrt.kbhit():
                    msvcrt.getwch()
            
            print("\n📝 [TASK INPUT BOX]")
            user_input = input(">> Enter your task: ").strip()
            if not user_input:
                continue

            user_input_lower = user_input.lower()
            if user_input_lower in ['help', 'agents', 'status', 'version', 'exit', 'quit']:
                if user_input_lower in ['exit', 'quit']:
                    print("Goodbye!")
                    break
                elif user_input_lower == 'help':
                    print("\n=== OmniMind OS Help ===")
                    print("Available System Commands:")
                    print("  help         - Display this help message")
                    print("  agents       - List all built-in and discovered agents")
                    print("  status       - Check the operational status of the OS core")
                    print("  version      - View current OmniMind OS version")
                    print("  exit / quit  - Exit the program")
                    print("\nOtherwise, enter any natural language task for multi-agent execution.")
                    continue
                elif user_input_lower == 'version':
                    print("\nOmniMind OS v1.0 (Zero-Token MVP Release)")
                    continue
                elif user_input_lower == 'status':
                    print("\n=== System Status ===")
                    print(f"  OS Core:       ONLINE")
                    print(f"  Planner:       ONLINE (Heuristic Engine)")
                    print(f"  Registry:      ONLINE ({len(registry._agents)} agents registered)")
                    print(f"  Memory Bus:    ONLINE (Global Session Storage)")
                    continue
                elif user_input_lower == 'agents':
                    print("\n=== Registered Agents ===")
                    agents_list = []
                    for name, agent in registry._agents.items():
                        meta = None
                        for cap, metas in registry.agent_catalog.resolver.catalog.items():
                            for m in metas:
                                if m.name == name:
                                    meta = m
                                    break
                            if meta:
                                break
                        agents_list.append({
                            "name": name,
                            "source": meta.source if meta else "Local",
                            "score": meta.score if meta else 1.0,
                            "cost": meta.cost if meta else "Free",
                            "license": meta.license if meta else "Internal"
                        })
                    print(TableRenderer.render("Installed Registry Agents", agents_list))
                    continue

            print(f"\n📥 USER INPUT: \"{user_input}\"")

            # Check for bypass keywords
            bypass_interaction = "free" in user_input.lower() or "local" in user_input.lower()
            
            if bypass_interaction:
                result = orchestrator.run(user_input)
            else:
                result = orchestrator.run(user_input, selection_callback=interactive_selection_callback)

            if "error" in result:
                print(f"\n❌ ERROR: {result['error']}\n")
                continue

            print("\n🎯 EXECUTION PLAN")
            for i, step in enumerate(result.get("plan", []), 1):
                print(f"  Step {i}: [{step['capability']}] → \"{step['task']}\"")

            if bypass_interaction:
                print("\n🔍 AGENT DISCOVERY")
                for cap, candidates in result.get("candidate_agents", {}).items():
                    print(f"  Capability: {cap}")
                    print(TableRenderer.render(f"Candidates for '{cap}'", candidates))

            print("\n⚡ AGENT SELECTION")
            for cap, agent in result.get("selected_agents", {}).items():
                print(f"  {cap} → {agent['name']} (score: {agent['score']}, source: {agent['source']}) ✅")

            print("\n📊 EXECUTION RESULTS")
            for i, res in enumerate(result.get("results", []), 1):
                print(f"  Step {i}: {res}")

            print("\n📋 EXECUTION TIMELINE")
            for i, tl in enumerate(result.get("timeline", []), 1):
                print(f"  [{i}] {tl['capability']} → {tl['selected_agent']} ({tl['source']}) → {tl['status']} ✅")

            print(f"\n✅ Execution complete. {len(result.get('plan', []))} step(s) processed.\n")
            
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    run_demo()