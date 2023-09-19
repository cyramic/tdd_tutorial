from common.math_functions import add_numbers
from common.input_functions import get_input_values, get_values_from_input
from common.output_functions import output_results

def my_function():
    result = False
    while not result:
        input = get_input_values()
        numbers, other = get_values_from_input(input)

        if len(numbers) > 0:
            result = True
        else:
            print("No numbers in the input. Please try again.")

    answer = add_numbers(numbers)
    output_results(answer, other)

if __name__ == "__main__":
    my_function()
