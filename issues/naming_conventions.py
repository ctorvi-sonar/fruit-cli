"""Intentional Sonar fixture: Python naming convention violations."""


class FruitBasket:
    """The class name deliberately violates the PascalCase convention."""

    def __init__(self, fruits: list[str]) -> None:
        self.fruits = fruits

    def count_fruits(self) -> int:
        """Return the number of fruits in the basket."""
        fruit_count = len(self.fruits)
        return fruit_count


def format_fruit_name(fruit_name: str) -> str:
    """Return the fruit name stripped of whitespace and title-cased."""
    formatted_name = fruit_name.strip().title()
    return formatted_name
