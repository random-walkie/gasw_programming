def powered_root(arg1, arg2):
    """
    Raises a supplied number arg1 to the power of arg2, then returns the
    square root of the result.
    
    Parameters:
    arg1 (int or float): The number to be raised.
    arg2 (int or float): The number representing the power.
    
    Returns:
    float: The square root of arg1 raised to the power of arg2.
    """
    
    return (arg1 ** arg2) ** (1/2)
    
# Main block to test the function
if __name__ == "__main__":
    arg1 = 16
    arg2 = 3
    result = powered_root(arg1, arg2)
    print(f"The squared root of {arg1}^{arg2} is: {result}")