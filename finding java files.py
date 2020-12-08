def Find_Java(s1, s2):
    if "java" in s1.casefold() and "java" in s2.casefold():
        print("2 files are with JAVA Extension")
    elif "java" in s1.casefold() or "java" in s2.casefold():
        print("1 file are with JAVA Extension")
    else:
        print("No file with JAVA Extension")


s1 = input()
s2 = input()
Find_Java(s1, s2)
print(s1.find("java"))