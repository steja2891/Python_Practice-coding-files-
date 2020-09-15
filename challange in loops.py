# challange in loops

print("Please choose the option from the list below: ")
print('''1. Learn Python
2. Learn java
3. Go Swimming
4. Have Dinner
5. Go to Bed
6. Playing cricket
7. Watching Netflix
8. Reading Books
9. Meeting Friends
0. Exit''')

while True:
    option = int(input("Enter a number in the range 0 to 9: "))
    if option == 1:
        print("Learn Python Buddy..!!")
    elif option == 2:
        print("Learn Java ")
    elif option == 3:
        print("Go Swimming")
    elif option == 4:
        print("Have Dinner")
    elif option == 5:
        print("Go to Bed")
    elif option == 6:
        print("Playing cricket")
    elif option == 7:
        print("Watching Netflix")
    elif option == 8:
        print("Reading Books")
    elif option == 9:
        print("Meeting Friends")
    elif option == 0:
        print("You Quit the game...")
        break
    else:
        print("Please choose numbers from the menu buddy...!!")
        print('''1. Learn Python
2. Learn java
3. Go Swimming
4. Have Dinner
5. Go to Bed
6. Playing cricket
7. Watching Netflix
8. Reading Books
9. Meeting Friends
0. Exit''')

