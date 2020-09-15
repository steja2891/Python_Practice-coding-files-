n = int(input("Enter the steps: "))
s = input()[:n]
sea = 0
valley = 0
for num,i in enumerate(s):
    if i =="U":
        sea += 1
    else:
        sea -= 1
    if sea == 0 and s[num] == "U":
        valley += 1

print(valley)