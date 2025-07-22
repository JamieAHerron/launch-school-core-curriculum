def multiply_numbers(number_list, multiplier):
    result = []

    for num in number_list:
        result.append(num * multiplier)
    
    return result

my_numbers = [1, 4, 3, 7, 2, 6]
print(multiply_numbers(my_numbers, 3))  # [3, 12, 9, 21, 6, 18]