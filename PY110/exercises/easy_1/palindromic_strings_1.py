'''
Write a function that returns True if the string passed as an argument is a palindrome, False otherwise. A palindrome reads the same forwards and backwards. For this problem, the case matters and all characters matter.

Input: string
Output: Boolean (True or False)

Explicit requirements:
    - Take a string as input
    - Evaluate if the string is a palindrome 
    - All characters in the string must be evaluated
    - Out True or False as a boolean (is/is not a palindrome)

Implicit requirements:
    - Do I assume the input will always be a string?
    - How to deal with empty strings/ non-string types?

Data structure:
    - string object (strings are iterable can use slicing)

Algorithm:
    - Compare input string with reversed version
    - Use slicing to create reversed version of input string 
    - if they match return True
    - if not return False
    - Use if statement to evaluate True or False
'''

def is_palindrome(string):
    if isinstance(string, str) and string != '':
        return string == string[::-1]
    else:
        return False

#LS refined solution

# def is_palindrome(string):
#     return isinstance(string, str) and string != '' and string == string[::-1]

# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)

#outliers
print(is_palindrome(5))
print(is_palindrome(''))