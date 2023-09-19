from tdd.common.input_functions import get_values_from_input

def test_get_only_numbers_from_input():
    input = "14 21 33 44 13 98"
    expected_numbers = [14, 21, 33, 44, 13, 98]

    answer = get_values_from_input(input)

    assert answer == expected_numbers


def test_get_mixed_from_input():
    input = "1 2 a 4"
    expected_numbers = [1, 2, 4]

    answer = get_values_from_input(input)

    assert answer == expected_numbers

def test_get_empty_input():
    input = ""
    expected_numbers = []

    answer = get_values_from_input(input)

    assert answer == expected_numbers