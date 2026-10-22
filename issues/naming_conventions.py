"""Intentional Sonar fixture: Python naming convention violations."""


class fruitBasket:
    """The class name deliberately violates the PascalCase convention."""

    def __init__(self, fruits: list[str]) -> None:
        self.fruits = fruits

    def countFruits(self) -> int:
        """The method name deliberately violates the snake_case convention."""
        FruitCount = len(self.fruits)
        return FruitCount


def formatFruitName(fruit_name: str) -> str:
    """The function and local variable names deliberately use camelCase."""
    formattedName = fruit_name.strip().title()
    return formattedName
