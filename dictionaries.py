# dict = {"sai":123,"teja":456}
# s1 = input()
# s2 = input()
# s3 = input()
# for item in dict:
#     if item in dict.keys():
#         print("{}={}".format(item,dict[item]))
# n = int(input())
# list = []
# for i in range(n):
#     list.append(tuple(map(str, input().rstrip().split())))
# dict = dict(list)
# p = input()
# while p != '':
#     if p in dict:
#         print("{0}={1}".format(p,dict[p]))
#     else:
#         print("NotFound")
#     p = input()
# def Details(a):
#     for item in a:
#         if item in dict:
#             print("{0}={1}".format(item,dict[item]))
#         else:
#             print("Not found")
#
# if __name__ == "__main__":
#     n = int(input())
#     list = []
#     for i in range(n):
#         list.append(tuple(map(str, input().rstrip().split())))
#     dict = dict(list)
#     a = []
#     while True:
#         p = input()
#         if p != "":
#             a.append(p)
#         else:
#             break
#     Details(a)
# while True:
#     try:
#         s = input()
#         if s in dict.keys():
#             print(i+"="+dict[i])
#         else:
#             print("Not found")
#     except:
#         break
#
#
import sys
n = int(input())
dict = {}
for i in range(n):
    key, value = input().split()
    dict[key] = value
s = sys.stdin.read()
for i in s.split():
    if i in dict.keys():
        print(i+"="+dict[i])
    else:
        print("Not found")

