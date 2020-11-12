n = int(input())
a = []
for i in range(2, n + 1):
    for j in range(2, n):
        if i == 2:
            a.append(i)
            break
        elif i % j == 0:
            break
        else:
            a.append(i)
            break
print(a)
sum = count = 0
for i in a:
    sum = sum + i
    if sum in a and sum != 2:
        count += 1
print(count)
