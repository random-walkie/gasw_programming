def sort_to_types(arbitrary_ordered_types: list) -> list | None:
    """
    This function takes a list with elements of different types (strings, integers, and floats) and returns a new list
    where strings come first, followed by integers, and finally floats.
    :param arbitrary_ordered_types: A list with elements of different types (strings, integers, and floats).
    :return: Returns a new list where strings come first, followed by integers, and finally floats.
    """
    # Initialise return variable
    ordered_types = None
    if isinstance(arbitrary_ordered_types, list):
        allowed_types = (str, int, float)

        # Check if all elements are of allowed types
        if not all(isinstance(inst, allowed_types) for inst in arbitrary_ordered_types):
            print("Error: Input can only contain strings, integers, and floats.")

        else:
            # Separate elements by type
            strings = [x for x in arbitrary_ordered_types if isinstance(x, str)]
            integers = [x for x in arbitrary_ordered_types if isinstance(x, int)]
            floats = [x for x in arbitrary_ordered_types if isinstance(x, float)]

            # Store a flat list with strings first, then integers, and floats last.
            ordered_types = strings + integers + floats
    else:
        print(f'Error: Input is not a list: {arbitrary_ordered_types}')

    return ordered_types

if __name__ == "__main__":
    # Unit Tests
    test = [['banana', 5, 3.14, 'apple', 42, 2.71],
            [['test', 'test1', 1], 'a', 'b', 3.14, 123], [['test']], {'a': 5, 'b':6},
            [3.42, 23, 'scarecrow'],
            [3.42, 23]
            ]
    # This list keeps the expected test results.
    expected_result = [['banana', 'apple', 5, 42, 3.14, 2.71],
                       None, None, None,
                       ['scarecrow', 23, 3.42],
                       [23, 3.42]
                       ]
    # Will initiate an empty list, so can keep test results.
    result = []
    for i in range(len(test)):
        result.append(sort_to_types(test[i]))

    if expected_result == result:
        print(f'Congratulations, your tests have passed. Result: {result}.')

    else:
        print(f'Sorry your tests have not passed. Result is different from expected results. '
              f'Have you updated your unit tests?\n',
              f'Result: {result}\n',
              f'Expected Result: {expected_result}')
