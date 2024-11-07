def sum_odd_numbers_in_table(n: int) -> int | None:
    """
    This function sums the odd numbers in the multiplication table up to n x n.
    :param n: An integer.
    :return: The sum of the odd numbers in the multiplication table up to n x n.
    """
    if isinstance(n, int):
        mult_list = [x for x in range(1, n * n, 2)]

        return sum(mult_list)
    else:
        print(f'Input must be an integer. Type of input is: {type(n)}')

if __name__ == "__main__":
    test = [1, 2, 3, 4, 5, 6, 1.2, 'a', {'a': 1, 'b': 1}, [1]]
    # This list keeps the expected test results.
    expected_result = [0, 4, 16, 64, 144, 324, None, None, None, None]
    # Will initiate an empty list, so can keep test results.
    result = []
    for i in range(len(test)):
        result.append(sum_odd_numbers_in_table(test[i]))

    if expected_result == result:
        print(f'Congratulations, your tests have passed. Result: {result}.')

    else:
        print(f'Sorry your tests have not passed. Result is different from expected results. '
              f'Have you updated your unit tests?\n',
              f'Result: {result}\n',
              f'Expected Result: {expected_result}')
