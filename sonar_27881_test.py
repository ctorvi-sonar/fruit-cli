"""Test file for SONAR-27881 severity decoration validation."""


def process(value):
    if value == value:  # S1764: identical expressions on both sides
        return value
    return None


def check_type(x):
    if x == "text" and x == 42:  # S2159: silly equality, int can't be both
        return True
    return False


def always_fails():
    result = None
    result.strip()  # S1192/S2259: None dereference - NullPointerException equiv
    return result


def wrong_args():
    fruits = ["apple", "banana"]
    separator = ",".join(fruits, "extra_arg")  # S930: join takes 1 arg not 2
    return separator
