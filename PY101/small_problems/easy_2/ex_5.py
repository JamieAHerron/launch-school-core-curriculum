#Write a program that prompts the user for two positive numbers (floating-point), then prints the results of the following operations on those two numbers: addition, subtraction, product, quotient, floor quotient, remainder, and power. Do not worry about validating the input.

# ==> Enter the first number:
# 3.141592
# ==> Enter the second number:
# 2.718282
# ==> 3.141592 + 2.718282 = 5.859811
# ==> 3.141592 - 2.718282 = 0.42324699999999993
# ==> 3.141592 * 2.718282 = 8.539561733178
# ==> 3.141592 / 2.718282 = 1.1557038600115808
# ==> 3.141592 // 2.718282 = 1.0
# ==> 3.141592 % 2.718282 = 0.42324699999999993
# ==> 3.141592 ** 2.718282 = 22.45792517468373

def prompt(message):
    return f'==> {message}'

first_number = float(input(prompt('Enter the first number: ')))
second_number = float(input(prompt('Enter the second number: ')))

addition_total = first_number + second_number
print(prompt(f'{first_number} + {second_number} = {addition_total}'))

subtraction_total = first_number - second_number
print(prompt(f'{first_number} - {second_number} = {subtraction_total}'))

product_total = first_number * second_number
print(prompt(f'{first_number} * {second_number} = {product_total}'))

quotient_total = first_number / second_number
print(prompt(f'{first_number} / {second_number} = {quotient_total}'))

floor_quotient_total = first_number // second_number
print(prompt(f'{first_number} // {second_number} = {floor_quotient_total}'))

remainder_total = first_number % second_number
print(prompt(f'{first_number} % {second_number} = {remainder_total}'))

power_total = first_number ** second_number
print(prompt(f'{first_number} ** {second_number} = {power_total}'))

#consider lambda functions to make the program more concise