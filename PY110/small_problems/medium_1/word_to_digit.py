'''
P:
input: string
output: string

- take string as argument
- any 'number word' convert to corresponding digit
- string does not contain any punctuation
- return new string with digits instead of words for numbers

D:
- strings

A:
- create word to digit number dictionary (helper function?)
- split string argument
- iterate over list of words using comprehension
- pass eahc word to helper function
- return equivalent digit if number, return original word if not
- join list comprehension together and return it
'''

#Code:

WORDS_AND_DIGITS = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def check_if_num(word):
    #(LS Suggestion) return WORDS_AND_DIGITS.get(word, word)
    if word in WORDS_AND_DIGITS:
        return WORDS_AND_DIGITS[word]
    else:
        return word

def word_to_digit(string):
    word_lst = string.split()

    return ' '.join([check_if_num(word) for word in word_lst])

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True