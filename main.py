"""Fruit CLI - Generate random fruits."""

import argparse
import random
import sys
from typing import List

# Comprehensive list of fruits
FRUITS = [
    "Apple", "Banana", "Orange", "Mango", "Strawberry",
    "Pineapple", "Watermelon", "Grape", "Kiwi", "Peach",
    "Pear", "Cherry", "Plum", "Blueberry", "Raspberry",
    "Blackberry", "Lemon", "Lime", "Grapefruit", "Papaya",
    "Coconut", "Avocado", "Pomegranate", "Fig", "Apricot",
    "Cantaloupe", "Honeydew", "Tangerine", "Nectarine", "Passion Fruit",
]


def get_random_fruits(count: int) -> List[str]:
    """
    Get a list of random fruits.

    Args:
        count: Number of fruits to return.

    Returns:
        List of random fruit names.

    Raises:
        ValueError: If count is less than or equal to 0.
    """
    if count <= 0:
        raise ValueError("Count must be a positive integer")

    # Use random.choices to allow duplicates when count > len(FRUITS)
    return random.choices(FRUITS, k=count)


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate random fruits",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s          # Get one random fruit
  %(prog)s 5        # Get 5 random fruits
  %(prog)s --count 3  # Get 3 random fruits
        """,
    )
    parser.add_argument(
        "count",
        nargs="?",
        type=int,
        default=1,
        help="Number of random fruits to generate (default: 1)",
    )
    return parser.parse_args()


def main() -> int:
    """
    Main entry point for the fruit CLI.

    Returns:
        Exit code (0 for success, 1 for error).
    """
    try:
        args = parse_arguments()
        fruits = get_random_fruits(args.count)

        # Print each fruit on a new line
        for fruit in fruits:
            print(fruit)

        return 0
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("\nAborted", file=sys.stderr)
        return 130
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
