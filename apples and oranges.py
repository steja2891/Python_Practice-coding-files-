# inputs
st = input().split()
s = int(st[0])
t = int(st[1])
ab = input().split()
a = int(ab[0])
b = int(ab[1])
mn = input().split()
m = int(mn[0])
n = int(mn[1])
apples = list(map(int, input().rstrip().split()))
oranges = list(map(int, input().rstrip().split()))
app = []
for fruit in apples:
    app.append(a + fruit)
oran = []
for fruit in oranges:
    oran.append(b + fruit)
app_count = 0
oran_count = 0
for i in app:
    if i in range(s, t + 1):
        app_count += 1
print(app_count)
for i in oran:
    if i in range(s, t + 1):
        oran_count += 1
print(oran_count)
