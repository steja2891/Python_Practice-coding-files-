n = int(input("Enter a number"))
binary = str(format(n,"b"))
count = 1
a = []
for i in range(1,len(binary)):
    if binary[i-1] == "1":
        if binary[i-1] == binary[i]:
            count += 1
            if i == len(binary)-1:
                a.append(count)
        else:
            a.append(count)
            count = 1


print(max(a))
