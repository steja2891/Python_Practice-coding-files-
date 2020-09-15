n = int(input())
a = []
i = 0
while i < n:
    element = int(input())
    a.append(element)
    i += 1
print(a)

count = 0
b = []
for item in a:
    if item not in b:
        b.append(item)
for j in b:
    num = a.count(j)
    if num % 2 == 0:
        count += num/2
    if num % 2 != 0:
        count += num//2

print(int(count))
