def calculate_percentage(part: int | float, total: int | float) -> float | None:
    """
    This function calculates a percentage, given a part, and a total.

    :param part: The part (numerator).
    :param total: The total (denominator)
    :return: A percentage, given a part and a total, or None, if not possible to calculate percentage.
    """
    percentage = None
    try: # try the following line of code
        percentage = float(part / total) * 100 # have to type case the division to float.
    except TypeError: # if we get a TypeError, print the following message
        print(f'The part: {part}, and/or total: {total} are not a number.')
    except ZeroDivisionError: # cannot divide by zero, so catching this error here.
        print('Cannot divide by zero')

    return percentage

if __name__ == "__main__":
    # Unit Tests
    test = [[30, 150], [0, 1], [1, 0], [0.1, 0.2], ['a', 'b'], [10, 'a']]
    # This list keeps the expected test results.
    expected_result = [20.0, 0.0, None, 50.0, None, None]
    # Will initiate an empty list, so I can keep my test results.
    result = []
    for i in range(len(test)):
        result.append(calculate_percentage(test[i][0], test[i][1]))

    if expected_result == result:
        print(f'Congratulations, your tests have passed. Result: {result}.')
    else:
        print(f'Sorry your tests have not passed. Result is different from expected results. '
              f'Have you updated your unit tests?\n',
              f'Result: {result}\n',
              f'Expected Result: {expected_result}')
