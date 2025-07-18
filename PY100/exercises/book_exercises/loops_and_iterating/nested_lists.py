# my_list = [
#     [1, 3, 6, 11],
#     [4, 2, 4],
#     [9, 17, 16, 0],
# ]

# for nested_list in my_list:
#     for number in nested_list:
#         if number % 2 == 0:
#             print(number)

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

even_odd_list = []
for index in my_list:
    
    if index % 2 == 0:
        even_odd_list.append('even')
    else:
        even_odd_list.append('odd')

print(even_odd_list)