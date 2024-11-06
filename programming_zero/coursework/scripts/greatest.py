def greatest(a: int | float, b: int | float, c: int | float) -> int | float | None:
    """
    This function finds the greatest of three numbers.

    :param a: The first number.
    :param b: The second number.
    :param c: The third number
    :return: The greatest of three numbers.
    """
    greatest_num = None
    # Here we catch the case where all parameters are of str type.
    if type(a) is str and type(b) is str and type(c) is str:
        print('a, b, and c are all of str type. Please, update your input')
    else:
        try:
            if b > a: # if 'b' is greater than 'a'
                greatest_num = b # then it is the greatest number
            else: # if not
                greatest_num = a # then 'a' is the greatest number
                if c > greatest_num: # if 'c' is greater than the greatest number
                    greatest_num = c # then 'c' is the greatest number

        except TypeError: # if we get a TypeError, e.g., when trying to compare str and int | float types
            print(f'At least one of a: {a}, b: {b}, c: {c} is not a number.')

    return greatest_num

if __name__ == "__main__":
    # Unit Tests
    test = [[5, 12, 8], [45, 1, 9], [3, 'a', 6], ['a', 'b', 'c'], [0.3, 0.9, 0.45]]
    # This list keeps the expected test results.
    expected_result = [12, 45, None, None, 0.9]
    # Will initiate an empty list, so I can keep my test results.
    result = []
    for i in range(len(test)):
        result.append(greatest(test[i][0], test[i][1], test[i][2]))

    if expected_result == result:
        print(f'Congratulations, your tests have passed. Result: {result}.')
    else:
        print(f'Sorry your tests have not passed. Result is different from expected results. '
              f'Have you updated your unit tests?\n',
              f'Result: {result}\n',
              f'Expected Result: {expected_result}')
