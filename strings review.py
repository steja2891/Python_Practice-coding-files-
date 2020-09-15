t = int(input("Enter no.of strings: "))

for i in range(t):
    s = input()
    for j in range(0,len(s),2):
        print(s[j],end="")
    print(end=" ")
    for k in range(1,len(s),2):
        print(s[k],end="")
    print("")