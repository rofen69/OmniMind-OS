class Guardrails:
    def validate_input(self, user_input: str) -> bool:
        return bool(user_input and user_input.strip() and len(user_input) < 2000)