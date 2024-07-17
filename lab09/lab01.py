# match

number = int(input("enter the number\n"))

match number:
    case 1:
        print("you have netered the 1")
    case 2:
        print("you have netered the 2")
    case _:
        print("no idea")

