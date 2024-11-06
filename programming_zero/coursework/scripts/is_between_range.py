def is_between_range(number: int | float, range: list) -> bool:
    """
    This function checks if a number is inclusively within a range.
    :param number: The number to check.
    :param range: The range to compare the number with.
    :return: True, if the number is inclusively within a range. False, otherwise.
    """
    between_range = False # initialising return variable to False
    try:
        # Check if number is inclusively within range
        if range[0] <= number <= range[1]:
            # If yes, change value of return variable to True
            between_range = True
    except TypeError: # if we get a TypeError, e.g., when trying to compare str and int | float types
        print(f'At least one of number: {number}, or range: {range} is not a number.')

    return between_range

if __name__ == "__main__":
    # Unit Tests
    test = [[5, [1, 10]], [50, [1, 50]], [5, [10, 1]], ['a', [1, 10]]]
    # This list keeps the expected test results.
    expected_result = [True, True, False, False]
    # Will initiate an empty list, so I can keep my test results.
    result = []
    for i in range(len(test)):
        result.append(is_between_range(test[i][0], test[i][1]))

    if expected_result == result:
        print(f'Congratulations, your tests have passed. Result: {result}.')
    else:
        print(f'Sorry your tests have not passed. Result is different from expected results. '
              f'Have you updated your unit tests?\n',
              f'Result: {result}\n',
              f'Expected Result: {expected_result}')
