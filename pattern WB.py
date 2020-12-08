n = int(input())
s = input()
for i in range(n):
    for j in range(n//2):
        if i%2==0:
            print(s, end = " ")
            print("B", end = " ")
        else:
            print("B", end = " ")
            print(s, end = " ")
    print()
