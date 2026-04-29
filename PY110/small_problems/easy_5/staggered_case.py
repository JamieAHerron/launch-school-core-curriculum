'''
P: 
input: string
output: string (staggered capitalization scheme)

- take string as argument
- return string with staggered capitalization 
- every other character starting from first should be capitalized 
- should also be followed by a lowercase or non-alphabetic characters
- non-alphabetic characters should not be changed BUT should be counted when determining to switch between upper and lower case

D:
- strings

A:
- convert to lowercase 
- create empty result string 
- iterate over lowercase string
- if char is alphabetical and odd index, make uppercase
- else keep lowercase (if alphabetical)
- or keep as-is (if not alphabetical)
'''

#code:

def staggered_case(string):
    lowercase_string = string.lower()
    result = ''

    for index, char in enumerate(lowercase_string, 1):
        if index % 2 == 1:
            result += char.upper()
        else:
            result += char
    
    return result


string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True