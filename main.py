"""Fruit CLI - Generate random fruits."""

import argparse
import sys
from fruit_catalog import FRUITS, filter_fruits
from fruit_output import format_fruits
from fruit_selection import get_random_fruits as select_fruits

def get_random_fruits(count: int) -> list[str]:
    """
    Get a list of random fruits.

    Args:
        count: Number of fruits to return.

    Returns:
        List of random fruit names.

    Raises:
        ValueError: If count is less than or equal to 0.
    """
    return select_fruits(count)


def parse_arguments(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate random fruits",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s          # Get one random fruit
  %(prog)s 5        # Get 5 random fruits
  %(prog)s 2 --unique --seed 42 --format json
        """,
    )
    parser.add_argument(
        "count",
        nargs="?",
        type=int,
        default=1,
        help="Number of random fruits to generate (default: 1)",
    )
    parser.add_argument("--filter", default="", help="Case-insensitive name substring")
    parser.add_argument("--unique", action="store_true", help="Select without duplicates")
    parser.add_argument("--seed", type=int, help="Seed for reproducible selections")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--list", action="store_true", help="List matching fruits instead")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """
    Main entry point for the fruit CLI.

    Returns:
        Exit code (0 for success, 1 for error).
    """
    try:
        args = parse_arguments(argv)
        if args.list:
            fruits = filter_fruits(args.filter)
        else:
            fruits = select_fruits(
                args.count, query=args.filter, unique=args.unique, seed=args.seed
            )
        output = format_fruits(fruits, args.format)
        if output:
            print(output)

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
