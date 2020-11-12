p = input()
x = int(input())
print(eval(p))
x, y, z, p, q, r, s = (int(input()) for _ in range(7))
print(x, y, z, p, q, r, s)
n = 3
list1 = [[a, b, c] for a in range(n) for b in range(n) for c in range(n)]
print(list1)

