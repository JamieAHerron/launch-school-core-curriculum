#Type coercions
#2: What coercion is happening here? Is it implicit or explicit?

a = 1
b = 2
print(a + b)

#3: What coercion is happening here? Is it implicit or explicit?

month = "December"
day = int(input("What day is it? "))
print(f"Today is the {day} of {month}")

#string methods
#4. What does this print and why? (focus on .format())

string1 = "HelloWorld"
string2 = "12345"
string3 = "Hello World"

result1 = string1.isalpha()
result2 = string2.isalpha()
result3 = string3.isalpha()

print("Is '{}' alphabetic?".format(string1), result1)
print("Is '{}' alphabetic?".format(string2), result2)
print("Is '{}' alphabetic?".format(string3), result3)

#10. What do these print and why?

s = "   Hello, World!   "
print(s.strip())
print(s.strip(" !")) #what does this do/ how does strip work?

#13. What do these print and why?

s = "Hello, World!"
print(s.replace("Hello", "Hi"))
print(s.replace("o", "0")) #how does this one behave?

#14. What do these print and why?

sentence = "This is a sample sentence."
words = sentence.split()
print(words)

csv_data = "John,Doe,30,New York"
fields = csv_data.split(",")
print(fields)

sentence = "This is a sample sentence."
words = sentence.split(maxsplit=2) #how does maxsplit work?
print(words)

#list and dictionary syntax
#2. What does this print and why?

lst_one = [0, 1, 2, 3]
lst_two = lst_one.append(4) #focus on what is happening here!
if lst_two:
    print(lst_two)
else:
    print(lst_one)

#4. What does this print and why?

elements = [0, 1 , 2, "Dima"]
print(elements.reverse()) #what does this do?
print(elements)

#(LSBot question) What will the following code output and why?
#Consider default argument/ parameter pitfalls 

def my_function(param=[]):
    param.append(1)
    return param
 
print(my_function())  # [1]
print(my_function())  # [1, 1]
print(my_function([5, 6, 7]))  # [5, 6, 7, 1]
print(my_function())  # [1, 1, 1]

#variable scope, global keyword, variables as pointers, variable shadowing
#4. What does this print and why?
var = 10

def function1():
    var = 20
    print(var)

function1()

try:
    print(var)
except NameError:
    print("Error occurred")

def function2():
    var += 5 #explain this!
    print(var)

try:
    function2()
except UnboundLocalError:
    print("Error occurred")

def function3():
    global var
    var += 5
    print(var)

function3()
print(var)
