#Write a program that asks the user to enter an integer greater than 0, then asks whether the user wants to determine the sum or the product of all numbers between 1 and the entered integer, inclusive.

# Example 1: Please enter an integer greater than 0: 5
# Enter "s" to compute the sum, or "p" to compute the product. s

# The sum of the integers between 1 and 5 is 15.

# Example 2: Please enter an integer greater than 0: 6
# Enter "s" to compute the sum, or "p" to compute the product. p

# The product of the integers between 1 and 6 is 720.
def product_compute(number):
    total = 1
    for num in range(1, (number + 1)):
        total *= num
    return total

#The below function could be much more pythonic
def sum_compute(number):
    total = 0
    for num in range(0, (number + 1)):
        total += num
    return total

print('Enter an integer greater than 0: ')
integer = int(input())

print('Enter "s" to compute the sum, or enter "p" to compute the product: ')
computation_choice = input().lower()

if computation_choice == 's':
    print(f'The product of the sum of integers from 0 to {integer} is {sum_compute(integer)}')
else:
    print(f'The product of the integers from 0 to {integer} is {product_compute(integer)}')

#re-factor sum_compute function and use more robust error checking 