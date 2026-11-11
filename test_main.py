"""Tests for main.py fruit CLI."""

import unittest

from main import FRUITS, MAX_FRUIT_COUNT, get_random_fruits


class GetRandomFruitsTest(unittest.TestCase):
    def test_non_positive_count_raises_value_error(self):
        with self.assertRaises(ValueError):
            get_random_fruits(0)
        with self.assertRaises(ValueError):
            get_random_fruits(-1)

    def test_max_count_returns_max_items(self):
        fruits = get_random_fruits(MAX_FRUIT_COUNT)
        self.assertEqual(len(fruits), MAX_FRUIT_COUNT)

    def test_count_above_max_raises_value_error(self):
        with self.assertRaises(ValueError):
            get_random_fruits(MAX_FRUIT_COUNT + 1)

    def test_normal_count_returns_requested_fruits(self):
        fruits = get_random_fruits(5)
        self.assertEqual(len(fruits), 5)
        for fruit in fruits:
            self.assertIn(fruit, FRUITS)


if __name__ == "__main__":
    unittest.main()
