def is_even_and_positive(number):
    """
    This function checks if a number is even and positive.
    :param number: an integer.
    :return: True, if number is both even and positive. False, otherwise.
    """
    even_and_positive = False
    try:
        # if number is even, the remainder of division by 2 should be 0
        # here the condition is it should be positive too.
        if number % 2 == 0 and number > 0:
            even_and_positive = True
    except TypeError: # if we get a TypeError, e.g., when trying to compare str and int | float types
        print(f'"number": {number} is not a number.')

    return even_and_positive

if __name__ == "__main__":
    # Unit Tests
    test = [10, 1, 2, 3, 4, 3041394103, 239392, -2, 0.45, 'abc', 'a', [1, 2, 3]]
    # This list keeps the expected test results.
    expected_result = [True, False, True, False, True, False, True, False, False, False, False, False]
    # Will initiate an empty list, so I can keep my test results.
    result = []
    for i in range(len(test)):
        result.append(is_even_and_positive(test[i]))

    if expected_result == result:
        print(f'Congratulations, your tests have passed. Result: {result}.')
    else:
        print(f'Sorry your tests have not passed. Result is different from expected results. '
              f'Have you updated your unit tests?\n',
              f'Result: {result}\n',
              f'Expected Result: {expected_result}')
