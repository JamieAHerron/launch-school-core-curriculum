def multiply(left, right):
    return left * right

def question(prompt):
    entry = float(input(prompt))
    return entry

first_number = question('Enter first number: ')
second_number = question('Enter second number: ')
product = multiply(first_number, second_number)

print(f'{first_number} * {second_number} = {product}')