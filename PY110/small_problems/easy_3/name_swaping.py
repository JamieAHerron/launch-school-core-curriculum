'''
Write a function that takes a string argument consisting of a first name, a space, and a last name. The function should return a new string consisting of the last name, a comma, a space, and the first name.

P:
input: string
output: string

- take string as argument
- string argument is first name, space, last name
- return new string
- new string is last name, comma, first name

D:
- strings

A:
- split string argument
- rebuild new string with f-string and return 
'''

#Code:

def swap_name(name):
    split_name = name.split(' ')

    return f'{split_name[1]}, {split_name[0]}'

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True