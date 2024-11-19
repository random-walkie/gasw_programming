def weather_advice(sunny: bool, rainy: bool, windy: bool, temperature: float) -> list:
    """
    This function evaluates weather conditions based on three boolean
    inputs: sunny, rainy, and windy, and one float temperature

    :param sunny: True, if it is sunny; False if it is not.
    :param rainy: True, if it is rainy; False if it is not.
    :param windy: True, if it is windy; False if it is not.
    :param temperature: Current temperature in Celsius. Must be a float.
    :return: It returns a list of advice strings based on these inputs using predefined
            advice strings provided in the script.
            If it is sunny, the function adds "Wear sun cream."
            If it is sunny and hot (temperature greater than 25°C), it also adds "It's hot and sunny!
            Eat some ice cream."
            If it is rainy, the function adds "Carry an umbrella." to the advice.
            If it is both rainy and windy, it adds "It's windy! Hold onto
            your umbrella tightly."
            Lastly, if it's
            windy (regardless of rain or sun), the
            function adds "Hold on to your hat."
    """
    # Check if variables are of the correct type
    if isinstance(sunny, bool) and isinstance(rainy, bool) and isinstance(windy, bool) and isinstance(temperature, float):
        # initialise an empty list of messages
        messages = []
        # if sunny is true
        if sunny:
            messages.append("Wear sun cream.")
        if sunny and temperature > 25.0:
            messages.append("It's hot and sunny! Eat some ice cream.")
        if rainy:
            messages.append("Carry an umbrella.")
        if rainy and windy:
            messages.append("It's windy! Hold onto your umbrella tightly.")
        if windy:
            messages.append("Hold on to your hat.")
        return messages
    # if variables are not of correct type, inform the user
    else:
        print(f'Input should be boolean values, True or False, or a float, for the temperature, e.g. 26.0',
              f'sunny is: {sunny}',
              f'rainy is: {rainy}',
              f'windy is: {windy}',
              f'temperature is: {temperature}'
              )

if __name__ == "__main__":
    test = [[True, False, False, 15.0],
            [True, False, False, 26.0],
            [False, True, False, 28.0],
            [False, True, True, 20.0],
            [False, False, True, 10.0],
            [True, True, True, 5.0],
            [True, True, True, 26.0]
            ]
    # This list keeps the expected test results.
    expected_result = [['Wear sun cream.'],
                       ['Wear sun cream.', "It's hot and sunny! Eat some ice cream."],
                       ['Carry an umbrella.'],
                       ['Carry an umbrella.', "It's windy! Hold onto your umbrella tightly.",
                        'Hold on to your hat.'],
                       ['Hold on to your hat.'],
                       ['Wear sun cream.',
                        'Carry an umbrella.',
                        "It's windy! Hold onto your umbrella tightly.",
                        'Hold on to your hat.'],
                       ['Wear sun cream.', "It's hot and sunny! Eat some ice cream.",
                        'Carry an umbrella.',
                        "It's windy! Hold onto your umbrella tightly.",
                        'Hold on to your hat.']
                       ]
    # Will initiate an empty list, so can keep test results.
    result = []
    for i in range(len(test)):
        result.append(weather_advice(test[i][0], test[i][1], test[i][2], test[i][3]))

    if expected_result == result:
        print(f'Congratulations, your tests have passed. Result: {result}.')

    else:
        print(f'Sorry your tests have not passed. Result is different from expected results. '
              f'Have you updated your unit tests?\n',
              f'Result: {result}\n',
              f'Expected Result: {expected_result}')
