def is_divisible_by(number: int | float, denominators: list) -> bool:
    """
    This function checks if a number is perfectly divisible by each element in a list of denominators.
    :param number: The number to check.
    :param denominators: The list of denominators to check.
    :return: True, if the number is perfectly divisible by each element in a list of denominators. False, otherwise.
    """
    is_divisible = False
    if type(number) is str and type(denominators[0]) is str and type(denominators[1]) is str:
        print('"number" and elements of "denominators" are of str type. Please, update your input.')
    try:
        remainder = 0
        # Check if number is inclusively within range
        for i in range(len(denominators)):
            # If yes, change value of return variable to True
            remainder += number % denominators[i]
        if remainder == 0:
            is_divisible = True
    except TypeError: # if we get a TypeError, e.g., when trying to compare str and int | float types
        print(f'At least one of "number": {number}, or "denominators": {denominators} is not a number.')

    return is_divisible

if __name__ == "__main__":
    # Unit Tests
    test = [[12, [3, 4]], [12, [5, 6]], [12, [3, 5]], ['a', [1, 10]], ['a', ['a', 'b']]]
    # This list keeps the expected test results.
    expected_result = [True, False, False, False, False]
    # Will initiate an empty list, so I can keep my test results.
    result = []
    for i in range(len(test)):
        result.append(is_divisible_by(test[i][0], test[i][1]))

    if expected_result == result:
        print(f'Congratulations, your tests have passed. Result: {result}.')
    else:
        print(f'Sorry your tests have not passed. Result is different from expected results. '
              f'Have you updated your unit tests?\n',
              f'Result: {result}\n',
              f'Expected Result: {expected_result}')