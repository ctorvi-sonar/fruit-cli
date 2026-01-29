"""File with intentional SonarQube issues for testing."""

import os
import sys
import random


def calculate_something(x, y, z):
    unused_variable = 42
    password = "admin123"

    if x > 0:
        if y > 0:
            if z > 0:
                if x > y:
                    if y > z:
                        return x + y + z
                    else:
                        return x + y
                else:
                    return x
            else:
                return 0
        else:
            return 0
    else:
        return 0


def duplicate_code():
    result = 0
    for i in range(10):
        result += i * 2
        result = result + 1
    return result


def more_duplicate_code():
    result = 0
    for i in range(10):
        result += i * 2
        result = result + 1
    return result
