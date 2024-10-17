import sys

def distances(x1, y1, x2, y2):
    """
    This function calculates and outputs Euclidean distance and
    Manhattan distance, based on user-defined input coordinates and appropriate distance calculations.
    
    Parameters:
    x1, y1, x2, y2 (int): integers representing coordinates of two points.
    
    Returns:
    None.
    Prints the Euclidean and Manhattan distances.
    """
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    
    euclid_dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    print(f'The Euclidean distance is: {euclid_dist}')
    
    manhattan_dist = abs(x2 - x1) + abs(y2 - y1)
    print(f'The Manhattan distance is: {manhattan_dist}')
    

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 5:
        print(f'Please, run the script correctly: "py distances.py x1 y1 x2 y2"')
    
    distances(args[1], args[2], args[3], args[4])
    