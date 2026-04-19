'''
P:
Input: string
Output: string

- swap the first and last letter of every word
- every word contains at least one letter
- only words and spaces contained within string
- no leading, trailing, or repeated spaces
- letter case remains the same

Questions:
- What if an empty string is entered as argument? Assume no empty strings

D:
- strings

A:
- take string as argument
- split string at whitespace
- iterate over word list, for loop
- if word is one letter, leave as is
- if word is two letters, reverse string
- if word is three or more letters, rebuild with slicing
    - assign first and last characters to variables
    - assign 'middle' of word to variables
    - rebuild word
- join list of rebuilt words back together
- return string
'''

def swap_word(word):
    if len(word) == 1:
        return word
    elif len(word) == 2:
        return word[::-1]
    else:
        first_letter = word[0]
        last_letter = word[-1]
        middle = word[1:-1]
        return last_letter + middle + first_letter


def swap(string):
    word_list = string.split()
    
    for i in range(len(word_list)):
        word_list[i] = swap_word(word_list[i])
    
    return ' '.join(word_list)

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True