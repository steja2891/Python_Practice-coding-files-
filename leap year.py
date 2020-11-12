def is_leap(year):
    leap = False
    if year % 100 == 0:
        if year % 400 == 0:
            return bool(1)
        else:
            return leap

    elif year%4 ==0:
        return bool(1)
    else:
        return leap

year = int(input())
print(is_leap(year))