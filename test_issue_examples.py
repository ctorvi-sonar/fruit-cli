"""Regression tests for the simplified Sonar examples."""

import unittest

from issues.bad import calculate_something
from issues.fruit_demo import describe_fruit


class IssueExampleTests(unittest.TestCase):
    def test_calculate_something(self):
        cases = [
            ((3, 2, 1), 6),
            ((3, 1, 2), 4),
            ((3, 2, 2), 5),
            ((1, 2, 3), 1),
            ((2, 2, 1), 2),
            ((0, 2, 1), 0),
            ((3, 0, 1), 0),
            ((3, 2, 0), 0),
            ((-1, 2, 1), 0),
            ((3, -1, 1), 0),
            ((3, 2, -1), 0),
            ((float("nan"), 2, 1), 0),
            ((3, float("nan"), 1), 0),
            ((3, 2, float("nan")), 0),
        ]
        for arguments, expected in cases:
            with self.subTest(arguments=arguments):
                self.assertEqual(calculate_something(*arguments), expected)

    def test_describe_fruit(self):
        cases = [("Apple", "APPLE"), ("banana", "BANANA"), ("", "")]
        for name, expected in cases:
            with self.subTest(name=name):
                self.assertEqual(describe_fruit(name), expected)
