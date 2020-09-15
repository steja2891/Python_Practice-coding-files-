
a = [[1,2,3], [4,5,6], [7,8,9]]
sum_1 = 0
sum_2 = 0
for i in range(3):
    for j in range(3):
        if i == j:
            sum_1 += a[i][j]
        if (i+j)==(3-1):
            sum_2 += a[i][j]
x = abs(sum_1)
y = abs(sum_2)
print(x)
print(y)
n = 6
for i in range(1,n+1):
    for j in range(n,0,-1):
        if j > i:
            print(end =" ")
        else:
            print("#")
    print(" ")

n = 6
for i in range(1,n+1):
    for j in range(n,0,-1):
        if j > i:
            print("", end =" ")
        else:
            print("#", end="")
    print("")




