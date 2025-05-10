#Write a function that takes two strings as arguments, determines the length of the two strings, and then returns the result of concatenating the shorter string, the longer string, and the shorter string once again. You may assume that the strings are of different lengths.

# These examples should all print True

def short_long_short(string_1, string_2):
    
    string_1_length = len(string_1)
    string_2_length = len(string_2)

    if string_1_length < string_2_length:
        return string_1 + string_2 + string_1
    else:
        return string_2 + string_1 + string_2

print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")