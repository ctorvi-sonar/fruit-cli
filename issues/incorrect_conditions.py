"""Intentional Sonar fixture: a condition that always evaluates to true."""


def is_supported_fruit(name: str) -> bool:
    if name == "apple" or name == "banana":
        return True
    return False
