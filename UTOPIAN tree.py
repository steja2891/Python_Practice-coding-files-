def utopianTree(n):
    count = 0
    if n == 0:
        count += 1
    else:
        for i in range(n+1):
            if i == 0:
                count += 1
            else:
                if i%2==0:
                    count+= 1
                else:
                    count+= count
        print(count)


t = int(input())
for t_itr in range(t):
    n = int(input())
    if n == 0:
        print(1)
    else:
        result = utopianTree(n)