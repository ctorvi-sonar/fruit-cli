"""Random selection with optional uniqueness and reproducibility."""

import random

from fruit_catalog import filter_fruits


def get_random_fruits(
    count: int, *, query: str = "", unique: bool = False, seed: int | None = None
) -> list[str]:
    """Select fruits without changing the process-wide random state."""
    if count <= 0:
        raise ValueError("Count must be a positive integer")
    candidates = filter_fruits(query)
    if not candidates:
        raise ValueError("No fruits match the filter")
    if unique and count > len(candidates):
        raise ValueError(f"Only {len(candidates)} matching fruits are available")
    generator = random.Random(seed)
    if unique:
        return generator.sample(candidates, k=count)
    return generator.choices(candidates, k=count)
