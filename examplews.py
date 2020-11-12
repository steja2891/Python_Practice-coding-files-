q = int(input())
for i in range(q):
    a = list(map(int, input().rstrip().split()))
    x, y, z = a[0], a[1], a[2]
    cat_a, cat_b = abs(z-x), abs(z-y)
    if cat_a == cat_b:
        print("Mouse C")
    elif cat_a > cat_b:
        print("Cat B")
    else:
        print("Cat A")