#Programmatically determine whether 42 lies between 10 and 100, 
#inclusive. Do the same for the values 100 and 101.

number1 = 42
number2 = 100
number3 = 101

def number_check(number):
    if number >= 10 and number <= 100:
        return True
    else:
        return False

print(number_check(number1))
print(number_check(number2))
print(number_check(number3))

#there is a much simpler way to do this!
