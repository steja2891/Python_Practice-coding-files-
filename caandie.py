N = 10
i = int(input())
if i > 10:
    print("Invalid Input")
else:
    k = 5
    if i < k and i > 0:
        print("NUMBER OF CANDIES SOLD: {}".format(i))
        print("NUMBER OF CANDIES AVAILABLE :{}".format(N-i))
    else:
        print("INVALID INPUT")
        print("NUMBER OF CANDIES AVAILABLE :{}".format(N))