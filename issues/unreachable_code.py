"""Intentional Sonar fixture: statements after an unconditional return."""


def fruit_price(quantity: int) -> int:
    """The intended bulk discount can never execute."""
    total = quantity * 3
    if quantity >= 10:
        total -= 5
    return total
