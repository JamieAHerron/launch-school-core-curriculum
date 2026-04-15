'''
USING all() NAME VALIDATOR PROBLEM

Here’s a fresh version of that problem you can save and revisit later:

You’re writing a simple “name validator” in Python.

Requirements:

- A valid name:
  - may contain one or more words separated by single spaces (e.g., `"Jamie"`, `"Jamie Herron"`, `"Jamie Alexander Herron"`),
  - each word must contain only alphabetic characters (`A`–`Z` or `a`–`z`),
  - leading and trailing whitespace should be ignored.
- An invalid name:
  - contains digits or other non-letter characters (e.g., `"Jamie123"`, `"Jamie!"`),
  - or is only whitespace (e.g., `"   "`).

Write a short snippet that:

- reads a string stored in `name`,
- decides whether it’s a valid name according to the rules above,
- prints `"Valid name"` or `"Invalid name"`.

Try to use these tools in your solution:

- `strip`
- `split`
- `all`
- `isalpha`

Example starting point:
'''

name = "  Jamie Herron  "

# your validation logic here

