t = int(input())
for t_itr in range(t):
    s = set({})
    list2 = []
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            s.add(i & j)
    for m in s:
        if m < k:
            list2.append(m)
    print(max(list2))
