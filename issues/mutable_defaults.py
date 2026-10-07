"""Intentional Sonar fixture: shared mutable default arguments."""


def add_fruit(name: str, basket: list[str] = []) -> list[str]:
    """Calls without a basket accidentally share the same list."""
    basket.append(name)
    return basket


def count_fruit(name: str, counts: dict[str, int] = {}) -> dict[str, int]:
    """Calls without counts accidentally retain previous totals."""
    counts[name] = counts.get(name, 0) + 1
    return counts
