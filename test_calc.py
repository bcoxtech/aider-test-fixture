from calc import add, multiply, is_even, power, cube


def test_add():
    assert add(2, 3) == 5


def test_multiply():
    assert multiply(3, 4) == 12


def test_is_even():
    assert is_even(4) is True
    assert is_even(3) is False


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1


def test_cube():
    assert cube(2) == 8
    assert cube(3) == 27
    assert cube(0) == 0
