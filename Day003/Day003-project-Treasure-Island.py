print("Welcome to Treasure Island.\nYour mission is to find the treaure.\n")
choice=input("Where you want to go? left or right?? ")
if choice.lower()=='right':
    print("You fall in hole.\nGame Over.")
elif choice.lower()=='left':
    choice=input("Enter your choice. swim or wait?? ")
    if choice.lower()=='swim':
        print("Boat sink.\nGame Over.")
    elif choice.lower()=='wait':
        choice=input("Which Door you want to go. Red Green Blue?? ")
        if choice.lower=='red' and choice.lower()=='blue':
            print("Fires in room.\nGame Over.")
        elif choice.lower()=='green':
            print("You found the treasure.\n YOU WIN GAME")
        else:
            print("Enter right")
    else:
        print("Enter right")
else:
    print("Enter right")