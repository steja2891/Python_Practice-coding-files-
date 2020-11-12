n = int(input())
s = list(map(int, input().rstrip().split()))
a = list(input().rstrip().split())
d, m = int(a[0]), int(a[1])
count = 0
for i in range(len(s)):
    if sum(s[i: (i + m)]) == d:
        count += 1
print(count)