n = int(input())
k = int(input())
arr = list(map(int, input().rstrip().split()))
i = 0
count = 0
b = []
c = []
for i in arr:
    if i == 0:
        c.append(arr.index(i))
  
while i <= len(arr)-1:
    if arr[i] == 1:
        count += 1
        i += 1
    else:
        b.append(count)
        count = 0
        i += 1
        continue
b.append(count)
print(b)