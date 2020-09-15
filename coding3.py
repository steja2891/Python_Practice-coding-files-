n = int(input("no="))
s = str(n)
even_no = ''
odd_no = ''
for i in range(len(s)):
    if i == 0 or i%2 == 0:
        even_no += s[i]
    else:
        odd_no += s[i]
print("no={},odd_no={},even_no={}".format(n,int(odd_no),int(even_no)))




