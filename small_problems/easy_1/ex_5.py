#Create a simple tip calculator. The program should prompt for a bill amount and a tip rate. The program must compute the tip, then print both the tip and the total amount of the bill. You can ignore input validation and assume that the user will enter valid numbers.

# What is the bill? 200
# What is the tip percentage? 20

# The tip is $40.00
# The total is $240.00

print('What is the bill amount? ')
bill_amount = float(input())
print('What is the tip percentage? ')
tip_percentage = float(input()) / 100

tip_amount = bill_amount * tip_percentage
total_bill = bill_amount + tip_amount

print(f'The tip is {tip_amount}')
print(f'The total is {total_bill:.2f}')

