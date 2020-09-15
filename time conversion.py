print("Enter the time in the format 'hh:mm:ssAM/PM' :" )
s = input()
#07:05:45PM
final = 0
if "PM" in s:
    x = int(s[:2])
    if x == 12:
        print(str(x) + s[2:8])
    else:
        y = x + 12
        final = str(y) + s[2:8]
        print(final)
else:
    a = s[:2]
    if a == "12":
        final2 = str("00")+s[2:8]
        print(final2)
    else:
        print(str(a)+s[2:8])