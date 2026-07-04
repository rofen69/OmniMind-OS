class TableRenderer:
    """
    Lightweight CLI table renderer for judge-friendly output.
    No external dependency.
    """

    @staticmethod
    def render(title: str, rows: list[dict]):

        if not rows:
            return f"\n{title}: No data\n"

        keys = list(rows[0].keys())

        output = f"\n=== {title} ===\n"

        # header
        output += " | ".join(keys) + "\n"
        output += "-" * (len(keys) * 10) + "\n"

        # rows
        for r in rows:
            output += " | ".join(str(r[k]) for k in keys) + "\n"

        return output