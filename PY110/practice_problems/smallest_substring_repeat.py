def smallest_substring_repeat(s):
    for length in range(1, len(s) + 1):
        sub = s[:length]
        count = len(s) // length
        if sub * count == s:
            return [sub, count]