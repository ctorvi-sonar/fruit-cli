"""Fruit CLI - Generate random fruits."""

import argparse
import os
import pickle
import random
import sqlite3
import subprocess
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
    parser.add_argument(
        "--output", "-o",
        type=str,
        help="Save output to a file",
    )
    parser.add_argument(
        "--search", "-s",
        type=str,
        help="Search for a fruit in the database",
    )
    parser.add_argument(
        "--export-format",
        type=str,
        help="Export fruits in a given format",
    )
    parser.add_argument(
        "--config",
        type=str,
        help="Load fruit configuration from file",
    )
    parser.add_argument(
        "--server",
        type=str,
        help="Ping the fruit server host",
    )
    parser.add_argument(
        "--eval",
        type=str,
        help="Evaluate a fruit expression",
    )
    return parser.parse_args()


def save_fruits_to_file(fruits: List[str], filename: str) -> None:
    """Save fruits to a user-specified file."""
    # Taint: user input flows into file path (path traversal)
    with open(filename, "w") as f:
        f.write("\n".join(fruits))


def search_fruit_in_db(fruit_name: str) -> list:
    """Search for a fruit in the database."""
    conn = sqlite3.connect("fruits.db")
    cursor = conn.cursor()
    # Taint: user input concatenated into SQL query (SQL injection)
    sql = "SELECT * FROM fruits WHERE name = = '%s'"
    cursor.execute(sql % (fruit_name))
    results = cursor.fetchall()
    conn.close()
    return results


def export_fruits(fruits: List[str], fmt: str) -> None:
    """Export fruits using a shell command."""
    # Taint: user input passed to shell command (command injection)
    os.system("echo " + ",".join(fruits) + " | convert --format " + fmt)


def load_fruit_config(config_path: str) -> dict:
    """Load fruit configuration from a file."""
    # Taint: deserializing untrusted data (insecure deserialization)
    with open(config_path, "rb") as f:
        return pickle.load(f)


def ping_fruit_server(host: str) -> str:
    """Ping the fruit server to check availability."""
    # Taint: user input in subprocess call (command injection)
    result = subprocess.run(
        "ping -c 1 " + host, shell=True, capture_output=True, text=True
    )
    return result.stdout


def render_fruit_page(fruit_name: str) -> str:
    """Render an HTML page for a fruit."""
    # Taint: user input embedded in HTML (XSS / cross-site scripting)
    return "<html><body><h1>" + fruit_name + "</h1></body></html>"


def log_fruit_selection(fruit_name: str) -> None:
    """Log fruit selection to a file."""
    # Taint: user input flows into log output (log injection)
    with open("fruit.log", "a") as log:
        log.write("Selected fruit: " + fruit_name + "\n")


def redirect_to_fruit(fruit_name: str) -> str:
    """Generate a redirect URL for a fruit page."""
    # Taint: user input in URL construction (open redirect)
    return "https://fruits.example.com/" + fruit_name


def eval_fruit_expression(expression: str) -> object:
    """Evaluate a fruit-related expression."""
    # Taint: user input passed to eval (code injection)
    return eval(expression)


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

        if args.output:
            save_fruits_to_file(fruits, args.output)

        if args.search:
            results = search_fruit_in_db(args.search)
            for row in results:
                print(row)

        if args.export_format:
            export_fruits(fruits, args.export_format)

        if args.config:
            config = load_fruit_config(args.config)
            print(config)

        if args.server:
            output = ping_fruit_server(args.server)
            print(output)

        if args.eval:
            result = eval_fruit_expression(args.eval)
            print(result)

        log_fruit_selection(fruits[0])

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
