def is_above_threshold(number: int | float, threshold: int | float) -> int:
    """
    This function takes a number and a threshold, and returns 1 if the number is greater than
    the threshold, otherwise returns 0.

    :param number: The number to check.
    :param threshold: The threshold to compare the number with.
    :return: 1 if the number is greater than the threshold, otherwise returns 0.
    """
    # Here we catch the case where all parameters are of str type.
    greater_than = 0
    if type(number) is str and type(threshold) is str:
        print('number and threshold are of str type. Please, update your input.')
    else:
        try:
            if number > threshold:
                greater_than = 1
        except TypeError: # if we get a TypeError, e.g., when trying to compare str and int | float types
            print(f'At least one of number: {number}, or threshold: {threshold} is not a number.')

    return greater_than

if __name__ == "__main__":
    # Unit Tests
    test = [[15, 10], [45, 1], [3, 'a'], ['a', 'b'], [0.3, 0.9], [15, 15], [0.9, 0.3]]
    # This list keeps the expected test results.
    expected_result = [1, 1, 0, 0, 0, 0, 1]
    # Will initiate an empty list, so I can keep my test results.
    result = []
    for i in range(len(test)):
        result.append(is_above_threshold(test[i][0], test[i][1]))

    if expected_result == result:
        print(f'Congratulations, your tests have passed. Result: {result}.')
    else:
        print(f'Sorry your tests have not passed. Result is different from expected results. '
              f'Have you updated your unit tests?\n',
              f'Result: {result}\n',
              f'Expected Result: {expected_result}')
