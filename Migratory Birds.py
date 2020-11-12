n = int(input())
arr = list(map(int, input().rstrip().split()))[:n]
d = {}
for i in arr:
    d[i] = arr.count(i)
a = []
for i, j in d.items():
    if j == max(d.values()):
        a.append(i)
print(min(a))