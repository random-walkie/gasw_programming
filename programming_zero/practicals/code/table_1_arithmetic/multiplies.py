def multiplies(list1, list2):
    """
    Receives list1 and list2, multiplies each element of each list
    and returns the sum of these two numbers.
    
    Parameters:
    list1 (list): The first list of float or int to multiply.
    list2 (list): The second list of float or int to multiply.
    
    Returns:
    int or float: The dot product of list1 and list2.
    """
    
    result1 = 1
    result2 = 1
    
    for i in list1:
        result1 = result1 * i
        
    for j in list2:
        result2 = result2 * j
        
    return result1 + result2
    
# Main block to test the function
if __name__ == "__main__":
  list1 = [1, 2, 3]
  list2 = [3, 2, 1]
  result = multiplies(list1, list2)
  print(f"The dot product of list1 and list2 is: {result}")