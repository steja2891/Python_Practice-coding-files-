n = int(input("no.of students:"))
a = []
for i in range(n):
    ele = int(input())
    a.append(ele)
for i in a:
    for j in range(1,10):
        n = i+j
        if n%5 == 0:
            break
    if n - i < 3 and n >= 40:
        print(n)
    else:
        print(i)

