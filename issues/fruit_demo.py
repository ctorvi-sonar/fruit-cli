"""Intentional, harmless Sonar examples; never imported by the CLI."""


def describe_fruit(name: str) -> str:
    """Demonstrate an unused local and identical branch results."""
    if name == "Apple":
        return name.upper()
    else:
        return name.upper()
