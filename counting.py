import math
s , n= input(),int(input())
if s == "a":
    print(n)
elif "a" not in s:
    print(0)
else:
    if n < 100:
        string = s*n
        print(string[:n].count("a"))
    else:
        print(int(n/len(s))*s.count("a")+s[:n%len(s)].count("a"))



