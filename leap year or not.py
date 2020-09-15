''' check Whether the given year is LEAP or NOT'''

year = int(input("Enter a year: "))
if year%100==0:
    if year%400==0:
        print("It is a 'LEAP' year")
    else:
        print("It is NOT a Leap year")
else:
    if year%4==0:
        print("It is a 'LEAP' year")
    else:
        print("It is NOT a Leap year")