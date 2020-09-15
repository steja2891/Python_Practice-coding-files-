#Mini challange 1  in list

computer_parts_list = []
print("Please choose the items from the list: ")
parts_list = ["1: Monitor",
              "2: Keyboard",
              "3: Wireless Mouse",
              "4: Speakers",
              "5: Mouse",
              "6: HDMI cable",
              "7: CPU",
              "8: Headset"]
print(parts_list)

while True:
    my_option = int(input("My choice is:"))
    if my_option == 1:
        print("Adding {} to the list".format("Monitor"))
        computer_parts_list.append("Monitor")
    elif my_option == 2:
        print("Adding {} to the list".format("Keyboard"))
        computer_parts_list.append("Keyboard")
    elif my_option == 3:
        print("Adding {} to the list".format("Wireless Mouse"))
        computer_parts_list.append("Wireless Mouse")
    elif my_option == 4:
        print("Adding {} to the list".format("Speakers"))
        computer_parts_list.append("Speakers")
    elif my_option == 5:
        print("Adding {} to the list".format("Mouse"))
        computer_parts_list.append("Mouse")
    elif my_option == 6:
        print("Adding {} to the list".format("HDMI cable"))
        computer_parts_list.append("HDMI cable")
    elif my_option == 7:
        print("Adding {} to the list".format("CPU"))
        computer_parts_list.append("CPU")
    elif my_option == 8:
        print("Adding {} to the list".format("Headset"))
        computer_parts_list.append("Headset")
    elif my_option == 0:
        print("Your Final selected items list is {}".format(computer_parts_list))
        print("Thank you for the purchase")
        break
    else:
        pass



