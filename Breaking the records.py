n = int(input())
arr = list(map(int, input().rstrip().split()))[:n]
high_count = low_count = 0
high = low = arr[0]
for i in arr[1:]:
    if i > high:
        high_count += 1
        high = i
    elif i < low:
        low_count += 1
        low = i
print(high_count,low_count)



