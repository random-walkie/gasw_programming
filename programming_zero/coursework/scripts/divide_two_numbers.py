def divide_two_numbers(m: int | float, n: int | float) -> float | str:
    """
    This function divides two numbers and returns the quotient.
    Handles division by zero by returning a string “NAN”.

    :param m: The numerator.
    :param n: The denominator.
    :return: The quotient, if two numbers are given; "NAN" string, otherwise.
    """
    quotient = "NAN"
    try: # try the following line of code
        quotient = float(m / n)  # have to type case the division to float.
    except TypeError: # if we get a TypeError, print the following message
        print(f'The numerator: {m}, and/or denominator: {n} are not a number.')
    except ZeroDivisionError: # cannot divide by zero, so catching this error here.
        print('Cannot divide by zero')

    return quotient

if __name__ == "__main__":
    # Unit Tests
    test = [[10, 2], [10, 0], [1, 0], [0.1, 0.2], ['a', 'b'], [10, 'a']]
    # This list keeps the expected test results.
    expected_result = [5.0, 'NAN', 'NAN', 0.5, 'NAN', 'NAN']
    # Will initiate an empty list, so I can keep my test results.
    result = []
    for i in range(len(test)):
        result.append(divide_two_numbers(test[i][0], test[i][1]))

    if expected_result == result:
        print(f'Congratulations, your tests have passed. Result: {result}.')
    else:
        print(f'Sorry your tests have not passed. Result is different from expected results. '
              f'Have you updated your unit tests?\n',
              f'Result: {result}\n',
              f'Expected Result: {expected_result}')
