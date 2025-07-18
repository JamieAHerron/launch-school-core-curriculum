separator = '-'

# proper usage with one argument
names = ['Bob', 'Jo', 'Kim']
result = separator.join(names)
print(result)                           # Bob-Jo-Kim

# calling with no arguments
# result = separator.join()             # raises TypeError

# calling with multiple arguments
# result = separator.join('Bob', 'Jo')  # raises TypeError