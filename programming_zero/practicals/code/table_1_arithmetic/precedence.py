def precedence(a, b, c, d, e, f, g):
    """
    Receives 7 parameters a to g, which are arranged  according to the
    following expression:
    
    ((a + b * c) * d / (e - f)) + g
    
    Parameters:
    a to g (int or float): Numbers to be arranged into the expression above.
    
    Returns:
    int or float: The result of the expression above.
    """
    
    if e - f == 0:
        return "Impossible! e - f can't be 0."
     
    else:
        return (((a + b * c) * d) / (e - f)) + g
    
# Main block to test the function
if __name__ == "__main__":
    a = 2
    b = 3
    c = 4
    d = 5
    e = 6
    f = 7
    g = 8
    result = precedence(a, b, c, d, e, f, g)
    print(f"The result is: {result}")    