
def output_results(answer: int, non_number_inputs: list):
    print("The answer is: {}".format(answer))
    for value in non_number_inputs:
        print('Value "{}" skipped as it is not a number'.format(value))