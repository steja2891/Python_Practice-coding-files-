n = int(input())
array_list = list(map(int, input().rstrip().split()))
set_list = set(array_list)
a = []
for count_num in range(1, n):
    for i in set_list:
        if i in a:
            continue
        if array_list.count(i) == count_num:
            if count_num > 1:
                for j in range(count_num):
                    a.append(i)
            else:
                a.append(i)
print(a)
