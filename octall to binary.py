n = int(input())
for i in str(n):
    s = format(int(i), "b")
    print(str(s).zfill(3), end="")
    print(str(s).rjust(3, "0"),end="")
