#Write a function that takes a string of integers as input and returns the number of substrings that result in an odd number when converted to an integer.

def solve(string):
    count = 0

    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = int(string[i:j])
            if substring % 2 == 1:
                count += 1
    
    return count

print(solve("1341")) # should return 7
print(solve("1357")) # should return 10