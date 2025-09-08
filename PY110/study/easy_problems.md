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

Write a function that takes a string consisting of zero or more space-separated words and returns a dictionary that shows the number of words of different sizes.

Words consist of any sequence of non-space characters.

```Python
# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})
```

<details>
<summary>Show solution</summary>

```Python
def word_sizes(words):
    result = {}
    word_list = words.split()

    for word in word_list:
        result[len(word)] = result.get(len(word), 0) + 1
    
    return result
```

`str.split()` Behavior

In your code, you use `words.split(' ')`. This splits the string specifically on a single space character. A more general and often-preferred approach is to use `words.split()` with no arguments.

When called without arguments, `split()` splits on any sequence of whitespace (one or more spaces, tabs, newlines, etc.) and discards empty strings. For example:

`'hello world'.split(' ')` results in `['hello', '', '', 'world']`
`'hello world'.split()` results in `['hello', 'world']`

Using `split()` makes your function more robust to variations in spacing within the input string.

Why the following is not necessary:
```Python
if words == '':
    return {}
```

If you use `words.split()` as suggested above, this check becomes unnecessary. This is because `''.split()` returns an empty list `[]`.

When your for loop attempts to iterate over an empty list, the loop's body will not execute at all. The function will then move to the next line, return result, returning the result dictionary in its initial empty state, `{}`. This means your code will naturally handle the empty string case without needing a separate conditional check.
</details>

## Problem 3


