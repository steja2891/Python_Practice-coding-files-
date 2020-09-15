list = []
n = int(input("Enter the size of the list: "))
i = 0
for i in range(1,n+1):
    element = input("Enter the {} elements: ".format(i))
    list.append(int(element))

print(list)

for index, element in enumerate("Sachin Tendulkar"):
    print("{} - {}".format(index,element))

print(ord("&"))  # converts Characters to ASCII values
#ASCII -  American Standard Code for Information Interchange
print(chr(122))

print(chr(38))  #converts ASCII value to character
print(bin(12))
print(oct(12))
print(hex(12))
print(round(12))
