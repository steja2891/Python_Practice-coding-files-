r = int(input())
c = int(input())
a = []
for i in range(r * c):
    a.append(int(input()))
sum = i = 0
while i <= len(a):
    sum += a[i]
    i += r+1
print(sum)