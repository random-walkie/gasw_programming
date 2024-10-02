def adds(a, b, c):
    """
    This function Receives three numbers, 
    adds them together, and returns the result.
    
    Parameters:
    a (int or float): The first number to add.
    b (int or float): The second number to add.
    c (int or float): The third number to add.
    
    Returns:
    int or float: The sum of a, b and c.
    """
    
    return a + b + c
    
# Main block to test the function
if __name__ == "__main__":
    result = adds(10, 4, 6.5)
    print(f"The sum of 10, 5, and 6 is: {result}")