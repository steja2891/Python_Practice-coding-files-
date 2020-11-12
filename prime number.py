n = int(input())
if n > 0:
    if n == 1:
        print("It is Not a Prime Number")
        exit()
    for i in range(2, n):
        if n % i == 0:
            print("It is not a Prime number")
            break
    else:
        print("It is a Prime Number")
else:
    print("It is not a Positive Number")
