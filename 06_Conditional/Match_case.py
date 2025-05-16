a = int(input("Enter number between 1 to 10 "))

match a:
    case 3:
        print("You win a charger")
    case 5:
        print("You win a phone")
    case 9:
        print("You win a laptop")
    case _:
        print("Better luck,next time")