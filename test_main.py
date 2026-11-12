"""Tests for main.py fruit count validation."""

import unittest

from main import get_random_fruits


class TestGetRandomFruits(unittest.TestCase):
    def test_accepts_upper_boundary(self):
        self.assertEqual(len(get_random_fruits(1000)), 1000)

    def test_rejects_above_upper_boundary(self):
        with self.assertRaises(ValueError):
            get_random_fruits(1001)

    def test_rejects_non_positive(self):
        with self.assertRaises(ValueError):
            get_random_fruits(0)
        with self.assertRaises(ValueError):
            get_random_fruits(-1)


if __name__ == "__main__":
    unittest.main()
