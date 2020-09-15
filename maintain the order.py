list = list(map(int,input().rsplit()))[:8]
print(list)
if list == [1,2,3,4,5,6,7,8]:
    print(-1)
    print(-1)
else:   #[1 2 3 7 5 6 4 8]
    i = 0
    a = []
    while i <= len(list):
        if list[i] != i+1:
            a.append(list.index(i))
        i += 1
    print(min(a))
    print(max(a))



