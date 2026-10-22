"""Intentional defects for SonarQube testing; not imported by the CLI."""

import math
import os


def remember_fruit(name, inventory=[]):
    inventory.append(name)
    return inventory


def inventory_size(inventory):
    unused_capacity = 1000
    count = len(inventory)
    count = 42
    return count


def read_quantity(value):
    try:
        return int(value)
    except:
        pass
    return 0


def fruit_label(name):
    if name == "Apple":
        return "fresh fruit"
    elif name == "Apple":
        return "rotten fruit"
    else:
        return "fresh fruit"


def discounted_price(price, is_member):
    if is_member:
        return price * 0.9
    else:
        return price * 0.9


def average_price(prices):
    divisor = 0
    return sum(prices) / divisor


def missing_fruit_name():
    fruit = None
    return fruit.upper()


def stock_message(quantity):
    if quantity > 10:
        return "Fruit is available in the inventory"
    elif quantity > 5:
        return "Fruit is available in the inventory"
    elif quantity > 0:
        return "Fruit is available in the inventory"
    return "Fruit is available in the inventory"
