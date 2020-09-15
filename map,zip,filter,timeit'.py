import math as m

a = [1,2,3]
p,q, r = map(m.sqrt,a)
print(p,q,r)



a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
f1 = map(m.sqrt, a)
print(f1)

b = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
f2 = list(zip(a, b))
print(f2)


def func(a):
    if a%2==0:
        return True
f3 = filter(func, a)
print(f3)

import timeit as time
print(time.timeit('x=[1,2,3,4,5,6,7,8,9,10]', number=10))
print(time.timeit('x=(1,2,3,4,5,6,7,8,9,10)', number=10))

