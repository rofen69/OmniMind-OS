"""
Git Tool Module

Executes safe git operations (capstone-friendly abstraction).
"""
import subprocess
import shlex
from typing import Any, Dict

class GitTool:
    """
    Executes safe git operations (capstone-friendly abstraction)
    """

    def execute(self, command: str) -> Dict[str, Any]:
        """
        Execute a safe git command.
        
        Args:
            command (str): The git subcommand and arguments to execute.
            
        Returns:
            Dict[str, Any]: The execution result containing stdout, stderr, and return code.
        """
        try:
            # Parse command safely to avoid shell injection
            args = shlex.split(command)
            if not args:
                return {"error": "Empty command"}
                
            # Whitelist safe read-only operations for the capstone demo
            allowed_subcommands = {"status", "log", "diff", "show", "branch"}
            if args[0] not in allowed_subcommands:
                return {"error": f"Git command '{args[0]}' is not allowed. Only read operations are permitted."}
                
            result = subprocess.run(
                ["git"] + args,
                capture_output=True,
                text=True,
                check=False
            )

            return {
                "stdout": result.stdout,
                "stderr": result.stderr,
                "code": result.returncode
            }

        except Exception as e:
            return {"error": str(e)}