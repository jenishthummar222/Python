import random

menu = """ 

    STONE 
    PAPER
    SCISSOR

"""

game_list = ["STONE","PAPER","SCISSORS"]
status = True

computer_score,user_score = 0,0

while status:
    computer = random.choice(game_list)

    print(menu)

    user = input("Enter Your Choice :- ").upper()

    if computer == user:
        print("*************** Match DRAW ***************")
        
    elif computer == "STONE" and user == "PAPER" or computer == "PAPER" and user == "SCISSORS" or computer == "SCISSORS" and user == "STONE":
        
        print("*************** User Won ***************")
        user_score +=1
    else:
        print("*************** Computer Won ***************")
        computer_score +=1

    print(f" Computer Choice : {computer}   User Choice : {user}\n")
    
    select = input("Do You Continue.. [y/n] : ") 

    if select=='n':
        print("--------------------------------SCORE-------------------------------------")
        print(f"| Computer : {computer_score}                User : {user_score}         ")
        print("--------------------------------------------------------------------------")

        status = False




