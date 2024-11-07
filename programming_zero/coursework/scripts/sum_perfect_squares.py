def sum_perfect_squares(number: int) -> int | None:
    """
    This function sums the perfect squares in the multiplication table up to n x n.
    :param number: An integer.
    :return: The perfect squares in the multiplication table up to n x n, or None.
    """
    if isinstance(number, int):
        products = []
        # Loop through all numbers in the multiplication table up to n * n
        for k in range(1, number + 1):
            for j in range(1, number + 1):
                product = k * j
                if int(product**0.5)**2 == product:  # Check if the product is odd
                    products.append(product)
        # According to the example output in the coursework pdf, we probably
        # have to get a set to get the correct output.
        # E.g., for n = 4, the output is expected to be 30.
        # This is only true if we consider the unique perfect squares.
        total_sum = sum(set(products))
        return total_sum
    else:
        print(f'Input must be an integer. Type of input is: {type(number)}')

if __name__ == "__main__":
    test = [4, 'a', [1], [1, 2], {'a': 1, 'b': 2}, 1, 0, 1.1]
    # This list keeps the expected test results.
    expected_result = [30, None, None, None, None, 1, 0, None]
    # Will initiate an empty list, so can keep test results.
    result = []
    for i in range(len(test)):
        result.append(sum_perfect_squares(test[i]))

    if expected_result == result:
        print(f'Congratulations, your tests have passed. Result: {result}.')

    else:
        print(f'Sorry your tests have not passed. Result is different from expected results. '
              f'Have you updated your unit tests?\n',
              f'Result: {result}\n',
              f'Expected Result: {expected_result}')
