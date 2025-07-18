#Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.

#Further Exploration
#Consider adding a way for the user to specify the starting and ending values of the odd numbers printed.

print('Input the start of the odd number range: ')
range_start = int(input())

print('Input the end of the odd number range: ')
range_end = int(input())

for num in range(range_start, (range_end + 1), 2):
    print(num)