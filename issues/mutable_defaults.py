"""Intentional Sonar fixture: shared mutable default arguments."""


def add_fruit(name: str, basket: list[str] | None = None) -> list[str]:
    """Calls without a basket accidentally share the same list."""
    if basket is None:
        basket = []
    basket.append(name)
    return basket


def count_fruit(name: str, counts: dict[str, int] | None = None) -> dict[str, int]:
    """Calls without counts accidentally retain previous totals."""
    if counts is None:
        counts = {}
    counts[name] = counts.get(name, 0) + 1
    return counts
