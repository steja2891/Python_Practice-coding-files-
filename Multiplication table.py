# Multiplication table

num = int(input("Enter a number: "))
i = 1;
while i<=10:
    print("{}x{:2}={:3}".format(num,i,num*i))
    i= i+1
print("--------------------------------")