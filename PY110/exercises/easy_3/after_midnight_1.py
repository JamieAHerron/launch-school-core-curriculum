'''
The time of day can be represented as the number of minutes before or after midnight. If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, the time is before midnight.

Write a function that takes a time using this minute-based format and returns the time of day in 24-hour format (hh:mm). Your function should work with any integer input.

You may not use Python's datetime module.

input: integer (minutes)
output: string (24 hour time)

Explicit requirements:
    - if number positive - number of minutes AFTER midnight
    - if number negative - number of minutes BEFORE midnight

Questions:
    - How best to convert the integer/operation performed to produce a string?
    - How can I break down the integer minutes (into 24 hours)?
    - What data structure is best to perform the operation (list of four digits for example)?
'''
MINUTES_PER_DAY = 1440
MINUTES_PER_HOUR = 60

def format_time(hours, minutes):
    return f"{hours:02d}:{minutes:02d}"

def time_of_day(num):
    while num < 0:
        num = num + MINUTES_PER_DAY
    
    num = num % MINUTES_PER_DAY
    hours = num // MINUTES_PER_HOUR
    minutes = num % MINUTES_PER_HOUR

    return format_time(hours, minutes)

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True

#Disregard Daylight Savings and Standard Time and other complications.