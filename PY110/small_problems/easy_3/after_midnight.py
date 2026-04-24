MINUTES_PER_DAY = 24 * 60

def append_zero(time):
    if time < 10:
        return f'0{str(time)}'
    return str(time)

def time_of_day(delta_minutes):
    #this while loop adds 1440 (total minutes in the day) to negative numbers, allowing the calculation to be carried out as it would with positive numbers
    while delta_minutes < 0:
        delta_minutes += MINUTES_PER_DAY
    # “delta_minutes % MINUTES_PER_DAY keeps only the number of minutes within the current day by throwing away any whole days’ worth of minutes.”
    delta_minutes = delta_minutes % MINUTES_PER_DAY
    hours = delta_minutes // 60
    minutes = delta_minutes % 60
    #the append_zero helper function deals with numbers less than 10 (in regards to time)
    return f'{append_zero(hours)}:{append_zero(minutes)}'

print(time_of_day(-50))
