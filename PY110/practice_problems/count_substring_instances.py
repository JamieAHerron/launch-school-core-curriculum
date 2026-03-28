# Write a function that takes two strings as input, full_text and search_text, and returns the number of times search_text appears in full_text.

def solution(full_text, search_text):
    count = 0
    start = 0

    while True:
        pos = full_text.find(search_text, start)
        if pos == -1:
            break
        else: # else not needed due to break above
            count += 1
            start = pos + 1
    
    return count

print(solution('abcdeb','b')) # should return 2 since 'b' shows up twice
print(solution('aaabbbcccc', 'bbb')) # should return 1
print(solution('aaabbbbcccc', 'bbb')) # should return 2