def multiply_two_numbers(m: int | float, n: int | float) -> int | float | None:
    """
    Multiplies two numbers and returns the product.
    :param m: An integer or float.
    :param n: An integer or float.
    :return: The product of the two integers.
    """
    try:
        if not isinstance(m, int | float) or not isinstance(n, int | float): # if m or n are not int or float
            raise TypeError # raise a TypeError

        return m * n # If both m and n are integers or floats, this part of the code will run

    # this part of the code, "catches" these error types, but prevents the program from stopping
    # and informs the user.
    except (TypeError, ValueError):
        print(f'"m" should be an integer or float. Check "m": {m}\n',
              f'"n" should be an integer or float. Check "n": {n}')

if __name__ == "__main__":
    # Unit Tests
    test = [[4, 6], [4, 'a'], ['a', 'b'], [0.5, 1], [0.6, 0.25], [1, [1, 2, 3]]]
    # This list keeps the expected test results.
    expected_result = [24, None, None, 0.5, 0.15, None]
    # Will initiate an empty list, so can keep test results.
    result = []
    for i in range(len(test)):
        result.append(multiply_two_numbers(test[i][0], test[i][1]))

    if expected_result == result:
        print(f'Congratulations, your tests have passed. Result: {result}.')
    else:
        print(f'Sorry your tests have not passed. Result is different from expected results. '
              f'Have you updated your unit tests?\n',
              f'Result: {result}\n',
              f'Expected Result: {expected_result}')
