def is_even(number: int) -> bool:
    """
    This function checks if a number is even.
    :param number: an integer.
    :return: True, if number is even. False, otherwise.
    """
    even = False
    try:
        if number % 2 == 0:
            even = True
    except TypeError: # if we get a TypeError, e.g., when trying to compare str and int | float types
        print(f'"number": {number} is not a number.')

    return even

if __name__ == "__main__":
    # Unit Tests
    test = [10, 1, 2, 3, 4, 3041394103, 239392, 'abc', 'a', [1, 2, 3]]
    # This list keeps the expected test results.
    expected_result = [True, False, True, False, True, False, True, False, False, False]
    # Will initiate an empty list, so I can keep my test results.
    result = []
    for i in range(len(test)):
        result.append(is_even(test[i]))

    if expected_result == result:
        print(f'Congratulations, your tests have passed. Result: {result}.')
    else:
        print(f'Sorry your tests have not passed. Result is different from expected results. '
              f'Have you updated your unit tests?\n',
              f'Result: {result}\n',
              f'Expected Result: {expected_result}')
