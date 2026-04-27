'''
P:
input: string
output: list 

- take a string as an argument
- return a list of every substring
- each substring must begin with first letter 
- the list must be arranged from shortest to longest

D:
- list

A:
- use slicing with counter to grab substrings and append to empty list object
- iterate over string using range(1, len(string))
- slice string [:i]
- append slice to result list
- return result list
'''

#Code:
def leading_substrings(string):
    result = []

    for i in range(1, len(string) + 1):
        result.append(string[:i])
        
    return result

    #list comprehension is another option
    #return [string[:i] for i in range(1, len(string) + 1)]


# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])
