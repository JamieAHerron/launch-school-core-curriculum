#Let's do some "ASCII Art": a stone-age form of nerd artwork from back in the days before computers had video screens.

#For this practice problem, write a program that outputs The Flintstones Rock! 10 times, with each line prefixed by one more hyphen than the line above it. The output should start out like this:

my_string = 'The Flinstones Rock!'
hyphen = '-'

for _ in range(0, 10):
    print(hyphen + my_string)
    hyphen += '-'

#not the launch school answer but a valid approach according to Launch School

