'''
P:
input: string
output: list

- take string as argument
- return list of palindromic substrings
- substring list should be sorted by order of appearance in string
- duplicate substrings should be included 
- substrings are case-sensitive 
- single characters are not palindromes
- if no palindromes found, return empty list

D:
- lists

A:
- carry out the same method from previous exercises gathering all substrings
- filter list of substrings for substrings that are palindromes
- return filtered list of palindromes
'''
def is_palindrome(substring):
    return substring == substring[::-1] and len(substring) > 1

def leading_substrings(string):
    return [string[:idx + 1] for idx in range(len(string)) if is_palindrome(string[:idx + 1])]

def palindromes(string):
    result = []

    for idx in range(len(string)):
        start_at_index = string[idx:]
        for substring in leading_substrings(start_at_index):
            result.append(substring)
    
    return result

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True