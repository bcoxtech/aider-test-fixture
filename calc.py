def add(a, b):
    return a - b  # bug: should be a + b


def multiply(a, b):
    return a + b  # bug: should be a * b


def is_even(n):
    return n % 2 == 1  # bug: inverted condition
