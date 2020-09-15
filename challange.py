n = int(input("Enter the size of the array: "))
customers = []
i = 0
while i < n:
    element = input()
    customers.append(element)
    i += 1
# ==============================
s = set(customers)
b = {}
for i in s:
    b[i] = customers.count(i) / n * 100
c = []
for key, value in b.items():
    if value >= 5.0:
        c.append(key)
c.sort()
for i in c:
    print(i)