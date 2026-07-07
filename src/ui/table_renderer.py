"""
Table Renderer Module

Provides lightweight CLI table rendering for judge-friendly output.
"""
from typing import List, Dict, Any


class TableRenderer:
    """
    Lightweight CLI table renderer for judge-friendly output.
    No external dependency. Dynamic column widths.
    """

    @staticmethod
    def render(title: str, rows: List[Dict[str, Any]]) -> str:
        """
        Render a list of dictionaries as a formatted CLI table.

        Args:
            title (str): The title of the table.
            rows (List[Dict[str, Any]]): The data rows to render.

        Returns:
            str: The formatted table string.
        """
        if not rows:
            return f"\n{title}: No data\n"

        keys = list(rows[0].keys())

        # Calculate max width for each column
        col_widths = {key: len(key) for key in keys}
        for row in rows:
            for key in keys:
                val_len = len(str(row.get(key, "")))
                if val_len > col_widths[key]:
                    col_widths[key] = val_len

        output = f"\n=== {title} ===\n"

        # Header
        header_parts = [key.ljust(col_widths[key]) for key in keys]
        output += " | ".join(header_parts) + "\n"

        # Separator
        separator_parts = ["-" * col_widths[key] for key in keys]
        output += "-+-".join(separator_parts) + "\n"

        # Rows
        for row in rows:
            row_parts = [str(row.get(key, "")).ljust(col_widths[key]) for key in keys]
            output += " | ".join(row_parts) + "\n"

        return output