# Study Guide (Easy Problems)

Below is a list of problems I found tricky on the first pass. I have listed them below with a solution and any relevant notes to help with further study.

## Problem 1

Write a function that returns True if the string passed as an argument is a palindrome, or False otherwise. This time, however, your function should be case-insensitive, and should ignore all non-alphanumeric characters. 

```Python
print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True
```

<details>
<summary>Show solution</summary>

```Python
def is_real_palindrome(s):
    cleaned_string = ''
    for char in s:
        if char.isalnum():
            cleaned_string += char.casefold()

    return is_palindrome(cleaned_string)
```

The solution uses Python's built-in str.isalnum method to check whether a character is alphanumeric -- a letter (A-Z, a-z) or a number (0-9). Note that isalnum recognizes non-ASCII letters and digits. If you don't want to include those characters, you should write:

```Python
if char.isalnum() and char.isascii():

#instead of

if char.isalnum():
```
</details>

## Problem 2



