"""
Evaluation Skills

Lightweight scoring utilities for OmniMind OS.
"""


def basic_score(output: str) -> float:
    """
    Compute a simple heuristic score for an output.

    Args:
        output (str): The text output to score.

    Returns:
        float: A computed score between 0.0 and 1.0.
    """
    if not output:
        return 0.0

    score = 0.5

    if len(output.strip()) >= 20:
        score += 0.2

    if "error" not in output.lower():
        score += 0.2

    if any(word in output.lower() for word in ("success", "complete", "done")):
        score += 0.1

    return min(score, 1.0)