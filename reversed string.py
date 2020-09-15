string = input()
i = len(string)-1
while i <= len(string)-1:
    print(string[i], end="")
    if i == 0:
        break
    i -= 1
