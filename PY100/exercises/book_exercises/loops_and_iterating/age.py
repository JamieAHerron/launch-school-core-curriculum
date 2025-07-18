

age = int(input('How old are you? '))
print()
print(f'You are {age} years old.')
# print(f'In 10 years, you will be {age + 10} years old.')
# print(f'In 20 years, you will be {age + 20} years old.')
# print(f'In 30 years, you will be {age + 30} years old.')
# print(f'In 40 years, you will be {age + 40} years old.')

for future in range(10, 50, 10):
    print(f'In {future} years, you will be '
          f'{age + future} years old.')
    


