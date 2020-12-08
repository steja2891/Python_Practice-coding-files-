# n = int(input())
# a,b = 0,1
# if n == 0:
#     print(0)
# elif n == 1:
#     print(1)
# else:
#     for i in range(2, n):
#         c = a+b
#         a = b
#         b = c
# print(c)

# Fibonacci series using Recursive Function...
#
def F(n):
    if n <= 1:
        return n
    else:
        return F(n - 1) + F(n - 2)


n = int(input())
for i in range(n):
    print(F(i))
