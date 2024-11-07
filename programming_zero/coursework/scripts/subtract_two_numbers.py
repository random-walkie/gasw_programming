def subtract_two_numbers(m: int | float, n: int | float) -> int | float | None:
    """
    This function subtracts the second number n from the first m.
    :param m: First numerical value.
    :param n: Second numerical value. It will be subtracted from m.
    :return: The subtracted numerical value, or None.
    """
    allowed_types = (int, float)
    if isinstance(m, allowed_types) and isinstance(n, allowed_types):
        return m - n
    else:
        print('Input values should be of type integer or float\n',
              f'm is of type: {type(m)}\n',
              f'n is of type: {type(n)}')

if __name__ == "__main__":
    # Unit Tests
    test = [[10, 4], [3.42, 'a'], ['a', 'a'], [[1], 1], [5, 10], [0.23, 1.23]]
    # This list keeps the expected test results.
    expected_result = [6, None, None, None, -5, -1.0]
    # Will initiate an empty list, so can keep test results.
    result = []
    for i in range(len(test)):
        result.append(subtract_two_numbers(test[i][0], test[i][1]))

    if expected_result == result:
        print(f'Congratulations, your tests have passed. Result: {result}.')

    else:
        print(f'Sorry your tests have not passed. Result is different from expected results. '
              f'Have you updated your unit tests?\n',
              f'Result: {result}\n',
              f'Expected Result: {expected_result}')
