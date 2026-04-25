'''
Write a function that takes a string as an argument and returns True if all parentheses in the string are properly balanced, False otherwise. To be properly balanced, parentheses must occur in matching '(' and ')' pairs.

P:
input: string
output: boolean

- takes string as argument
- returns true if all parentheses are balanced
- returns false is parentheses not balanced
- balanced means parentheses must occur in matching pairs 

D:
- strings

A:
- count number of open brackets
- count number of closed brackets
- if the number of open and closed match then return True
- return False otherwise 

'''

#Code:

def is_balanced(string):
    balance = 0

    for char in string:
        if char == '(':
            balance += 1
        if char == ')':
            balance -= 1
        if balance < 0:
            return False
    
    return balance == 0
    


print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True