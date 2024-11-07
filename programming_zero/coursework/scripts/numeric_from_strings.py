def numeric_from_strings(list_of_strings):
    """
    This function converts a list of strings representing numbers ('zero' to 'nine') into a single integer.
    :param list_of_strings: List of strings representing number (e.g., ['one', 'zero', 'two', 'nine', 'zero'])
    :return: Returns a single integer (e.g., 10290).
    """
    try:
        # Keeping the expected conversions in a dictionary - better than keeping in two separate lists
        strings_to_number = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
                             "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
        # Initialise an empty string
        converted_integer = ''
        # Iterate over the elements in list_of_strings, which have a corresponding key in the strings_to_number dictionary
        for x in list_of_strings:
            # Add each corresponding dictionary value to converted_integer
            converted_integer += strings_to_number[x]

        return int(converted_integer)
    # This error catches the case where list_of_strings contains a non-existing dictionary key (e.g., 'twenty')
    except KeyError:
        print('Please enter a list_of_strings representing numbers ("zero" to "nine")',
              f'Current input is: {list_of_strings}')

if __name__ == "__main__":
    # Unit Tests
    test = [['one', 'zero', 'two', 'nine', 'zero'],
            ['one', 'zero', 'two', 'nine', 'twenty'],
            ['a', 'b', 'c', 'd', 'e'],
            [1, 2, 3, 4, 5],
            ['six', 'seven', 'zero', 'three']]
    # This list keeps the expected test results.
    expected_result = [10290, None, None, None, 6703]
    # Will initiate an empty list, so can keep test results.
    result = []
    for i in range(len(test)):
        result.append(numeric_from_strings(test[i]))

    if expected_result == result:
        print(f'Congratulations, your tests have passed. Result: {result}.')

    else:
        print(f'Sorry your tests have not passed. Result is different from expected results. '
              f'Have you updated your unit tests?\n',
              f'Result: {result}\n',
              f'Expected Result: {expected_result}')
