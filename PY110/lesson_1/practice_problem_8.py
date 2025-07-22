#Given the following string, create a dictionary that represents the frequency with which each letter occurs. The frequency count should be case-sensitive:

statement = "The Flintstones Rock"

result = {}
statement = statement.replace(' ', '')
for char in statement:
    result[char] = result.get(char, 0) + 1

print(result)