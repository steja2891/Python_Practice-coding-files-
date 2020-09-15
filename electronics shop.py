budget,num_of_keyboards, num_of_drives = int(input()), int(input()), int(input())
keyboard_list = list(map(int,input().rstrip().split()))[:num_of_keyboards]
drives_list = list(map(int,input().rstrip().split()))[:num_of_drives]
sum = 0
sum_list = []
for i in keyboard_list:
    for j in drives_list:
        sum = i + j
        if budget >= sum:
            sum_list.append(sum)
if sum_list == []:
    print(-1)
else:
    print(max(sum_list))