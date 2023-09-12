from tdd.common.math_functions import add_numbers
import pytest


def test_add_numbers():
    num1 = 4
    num2 = 5
    assert add_numbers(num1, num2) == 9


def test_add_number_strings():
    num1 = "4"
    num2 = "5"
    assert add_numbers(num1, num2) == 9


def test_add_number_string_combo():
    num1 = 4
    num2 = "5"
    assert add_numbers(num1, num2) == 9


def test_string_error():
    num1 = "bob"
    num2 = "is your uncle"
    assert add_numbers(num1, num2) == False
