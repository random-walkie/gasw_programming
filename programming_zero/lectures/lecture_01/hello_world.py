# Topic is to learn how to run a script
# from the command line
def accelerate(x, y, z):
    return [x + 1, y + 1, z + 1]
    
def main():
    a = 1
    b = 2
    c = 3
    
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)
    
    print("Hello World")
    
    c = c * b
    print('c = ', c)
    
    lst = accelerate(a, b , c)
    print(lst)
    
if __name__ == "__main__":
    
    main()

# __main__ has nothing to do with the main() function.
# E.g., you cna also write:
#def test():
#    print("Hello World")
#    
#if __name__ == "__main__":
#    test()
