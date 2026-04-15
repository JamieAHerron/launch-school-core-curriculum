'''
P:
Input: string
Output: boolean

- return True if string passed is palindrome
- False otherwise
- must be case-INsensitive
- ignore non-alphanumeric characters

D:
- strings

A:
- if string entered is alphanumeric, simply change case to lower or upper and proceed with comparing to reversed slice
- If string is not alphanumeric, rebuild string ignoring all non-alphanumeric characters 
    - rebuild string 
    - ask, is alphanumeric? 
    - if yes, add to string construction
    - if no, continue
- compare newly built string to reversed slice
- return True or False according to palindromic rules
'''
#Code:

def is_real_palindrome(string):
    new_string = ''.join([char.lower() for char in string if char.isalnum()])
    
    return new_string == new_string[::-1]

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True