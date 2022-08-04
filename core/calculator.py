"""Calculation functions"""


def add(x, y):  # pylint: disable=invalid-name
    """Add function"""
    return x + y


def subtract(x, y):  # pylint: disable=invalid-name
    """Subtract function"""
    return x - y


def multiply(x, y):  # pylint: disable=invalid-name
    """Multiply function"""
    return x * y


def divide(x, y):  # pylint: disable=invalid-name
    """Divide function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y
