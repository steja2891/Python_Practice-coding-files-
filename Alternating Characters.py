s = input("Enter a string: ")
# a = list(s)
# rmcount = 0
# i = 0
# while i < len(a) - 1:
#     if a[i] == a[i + 1]:
#         del a[i + 1]
#         rmcount += 1
#         i = 0
#     else:
#         i += 1
# print(rmcount)
n = len(s)
count = 0
for i in range(1,n):
    if s[i-1]==s[i]:
        count += 1
print(count)