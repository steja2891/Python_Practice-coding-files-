n = int(input("Enter the size of the array: "))

a = []
i = 0
while i<n:
    element = int(input())
    a.append(element)
    i += 1
print(a)
max_num = max(a)
count = 0
for i in a:
    if i == max_num:
        count += 1
print(count)