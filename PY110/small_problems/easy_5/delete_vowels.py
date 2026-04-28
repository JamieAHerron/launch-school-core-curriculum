'''
P:
input: list (of strings)
output: list (of strings with vowels removed)

D:
- list/ strings

A:
***Helper function***
- create empty result string
- iterate over string
- build new string omitting 'aeiou'
- should not be case sensitive 
***Main function***
- list comprehension 
- iterate over strings in list
- pass each string into helper function
- return list comprehension 
'''
def vowel_finder(string):
    result = ''

    for char in string:
        if char.lower() not in 'aeiou':
            result += char
    
    return result

def remove_vowels(word_list):

    return [vowel_finder(word) for word in word_list]




# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True