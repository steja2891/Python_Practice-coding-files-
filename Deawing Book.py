pages, num = int(input()),int(input())
back_count = count = 0
for i in range(1, pages+1,2):
    if i < num and i-1 < num:
        count+= 1
for i in range(pages ,0, -2):
    if i > num and i+1 > num:
        back_count += 1
print(min([count,back_count]))
