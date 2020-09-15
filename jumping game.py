n = int(input())
a = list(map(int,input().rstrip().split()))
step = i = 0
while i < len(a):
    if a[0] == 1:
        i += 1
        continue
    elif (i+2) < len(a):
        if a[i] == a[i+2]:
            step += 1
            i += 2
        elif a[i] == a[i+1]:
            step += 1
            i += 1
    else:
        if a[i] == a[i+1]:
            step += 1
            i += 1


