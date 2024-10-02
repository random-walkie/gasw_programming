def squared(a):
    """
    Return the square of a supplied number.
    
    Parameters:
    a (int or float): The number to be squared.
    
    Returns:
    int or float: The square of the supplied number.
    """
    
    return a ** 2
    
# Main block to test the function
if __name__ == "__main__":
    a = -1.5
    result = squared(a)
    print(f"The square of {a} is: {result}")