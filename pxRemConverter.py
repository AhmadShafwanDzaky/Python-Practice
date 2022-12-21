while True:
    print("\nConvert selection.")
    print("1. pixels to rem")
    print("2. rem to pixels")
    choice = input("input your choice (1/2): ")
    if choice.isdigit():
        choice = int(choice)
    else:
        print("\nPlease enter a number.")
    if choice == 1:
        px = int(input("\ninput your pixels: "))
        convertRem = px/16
        print(f"Your conversion was successful, the result was: {convertRem}rem")
    elif choice == 2:
        rem = int(input("\ninput your rem: "))
        convertPx = rem*16
        print(f"Your conversion was successful, the result was: {convertPx}px")
    else:
        print("\nPlease enter 1/2.\n")
        continue
    while True:
        yn = input("\nWant to convert again? (y/n): ")
        if yn == "y":
            break
        elif yn == "n":
            exit()
        else:
            print("Please enter y/n.")