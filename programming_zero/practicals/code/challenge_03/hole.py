# TODO: RE-WRITE CODE; THIS FUNCTION DOES NOT FOLLOW PEP8 PRINCIPLES
def hole(r, metric = 'manhattan'):
    """
    Generates and outputs a square (with side length equal to
    51) pattern of uniform characters (using #) to the console. In the centre of the square, there should
    be a circular "hole" with integer radius r.
    
    Parameters:
    r (int): integer representing radius of circle.
    metric (str): string representing the distance metric to use. 'euclidean' or 'manhattan' (default).
    
    Returns:
    None.
    Prints string: a square, string with pattern '#'.
    """
    root = 51
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
        
        replace_xy = [] # list to get coordinates to replace
        middle_x = root//2 # finding middle x
        middle_y = root//2 # finding middle y
        for y in range(root): # iterating over each y
            for x in range(root): # iterating over each x
                if metric == 'euclidean':
                    dist = ((x - middle_x)**2 + (y - middle_y)**2)**0.5
                else:
                    dist = abs(x - middle_x) + abs(y - middle_y)
                if dist < r:
                    replace_xy.append([y, x]) # append the coordinates to replace
        
        for coord in replace_xy:
            square[coord[0]][coord[1]] = ' ' # replacing coordinates here
        
        for line in square:
            print(''.join(line)) # printing each line
    
if __name__ == "__main__":
    hole(10, 'euclidean')
    