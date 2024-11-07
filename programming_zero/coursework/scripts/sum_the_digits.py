def sum_the_digits(number: int) -> int | None:
    """
    This function calculates the sum of the digits of a number.
    :param number: An integer.
    :return: The sum of the digits of a number, or None
    """
    if isinstance(number, int):
        if len(str(number)) == 1:
            return number
        else:
            number = str(number)
            sum_digits = 0
            for digit in number:
                sum_digits += int(digit)
        return sum_digits
    else:
        print(f'Input must be an integer. Type of input is: {type(number)}')

if __name__ == "__main__":
    test = [1234, 4, 3459, 304132490, 'a', [1], [1, 2], {'a': 1, 'b': 2}, 1, 0, 1.1]
    # This list keeps the expected test results.
    expected_result = [10, 4, 21, 26, None, None, None, None, 1, 0, None]
    # Will initiate an empty list, so can keep test results.
    result = []
    for i in range(len(test)):
        result.append(sum_the_digits(test[i]))

    if expected_result == result:
        print(f'Congratulations, your tests have passed. Result: {result}.')

    else:
        print(f'Sorry your tests have not passed. Result is different from expected results. '
              f'Have you updated your unit tests?\n',
              f'Result: {result}\n',
              f'Expected Result: {expected_result}')
