arr = [1,2,3,4,5]
list = []
for index_1,num in enumerate(arr):
    sum = 0
    for index,j in enumerate(arr):
        if index_1 != index:
            sum += arr[index]
        else:
            pass
    list.append(sum)
print(min(list), max(list))