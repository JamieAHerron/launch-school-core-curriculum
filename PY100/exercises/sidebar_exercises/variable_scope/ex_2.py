x = 10

def my_function():
    #global x <<< Without using the global keyword an error will appear
    #x is not initialzed locally 
    x = x + 5
    print(x)

my_function()