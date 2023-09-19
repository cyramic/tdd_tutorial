def get_input_values() -> str:
    input = input("Enter a series of numbers separated by spaces: ")
    return input


def get_values_from_input(input: str):
    values = input.split(" ")
    numbers = []
    other = []
    for value in values:
        try:
            numbers.append(int(value))
        except ValueError:
            if value.strip() != "":
                other.append(value)
    return numbers, other
