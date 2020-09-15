n = int(input())
list1 = list(map(int, input().rstrip().split()))
maximum = max(list1)
count = 0
for i in range(1, 100):
    for j in list1:
        if (maximum * i) % j == 0 and j != maximum:
            count += 1
    if count == n-1:
        print(maximum * i)
        break
    count = 0