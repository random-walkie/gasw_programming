def is_monotonic(string_of_digits: str) -> bool:
    """
    This function checks if a string of digits follow a monotonic pattern (consistently increasing / decreasing).
    :param string_of_digits:
    :return: Returns True if so, otherwise False.
    """
    monotonic = False
    warning_message = f'"string_of_digits": {string_of_digits} is not a string of digits (e.g., "12345").'
    if type(string_of_digits) is str: # Here I am checking if string_of_digits is indeed of type str
        try:
            # Using a while loop, to iterate over string of digits.
            # I have to have two stop points for this loop:
            # 1) Iterate over all digits (excluding first and last), and if it is monotonic, record it in a counter.
            # 2) If it isn't monotonic, I have to use a 'break' to leave the while cycle.
            counter = 1 # initialising a counter
            while counter < len(string_of_digits) - 1:
                if string_of_digits[counter - 1] <= string_of_digits[counter] <= string_of_digits[counter + 1] or \
                        string_of_digits[counter + 1] <= string_of_digits[counter] <= string_of_digits[counter - 1]:
                    counter += 1
                else:
                    break
            # If string_of_digits is of type string, but not a string of digits, e.g., 'abcs',
            # the code above will still run smoothly, even though it doesn't really make sense.
            # Therefore, I will try to typecast the variable to int. This will cause an error,
            # If string_of_digits is not a string of digits.
            int(string_of_digits)
        except ValueError:
            print(warning_message)
        # I have to add this else here, because I am not raising the error above, because I don't want to code
        # to stop. If I don't add this else, the program will still return True for inputs such as 'abcs'
        else:
            # If my counter has same length as string_of_digits - 1, this means my function is monotonic
            if counter == len(string_of_digits) - 1:
                monotonic =  True
    else:
        # In this block, I am catching the cases where string_of_digits is not of type str,
        # And alert the user if that is the case
        print(warning_message + f' It is of {type(string_of_digits)}')

    return monotonic

if __name__ == "__main__":
    # Unit Tests
    test = ['22456', '66521', '98612', 12343, ['12345'], 'abcs']
    # This list keeps the expected test results.
    expected_result = [True, True, False, False, False, False]
    # Will initiate an empty list, so I can keep my test results.
    result = []
    for i in range(len(test)):
        result.append(is_monotonic(test[i]))

    if expected_result == result:
        print(f'Congratulations, your tests have passed. Result: {result}.')
    else:
        print(f'Sorry your tests have not passed. Result is different from expected results. '
              f'Have you updated your unit tests?\n',
              f'Result: {result}\n',
              f'Expected Result: {expected_result}')
