import random #import random module

#list for dice eyes
EYES_DICE = [
        "┌─────────┐\n"
        "│         │\n"
        "│    ●    │\n"
        "│         │\n"
        "└─────────┘",
        "┌─────────┐\n"
        "│  ●      │\n"
        "│         │\n"
        "│      ●  │\n"
        "└─────────┘",
        "┌─────────┐\n"
        "│  ●      │\n"
        "│    ●    │\n"
        "│      ●  │\n"
        "└─────────┘",
        "┌─────────┐\n"
        "│  ●   ●  │\n"
        "│         │\n"
        "│  ●   ●  │\n"
        "└─────────┘",
        "┌─────────┐\n"
        "│  ●   ●  │\n"
        "│    ●    │\n"
        "│  ●   ●  │\n"
        "└─────────┘",
        "┌─────────┐\n"
        "│  ●   ●  │\n"
        "│  ●   ●  │\n"
        "│  ●   ●  │\n"
        "└─────────┘",

        ]

#choice roll dice or no
yn = str(input("Roll dice? (yes/no)      => ").lower())
while True:
    if yn == "yes":    
        YOUR_DICE = [] # list to store your dice roll
        dices = input("How many dice to roll?   => ")
        if dices.isdigit(): #to check whether "dices" is a number or not
            dices = int(dices)
        else:
            print("Please input a number")
            continue

        for i in range(0, dices):
            dice1 = random.randint(1, 6) #random is using to get 1 random integer
            YOUR_DICE.append(dice1) #append to add random result to the list
            print(EYES_DICE[dice1-1]) #print the eye dice
        print("\nYour dices are: ", end='')
        for i in YOUR_DICE: #print results in integer format
            print(i, end= " ")
        
        while True:
            again = str(input("\nRoll again?? (yes/no) => "))
            if again == "yes":
                break #break to stop the loop
            elif again == "no":
                exit() #exit() to terminate the program
            else:
                print("Please enter yes/no!!")
    elif yn == "no":
        exit() #exit() is using to terminate the program
    else:
        print("Please enter yes/no!!")