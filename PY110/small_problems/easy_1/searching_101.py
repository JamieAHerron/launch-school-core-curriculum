# Your code goes here
'''
P:
Explicit:
-solicit six numbers (one by one)
-prints message stating if sixth number is in the first five
Implicit:
- Numbers must be numeric
- a number must be entered (no blanks)

Input: 6 numbers (integers)
Output: string (stating if sixth number is in first five)

D:
- lists (to store numbers)
- string (output)

A:
- prompt user for number (six times)
- after each prompt, store number in list
- once list complete (six items) ask if last item is contained within first five
- remove last item and ask 'item in first five'
- construct string to be returned (yes/no)
'''

#Code:

def searching_101():
    print('You will be asked to enter six numbers:')
    
    count = 0
    num_list = []
    while count < 6:
        answer = int(input('Enter a number:'))
        num_list.append(answer)
        count += 1
    
    last_num = num_list[5]
    first_five_list = num_list[:5]
    first_five = ','.join(str(num) for num in num_list)
    if last_num in first_five_list:
        print(f'{last_num} is in {first_five}')
    else:
        print(f'{last_num} is not in {first_five}')

searching_101()

'''
LAUNCH SCHOOL VERSION

def searching_101():
    print('You will be asked to enter six numbers:')

    num_list = []
    for _ in range(6):
        answer = int(input('Enter a number: '))
        num_list.append(answer)

    first_five = num_list[:5]
    last_num = num_list[5]
    numbers_str = ','.join(str(num) for num in first_five)

    if last_num in first_five:
        print(f'{last_num} is in {numbers_str}.')
    else:
        print(f"{last_num} isn't in {numbers_str}.")

searching_101()
'''