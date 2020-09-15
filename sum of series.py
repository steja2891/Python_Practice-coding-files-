n = int(input())


def factorial(i):
    if i == 0 or i == 1:
        return 1
    else:
        return i * factorial(i - 1)


_sum = 0
for i in range(1, n + 1):
    _sum += (i / factorial(i))
print("{:4.6f}".format(_sum))
