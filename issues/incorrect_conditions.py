"""Intentional Sonar fixture: a condition that always evaluates to true."""


def is_supported_fruit(name: str) -> bool:
    """The nonempty string makes unsupported fruits pass validation."""
    if name == "apple" or "banana":
        return True
    return False
