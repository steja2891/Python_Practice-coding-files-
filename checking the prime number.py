# Check whether the given number is prime or not

num = int(input("Enter a number: "))
for i in range(2, num):
    if num%i==0:
        print("The given number {} is NOT a Prime Number".format(num))
        break
else:
    print("The Given number {} is a 'Prime Number'".format(num))