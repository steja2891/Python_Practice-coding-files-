import math as m

n = int(input())
for i in range(1, n + 1):
    temp = i
    sum = 0
    while i > 0:
        rem = i % 10
        sum += m.factorial(rem)
        i = i // 10
    if temp == sum:
        print(temp)
