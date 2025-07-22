# def double_numbers(numbers):
#     for i in range(len(numbers)):
#         numbers[i] = numbers[i] * 2
#     return numbers

# my_numbers = [1, 4, 3, 7, 2, 6]
# print(double_numbers(my_numbers)) # [2, 8, 6, 14, 4, 12]
# print(my_numbers)                 # [2, 8, 6, 14, 4, 12]

# Here's an exercise for you: suppose we wanted to transform the numbers based on their position in the list rather than their value? Try coding a solution that doubles the numbers that have odd indexes:

def double_numbers(numbers):
    result = []
    for i in range(len(numbers)):
        if i % 2 == 1:
            result.append(numbers[i] * 2)
        else:
            result.append(numbers[i])
    return result

my_numbers = [1, 4, 3, 7, 2, 6]
print(double_numbers(my_numbers)) 
print(my_numbers)                 