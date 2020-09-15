name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age > 18 and age < 31:
    print("Welcome {}, Enjoy your Holiday ".format(name))
else:
    print("Sorry, You r not allowed to the holiday")