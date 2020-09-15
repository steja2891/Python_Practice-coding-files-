list_strings = list(map(str, input().rstrip().split()))
vowels = frozenset("aeiou")
count = 0
for word in list_strings:
    string = word.casefold()
    for i in range(1, len(word) - 1):
        if (string[i - 1] in vowels) and (string[i] in vowels):
            print(word)
            count += 1
            break
if count == 0:
    print("Invalid Input")
