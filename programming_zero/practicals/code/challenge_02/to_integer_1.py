def to_integer_1(binary_string):
    """
    This function converts binary strings (up to 8 bits) into its
    corresponding integer value, using conditional logic.
    
    Parameters:
    binary_string (str): Binary string.
    
    Return:
    int: The integer value corresponding to the input binary string.
    """    
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
                
        integer = 0
        if binary_string[0] == "1":
            integer += 2**7
        
        if binary_string[1] == "1":
            integer += 2**6
        
        if binary_string[2] == "1":
            integer += 2**5
        
        if binary_string[3] == "1":
            integer += 2**4
        
        if binary_string[4] == "1":
            integer += 2**3
        
        if binary_string[5] == "1":
            integer += 2**2
        
        if binary_string[6] == "1":
            integer += 2**1
        
        if binary_string[7] == "1":
            integer += 2**0
                
        return integer

# Main block to test the function
if __name__ == "__main__":
    binary_string = "1010101"
    result = to_integer_1(binary_string)
    print(f"The input string: {binary_string}")
    print(f"The corresponding integer is: {result}")
    