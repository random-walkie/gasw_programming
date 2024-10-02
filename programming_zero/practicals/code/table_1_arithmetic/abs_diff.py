def abs_diff(a, b):
    """
    Receives two numbers and returns their difference as an absolute value.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    
    Returns:
    int or float: The absolute difference between a and b.
    """
    
    diff = a - b
    
    if diff < 0:
        diff = diff * (-1)
        
    return diff
    
 # Main block to test the function
if __name__ == "__main__":
    a = -9
    b = 10
    result = abs_diff(a, b)
    print(f"The absolute difference between {a} and {b} is: {result}")