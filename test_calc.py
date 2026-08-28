from calc import add, multiply, is_even


def test_add():
    assert add(2, 3) == 5


def test_multiply():
    assert multiply(3, 4) == 12


def test_is_even():
    assert is_even(4) is True
    assert is_even(3) is False
