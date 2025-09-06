#Write a function that takes one argument, a positive integer, and returns the sum of its digits.

# def sum_digits(num):
#     result = 0

#     while num > 0:
#         num, last_digit = divmod(num, 10)
#         result += last_digit
    
#     return result

def sum_digits(num):

    return sum([int(char) for char in str(num)])


print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True