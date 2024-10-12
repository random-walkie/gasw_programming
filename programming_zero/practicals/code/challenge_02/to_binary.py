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
    
    else:
        binary_string = '' # initialise binary string
        div = 1 # initialise division tracker
        while div > 0: # while tracker is positive
           div = int(integer / 2) # divide integer by 2
           # append remainder to beginning of binary string
           binary_string = str(integer % 2) + binary_string
           # integer must now be set to div, so we can
           # advance in the loop
           integer = div
           
    return binary_string
        

# Main block to test the function
if __name__ == "__main__":
    integer = "2"
    result = to_binary(integer)
    print(f"The binary conversion is: {result}")
    