year = int(input())
days = 215
if 1700 <= year <= 1917:
    if year% 4 == 0:
        days += 29
    else:
        days+= 28
else:
    if year %4 == 0 or year%400 == 0:
        days += 29
    elif year == 1918:
        days += 15
    else:
        days += 28
print("{}.09.{}".format(256-days,year))