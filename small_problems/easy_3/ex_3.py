# Write a function that takes a short line of text and prints it within a box.

def print_in_box(message):
    horizontal_border = f'+-{'-' * len(message)}-+'
    vertical_border = f'| {' ' * len(message)} |'

    print(horizontal_border)
    print(vertical_border)
    print(f'| {message} |')
    print(vertical_border)
    print(horizontal_border)

print_in_box('To boldly go where no one has gone before.')
print_in_box('')