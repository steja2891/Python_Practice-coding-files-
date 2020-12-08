n = int(input())
a = list(map(int, input().rstrip().split()))
l = int(input())
b = []
try:
    for i in range(len(a)):
        pro = 1
        for j in range(i,l+i):
            pro *= a[j]
        b.append(pro)
except:
    print(max(b))

