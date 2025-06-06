#Using the multiply function from the "Multiplying Two Numbers" exercise, write a function that computes the square of its argument (the square is the result of multiplying a number by itself).

def multiply(num1, num2): #function from previous exercise
    return num1 * num2

def square(number):
    return multiply(number, number)

print(square(5) == 25)   # True
print(square(-8) == 64)  # True