'''
The solution uses two variables, previous and current, to maintain the values of the current pair of numbers in the Fibonacci series.

The solution starts by setting the two variables to the first two numbers in the series. Using these numbers as a foundation, the solution loops and reassigns the value of the tuple nth - 2 times. If nth is 1 or 2, no iteration is needed; you just have to return 1. Otherwise, we perform the iteration, then return the final value assigned to current.

For example, given an argument of 6, the values of previous and current, starting with the initial values, are shown below:

# previous, current
# 1, 1
# 1, 2    # values after 1st iteration (nth = 3)
# 2, 3    # values after 2nd iteration (nth = 4)
# 3, 5    # values after 3rd iteration (nth = 5)
# 5, 8    # values after 4th iteration (nth = 6)
'''

def fibonacci(nth):
    if nth <= 2:
        return 1

    previous, current = 1, 1
    for _ in range(3, nth + 1):
        previous, current = current, previous + current
        

    return current

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True