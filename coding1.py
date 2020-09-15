string = input()
if len(string)%2 == 0:
    print("Invalid Input")
else:
    temp = 0
    for i in range(1,len(string)+1):
        for j in range(1,len(string)+1):
            if i == j:
                print(string[i-1], end=" ")
            elif j == len(string)-temp:
                print(string[(len(string)-1)-temp], end=" ")
            else:
                print(end="  ")
        print()
        temp += 1