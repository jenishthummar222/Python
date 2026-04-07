menu = """ 

        MENU
    
    press 1: Play game
    press 2: pause game
    press 3: exit game

"""

print(menu)

choice = int(input("Enter your choice : "))

match choice:
    case 1:
        print("Welcome to super mario game")
    case 2: 
        print("pause the game")
    case 3:
        print("Thank you for using game")
    case _:
        print("Invalid Input")
