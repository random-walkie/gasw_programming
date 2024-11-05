def adds(p1, p2):
    """
    Adds and returns generic list vectors p1 and p2.

    Parameters:
    p1 (list): The first list of numbers (represents a vector).
    p2 (list): The second list of numbers (represents a vector).

    Returns:
    list: A list with the added vectors (p1 + p2), if p1 and p2 have same length.
    None: If p1 and p2 have different sizes.
    """
    # First, create the output empty list
    list_of_sums = []
    if len(p1) == len(p2): # If lists have the same length
        for idx, value in enumerate(p1): # iterate over the indices, and the values of first list
            try: # implementing this within for loop, because we may be interested in getting partial lists
                list_of_sums.append(value + p2[idx]) # append the value of p1 after adding to the value of p2, at the same index
            except TypeError: # if we get a TypeError, e.g., when we try to add an integer to a string type
                continue # we skip iteration
        if len(list_of_sums) == 0: # This line is added to catch the case where there are no numbers at all in the list(s).
            print(f"TypeError: Check if p1: {p1} and p2: {p2} contain numbers at the same positions.")
            list_of_sums = None
    else: # If lists do not have the same length return None, as per instructions.
        list_of_sums = None

    return list_of_sums

if __name__ == "__main__":
    # Unit Tests
    # Will keep my test cases in a list of lists - each sub-list is a test case.
    test = [[5, 7, 3], [2, -1, 4], [3, 4, 5, 6], [1, 2, 'c'], [1, 2, 3, 'c'], ['a', 'b', 'c'], [0.1, 0.56, 3.14]]
    # This list keeps the expected test results.
    expected_result = [[10, 14, 6], [7, 6, 7], None, [6, 9], None, None, [5.1, 7.5600000000000005, 6.140000000000001]]
    # Will initiate an empty list, so I can keep my test results.
    result = []
    for i in range(len(test)):
        result.append(adds(test[0], test[i]))

    if expected_result == result:
        print(f'Congratulations, your tests have passed. Result: {result}.')
    else:
        # For example, if
        # test = [[5, 7, 3], [2, -1, 4], [3, 4, 5, 6], [1, 2, 'c'], [1, 2, 3, 'c'], 'a'],
        # and expected_result is not updated
        print(f'Sorry your tests have not passed. Result is different from expected results. '
              f'Have you updated your unit tests?\n',
              f'Result: {result}\n',
              f'Expected Result: {expected_result}')
