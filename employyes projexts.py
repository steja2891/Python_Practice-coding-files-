n = int(input())
_list = list(map(int, input().rstrip().split()))
a = []
for i in _list:
    for j in range(1, i + 1):
        a.append(i)
i = 1
while True:
    if a[i-1] != a[i]:
       pass
    i += 1
