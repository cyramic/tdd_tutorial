from common.math_functions import add_numbers


def test_add_numbers():
    num1 = 4
    num2 = 5
    assert add_numbers(num1, num2) == 9
