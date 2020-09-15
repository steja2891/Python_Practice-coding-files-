n = int(input())
l = float(input())
time = (n/l)*360
if time > 12:
    time = time - 12
x = "{:4.2f}".format(time)
time = str(x)
if len(time) == 4:
    hr = int(time[0])
    min = int(time[2:])
else:
    hr = int(time[:2])
    min = int(time[3:])
degrees = 30*hr - (11/2)*min
if degrees > 180:
    print(360-degrees)
else:
    print("{:4.2f}".format(degrees))5