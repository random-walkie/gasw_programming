def to_integer_2(binary_string):
    """
    This function converts binary strings (up to 8 bits) into its
    corresponding integer value, using a for loop.
    
    Parameters:
    binary_string (str): Binary string.
    
    Return:
    int: The integer value corresponding to the input binary string.
    """
    print(f"The input string: {binary_string}")
    
    # The script should handle binary strings with 
    # a maximum length of 8 bits (or less).
    string_length = len(binary_string)
    bits = 8
    if string_length > bits:
        return f"Stop! The binary string needs to be {bits} bits"
    
    else:
        # Pad the string with additional bits, if the length of 
        # the string is less than 8
        if string_length < bits:
            binary_string = "0" * (bits - string_length) + binary_string
        # Below I am getting the exponent to calculate the 
        # integer value corresponding to the binary number.
        # E.g. 111:
        # 1 x 2 x 2 (or 2^2) = 4
        # 1 x 2 (or 2^1) = 2
        # 1 x 1 (or 2^0) = 1
        # So 111 -> 4 + 2 + 1 = 7
        exponent = len(binary_string) - 1 # need to subtract 1 to lenght, because we have exponent 0
        integer = 0
        # Now iterate over each character in the string
        for char in binary_string:
            # Then calculate as explained above
            integer += int(char) * 2**exponent
            # Need to subtract 1 to the exponent in each iteration
            exponent -= 1
                
        return integer

# Main block to test the function
if __name__ == "__main__":
    binary_string = "011"
    result = to_integer_2(binary_string)
    print(f"The result is: {result}")
    