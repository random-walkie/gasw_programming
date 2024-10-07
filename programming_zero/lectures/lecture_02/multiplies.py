# this function catches two arguments
def multiplies(lst_a, lst_b):
    """
    Receives list1 and list2, multiplies each element of list1, multiplies
    each element of list2. This results in two numbers. The function returns
    the sum of these numbers.
    """
    # Here we are declaring a variable that describes something
    product_a = 1
    for element in lst_a:
        product_a = product_a * element
    # If you want to check how the function is working
    # You can add a print statement, like the one below
    print("product_a = ", product_a)
    
    product_b = 1
    for element in lst_b:
        product_b = product_b * element
    print("product_b = ", product_b)
    
    # answer gets a changed value based on a an algorithm
    answer = product_a + product_b
    print(f"The value of the result is: {answer}")
    return answer

# This means if this script is called from PowerShell / Terminal     
if __name__ == "__main__":    
    # Test code (maybe messy to begin with)
    list_1 = [1, 2, 3] # 1 * 2 * 3 = 6
    list_2 = [4, 5, 2] # 4 * 5 * 2 = 40
    # if we keep function_name() it will crash python
    # this function must match the name of the
    # function implemented above, i.e. def multiplies()...
    # this function passes two arguments
    expected = 46
    result = multiplies(list_1, list_2) # 46
    if expected == result:
       print(f"Test passed")
    else:
        print(f"Test failed")

# These are not part of the script
# Python Primitives
an_integer  = 4 # positive, negative, 'whole'
a_float = 5.6535 # fractional (rational and irrational)
a_string = "h" # single character
another_string = "hello world" 
# inline comments
"""
'Block' comment.
"""