n = int(input())
s = input()
count = 0
a,b,c  = [],[],[]
for i in s:
    if i.isalpha() == True:
        a.append(i)
    else:
        if count > n-1:
            a.append(i)
        else:
            if i == " ":
                a.append(".")
            else:
                a.append(i)
        b.append("".join(a))
        c.append(len(b[0]))
        a,b = [],[]
        count += 1
print(max(c))

