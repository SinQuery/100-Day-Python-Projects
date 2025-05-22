print("Welcome to Treaure Island.\nYour mission is to find the treasure.")
direction = input("Which direction would you like to head, left or right?\n")
direction = direction.lower()
if direction.lower() == "left":
    act = input("Would you like to swim to the next point, or wait?\n")
    if act.lower() == "wait":
        door = input("Which door would you like to use, Red, Yellow or Blue\n")
        if door.lower() == "yellow":
            print("\033[92mYou Win!\033[0m")
        elif door.lower() == "red":
            print("You have been burned by fire.\n\033[91mGAME OVER\033[0m")
        elif door.lower() == "blue":
            print("You have been eaten by beasts.\n\033[91mGAME OVER\033[0m")
        else: 
            print("\033[91mGAME OVER")
    else: 
        print("You've been attacked by trout.\n\033[91mGAME OVER!\033[0m")
else: 
    print("You have fallen into a hole.\n\033[91mGAME OVER!\033[0m")