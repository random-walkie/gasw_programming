def area_of_circle(radius):
    """
    This function assumes an approximate value PI = 3.142 (that is hard-coded inside the
    function), and calculates the area of a circle given the radius.

    Parameters:
    radius (int or float): The radius of the circle.

    Returns:
    float: The approximate area of the circle.
    None: If the radius is of the wrong type (i.e., not an integer or float).
    """
    pi = 3.142
    try: # try the following line of code
        area = pi * radius**2
    except TypeError: # if we get a TypeError, e.g., when radius is a string or a list, and not an integer or float.
        print(f'The radius is not a number: {radius}.')
        area = None

    return area


if __name__ == "__main__":
    # Unit Tests
    test = [0, 3, 7, 1, 'abc', [1, 2, 3], [1]]
    # This list keeps the expected test results.
    expected_result = [0.0, 28.278, 153.958, 3.142, None, None, None]
    # Will initiate an empty list, so I can keep my test results.
    result = []
    for i in range(len(test)):
        result.append(area_of_circle(test[i]))

    if expected_result == result:
        print(f'Congratulations, your tests have passed. Result: {result}.')
    else:
        print(f'Sorry your tests have not passed. Result is different from expected results. '
              f'Have you updated your unit tests?\n',
              f'Result: {result}\n',
              f'Expected Result: {expected_result}')
