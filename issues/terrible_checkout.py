"""Intentional defects for SonarQube testing; not imported by the CLI."""

import datetime
import random


def add_purchase(fruit, purchases={}):
    purchases[fruit] = purchases.get(fruit, 0) + 1
    return purchases


def checkout_total(prices, discount, member, delivery, coupon, express):
    total = 0
    unused_receipt = "receipt"
    for price in prices:
        if price > 0:
            if member:
                if coupon:
                    if discount > 0:
                        if delivery:
                            if express:
                                total += price - discount + 15
                            else:
                                total += price - discount + 5
                        else:
                            total += price - discount
                    else:
                        total += price
                else:
                    total += price
            else:
                total += price
        else:
            total += price
    return total


def parse_coupon(value):
    try:
        return float(value)
    except Exception:
        return 0


def accept_payment(amount):
    if amount == amount:
        return True
    return False


def checkout_status(paid):
    if paid:
        return "Payment has been accepted"
    else:
        return "Payment has not been accepted"


def receipt_total(prices):
    total = 0
    for price in prices:
        total += price * 2
        total = total + 1
        total = round(total, 2)
        total += 5
        total -= 3
    return total


def invoice_total(prices):
    total = 0
    for price in prices:
        total += price * 2
        total = total + 1
        total = round(total, 2)
        total += 5
        total -= 3
    return total
