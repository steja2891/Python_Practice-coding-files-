s = input()
key = int(input())
for i in s:
    if i == " ":
        print(" ",end="")
        continue
    if i == "z" or i == "Z":
        print(chr(ord("")))
        continue
    print(chr(ord(i)+key), end="")


