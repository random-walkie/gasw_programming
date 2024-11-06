def is_strong_password(password: str) -> bool:
    """
    Evaluates the strength of a password, i.e., that it contains:
    a) At least 8 characters
    b) At least one uppercase letter
    c) At least one lowercase letter
    d) At least one integer digit
    e) At least one special character: ! @ # $ % ^ & * ( )
    :param password: alphanumeric string.
    :return: True, if password is strong, otherwise False.
    """
    # First, I initialise a boolean variable
    password_strong = False
    try:
        # Then I am storing the special characters in a list
        special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
        # Then I am writing each condition in if - elif - else statements.
        # For each char in password
        if len(password) < 8:
            print('Length should be at least 8')

        elif not any(char.isupper() for char in password):
            print('Password should have at least one uppercase letter.')

        elif not any(char.islower() for char in password):
            print('Password should have at least one lowercase letter.')

        elif not any(char.isdigit() for char in password):
            print('Password should have at least one digit.')

        elif not any(char in special_chars for char in password):
            print('Password should have at least one special character from: "! @ # $ % ^ & * ( )"')

        else:
            print('Password strong')
            password_strong = True

    except TypeError:
        print('The input is not of str type.')

    return password_strong

if __name__ == "__main__":
    # Unit Tests
    test = ["password1!", "PASSWORD1!", "Password!", "Password1", "password1",
            "PASSWORD!", "Password", "Pass1!", "pass1", "", "Passw0rd!",
            "Secure123$", "Hello@2023", "MyPass#9!", "Str0ng!Pwd", 1111, ["Str0ng!Pwd"]]
    # This list keeps the expected test results.
    expected_result = [False, False, False, False, False, False, False, False,
                       False, False, True, True, True, True, True, False, False]
    # Will initiate an empty list, so I can keep my test results.
    result = []
    for i in range(len(test)):
        result.append(is_strong_password(test[i]))

    if expected_result == result:
        print(f'Congratulations, your tests have passed. Result: {result}.')
    else:
        print(f'Sorry your tests have not passed. Result is different from expected results. '
              f'Have you updated your unit tests?\n',
              f'Result: {result}\n',
              f'Expected Result: {expected_result}')
