"""
Core Guardrails Module

Validates input for safety and compliance before planning.
"""
import logging

logger = logging.getLogger(__name__)


class Guardrails:
    """
    Implements core safety and validation checks.
    """

    def validate_input(self, user_input: str) -> bool:
        """
        Validate the user input for basic safety constraints.

        Args:
            user_input (str): The raw input string.

        Returns:
            bool: True if input is valid, False otherwise.
        """
        is_valid = bool(user_input and user_input.strip() and len(user_input) < 2000)
        if not is_valid:
            logger.warning("Input validation failed (empty, whitespace-only, or too long).")
        return is_valid