#Write a function that takes a string as an argument and returns True if all parentheses in the string are properly balanced, False otherwise. To be properly balanced, parentheses must occur in matching '(' and ')' pairs.

def is_balanced(string):
    counter = 0
    for char in string:
        if char == '(':
            counter += 1
        elif char == ')':
            counter -= 1
            if counter < 0:
                return False
    
    return counter == 0

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True

# Note that balanced pairs must start with a (, not a ).