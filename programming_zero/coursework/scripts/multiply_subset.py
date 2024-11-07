def multiply_subset(numbers: list, indices:list) -> int | float | None:
    """
    Multiplies numbers from a list at specified indices.
    :param numbers: A list of numbers (int | float).
    :param indices: A list of indices (int). Specify the elements in "numbers" to be multiplied.
    :return: A number, the multiplication result of the numbers at the specified indices, or None, if multiplication
    is not possible.
    """
    mult_result = 1 # This variable stores the multiplication values. Have to initialise with 1.
    tracker = False # Use this tracker to check if the code inside the try condition is successfully ran.
    try:
        # Below, iterate over the elements in "indices", and return the corresponding values from numbers.
        numbers_mult = [numbers[x] for x in indices]
        # Afterwards, iterate over the list containing the values to be multiplied
        # And add the multiplication result in mult_result
        for number in numbers_mult:
            mult_result *= number
            tracker = True
            # Setting tracker to True to indicate a successful code run inside the try condition
            # i.e.,didn't encounter any errors.

    # If a TypeError occurs, indicate this the user.
    except TypeError:
        print(f'"numbers" should be a list of integers or float. Check "numbers": {numbers}\n',
              f'"indices" should be a list of integers. Check "indices": {indices}')

    # If the indices given are out of range, indicate this to the user.
    except IndexError:
        print(f'Indices given are out of range, i.e, max(indices) = {max(indices)} >= len(numbers) = {len(numbers)}')

    # If the tracker is true, and mult_result is of the correct type, return the multiplication result
    if tracker and type(mult_result) is int or type(mult_result) is float:
        return mult_result
    # If not, return None
    else:
        return None

if __name__ == "__main__":
    # Unit Tests
    test = [[[2, 3, 4, 5,6, 7, 8], [0, 2, 4]],
            [[2, 3, 4, 5,6, 7, 8], [0, 2, 8]],
            [[2, 3, 4, 5,6, 7, 8], ['a', 'b', 'c']],
            [['a', 'b', 'c'], [0, 2]],
            [[1, 1, 1], [0, 1, 2]],
            [[0.1, 0.2, 0.5], [1, 2]]]
    # This list keeps the expected test results.
    expected_result = [48, None, None, None, 1, 0.1]
    # Will initiate an empty list, so can keep test results.
    result = []
    for i in range(len(test)):
        result.append(multiply_subset(test[i][0], test[i][1]))

    if expected_result == result:
        print(f'Congratulations, your tests have passed. Result: {result}.')
    else:
        print(f'Sorry your tests have not passed. Result is different from expected results. '
              f'Have you updated your unit tests?\n',
              f'Result: {result}\n',
              f'Expected Result: {expected_result}')
