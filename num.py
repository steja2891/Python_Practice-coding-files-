i = 0
a = []
while i.casefold() == "q":
    if i == 0:
        pass
    i = input()

count = 0
for i in a:
    if i.isnumeric() and len(i) == 10:
        count += 1
print(count)

