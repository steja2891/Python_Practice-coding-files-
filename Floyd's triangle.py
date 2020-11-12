n = int(input())
k = 1
for i in range(1,n+1):
    for j in range(i):
        print(k+j, end="\t")
    print()
    k = k+j+1