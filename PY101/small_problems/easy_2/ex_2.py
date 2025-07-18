#Write a program that asks for user's name, then greets the user. If the user appends a ! to their name, the computer will yell the greeting (print it using all uppercase).

#What is your name? Sue
#Hello Sue.

#What is your name? Bob!
#HELLO BOB! WHY ARE WE YELLING?

name = input('Please enter your name: ')

while name == '' or name.isdigit():
    name = input('Please enter a valid name: ')

if name[-1:] == '!':
    print(f'HELLO {name.upper()} WHY ARE YOU YELLING?')
else:
    print(f'Hello {name}.')