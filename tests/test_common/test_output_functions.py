from tdd.common.output_functions import output_results
import sys


def test_console_output(capsys):
    answer = 12
    other_values = ["a"]
    output_results(answer, other_values)

    captured = capsys.readouterr()
    lines = captured.out.split("\n")
    assert lines[0] == "The answer is: 12"
    assert lines[1] == 'Value "a" skipped as it is not a number'
    assert len(lines) == 3


def test_multiple_other_values_in_output(capsys):
    answer = 25
    other_values = ["a", "bob", "c"]
    output_results(answer, other_values)

    captured = capsys.readouterr()
    lines = captured.out.split("\n")
    assert lines[0] == "The answer is: 25"
    assert lines[1] == 'Value "a" skipped as it is not a number'
    assert lines[2] == 'Value "bob" skipped as it is not a number'
    assert lines[3] == 'Value "c" skipped as it is not a number'
    assert len(lines) == 5