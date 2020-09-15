a = []
b = []
i = 0
j = 0

while i<3:
    element = int(input("Enter a[{}] element".format(i)))
    a.append(element)
    i += 1
while j<3:
    element = int(input("Enter b[{}] element".format(j)))
    b.append(element)
    j += 1

def compareTriplets(p1,p2):
    alice_points = 0
    bob_points = 0
    if p1[0] > p2[0]:
        alice_points += 1
    elif p1[0] < p2[0]:
        bob_points = 0
    else:
        pass

    if p1[1] < p2[1]:
        bob_points += 1
    elif p1[1] > p2[1]:
        alice_points += 1
    else:
        pass

    if p1[2] < p2[2]:
        bob_points += 1
    elif p1[2] > p2[2]:
        alice_points += 1
    else:
        pass
    return [alice_points,bob_points]


print(compareTriplets(a, b))