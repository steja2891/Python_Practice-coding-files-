n= int(input())
_list = list(map(int, input().rstrip().split()))
marks = int(input())
sorted_list = sorted(_list)
print(sorted_list)
print(sorted_list.index(marks)+1)