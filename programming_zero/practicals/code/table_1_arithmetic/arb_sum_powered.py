def arb_sum_powered(list1):
    """
    Receives a list. The sum of the first n - 1 elements is raised to the
    power of the nth element.
    
    Paramters:
    list1 (list): The list of int or floats.
    
    Returns:
    int or float: The sum of the first n - 1 elements raised to the
    power of the nth element.
    """
    
    list_sum = 0 
    for i in range(len(list1)-1): # len(list1)-1 is 3, and range will start from 0, so 0, 1, 2.
        list_sum += list1[i]
        
    return list_sum ** list1[len(list1)-1] 
    
# Main block to test the function
if __name__ == "__main__":
    list1 = [1, 2, 3, 2]
    result = arb_sum_powered(list1)
    print(f"The result is: {result}")