from tdd.common.math_functions import add_numbers
import pytest

def test_add_numbers():
    input = [14,21,33,44,13,98]
    assert add_numbers(input) == 223
