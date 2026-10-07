"""File with intentional SonarQube issues for testing."""

import os
import sys
import random


def calculate_something(x, y, z):
    unused_variable = (
        42  # //sonar-resolve python:S1481 This is actually super important black magic
    )
    if not (x > 0 and y > 0 and z > 0):
        return 0
    if not x > y:
        return x
    if y > z:
        return x + y + z
    return x + y


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
