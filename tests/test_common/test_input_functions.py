from tdd.common.input_functions import get_values_from_input
import pytest


def test_get_only_numbers_from_input():
    input = "14 21 33 44 13 98"
    numbers, other = get_values_from_input(input)
    assert numbers == [14,21,33,44,13,98]
    assert other == []


def test_get_mixed_from_input():
    input = "1 2 a 4"
    numbers, other = get_values_from_input(input)
    assert numbers == [1,2,4]
    assert other == ["a"]


def test_word_in_input():
    input = "0 4 bob 6"
    numbers, other = get_values_from_input(input)
    assert numbers == [0, 4, 6]
    assert other == ["bob"]


def test_extra_spaces():
    input = "1                         2    4"
    numbers, other = get_values_from_input(input)
    assert numbers == [1,2,4]
    assert other == []


def test_empty_input():
    input = "                     "
    numbers, other = get_values_from_input(input)
    assert numbers == []
    assert other == []


def test_only_string_inputs():
    input = "a b c d e"
    numbers, other = get_values_from_input(input)
    assert numbers == []
    assert other == ["a", "b", "c", "d", "e"]
