def einstein():
    # Exercise 5 of Challenge 1
    physicist = "Albert Einstein" # Exercise 6: DRY
    
    string1 = "We cannot solve our problems with the same thinking " \
              "we used when we created them.\n\t\t\t\t\t\t\t\t" + \
              physicist
              
    string2 = "Learn from yesterday, live for today, hope for tomorrow. " \
              "The important thing is not to stop questioning." \
              "\n\t\t\t\t\t\t\t\t\t\t\t" + \
              physicist
    
    string3 = "It's not that I'm so smart, it's " \
              "just that I stay with problems longer." \
              "\n\t\t\t\t\t\t\t" + \
              physicist
     
    # Exercise 7: Word counting
    # Here: len(string1.split()) - len(physicist.split())
    # I am removing the 'Albert Einstein' word count, from the quote word count.
    print(string1 + "\n" + str(len(string1.split()) - len(physicist.split())) + " words long")
    print(string2 + "\n" + str(len(string2.split()) - len(physicist.split())) + " words long")
    print(string3 + "\n" + str(len(string3.split()) - len(physicist.split())) + " words long")
    
    # Exercise 8: Einstein's equation
    # First transform physicist to lower case
    physicist_lower = physicist.lower()
    # Now remove whitespace
    physicist_lower = physicist_lower.replace(" ", "")
    # Now get unique letters
    unique_letters = []
    # iterate over each letter
    for letter in physicist_lower:
        # if letter is not in the empty list
        if letter not in unique_letters:
            # append the letter to list
            unique_letters.append(letter)
    
    # start a counter for maximum count
    max_count = 0
    # start a counter for current letter count
    current_count = 0
    # iterate over unique letters
    for i in unique_letters:
        # iterate over all letters
        for j in physicist_lower:
            # if unique letter is equal to letter
            if i == j:
                # append to counter
                current_count += 1
        if current_count > max_count:
            max_count = current_count
            eqn = i
        # must re-set current counter for next letter
        current_count = 0
        
    # set mass
    mass = 90
    # set speed of light
    c = 3e8
    # calculate e = mc^2
    number = mass * (c ** 2)
    
    string4 = eqn + " = mc^2"
    print(f"result: {eqn}")
    print( "According to the equation " + string4 + f", a famous physicist has a mass <{mass}>" +
    f" and, therefore, energy <{number}>")
    

if __name__ == "__main__":
    einstein()