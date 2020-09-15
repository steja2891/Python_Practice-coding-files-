def kangaroo(x1, v1, x2, v2):
     x1 + v1
    y = x2 + v2
    while x != y:
        if (x1 < x2) and (v1 < v2):
            return "NO"
        x += v1
        y += v2
    return "YES"
x1V1X2V2 = input().split()

x1 = int(x1V1X2V2[0])

v1 = int(x1V1X2V2[1])

x2 = int(x1V1X2V2[2])

v2 = int(x1V1X2V2[3])

result = kangaroo(x1, v1, x2, v2)
print(result)