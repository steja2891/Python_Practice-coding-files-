n = int(input("Enter the size of array: "))
arr = list(map(int, input().rstrip().split()))[:n]
for i in range(len(arr),0,-1):
    print(arr[i] ,end=" ")
