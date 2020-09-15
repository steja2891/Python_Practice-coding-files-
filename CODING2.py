list1 = list(map(int, input().rstrip().split(",")))
a = []
list = list(set(list1))
for i in list:
    if i == list[len(list)-1]:
        print(i)
        break
    print(i,end=",")
# for item in list1:
#     if item not in a:
#         a.append(item)
# print(a)