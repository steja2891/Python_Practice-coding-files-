s = input()
n = int(input())
dict1 = {1: "Espresso Coffee", 2: "Cappuccino Coffee", 3: "Latte Coffee"}
dict2 = {1: "Plain Tea", 2: "Assam Tea", 3: "Ginger Tea", 4: "Cardamom Tea", 5: "Masala Tea", 6: "Lemon Tea",
         7: "Green Tea", 8: "Organic Darjeeling Tea"}
dict3 = {1: "Hot Chocolate Drink", 2: "Veg Corn Soup", 3: "Tomato Soup", 4: "Spicy Tomato Soup"}
print("Welcome to CCD!")
if s.casefold() == "c":
    try:
        print("Enjoy your {}!".format(dict1[n]))
    except:
        print("INVALID INPUT!")
elif s.casefold() == "t":
    try:
        print("Enjoy your {}!".format(dict2[n]))
    except:
        print("INVALID INPUT!")
elif s.casefold() == "b":
    try:
        print("Enjoy your {}!".format(dict3[n]))
    except:
        print("INVALID INPUT!")
