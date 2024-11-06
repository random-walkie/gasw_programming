def is_vowel(character):
    """
    Checks if a given character is a vowel.
    :param character: A string, representing a character.
    :return: True, if character is a vowel, otherwise False.
    """
    vowel_bool = False # Initiate the variable to be returned
    try:
        vowels = ['a', 'e', 'i', 'o', 'u'] # store the vowels in this list
        if character.lower() in vowels: # using lower() method to lowercase the values
            vowel_bool = True
    except AttributeError: # lower() method is a str attribute, so it will fail for other types
        print(f'The input {character} is not of type str.')

    return vowel_bool

if __name__ == "__main__":
    # Unit Tests
    test = ["a", "b", "e", "f", "1", "A", "B", "E", 1, [1, 2, 3], 'as', 'AA']
    # This list keeps the expected test results.
    expected_result = [True, False, True, False, False, True, False, True, False, False, False, False]
    # Will initiate an empty list, so I can keep my test results.
    result = []
    for i in range(len(test)):
        result.append(is_vowel(test[i]))

    if expected_result == result:
        print(f'Congratulations, your tests have passed. Result: {result}.')
    else:
        print(f'Sorry your tests have not passed. Result is different from expected results. '
              f'Have you updated your unit tests?\n',
              f'Result: {result}\n',
              f'Expected Result: {expected_result}')
