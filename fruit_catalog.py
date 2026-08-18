"""Fruit catalog and case-insensitive filtering."""

FRUITS = [
    "Apple", "Banana", "Orange", "Mango", "Strawberry", "Pineapple",
    "Watermelon", "Grape", "Kiwi", "Peach", "Pear", "Cherry", "Plum",
    "Blueberry", "Raspberry", "Blackberry", "Lemon", "Lime", "Grapefruit",
    "Papaya", "Coconut", "Avocado", "Pomegranate", "Fig", "Apricot",
    "Cantaloupe", "Honeydew", "Tangerine", "Nectarine", "Passion Fruit",
]


def filter_fruits(query: str = "") -> list[str]:
    """Return fruits containing the query, preserving catalog order."""
    return [fruit for fruit in FRUITS if query.casefold() in fruit.casefold()]
