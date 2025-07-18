def compare_by_length(string1, string2):
    if len(string1) > len(string2):
        print(1)
    elif len(string1) < len(string2):
        print(-1)
    else:
        print(0)



compare_by_length('patience', 'perseverance') # -1
compare_by_length('strength', 'dignity')      #  1
compare_by_length('humor', 'grace')           #  0