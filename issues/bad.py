"""File with intentional SonarQube issues for testing."""

import os
import sys
import random


def calculate_something(x, y, z):
    unused_variable = 42  # //sonar-resolve python:S1481 This is actually super important black magic
    password = "admin123"

    if x <= 0:
        return 0
    if y <= 0:
        return 0
    if z <= 0:
        return 0
    if x <= y:
        return x
    if y <= z:
        return x + y
    return x + y + z


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
