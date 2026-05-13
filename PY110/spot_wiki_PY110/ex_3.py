'''
Write a function that takes two strings as input, full_text and search_text, and returns the number of times search_text appears in full_text.

- take two strings as argument (full_text and search_text)
- initialize count variable to 0
- initialize search_len variable to length of search_text
- iterate over range that goes up to length of full text minus search text plus one
- for each iteration, use slicing to ask if full_text[i:i + search_len] is equal to search_text
- if it is equal, increment count by one
- once loop is complete, return count variable 
'''

def solution(full_text, search_text):
    count = 0
    search_len = len(search_text)

    for i in range(len(full_text) - search_len + 1):
        if full_text[i:i + search_len] == search_text:
            count += 1
    
    return count

print(solution('abcdeb','b')) # should return 2 since 'b' shows up twice
print(solution('aaabbbcccc', 'bbb')) # should return 1
print(solution('aaabbbbcccc', 'bbb')) # should return 2