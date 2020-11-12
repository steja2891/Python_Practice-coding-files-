m = int(input())
a = []
for i in input().split():
    if int(i) not in a:
        a.append(int(i))
n = int(input())
player = list(map(int, input().rstrip().split()))
print(a)
for j in player:
    if j not in a:
        a.append(j)
        a.sort(reverse=True)
        print(a.index(j)+1)
    else:
        print(a.index(j)+1)