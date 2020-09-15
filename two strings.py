n = int(input("No.of cases: "))
s1 = 0
s2 = 0
count = 0
for i in range(1,n):
    s1 = input()
    s2 = input()
    for i in s1:
        if i in s2:
            count+=1
            break
if count == 1:
    print("YES")
else:
    print("NO")