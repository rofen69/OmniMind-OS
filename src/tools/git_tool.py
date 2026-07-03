import subprocess

class GitTool:
    """
    Executes safe git operations (capstone-friendly abstraction)
    """

    def execute(self, command: str):
        try:
            result = subprocess.run(
                ["git"] + command.split(),
                capture_output=True,
                text=True
            )

            return {
                "stdout": result.stdout,
                "stderr": result.stderr,
                "code": result.returncode
            }

        except Exception as e:
            return {"error": str(e)}