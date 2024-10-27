import sys
import random

def generate_bit_string(N):
    """
    This function generates a binary string (i.e., 0s and 1s) of user-specified
    length.

    Parameters:
    - N (int): integer representing the string length.

    Returns:
    - bit_string (str): a binary string with user-specified length.
    """
    # Initiate empty string
    bit_string  = ''
    for n in range(N):
        bit_string += str(random.randint(0, 1))
    return bit_string
    
def find_clusters(bit_string):
    """
    This function identifies all clusters of contiguous 1s in the generated bit string, 
    accounting for the circular nature
    of the string.
    
    Parameters:
    - bit_string (str): a binary string with user-specified length.
    
    Returns:
    - clusters (list of tuples): a list of tuples containing the (size, indices) of the 1s clusters.
    """
    clusters = []
    current_indices = []

    for idx, bit in enumerate(bit_string):
        if bit == '1':
            current_indices.append(idx)
        if bit == '0' and len(current_indices) > 0:
            clusters.append((len(current_indices), current_indices))
            current_indices = []

    if idx == len(bit_string)-1 and len(current_indices) > 0:
        clusters.append((len(current_indices), current_indices))            
        if bit_string[0] == bit_string[-1] and bit_string[-1] == '1' and ''.join(set(bit_string)) != '1':
            clusters.append((clusters[0][0] + clusters[-1][0], clusters[0][1] + clusters[-1][1]))
            clusters.pop(len(clusters)-2)
            clusters.pop(0)
        
    return clusters
    

def average_cluster_size(clusters):
    """
    This function calculates the average lenght per cluster.
    
    Parameters:
    - clusters (list of tuples): a list of tuples containing the (size, indices) of the 1s clusters.

    Returns:
    - avg_clstr (float): a float representing the average size (number of 1s) per cluster.
    """
    numerator = 0
    denominator = 0
    for cluster in clusters:
        numerator += cluster[0]
        denominator += 1
        
    avg_clstr = numerator / denominator
    
    return avg_clstr
        
    
def main():
    """
    Executes the program.
    """   
    # Check if command-line arguments were provided    
    args = sys.argv

    # If exactly one command-line argument is provided, use it as the number of words
    if len(args) == 2:
        # Convert the string arg to an int
        string_length = int(args[1])
        binary_string =  generate_bit_string(N=string_length)
        #binary_string = '111111'
        print(f'Bit string lenght = {len(binary_string)}.')
        print(binary_string)
        clusters = find_clusters(bit_string=binary_string)
        print(f'There are: {len(clusters)} cluster(s).')
        print(f'The clusters are:')
        for cluster in clusters:
            print(cluster[1])
        average_cluster = average_cluster_size(clusters)
        print(f'The average size per cluster is {average_cluster}.')
    else:
        # Provide usage information if the input argument list has the wrong length
        print("\nUSAGE: Please input the string length you require")
        print("E.G. <python3 clusters.py 50> (mac)")
        print("E.G. <py clusters.py 50> (win)")
        print("Yours sincerely\n" + "<" + args[0] + ">")
      
if __name__ == "__main__":
    main()
    
     
    