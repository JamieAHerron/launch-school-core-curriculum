'''
P:
Input: string
Output: boolean 

- Return True if string passed in is a palindrome
- False otherwise
- case-sensitive 
- all characters matter (not just alphabetical)

D:
- strings

A:
- compare string entered as argument to reversed version
- if equal, return True, if not, return False
- use slicing to reverse string 

'''

#Code:

def is_palindrome(string):
    return string == string[::-1]

# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)