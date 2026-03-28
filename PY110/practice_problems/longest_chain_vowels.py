#Write a function that takes a lowercase string as input and returns the length of the longest substring that consists entirely of vowels (a, e, i, o, u).

def solve(string):
    sub_count = 0
    final_count = 0
    vowels = 'aeiou'

    for letter in string.lower():
        if letter in vowels:
            sub_count += 1
            if sub_count > final_count:
                final_count = sub_count
        else:
            sub_count = 0
    
    return final_count


print(solve("roadwarriors")) # should return 2
print(solve("suoidea")) # should return 3