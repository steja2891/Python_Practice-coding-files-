n = int(input())
a = list(map(int, input().rstrip().split()))
b = []
for i in range(1,len(a)):
    b.append(a[i-1]-a[i])
print(max(b))
