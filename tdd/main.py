from common.math_functions import add_numbers
from common.input_functions import get_input_values


def my_function():
    result = False
    while not result:
        num_a, num_b = get_input_values()
        result = add_numbers(num_a, num_b)
        if not result:
            print("Incorrect values specified. Make sure you enter numbers only.")

    print(result)


if __name__ == "__main__":
    my_function()
