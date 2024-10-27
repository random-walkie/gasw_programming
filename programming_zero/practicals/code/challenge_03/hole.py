def create_square(r, root):
    """
    Generates a square (with side length equal to
    51) pattern of uniform characters (using #).
    
    Parameters:
    r (int): integer representing radius of circle. Deafult is 10.
    
    Returns:
    A nested list, representing a 2D array (square).
    Each element of the sub-lists represents an x-axis coordinate.
    Each sub-list represents the y-axis coordinate.
    E.g. [['#', '#', '#', ..., '#], ['#', '#', '#', ..., '#], ...] 
    """
    r = int(r)
    if r < root / 2 and r >=1:        
        square = []
        for i in range(root):
        # Append an empty sublist inside the list
            square.append([])
            for j in range(root):
                square[i].append('#')
                
    """ 
    BE VERY CAREFUL WHEN CREATING NESTED LISTS.
    INDEXING CAN GO VERY WRONG, E.G. THIS DOES NOT WORK:
    x_axis = []
    square = []
    for i in range(root):
      x_axis.append('#')
      square.append(x_axis)
     
    The list x_axis is defined outside the loop and is not re-initialized for each row.
    When x_axis.append('#') is called in the loop, it adds '#' to the same list each time.
    Consequently, when square.append(x_axis) is executed, it appends the same reference to x_axis for every row.
    As a result, all entries in square point to the same list x_axis. 
    Thus, after the loop, all rows in square will be identical and will contain root number of '#' characters.
    """
    
    return square
    
def get_coordinates(r, metric, root):
    """
    This function iterates over the nested list to get
    the coordinates of '#' characters to be replaced, to create the 'hole'.
    
    Parameters:
    square (nested list): A nested list, representing a 2D array (square).
    Each element of the sub-lists represents an x-axis coordinate.
    Each sub-list represents the y-axis coordinate.
    E.g. [['#', '#', '#', ..., '#], ['#', '#', '#', ..., '#], ...] 
    metric (str): The distance metric to use to determine the coordinates of the
    characters to be replaced by empty spaces to form the 'hole'.
    'euclidean' or 'manhattan' (default).
    root (int): integer representing the square dimension. Default is 51.
    
    Returns:
    A nested sub-list of x-y coordinates to be replaced    
    E.g., [[10, 15], [12, 13], ...]
    """
    replace_xy = [] # list to get coordinates to replace
    middle_x = middle_y = root//2 # finding middle x and y. Square, so this is OK.
    for y in range(root): # iterating over each y
        for x in range(root): # iterating over each x
            if metric == 'euclidean':
                dist = ((x - middle_x)**2 + (y - middle_y)**2)**0.5
            else:
                dist = abs(x - middle_x) + abs(y - middle_y)
            if dist < r:
                replace_xy.append([y, x]) # append the coordinates to replace
    
    return replace_xy

def hole(r=10, metric='manhattan', root=51):
    """
    Outputs a square (with side length equal to
    51) pattern of uniform characters (using #).
    In the centre of the square, there should
    be a circular "hole" with integer radius r.
    
    r (int): integer representing radius of circle. Deafult is 10.
    metric (str): The distance metric to use to determine the coordinates of the
    characters to be replaced by empty spaces to form a 'hole'.
    'euclidean' or 'manhattan' (default).
    root (int): integer representing the square dimension. Default is 51.
    
    Returns:
    square (nested list):A nested list, representing a 2D array (square).
    In the centre of the square, there should
    be a circular "hole" with integer radius r.
    """
    square = create_square(r=r, root=root)
    replace_xy = get_coordinates(r=r, metric=metric, root=root)
    
    for coord in replace_xy:
        square[coord[0]][coord[1]] = ' ' # replacing coordinates here
            
    return square 
    
if __name__ == "__main__":
    square = hole(r=10, metric='euclidean')
    for line in square:
        print(''.join(line)) # printing each line
    