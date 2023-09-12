from common.math_functions import add_numbers


def my_function():
    num_a = input("Enter a number: ")
    num_b = input("Enter a second number: ")

    result = add_numbers(num_a, num_b)
    print(result)


if __name__ == "__main__":
    my_function()
