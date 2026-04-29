'''
Modify the function from the previous exercise so it ignores non-alphabetic characters when determining whether it should uppercase or lowercase each letter. The non-alphabetic characters should still be included in the return value; they just don't count when toggling the desired case.

P:
input: string
output: string

- take string as argument
- return string with staggered capitalization 
- every other character starting from first should be capitalized 
- should also be followed by a lowercase or non-alphabetic characters
- non-alphabetic characters should not be counted when determining to switch between upper and lower case
'''

def staggered_case(string):
    #LS more refined solution using boolean flag/switch
    result = ''
    upper = True

    for char in string:
        if char.isalpha():
            if upper:
                result += char.upper()
            else:
                result += char.lower()
            upper = not upper
        else:
            result += char
    
    return result
    #My solution below:
    if string == '':
        return ''

    result = string[0].upper()
    selected_letter = string[0].upper()

    for char in string[1:]:
        if char.isalpha() and selected_letter.isupper():
            result += char.lower()
            selected_letter = char.lower()
        elif char.isalpha() and selected_letter.islower():
            result += char.upper()
            selected_letter = char.upper()
        else:
            result += char
        
    return result

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True