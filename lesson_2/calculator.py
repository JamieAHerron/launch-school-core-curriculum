#ask user for first number
#ask user for second number 
#ask the user for an operation to perform
#perform said operation
#print result to terminal

print('Welcome to Calculator!')

#Ask the user for the first number
print('What is the first number?')
number1 = input()
#Ask for input second number
print("What is the second number?")
number2 = input()

print("What operation would you like to perform?\n" \
"1) Add 2) Subtract 3) Multiply 4) Divide")
operation = input()

if operation == '1':
    output = int(number1) + int(number2)
elif operation == '2':
    output = int(number1) - int(number2)
elif operation == '3':
    output = int(number1) * int(number2)
elif operation == '4':
    output = int(number1) / int(number2)

print(f"The result is: {output}")