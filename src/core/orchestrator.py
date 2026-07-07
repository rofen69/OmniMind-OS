"""
Orchestrator Module

Provides the core OmniMind Execution Engine.
"""
import logging
from typing import Any, Dict

from src.core.guardrails import Guardrails
from src.core.planner import Planner
from src.core.registry import AgentRegistry
from src.discovery.selector import AgentSelector
from src.shared.preferences import UserPreferences

logger = logging.getLogger(__name__)


class Orchestrator:
    """
    OmniMind Execution Engine

    Flow:
    User Input
        ↓
    Planner (Capability Plan)
        ↓
    Discovery (Agent Candidates)
        ↓
    Selection (Best Agent)
        ↓
    Execution (Agent Output)
    """

    def __init__(self, planner: Planner, registry: AgentRegistry) -> None:
        """
        Initialize the Orchestrator with a planner and an agent registry.

        Args:
            planner (Planner): The planner instance used to decompose goals.
            registry (AgentRegistry): The registry for discovering agents and tools.
        """
        self.planner = planner
        self.registry = registry

        self.guardrails = Guardrails()
        self.selector = AgentSelector()
        self.preferences = UserPreferences()

    def run(self, user_input: str, selection_callback=None) -> Dict[str, Any]:
        """
        Execute a user request by planning, discovering, selecting, and executing.

        Args:
            user_input (str): The raw input provided by the user.
            selection_callback (callable, optional): Callback for interactive agent selection.

        Returns:
            Dict[str, Any]: A detailed execution trace including plan, selected agents, and results.
        """
        logger.info(f"Starting execution for input: {user_input[:50]}...")

        # Guardrails check before planning
        if not self.guardrails.validate_input(user_input):
            logger.warning("Input blocked by guardrails.")
            return {"error": "Blocked by guardrails"}

        plan = self.planner.create_plan(user_input)
        logger.info(f"Created plan with {len(plan.steps)} steps.")

        discovered: Dict[str, Any] = {}
        selected: Dict[str, Any] = {}
        timeline: list[Dict[str, str]] = []
        results: list[Any] = []

        for step in plan.steps:
            capability = step.capability
            logger.info(f"Processing step for capability: {capability}")

            # 1. DISCOVER: Find candidates via the registry's capability search
            candidates = self.registry.discover_capability(capability)
            logger.debug(f"Discovered {len(candidates)} candidates for {capability}.")

            discovered[capability] = [
                {
                    "name": a.name,
                    "source": a.source,
                    "installed": getattr(a, "installed", False),
                    "cost": a.cost,
                    "license": a.license,
                    "score": a.score,
                    "limitations": a.limitations,
                    "requirements": a.requirements,
                }
                for a in candidates
            ]

            # 2. SELECT BEST AGENT: Choose the best candidate based on user preferences
            chosen = self.selector.select(candidates, self.preferences)
            
            # Interactive selection if callback is provided
            if selection_callback and candidates:
                chosen = selection_callback(capability, candidates, chosen)

            if chosen:
                logger.info(f"Selected agent {chosen.name} for {capability}.")
                selected[capability] = {
                    "name": chosen.name,
                    "source": chosen.source,
                    "score": chosen.score,
                }
            else:
                logger.warning(f"No suitable agent found for {capability}.")

            # 3. EXECUTION: Run via agent or tool based on prefix routing
            if capability.startswith("tool:"):
                # Extract tool name and execute
                tool = self.registry.get_tool(capability.split(":")[1])
                if tool:
                    result = tool.execute(step.task)
                else:
                    logger.error(f"Tool {capability} not found in registry.")
                    result = {"error": f"Tool {capability} not found"}
                    
                timeline.append({
                    "capability": capability,
                    "selected_agent": capability,
                    "source": "Local",
                    "status": "executed" if tool else "failed"
                })
            else:
                # Route to the selected agent based on chosen.name
                if chosen:
                    if self.registry.has_agent(chosen.name):
                        agent = self.registry.get_agent(chosen.name)
                        result = agent.execute(step.task)
                        timeline.append({
                            "capability": capability,
                            "selected_agent": chosen.name,
                            "source": chosen.source,
                            "status": "executed"
                        })
                    else:
                        logger.error(f"Agent {chosen.name} not found in registry.")
                        result = {"error": f"Agent {chosen.name} not found"}
                        timeline.append({
                            "capability": capability,
                            "selected_agent": chosen.name,
                            "source": chosen.source,
                            "status": "failed"
                        })
                else:
                    result = {"error": f"No candidate found for {capability}"}
                    timeline.append({
                        "capability": capability,
                        "selected_agent": "None",
                        "source": "None",
                        "status": "failed"
                    })

            results.append(result)

        # Assemble the final result output
        return {
            "input": user_input,
            "plan": [
                {
                    "capability": s.capability,
                    "task": s.task,
                }
                for s in plan.steps
            ],
            "candidate_agents": discovered,
            "selected_agents": selected,
            "timeline": timeline,
            "results": results,
        }