name = 'Roger'

def string_compare(string1, string2):
    if string1.casefold() == string2.casefold():
        print('true')
    else:
        print('false')

string_compare(name, 'RoGeR')
string_compare(name, 'Dave')
