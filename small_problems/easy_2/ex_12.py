# Write a function that takes a number as an argument. If the argument is a positive number, return the negative of that number. If the argument is a negative number, return it as-is.

def negative(num):
    if num <= 0:
        return num
    else:
        return num - (num + num)

print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True

#this function can be written much more concisely using one of pythons built-in functions