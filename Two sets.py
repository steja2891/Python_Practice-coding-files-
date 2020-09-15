size = input().rstrip().split()
n = int(size[0])
m = int(size[1])
a = list(map(int, input().rstrip().split()))[:n]
b = list(map(int, input().rstrip().split()))[:m]
l2 = set()
for i in range(1, min(b)+1):
    count = 0
    for j in b:
        if min(b) % i == 0 and j % i == 0:
            count += 1
    if count == len(b):
        l2.add(i)
l3 = []
for j in l2:
    count = 0
    for k in a:
        if j % k == 0:
            count += 1
    if count == len(a):
        l3.append(j)
print(len(l3))