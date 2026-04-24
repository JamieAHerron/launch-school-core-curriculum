'''
Write a function that takes a string, doubles every character in the string, then returns the result as a new string.

P:
input: string
output: string

- take string as argument
- double every character in string
- return new string

D:
- strings

A:
- initialize result varaible to empty string
- iterate over string argument
- for each character, multiply by 2 and add to result string
- return result string

'''

def repeater(string):
    result = ''

    for char in string:
        result += char * 2
    
    #LS suggestion
    # return ''.join(char * 2 for char in string)
    
    return result

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True