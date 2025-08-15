#Write a function that takes a list of strings and returns a list of the same string values, but with all vowels (a, e, i, o, u) removed.

VOWELS = 'aeiouAEIOU'

def vowel_remover(item):
    return ''.join([char for char in item if char not in VOWELS])

def remove_vowels(lst):
    return [vowel_remover(item) for item in lst]

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