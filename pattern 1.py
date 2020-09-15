n= int(input())
if n < 0:
    print("Invalid Input")
for i in range(n):
    for j in range(i):
        if j == i:
            print(j, end=" ")
    print("")