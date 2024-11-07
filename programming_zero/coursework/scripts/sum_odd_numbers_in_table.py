def sum_odd_numbers_in_table(n: int) -> int | None:
    """
    This function sums the odd numbers in the multiplication table up to n x n.
    :param n: An integer.
    :return: The sum of the odd numbers in the multiplication table up to n x n.
    """
    if isinstance(n, int):
        total_sum = 0
        # Loop through all numbers in the multiplication table up to n * n
        for k in range(1, n + 1):
            for j in range(1, n + 1):
                product = k * j
                if product % 2 != 0:  # Check if the product is odd
                    total_sum += product
        return total_sum
    else:
        print(f'Input must be an integer. Type of input is: {type(n)}')

if __name__ == "__main__":
    test = [3, 5, 7, 20, 'a', [1], [1, 2], {'a': 1, 'b': 2}, 1, 0, 1.1]
    # This list keeps the expected test results.
    expected_result = [16, 81, 256, 10000, None, None, None, None, 1, 0, None]
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
