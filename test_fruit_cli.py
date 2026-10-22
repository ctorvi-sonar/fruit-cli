"""Standard-library tests for fruit selection and CLI behavior."""

import contextlib
import io
import json
import random
import unittest

from fruit_catalog import FRUITS, filter_fruits
from fruit_output import format_fruits
from fruit_selection import get_random_fruits
from main import main, parse_arguments


class FruitTests(unittest.TestCase):
    def run_cli(self, arguments):
        stdout, stderr = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            status = main(arguments)
        return status, stdout.getvalue(), stderr.getvalue()

    def test_catalog_and_filter(self):
        self.assertEqual(len(FRUITS), 30)
        self.assertEqual(filter_fruits("APPLE"), ["Apple", "Pineapple"])
        self.assertEqual(filter_fruits(), FRUITS)

    def test_seed_is_repeatable_and_does_not_change_global_state(self):
        state = random.getstate()
        self.assertEqual(get_random_fruits(10, seed=4), get_random_fruits(10, seed=4))
        self.assertEqual(random.getstate(), state)

    def test_unique_and_filtered_selection(self):
        fruits = get_random_fruits(2, query="apple", unique=True, seed=2)
        self.assertEqual(set(fruits), {"Apple", "Pineapple"})
        self.assertEqual(len(set(get_random_fruits(30, unique=True))), 30)

    def test_duplicates_are_allowed(self):
        self.assertEqual(get_random_fruits(40, query="banana"), ["Banana"] * 40)

    def test_invalid_selections(self):
        cases = [(0, {}), (-1, {}), (1, {"query": "nothing"}),
                 (31, {"unique": True}),
                 (3, {"query": "apple", "unique": True})]
        for count, options in cases:
            with self.subTest(count=count, options=options):
                with self.assertRaises(ValueError):
                    get_random_fruits(count, **options)

    def test_formats(self):
        self.assertEqual(format_fruits(["Apple", "Pear"]), "Apple\nPear")
        self.assertEqual(json.loads(format_fruits([], "json")), [])
        with self.assertRaises(ValueError):
            format_fruits([], "invalid")

    def test_cli_defaults_and_positional_count(self):
        self.assertEqual(parse_arguments([]).count, 1)
        status, output, error = self.run_cli(["3", "--filter", "banana"])
        self.assertEqual((status, output, error), (0, "Banana\n" * 3, ""))

    def test_cli_json_list_and_empty_list(self):
        arguments = ["--list", "--filter", "APPLE", "--format", "json"]
        status, output, error = self.run_cli(arguments)
        self.assertEqual(status, 0)
        self.assertEqual(json.loads(output), ["Apple", "Pineapple"])
        self.assertEqual(error, "")
        self.assertEqual(self.run_cli(["--list", "--filter", "nothing"]), (0, "", ""))
        status, output, error = self.run_cli(["--list", "--filter", "nothing", "--format", "json"])
        self.assertEqual((status, json.loads(output), error), (0, [], ""))

    def test_cli_selection_error(self):
        status, output, error = self.run_cli(["31", "--unique"])
        self.assertEqual(status, 1)
        self.assertEqual(output, "")
        self.assertIn("Only 30", error)

    def test_cli_invalid_arguments(self):
        with contextlib.redirect_stderr(io.StringIO()):
            for arguments in [["no-number"], ["--format", "xml"]]:
                with self.subTest(arguments=arguments):
                    with self.assertRaises(SystemExit) as raised:
                        parse_arguments(arguments)
                    self.assertEqual(raised.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
