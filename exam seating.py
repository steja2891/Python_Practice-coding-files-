a = []
b = []
for i in range(10):
    s = input()
    if "TY" in s:
        a.append(s)
    else:
        b.append(s)
a.sort()
b.sort()
for j in range(5):
    try:
        print("[{}]".format(a[j]), end="")
    except:
        print("[ABSENT]", end= "")
    try:
        print("[{}]".format(b[j]))
    except:
        print("[ABSENT]")
