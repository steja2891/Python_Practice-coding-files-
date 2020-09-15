currency = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
n = int(input())
coins = 0
i = len(currency)-1
while True:
    if n >= currency[i]:
        n1 = n - currency[i]
        coins += 1
        n = n1
        i = len(currency)-1
        continue
    if n == 0:
        break
    i -= 1
print(coins)