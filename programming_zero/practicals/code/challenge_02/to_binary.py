def to_binary(integer):
    """
    This function converts a positive 
    integer number to a binary string, using a for loop.
    
    Parameters:
    integer (int): Integer number.
    
    Return:
    string: The binary value corresponding to the input integer.
    """
    print(f"The input integer: {integer}")
    
    integer = int(integer) #  casting to integer, if input is string
    # if integer is negative, return error
    if integer < 0:
        return 'Please, enter a positive integer, e.g., 10'
    elif integer == 0:
        binary_string = '0'
    else:
        binary_string = '' # initialise binary string
        while integer > 0: # while number is positive
           # append remainder to beginning of binary string
           binary_string = str(integer % 2) + binary_string
           integer = int(integer / 2) # divide integer by 2

    return binary_string
        

# Main block to test the function
if __name__ == "__main__":
    integer = "0"
    result = to_binary(integer)
    print(f"The binary conversion is: {result}")
    