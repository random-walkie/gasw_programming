import sys
import random

# TODO: WRITE TESTS
def random_words(n_words):
    n_words = int(n_words)
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    word_list = []
    for word in range(n_words):
        word_len = random.randint(3, 10)
        char_list = []
        for char in range(word_len):
            char_idx = random.randint(0, len(alphabet)-1)
            char_list.append(alphabet[char_idx])
            
        word_list.append(''.join(char_list))
    
    return word_list

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print(f'Please, run the script correctly: "py random_words.py 10"')
    else:
        random_words = random_words(args[1])
        for word in random_words:
            print(word)

                