"""Formatting for terminal and machine-readable output."""

import json


def format_fruits(fruits: list[str], output_format: str = "text") -> str:
    """Render fruits as lines or a JSON array."""
    if output_format == "json":
        return json.dumps(fruits)
    if output_format == "text":
        return "\n".join(fruits)
    raise ValueError(f"Unsupported output format: {output_format}")
