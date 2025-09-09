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

Modify the `word_sizes` function from the previous exercise to exclude non-letters when determining word size. For instance, the word size of `"it's"` is `3`, not `4`.

```Python
# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})
```

<details>
<summary>Show solution</summary>

```Python
def remove_non_letters(string):
    result = ""
    for char in string:
        if char.isalpha():
            result += char

    return result

def word_sizes(words):
    words_list = words.split()
    counts = {}

    for word in words_list:
        clean_word = remove_non_letters(word)

        clean_word_size = len(clean_word)
        if clean_word_size == 0:
            continue

        counts[clean_word_size] = counts.get(clean_word_size, 0) + 1

    return counts
```

The function `remove_non_letters` uses the built-in string method `isalpha` to detect alphabetic characters. It returns `True` when a character is a letter, `False` otherwise. When it returns `True`, we append the character to the `result` string.

The `word_sizes` function is very similar to the one we wrote for the previous exercise. However, this version strips out all the non-letters from each word.
</details>

## Problem 4

Given a string of words separated by spaces, write a function that swaps the first and last letters of every word.

You may assume that every word contains at least one letter, and that the string will always contain at least one word. You may also assume that each string contains nothing but words and spaces, and that there are no leading, trailing, or repeated spaces.

```Python
print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
```

<details>
<summary>Show solution</summary>

```Python
def swap(words):
    words_list = words.split()

    for idx in range(len(words_list)):
        words_list[idx] = swap_first_last_characters(words_list[idx])

    return ' '.join(words_list)

def swap_first_last_characters(word):
    if len(word) == 1:
        return word

    return word[-1] + word[1:-1] + word[0]
```

We start by splitting the input string into a list of words using the `split` method. We then iterate over the words in `words_list`, swapping the first and last character of each word with the `swap_first_last_characters` function.

The trickiest part is swapping the first and last characters. During iteration, `swap_first_last_characters` handles this. The function takes a `word` argument and returns the word with its first and last characters swapped. The swap is achieved by constructing a string composed of the last character (`word[-1]`), the middle characters (`word[1:-1]`), and the first character (`word[0]`). The function also includes a check for the case where the word is only a single character; in such cases, it directly returns the `word` since there's no need for a swap.
</details>

## Problem 5

Write a function that takes a string of digits and returns the appropriate number as an integer. You may not use any of the standard conversion functions available in Python, such as `int`. Your function should calculate the result by using the characters in the string.

For now, do not worry about leading `+` or`-` signs, nor should you worry about invalid characters; assume all characters are numeric.

```Python
print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True
```

<details>
<summary>Show solution</summary>

```Python
def string_to_integer(s):
    DIGITS = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }

    value = 0
    for char in s:
        value = (10 * value) + DIGITS[char]

    return value
```

This isn't the shortest or even the easiest solution to this problem, but it's straightforward. The big takeaway from this solution is our use of the `DIGITS` dictionary to convert string digits to their numeric values. This technique of using dictionaries to perform conversions is a common idiom that you can use in a wide variety of situations, often resulting in code that is easier to read, understand, and maintain.

The actual computation of the numeric value of string `s` is mechanical. We take each digit and add it to 10 times the previous value, which generates the desired result. For example, if we have 4, 3, and 1, we compute the result as:

```Python
initial value is 0
10 * 0 + 4 -> 4
10 * 4 + 3 -> 43
10 * 43 + 1 -> 431
```
</details>

## Problem 6

In the previous exercise, you developed a function that converts simple numeric strings to integers. In this exercise, you're going to extend that function to work with signed numbers.

Write a function that takes a string of digits and returns the appropriate number as an integer. The string may have a leading`+` or`-` sign; if the first character is a `+`, your function should return a positive number; if it is a `-`, your function should return a negative number. If there is no sign, return a positive number.

You may assume the string will always contain a valid number.

You may not use any of the standard conversion functions available in Python, such as `int`. You may, however, use the `string_to_integer` function from the previous exercise.

```Python
print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True
```
<details>
<summary>Show solution</summary>

```Python
def string_to_integer(s):
    DIGITS = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }

    value = 0
    for char in s:
        value = (10 * value) + DIGITS[char]

    return value

def string_to_signed_integer(string):
    match string[0]:
        case '-':
            return -string_to_integer(string[1:])
        case '+':
            return string_to_integer(string[1:])
        case _:
            return string_to_integer(string)
    

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True
```

We've opted to reuse the `string_to_integer` function from the previous exercise. Why waste effort reinventing the wheel? (Oh, wait. That's exactly what we're doing, isn't it?)

This solution is reasonably straightforward: it simply looks at the first character of `string`. If the character is a `-`, the negative of the number represented by the rest of the string is returned. If it is not a `-`, it returns the value of the rest of the string as a number, skipping over a leading `+` if present.

To obtain the remainder of the string after a leading `+` or `-`, we use Python's string slicing syntax.
</details>